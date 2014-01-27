#!/usr/bin/python
#
# This file is part of the Tau Meta Tau Physica project.
# For more information, see http://www.taumeta.org/
#
# Copyright (C) 2010 - 2013  Susan Spencer and Steve Conklin
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>..

#from pysvg.builders import path
#from tmtpl.designbase import *
from tmtpl.document import *
from tmtpl.pattern import *
from tmtpl.constants import *
#from tmtpl.utils import *


class designBase(object):
    """
    Base class for the tmtp design file
    """

    def __init__(self, ClientData, styledefs, markerdefs, config):
        self.styledefs = styledefs
        self.markerdefs = markerdefs
        self.cfg = config
        self.cfg['metainfo'] = {}
        # -spc- TODO, do we really need both of these?
        self.cfg['clientdata'] = ClientData
        # TODO printer stuff needs work
        #self.printer = '36" wide carriage plotter'
        self.printer = '44" wide carriage plotter'
        #self.cfg['paper_width'] = 36.0 * IN
        self.cfg['paper_width'] = 44.0 * IN
        self.cfg['border'] = 2.5 * CM

        # create the document into which all objects go
        docattrs = {
            'currentscale': "0.5:1",
            'fitBoxtoViewport': "True",
            'preserveAspectRatio': "xMidYMid meet",
            }
        # TODO review this, and perhaps put them in different groups than 'notes'
        # adn make grid optional
        self.doc = Document(self.cfg, name='document', attributes=docattrs)
        self.doc.add(TitleBlock('notes', 'titleblock', 0.0, 0.0, stylename='titleblock_text_style'))
        self.doc.add(TestGrid('notes', 'testgrid', self.cfg['paper_width'] / 3.0, 0.0, stylename='cuttingline_style'))


    # ClientData is the name and measurements to draw the pattern for
    #
    @property
    def CD(self):
        return self.cfg['clientdata']
    @CD.setter
    def CD(self, value):
        self.cfg['clientdata'] = value

    # Meta info, which is typically printed on each pattern sheet
    #
    def setInfo(self, name, value):
        self.cfg['metainfo'][name] = value

    def addPattern(self, pname):
        pat = Pattern(pname)
        pat.styledefs.update(self.styledefs)
        pat.markerdefs.update(self.markerdefs)
        self.doc.add(pat)
        return pat

    def draw(self):
        self.doc.draw()
