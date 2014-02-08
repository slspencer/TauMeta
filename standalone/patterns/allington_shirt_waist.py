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
It was adapted from Sara May Allington's 'Dressmaking',  1917.""")
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
        E = bodice.addPiece('waistband_front', 'E', fabric = 2, interfacing = 1, lining = 0)
        F = bodice.addPiece('waistband_back', 'F', fabric = 4, interfacing = 2, lining = 0)

        #pattern points
        # x, y coordinates are always passed as a two-item list like this: (23.6, 67.0)
        # points are always in the 'reference' group, and always have style='point_style'

        #---Back B---#
        BNC = B.addPoint('BNC', (0.0, 0.0)) #back neck center
        BWC = B.addPoint('BWC', down(BNC, CD.back_waist_length)) #back waist center
        BWS = B.addPoint('BWS', left(BWC, CD.back_waist/2.0)) #back waist side
        BSH = B.addPoint('BSH', up(BWC, CD.back_shoulder_height)) #back shoulder height
        BSW = B.addPoint('BSW', left(BSH, CD.back_shoulder_width/2.0)) #back shoulder width
        BUW = B.addPoint('BUW', left(BSH, CD.back_underarm/2.0)) #back underarm width
        BST = B.addPoint('BST', leftmostP(intersectCircles(BWC, CD.back_shoulder_balance, BNC, CD.back_shoulder_width/2.0))) #back shoulder tip
        BNS = B.addPoint('BNS', highestP(onCircleAtY(BST, CD.shoulder, BSH.y))) #back neck side
        BAS = B.addPoint('BAS', lowestP(onCircleAtX(BNS, CD.back_underarm_balance, BNC.x - CD.across_back/2.0))) #back armscye
        BUC = B.addPoint('BUC', (BNC.x, BAS.y)) #back underarm center
        BUS = B.addPoint('BUS', left(BUC, CD.back_bust/2.0)) #back underarm side

        b1 = B.addPoint('b1', BNC) #B
        b2 = B.addPoint('b2', down(b1, 1.05 * distance(b1, BWC))) #A
        b3 = B.addPoint('b3', left(BUC, 1.05 * distance(BUC, BAS))) #E
        b4 = B.addPoint('b4', left(BUC, 1.1 * distance(BUC, BUS)))
        b5 = B.addPoint('b5', onLineAtLength(BNS, BST, 0.05 * CD.shoulder)) #H
        b6 = B.addPoint('b6', left(BST, 0.2 * CD.shoulder)) #I
        b7 = B.addPoint('b7', midPoint(b4, b3)) #T on back bodice B
        b8 = B.addPoint('b8', (b7.x, b2.y)) #U
        b9 = B.addPoint('b9', right(b8, 0.1 * CD.back_waist/2.0)) #V - back waist side
        b10 = B.addPoint('b10', down(b7, 0.12 * CD.side))

        #Back B control points
        #back neck control points from b5 to b1
        length = distance(b5, b1)/3.0
        b1.addInpoint(left(b1, length*2)) #long control point handle
        b5.addOutpoint(polar(b5, length/2.0, angleOfLine(b5, b1.inpoint))) #short control point handle
        #back side control points from b9 back waist side to b10 back underarm
        length = distance(b9, b10)/3.0
        b9.addOutpoint(up(b9, length))
        b10.addInpoint(down(b10, length))
        #back armscye points from b10 to b3 to b6
        b10.addOutpoint(right(b10, distance(b10, b3)/3.0))
        b3.addOutpoint(polar(b3, distance(b3, b6)/3.0, (angleOfLine(b10, b3) + angleOfLine(b3, BNS))/2.0))
        b3.addInpoint(polar(b3, distance(b3, b10)/3.0, angleOfLine(b3.outpoint, b3)))
        b6.addInpoint(polar(b6, distance(b3, b6)/6.0, angleOfLine(b5, b6) - ANGLE90)) #short control handle

        #---Front A---#
        FBC = A.addPoint('FBC', left(BUC, CD.bust/2.0)) #front bust center
        FBP = A.addPoint('FBP', right(FBC, CD.bust_distance/2.0)) #front bust point
        FWC = A.addPoint('FWC', down(FBC, CD.bust_length)) #front waist center
        FWS = A.addPoint('FWS',  right(FWC, CD.front_waist/2.0)) #front waist side
        FNC = A.addPoint('FNC', up(FWC, CD.front_waist_length)) #front neck center
        FSH = A.addPoint('FSH', up(FWC, CD.front_shoulder_height)) #front shoulder height
        FSW = A.addPoint('FSW', right(FSH, CD.front_shoulder_width/2.0)) #front shoulder width
        FUW = A.addPoint('FUW', right(FSH, CD.front_underarm/2.0)) #front underarm width
        FST = A.addPoint('FST', rightmostP(intersectCircles(FWC, CD.front_shoulder_balance, FNC, CD.front_shoulder_width/2.0)))
        FNS = A.addPoint('FNS', leftmostP(onCircleAtY(FST, CD.shoulder, FSH.y)))
        FAS = A.addPoint('FAS', lowestP(onCircleAtX(FNS, CD.front_underarm_balance, FNC.x + CD.across_chest/2.0)))
        FUC = A.addPoint('FUC', (FNC.x, FAS.y))
        FUS = A.addPoint('FUS', right(FUC, CD.front_underarm/2.0))
        FBS = A.addPoint('FBS', rightmostP(onCircleTangentFromOutsidePoint(FBP, CD.front_bust/2.0 - distance(FBC, FBP), FUS))) #bust side is where line from bust point is perpendicular to line through FUS

        a1 = A.addPoint('a1', down(FNC, distance(FNC, FUC)/4.0)) #S
        a2 = A.addPoint('a2', extendLine(a1, FWC, distance(BWC, b2))) #X
        a3 = A.addPoint('a3', right(FUC, 1.05 * distance(FUC, FAS))) #L - front armscye + 5% ease
        a4 = A.addPoint('a4', right(FUS, 1.2 * distance(BUS, b7))) #K - front underarm side + 10% ease
        a5 = A.addPoint('a5', onLineAtLength(FNS, FST, 0.05 * CD.shoulder)) #P
        a6 = A.addPoint('a6', right(FST, 0.1 * CD.shoulder)) #N
        a7 = A.addPoint('a7', polar(a4, distance(b4, b7), angleOfLine(FBP, FBS))) #T
        a8 = A.addPoint('a8', down(a4, distance(b10, b8)))
        a9 = A.addPoint('a9', left(a8, distance(b8, b9))) #W - front waist side
        a10 = A.addPoint('a10', down(FBP, distance(FBC, a2))) #front waist under bust point
        a11 = A.addPoint('a11', onLineAtX(FBP, FBS, FUS.x))
        a12 = A.addPoint('a12', a9) #copy a9

        #front control points - path runs counterclockwise from front neck center a1
        #b/w a9 front waist side to a4 front underarm side
        length = distance(a9, a4)/3.0
        a9.addOutpoint(up(a9, length))
        a4.addInpoint(down(a4, length))
        #rotate side seam
        slashAndSpread(a4, -angleOfVector(a11, FUS, FBS), a9, a9.outpoint, a4.inpoint)
        #b/w a5 front neck side to a1 front neck center
        length = distance(a5, a1)/3.0
        a1.addInpoint(right(a1, 0.7 * abs(a1.x - a5.x)))
        a5.addOutpoint(polar(a5, length, angleOfLine(a5, a6) + ANGLE90))
        #b/w a10 front waist center to a9 front waist side
        length = distance(a10, a9)/3.0
        a10.addOutpoint(right(a10, 2 * length)) #control handle line is perpendicular to line a2-a1
        a9.addInpoint(polar(a9, length/2.0, angleOfLine(a4, a9) + ANGLE90))
        #b/w a4 to a3 to a6 armscye
        a4.addOutpoint(polar(a4, distance(a4, a3)/3.0, angleOfLine(a9, a4) - ANGLE90))
        a3.addOutpoint(polar(a3, distance(a3, a6)/3.0, (angleOfLine(a4, a3) + angleOfLine(a3, FNS))/2.0))
        a3.addInpoint(polar(a3, distance(a3, a4)/3.0, angleOfLine(a3.outpoint, a3)))
        a6.addInpoint(polar(a6, distance(a3, a6)/6.0, angleOfLine(a5, a6) + ANGLE90)) #short control handle

        #sleeve C
        c1 = C.addPoint('c1', (0, 0)) #A
        c2 = C.addPoint('c2', down(c1, CD.undersleeve_length)) #B
        c3 = C.addPoint('c3', up(c2, CD.elbow_length)) #C
        c4 = C.addPoint('c4', right(c2, 0.15 * CD.wrist)) #D
        c5 = C.addPoint('c5', right(c3, 0.1 * CD.wrist)) #E
        c6 = C.addPoint('c6', left(c1, 0.15 * CD.wrist)) #F
        c7 = C.addPoint('c7', right(c4, 0.15 * CD.wrist)) #G
        c8 = C.addPoint('c8', right(c7, CD.hand + 0.25 * CD.wrist)) #H
        c9 = C.addPoint('c9', right(c8, 0.15 * CD.wrist)) #I
        c10 = C.addPoint('c10', right(c5, 0.15 * CD.wrist)) #J
        c11 = C.addPoint('c11', right(c10, CD.elbow)) #K
        c12 = C.addPoint('c12', right(c11, 0.1 * CD.wrist)) #L
        c13 = C.addPoint('c13', right(c1, CD.arm_scye)) #M
        c14 = C.addPoint('c14', right(c13, 0.25 * CD.wrist)) #N
        c15 = C.addPoint('c15', up(c1, 0.3 * CD.wrist)) #O
        c16 = C.addPoint('c16', right(c1, 0.15 * CD.wrist)) #P
        c17 = C.addPoint('c17', left(c13, 0.25 * CD.wrist)) #Q
        c18 = C.addPoint('c18', (c16.x, c15.y)) #R
        c19 = C.addPoint('c19', (c17.x, c15.y)) #S
        c20 = C.addPoint('c20', midPoint(c16, c17)) #T
        c21 = C.addPoint('c21', up(c20, distance(c20, c18))) #U - above T
        c22 = C.addPoint('c22', down(midPoint(c7, c8), 0.08 * CD.wrist)) #V - was U

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
        length2 = distance(c19, c14)/3.0
        c21.addOutpoint(right(c21, length1))
        c19.addInpoint(polar(c19, length1, angleOfLine(c19, c21.outpoint)))
        c19.addOutpoint(polar(c19, length2, angleOfLine(c19.inpoint, c19)))
        c14.addInpoint(left(c14, length2))
        # c14 to c12
        length = distance(c14, c12)/3.0
        c12.addInpoint(polar(c12, length, angleOfLine(c9, c12)))
        c14.addOutpoint(polar(c14, length, angleOfLine(c14, c12.inpoint)))
        # c9 to c22
        length = distance(c9, c22)/3.0
        c22.addInpoint(right(c22, length))
        c9.addOutpoint(polar(c9, length, angleOfLine(c9, c22.inpoint)))
        #c22 to c4
        length = distance(c22, c4)/3.0
        c22.addOutpoint(left(c22, length))
        c4.addInpoint(polar(c4, length, angleOfLine(c4, c22.outpoint)))
        #c5 to c6
        length = distance(c5, c6)/3.0
        c5.addOutpoint(polar(c5, length, angleOfLine(c4, c5)))
        c6.addInpoint(polar(c6, length, angleOfLine(c6, c5.outpoint)))

        #add points for sleeve cuff opening
        c23 = C.addPoint('c23', right(c4, 0.75 * distance(c4, c8))) #W
        c24 = C.addPoint('c24', up(c23, distance(c4, c3)/3.0)) #X - was V
        c25 = C.addPoint('c25', onCurveAtX(points2List(c22, c22.inpoint, c9, c9.outpoint), c23.x)) #Y - new point
        c26 = C.addPoint('c26', down(c25, SEAM_ALLOWANCE))

        #cuff D
        d1 = D.addPoint('d1', (0, 0))
        d2 = D.addPoint('d2', right(d1, CD.hand + 0.25 * CD.wrist))
        d3 = D.addPoint('d3', down(d2, 0.35 * CD.wrist))
        d4 = D.addPoint('d4', up(d3, 0.08 * CD.wrist))
        d5 = D.addPoint('d5', left(d3, 0.15 * CD.wrist))
        d6 = D.addPoint('d6', down(d1, 0.35 * CD.wrist))
        d7 = D.addPoint('d7', right(d6, 0.15 * CD.wrist))
        d8 = D.addPoint('d8', up(d6, 0.08 * CD.wrist))
        length1 = 0.7*distance(d1, d6)
        length2 = 0.075 * CD.wrist
        d9 = D.addPoint('d9', (d1.x + 0.1 * CD.wrist, d1.y + length1))
        d10 = D.addPoint('d10', right(d9, length2))
        d11 = D.addPoint('d11', (d2.x - 0.1 * CD.wrist, d2.y + length1))
        d12 = D.addPoint('d12', left(d11, length2))
        #cuff D control points
        length = distance(d4, d5)/3.0
        d4.addOutpoint(down(d4, length))
        d5.addInpoint(right(d5, length))
        d7.addOutpoint(left(d7, length))
        d8.addInpoint(down(d8, length))

        #---waistband-front E---#
        e1 = E.addPoint('e1', (0, 0))
        e2 = E.addPoint('e2', down(e1, CD.bust_length/4.0))
        e3 = E.addPoint('e3', right(e2, CD.front_waist/2.0))
        e4 = E.addPoint('e4', up(e3, distance(e1, e2)))

        #---waistband-back F---#
        f1 = F.addPoint('f1', (0, 0))
        f2 = F.addPoint('f2', down(f1, distance(e1, e2)))
        f3 = F.addPoint('f3', right(f2, 1.1 * CD.back_waist))
        f4 = F.addPoint('f4', up(f3, distance(f1, f2)))

        #all points are defined,  now create marks, labels, grainlines, seamlines, cuttinglines, darts, etc.
        #Bodice Front A
        pnt1 = down(a5, distance(a5, a2)/3.0)
        A.setLabelPosition(pnt1)
        A.setLetter(up(pnt1, 0.5*IN), scaleby = 10.0)
        aG1 = dPnt((FNC.x + (a5.x - a1.x)/2.0, FUC.y))
        aG2 = down(aG1, 0.75 * CD.front_waist_length)
        A.addGrainLine(aG1, aG2)
        A.addGridLine(['M', FUC, 'L', FUS, 'L', FUW, 'L', FSH, 'L', FWC, 'L', FWS, 'M', FBP, 'L', FNS, 'L', FAS, 'M', FWC, 'L', FST, 'L', FNS, 'M', FBC, 'L', FBP, 'L', FBS])
        pathparts = (['M', a1, 'L', a2, 'L', a10, 'C', a9, 'C', a4, 'C', a3, 'C', a6, 'L', a5, 'C', a1])
        A.addSeamLine(pathparts)
        A.addCuttingLine(pathparts)

        #Bodice Back B
        pnt1 = dPnt((BNC.x - abs(BNC.x - BST.x)/2.0, BNC.y + abs(BUC.y - BNC.y)/2.0))
        B.setLabelPosition(pnt1)
        pnt2 = up(pnt1, 0.5*IN)
        B.setLetter(pnt2, scaleby = 10.0)
        bG1 = dPnt((BNC.x - abs(BNS.x - BNC.x)/2.0, abs(BUC.y - BNC.y)/2.0))
        bG2 = down(bG1, 0.75 * CD.back_waist_length)
        B.addGrainLine(bG1, bG2)
        B.addGridLine(['M', BST, 'L', BSW, 'L', BSH, 'L', BWC, 'L', BWS, 'M', BWC, 'L', BST, 'L', BNS, 'L',BAS, 'M', BUC, 'L', b4, 'M', b7, 'L', b8, 'L', b9])
        pth = (['M', b1, 'L', b2, 'L', b9, 'C', b10, 'C', b3, 'C', b6, 'L', b5, 'C', b1])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        #Bodice Sleeve C
        C.setLetter((c21.x, c6.y), scaleby=12.0)
        C.setLabelPosition((c21.x, c6.y + 0.5*IN))
        cG1 = dPnt((c9.x/3.0, c20.y))
        cG2 = dPnt((cG1.x, c9.y*0.75))
        C.addGrainLine(cG1, cG2)
        C.addGridLine(['M', c15, 'L', c2, 'M', c15, 'L', c19, 'M', c2, 'L', c9, 'M', c3, 'L', c12, 'M', c6, 'L', c14, 'M', c18, 'L', c16, 'M', c19, 'L', c17])
        mpth = C.addMarkingLine(['M', c24, 'L', c26])
        mpth.name = 'SleeveSlash'
        pathparts = (['M', c6, 'C', c18, 'C', c21, 'C', c19, 'C', c14, 'C', c12, 'L', c9, 'C', c22, 'C', c4, 'L', c5, 'C', c6])
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

        #Waistband Front E
        pnt1 = dPnt((e1.x + distance(e1, e4)/4.0, e1.y + 0.75 * distance(e1, e2)))
        E.setLetter((pnt1.x, pnt1.y), scaleby=5)
        E.setLabelPosition((pnt1.x + distance(e1, e4)/4.0, e1.y + distance(e1, e2)/4.0))
        eG1 = dPnt((e1.x + 0.75 * distance(e1, e4), e1.y + distance(e1, e2)/5.0))
        eG2 = down(eG1, 0.75 * distance(e1, e2))
        E.addGrainLine(eG1, eG2)
        pathparts = (['M', e1, 'L', e2, 'L', e3, 'L', e4, 'L', e1])
        E.addSeamLine(pathparts)
        E.addCuttingLine(pathparts)

        #Waistband Back F
        pnt1 = dPnt((f1.x + distance(f1, f4)/4.0, f1.y + 0.75 * distance(f1, f2)))
        F.setLetter((pnt1.x, pnt1.y), scaleby=5)
        F.setLabelPosition((pnt1.x + distance(f1, f4)/4.0, f1.y + distance(f1, f2)/4.0))
        fG1 = dPnt((f1.x + 0.75 * distance(f1, f4), f1.y + distance(f1, f2)/5.0))
        fG2 = down(fG1, 0.75 * distance(f1, f2))
        F.addGrainLine(fG1, fG2)
        pathparts = (['M', f1, 'L', f2, 'L', f3, 'L', f4, 'L', f1])
        F.addSeamLine(pathparts)
        F.addCuttingLine(pathparts)

        #call draw() to generate svg file
        self.draw()

        return

