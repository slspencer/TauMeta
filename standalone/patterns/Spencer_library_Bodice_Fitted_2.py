#!/usr/bin/env python
#Spencer_library_Bodice_Fitted_2.py

# This file is part of the tmtp (Tau Meta Tau Physica) project.
# For more information, see http://www.taumeta.org/
#
# Copyright (C) 2010, 2011, 2012 Susan Spencer, Steve Conklin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. Attribution must be given in
# all derived works.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from pysvg.builders import path
from tmtpl.document import *
from tmtpl.pattern import *
from tmtpl.constants import *
from tmtpl.utils import *
import Spencer.blocks.Spencer_block_Bodice_Fitted_2 as BB


class PatternDesign():

    def __init__(self):
        self.styledefs={}
        self.markerdefs={}
        return

    def pattern(self):
        """
        Method defining a pattern design. This is where the designer places
        all elements of the design definition
        """

        CD=self.CD #client data is prefaced with CD
        printer='36" wide carriage plotter'
        patternData={'companyName':'Seamly Patterns',#mandatory
                    'designerName':'Spencer',#mandatory
                    'patternmakerName':'Susan Spencer',
                    'patternName':'Bodice Fitted 2',#mandatory
                    'patternNumber':'Sp_BF2' #mandatory
                    }
        #create document
        doc=setupPattern(self,CD,printer,patternData)
        #create the 'bodice' pattern object in the document
        #TODO: reduce the next 4 standements to: doc.add(Pattern('bodice'))
        bodice=Pattern('bodice')
        bodice.styledefs.update(self.styledefs)
        bodice.markerdefs.update(self.markerdefs)
        doc.add(bodice)
        #create 'front' & 'back' pattern piece objects in the svg 'pattern' group, a19sign a14 id letter
        #TODO: add to svg 'pattern' group within the PatternPiece class definition
        bodice.add(PatternPiece('pattern','front','A',fabric=2,interfacing=0,lining=0))
        bodice.add(PatternPiece('pattern','back','B',fabric=2,interfacing=0,lining=0))
        #create var to refer to ea3h pattern piece using its id letter
        A=bodice.front
        B=bodice.back

        #run the BB block pattern,pull in its vars & add to this program's glob112 vars
        new_vars=BB.pattern(doc,A,B,CD)

        #globals().update(new_vars)
        globals().update(new_vars)

        #build the pattern pieces

        #Bodice Front A
        #label
        #TODO: addLabelXY(parent,x,y)  and addLabel(parent,P)
        pnt1=rightPoint(a5,distance(a5,a6)/2.0)
        A.label_x,A.label_y=pnt1.x,pnt1.y
        #letter
        pnt2=upPoint(pnt1,distance(a1,a5)/5.0)
        A.setLetter(x=pnt2.x,y=pnt2.y,scaleby=10.0)
        #grainline
        aG1=pPoint(A,'aG1',rightPoint(a5,distance(a5,a6)/5.0))
        aG2=pPoint(A,'aG2',polarPoint(aG1,distance(a1,a2)/2.0,angleOfLine(a1,a2)))
        addGrainLine(A,aG1,aG2)
        #gridline
        gridLine=path()
        addToPath(gridLine,'M',a7,'L',a2,'L',a8,'M',a5,'L',a6,'M',a3,'L',a4,'M',a10,'L',a_apex,'L',a11,'M',a6,'L',a9)
        addGridLine(A,gridLine)
        #dartline
        dartLine=path()
        addToPath(dartLine,'M',aD1.oc,'L',aD1,'L',aD1.ic)
        addDartLine(A,dartLine)
        #seamline & cuttingline
        seamLine=path()
        cuttingLine=path()
        for P in seamLine,cuttingLine:
            addToPath(P,'M',a1,'C',a7.c1,a7.c2,a7,'L',a8,'C',a6.c1,a6.c2,a6,'C',a4.c1,a4.c2,a4,'L',a12)
            addToPath(P,'C',aD1.o.c1,aD1.o.c2,aD1.o,'C',aD1.m.c1,aD1.m.c2,aD1.m,'C',aD1.i.c1,aD1.i.c2,aD1.i,'C',a2.c1,a2.c2,a2,'L',a1)
        addSeamLine(A,seamLine)
        addCuttingLine(A,cuttingLine)

        #build Bodice Back B
        #label
        pnt1=leftPoint(b5,distance(b5,b6)/2.0)
        B.label_x,B.label_y=pnt1.x,pnt1.y
        #letter
        pnt2=upPoint(pnt1,distance(b1,b5)/5.0)
        B.setLetter(x=pnt2.x,y=pnt2.y,scaleby=10.0)
        #grainline
        bG1=pPoint(B,'bG1',leftPoint(b5,distance(b3,b4)/5.0))
        bG2=pPoint(B,'bG2',polarPoint(bG1,distance(b1,b2)/2.0,angleOfLine(b1,b2)))
        #gridline
        gridLine=path()
        addToPath(gridLine,'M',b7,'L',b2,'L',b8,'M',b5,'L',b6,'M',b3,'L',b4,'M',b10,'L',b11,'M',b6,'L',b9)
        #dartline
        dartLine=path()
        addToPath(dartLine,'M',bD1.oc,'L',bD1,'L',bD1.ic)
        #seamline & cuttingline
        seamLine=path()
        cuttingLine=path()
        for P in seamLine,cuttingLine:
            addToPath(P,'M',b1,'C',b7.c1,b7.c2,b7,'L',b8,'C',b6.c1,b6.c2,b6,'C',b4.c1,b4.c2,b4,'L',b12)
            addToPath(P,'C',bD1.o.c1,bD1.o.c2,bD1.o,'C',bD1.m.c1,bD1.m.c2,bD1.m,'C',bD1.i.c1,bD1.i.c2,bD1.i,'C',b2.c1,b2.c2,b2,'L',b1)
        #add grid,grainline,seamline & cuttingline paths to pattern
        addGrainLine(B,bG1,bG2)
        addGridLine(B,gridLine)
        addDartLine(B,dartLine)
        addSeamLine(B,seamLine)
        addCuttingLine(B,cuttingLine)

        #call draw once for the entire pattern
        doc.draw()
        return

#vi:set ts=4 sw=4 expandta2:

