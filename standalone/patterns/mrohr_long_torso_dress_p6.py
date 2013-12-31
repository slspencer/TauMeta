#!/usr/bin/env python
# patternName: Dress_Long_Torso_MRohr
# patternNumber: D_Long_Torso_MRohr

from tmtpl.designbase import *
from tmtpl.document import *
from tmtpl.pattern import *
from tmtpl.patternmath import *
from tmtpl.constants import *
from tmtpl.utils import *

class Design(designBase):

    def pattern(self):
        """
        Method defining a pattern design. This is where the designer places
        all elements of the design definition
        """

        # The designer must supply certain information to allow
        #   tracking and searching of patterns
        #
        # This group is all mandatory
        #
        self.setInfo('patternNumber', 'D_Long_Torso_MRohr')
        self.setInfo('patternTitle', 'Long Torso Dress - MRohr')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'M. Rohr')
        self.setInfo('patternmakerName', 'S.L.Spencer')
        self.setInfo('description', """Sleeveless fitted dress with square neckline, dropped waist and gathered skirt""")
        #TODO: add new category 'Block Patterns'
        self.setInfo('category', 'Dress')
        self.setInfo('type', 'block')
        self.setInfo('gender', 'F') # 'M',  'F',  or ''
        #
        # The next group are all optional
        #
        self.setInfo('recommendedFabric', '')
        self.setInfo('recommendedNotions', '')
        #
        self.setInfo('yearstart', '1950' )
        self.setInfo('yearend', '1959')
        self.setInfo('culture', 'European')
        #self.setInfo('wearer', '')
        #self.setInfo('source', '')
        #self.setInfo('characterName', '')
        #
        #get client data
        CD = self.CD #client data is prefaced with CD
        #
        #create pattern called 'dress'
        dress = self.addPattern('dress')
        #
        #create pattern pieces
        A = dress.addPiece('Bodice Front', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = dress.addPiece('Bodice Back', 'B', fabric = 2, interfacing = 0, lining = 0)
        C = dress.addPiece('Skirt Front', 'C', fabric = 2, interfacing = 0, lining = 0)
        D = dress.addPiece('Skirt Back', 'D', fabric = 2, interfacing = 0, lining = 0)

        #---Bodice Front A---#
        a1 = A.addPoint('a1', (0.0, 0.0)) #front neck center
        a2 = A.addPoint('a2', down(a1, CD.front_waist_length)) #front waist center
        a3 = A.addPoint('a3', up(a2, CD.bust_length)) #bust center
        a4 = A.addPoint('a4', left(a3, CD.bust_distance/2.0)) #bust point
        a5 = A.addPoint('a5', leftmostP(intersectCircles(a2, CD.front_shoulder_balance, a1, CD.front_shoulder_width))) #front shoulder point
        a6 = A.addPoint('a6', highestP(intersectCircles(a5, CD.shoulder, a4, CD.bust_balance))) #front neck point
        a7 = A.addPoint('a7', lowestP(onCircleAtX(a6, CD.front_underarm_balance, a1.x - CD.across_chest/2.0))) #front underarm point
        a8 = A.addPoint('a8', (a1.x, a7.y)) #front undearm center
        a9 = A.addPoint('a9', left(a8, CD.front_underarm/2.0)) #front underarm side
        a10 = A.addPoint('a10', leftmostP(onCircleTangentFromOutsidePoint(a4, CD.front_bust/2.0 - distance(a3, a4), a9))) #bust side is where line from bust point is perpendicular to line through a9
        a11 = A.addPoint('a11', onLineAtLength(a9, a10, 0.13 * CD.side)) #adjusted front underarm side on line a9-10
        a12 = A.addPoint('a12', left(a2, CD.front_waist/2.0)) #temporary front waist side 1 - on waist line
        a13 = A.addPoint('a13', dPnt((a4.x, a2.y))) #below bust point at waist
        a14 = A.addPoint('a14', intersectLines(a3, a4, a10, a11)) #intersect bust line & side seam
        a15 = A.addPoint('a15', onLineAtLength(a9, a10, CD.side)) #temporary front waist side 2 - on side seam

        #---darts---
        #Front A waist dart
        totalDartAngle = abs(angleOfVector(a12, a4, a15))
        frontWaistDartAngle = totalDartAngle/2.0
        bustDartAngle = totalDartAngle/2.0
        aD1 = A.addPoint('aD1', (a4)) #front waist dart point
        aD1.i = A.addPoint('aD1.i', onRayAtY(a4, ANGLE90 - frontWaistDartAngle/2.0, a2.y)) #front waist dart inside leg
        aD1.o = A.addPoint('aD1.o', onRayAtY(a4, ANGLE90 + frontWaistDartAngle/2.0, a2.y)) #front waist dart outside leg
        #Front A bust dart
        aD2 = A.addPoint('aD2', (a4)) #bust dart point
        aD2.i = A.addPoint('aD2.i', intersectLineRay(a9, a10, a4, ANGLE180 + bustDartAngle/2.0)) #bust dart inside leg
        aD2.o = A.addPoint('aD2.o', polar(a4, distance(a4, aD2.i), ANGLE180 - bustDartAngle/2.0)) #bust dart outside leg

        #TODO: create function pivot(pivot_point, rotation_angle, point_to_pivot) for slash_and_spread
        #finalize front waist side
        remainingSideSegment = distance(a11, a15) - distance(a11, aD2.i)
        remainingWaistSegment = distance(a2, a12) - distance(a2, aD1.i)
        a16 = A.addPoint('a16', leftmostP(intersectCircles(aD2.o, remainingSideSegment, aD1.o, remainingWaistSegment))) #front waist side
        #Front A hip extension
        a17 = A.addPoint('a17', left(aD1.o, distance(aD1.o, a16))) #temporary extension waist side
        a18 = A.addPoint('a18', down(a2, CD.front_hip_height)) #front hip center
        a19 = A.addPoint('a19', left(a18, CD.front_hip/2.0)) #front hip side
        a20 = A.addPoint('a20', (aD1.x, a18.y)) #waist dart point on hip line
        #finalize extension waist side
        a21 = A.addPoint('a21', leftmostP(intersectCircles(a20, distance(a20, a19), a16, CD.side_hip_height))) #front hip side
        #create front shoulder extension
        a22 = A.addPoint('a22', onLineAtLength(a6, a5, distance(a6, a5)/3.0)) #move neck point 1/3 down shoulder seam
        a23 = A.addPoint('a23', polar(a22, 0.75 * abs(a11.y - a22.y), angleOfLine(a5, a6) + ANGLE90)) #neck corner point
        a24 = A.addPoint('a24', (a1.x, a23.y)) #new front neck center
        a25 = A.addPoint('a25', midPoint(aD2.i, a11)) #b/w dart & underarm on side seam
        a26 = A.addPoint('a26', polar(a22, 2 * distance(a22, a5), angleOfLine(a6, a5) + angleOfDegree(6))) #temporary new shoulder tip
        a27 = A.addPoint('a27', midPoint(a2, a18)) #new front hip center
        a28 = A.addPoint('a28', midPoint(a16, a21)) #new front hip side
        #front lower waist dart
        aD3 = A.addPoint('aD3', up(a20, distance(a20, a13)/7.0)) #front waist dart point at hip
        aD3.i = A.addPoint('aD3.i', onLineAtY(aD1.i, aD3, a27.y)) #new lower waist dart inside
        aD3.o = A.addPoint('aD3.o', onLineAtY(aD1.o, aD3, a27.y)) #new lower waist dart outside

        #create curve at dart base
        ##adjustDartLength(a16, aD1, a2, extension=0.25) #smooth waistline curve from a16 to a2 at dart
        foldDart2(aD1, a2) #creates aD1.m,aD1.oc,aD1.ic; dart folds in toward waist center a2
        #do not call adjustDartLength(a12,aD2,a11) -- bust dart aD2 is not on a curve
        foldDart2(aD2, a11) #creates aD2.m,aD2.oc,aD2.ic; dart folds up toward underarm side a11
        foldDart2(aD3, a27) #creates aD3.m,aD3.oc,aD3.ic; dart folds in toward a27 front hip center
        #adjust aD1 & aD2 away from a4 bust point
        (aD1.x, aD1.y) = down(aD1, distance(aD1, aD1.i)/7.0)
        (aD2.x, aD2.y) = left(aD2, distance(aD2, aD2.i)/7.0)
        #adjust seam allowances for lower darts
        aD3.oc = dPnt(onLineAtLength(aD3.o, aD1.o, -SEAM_ALLOWANCE))
        aD3.ic = dPnt(onLineAtLength(aD3.i, aD1.i, -SEAM_ALLOWANCE))

        #dress Front A control points
        #b/w a6 front neck point & a1 front neck center
        a6.addOutpoint(down(a6, abs(a1.y - a6.y)/2.0))
        a1.addInpoint(left(a1, 0.75 * abs(a1.x - a6.x)))
        #b/w aD1.o waist dart outside leg & a16 front waist side - short control handles
        aD1.o.addOutpoint(polar(aD1.o, distance(aD1.o, a16)/6.0, angleOfLine(aD1.o, aD1) - (angleOfLine(aD1.i, aD1) - ANGLE180))) #control handle forms line with a2,aD1.i
        a16.addInpoint(polar(a16, distance(aD1.o, a16)/6.0, angleOfLine(a16, aD1.o.outpoint))) #a16 control handle points to aD1.o control handle
        #b/w a7 front underarm point & a5 front shoulder point
        a5.addInpoint(polar(a5, distance(a7, a5)/6.0, angleOfLine(a5, a6) + ANGLE90)) #short control handle perpendicular to shoulder seam
        a7.addOutpoint(polar(a7, distance(a7, a5)/3.0, angleOfLine(a7, a6))) #control handle points to front neck point
        #b/w a11 front underarm side & a7 front underarm point
        a7.addInpoint(polar(a7, distance(a11, a7)/3.0, angleOfLine(a6, a7)))
        a11.addOutpoint(polar(a11, distance(a11, a7)/3.0, angleOfLine(aD2.i, a11) + ANGLE90)) #control handle is perpendicular to side seam at underarm

        #--- Bodice Back B---#
        b1 = B.addPoint('b1', (0.0, 0.0)) #back neck center
        b2 = B.addPoint('b2', down(b1, CD.back_waist_length)) #back waist center
        b3 = B.addPoint('b3', up(b2, CD.back_shoulder_height)) #shoulder height reference point
        b4 = B.addPoint('b4', right(b2, CD.back_waist/2.0)) #back waist side reference point
        b5 = B.addPoint('b5', rightmostP(intersectCircles(b2, CD.back_shoulder_balance, b1, CD.back_shoulder_width))) #back shoulder point

        b6 = B.addPoint('b6', leftmostP(onCircleAtY(b5, CD.shoulder, b3.y))) #back neck point
        b7 = B.addPoint('b7', lowestP(onCircleAtX(b6, CD.back_underarm_balance, b1.x + CD.across_back/2.0))) #back underarm point
        b8 = B.addPoint('b8', (b1.x, b7.y)) #back undearm center
        b9 = B.addPoint('b9', right(b8, CD.back_underarm/2.0)) #back underarm side reference point
        b10 = B.addPoint('b10', down(b9, distance(a9, a11))) #adjusted back underarm side
        bD1 = B.addPoint('bD1', intersectLines(b2, b5, b8, b9)) #back waist dart point is at underarm height
        b12 = B.addPoint('b12', dPnt((bD1.x, b2.y))) # below dart point at waist
        bD1.i = B.addPoint('bD1.i', left(b12, distance(b2, b12)/5.0)) #dart inside leg
        bD1.o = B.addPoint('bD1.o', right(b12, distance(b12, bD1.i))) #dart outside leg
        b11 = B.addPoint('b11',  rightmostP(intersectCircles(b10, distance(a11, aD2.i) + distance(aD2.o, a16), bD1.o, CD.back_waist/2.0 - distance(b2, bD1.i)))) #back waist side
        #dress Back hip extension
        b13 = B.addPoint('b13', down(b2, CD.back_hip_height)) #back hip center
        b14 = B.addPoint('b14', right(bD1.o, distance(bD1.o, b11))) #back waist side
        b15 = B.addPoint('b15', (bD1.x, b13.y)) # back waist dart at hip line
        b16 = B.addPoint('b16', right(b13, CD.back_hip/2.0)) #temporary back hip side
        b17 = B.addPoint('b17', rightmostP(intersectCircles(b15, distance(b15, b16), b11, CD.side_hip_height))) #back waist side
        #create back shoulder extension
        b18 = B.addPoint('b18', onLineAtLength(b6, b5, distance(b6, b5)/3.0)) #move neck point 1/3 down shoulder seam
        b19 = B.addPoint('b19', down(b1, 0.66 * distance(b6, b18))) #new back neck center
        b20 = B.addPoint('b20', onLineAtLength(b10, b11, distance(a11, a25))) #new back underarm
        b21 = B.addPoint('b21', polar(b18, distance(a22, a26), angleOfLine(b6, b5) - angleOfDegree(6))) #new shoulder tip
        b22 = B.addPoint('b22', midPoint(b2, b13)) #new back hip center
        b23 = B.addPoint('b23', midPoint(b11, b17)) #new back hip side
        #Back lower waist dart
        bD2 = B.addPoint('bD2', up(b15, distance(b15, b12)/7.0)) # back waist dart point at hip
        bD2.i = B.addPoint('bD2.i', onLineAtY(bD1.i, bD2, b22.y)) #new lower waist dart inside
        bD2.o = B.addPoint('bD2.o', onLineAtY(bD1.o, bD2, b22.y)) #new lower waist dart outside
        #create curve at dart base
        foldDart2(bD1, b2) #creates bD1.m, bD1.oc, bD1.ic; dart folds toward waist center b2
        foldDart2(bD2, b22) #creates bD2.m, bD2.oc, bD2.ic; dart folds toward hip center b22
        #adjust seam allowances for lower darts
        bD2.oc = dPnt(onLineAtLength(bD2.o, bD1.o, -SEAM_ALLOWANCE))
        bD2.ic = dPnt(onLineAtLength(bD2.i, bD1.i, -SEAM_ALLOWANCE))

        #dress Back B control points
        #b/w b6 back neck point & b1 back neck center
        b1.addInpoint(right(b1, 0.75 * abs(b1.x - b6.x)))
        b6.addOutpoint(polar(b6, abs(b6.y - b1.y)/2.0, angleOfLine(b6, b5) + ANGLE90)) #perpendicular to shoulder seam
        #b/w b10 underarm point & b7 underarm curve
        b10.addOutpoint(polar(b10, distance(b10, b7)/3.0, angleOfLine(b10, b11) + ANGLE90)) #perpendicular to side seam
        b7.addInpoint(polar(b7, distance(b10, b7)/3.0, angleOfLine(b6, b7)))
        #b/w b7 underarm curve & b6 shoulder point
        b7.addOutpoint(polar(b7, distance(b7, b5)/3.0, angleOfLine(b7, b6)))
        b5.addInpoint(polar(b5, distance(b7, b5)/6.0, angleOfLine(b6, b5) + ANGLE90)) #short control handle, perpendicular to shoulder seam
        #b/w bD1.o waist dart outside leg & b11 waist side
        bD1.o.addOutpoint(polar(bD1.o, distance(bD1.o, b11)/6.0, angleOfLine(bD1.o, bD1) + ANGLE180 - angleOfVector(b2, bD1.i, bD1))) #short control handle, forms line with control handle for inside leg
        b11.addInpoint(polar(b11, distance(bD1.o, b11)/3.0, angleOfLine(b10, b11) + angleOfVector(aD2.o, a16, a16.inpoint))) #forms line with control handle for a16 front waist
        #b/w b18 back neck point & b19 back neck center
        b19.addInpoint(right(b19, abs(b18.x - b19.x)/2.0))
        b18.addOutpoint(polar(b18, abs(b18.y - b19.y)/2.0, angleOfLine(b18, b19.inpoint)))

        #---Skirt Front C---#
        c1 = C.addPoint('c1', (0, 0)) #front skirt waist center
        c2 = C.addPoint('c2', down(c1, (2 * CD.back_waist_length) - distance(b2, b22))) #front skirt hem center - length from waistline to hem is 2*back_waist_length
        c3 = C.addPoint('c3', left(c1, 3 * (distance(a27, aD3.i) + distance(aD3.o, a28)))) #front skirt waist side - skirt width is 3 * front hipline width
        c4 = C.addPoint('c4', down(c3, distance(c1, c2))) #front skirt hem side

        #---Skirt Back D---#
        d1 = D.addPoint('d1', (0, 0)) #back skirt waist center
        d2 = D.addPoint('d2', down(d1, distance(c1, c2))) #back skirt hem center
        d3 = D.addPoint('d3', right(d1, 3 * (distance(b22, bD2.i) + distance(bD2.o, b23)))) #back skirt waist side - skirt width is 3 * back hipline width
        d4 = D.addPoint('d4', down(d3, distance(c1, c2))) #back skirt hem side

        #---------------------------------------------#
        #---all points defined, draw pattern pieces---#
        #---------------------------------------------#

        #draw dress Front A
        A.setLetter((a22.x, a10.y), scaleby=10.0)
        A.setLabelPosition((a22.x, a25.y))
        aG1 = dPnt(left (a8, distance(a1, a6)/3.0))
        aG2 = dPnt(down(aG1, .75 * distance(a1, a18)))
        A.addGrainLine(aG1, aG2)
        A.addGridLine(['M', a1, 'L', a2, 'L', a5, 'M', a2, 'L', a18, 'M', a8, 'L', a9, 'M', a1, 'L', a5, 'M', a3, 'L', a4, 'M', a2, 'L', a12, 'M', a4, 'L', a6, 'L', a7, 'M', a11, 'L', a15, 'M', a4, 'L', a10, 'M', a14, 'L', a4, 'L', a20, 'L', a21,'M', a18, 'L', a19, 'M', a17, 'L', aD1.o, 'L', a16, 'M', a21, 'L', a16, 'M', a11, 'C', a7, 'C', a5, 'L', a6, 'C', a1, 'M', a27, 'L', aD3.i, 'L', aD3.o, 'L', a28,  'M', aD3.i, 'L', aD3, 'L', aD3.o])
        A.addDartLine(['M', aD3.oc, 'L', aD1.o, 'L', aD1, 'L', aD1.i, 'L', aD3.ic, 'M', aD2.ic, 'L', aD2, 'L', aD2.oc])

        #pth = (['M', a24, 'L', a18, 'L', a20, 'L', a21, 'L', a16, 'L', aD2.o, 'L', aD2.m, 'L', aD2.i, 'L', a25, 'L', a26, 'L', a22, 'L', a23, 'L', a24])
        pth = (['M', a24, 'L', a27, 'L', aD3.i, 'L', aD3.m, 'L', aD3.o, 'L', a28, 'L', a16, 'L', aD2.o, 'L', aD2.m, 'L', aD2.i, 'L', a25, 'L', a26, 'L', a22, 'L', a23, 'L', a24])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        #draw Bodice Back B
        B.setLetter((b6.x, 0.7 * distance(b19, b8)), scaleby=10.0)
        B.setLabelPosition((b6.x, 0.75 * distance(b19, b8)))
        bG1 = dPnt((distance(b3, b6)/2.0, 0.75 * distance(b19, b8)))
        bG2 = dPnt(down(bG1, 0.75 * distance(b19, b13)))
        B.addGrainLine(bG1, bG2)
        B.addGridLine(['M', b6, 'L', b3, 'L', b2, 'L', b14, 'M', bD1.o, 'L', b11, 'M', b1, 'L', b5, 'M', b2, 'L', b5, 'M', b6, 'L', b7, 'M', b8, 'L', b9, 'M',  bD1, 'L', b15, 'L', b16, 'M', b17, 'L', b11, 'M', b10, 'C', b7, 'C', b5, 'L', b6, 'C', b1, 'M', b22, 'L', bD2.i, 'L', bD2.o, 'L', b23, 'M', b2,  'L', b13, 'L', b15, 'L', b17, 'L', b11, 'M', bD2.ic, 'L', bD2, 'L', bD2.oc])

        B.addDartLine(['M', bD2.ic, 'L', bD1.i, 'L', bD1, 'L', bD1.o, 'L', bD2.oc])

        pth = (['M', b19, 'L', b22, 'L', bD2.i, 'L', bD2.m, 'L', bD2.o, 'L', b23, 'L', b11, 'L', b20, 'L', b21, 'L', b18, 'C', b19])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        #draw Skirt Front C
        C.setLetter(((c3.x - c1.x)/3.0, (c2.y - c1.y)/3.0), scaleby=10.0)
        C.setLabelPosition(((c3.x - c1.x)/3.0, (c2.y - c1.y)/2.0))
        cG1 = dPnt(( (c3.x - c1.x)/4.0, (c2.y - c1.y)/4.0 ))
        cG2 = dPnt(down(cG1, 0.75 * distance(c1, c2)))
        C.addGrainLine(cG1, cG2)
        pth = (['M', c1, 'L', c2, 'L', c4, 'L', c3, 'L', c1])
        C.addSeamLine(pth)
        C.addCuttingLine(pth)

        #draw Skirt Back D
        D.setLetter(((d3.x - d1.x)/3.0, (d2.y - d1.y)/3.0), scaleby=10.0)
        D.setLabelPosition(((d3.x - d1.x)/3.0, (d2.y - d1.y)/2.0))
        dG1 = dPnt(((d3.x - d1.x)/4.0, (d2.y - d1.y)/4.0))
        dG2 = dPnt(down(dG1, 0.75 * distance(d1, d2)))
        D.addGrainLine(dG1, dG2)
        pth = (['M', d1, 'L', d2, 'L', d4, 'L', d3, 'L', d1])
        D.addSeamLine(pth)
        D.addCuttingLine(pth)



        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

