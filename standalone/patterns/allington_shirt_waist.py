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

from tmtpl.designbase import *
from tmtpl.document import *
from tmtpl.pattern import *
from tmtpl.patternmath import *
from tmtpl.constants import *
from tmtpl.utils import *

class Design(designBase):

    def pattern(self) :
        """
        Method defining a pattern design. This is where the designer places
        all elements of the design definition
        """

        # The designer must supply certain information to allow
        #   tracking and searching of patterns
        #
        # This group is all mandatory
        #
        self.setInfo('patternNumber', 'AL_B1')
        self.setInfo('patternTitle', 'Allington Shirt Waist 1')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'Sara May Allington')
        self.setInfo('patternmakerName', 'S.L.Spencer')
        self.setInfo('description', """This is a test pattern for Seamly Patterns.
It was taken from Sara May Allington's 'Dressmaking',  1917.""")
        self.setInfo('category', 'Shirt/TShirt/Blouse')
        self.setInfo('type', 'Historical')
        #
        # The next group are all optional
        #
        self.setInfo('gender', 'F') # 'M',  'F',  or ''
        self.setInfo('yearstart', 1910)
        self.setInfo('yearend', 1920)
        self.setInfo('culture', 'European')
        self.setInfo('wearer', '')
        self.setInfo('source', '')
        self.setInfo('characterName', '')
        self.setInfo('recommendedFabric', '')
        self.setInfo('recommendedNotions', '')

        #get client data
        CD = self.CD #client data is prefaced with CD

        #create a pattern named 'bodice'
        bodice = self.addPattern('bodice')

        #create pattern pieces,  assign an id lettercd ..
        A = bodice.addPiece('front', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = bodice.addPiece('back', 'B', fabric = 2, interfacing = 0, lining = 0)
        C = bodice.addPiece('sleeve', 'C', fabric = 2, interfacing = 0, lining = 0)
        D = bodice.addPiece('cuff', 'D', fabric = 2, interfacing = 0, lining = 0)

        #pattern points
        # x, y coordinates are always passed as a two-item list like this: (23.6, 67.0)
        # points are always in the 'reference' group, and always have style='point_style'
        BNC = B.addPoint('BNC', (0.0, 0.0))
        BWC = B.addPoint('BWC', down(BNC, CD.back_waist_length))
        BSH = B.addPoint('BSH', up(BWC, CD.back_shoulder_height))
        BST = B.addPoint('BST', leftmostP(intersectCircles(BWC, CD.back_shoulder_balance, BNC, CD.back_shoulder_width)))
        BNS = B.addPoint('BNS', highestP(onCircleAtY(BST, CD.shoulder, BSH.y)))
        BAS = B.addPoint('BAS', lowestP(onCircleAtX(BNS, CD.back_underarm_balance, BNC.x - CD.across_back/2.0)))
        BUC = B.addPoint('BUC', (BNC.x, BAS.y))
        BUS = B.addPoint('BUS', left(BUC, CD.bust/4.0))
        BWS = B.addPoint('BWS', left(BWC, CD.waist/4.0))
        b1 = B.addPoint('b1', BNC) #B
        b2 = B.addPoint('b2', BWC) #A
        b3 = B.addPoint('b3', BUC) #C
        b4 = B.addPoint('b4', left(BUC, 1.05 * distance(BUC, BAS))) #E
        #b5  = B.addPoint('b5', up(b4, CD.arm_scye/3.0)) #F
        #b6  = B.addPoint('b6', up(b1, 0.5*IN)) #G
        #b7  = B.addPoint('b7', left(b6, 1.5*IN)) #H
        b5 = B.addPoint('b5', BST) #F
        b6 = B.addPoint('b6', BSH) #G
        b7 = B.addPoint('b7', BNS) #H
        #b8  = B.addPoint('b8', onLineAtLength(b5, b7, -0.5*IN)) #I
        b8 = B.addPoint('b8', left(b5, 0.1 * CD.shoulder)) #I
        b9 = B.addPoint('b9', midPoint(BUS, b4)) #T on back bodice B
        b10 = B.addPoint('b10', down(b9, CD.side)) #U
        b11 = B.addPoint('b11', right(b10, 1*IN)) #V
        #b12 = B.addPoint('b12', up(b4, distance(b5, b4)/3.0)) #Z - new point at back armscye - 1/3 up from

        FBC = A.addPoint('FBC', left(BUC, CD.bust/2.0))
        FBP = A.addPoint('FBP', right(FBC, CD.bust_distance/2.0))
        FWC = A.addPoint('FWC', down(FBC, CD.bust_length))
        FNC = A.addPoint('FNC', up(FWC, CD.front_waist_length)) #front neck center
        FSH = A.addPoint('FSH', up(FWC, CD.front_shoulder_height))
        FSW = A.addPoint('FSW', right(FSH, CD.front_shoulder_width))
        FUW = A.addPoint('FUW', right(FSH, CD.front_underarm/2.0))
        FST = A.addPoint('FST', rightmostP(intersectCircles(FWC, CD.front_shoulder_balance, FNC, CD.front_shoulder_width)))
        FNS = A.addPoint('FNS', leftmostP(onCircleAtY(FST, CD.shoulder, FSH.y)))
        FAS = A.addPoint('FAS', lowestP(onCircleAtX(FNS, CD.front_underarm_balance, FNC.x + CD.across_chest/2.0)))
        FUC = A.addPoint('FUC', (FNC.x, FAS.y))
        FUS = A.addPoint('FUS', right(FUC, CD.front_underarm/2.0))
        FBS = A.addPoint('FBS', rightmostP(onCircleTangentFromOutsidePoint(FBP, CD.front_bust/2.0 - distance(FBC, FBP), FUS))) #bust side is where line from bust point is perpendicular to line through FUS

        #a1 = A.addPoint('a1', left(b3, CD.bust/2.0)) #D
        #a2 = A.addPoint('a2', left(b4, CD.arm_scye/4.0)) #J
        #a2 = A.addPoint('a2', FAS) #J
        #a4 = A.addPoint('a4', up(a2, 2.5*IN)) #L
        #a5 = A.addPoint('a5', up(b5, 1.5*IN)) #M
        #a6 = A.addPoint('a6', left(a5, 2*IN)) #N
        #a6 = A.addPoint('a6', onLineAtLength(a8, a5, distance(b7, b8))) #N
        #a8 = A.addPoint('a8', (a7.x, b3.y - (CD.bust_balance - distance(b1, b7)))) #P
        #a11 = A.addPoint('a11', left(a10, (CD.neck/6.0) + 0.25*IN)) #S
        #a11 = A.addPoint('a11', left(a4, CD.across_chest/2.0 + 0.25*IN)) #S
        #a12 = A.addPoint('a12', b9) #T on front bodice A
        #a15 = A.addPoint('a15', down(a8, distance(a8, a14))) #Y - new point at front waist
        #a16 = A.addPoint('a16', down(a12, distance(b9, b13))) #front underarm point
        a1 = A.addPoint('a1', FUC) #D
        a3 = A.addPoint('a3', right(FUC, 1.1 * distance(FUC, FUS))) #K
        a4 = A.addPoint('a4', right(FUC, 1.05 * distance(FUC, FAS))) #L
        a5 = A.addPoint('a5', FST) #M
        a8 = A.addPoint('a8', FNS) #P
        a6 = A.addPoint('a6', right(a5, distance(b5, b8))) #N
        a7 = A.addPoint('a7', left(a6, distance(b7, b8))) #O
        a9 = A.addPoint('a9', down(a8, CD.neck/4.0)) #Q
        a10 = A.addPoint('a10', up(a9, 0.5*IN)) #R
        a11 = A.addPoint('a11', down(FNC, distance(FNC, FUC)/4.0)) #S
        a12 = A.addPoint('a12', right(FUS, distance(BUS, b9))) #T on front bodice A
        a19 = A.addPoint('a19', down(a12, distance(b9, b10)))
        a13 = A.addPoint('a13', left(a19, distance(b10, b11))) #W
        a14 = A.addPoint('a14', onLineAtLength(a11, a1, CD.front_waist_length)) #X
        a15 = A.addPoint('a15', (a8.x, a14.y)) #Y - new point at front waist
        a20 = A.addPoint('a20', down(FUS, 0.13 * CD.side))

        #temporary armscye curve from a3 to b12 to find top point of side seam
        a17 = A.addPoint('a17', right(a12, distance(b9, b4)))
        a18 = A.addPoint('a18', up(a17, distance(b4, BAS)))
        #length = distance(a3, b12)/3.0
        #temp_b12_c1 = right(a3, length) #don't create an svg controlpoint circle for this point
        #temp_b12_c2 = down(b12, length) #or for this point
        length = distance(a3, a18)/3.0
        t_a3out = right(a3, length)
        t_a18in = down(a18, length)


        #find top point of side seam with intersection of side and armscye curve, save to two points a16 and b13
        #curve1 = points2List(a3, temp_b12_c1, temp_b12_c2, b12)
        #intersections = intersectLineCurve(b10, b9, curve1) #this line is directional from b10 to b9
        #b13 = B.addPoint('b13', intersections[0]) # AA on bodice back B -use 1st intersection found, in this case there's only one intersection
        #a16 = A.addPoint('a16', b13) #AA on bodice back A
        #curve1 = points2List(a3, t_a3out, t_a18in, a18)
        #a16 = A.addPoint('a16', onCurveAtX(curve1, a12.x))
        a20.addOutpoint(right(a20, distance(a20, a18)/3.0))
        a18.addInpoint(polar(a18, distance(a20, a18)/3.0, angleOfLine(BNS, BAS)))
        curve1 = points2List(a20, a20.outpoint, a18.inpoint, a18)
        a21 = A.addPoint('a21', onCurveAtX(curve1, a12.x)) #new front underarm side
        curve2 = splitCurveAtPoint(curve1, a21)
        a21.addOutpoint(curve2[2])
        b12 = B.addPoint('b12', polar(BAS, distance(a18, a21), angleOfLine(a18, a21)))
        b12.addOutpoint(polar(b12, distance(b12, BAS)/3.0, angleOfLine(a21.outpoint, a21)))



        #front control points - path runs counterclockwise from front neck center a11
        #b/w a8 front neck side to a11 front neck center
        length = distance(a8, a11)/3.0
        a11.addInpoint(right(a11, 1.5*length))
        a8.addOutpoint(polar(a8, length, angleOfLine(a8, a11.inpoint)))
        #b/w a14 front waist center to a15 front waist middle
        length = distance(a14, a15)/3.0
        a14.addOutpoint(polar(a14, length, angleOfLine(a14, a11) + ANGLE90)) #control handle line is perpendicular to line a14-a11
        a15.addInpoint(left(a15, length))
        #b/w a13 front waist side to a21 front underarm side
        length = distance(a13, a21)/3.0
        a13.addOutpoint(up(a13, length))
        a21.addInpoint(down(a21, length))
        #b/w a15 front waist middle to a13 front waist side
        length = distance(a15, a13)/3.0
        a15.addOutpoint(right(a15, 2*length))
        a13.addInpoint(polar(a13, length/3.0, angleOfLine(a13.outpoint, a13) + ANGLE90))
        #b/w a21 to a4 to a6
        length1 = distance(a21, a4)/3.0
        length2 = distance(a4, a6)/3.0
        angle1 = angleOfLine(a21, a4)
        angle2 = angleOfLine(a4, a6)
        angle3 = (angle1 + angle2)/2.0
        a4.addInpoint(polar(a4, length1, angleOfLine(FNS, a4)))
        a4.addOutpoint(polar(a4, length2, angleOfLine(a4, FNS)))
        a6.addInpoint(polar(a6, length2/2.0, angleOfLine(a8, a6) + ANGLE90))

        slashAndSpread(a21, -angleOfVector(a20, FUS, FBS), a13.inpoint, a13, a13.outpoint, a21.inpoint)

        #back control points
        #back neck control points from b7 to b1
        length = distance(b7, b1)/3.0
        b7.addOutpoint(down(b7, length/2.0)) #short control point handle
        b1.addInpoint(left(b1, length*2)) #long control point handle
        #back side control points from b11 to b12
        length = distance(b11, b12)/3.0
        b11.addOutpoint(up(b11, length))
        b12.addInpoint(down(b12, length))
        #back armscye points from b12 to BAS to b8
        BAS.addInpoint(polar(BAS, distance(b12, BAS)/3.0, angleOfLine(BNS, BAS)))
        BAS.addOutpoint(polar(BAS, distance(BAS, b8)/3.0, angleOfLine(BAS, BNS)))
        b8.addInpoint(polar(b8, distance(BAS, b8)/6.0, angleOfLine(b7, b8) - ANGLE90)) #short control handle

        #sleeve C
        c1 = C.addPoint('c1', (0, 0)) #A
        c2 = C.addPoint('c2', down(c1, CD.oversleeve_length)) #B
        c3 = C.addPoint('c3', up(c2, CD.elbow_length)) #C
        c4 = C.addPoint('c4', right(c2, 1*IN)) #D
        c5 = C.addPoint('c5', right(c3, 0.5*IN)) #E
        c6 = C.addPoint('c6', left(c1, 1*IN)) #F
        c7 = C.addPoint('c7', right(c4, 1*IN)) #G
        c8 = C.addPoint('c8', right(c7, CD.hand + 2*IN)) #H
        c9 = C.addPoint('c9', right(c8, 1*IN)) #I
        c10 = C.addPoint('c10', right(c5, 1*IN)) #J
        c11 = C.addPoint('c11', right(c10, CD.elbow)) #K
        c12 = C.addPoint('c12', right(c11, 0.5*IN)) #L
        c13 = C.addPoint('c13', right(c1, CD.arm_scye)) #M
        c14 = C.addPoint('c14', right(c13, 2*IN)) #N
        c15 = C.addPoint('c15', up(c1, 2.5*IN)) #O
        c16 = C.addPoint('c16', right(c1, 1.5*IN)) #P
        c17 = C.addPoint('c17', left(c13, 3*IN)) #Q
        c18 = C.addPoint('c18', (c16.x, c15.y)) #R
        c19 = C.addPoint('c19', (c17.x, c15.y)) #S
        c20 = C.addPoint('c20', midPoint(c16, c17)) #T
        c21 = C.addPoint('c21', up(c20, distance(c20, c18))) #U - above T
        c22 = C.addPoint('c22', down(midPoint(c7, c8), 0.75*IN)) #V - was U
        c23 = C.addPoint('c23', right(c4, distance(c4, c8)*3/5.0)) #W
        c24 = C.addPoint('c24', up(c23, distance(c4, c3)/3.0)) #X - was V
        c25 = C.addPoint('c25', down(c23, 0.75*IN)) #Y - new point
        c26 = C.addPoint('c26', down(c25, SEAM_ALLOWANCE))
        # sleeve C control points
        # sleevecap c6 to c18 to c21 to c19 to c13 to c14
        length1 = distance(c6, c18)/3.0
        length2 = distance(c18, c21)/3.0
        c21.addInpoint(left(c21, length2))
        c18.addOutpoint(polar(c18, length2, angleOfLine(c18, c21.inpoint)))
        angle = angleOfLine(c6, c18) + angleOfVector(c18, c6, c1)/2.0
        c6.addOutpoint(polar(c6, length1, angle))
        c18.addInpoint(polar(c18, length1, angleOfLine(c21.inpoint, c18)))
        length1 = distance(c21, c19)/3.0
        length2 = distance(c19, c13)/3.0
        length3 = distance(c13, c14)/3.0
        c21.addOutpoint(right(c21, length1))
        c19.addInpoint(polar(c19, length1, angleOfLine(c19, c21.outpoint)))
        c19.addOutpoint(polar(c19, length2, angleOfLine(c19.inpoint, c19)))
        angle1 = angleOfLine(c19.outpoint, c13)/2.0
        c13.addInpoint(polar(c13, length2, angle1 + ANGLE180))
        c13.addOutpoint(polar(c13, length3, angle1))
        c14.addInpoint(polar(c14, length3, angleOfLine(c14, c13.outpoint)))
        # c14 to c12
        length = distance(c14, c12)/3.0
        c12.addInpoint(polar(c12, length, angleOfLine(c9, c12)))
        c14.addOutpoint(polar(c14, length, angleOfLine(c14, c12.inpoint)))
        # c9 to c25
        length = distance(c9, c25)/3.0
        c25.addInpoint(right(c25, length))
        c9.addOutpoint(polar(c9, length, angleOfLine(c9, c25.inpoint)))
        #c22 to c4
        length = distance(c22, c4)/3.0
        c22.addOutpoint(left(c22, length))
        c4.addInpoint(polar(c4, length, angleOfLine(c4, c22.outpoint)))
        #c5 to c6
        length = distance(c5, c6)/3.0
        c5.addOutpoint(polar(c5, length, angleOfLine(c4, c5)))
        c6.addInpoint(polar(c6, length, angleOfLine(c6, c5.outpoint)))

        #cuff D
        d1 = D.addPoint('d1', (0, 0))
        d2 = D.addPoint('d2', right(d1, CD.hand + 2*IN))
        d3 = D.addPoint('d3', down(d2, 3*IN))
        d4 = D.addPoint('d4', up(d3, 0.75*IN))
        d5 = D.addPoint('d5', left(d3, 1*IN))
        d6 = D.addPoint('d6', down(d1, 3*IN))
        d7 = D.addPoint('d7', right(d6, 1*IN))
        d8 = D.addPoint('d8', up(d6, 0.75*IN))
        length1 = 0.7*distance(d1, d6)
        length2 = 0.75*IN
        d9 = D.addPoint('d9', (d1.x + 0.5*IN, d1.y + length1))
        d10 = D.addPoint('d10', right(d9, length2))
        d11 = D.addPoint('d11', (d2.x - 0.5*IN, d2.y + length1))
        d12 = D.addPoint('d12', left(d11, length2))
        #cuff D control points
        length = distance(d4, d5)/3.0
        d4.addOutpoint(down(d4, length))
        d5.addInpoint(right(d5, length))
        d7.addOutpoint(left(d7, length))
        d8.addInpoint(down(d8, length))

        #all points are defined,  now create marks, labels, grainlines, seamlines, cuttinglines, darts, etc.
        #Bodice Front A
        pnt1 = down(a8, distance(a8, a15)/3.0)
        A.setLabelPosition(pnt1)
        A.setLetter(up(pnt1, 0.5*IN), scaleby = 10.0)
        aG1 = down(a11, CD.front_waist_length/3.0)
        aG2 = down(aG1, CD.front_waist_length/2.0)
        A.addGrainLine(aG1, aG2)
        A.addGridLine(['M', FNS, 'L',FSH, 'L', FWC, 'M', FUC, 'L', FUS, 'M', a8, 'L', a15, 'M', a11, 'L', a10, 'M', a7, 'L', a5])
        pathparts = (['M', a11, 'L', a14, 'C', a15, 'C', a13, 'C', a21, 'C', a4, 'C', a6, 'L', a8, 'C', a11])
        A.addSeamLine(pathparts)
        A.addCuttingLine(pathparts)

        #Bodice Back B
        pnt1 = down(midPoint(b7, b8), distance(b1, b2)/4.0)
        B.setLabelPosition(pnt1)
        pnt2 = up(pnt1, 0.5*IN)
        B.setLetter(pnt2, scaleby = 10.0)
        bG1 = down(b7, CD.back_waist_length/3.0)
        bG2 = down(bG1, CD.back_waist_length/2.0)
        B.addGrainLine(bG1, bG2)
        B.addGridLine(['M', BNS, 'L', b4, 'M', b3, 'L', b9, 'M', b9, 'L', b10, 'M', b7, 'L', b6, 'L', b1, 'M', b11, 'L', b10])
        pathparts = (['M', b1, 'L', b2, 'L', b11, 'C', b12, 'C', BAS, 'C', b8, 'L', b7, 'C', b1])
        B.addSeamLine(pathparts)
        B.addCuttingLine(pathparts)

        #Bodice Sleeve C
        C.setLetter((c21.x, c6.y), scaleby=12.0)
        C.setLabelPosition((c21.x, c6.y + 0.5*IN))
        cG1 = dPnt((c9.x/3.0, c20.y))
        cG2 = dPnt((cG1.x, c9.y*0.75))
        C.addGrainLine(cG1, cG2)
        C.addGridLine(['M', c15, 'L', c2, 'M', c15, 'L', c19, 'M', c2, 'L', c9, 'M', c3, 'L', c12, 'M', c6, 'L', c14, 'M', c18, 'L', c16, 'M', c19, 'L', c17])
        mpth = C.addMarkingLine(['M', c24, 'L', c26])
        mpth.name = 'SleeveSlash'
        pathparts = (['M', c6, 'C', c18, 'C', c21, 'C', c19, 'C', c13, 'C', c14, 'C', c12, 'L', c9, 'C', c25, 'L', c22, 'C', c4, 'L', c5, 'C', c6])
        C.addSeamLine(pathparts)
        C.addCuttingLine(pathparts)

        #Bodice Cuff D
        D.setLetter((d2.x/10.0, d6.y/2.0), scaleby=5)
        D.setLabelPosition((d2.x/4.0, d6.y/5.0))
        dG1 = (d2.x/4.0, d6.y*0.75)
        dG2 = right(dG1, distance(d1, d2)/2.0)
        D.addGrainLine(dG1, dG2)
        D.addGridLine(['M', d1, 'L', d2, 'L', d4, 'L', d5, 'L', d7, 'L', d8, 'L', d1])
        # buttonholes
        mpth = D.addMarkingLine(['M', d9, 'L', d10, 'M', d11, 'L', d12])
        mpth.name = 'CuffButtonHoles'
        pathparts = (['M', d1, 'L', d2, 'L', d4, 'C', d5, 'L', d7, 'C', d8, 'L', d1])
        D.addSeamLine(pathparts)
        D.addCuttingLine(pathparts)

        #call draw() to generate svg file
        self.draw()

        return

