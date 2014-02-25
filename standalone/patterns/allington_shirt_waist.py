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
        self.setInfo('description', """This is a test pattern for Seamly Patterns. Adapted from Sara May Allington's 'Dressmaking', 1917""")
        self.setInfo('category', 'Shirt/TShirt/Blouse')
        self.setInfo('type', 'Historical')
        #
        # The next group are all optional
        #
        self.setInfo('gender', 'F') # 'M',  'F',  or ''
        self.setInfo('yearstart', 1900)
        self.setInfo('yearend', 1910)
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
        A = bodice.addPiece('Bodice Front', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = bodice.addPiece('Bodice Back', 'B', fabric = 2, interfacing = 0, lining = 0)
        C = bodice.addPiece('Sleeve', 'C', fabric = 2, interfacing = 0, lining = 0)
        D = bodice.addPiece('Cuff', 'D', fabric = 2, interfacing = 1, lining = 0)
        E = bodice.addPiece('Waistband Front', 'E', fabric = 2, interfacing = 1, lining = 0)
        F = bodice.addPiece('Waistband Back', 'F', fabric = 4, interfacing = 1, lining = 0)
        G = bodice.addPiece('Sleeve Under Placket', 'G', fabric = 2, interfacing = 0, lining = 0)
        H = bodice.addPiece('Sleeve Over Placket', 'H', fabric = 2, interfacing = 0, lining = 0)

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
        BWW = B.addPoint('BWW', left(BSH, CD.back_waist/2.0)) #back waist width
        BST = B.addPoint('BST', leftmostP(intersectCircles(BWC, CD.back_shoulder_balance, BNC, CD.back_shoulder_width/2.0))) #back shoulder point
        BNS = B.addPoint('BNS', highestP(onCircleAtY(BST, 1.1 * CD.shoulder, BSH.y))) #back neck side
        BAP = B.addPoint('BAP', lowestP(onCircleAtX(BNS, CD.back_underarm_balance, BNC.x - CD.across_back/2.0))) #back armscye point
        BUC = B.addPoint('BUC', (BNC.x, BAP.y)) #back underarm center
        BUS = B.addPoint('BUS', (BUW.x, BAP.y)) #back underarm side

        b1 = B.addPoint('b1', BNC) #B - new back neck center
        b2 = B.addPoint('b2', down(b1, 1.05 * distance(b1, BWC))) #A - new back waist center
        b3 = B.addPoint('b3', left(BUC, 1.05 * distance(BUC, BAP))) #E - back armscye
        b4 = B.addPoint('b4', left(BUC, 1.1 * distance(BUC, BUS))) #new back underarm side 1
        b5 = B.addPoint('b5', down(b4, 0.10 * CD.side)) # new lowered back underarm side
        b6 = B.addPoint('b6', onLineAtLength(BNS, BST, 0.05 * CD.shoulder)) #H - new back neck side
        b7 = B.addPoint('b7', BST) #back shoulder point
        b8 = B.addPoint('b8', left(BWC, 1.1 * CD.back_waist/2.0)) #U - temp back waist side
        b9 = B.addPoint('b9', (b8.x, b2.y)) #V - new back waist side
        b10 = B.addPoint('b10', up(b6))

        #back shoulder dart
        dart_width = 0.1 * CD.shoulder
        pnt1 = midPoint(BST, BNS)
        bD1 = B.addPoint('bD1', polar(pnt1, distance(BST, BAP)/3.0, angleOfLine(BNS, BST) - ANGLE90))
        bD1.i = B.addPoint('bD1.i', onLineAtLength(pnt1, BNS, dart_width/2.0))
        bD1.o = B.addPoint('bD1.o', onLineAtLength(pnt1, BST, dart_width/2.0))
        extendDart(b7, bD1, b6)
        foldDart(bD1, b6) #creates bD1.m for seamline, bD1.ic & bD1.oc for dartline

        #Back B control points
        #back neck control points from b6 to b1
        length = distance(b6, b1)/3.0
        b1.addInpoint(left(b1, length*2)) #long control point handle
        b6.addOutpoint(polar(b6, length/2.0, angleOfLine(b6, b1.inpoint))) #short control point handle
        #back side control points from b9 back waist side to b5 back underarm
        length = distance(b9, b5)/3.0
        b9.addOutpoint(up(b9, length))
        b5.addInpoint(down(b5, length))
        #back armscye points from b5 to b3 to b7
        b5.addOutpoint(right(b5, distance(b5, b3)/3.0))
        b3.addOutpoint(polar(b3, distance(b3, b7)/3.0, angleOfLine(b3, BNS)))
        b3.addInpoint(polar(b3, distance(b3, b5)/3.0, angleOfLine(b3.outpoint, b3)))
        b7.addInpoint(polar(b7, distance(b3, b7)/6.0, angleOfLine(b6, b7) - ANGLE90)) #short control handle



        #---Front A---#
        FNC = A.addPoint('FNC',(0, 0)) #front neck center
        FWC = A.addPoint('FWC', down(FNC, CD.front_waist_length)) #front waist center
        FSH = A.addPoint('FSH', up(FWC, CD.front_shoulder_height)) #front shoulder height
        FSW = A.addPoint('FSW', right(FSH, CD.front_shoulder_width/2.0)) #front shoulder width
        FUW = A.addPoint('FUW', right(FSH, CD.front_underarm/2.0)) #front underarm width
        FWW = A.addPoint('FWW', right(FSH, CD.front_waist/2.0)) #front waist widths
        FWS = A.addPoint('FWS', (FWW.x, FWC.y)) #front waist side
        FST = A.addPoint('FST', highestP(onCircleAtX(FWC, CD.front_shoulder_balance, FSW.x))) #front shoulder point
        FNS = A.addPoint('FNS', leftmostP(onCircleAtY(FST, CD.shoulder, FSH.y)))

        FAP = A.addPoint('FAP', lowestP(onCircleAtX(FNS, CD.front_underarm_balance, FNC.x + CD.across_chest/2.0))) #front armscye point
        FUC = A.addPoint('FUC', (FNC.x, FAP.y)) #front underarm center
        FUS = A.addPoint('FUS', (FUW.x, FAP.y)) #front undearm side
        FBP = A.addPoint('FBP', lowestP(onCircleAtX(FNS, FNC.x + CD.bust_balance, CD.bust_distance/2.0))) #front bust center
        FBC = A.addPoint('FBC', (FNC.x, FBP.y)) #front bust point
        FBS = A.addPoint('FBS', rightmostP(onCircleTangentFromOutsidePoint(FBP, CD.front_bust/2.0 - distance(FBC, FBP), FUS))) #bust side is where line from bust point is perpendicular to line through FUS

        a1 = A.addPoint('a1', down(FNC, distance(FNC, FUC)/4.0)) #S - new front neck center
        a2 = A.addPoint('a2', down(a1,  FWC.y + distance(BWC, b2))) #X -front waist center
        a3 = A.addPoint('a3', down(a2, 0.1 * CD.front_waist_length)) #new lowered front waist center
        a4 = A.addPoint('a4', (FNS.x, a3.y)) #point on front waist line
        a5 = A.addPoint('a5', right(FUC, 1.05 * distance(FUC, FAP))) #front armscye point
        a6 = A.addPoint('a6', right(FUC, 1.1 * distance(FUC, FUS))) #K - temp front underarm side
        a7 = A.addPoint('a7', onLineAtLength(FNS, FST, 0.05 * CD.shoulder)) #P - front neck side
        a8 = A.addPoint('a8', FST) #N - front shoulder point
        a9 = A.addPoint('a9', extendLine(FBP, FBS, 0.1 * CD.front_bust/2.0)) #front bust side
        a10 = A.addPoint('a10', onLineAtLength(a6, a9, distance(b4, b5)))  #lowered front underarm side
        a11 = A.addPoint('a11', onLineAtLength(a6, a9, distance(BUC, b2))) #temp front waist side
        a12 = A.addPoint('a12', polar(a11, abs(b8.x - b5.x), angleOfLine(a6, a9) + ANGLE90)) #front waist side

        #front control points - path runs counterclockwise from front neck center a1
        #b/w a7 front neck side to a1 front neck center
        length = distance(a7, a1)/3.0
        a1.addInpoint(right(a1, 0.7 * abs(a1.x - a7.x)))
        a7.addOutpoint(polar(a7, length, angleOfLine(a7, a8) + ANGLE90))
        #b/w a4 to a12 on front waistline
        length = distance(a4, a12)/3.0
        a4.addOutpoint(right(a4, 2 * length))
        a12.addInpoint(polar(a12, length/2.0, angleOfLine(FNS, a12) + ANGLE90))
        #b/w a12 front waist side to a10 front underarm side
        length = distance(a12, a10)/3.0
        a12.addOutpoint(polar(a12, length, angleOfLine(a11, a10)))
        a10.addInpoint(polar(a10, length, angleOfLine(a10, a11)))
        #b/w a10 front waist side to a5 front armscye point to a8 front shoulder point
        a10.addOutpoint(polar(a10, distance(a10, a5)/3.0, angleOfLine(FBS, FBP))) # same angle as side bust line)
        a5.addInpoint(polar(a5, distance(a5, a10)/3.0, angleOfLine(FNS, a5))) #angle from front neck side to front armscye point
        a5.addOutpoint(polar(a5, distance(a5, a8)/3.0, angleOfLine(a5, FNS)))
        a8.addInpoint(polar(a8, distance(a5, a8)/6.0, angleOfLine(a7, a8) + ANGLE90)) #short control handle

        #sleeve C
        c1 = C.addPoint('c1', (0, 0)) #A
        c2 = C.addPoint('c2', down(c1, CD.undersleeve_length)) #B
        c3 = C.addPoint('c3', up(c2, CD.elbow_length)) #C
        c5 = C.addPoint('c5', right(c3, 0.2 * CD.wrist)) #E - back elbow
        c4 = C.addPoint('c4', right(c2, 0.3 * CD.wrist)) #D - back wrist
        c6 = C.addPoint('c6', left(c1, 0.15 * CD.wrist)) #F - back underarm
        c7 = C.addPoint('c7', right(c4, 0.15 * CD.wrist)) #G
        c8 = C.addPoint('c8', right(c7, CD.hand + 0.25 * CD.wrist)) #H
        c9 = C.addPoint('c9', right(c8, 0.15 * CD.wrist)) #I - front wrist
        c10 = C.addPoint('c10', right(c5, 0.15 * CD.wrist)) #J
        c11 = C.addPoint('c11', right(c10, CD.elbow)) #K
        c12 = C.addPoint('c12', right(c11, 0.1 * CD.wrist)) #L - front elbow
        c13 = C.addPoint('c13', right(c1, CD.arm_scye)) #M
        c14 = C.addPoint('c14', right(c13, 0.25 * CD.wrist)) #N - front underarm
        c15 = C.addPoint('c15', up(c1, 0.3 * CD.wrist)) #O
        c16 = C.addPoint('c16', right(c1, 0.15 * CD.wrist)) #P
        c17 = C.addPoint('c17', left(c13, 0.25 * CD.wrist)) #Q
        c18 = C.addPoint('c18', (c16.x, c15.y)) #R
        c19 = C.addPoint('c19', (c17.x, c15.y)) #S
        c20 = C.addPoint('c20', midPoint(c16, c17)) #T
        c21 = C.addPoint('c21', up(c20, distance(c20, c18))) #U - above T - mid cap
        c22 = C.addPoint('c22', down(midPoint(c7, c8), 0.08 * CD.wrist)) #V - was U - mid-wrist

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

        #sleeve dart
        back_curve_length = distance(c4, c5) + curveLength(points2List(c5, c5.outpoint, c6.inpoint, c6))
        front_curve_length = distance(c9, c12) + curveLength(points2List(c14, c14.outpoint, c12.inpoint, c12))
        dart_width = front_curve_length - back_curve_length
        pnt1 = onLineAtLength(c12, c9, dart_width/2.0)
        pnt2 = extendLine(c9, c12, dart_width/2.0)
        pnt3 = midPoint(pnt1, pnt2)
        cD1 = C.addPoint('cD1', polar(pnt3, distance(c12, c5)/5.0, angleOfLine(pnt1, pnt2) - ANGLE90))
        cD1.o = C.addPoint('cD1.o', pnt1)
        cD1.i = C.addPoint('cD1.i', pnt2)
        extendDart(c9, cD1, c12.inpoint, extension=1/5.0)
        foldDart(cD1, c12.inpoint) #fold dart towards c12.inpoint - adds cD1.ic, cD1.oc, cD1.m
        #control points b/w c14 & cD1.i
        length = distance(c14, cD1.i)/3.0
        cD1.i.addInpoint(polar(cD1.i, length/2.0, angleOfLine(cD1, cD1.i) - ANGLE90))
        length = distance(cD1.o, c9)/3.0
        cD1.o.addOutpoint(polar(cD1.o, length/2.0, angleOfLine(cD1, cD1.o) + ANGLE90))
        c9.addInpoint(onLineAtLength(c9, cD1.o, length))

       #check sleeve length
       #back of sleeve - line c4,c5, curve c5,c8
        back_curve = points2List(c5, c5.outpoint, c6.inpoint, c6)
        back_sleeve_length = distance(c4, c5) + curveLength(back_curve)
        #front of sleeve - curve1 c14, cD1.i, curve2 cD1.o, c9
        front_curve1 = points2List(c14, c14.outpoint, cD1.i.inpoint, cD1.i)
        front_curve2 = points2List(cD1.o, cD1.o.outpoint, c9.inpoint, c9)
        front_sleeve_length = curveLength(front_curve1) + curveLength(front_curve2)
        #compare
        diff = back_sleeve_length - front_sleeve_length
        if diff != 0.0:
            if diff < 0.0 :
                #shorten sleeve front
                updatePoint(c9, up(c4, -diff))
                updatePoint(c22, up(c22, -diff/2.0))
            elif diff > 0.0:
                #lengthen sleeve front
                updatePoint(c9, down(c9, diff))
                updatePoint(c22, down(c22, diff/2.0))
            #update curve at wrist
            #c9 front wrist to c22 sleeve opening
            length = distance(c9, c22)/3.0
            updatePoint(c22.inpoint, right(c22, length))
            updatePoint(c9.outpoint, polar(c9, length, angleOfLine(c9, c22.inpoint)))
            #c22 sleeve opening to c4 back wrist
            length = distance(c22, c4)/3.0
            updatePoint(c22.outpoint, left(c22, length))
            updatePoint(c4.inpoint, polar(c4, length, angleOfLine(c4, c22.outpoint)))

        #sleeve cuff opening
        c23 = C.addPoint('c23', right(c4, 0.25 * distance(c4, c8))) #W
        c24 = C.addPoint('c24', up(c23, distance(c4, c3)/3.0)) #X - was V
        c25 = C.addPoint('c25', onCurveAtX(points2List(c22, c22.outpoint, c4.inpoint, c4), c23.x)) #Y - slash at wristline
        c26 = C.addPoint('c26', down(c25, SEAM_ALLOWANCE))

        #---cuff D---
        d1 = D.addPoint('d1', (0, 0))
        d2 = D.addPoint('d2', right(d1, CD.hand + 0.25 * CD.wrist)) # cuff width
        d3 = D.addPoint('d3', down(d2, 0.35 * CD.wrist)) #cuff height
        d4 = D.addPoint('d4', up(d3, distance(d2, d3)/3.0)) #start cuff curved corner 1
        d5 = D.addPoint('d5', left(d3, distance(d3, d4))) #end cuff curved corner 1
        d6 = D.addPoint('d6', down(d1, distance(d2, d3))) #cuff height
        d7 = D.addPoint('d7', right(d6, distance(d3, d5))) #end cuff curved corner 2
        d8 = D.addPoint('d8', up(d6, distance(d3, d4))) #start cuff curved corner 2
        #buttonhole
        buttonhole_startx = 0.1 * CD.wrist #place buttonhole at 10% cuff width
        buttonhole_starty = 0.55*distance(d1, d6) #place buttonhole at 70% cuff height
        buttonhole_width = 0.08 * CD.wrist #buttonhole length is 8% cuff width
        d9 = D.addPoint('d9', (d1.x + buttonhole_startx, d1.y + buttonhole_starty))
        d10 = D.addPoint('d10', right(d9, buttonhole_width))
        #button
        pnt1 = (d2.x - buttonhole_startx, d9.y)
        d11 = D.addPoint('d11', polar(pnt1, buttonhole_width/3.0, ANGLE45))
        d12 = D.addPoint('d12', polar(pnt1, buttonhole_width/3.0, ANGLE225))
        d13 = D.addPoint('d13', polar(pnt1, buttonhole_width/3.0, ANGLE135))
        d14 = D.addPoint('d14', polar(pnt1, buttonhole_width/3.0, ANGLE315))
        #cuff D control points
        length = distance(d4, d5)/3.0
        d4.addOutpoint(down(d4, length))
        d5.addInpoint(right(d5, length))
        d7.addOutpoint(left(d7, length))
        d8.addInpoint(down(d8, length))

        #---waistband-front E---
        e1 = E.addPoint('e1', (0, 0))
        e2 = E.addPoint('e2', right(e1, 1.1 * CD.front_waist/2.0 + 2.5 * buttonhole_width)) #waistband width (incl.10% ease)
        e3 = E.addPoint('e3', down(e2, CD.bust_length/4.0)) #waistband height
        e4 = E.addPoint('e4', down(e1, distance(e2, e3)))
        #waist centerfront line
        e5 = E.addPoint('e5', left(e2, 2.5 * buttonhole_width))
        e6 = E.addPoint('e6', down(e5, distance(e1, e4)))
        #buttonhole1
        buttonhole_startx = 0.75 * buttonhole_width
        buttonhole_starty = 0.5 * distance(e1, e4)
        e7 = E.addPoint('e7', (e5.x + buttonhole_startx, e1.y + buttonhole_starty))
        e8 = E.addPoint('e8', right(e7, buttonhole_width))
        #button1
        pnt1 = e8
        e9 = E.addPoint('e9', polar(pnt1, buttonhole_width/3.0, ANGLE45))
        e10 = E.addPoint('e10', polar(pnt1, buttonhole_width/3.0, ANGLE225))
        e11 = E.addPoint('e11', polar(pnt1, buttonhole_width/3.0, ANGLE135))
        e12 = E.addPoint('e12', polar(pnt1, buttonhole_width/3.0, ANGLE315))
        #buttonhole2
        e13 = E.addPoint('e13', (e5.x - 0.75*buttonhole_width, e7.y))
        e14 = E.addPoint('e14', left(e13, buttonhole_width))
        #button2
        pnt2 = e14
        e15 = E.addPoint('e15', polar(pnt2, buttonhole_width/3.0, ANGLE45))
        e16 = E.addPoint('e16', polar(pnt2, buttonhole_width/3.0, ANGLE225))
        e17 = E.addPoint('e17', polar(pnt2, buttonhole_width/3.0, ANGLE135))
        e18 = E.addPoint('e18', polar(pnt2, buttonhole_width/3.0, ANGLE315))

        #---Waistband-Back F---#
        f1 = F.addPoint('f1', (0, 0))
        f2 = F.addPoint('f2', right(f1, 1.1 * CD.back_waist)) #back waistband width
        f3 = F.addPoint('f3', down(f2, distance(e1, e4))) #back waistband height
        f4 = F.addPoint('f4', left(f3, distance(f1, f2)))

        #---Sleeve Underplacket G---#
        g1 = G.addPoint('g1', (0, 0))
        g2 = G.addPoint('g2', right(g1, distance(c4, c7))) #2 * placket width - distance(c4,c7) is arbitrary
        g3 = G.addPoint('g3', down(g2, distance(c24, c26))) #placket height
        g4 = G.addPoint('g4', left(g3, distance(g1, g2)))

        #---Sleeve Over Placket H---#
        h1 = H.addPoint('h1', g1)
        h2 = H.addPoint('h2', right(g1, distance(g1, g2))) #overplacket width = underplacket width
        h3 = H.addPoint('h3', down(h2, distance(g1, g4))) #overplacket height
        h4 = H.addPoint('h4', left(h3, distance(h1, h2)))
        h5 = H.addPoint('h5', midPoint(h1, h2))
        h6 = H.addPoint('h6', up(h5, 0.2 * distance(h1, h4))) #overplacket point

        #all points are defined,  now create marks, labels, grainlines, seamlines, cuttinglines, darts, etc.
        #Bodice Front A
        pnt1 = down(a7, distance(a7, a2)/3.0)
        A.setLabelPosition(pnt1)
        A.setLetter(up(pnt1, 0.5*IN), scaleby = 10.0)
        aG1 = dPnt((FNC.x + (a7.x - a1.x)/2.0, FUC.y))
        aG2 = down(aG1, 0.75 * CD.front_waist_length)
        A.addGrainLine(aG1, aG2)
        A.addGridLine(['M', FUW, 'L', FSH, 'L', FWC, 'L', FWS, 'L', FUS, 'L', FAP, 'L', FST, 'L', FNS, 'L', FNC, 'M', FUW, 'L', FUS, 'L', FUC, 'M', FSW, 'L', FST, 'M', FWW, 'L', FWS, 'M', FWC, 'L', FST, 'M', FBP, 'L', FNS, 'L', FAP, 'M', FBC, 'L', FBP, 'L', FBS])
        pathparts = (['M', a1, 'L', a3, 'L', a4, 'C', a12, 'C', a10, 'C', a5, 'C', a8, 'L', a7, 'C', a1])
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
        B.addGridLine(['M', BUW, 'L', BSH, 'L', BWC, 'L', BWS, 'L', BUS, 'L', BAP, 'L', BST, 'L', BNS, 'L', BNC, 'M', BUW, 'L', BUS, 'L', BUC, 'M',BSW, 'L', BST, 'M', BWW, 'L', BWS, 'M', BWC, 'L', BST, 'M', BNS, 'L', BAP])
        B.addDartLine(['M', bD1.oc, 'L', bD1, 'L', bD1.ic])
        pth = (['M', b1, 'L', b2, 'L', b9, 'C', b5, 'C', b3, 'C', b7, 'L', bD1.o, 'L', bD1.m, 'L', bD1.i, 'L', b6, 'C', b1])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        #Bodice Sleeve C
        C.setLetter((c21.x, c6.y), scaleby=12.0)
        C.setLabelPosition((c21.x, c6.y + 0.5*IN))
        cG1 = dPnt((c9.x/3.0, c20.y))
        cG2 = dPnt((cG1.x, c9.y*0.75))
        C.addGrainLine(cG1, cG2)
        C.addGridLine(['M', c15, 'L', c2, 'M', c15, 'L', c19, 'M', c2, 'L', c9, 'M', c3, 'L', c12, 'M', c6, 'L', c14, 'M', c18, 'L', c16, 'M', c19, 'L', c17])
        C.addDartLine(['M', cD1.ic, 'L', cD1, 'L', cD1.oc])
        mpth = C.addMarkingLine(['M', c24, 'L', c26])
        mpth.name = 'SleeveSlash'
        pathparts = (['M', c6, 'C', c18, 'C', c21, 'C', c19, 'C', c14, 'C', cD1.i, 'L', cD1.m, 'L', cD1.o, 'C', c9, 'C', c22, 'C', c4, 'L', c5, 'C', c6])
        C.addSeamLine(pathparts)
        C.addCuttingLine(pathparts)

        #Bodice Cuff D
        D.setLetter((0.3 * d2.x, 0.6 * d6.y), scaleby=4)
        D.setLabelPosition((0.5 * d2.x, 0.2 * d6.y))
        dG1 = (0.25 * d2.x, 0.75 * d6.y)
        dG2 = right(dG1, 0.5 * distance(d1, d2))
        D.addGrainLine(dG1, dG2)
        D.addGridLine(['M', d1, 'L', d2, 'L', d4, 'L', d5, 'L', d7, 'L', d8, 'L', d1])
        # buttonholes & buttons
        mpth = D.addMarkingLine(['M', d9, 'L', d10, 'M', d11, 'L', d12, 'M', d11, 'L', d12, 'M', d13, 'L', d14])
        mpth.name = 'Cuff D Button & Buttonhole'
        #seamline & cuttingline
        pathparts = (['M', d1, 'L', d2, 'L', d4, 'C', d5, 'L', d7, 'C', d8, 'L', d1])
        D.addSeamLine(pathparts)
        D.addCuttingLine(pathparts)

        #Waistband Front E
        #letter & label
        pnt1 = dPnt((0.15 * distance(e1, e2), 0.75 * distance(e1, e4)))
        E.setLetter((pnt1.x, pnt1.y), scaleby=4)
        E.setLabelPosition((0.25 * distance(e1, e2), 0.25 * distance(e1, e4)))
        #grainline
        eG1 = dPnt((0.5 * distance(e1, e2), 0.1 * distance(e1, e4)))
        eG2 = down(eG1, 0.75 * distance(e1, e4))
        E.addGrainLine(eG1, eG2)
        #center fold line, buttons, buttonholes
        mpth = E.addMarkingLine(['M', e5, 'L', e6, 'M', e7, 'L', e8, 'M', e9, 'L', e10, 'M', e11, 'L', e12, 'M', e13, 'L', e14, 'M', e15, 'L', e16, 'M', e17, 'L', e18])
        mpth.name = 'Waistband E Center Line, Buttons, Buttonholes'
        #seamline & cuttingline
        pathparts = (['M', e1, 'L', e2, 'L', e3, 'L', e4, 'L', e1])
        E.addSeamLine(pathparts)
        E.addCuttingLine(pathparts)

        #Waistband Back F
        pnt1 = dPnt((0.25 * distance(f1, f2), 0.75 * distance(f1, f4)))
        F.setLetter((pnt1.x, pnt1.y), scaleby=4)
        F.setLabelPosition((0.4 * distance(f1, f2), 0.25 * distance(f1, f4)))
        fG1 = dPnt((0.75 * distance(f1, f2), 0.15 * distance(f1, f4)))
        fG2 = down(fG1, 0.75 * distance(f1, f4))
        F.addGrainLine(fG1, fG2)
        pathparts = (['M', f1, 'L', f2, 'L', f3, 'L', f4, 'L', f1])
        F.addSeamLine(pathparts)
        F.addCuttingLine(pathparts)

        #Sleeve Placket G
        pnt1 = dPnt((0.2 * distance(g1, g2), 0.4 * distance(g1, g4)))
        G.setLetter((pnt1.x, pnt1.y), scaleby=2)
        G.setLabelPosition((0.1 * distance(g1, g2), 0.5 * distance(g1, g4)))
        gG1 = dPnt((0.8 * distance(g1, g2), 0.15 * distance(g1, g4)))
        gG2 = down(gG1, 0.75 * distance(g1, g4))
        G.addGrainLine(gG1, gG2)
        pathparts = (['M', g1, 'L', g2, 'L', g3, 'L', g4, 'L', g1])
        G.addSeamLine(pathparts)
        G.addCuttingLine(pathparts)

        #Sleeve Placket H
        pnt1 = dPnt((0.2 * distance(h1, h2), 0.4 * distance(h1, h4)))
        H.setLetter((pnt1.x, pnt1.y), scaleby=2)
        H.setLabelPosition((0.1 * distance(h1, h2), 0.5 * distance(h1, h4)))
        hG1 = dPnt((0.8 * distance(h1, h2), 0.15 * distance(h1, h4)))
        hG2 = down(hG1, 0.75 * distance(h1, h4))
        H.addGrainLine(hG1, hG2)
        pathparts = (['M', h1, 'L', h6, 'L', h2, 'L', h3, 'L', h4, 'L', h1])
        H.addSeamLine(pathparts)
        H.addCuttingLine(pathparts)

        #call draw() to generate svg file
        self.draw()

        return

