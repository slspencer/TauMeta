#!/usr/bin/python
#
# This file is part of the tmtp (Tau Meta Tau Physica) project.
# For more information, see http://www.taumeta.org/
#
# Copyright (C) 2010 - 2013 Susan Spencer and Steve Conklin
#
# This program is free software:you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version. Attribution must be given in
# all derived works.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see < http://www.gnu.org/licenses/ > .

import datetime
import math
import re
from math import sin, cos, sqrt, asin

import pysvg.builders as PYB

from document import *
from constants import *
from patternmath import *
from utils import debug


# -spc- this has to go once darts are reworked
def pPoint(parent, id, p1, transform=''):
    '''
    Creates an SVG red pattern point in group/layer 'reference',  id=p2.id,  stroke=none,  fill=red
    Accepts:
        parent of class patternPiece,
        id of type string,
        p1 of class Point or function which returns a Point,
        optional SVG transform phrase.
    Returns:
        p2 of class Point as child of parent,
        p2.x=p1.x+transform,
        p2.y=p1.y+transform,
        p2.name=id,
    Always assign to python variable of same name in pattern design file
        Examples:
            ac=pPoint(A, 'ac', downP(aa, 2*IN)) #ac is point on pattern piece A,  2inches below point aa
            bd=pPoint(B, 'bd', temp_point) #bd is point on pattern piece B,  same x & y values as variable temp_point
            cc=pPoint(C, 'cc', ba)#cc is point on pattern piece B,  same x & y values as ba
    The python variable assignment is required because they are used to write the SVG circles and paths to the XML Document at the doc.draw() command at the end of the pattern design file
    Paths are built as    'M', aa, 'L', ab, 'C', ac.c1, ac.c2, ac, 'L', aa   (no 'm', 'l', 'h', 'v', 'z' relative path or 'Q' quadratic curve commands)
    '''
    p2 = Point('reference', id, p1.x, p1.y, 'point_style', transform)
    parent.add(p2)
    return p2

# -spc- TODO This must go. Create another way to generate a circle
# also do away with special handling in the Point class which depends on
# finding 'circle' in the id
#def circle(parent, id, p1):
#    """creates an unfilled circle """
#    p2 = Point('reference', id+'_circle', p1.xy, 'circle_style', transform='', size=p1.size)
#    parent.add(p2)
#    p3 = Point('reference', id, p1.xy, 'point_style', transform='', size=5)
#    parent.add(p3)
#    return

def extractMarkerId(markertext):
    # Regex -
    # < marker id=\"grainline_mk\"\nviewBox=
    # one or more WS, followed by 'id' followed by zero or more WS followed by '=' followed by zero or more WS, followed by '"',
    m = re.search('(\s+id\s*=\s*\"\w+\")', markertext, re.I)
    mid = m.group(0).split('"')[1]
    return mid

# -spc- Notes for adding dart handling later, see also *dart methods in patternmath.py
#
#    def getDartPoints(parent, name, pnt):
#        #all darts have .o, .oc, .i, .ic, .m dynamic object attributes of class Pnt()
#        for attrib in 'i', 'ic', 'o', 'oc', 'm':
#            name1 = name + '.' + attrib #'aD1.i', 'aD1.ic', etc.
#            pnt1 = getattr(pnt, attrib)
#            pPoint(parent, name1, pnt1)
#            getControlPoints(parent, name1, pnt1) # find & create control points SVG objects,  if any
#        return

def getOutsetLine(p1, p2):
     '''
     Accepts points of line p1 & p2, and outset width.
     Returns outset line array [op1, op2]
     '''
    
     d  = p2.outset   
     angle1 = angleOfLine(p1, p2) - ANGLE90
     
     #outset each point by d
     op1 = polar(p1, d, angle1)
     op2 = polar(p2, d, angle1)
     
     return points2List(op1, op2)

def getOutsetCurve(curve):
     '''
     Accepts curve array [P1, C1, C2, P2] and outset width.
     Returns outset curve array [OP1, OC1, OC2, OP2]
     '''
     p1 = dPnt(curve[0])
     c1 = dPnt(curve[1])
     c2 = dPnt(curve[2])
     p2 = dPnt(curve[3])
     d = p2.outset
     
     angle1 = angleOfLine(p1, c1) - ANGLE90
     angle2 = angleOfLine(c1, c2) - ANGLE90
     angle3 = angleOfLine(c2, p2) - ANGLE90     

     #outset each leg of control polygon by d
     op1 = dPnt(polar(p1, d, angle1))
     oc1_a = dPnt(polar(c1, d, angle1))
     
     oc1_b = dPnt(polar(c1, d, angle2))
     oc2_a = dPnt(polar(c2, d, angle2))     

     oc2_b = dPnt(polar(c2, d, angle3))
     op2 = dPnt(polar(p2, d, angle3))     
     
     oc1 = dPnt(intersectLines(op1, oc1_a, oc1_b, oc2_a))
     oc2 = dPnt(intersectLines(oc1_b, oc2_a, oc2_b, op2))

     print '   getOutsetCurve()'
     print '      op1 ', op1.x, op1.y
     print '      oc1 ', oc1.x, oc1.y
     print '      oc2 ', oc2.x, oc2.y
     print '      op2 ', op2.x, op2.y               
     
     return points2List(op1, oc1, oc2, op2)
     
def createOutset(array):
    '''
    Accepts array of 'M', P1 [, ('L' , P2) | ('C', C1, C2, P2)]
    Returns outset_array of 'M', oP1 [, ('L' , oP2) | ('C', oC1, oC2, oP2)]
    '''
    c = array
    outset_array = []
    
    #Move c[0] is always 'M', add to outset_array
    outset_array.append(c[0])
    print '0', c[0]   
      
    i = 2
    while i < len(c):
        print '     '
        p1 = c[i - 1]  #previous point
        print '   ', (i - 1) , 'p1', p1.x, p1.y         
        action = c[i]
        print '   ', i, action
        
        p2 = c[i + 1]  #next point        
        print '   ', i + 1, 'p2', p2.x, p2.y        
                                                       
        # Line
        if action == 'L':
                     
            #get outset points
            L_array = getOutsetLine(p1, p2)
            op1 = dPnt(L_array[0])
            op2 = dPnt(L_array[1])
            print '   op1', op1.x, op1.y
            print '   op2', op2.x, op2.y
            
            #append outset points to outset array
            outset_array.append(op1)
            outset_array.append(action)
            outset_array.append(op2)
            
            i = i + 2
                      
        elif action == 'C':
           
            c1 = p1.outpoint
            print '   ', i, 'c1', c1.x, c1.y
            c2 = c[i + 1].inpoint
            print '   ', i + 1, 'c2', c2.x, c2.y            
            p2 = c[i + 1]
            print '   ', i + 1, 'p2', p2.x, p2.y            

            #get outset points
            C_array = getOutsetCurve(points2List(p1, c1, c2, p2))
            op1 = dPnt(C_array[0])
            oc1 = dPnt(C_array[1])
            oc2 = dPnt(C_array[2])
            op2 = dPnt(C_array[3])
            print '     op1', op1.x, op1.y
            print '     oc1', oc1.x, oc1.y
            print '     oc2', oc2.x, oc2.y
            print '     op2', op2.x, op2.y
            op1.addOutpoint(oc1)
            op2.addInpoint(oc2)                    
            
            #append outset points to outset array
            outset_array.append(op1)
            outset_array.append(action)
            outset_array.append(op2)
            
            i = i + 2
            
        else:
            print 'Action is invalid'
            
    return outset_array                     

def addToPath(p, tokens):
    """
    Accepts a path object and a string variable containing a pseudo svg path using M, L, C and point objects.
    Calls functions to add commands and points to the path object
    """
    i = 0
    while (i < len(tokens)):
        cmd = tokens[i]
        if (cmd == 'M'):
            pnt = tokens[i + 1]
            moveP(p, pnt)
            i = i + 2
        elif (cmd == 'L'):
            pnt = tokens[i + 1]
            lineP(p, pnt)
            i = i + 2
        elif (cmd == 'C'):
            # C uses the outpoint of the previous point and inpoint of the next point,
            # which are sub-points of those points
            if i < 2:
                raise ValueError("'C' path definition must be preceded by at least one point")
            pnt1 = tokens[i - 1]
            pnt2 = tokens[i + 1]
            try:
                outpoint = pnt1.outpoint
                inpoint = pnt2.inpoint
            except:
                print "Failure processing point", pnt2.name
                raise ValueError("'C' path definition must be followed by a point with outpoint and inpoint defined")
            i = i + 2
            cubicCurveP(p, outpoint, inpoint, pnt2)
        else:
            print 'Unknown command token ' + cmd
    return

def addToOutsetPath(p, tokens):
    """
    Accepts a path object and a string variable containing a pseudo svg path using M, L, C and point objects.
    Calls functions to add commands and points to the path object
    """
    i = 0
    while (i < len(tokens)):
        cmd = tokens[i]
        if (cmd == 'M'):
            pnt = tokens[i + 1]
            moveP(p, pnt)
            i = i + 2
        elif (cmd == 'L'):
            pnt = tokens[i + 1]
            lineP(p, pnt)
            i = i + 2
        elif (cmd == 'C'):
            # C uses the outpoint of the previous point and inpoint of the next point,
            # which are sub-points of those points
            if i < 2:
                raise ValueError("'C' path definition must be preceded by at least one point")
            pnt1 = tokens[i - 1]
            pnt2 = tokens[i + 1]
            try:
                outpoint = pnt1.outpoint
                inpoint = pnt2.inpoint
            except:
                print "Failure processing point", pnt2.name
                raise ValueError("'C' path definition must be followed by a point with outpoint and inpoint defined")
            i = i + 2
            cubicCurveP(p, outpoint, inpoint, pnt2)
        else:
            print 'Unknown command token ' + cmd
    return
# ---- Pattern Classes ----------------------------------------

class Point(pBase):
    """
    Creates instance of Python class Point
    """
    def __init__(self, group, name, xy, styledef='default', transform='', size=5) :

        self.groupname = group
        self.name = name
        self.sdef = styledef
        ipnt = dPnt(xy)
        self.x = ipnt.x
        self.y = ipnt.y
        self.attrs = {}
        self.txtstyle = 'point_text_style'
        self.attrs['transform'] = transform
        self.size = size
        self.coords = str(self.x) + ", " +str(self.y)
        pBase.__init__(self)

    @property
    def xy(self):
        return (self.x, self.y)

    def addInpoint(self, xy):
        """
        Add a control point as a child of this point. These control points are
        used for bezier curve drawing
        """
        pnt = Point('reference', 'inpoint', xy, 'controlpoint_style')
        pnt.txtstyle = 'control_point_text_style'
        self.add(pnt)
        return pnt

    def addOutpoint(self, xy):
        """
        Add a control point as a child of this point. These control points are
        used for bezier curve drawing
        """
        pnt = Point('reference', 'outpoint', xy, 'controlpoint_style')
        pnt.txtstyle = 'control_point_text_style'
        self.add(pnt)
        return pnt

    def getsvg(self):
        """
        generate the svg for a this point and return it as a pysvg object
        """
        if self.debug:
            print 'getsvg() called for Point ID ', self.id

        # call the baseclass svg method on this object. Returns a dictionary of all groups to be drawn.
        child_group_dict=pBase.getsvg(self)

        # an empty dict to hold our svg elements
        md=self.mkgroupdict()

        # build SVG info for this point
        pstyle = PYB.StyleBuilder(self.styledefs[self.sdef])
        p = PYB.circle(self.x, self.y, self.size)
        p.set_style(pstyle.getStyle())
        p.set_id(self.id)
        if 'tooltips' in self.cfg:
            p.set_onmouseover('ShowTooltip(evt)')
            p.set_onmouseout('HideTooltip(evt)')

        for attrname, attrvalue in self.attrs.items():
            p.setAttribute(attrname, attrvalue)

        md[self.groupname].append(p)

        txtlabel = self.id + '.text'
        # special handling for inpoints and outpoints
        if self.name == 'inpoint':
            txttxt = self.parent.name + '.in'
        elif self.name == 'outpoint':
            txttxt = self.parent.name + '.out'
        else:
            txttxt = self.name
        txt=self.generateText(self.x + 7, self.y - 7, txtlabel, txttxt, self.txtstyle)
        md[self.groupname].append(txt)

        # for each group used in this point
        for md_group_name, members in md.items():
            if md_group_name not in child_group_dict:
                # add the group is it's not already there
                child_group_dict[md_group_name] = []
            for member in members:
                child_group_dict[md_group_name].append(member)

        return child_group_dict

    def boundingBox(self, grouplist=None):
        """
        Return two points which define a bounding box around the object
        """
        # get all the children
        cxmin, cymin, cxmax, cymax = pBase.boundingBox(self, grouplist)
        #cxmin, cymin, cxmax, cymax = transformBoundingBox(xmin, ymin, xmax, ymax, self.attrs['transform'])

        if grouplist is None:
            grouplist = self.groups.keys()
        if self.groupname in grouplist:
            (x1, y1) = (self.x - (self.size / 2.0), self.y - (self.size / 2.0))
            (x2, y2) = (self.x + (self.size / 2.0), self.y + (self.size / 2.0))
            mxmin, mymin, mxmax, mymax, = x1, y1, x2, y2
        else:
            mxmin, mymin, mxmax, mymax = None, None, None, None

        tx1, ty1, tx2, ty2 = mergeBoundingBox(cxmin, cymin, cxmax, cymax, mxmin, mymin, mxmax, mymax)
        return transformBoundingBox(tx1, ty1, tx2, ty2, self.attrs['transform'])

class Line(pBase):
    """
    Creates instance of Python class Line
    """
    def __init__(self, group, name, label, xstart, ystart, xend, yend, styledef='default', transform='') :

        self.groupname = group
        self.name = name
        self.sdef = styledef
        self.label = label
        self.xstart = xstart
        self.ystart = ystart
        self.xend = xend
        self.yend = yend
        self.attrs = {}
        self.attrs['transform'] = transform
        # make some checks
        if self.sdef not in self.styledefs:
            raise ValueError("Style %s was specified but isn't defined" % self.sdef)
        pBase.__init__(self)

    def setMarker(self, markername=None, start=True, end=True):

        if markername not in self.markerdefs:
            raise ValueError("Marker %s was specified but isn't defined" % markername)
        else:
            # List it as used so we put it in the output file
            if markername not in self.markers:
                self.markers.append(markername)
            if type(self.markerdefs[markername]) is str:
                # This is a plain marker, not start, end or mid markers in a dict
                if start:
                    startMarkID = extractMarkerId(self.markerdefs[markername])
                    self.attrs['marker-start'] = "url(#%s)" % startMarkID
                if end:
                    endMarkID = extractMarkerId(self.markerdefs[markername])
                    self.attrs['marker-end'] = "url(#%s)" % endMarkID
            elif type(self.markerdefs[markername]) is dict:
                # Extract start and end as needed
                if start:
                    startMarkID = extractMarkerId(self.markerdefs[markername]['start'])
                    self.attrs['marker-start'] = "url(#%s)" % startMarkID
                if end:
                    endMarkID = extractMarkerId(self.markerdefs[markername]['end'])
                    self.attrs['marker-end'] = "url(#%s)" % endMarkID
            else:
                raise ValueError('marker %s is an unexpected type of marker' % markername)

    def add(self, obj):
        # Lines don't have children. If this changes, change the svg method also.
        raise RuntimeError('The Line class can not have children')

    def getsvg(self):
        """
        generate the svg for this item and return it as a pysvg object
        """
        if self.debug:
            print 'getsvg() called for Line ID ', self.id

        # an empty dict to hold our svg elements
        md = self.mkgroupdict()

        pstyle = PYB.StyleBuilder(self.styledefs[self.sdef])
        p = PYB.line(self.xstart, self.ystart, self.xend, self.yend)
        p.set_style(pstyle.getStyle())
        p.set_id(self.id)
        for attrname, attrvalue in self.attrs.items():
            p.setAttribute(attrname, attrvalue)
        md[self.groupname].append(p)

        return md

    def boundingBox(self, grouplist=None):
        """
        Return two points which define a bounding box around the object
        """
        if grouplist is None:
            grouplist = self.groups.keys()
        #if self.groupname in grouplist:
            #print '         end pattern.Line.boundingBox(', self.name, ')-returning (xmin:', min(self.xstart, self.xend), ' ymin:', min(self.ystart, self.yend) , ') ( xmax:', max(self.xstart, self.xend), ' ymax:', max(self.ystart, self.yend), ')'
            #return (min(self.xstart, self.xend), min(self.ystart, self.yend), max(self.xstart, self.xend), max(self.ystart, self.yend))
        #else:
            #print '         end pattern.Line.boundingBox(', self.name, ')-returning (None, None, None, None)'
            #return None, None, None, None
        if self.groupname in grouplist:
            dd = 'M ' + str(self.xstart) + ' ' + str(self.ystart) + ' L ' +str(self.xend) + ' ' + str(self.yend)
            xmin, ymin, xmax, ymax=getBoundingBox(dd)
            return xmin, ymin, xmax, ymax
        else:
            return None, None, None, None

class Path(pBase):
    """
    Creates instance of Python class Path
    Holds a path object and applies grouping, styles, etc when drawn
    """
    def __init__(self, group, name, label, pathSVG, styledef='default', transform='') :

        self.groupname = group
        self.name = name
        self.label = label
        self.sdef = styledef
        self.pathSVG = pathSVG
        self.attrs = {}
        self.attrs['transform'] = transform

        pBase.__init__(self)

    def setMarker(self, markername=None, start=True, end=True, mid=True):

        if markername not in self.markerdefs:
            print 'Markerdefs:', self.markerdefs
            raise ValueError("Marker %s was specified but isn't defined" % markername)
        else:
            # List it as used so we put it in the output file
            if markername not in self.markers:
                self.markers.append(markername)

            if type(self.markerdefs[markername]) is str:
                # This is a plain marker, not start, end or mid markers in a dict
                if start:
                    markID = extractMarkerId(self.markerdefs[markername])
                    self.attrs['marker-start'] = "url(#%s)" % markID
                if end:
                    markID = extractMarkerId(self.markerdefs[markername])
                    self.attrs['marker-end'] = "url(#%s)" % markID
                if mid:
                    markID = extractMarkerId(self.markerdefs[markername])
                    self.attrs['marker-mid'] = "url(#%s)" % markID
            elif type(self.markerdefs[markername]) is dict:
                # Extract start and end as needed
                if start:
                    markID = extractMarkerId(self.markerdefs[markername]['start'])
                    self.attrs['marker-start'] = "url(#%s)" % markID
                if end:
                    markID = extractMarkerId(self.markerdefs[markername]['end'])
                    self.attrs['marker-end'] = "url(#%s)" % markID
                if mid:
                    if 'mid' not in self.markerdefs[markername]:
                        # TODO Not sure whether this should be an exception,
                        # or just print a warning and not set mid markers
                        raise ValueError()
                    markID = extractMarkerId(self.markerdefs[markername]['mid'])
                    self.attrs['marker-mid']="url(#%s)" % markID
            else:
                raise ValueError('marker %s is an unexpected type of marker' % markername)

    def add(self, obj):
        # Paths don't have children. If this changes, change the svg method also.
        raise RuntimeError('The Path class can not have children')

    def getsvg(self):
        """
        generate the svg for this item and return it as a pysvg object
        """
        if self.debug:
            print 'getsvg() called for Line ID ', self.id

        try:
            # an empty dict to hold our svg elements
            md = self.mkgroupdict()

            pstyle = PYB.StyleBuilder(self.styledefs[self.sdef])

            self.pathSVG.set_id(self.id)
            self.pathSVG.set_style(pstyle.getStyle())
            for attrname, attrvalue in self.attrs.items():
                self.pathSVG.setAttribute(attrname, attrvalue)
            md[self.groupname].append(self.pathSVG)
        except:
            print '************************'
            print 'Exception in element', self.id
            print '************************'
            raise

        return md

    def boundingBox(self, grouplist=None):
        """
        Return two points which define a bounding box around the object
        """
        # This is not elegant, should perhaps be redone
        if grouplist is None:
            grouplist=self.groups.keys()
        if self.groupname in grouplist:
            dd = self.pathSVG.get_d()
            xmin, ymin, xmax, ymax=getBoundingBox(dd)
            return xmin, ymin, xmax, ymax
        else:
            return None, None, None, None

class TextBlock(pBase):
    """Creates instance of Python class TextBlock"""
    def __init__(self, group, name, headline, x, y, text, textstyledef='default_textblock_text_style', boxstyledef=None, transform=''):
        self.groupname = group
        self.name = name
        self.text = text
        self.textsdef = textstyledef
        self.boxsdef = boxstyledef
        self.headline = headline
        self.x = x
        self.y = y
        self.attrs = {}
        self.attrs['transform'] = transform

        pBase.__init__(self)

    def add(self, obj):
        # Text Blocks don't have children. If this changes, change the svg method also.
        raise RuntimeError('The TextBlock class can not have children')

    def getsvg(self):
        """
        generate the svg for this item and return it as a pysvg object
        """
        if self.debug:
            print 'getsvg() called for TextBlock ID ', self.id

        # an empty dict to hold our svg elements
        md = self.mkgroupdict()

        # create the text first
        tg = PYB.g()
        tg.set_id(self.id)
        x = self.x
        y = self.y

        if self.text is None:
            if self.debug:
                print '  TextBlock special case for pattern letter, getting text from parent'
            label = self.id+'.letterline'
            # TODO possibly check type of parent object to make sure it's a PatternPiece
            txt = self.generateText(x, y, label, self.parent.lettertext, self.textsdef)
            tg.addElement(txt)
        else:
            # this is a bit cheesy
            spacing = (int(self.styledefs[self.textsdef]['font-size']) * 1.2)
            line = 1
            for line in self.text:
                label = self.id + '.line' + str(line)
                txt = self.generateText(x, y, label, line, self.textsdef)
                y = y + spacing
                tg.addElement(txt)

        # if headline is None, then don't print it or space for it
        # if boxstyledef is none, then no box

        # TODO getting element sizes is note yet supported in pySVG,
        # so we'll do the outline box and headline later
        for attrname, attrvalue in self.attrs.items():
            tg.setAttribute(attrname, attrvalue)
        md[self.groupname].append(tg)

        return md
        
class Notch(pBase):
    """
    Creates instance of Python class Notch
    Draw notch in pattern group on pattern piece.
    All notches exist in pairs
    """
    def __init__(self, number, xstart, ystart, angle, transform='') :

        self.groupname = 'pattern'
        self.name = 'Notch' + number
        self.label = self.name
        self.sdef = 'notch_style'
        self.xstart = xstart
        self.ystart = ystart
        self.length = SEAM_ALLOWANCE
        self.angle = angle
        self.attrs = {}
        self.attrs['transform'] = transform
        self.xend = 0.0
        self.yend = 0.0
        
        # make some checks
        if self.sdef not in self.styledefs:
            raise ValueError("Style %s was specified but isn't defined" % self.sdef)
        pBase.__init__(self)

    def add(self, obj):
        # Lines don't have children. If this changes, change the svg method also.
        raise RuntimeError('The Line class can not have children')

    def getsvg(self):
        """
        generate the svg for this notch and return it as a pysvg object
        """
        if self.debug:
            print 'getsvg() called for Line ID ', self.id

        #create empty dict to hold svg elements for this notch object
        md = self.mkgroupdict()
        #create style dictionary
        pstyle = PYB.StyleBuilder(self.styledefs[self.sdef])
        #find end of notch line
        pnt = dPnt(polar(dPnt((self.xstart, self.ystart)), self.length, self.angle))
        self.xend, self.yend = pnt.x, pnt.y
        #create the svg line object as n
        n = PYB.line(self.xstart, self.ystart, self.xend, self.yend)
        n.set_style(pstyle.getStyle())
        n.set_id(self.id)
        #creat attribute list for n object 
        for attrname, attrvalue in self.attrs.items():
            n.setAttribute(attrname, attrvalue)
        #add n object to dictionary for patternpiece/groupname   
        md[self.groupname].append(n)
        #return dictionary object to <patternpiece>.Notch<number>.getsvg() call
        return md

    def boundingBox(self, grouplist=None):
        """
        Return two points which define a bounding box around the object
        """
        if grouplist is None:
            grouplist = self.groups.keys()
        #if self.groupname in grouplist:
            #print '         end pattern.Line.boundingBox(', self.name, ')-returning (xmin:', min(self.xstart, self.xend), ' ymin:', min(self.ystart, self.yend) , ') ( xmax:', max(self.xstart, self.xend), ' ymax:', max(self.ystart, self.yend), ')'
            #return (min(self.xstart, self.xend), min(self.ystart, self.yend), max(self.xstart, self.xend), max(self.ystart, self.yend))
        #else:
            #print '         end pattern.Line.boundingBox(', self.name, ')-returning (None, None, None, None)'
            #return None, None, None, None
        if self.groupname in grouplist:
            dd = 'M ' + str(self.xstart) + ' ' + str(self.ystart) + ' L ' +str(self.xend) + ' ' + str(self.yend)
            xmin, ymin, xmax, ymax=getBoundingBox(dd)
            return xmin, ymin, xmax, ymax
        else:
            return None, None, None, None

        

class PatternPiece(pBase):
    """
    Create an instance of the PatternPiece class, eg jacket.back, pants.frontPocket, corset.stayCover
    which will contain the set of seams and all other pattern piece info,
    eg-jacket.back.seam.shoulder, jacket.back.grainline, jacket.back.interfacing
    """
    def __init__(self, group, name, lettertext='?', fabricCnt=0, interfacingCnt=0, liningCnt=0):
        self.name = name
        self.groupname = group
        self.width = 0
        self.height = 0
        self.labelx = 0
        self.labely = 0
        self.lettertext = lettertext
        self.fabric = fabricCnt
        self.interfacing = interfacingCnt
        self.lining = liningCnt
        self.attrs = {}
        self.attrs['transform'] = ''
        pBase.__init__(self)

    def setLabelPosition(self, xy):
        p1 = dPnt(xy)
        self.labelx = p1.x
        self.labely = p1.y

    def addPoint(self, name, xy):
        pnt = Point('reference', name, xy, 'point_style')
        self.add(pnt)
        return pnt
       
    def addNotch(self, number, pnt, angle, transform=''):
        notch = Notch(number, pnt.x, pnt.y, angle, transform)
        self.add(notch)
        return notch     

    def addGrainLine(self, p1, p2, transform=''):
        p1 = dPnt(p1)
        p2 = dPnt(p2)
        #           group,     name,      label,                  xstart, ystart, xend, yend, styledef='default', transform='') :
        gline=Line("pattern", 'grainline', self.name + ' Grainline',  p1.x, p1.y, p2.x, p2.y, "grainline_style", transform)
        gline.setMarker('Arrow1M', start=True, end=True)
        self.add(gline)
        return gline

    def addGridLine(self, pathList):
        pth = PYB.path()
        addToPath(pth, pathList)
        newpth = Path('reference', 'gridline', self.name + ' Gridline', pth, 'gridline_style')
        self.add(newpth)
        return newpth

    def addSeamLine(self, pathList):
        pth = PYB.path()
        addToPath(pth, pathList)
        self.add(Path('pattern', 'seamline', self.name + ' Seamline', pth, 'seamline_style'))

    def addCuttingLine(self, pathList):
        pth = PYB.path()
        addToPath(pth, pathList)
        newpth = Path('pattern', 'cuttingline', self.name + ' Cuttingline', pth, 'cuttingline_style')
        self.add(newpth)
        return newpth

    def addMarkingLine(self, pathList):
        pth = PYB.path()
        addToPath(pth, pathList)
        newpth = Path('pattern', 'markingline', self.name + ' Markingline', pth, 'markingline_style')
        self.add(newpth)
        return newpth

    def addFoldLine(self, pathList):
        pth = PYB.path()
        addToPath(pth, pathList)
        newpth = Path('pattern', 'foldline', self.name + ' Foldline', pth, 'foldline_style')
        self.add(newpth)
        return newpth

    def addDartLine(self, pathList):
        pth = PYB.path()
        addToPath(pth, pathList)
        newpth = Path('pattern', 'dartline', self.name + ' Dartline', pth, 'dartline_style')
        self.add(newpth)
        return newpth

    def addCenterLine(self, pathList):
        pth = PYB.path()
        addToPath(pth, pathList)
        newpth = Path('pattern', 'centerline', self.name + ' CenterLine', pth, 'centerline_style')
        self.add(newpth)
        return newpth
        
    def addOutsetLine(self, pathList):
        pth = PYB.path()
        pth.extend(pathList)
        #addToPath(pth, pathList)
        newpth = Path('pattern', 'outsetline', self.name + ' OutsetLine', pth, 'cuttingline_style')
        self.add(newpth)
        return newpth        

    # TODO This may not be used, uncomment if used, delete if not
    #def addPatternLine(self, pathList):
    #    pth = PYB.path()
    #    addToPath(pth, pathList)
    #    self.add(Path('pattern', 'patternline', self.name + ' PatternLine', pth, 'dartline_style'))


    def getsvg(self):
        """
        generate the svg for this patternpiece and return it in a dictionary of groups which contain the svg objects
        """
        if self.debug:
            print 'getsvg() called for PatternPiece ID ', self.id

        # generate the label from information which is part of the pattern piece
        self.makeLabel()

        # call the baseclass svg method on this pattern piece. Returns a dictionary of all groups to be drawn.
        child_group_dict=pBase.getsvg(self)

        for child_group_name, members in child_group_dict.items():# for each group used in this pattern piece
            if self.debug:
                print 'self.id =', self.id, 'child_group_name =', child_group_name
                print '++ Group ==', child_group_name, ' in pattern.PatternPiece.getsvg()'

            # create a temporary pySVG group object
            temp_group = PYB.g()

            # assign temp group a unique id
            try:
                grpid = self.id + '.' + child_group_name
            except:
                print 'self.id =', self.id, 'child_group_name =', child_group_name, 'in pattern.PatternPiece.getsvg()'
            temp_group.set_id(grpid)

            # temp group gets all patternpiece's attributes
            for attrname, attrvalue in self.attrs.items():
                temp_group.setAttribute(attrname, attrvalue)
            # and all patternpiece's child elements
            for cgitem in child_group_dict[child_group_name]:
                temp_group.addElement(cgitem)

            # Add temp group to a temp list (list will have only one item)
            temp_group_list = []
            temp_group_list.append(temp_group)
            # Replace dictionary entry for this group with the temp list
            child_group_dict[child_group_name]=temp_group_list

        return child_group_dict

    def setLetter(self, xy=None, style='default_letter_text_style', text=None, scaleby=None):
        #TODO: Implement rotate transform
        if xy is None:
            x = None
            y = None
        else:
            x = xy[0]
            y = xy[1]
        # text=None is a flag to get the letter from the pattern piece at draw time
        if scaleby is not None:
            tform = scaleAboutPointTransform(x, y, scaleby)
        else:
            tform = ''
        tb=TextBlock('pattern', 'letter', None, x, y, text, textstyledef=style, transform=tform)
        self.add(tb)

    def makeLabel(self):
        """
        Create a label block for display on the pattern piece, which contains
        information like pattern number, designer name, logo, etc
        """
        text = []
        mi = self.cfg['metainfo']
        i = datetime.datetime.now()

        text.append(mi['companyName'])
        text.append(mi['patternNumber'])
        text.append(mi['patternTitle'])  
        text.append('Pattern Piece %s' % self.lettertext)
        if self.fabric > 0:
            text.append('Cut %d Fabric' % self.fabric)
        if self.lining > 0:
            text.append('Cut %d Lining' % self.lining)            
        if self.interfacing > 0:
            text.append('Cut %d Interfacing' % self.interfacing) 
        text.append(" ")                         
        text.append(self.cfg['clientdata'].customername)
        text.append("%s/%s/%s %s:%s" % (i.year, i.month, i.day, i.hour, i.minute))
        tb = TextBlock('pattern', 'info', 'Headline', self.labelx, self.labely, text, 'default_textblock_text_style', 'textblock_box_style')
        self.add(tb)

        return

    def boundingBox(self, grouplist=None):
        """
        Return two points which define a bounding box around the object
        """
        # get all the children
        xmin, ymin, xmax, ymax = pBase.boundingBox(self, grouplist)
        xmin, ymin, xmax, ymax = transformBoundingBox(xmin, ymin, xmax, ymax, self.attrs['transform'])

        return xmin, ymin, xmax, ymax

class Pattern(pBase):
    """
    Create an instance of Pattern class, eg-jacket, pants, corset, which will contain the set of pattern piece objects-eg  jacket.back, pants.frontPocket, corset.stayCover
    A pattern does not generate any svg itself, output is only generated by children objects
    """
    def __init__(self, name):
        self.name = name
        pBase.__init__(self)

    def addPiece(self, pieceName, pieceLetter, fabric = 0, interfacing = 0, lining = 0):
        self.add(PatternPiece('pattern', pieceName, pieceLetter, fabricCnt = fabric, interfacingCnt = interfacing, liningCnt = lining))
        return getattr(self, pieceName)

    def autolayout(self):
        """
        find out the bounding box for each pattern piece in this pattern, then make them fit within the
        width of the paper we're using
        """

        # get a collection of all the parts, we'll sort them before layout
        parts={}
        for chld in self.children:
            if isinstance(chld, PatternPiece):
                #print 'Pattern.py calling ', chld.name, '.boundingBox()'
                xlo, ylo, xhi, yhi = chld.boundingBox()
                #print 'Pattern.py -', chld.name, '.boundingBox() returned info[xlo]:', xlo, 'info[ylo]:', ylo, 'info[xhi]:', xhi, 'info[yhi]:', yhi
                parts[chld] = {}
                parts[chld]['xlo'] = xlo
                parts[chld]['ylo'] = ylo
                parts[chld]['xhi'] = xhi
                parts[chld]['yhi'] = yhi

        # our available paper width is reduced by twice the border
        #print self.cfg['paper_width']
        pg_width = self.cfg['paper_width'] - (2 * self.cfg['border'])
        if 'verbose' in self.cfg:
            print 'Autolayout:'
            print ' total paperwidth=', self.cfg['paper_width']
            print ' border width=', self.cfg['border']
            print ' available paperwidth=', pg_width
            print ' pattern outset=', PATTERN_OFFSET

        next_x = SEAM_ALLOWANCE
        # -spc- FIX Leave room for the title block!
        next_y = 6.0 * IN_TO_PT # this should be zero
        #next_y=0 # this should be zero
        max_height_this_row = 0
        # a very simple algorithm

        # we want to process these in alphabetical order of part letters
        index_by_letter = {}
        letters = []
        for pp, info in parts.items():
            letter = pp.lettertext
            if letter in index_by_letter:
                raise ValueError('The same Pattern Piece letter < %s >  is used on more than one pattern piece' % letter)
            index_by_letter[letter] = pp
            letters.append(letter)

        # sort the list
        letters.sort()

        for thisletter in letters:
            #print 'thisletter =', thisletter
            pp = index_by_letter[thisletter]
            #print 'pp=', pp
            info = parts[pp]
            pp_width = info['xhi'] - info['xlo']
            pp_height = info['yhi'] - info['ylo']

            if 'verbose' in self.cfg:
                print '   Part letter:', thisletter
                print '     part width=pp_width:', pp_width, ' < -- info[xhi]:', info['xhi'], '-info[xlo]:', info['xlo']
                print '     part height=pp_height:', pp_height, ' < -- info[yhi]:', info['yhi'], '-info[ylo]:', info['ylo']
                print '     current x=next_x:', next_x
                print '     current y=next_y:', next_y

            if pp_width > pg_width:
                print 'Error:Pattern piece < %s >  is too wide to print on page width' % pp.name
                # TODO:-figure out something smarter
                ## raise

            if next_x + pp_width > pg_width:
                # start a new row
                real_next_y = next_y + max_height_this_row + PATTERN_OFFSET
                if 'verbose' in self.cfg:
                    print '     Starting new row, right side of piece would have been=', next_x+pp_width
                    print '     New x=0'
                    print '     Previous y=next_y:', next_y
                    print '     New y=real_next_y:', real_next_y, ' < -- (next_y:', next_y, '+max_height_this_row:', max_height_this_row, '+PATTERN_OFFSET:', PATTERN_OFFSET, ')'
                    print '     New max_height_this_row=pp_height:', pp_height
                next_y = real_next_y
                max_height_this_row = pp_height
                #next_x = 0
                next_x = self.cfg['border']
            else:
                if pp_height > max_height_this_row:
                    max_height_this_row = pp_height
                    if 'verbose' in self.cfg:
                        print'       Previous y=next_y:', next_y
                        print'       New y=Previous y'
                        print'       New max_height_this_row=pp_height:', pp_height
            # now set up a transform to move this part to next_x, next_y
            xtrans = (next_x - info['xlo'])
            ytrans = (next_y - info['ylo'])
            pp.attrs['transform'] = pp.attrs['transform'] + (' translate(%f, %f)' % (xtrans, ytrans))
            if 'verbose' in self.cfg:
                print '     Transform=translate(xtrans:', xtrans, ', ytrans:', ytrans, ') < -- (next_x:', next_x, '- info[xlo]:', info['xlo'], '), next_y:', next_y, '- info[ylo]:', info['ylo'], ')'
                print '     New x is next_x:', next_x + pp_width + PATTERN_OFFSET, ' < --(next_x:', next_x, '+ppwidth:', pp_width, '+PATTERN_OFFSET:', PATTERN_OFFSET, ')'
            next_x = next_x + pp_width + PATTERN_OFFSET
        if 'verbose' in self.cfg:
            print 'Autolayout END'
        return

    def getsvg(self):
        # Automatically change pattern piece locations as needed
        self.autolayout()
        # Now call the base class method to assemble the SVG for all my children
        return pBase.getsvg(self)
