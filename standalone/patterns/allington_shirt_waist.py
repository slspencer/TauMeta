# !/usr/bin/python
#
# allington_shirt_waist.py
# Inkscape extension - Effects - Sewing Patterns - Shirt Waist Allington
# Copyright (C) 2010, 2011, 2012 Susan Spencer, Steve Conklin <www.taumeta.org>

'''
Licensing paragraph :

1. CODE LICENSE :  GPL 2.0 +
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111 - 1307  USA

2. PATTERN LICENSE :  CC BY - NC 3.0
The output of this code is a pattern and is considered a
visual artwork. The pattern is licensed under
Attribution - NonCommercial 3.0 (CC BY - NC 3.0)
<http : //creativecommons.org/licenses/by - nc/3.0/>
Items made from the pattern may be sold;
the pattern may not be sold.

End of Licensing paragraph.
'''

from pysvg.builders import path
from tmtpl.document import *
from tmtpl.pattern import *
from tmtpl.constants import *
from tmtpl.utils import *


class PatternDesign() :

    def __init__(self) :
        self.styledefs = {}
        self.markerdefs = {}
        self.printer = '36" wide carriage plotter'
        self.patternData = {
            'patternNumber' : 'AL_B1',  # Mandatory
            'patternTitle' : 'Allington Shirt Waist 1',  # Mandatory
            'description' : """
This is a test pattern for Seamly Patterns.
It was taken from Sara May Allington's 'Dressmaking',  1917.
""",  # Mandatory (paragraph)
            'category' : 'Shirt/TShirt/Blouse',  # Mandatory
            'type' : 'Historical',  # Mandatory
            'gender' : 'F',  # Optional 'M',  'F',  or ''
            'yearstart' : 1910,  # Optional
            'yearend' : 1920,  # Optional
            'culture' : 'European',  # Optional
            'wearer' : '',  # Optional
            'source' : '',  # Optional
            'characterName' : '',  # Optional
            'recommendedFabric' : '',
            'recommendedNotions' : '',
            'companyName' : 'Seamly Patterns',  # Mandatory
            'designerName' : 'Sara May Allington',  # Mandatory
            'patternmakerName' : 'S.L.Spencer',  # Mandatory
            }
        return

    def pattern(self) :
        """
        Method defining a pattern design. This is where the designer places
        all elements of the design definition
        """
        CD = self.CD #client data is prefaced with CD

        #create document
        doc = setupPattern(self, CD, self.printer, self.patternData)

        #create the 'bodice' pattern object in the document
        #TODO :  reduce the next 4 statements to  doc.add(Pattern('bodice'))
        bodice = Pattern('bodice')
        bodice.styledefs.update(self.styledefs)
        bodice.markerdefs.update(self.markerdefs)
        doc.add(bodice)

        #create 'front' & 'back' pattern piece objects in the svg 'pattern' group,  assign an id letter
        bodice.add(PatternPiece('pattern', 'front', 'A', fabric = 2, interfacing = 0, lining = 0))
        bodice.add(PatternPiece('pattern', 'back', 'B', fabric = 2, interfacing = 0, lining = 0))
        bodice.add(PatternPiece('pattern', 'sleeve', 'C', fabric = 2, interfacing = 0, lining = 0))
        bodice.add(PatternPiece('pattern', 'cuff', 'D', fabric = 2, interfacing = 0, lining = 0))

        #refer to each pattern piece using a letter
        A = bodice.front
        B = bodice.back
        C = bodice.sleeve
        D = bodice.cuff

        #pattern points
        b1 = Pnt(0, 0) #B
        b2 = down(b1, CD.front_waist_length) #A
        b3 = up(b2, CD.side) #C
        a1 = left(b3, CD.bust/2.0) #D
        b4 = left(b3, CD.back_armfold_distance/2.0) #E
        b5 = up(b4, CD.arm_scye/3.0) #F
        b6 = up(b1, 0.5*IN) #G
        b7 = left(b6, 1.5*IN) #H
        b8 = onLineAtLength(b5, b7, -0.5*IN) #I
        a2 = left(b4, CD.arm_scye/4.0) #J
        a3 = midPoint(a2, b4) #K
        a4 = up(a2, 2.5*IN) #L
        a5 = up(b5, 1.5*IN) #M
        a6 = left(a5, 2*IN) #N
        a7 = left(a6, distance(b7, b8)) #O
        a8 = Pnt(a7.x, b3.y - (CD.bust_balance - distance(b1, b7))) #P
        a9 = down(a8, CD.neck/4.0) #Q
        a10 = up(a9, 0.5*IN) #R
        a11 = left(a10, (CD.neck/6.0) + 0.25*IN) #S
        b9 = midPoint(a3, b4) #T on back bodice B
        a12 = Pnt(b9.x, b9.y) #T on front bodice A
        b10 = down(b9, CD.side) #U
        b11 = right(b10, 1*IN) #V
        a13 = left(b10, 1*IN) #W
        a14 = onLineAtLength(a11, a1, CD.front_waist_length) #X
        a15 = down(a8, distance(a8, a14)) #Y - new point at front waist
        b12 = up(b4, distance(b5, b4)/3.0) #Z - new point at back armscye
        #temporary armscye curve from a3 to b12 to find top point of side seam
        length = distance(a3, b12)/3.0
        temp_b12_c1 = right(a3, length) #don't create an svg controlpoint circle for this point
        temp_b12_c2 = down(b12, length) #or for this point
        #find top point of side seam with intersection of side and armscye curve, save to two points a16 and b13
        curve1 = pointList(a3, temp_b12_c1, temp_b12_c2, b12)
        intersections = intersectLineCurve(b10, b9, curve1) #this line is directional from b10 to b9
        b13 = Pnt(intersections[0].x, intersections[0].y) # AA on bodice back B -use 1st intersection found, in this case there's only one intersection
        a16 = Pnt(b13.x, b13.y) #AA on bodice back A

        #front control points - path runs counterclockwise from front neck center a11
        #front neck control points from a8 to a11
        length = distance(a8, a11)/3.0
        a11.c2 = right(a11, 1.5*length)
        a11.c1 = polar(a8, length, angleOfLine(a8, a11.c2))
        #front waist control points from a14 to a15
        length = distance(a14, a15)/3.0
        a15.c1 = polar(a14, length, angleOfLine(a14, a11) + ANGLE90) #control handle line is perpendicular to line a14-a11
        a15.c2 = left(a15, length)
        #front waist control points from a15 to a13
        length = distance(a15, a13)/3.0
        a13.c1 = right(a15, 1.5*length)
        a13.c2 = polar(a13, length, angleOfLine(a13, a13.c1)) #second control aimed at first control point
        #front side control points from a13 to a12
        length = distance(a13, a12)/3.0
        a12.c1 = up(a13, length)
        a12.c2 = down(a12, length)
        #front armscye control points from a16 to a3 to a4 to 16
        length1 = distance(a16, a3)/3.0
        length2 = distance(a3, a4)/3.0
        length3 = distance(a4, a6)/3.0
        angle1 = angleOfLine(a16, a3)
        angle2 = ANGLE180
        angle3 = (angle1 + angle2)/2.0
        a3.c1 = polar(a16, length1, angle1)
        a3.c2 = polar(a3, length1, angle3 - ANGLE180)
        a4.c1 = polar(a3, length2, angle3)
        angle4 = angleOfLine(a3, a6)
        angle5 = angleOfLine(a4, a6)
        angle6 = (angle4 + angle5)/2.0
        a4.c2 = polar(a4, 1.5*length2, angle6 - ANGLE180)
        a6.c1 = polar(a4, length3, angle6)
        a6.c2 = polar(a6, length3/2.0, angleOfLine(a8, a6) + ANGLE90)

        #back control points - path runs clockwise from back nape b1
        #back neck control points from b7 to b1
        length = distance(b7, b1)/3.0
        b1.c1 = down(b7, length/2.0) #short control point handle
        b1.c2 = left(b1, length*2) #long control point handle
        #back side control points from b11 to b9
        length = distance(b11, b9)/3.0
        b9.c1 = up(b11, length)
        b9.c2 = down(b9, length)
        #back armscye points from b13 to b12 to b8
        length1 = distance(b13, b12)/3.0
        length2 = distance(b12, b8)/3.0
        angle1 = angleOfLine(b13, b8)
        b12.c1 = polar(b13, length1, angleOfLine(a3.c1, a16))
        b12.c2 = polar(b12, length1, angle1 - ANGLE180)
        b8.c1 = polar(b12, length2, angle1)
        b8.c2 = polar(b8, length2/2.0, angleOfLine(b7, b8) - ANGLE90)

        #sleeve C
        c1 = Pnt(0, 0) #A
        c2 = down(c1, CD.oversleeve_length) #B
        c3 = up(c2, CD.elbow_length) #C
        c4 = right(c2, 1*IN) #D
        c5 = right(c3, 0.5*IN) #E
        c6 = left(c1, 1*IN) #F
        c7 = right(c4, 1*IN) #G
        c8 = right(c7, CD.hand + 2*IN) #H
        c9 = right(c8, 1*IN) #I
        c10 = right(c5, 1*IN) #J
        c11 = right(c10, CD.elbow) #K
        c12 = right(c11, 0.5*IN) #L
        c13 = right(c1, CD.arm_scye) #M
        c14 = right(c13, 2*IN) #N
        c15 = up(c1, 2.5*IN) #O
        c16 = right(c1, 1.5*IN) #P
        c17 = left(c13, 3*IN) #Q
        c18 = Pnt(c16.x, c15.y) #R
        c19 = Pnt(c17.x, c15.y) #S
        c20 = midPoint(c16, c17) #T
        c21 = up(c20, distance(c20, c18)) #U - above T
        c22 = down(midPoint(c7, c8), 0.75*IN) #V - was U
        c23 = right(c4, distance(c4, c8)*3/5.0) #W
        c24 = up(c23, distance(c4, c3)/3.0) #X - was V
        c25 = down(c23, 0.75*IN) #Y - new point
        # sleeve C control points
        # sleevecap c6 to c18 to c21 to c19 to c13 to c14
        length1 = distance(c6, c18)/3.0
        length2 = distance(c18, c21)/3.0
        c21.c2 = left(c21, length2)
        c21.c1 = polar(c18, length2, angleOfLine(c18, c21.c2))
        angle = angleOfLine(c6, c18) + angleOfVector(c18, c6, c1)/2.0
        c18.c1 = polar(c6, length1, angle)
        c18.c2 = polar(c18, length1, angleOfLine(c21.c1, c18))
        length1 = distance(c21, c19)/3.0
        length2 = distance(c19, c13)/3.0
        length3 = distance(c13, c14)/3.0
        c19.c1 = right(c21, length1)
        c19.c2 = polar(c19, length1, angleOfLine(c19, c19.c1))
        c13.c1 = polar(c19, length2, angleOfLine(c19.c2, c19))
        angle1 = angleOfLine(c13.c1, c13)/2.0
        c13.c2 = polar(c13, length2, angle1 + ANGLE180)
        c14.c1 = polar(c13, length3, angle1)
        c14.c2 = polar(c14, length3, angleOfLine(c18.c1, c6))
        # c14 to c12
        length = distance(c14, c12)/3.0
        c12.c2 = polar(c12, length, angleOfLine(c9, c12))
        c12.c1 = polar(c14, length, angleOfLine(c14, c12.c2))
        # c9 to c25
        length = distance(c9, c25)/3.0
        c25.c2 = right(c25, length)
        c25.c1 = polar(c9, length, angleOfLine(c9, c25.c2))
        #c22 to c4
        length = distance(c22, c4)/3.0
        c4.c1 = left(c22, length)
        c4.c2 = polar(c4, length, angleOfLine(c4, c4.c1))
        #c5 to c6
        length = distance(c5, c6)/3.0
        c6.c1 = polar(c5, length, angleOfLine(c4, c5))
        c6.c2 = polar(c6, length, angleOfLine(c6, c6.c1))

        #cuff D
        d1 = Pnt(0, 0)
        d2 = right(d1, CD.hand + 2*IN)
        d3 = down(d2, 3*IN)
        d4 = up(d3, 0.75*IN)
        d5 = left(d3, 1*IN)
        d6 = down(d1, 3*IN)
        d7 = right(d6, 1*IN)
        d8 = up(d6, 0.75*IN)
        length1 = 0.7*distance(d1, d6)
        length2 = 0.75*IN
        d9 = Pnt(d1.x + 0.5*IN, d1.y + length1)
        d10 = right(d9, length2)
        d11 = Pnt(d2.x - 0.5*IN, d2.y + length1)
        d12 = left(d11, length2)
        #cuff D control points
        length = distance(d4, d5)/3.0
        d5.c1 = down(d4, length)
        d5.c2 = right(d5, length)
        d8.c1 = left(d7, length)
        d8.c2 = down(d8, length)

        #all points are defined,  now create marks, labels, grainlines, seamlines, cuttinglines, darts, etc.

        #bodice front A
        #draw points
        drawPoints(A, locals())
        #label
        #TODO :  addLabel(parent, x, y)  and addLabelP(parent, P)
        pnt1 = down(a8, distance(a8, a15)/3.0)
        A.label_x, A.label_y = pnt1.x, pnt1.y
        #letter
        pnt2 = up(pnt1, 0.5*IN)
        A.setLetter(x = pnt2.x, y = pnt2.y, scaleby = 10.0)
        #grainline
        aG1 = down(a11, CD.front_waist_length/3.0)
        aG2 = down(aG1, CD.front_waist_length/2.0)
        addGrainLine(A, aG1, aG2)
        # gridline
        # this grid is helpful to troubleshoot during design phase
        gridLine = path()
        addToPath(gridLine, 'M', a1, 'L', a3, 'M', a4, 'L', a2, 'M', a8, 'L', a15, 'M', a11, 'L', a10, 'M', a7, 'L', a5)
        addGridLine(A, gridLine)
        #seamline & cuttingline
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine :
            addToPath(P, 'M', a11, 'L', a14, 'C', a15.c1, a15.c2, a15, 'C', a13.c1, a13.c2, a13, 'C', a12.c1, a12.c2, a12)
            addToPath(P, 'L', a16, 'C', a3.c1, a3.c2, a3, 'C', a4.c1, a4.c2, a4, 'C', a6.c1, a6.c2, a6, 'L', a8, 'C', a11.c1, a11.c2, a11)
        addSeamLine(A, seamLine)
        addCuttingLine(A, cuttingLine)

        #bodice back B
        #draw svg points
        drawPoints(B, locals())
        #label
        pnt1 = down(midPoint(b7, b8), distance(b1, b2)/4.0)
        B.label_x, B.label_y = pnt1.x, pnt1.y
        #letter
        pnt2 = up(pnt1, 0.5*IN)
        B.setLetter(x = pnt2.x, y = pnt2.y, scaleby = 10.0)
        #grainline X
        bG1 = down(b7, CD.back_waist_length/3.0)
        bG2 = down(bG1, CD.back_waist_length/2.0)
        addGrainLine(B, bG1, bG2)
        # gridline X
        gridLine = path()
        addToPath(gridLine, 'M', a5, 'L', b4, 'M', b3, 'L', b9, 'M', b9, 'L', b10, 'M', b7, 'L', b6, 'L', b1, 'M', b11, 'L', b10)
        addGridLine(B, gridLine)
        #seamline & cuttingline X
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine :
            addToPath(P, 'M', b1, 'L', b2, 'L', b11, 'C', b9.c1, b9.c2, b9, 'L', b13, 'C', b12.c1, b12.c2, b12, 'C', b8.c1, b8.c2, b8, 'L', b7, 'C', b1.c1, b1.c2, b1)
        addSeamLine(B, seamLine)
        addCuttingLine(B, cuttingLine)

        #bodice sleeve C
        drawPoints(C, locals())
        #label
        pnt1 = Pnt(c19.c1.x, c12.c1.y)
        C.label_x,  C.label_y = pnt1.x, pnt1.y
        #letter
        pnt2 = down(pnt1, 0.5*IN)
        C.setLetter(x = pnt2.x, y = pnt2.y)
        #grainline points
        cG1 = Pnt(c20.x,  c20.y)
        cG2 = down(cG1, CD.oversleeve_length/2.0)
        addGrainLine(C, cG1, cG2)
        # gridline
        gridLine = path()
        addToPath(gridLine, 'M', c15, 'L', c2, 'M', c15, 'L', c19, 'M', c2, 'L', c9, 'M', c3, 'L', c12, 'M', c6, 'L', c14, 'M', c18, 'L', c16, 'M', c19, 'L', c17)
        addGridLine(C, gridLine)
        # slashline
        slashLine = path()
        addToPath(slashLine, 'M', c24, 'L', c25)
        #seamline & cuttingline
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine :
            addToPath(P, 'M', c6, 'C', c18.c1, c18.c2, c18, 'C', c21.c1, c21.c2, c21, 'C', c19.c1, c19.c2, c19, 'C', c13.c1, c13.c2, c13, 'C', c14.c1, c14.c2, c14, 'C', c12.c1, c12.c2, c12, 'L', c9, 'C', c25.c1, c25.c2, c25, 'L', c22, 'C', c4.c1, c4.c2, c4, 'L', c5, 'C', c6.c1, c6.c2, c6)
        addSeamLine(C, seamLine)
        addCuttingLine(C, cuttingLine)

        #bodice cuff D
        drawPoints(D, locals())
        #letter
        pnt1 = Pnt(d7.x, d6.y/4.0)
        #label
        pnt2 = right(pnt1, 1*IN)
        D.label_x,  D.label_y = pnt2.x, pnt2.y
        #letter
        pnt3 = right(pnt2, 4*IN)
        D.setLetter(x = pnt3.x,  y = pnt3.y)
        #grainline points
        pnt1 = midPoint(d1, d6)
        dG1 = right(pnt1, distance(d1, d2)/4.0)
        dG2 = right(dG1, distance(d1, d2)/2.0)
        addGrainLine(D, dG1, dG2)
        # gridline
        gridLine = path()
        addToPath(gridLine, 'M', d1, 'L', d2, 'L', d4, 'L', d5, 'L', d7, 'L', d8, 'L', d1 )
        addGridLine(D, gridLine)
        # slashline
        slashLine = path()
        addToPath(slashLine, 'M', d9, 'L', d10, 'M', d11, 'L', d12)
        #seamline & cuttingline
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine :
            addToPath(P, 'M', d1, 'L', d2, 'L', d4, 'C', d5.c1, d5.c2, d5, 'L', d7, 'C', d8.c1, d8.c2, d8, 'L', d1)
        addSeamLine(D, seamLine)
        addCuttingLine(D, cuttingLine)

        #call doc.draw() to generate svg file

        doc.draw()
        return

