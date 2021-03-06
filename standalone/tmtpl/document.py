#!/usr/bin/python
# document.py
#
# This file is part of the Tau Meta Tau Physica project.
# For more information, see http://www.taumeta.org/
#
# Copyright (C) 2010, 2011, 2012 Susan Spencer and Steve Conklin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. Attribution must be given in
# all derived works.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import datetime
import json
import pysvg.builders as PYB

from constants import *
from patternbase import pBase

class Document(pBase):
    """
    This is the base container that everything else goes into. The svg is drawn by calling
    the draw() method on the document, which creates the svg document, then the groups
    within that and calls the getsvg() methods on each item to be drawn
    """
    def __init__(self, prog_cfg, name = 'UnnamedDocument', attributes = None):
        self.name = name
        self.id = name
        self.x = 0
        self.y = 0
        self.width = 8.5 * IN_TO_PT #starting document size
        self.height = 11.0 * IN_TO_PT #starting document size
        self.cfg.update(prog_cfg)
        self.filename = self.cfg['args'][0]
        self.attrs = attributes

        # if any print groups specified, aset up the internal list
        if 'print_groups' in self.cfg:
            self.displayed_groups = self.cfg['print_groups'].split(',')

        # if debug prints have been requested, enable them
        if self.cfg.has_key('debug'):
            debugstr = self.cfg['debug']
            if "prints" in debugstr:
                pBase.debug = True
                print "Debug: prints enabled"

        pBase.__init__(self)


    def draw(self):

        #TODO:place testgrid 1" to the right of the TitleBlock

        # the user may have specified on the command line to draw groups that
        # aren't present in the file. If not present, print a warning and remove those groups from the self.displayed_groups list.
        todelete = []
        for gpname in self.displayed_groups:
            if gpname not in self.groups:
                print 'Warning: Command line printgroups argument included group <%s> but that group is not in the pattern' % gpname
                todelete.append(gpname)
        for delgrp in todelete:
            self.displayed_groups.remove(delgrp)

        # any sanity checks on configuration before drawing go here
        if 'border' not in self.cfg:
            self.cfg['border'] = 2.54*CM_TO_PX

        # if there are no groups in the list of ones to draw, then default to all of them
        if len(self.displayed_groups) == 0:
            for groupname in self.groups:
                self.displayed_groups.append(groupname)

        # create the base pysvg object
        svg_base = PYB.svg()

        if 'tooltips' in self.cfg:
            # If --tooltips specified in mkpattern command line options
            # create pysvg script class object, add to svg_base object, & set script to initialize on document load
            svg_script = PYB.script()
            svg_script.set_xlink_href('tmtp_mouse.js')
            svg_script.set_xlink_type('text/ecmascript')
            svg_base.addElement(svg_script)
            svg_base.set_onload('init(evt)')

            # Add the tooltip text element. Start it hidden at upper left with 'ToolTip' as it's displayable string.
            ttel = self.generateText(0, 0, 'tooltip', 'ToolTip', 'tooltip_text_style')
            ttel.setAttribute('visibility', 'hidden')
            svg_base.addElement(ttel)

        # for some of the common information, make them attributes also
        meta_info = self.cfg['metainfo']
        for lbl in ['companyName', 'designerName', 'patternname', 'patternNumber']:
            if lbl in meta_info:
                self.attrs[lbl] = meta_info[lbl] # adds the self.cfg metainfo dictionary items to self.attrs so they will be written to the svg document.

        self.attrs['client-name'] = self.cfg['clientdata'].customername # Add customername to self.attrs so it can be written to the svg document.

        # Writes border values to the svg document, in case they were adjusted in self.cfg[] in the design
        self.attrs['margin-bottom'] = str(self.cfg['border'])
        self.attrs['margin-left'] = str(self.cfg['border'])
        self.attrs['margin-right'] = str(self.cfg['border'])
        self.attrs['margin-top'] = str(self.cfg['border'])

        # Add namespaces
        if 'noinkscape' not in self.cfg:
            self.attrs['xmlns:inkscape'] = 'http://www.inkscape.org/namespaces/inkscape'

        # Add attributes - TODO probably put these in a dictionary as
        # part of the document class
        if self.attrs:
            for attr, value in self.attrs.items():
                svg_base.setAttribute(attr, value)
        svg_base.setAttribute('xmlns:sodipodi', 'http://inkscape.sourceforge.net/DTD/sodipodi-0.dtd')

        # //svg:svg/sodipodi:namedspace/inkscape:document-units
        svg_base.appendTextContent("""<sodipodi:namedview
             id="base"
             pagecolor="#ffffff"
             bordercolor="#666666"
             borderopacity="1.0"
             inkscape:pageopacity="0.0"
             inkscape:pageshadow="2"
             inkscape:zoom="0.5"
             inkscape:document-units="pt"
             showgrid="false"
             inkscape:window-maximized="1" />\n""")

        # If any markers used, add marker definitions to the svg document so they can be referenced within the svg document
        # two types of markers -- plain is a string, dictionary has more than one marker
        # each marker has a start & end, with optional mid
        if len(self.markers):
            pdefs = PYB.defs() # Create pysvg builder defs class object
            for mname in self.markers:
                #print 'Adding marker %s' % mname
                if type(self.markerdefs[mname]) is str:
                    # this is just a plain marker, append it
                    pdefs.appendTextContent(self.markerdefs[mname]) # append marker def to pdfs[]
                elif type(self.markerdefs[mname]) is dict:
                    # contains a dict of marks
                    for submrk in self.markerdefs[mname]: # append each marker in the marker dictionary to pdefs[]
                        # always has start and end, may also have mid
                        pdefs.appendTextContent(self.markerdefs[mname][submrk])
                else:
                    print mname, 'marker is an unexpected type ***************'

            svg_base.addElement(pdefs) # write pdefs to pysvg base object

        # Recursively get everything to draw. svgdict[] will contain everything that will be written to the svg document.
        svgdict = self.getsvg()

        # Add/modify the transform so that the whole pattern piece originates at 0,0 and is offset by border
        xlo, ylo, xhi, yhi = self.boundingBox()
        xtrans = (-1.0 * xlo) + self.cfg['border']
        ytrans = (-1.0 * ylo) + self.cfg['border']
        fixuptransform = ('translate(%f,%f)' % (xtrans, ytrans))

        # -spc- TODO This is clearly wrong - it sizes the document to the pattern and ignores paper size
        xsize = (xhi - xlo) + (2.0 * self.cfg['border']) + SEAM_ALLOWANCE
        ysize = (yhi - ylo) + (2.0 * self.cfg['border']) + SEAM_ALLOWANCE
        svg_base.set_height(ysize)
        svg_base.set_width(xsize)
        #print 'document height = ', ysize
        #print 'document width = ', xsize

        for dictname, dictelements in svgdict.items():
            if self.debug:
                print 'processing group %s for output' % dictname
            if dictname not in self.displayed_groups:
                if self.debug:
                    print 'Group %s is not enabled for display' % dictname
                continue

            svg_group = PYB.g()
            self.groups[dictname] = svg_group
            # Set the ID to the group name
            svg_group.set_id(dictname)

            # set the transform in each group
            svg_group.setAttribute('transform', fixuptransform)
            if 'noinkscape' not in self.cfg:
                # add inkscape layer attributes
                svg_group.setAttribute('inkscape:groupmode', 'layer')
                svg_group.setAttribute('inkscape:label', ('Label-%s' % dictname))

            # Now add all the elements to it
            for svgel in dictelements:
                svg_group.addElement(svgel)

            # Now add the top level group to the document
            svg_base.addElement(svg_group)

        # Write out the svg file
        svg_base.save(self.filename)
        return

class TitleBlock(pBase):
    def __init__(self, group, name, x, y, stylename = ''):
        self.name = name
        self.groupname = group
        self.stylename = stylename
        self.x = x
        self.y = y
        pBase.__init__(self)
        return

    def add(self, obj):
        # Title Blocks don't have children. If this changes, change the svg method also.
        raise RuntimeError('The TitleBlock class can not have children')

    def getsvg(self):
        if self.debug:
            print 'getsvg() called for titleblock ID ', self.id

        # an empty dict to hold our svg elements
        svg_dict = self.mkgroupdict()

        # TODO make the text parts configurable
        svg_textgroup = PYB.g()
        svg_textgroup.set_id(self.id)
        # this is a bit cheesy
        text_space =  ( int(self.styledefs[self.stylename]['font-size']) * 1.1 )
        x = self.x
        y = self.y
        meta_info = self.cfg['metainfo']
        svg_textgroup.addElement(self.generateText(x, y, 'company', meta_info['companyName'], self.stylename))
        y = y + text_space
        svg_textgroup.addElement(self.generateText(x, y, 'designer', meta_info['designerName'], self.stylename))
        y = y + text_space
        svg_textgroup.addElement(self.generateText(x, y, 'pattern_number', meta_info['patternNumber'], self.stylename))
        y = y + text_space
        svg_textgroup.addElement(self.generateText(x, y, 'pattern_name', meta_info['patternTitle'], self.stylename))
        y = y + text_space
        svg_textgroup.addElement(self.generateText(x, y, 'client', self.cfg['clientdata'].customername, self.stylename))
        y = y + text_space
        i = datetime.datetime.now()
        svg_textgroup.addElement(self.generateText(x, y, 'date', "%s/%s/%s %s:%s" % (i.year, i.month, i.day, i.hour, i.minute), self.stylename))
        y = y + text_space

        svg_dict[self.groupname].append(svg_textgroup)
        return svg_dict

class TestGrid(pBase):
    def __init__(self, group, name, x, y, centimeters=6, inches=3, stylename = ''):
        self.centimeters = 6
        self.inches = 3
        self.name = name
        self.groupname = group
        self.stylename = stylename
        self.x = x
        self.y = y
        pBase.__init__(self)
        return

    def add(self, obj):
        # Test Grids don't have children. If this changes, change the svg method also.
        raise RuntimeError('The TestGrid class can not have children')

    def getsvg(self):
        if self.debug:
            print 'getsvg() called for TestGrid ID ', self.id

        # an empty dict to hold our svg elements
        svg_dict = self.mkgroupdict()

        # TODO make the text parts configurable
        svg_gridgroup = PYB.g()
        svg_gridgroup.set_id(self.id)

        """
        Creates two TestGrids at top of pattern --> 20cm & 8in
        """

        CMW = self.centimeters * CM_TO_PX
        INW = self.inches * IN_TO_PX
        svg_gridpath = PYB.path()

        gstyle = PYB.StyleBuilder(self.styledefs[self.stylename])
        svg_gridpath.set_style(gstyle.getStyle())
        svg_gridpath.set_id(self.name)
        #t.setAttribute('transform', trans)


        svg_gridgroup.addElement(svg_gridpath)

        #Points
        start_x, start_y = self.x, self.y
        startcm_x, startcm_y = start_x,  start_y
        startin_x, startin_y = start_x + CMW + 5*CM_TO_PX,  start_y
        #self.attrs['transform']='translate(' + str(-x)+', '+ str(-y) + ')'

        # centimeter grid
        i=0
        while (i <= self.centimeters): # vertical lines
            x = startcm_x + i*CM
            svg_gridpath.appendMoveToPath(x, startcm_y, relative=False)
            svg_gridpath.appendLineToPath(x, startcm_y + CMW, relative=False)
            i = i + 1
        i=0
        while (i <= self.centimeters): # horizontal lines
            y = startcm_y + i*CM
            svg_gridpath.appendMoveToPath(startcm_x, y, relative=False)
            svg_gridpath.appendLineToPath(startcm_x + CMW, y, relative=False)
            i = i + 1

        # inch grid
        i = 0
        while (i <= self.inches): #vertical
            x = startin_x + i*IN
            svg_gridpath.appendMoveToPath(x, startin_y, relative=False)
            svg_gridpath.appendLineToPath(x, startin_y + INW, relative=False)
            i = i + 1
        i = 0
        while (i <= self.inches): #horizontal
            y = startin_y + i*IN
            svg_gridpath.appendMoveToPath(startin_x, y, relative=False)
            svg_gridpath.appendLineToPath(startin_x + INW, y, relative=False)
            i = i + 1

        svg_dict[self.groupname].append(svg_gridgroup)
        return svg_dict
