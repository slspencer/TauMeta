#!/usr/bin/env python
# patternName: Womens Long Bodice Block - Spencer
# patternNumber: Block_W_Bodice-Long_Spencer

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
        self.setInfo('patternNumber', 'Block_W_Bodice-Long_Spencer')
        self.setInfo('patternTitle', 'Womens Long Bodice Block - Spencer')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'S.L.Spencer')
        self.setInfo('patternmakerName', 'S.L.Spencer')
        self.setInfo('description', """This is a test pattern for Seamly Patterns""")
        self.setInfo('category', 'Shirt/TShirt/Blouse')
        self.setInfo('type', 'block')
        self.setInfo('gender', 'F') # 'M',  'F',  or ''
        #
        # The next group are all optional
        #
        self.setInfo('recommendedFabric', '')
        self.setInfo('recommendedNotions', '')
        #
        #self.setInfo('yearstart',1940 )
        #self.setInfo('yearend', 2013)
        #self.setInfo('culture', 'European')
        #self.setInfo('wearer', '')
        #self.setInfo('source', '')
        #self.setInfo('characterName', '')
        #
        #get client data
        CD = self.CD #client data is prefaced with CD
        #
        #create pattern called 'bodice'
        bodice = self.addPattern('bodice')
        #
        #create pattern pieces
        A = bodice.addPiece('Front', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = bodice.addPiece('Back', 'B', fabric = 2, interfacing = 0, lining = 0)
        C = bodice.addPiece('Sleeve', 'C', fabric = 2, interfacing = 0, lining = 0)

        #---Bodice Front A---#
        a1 = A.addPoint('a1', (0.0, 0.0)) #front neck center
        a2 = A.addPoint('a2', down(a1, CD.front_waist_length)) #front waist center
        a23 = A.addPoint('a23', up(a2, CD.front_shoulder_height)) #front shoulder height
        a3 = A.addPoint('a3', up(a2, CD.bust_length)) #bust center
        a4 = A.addPoint('a4', left(a3, CD.bust_distance/2.0)) #bust point
        a5 = A.addPoint('a5', leftmostP(intersectCircles(a2, CD.front_shoulder_balance, a1, CD.front_shoulder_width))) #front shoulder point
        #a6 = A.addPoint('a6', highestP(intersectCircles(a5, CD.shoulder, a4, CD.bust_balance))) #front neck point
        a6 = A.addPoint('a6', rightmostP(onCircleAtY(a5, CD.shoulder, a23.y))) #front neck point
        a7 = A.addPoint('a7', lowestP(onCircleAtX(a6, CD.front_underarm_balance, a1.x - CD.across_chest/2.0))) #front underarm point
        a8 = A.addPoint('a8', (a1.x, a7.y)) #front undearm center
        a9 = A.addPoint('a9', left(a8, CD.front_underarm/2.0)) #front underarm side
        #TODO: create function onCircleAtTangentOfPoint()
        a10 = A.addPoint('a10', leftmostP(onCircleTangentFromOutsidePoint(a4, CD.front_bust/2.0 - distance(a3, a4), a9))) #bust side is where line from bust point is perpendicular to line through a9
        a11 = A.addPoint('a11', onLineAtLength(a9, a10, 0.13 * CD.side)) #adjusted front underarm side on line a9-10
        a12 = A.addPoint('a12', left(a2, CD.front_waist/2.0)) #temporary front waist side 1 - on waist line
        a13 = A.addPoint('a13', dPnt((a4.x, a2.y))) #below bust point at waist
        a14 = A.addPoint('a14', intersectLines(a3, a4, a10, a11)) #intersect bust line & side seam
        a15 = A.addPoint('a15', onLineAtLength(a9, a10, CD.side)) #temporary front waist side 2 - on side seam

        #front waist dart
        totalDartAngle = abs(angleOfVector(a12, a4, a15))
        frontWaistDartAngle = totalDartAngle/2.0
        bustDartAngle = totalDartAngle/2.0
        aD1 = A.addPoint('aD1', (a4)) #front waist dart point
        aD1.i = A.addPoint('aD1.i', onRayAtY(a4, ANGLE90 - frontWaistDartAngle/2.0, a2.y)) #front waist dart inside leg
        aD1.o = A.addPoint('aD1.o', onRayAtY(a4, ANGLE90 + frontWaistDartAngle/2.0, a2.y)) #front waist dart outside leg
        #bust dart
        aD2 = A.addPoint('aD2', (a4)) #bust dart point
        aD2.i = A.addPoint('aD2.i', intersectLineRay(a9, a10, a4, ANGLE180 + bustDartAngle/2.0)) #bust dart inside leg
        aD2.o = A.addPoint('aD2.o', polar(a4, distance(a4, aD2.i), ANGLE180 - bustDartAngle/2.0)) #bust dart outside leg
        #TODO: create function pivot(pivot_point, rotation_angle, point_to_pivot)

        #finalize front waist side
        remainingSideSegment = distance(a11, a15) - distance(a11, aD2.i)
        remainingWaistSegment = distance(a2, a12) - distance(a2, aD1.i)
        a16 = A.addPoint('a16', leftmostP(intersectCircles(aD2.o, remainingSideSegment, aD1.o, remainingWaistSegment))) #front waist side created after all darts defined

        #create curve at dart base
        ##adjustDartLength(a16, aD1, a2, extension=0.25) #smooth waistline curve from a16 to a2 at dart
        foldDart2(aD1, a2) #creates aD1.m,aD1.oc,aD1.ic; dart folds in toward waist center a2
        #do not call adjustDartLength(a12,aD2,a11) -- bust dart aD2 is not on a curve
        foldDart2(aD2, a11) #creates aD2.m,aD2.oc,aD2.ic; dart folds up toward underarm side a11
        #adjust aD1 & aD2 away from a4 bust point
        (aD1.x, aD1.y) = down(aD1, distance(aD1, aD1.i)/7.0)
        (aD2.x, aD2.y) = left(aD2, distance(aD2, aD2.i)/7.0)

        #Bodice Front A hip extension
        a17 = A.addPoint('a17', down(a2, CD.front_hip_height)) #front hip center
        a18 = A.addPoint('a18', left(aD1.o, distance(aD1.o, a16))) #front waist side
        a19 = A.addPoint('a19', (aD1.x, a17.y)) #lower waist dart point on hip line
        a20 = A.addPoint('a20', left(a17, CD.front_hip/2.0)) #temporary front hip side
        #a21 = A.addPoint('a21', polar(19, distance(aD1.o, a20), angleOfLine(aD1.o, a20) + angleOfVector(a18, aD1.o, a16))) #final front hip side
        #a22 = A.addPoint('a22', onLineAtLength(a16, a21, CD.side_hip_height)) #front hip side
        a21 = A.addPoint('a21', leftmostP(intersectCircles(a19, CD.front_hip/2.0 - distance(a17, a19), a16, CD.side_hip_height)))
        aD1.d = A.addPoint('aD1.d', up(a19, distance(a19, a13)/7.0)) #front waist dart point at hip

        #Bodice Front A control points
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

        #---Bodice Back B---#
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
        b18 = B.addPoint('b18', intersectLines(b2, b5, b8, b9)) #dart reference point
        b12 = B.addPoint('b12', dPnt((b18.x, b2.y))) # below dart point at waist
        #bD1 = B.addPoint('bD1', intersectLines(b2, b5, b8, b9)) #back waist dart point is at underarm height
        bD1 = B.addPoint('bD1', (b18.x, b10.y)) #back waist dart point is at underarm height
        bD1.i = B.addPoint('bD1.i', left(b12, distance(b2, b12)/5.0)) #dart inside leg
        bD1.o = B.addPoint('bD1.o', right(b12, distance(b12, bD1.i))) #dart outside leg
        b11 = B.addPoint('b11',  rightmostP(intersectCircles(b10, distance(a11, aD2.i) + distance(aD2.o, a16), bD1.o, CD.back_waist/2.0 - distance(b2, bD1.i)))) #back waist side

        #create curve at dart base
        ##adjustDartLength(a16, aD1, a2, extension=0.25) #smooth waistline curve from a16 to a2 at dart
        foldDart2(bD1, b2) #creates bD1.m, bD1.oc, bD1.ic; dart folds toward waist center b2

        #back hip extension
        b13 = B.addPoint('b13', down(b2, CD.back_hip_height)) #back hip center
        b14 = B.addPoint('b14', right(bD1.o, distance(bD1.o, b11))) #back waist side
        b15 = B.addPoint('b15', (bD1.x, b13.y)) # back waist dart at hip line
        b16 = B.addPoint('b16', right(b13, CD.back_hip/2.0)) #temporary back hip side
        b17 = B.addPoint('b17', rightmostP(intersectCircles(b15, CD.back_hip/2.0 - distance(b13, b15), b14, CD.side_hip_height)))
        bD1.d = B.addPoint('bD1.d', up(b15, distance(b15, b12)/7.0)) # back waist dart point at hip

        #Bodice Back B control points
        #b/w b6 back neck point & b1 back neck center
        b1.addInpoint(right(b1, 0.75 * abs(b1.x - b6.x)))
        b6.addOutpoint(polar(b6, abs(b6.y - b1.y)/2.0, angleOfLine(b6, b5) + ANGLE90)) #perpendicular to shoulder seam
        #b/w b10 underarm point & b7 underarm curve
        b10.addOutpoint(polar(b10, distance(b10, b7)/3.0, angleOfLine(b10, b11) + ANGLE90)) #perpendicular to side seam
        b7.addInpoint(polar(b7, distance(b10, b7)/3.0, angleOfLine(b6, b7)))
        #b/w b7 underarm curve & b5 shoulder point
        b7.addOutpoint(polar(b7, distance(b7, b5)/3.0, angleOfLine(b7, b6)))
        b5.addInpoint(polar(b5, distance(b7, b5)/6.0, angleOfLine(b6, b5) + ANGLE90)) #short control handle, perpendicular to shoulder seam
        #b/w bD1.o waist dart outside leg & b11 waist side
        bD1.o.addOutpoint(polar(bD1.o, distance(bD1.o, b11)/6.0, angleOfLine(bD1.o, bD1) + ANGLE180 - angleOfVector(b2, bD1.i, bD1))) #short control handle, forms line with control handle for inside leg
        b11.addInpoint(polar(b11, distance(bD1.o, b11)/3.0, angleOfLine(b10, b11) + angleOfVector(aD2.o, a16, a16.inpoint))) #forms line with control handle for a16 front waist

        #---Shirt sleeve C---#
        #get front & back armcye length
        back_armscye_curve = points2List(b10, b10.outpoint, b7.inpoint, b7, b7.outpoint, b5.inpoint, b5)
        back_armscye_curve_length = curveLength(back_armscye_curve, n=200)
        back_lower_armscye_curve = points2List(b10, b10.outpoint, b7.inpoint, b7)
        back_lower_armscye_curve_length = curveLength(back_lower_armscye_curve, n=200)
        back_upper_armscye_curve = points2List(b7, b7.outpoint, b5.inpoint, b5)
        back_upper_armscye_curve_length = curveLength(back_upper_armscye_curve, n=200)

        front_armscye_curve = points2List(a11, a11.outpoint, a7.inpoint, a7, a7.outpoint, a5.inpoint, a5)
        front_armscye_curve_length = curveLength(front_armscye_curve, n=200)
        front_lower_armscye_curve = points2List(a11, a11.outpoint, a7.inpoint, a7)
        front_lower_armscye_curve_length = curveLength(front_lower_armscye_curve, n=200)
        front_upper_armscye_curve = points2List(a7, a7.outpoint, a5.inpoint, a5)
        front_upper_armscye_curve_length = curveLength(front_upper_armscye_curve, n=200)

        ARMSCYE_LENGTH = back_armscye_curve_length + front_armscye_curve_length
        SLEEVE_LENGTH = CD.oversleeve_length
        BICEP_WIDTH = 1.08 * CD.bicep #8% ease in bicep
        WRIST_WIDTH = 1.08 * CD.wrist #8% ease in wrist
        ELBOW_WIDTH = 1.05 * CD.elbow #8% ease in elbow

        c1 = C.addPoint('c1', (-BICEP_WIDTH/2.0, 0.0)) #back underarm
        c2 = C.addPoint('c2', (BICEP_WIDTH/2.0, 0.0)) #front underarm
        c3 = C.addPoint('c3', highestP(intersectCircles(c1, 0.9 * distance(b10, b7) + distance(b7, b5), c2, 0.9 * distance(a11, a7) + distance(a7, a5)))) #top of sleeve cap
        c4 = C.addPoint('c4', midPoint(c1, c2)) #mid-bicep
        c5 = C.addPoint('c5', down(c4, CD.undersleeve_length)) #mid-wrist
        c6 = C.addPoint('c6', midPoint(c4, c5)) #mid elbow
        c7 = C.addPoint('c7', onLineAtLength(c1, c3, distance(b10, b7))) #back cap curve point
        c8 = C.addPoint('c8', onLineAtLength(c2, c3, distance(a11, a7))) #front cap curve point
        c9 = C.addPoint('c9', left(c5, WRIST_WIDTH/2.0)) #back wrist
        c10 = C.addPoint('c10', right(c5, WRIST_WIDTH/2.0)) #front wrist
        c11 = C.addPoint('c11', left(c6, ELBOW_WIDTH/2.0)) #back elbow
        c12 = C.addPoint('c12', right(c6, ELBOW_WIDTH/2.0)) #front elbow

        #cap control points
        c3.addInpoint(left(c3, abs(c3.x - c1.x)/2.0))
        c3.addOutpoint(right(c3, abs(c3.x - c2.x)/2.0))

        #b/w c1 back underarm & c7 back cap curve point
        c1.addOutpoint(right(c1, distance(c1, c7)/3.33))
        c7.addInpoint(polar(c7, distance(c1, c7)/3.33, angleOfLine(c3.inpoint, c7)))
        adjustCurves(back_lower_armscye_curve, c1, c1.outpoint, c7.inpoint, c7)

        #b/w c7 back cap curve point & c3 top cap
        c7.addOutpoint(polar(c7, distance(c7, c3.inpoint)/3.33, angleOfLine(c7, c3.inpoint)))
        adjustCurves(back_upper_armscye_curve, c7, c7.outpoint, c3.inpoint, c3)

        #front sleeve cap
        c8.addInpoint(polar(c8, distance(c3.outpoint, c8)/3.33, angleOfLine(c8, c3.outpoint)))
        adjustCurves(front_upper_armscye_curve, c3, c3.outpoint, c8.inpoint, c8)
        c8.addOutpoint(polar(c8, distance(c8, c2)/3.33, angleOfLine(c3.outpoint, c8)))
        c2.addInpoint(polar(c2, distance(c8, c2)/3.33, angleOfLine(c12, c2) - ANGLE90))
        adjustCurves(front_lower_armscye_curve, c8, c8.outpoint, c2.inpoint, c2)

        #---------------------------------------------#
        #---all points defined, draw pattern pieces---#
        #---------------------------------------------#

        #draw Bodice Front A
        pnt1 = dPnt(midPoint(a7, a8))
        A.setLabelPosition((pnt1))
        A.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        aG1 = dPnt(left(a8, distance(a8, pnt1)/4.0))
        aG2 = dPnt(down(aG1, distance(a1, a2)/2.0))
        A.addGrainLine(aG1, aG2)
        A.addGridLine(['M', a1, 'L', a2, 'L', a5, 'M', a8, 'L', a9, 'M', a1, 'L', a5, 'M', a3, 'L', a4, 'M', a2, 'L', a12, 'M', a4, 'L', a6, 'L', a7, 'M', a11, 'L', a15, 'M', a4, 'L', a10, 'M', a14, 'L', a4, 'L', a19, 'M', a17, 'L', a20, 'M', a18, 'L', aD1.o, 'L', a16, 'M', a21, 'L', a16])
        A.addDartLine(['M', aD1.i, 'L', aD1, 'L', aD1.o, 'L', aD1.d, 'L', aD1.i, 'M', aD2.ic, 'L', aD2, 'L', aD2.oc])
        pth = (['M', a1, 'L', a17, 'L', a19, 'L', a21, 'L', a16, 'L', aD2.o, 'L', aD2.m, 'L', aD2.i, 'L', a11, 'C', a7, 'C', a5, 'L', a6, 'C', a1])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        #draw Bodice Back B
        pnt1 = dPnt((distance(b3, b6)/2.0, distance(b1, b8)/2.0))
        B.setLabelPosition((pnt1))
        B.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        bG1 = dPnt((distance(b3, b6)/4.0, distance(b1, b8)/4.0))
        bG2 = dPnt(down(bG1, distance(b1, b2)/2.0))
        B.addGrainLine(bG1, bG2)
        B.addGridLine(['M', b6, 'L', b3, 'L', b2, 'L', b14, 'M', bD1.o, 'L', b11, 'M', b1, 'L', b5, 'M', b2, 'L', b5, 'M', b6, 'L', b7, 'M', b8, 'L', b9, 'M',  bD1, 'L', b15, 'L', b16, 'M', b17, 'L', b11])
        B.addDartLine(['M', bD1.i, 'L', bD1, 'L', bD1.o, 'L', bD1.d, 'L', bD1.i])
        pth = (['M', b1, 'L', b13, 'L', b15, 'L', b17, 'L', b11, 'L', b10, 'C', b7, 'C', b5, 'L', b6, 'C', b1])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        #draw Shirt Sleeve C
        C.setLetter((c7.outpoint.x, c6.y), scaleby=12.0)
        C.setLabelPosition((c7.outpoint.x, c6.y + 2*CM))
        cG1 = dPnt((c3.outpoint.x, c1.y))
        cG2 = down(cG1, 0.75 * CD.undersleeve_length)
        C.addGrainLine(cG1, cG2)

        C.addGridLine(['M', c1, 'L', c2, 'M', c4, 'L', c5, 'M', c11, 'L', c12])
        pth = (['M', c3, 'C', c8, 'C', c2, 'L', c12, 'L', c10, 'L', c9, 'L', c11, 'L', c1, 'C', c7, 'C', c3])
        C.addSeamLine(pth)
        C.addCuttingLine(pth)

        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

