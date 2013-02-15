# !/usr/bin/python
#
# allington_shirt_waist.py
# Inkscape extension-Effects-Sewing Patterns-Shirt Waist Allington
# Copyright (C) 2010,2011,2012 Susan Spencer,Steve Conklin <www.taumeta.org>

'''
Licensing paragraph:

1. CODE LICENSE: GPL 2.0+
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License,or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not,write to the Free Software
Foundation,Inc.,59 Temple Place,Suite 330,Boston,MA  02111-1307  USA

2. PATTERN LICENSE: CC BY-NC 3.0
The output of this code is a pattern and is considered a
visual artwork. The pattern is licensed under
Attribution-NonCommercial 3.0 (CC BY-NC 3.0)
<http://creativecommons.org/licenses/by-nc/3.0/>
Items made from the pattern may be sold;
the pattern may not be sold.

End of Licensing paragraph.
'''

from pprint import pprint
from pysvg.builders import path
from tmtpl.document import *
from tmtpl.pattern import *
from tmtpl.constants import *
from tmtpl.utils import *


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
        patternData={'companyName':'Sample Company',#mandatory
                    'designerName':'Sara May Allington',#mandatory
                    'patternmakerName':'Tau Meta Tau Physica',
                    'patternName':'Shirt Waist 1',#mandatory
                    'patternNumber':'AL_B1' #mandatory
                    }
        #create document
        doc=setupPattern(self,CD,printer,patternData)

        #create the 'bodice' pattern object in the document
        #TODO: reduce the next 4 statements to: doc.add(Pattern('bodice'))
        bodice=Pattern('bodice')
        bodice.styledefs.update(self.styledefs)
        bodice.markerdefs.update(self.markerdefs)
        doc.add(bodice)

        #create 'front' & 'back' pattern piece objects in the svg 'pattern' group, assign an id letter
        bodice.add(PatternPiece('pattern','front','A',fabric=2,interfacing=0,lining=0))
        bodice.add(PatternPiece('pattern','back','B',fabric=2,interfacing=0,lining=0))

        #refer to each pattern piece using a letter
        A=bodice.front
        B=bodice.back

        #pattern points
        b1=Pnt(0,0)
        b2=downPoint(b1, CD.front_waist_length)
        b3=upPoint(b2, CD.side)
        a1=leftPoint(b3, CD.bust_circumference/2.0)
        b4=leftPoint(b3,CD.across_back/2.0)
        b5=upPoint(b4,CD.armscye_circumference/3.0)
        b6=upPoint(b1, 0.5*IN)
        b7=leftPoint(b6,1.5*IN)
        b8=intersectLineAtLength(b5,b7, -0.5*IN)
        a2=leftPoint(b4, CD.armscye_circumference/4.0)
        a3=midPoint(a2,b4)
        a4=upPoint(a2, 2.5*IN)
        a5=upPoint(b5,1.5*IN)
        a6=leftPoint(a5,2*IN)
        length=distance(b7,b8)
        a7=leftPoint(a6,length)
        a8=Pnt(a7.x, b3.y-(CD.upper_front_height-distance(b1,b7)))
        a9=downPoint(a8, CD.neck_circumference/4.0)
        a10=upPoint(a9, 0.5*IN)
        a11=leftPoint(a10, (CD.neck_circumference/6.0)+0.25*IN )
        b9=midPoint(a3,b4)
        a12=PntP(b9)
        b10=downPoint(b9,CD.side)
        b11=rightPoint(b10,1*IN)
        a13=leftPoint(b10,1*IN)
        a14=intersectLineAtLength(a11, a1, CD.front_waist_length)
        a15=downPoint(a8,distance(a8,a14))
        b12=upPoint(b4,distance(b5, b4)/3.0)
        #armscye curve from a3 to b12
        length=distance(a3,b12)/3.0
        b12.c1=rightPoint(a3,length)
        b12.c2=downPoint(b12,length)
        #find intersection of side and armscye curve
        curve1=pointList(a3,b12.c1,b12.c2,b12)
        intersections=intersectLineCurve(b10,b9,curve1) #this line is directional from b10 to b9
        b13=intersections[0] #use the 1st intersection found - in this case there's only one intersection
        a16=PntP(b13)

        #back control points - path runs clockwise from nape b1
        #back neck control points from b7 to b1
        length=distance(b7,b1)/3.0
        b1.c1=downPoint(b7,length/2.0) #short control point handle
        b1.c2=leftPoint(b1,length*2) #long control point handle
        #back armscye control points from b13 to b12
        length=distance(b12,b13)/3.0
        pnt1=polarPoint(b13,length,angleOfLine(a3,a16))
        updatePoint(b12.c1,pnt1)
        pnt2=downPoint(b12,length)
        updatePoint(b12.c2,pnt2)
        #back armscye control points from b12 to b8
        length=distance(b12,b8)/3.0
        b8.c1=upPoint(b12,length)
        b8.c2=polarPoint(b8,length,angleOfLine(b8,b12))
        #back side control points from b11 to b9
        length1=distance(b11,b9)/3.0
        b9.c1=intersectLineAtLength(b11,b9,length1)
        b9.c2=downPoint(b9,length1)


        #front control points - path runs counterclockwise from front neck center a11
        #front neck control points from a8 to a11
        length=distance(a8,a11)/3.0
        a11.c2=rightPoint(a11,1.5*length)
        a11.c1=polarPoint(a8,length,angleOfLine(a8,a11.c2))
        #front waist control points from a14 to a15
        length=distance(a14,a15)/3.0
        a15.c1=polarPoint(a14,length,angleOfLine(a14,a11)+ANGLE90) #control handle line is perpendicular to line a14-a11
        a15.c2=leftPoint(a15,length)
        #front waist control points from a15 to a13
        length=distance(a15,a13)/3.0
        a13.c1=rightPoint(a15,1.5*length)
        a13.c2=polarPoint(a13,length,angleOfLine(a13,a13.c1)) #second control aimed at first control point
        #front armscye control points from a16 to a3 to a4 to 16
        length=distance(a16,a3)/3.0
        angle_a16a3=angleOfLine(a16,a3)
        angle12=(angleOfLine(a16,a3)+ANGLE180)/2.0
        angle11=angle12+ANGLE180
        a3.c1=polarPoint(a16,length,angle_a16a3)
        a3.c2=polarPoint(a3,length,angle11)
        length1=distance(a3,a4)/3.0
        length2=distance(a4,a6)/3.0
        angle_a6a4=angleOfLine(a6,a4)
        angle21=(ANGLE90+angle_a6a4)/2.0
        angle22=angle21+ANGLE180
        a4.c1=polarPoint(a3,length1,angle12)
        a4.c2=polarPoint(a4,1.5*length1,angle21)
        a6.c1=polarPoint(a4,length2,angle22)
        a6.c2=polarPoint(a6,length2,angle_a6a4)
        #front side control points from a13 to a12
        length=distance(a13,a12)/3.0
        a12.c1=intersectLineAtLength(a13,a12,length)
        a12.c2=downPoint(a12,length)

        #all points are defined, now create marks,labels,grainlines,seamlines,cuttinglines,darts,etc.
        #bodice front A
        #draw points
        drawPoints(A,locals())
        #label
        #TODO: addLabel(parent,x,y)  and addLabelP(parent,P)
        pnt1=downPoint(a8,distance(a8,a15)/3.0)
        A.label_x,A.label_y=pnt1.x,pnt1.y
        #letter
        pnt2=upPoint(pnt1,0.5*IN)
        A.setLetter(x=pnt2.x,y=pnt2.y,scaleby=10.0)
        #grainline
        aG1=downPoint(a11,CD.front_waist_length/3.0)
        aG2=downPoint(aG1,CD.front_waist_length/2.0)
        addGrainLine(A,aG1,aG2)
        # gridline
        # this grid is helpful to troubleshoot during design phase
        gridLine=path()
        addToPath(gridLine,'M',a1,'L',a3,'M',a4,'L',a2,'M',a8,'L',a15,'M',a11,'L',a10,'M',a7,'L',a5)
        addGridLine(A,gridLine)
        #seamline & cuttingline
        seamLine=path()
        cuttingLine=path()
        for P in seamLine,cuttingLine:
            addToPath(P,'M',a11,'L',a14,'C',a15.c1,a15.c2,a15,'C',a13.c1,a13.c2,a13,'C',a12.c1,a12.c2,a12)
            addToPath(P,'L',a16,'C',a3.c1,a3.c2,a3,'C',a4.c1,a4.c2,a4,'C',a6.c1,a6.c2,a6,'L',a8,'C',a11.c1,a11.c2,a11)
        addSeamLine(A,seamLine)
        addCuttingLine(A,cuttingLine)

        #bodice back B
        #draw svg points
        drawPoints(B,locals())
        #label
        pnt1=downPoint(midPoint(b7,b8),distance(b1,b2)/4.0)
        B.label_x,B.label_y=pnt1.x,pnt1.y
        #letter
        pnt2=upPoint(pnt1,0.5*IN)
        B.setLetter(x=pnt2.x,y=pnt2.y,scaleby=10.0)
        #grainline X
        bG1=downPoint(b7,CD.back_waist_length/3.0)
        bG2=downPoint(bG1,CD.back_waist_length/2.0)
        addGrainLine(B,bG1,bG2)
        # gridline X
        gridLine=path()
        addToPath(gridLine,'M',a5,'L',b4,'M',b3,'L',b9,'M',b9,'L',b10,'M',b7,'L',b6,'L',b1,'M',b11,'L',b10)
        addGridLine(B,gridLine)
        #seamline & cuttingline X
        seamLine=path()
        cuttingLine=path()
        for P in seamLine,cuttingLine:
            addToPath(P,'M',b1,'L',b2,'L',b11,'C',b9.c1,b9.c2,b9,'L',b13,'C',b12.c1,b12.c2,b12,'C',b8.c1,b8.c2,b8,'L',b7,'C',b1.c1,b1.c2,b1)
        addSeamLine(B,seamLine)
        addCuttingLine(B,cuttingLine)


        #call doc.draw() to generate svg file

        doc.draw()
        return

