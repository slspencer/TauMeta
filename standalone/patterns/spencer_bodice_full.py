#!/usr/bin/env python
# patternName: Spencer_bodice
# patternNumber: W_Bl_B_1

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
        self.setInfo('patternNumber', 'W_Block_Bodice_1')
        self.setInfo('patternTitle', 'Spencer Bodice Block')
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

        #Bodice Front A
        a1 = A.addPoint('a1', (0.0, 0.0)) #front neck center
        a2 = A.addPoint('a2', down(a1, CD.front_waist_length)) #front waist center
        a3 = A.addPoint('a3', up(a2, CD.bust_length)) #bust center
        a4 = A.addPoint('a4', left(a3, CD.bust_distance/2.0)) #bust point
        a5 = A.addPoint('a5', leftmostP(intersectCircles(a2, CD.front_shoulder_balance, a1, CD.front_shoulder_width))) #front shoulder point
        a6 = A.addPoint('a6', highestP(intersectCircles(a5, CD.shoulder, a4, CD.bust_balance))) #front neck point
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

        #---darts---
        #front waist dart
        totalDartAngle = abs(angleOfVector(a12, a4, a15))
        frontWaistDartAngle = totalDartAngle/2.0
        bustDartAngle = totalDartAngle/2.0
        ac1 = A.addPoint('ac1', (a4)) #front waist dart point
        ac1.i = A.addPoint('ac1.i', onRayAtY(a4, ANGLE90 - frontWaistDartAngle/2.0, a2.y)) #front waist dart inside leg
        ac1.o = A.addPoint('ac1.o', onRayAtY(a4, ANGLE90 + frontWaistDartAngle/2.0, a2.y)) #front waist dart outside leg
        #bust dart
        aD2 = A.addPoint('aD2', (a4)) #bust dart point
        aD2.i = A.addPoint('aD2.i', intersectLineRay(a9, a10, a4, ANGLE180 + bustDartAngle/2.0)) #bust dart inside leg
        aD2.o = A.addPoint('aD2.o', polar(a4, distance(a4, aD2.i), ANGLE180 - bustDartAngle/2.0)) #bust dart outside leg
        #TODO: create function pivot(pivot_point, rotation_angle, point_to_pivot)

        #finalize front waist side
        remainingSideSegment = distance(a11, a15) - distance(a11, aD2.i)
        remainingWaistSegment = distance(a2, a12) - distance(a2, ac1.i)
        a16 = A.addPoint('a16', leftmostP(intersectCircles(aD2.o, remainingSideSegment, ac1.o, remainingWaistSegment))) #front waist side created after all darts defined

        #create curve at dart base
        ##adjustDartLength(a16, ac1, a2, extension=0.25) #smooth waistline curve from a16 to a2 at dart
        foldDart2(ac1, a2) #creates ac1.m,ac1.oc,ac1.ic; dart folds in toward waist center a2
        #do not call adjustDartLength(a12,aD2,a11) -- bust dart aD2 is not on a curve
        foldDart2(aD2, a11) #creates aD2.m,aD2.oc,aD2.ic; dart folds up toward underarm side a11
        #adjust ac1 & aD2
        (ac1.x, ac1.y) = down(ac1, distance(ac1, ac1.i)/7.0)
        (aD2.x, aD2.y) = left(aD2, distance(aD2, aD2.i)/7.0)

        #Bodice Front A control points
        #b/w a6 front neck point & a1 front neck center
        a6.addOutpoint(down(a6, abs(a1.y - a6.y)/2.0))
        a1.addInpoint(left(a1, 0.75 * abs(a1.x - a6.x)))
        #b/w ac1.o waist dart outside leg & a16 front waist side - short control handles
        ac1.o.addOutpoint(polar(ac1.o, distance(ac1.o, a16)/6.0, angleOfLine(ac1.o, ac1) - (angleOfLine(ac1.i, ac1) - ANGLE180))) #control handle forms line with a2,ac1.i
        a16.addInpoint(polar(a16, distance(ac1.o, a16)/6.0, angleOfLine(a16, ac1.o.outpoint))) #a16 control handle points to ac1.o control handle
        #b/w a7 front underarm point & a5 front shoulder point
        a5.addInpoint(polar(a5, distance(a7, a5)/6.0, angleOfLine(a5, a6) + ANGLE90)) #short control handle perpendicular to shoulder seam
        a7.addOutpoint(polar(a7, distance(a7, a5)/3.0, angleOfLine(a7, a6))) #control handle points to front neck point
        #b/w a11 front underarm side & a7 front underarm point
        a7.addInpoint(polar(a7, distance(a11, a7)/3.0, angleOfLine(a6, a7)))
        a11.addOutpoint(polar(a11, distance(a11, a7)/3.0, angleOfLine(aD2.i, a11) + ANGLE90)) #control handle is perpendicular to side seam at underarm

        #Bodice Back B
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
        bc1 = B.addPoint('bc1', intersectLines(b2, b5, b8, b9)) #back waist dart point is at underarm height
        b12 = B.addPoint('b12', dPnt((bc1.x, b2.y))) # below dart point at waist
        bc1.i = B.addPoint('bc1.i', left(b12, distance(b2, b12)/5.0)) #dart inside leg
        bc1.o = B.addPoint('bc1.o', right(b12, distance(b12, bc1.i))) #dart outside leg
        b11 = B.addPoint('b11',  rightmostP(intersectCircles(b10, distance(a11, a16), bc1.o, CD.back_waist/2.0 - distance(b2, bc1.i)))) #back waist side
        #create curve at dart base
        ##adjustDartLength(a16, ac1, a2, extension=0.25) #smooth waistline curve from a16 to a2 at dart
        foldDart2(bc1, b2) #creates bc1.m, bc1.oc, bc1.ic; dart folds toward waist center b2

        #Bodice Back B control points
        #b/w b6 back neck point & b1 back neck center
        b1.addInpoint(right(b1, 0.75 * abs(b1.x - b6.x)))
        b6.addOutpoint(polar(b6, abs(b6.y - b1.y)/2.0, angleOfLine(b6, b5) + ANGLE90)) #perpendicular to shoulder seam
        #b/w b10 underarm point & b7 underarm curve
        b10.addOutpoint(polar(b10, distance(b10, b7)/3.0, angleOfLine(b10, b11) + ANGLE90)) #perpendicular to side seam
        b7.addInpoint(polar(b7, distance(b10, b7)/3.0, angleOfLine(b6, b7)))
        #b/w b7 underarm curve & b6 shoulder point
        b7.addOutpoint(polar(b7, distance(b7, b5)/3.0, angleOfLine(b7, b6)))
        b5.addInpoint(polar(b5, distance(b7, b5)/6.0, angleOfLine(b6, b5) + ANGLE90)) #short control handle, perpendicular to shoulder seam
        #b/w bc1.o waist dart outside leg & b11 waist side
        bc1.o.addOutpoint(polar(bc1.o, distance(bc1.o, b11)/6.0, angleOfLine(bc1.o, bc1) + ANGLE180 - angleOfVector(b2, bc1.i, bc1))) #short control handle, forms line with control handle for inside leg
        b11.addInpoint(polar(b11, distance(bc1.o, b11)/3.0, angleOfLine(b10, b11) + angleOfVector(aD2.o, a16, a16.inpoint))) #forms line with control handle for a16 front waist

        # Shirt sleeve C
        #get front & back armcye length
        back_armscye = points2List(b10, b10.outpoint, b7.inpoint, b7, b7.outpoint, b5.inpoint, b5)
        front_armscye = points2List(a11, a11.outpoint, a7.inpoint, a7, a7.outpoint, a5.inpoint, a5)
        ARMSCYE_LENGTH = curveLength(back_armscye) + curveLength(front_armscye)

        c1 = C.addPoint('c1', (0.0, 0.0)) #midpoint of sleevecap - top of sleeve
        c2 = C.addPoint('c2', (c1.x, c1.y + ARMSCYE_LENGTH/4.0 + 1.5*CM)) #middle bicep line
        c3 = C.addPoint('c3', (c1.x, c1.y + CD.oversleeve_length + 6*CM)) #wrist line
        c4 = C.addPoint('c4', midPoint(c2, c3)) #middle elbow line
        c5 = C.addPoint('c5', (c2.x - (ARMSCYE_LENGTH/2.0 - 0.5*CM), c2.y)) #back bicep line
        c6 = C.addPoint('c6', (c5.x, c3.y)) #back wrist line
        c7 = C.addPoint('c7', (c2.x + (ARMSCYE_LENGTH/2.0 - 0.5*CM), c2.y)) #front bicep line
        c8 = C.addPoint('c8', (c7.x, c3.y)) #front wrist line
        #back armscye points
        c9 = C.addPoint('c9', onLineAtLength(c5, c1, distance(c5, c1)/4.0)) #back armscye point 1
        c10 = C.addPoint('c10', polar(midPoint(c5, c1), 1*CM, angleOfLine(c5, c1) - ANGLE90)) #back armscye point 2
        pnt = onLineAtLength(c5, c1, 0.75*distance(c5, c1))
        c11 = C.addPoint('c11', polar(pnt, 2*CM, angleOfLine(c5, c1) - ANGLE90)) #back armcye point 3
        #front armscye points
        pnt = onLineAtLength(c7, c1, distance(c7, c1)/4.0)
        c12 = C.addPoint('c12', polar(pnt, 1*CM, angleOfLine(c7, c1) - ANGLE90)) #front armscye point 1
        c13 = C.addPoint('c13', midPoint(c7, c1)) #front armscye point 2
        pnt = onLineAtLength(c7, c1, 0.75*distance(c7, c1))
        c14 = C.addPoint('c14', polar(pnt, 1*CM, angleOfLine(c7, c1) + ANGLE90)) #front armscye point 3
        #c15 = C.addPoint('c15', onLineAtLength(c6, c3, distance(c6, c3)/3.0)) #back wrist point
        #c16 = C.addPoint('c16', onLineAtLength(c8, c3, distance(c8, c3)/3.0)) #front wrist point
        c15 = C.addPoint('c15', onLineAtLength(c3, c6, 0.7 * CD.wrist)) #back wrist point
        c16 = C.addPoint('c16', onLineAtLength(c3, c8, 0.7 * CD.wrist)) #front wrist point
        c17 = C.addPoint('c17', midPoint(c6,c15)) #wristline reference point
        c18 = C.addPoint('c18', midPoint(c8,c16)) #wristline reference point
        #c19 = C.addPoint('c19', midPoint(c3,c15)) #slashline reference point
        #c20 = C.addPoint('c20', (c19.x, c19.y - 15*CM)) #top of slashline
        #c21 = C.addPoint('c21', (c19.x, c19.y + 1*CM)) #bottom of slashline
        #c22 = C.addPoint('c22', onLineAtY(c5, c17, c4.y)) #back elbow
        #c23 = C.addPoint('c23', onLineAtY(c7, c18, c4.y)) #front elbow
        c22 = C.addPoint('c22', left(c4, 0.55 * CD.elbow)) #back elbow
        c23 = C.addPoint('c23', right(c4, 0.55 * CD.elbow)) #front elbow
        c24 = C.addPoint('c24', midPoint(c2, c4)) #middle of sleeve - label reference point
        #c25 = C.addPoint('c25', down(c21, SEAM_ALLOWANCE)) #extend slashline out to cuttingline

        #Shirt Sleeve D control points
        cArray = points2List(c5, c9, c10, c11, c1, c14, c13, c12, c7)
        C1, C2 = controlPoints('sleeve_cap', cArray)
        c5.addOutpoint(C1[0])
        c9.addInpoint(C2[0])
        c9.addOutpoint(C1[1])
        c10.addInpoint(C2[1])#
        c10.addOutpoint(C1[2])
        c11.addInpoint(C2[2])
        c11.addOutpoint(C1[3])
        c1.addInpoint(C2[3])
        c1.addOutpoint(C1[4])
        c14.addInpoint(C2[4])
        c14.addOutpoint(C1[5])
        c13.addInpoint(C2[5])
        c13.addOutpoint(C1[6])
        c12.addInpoint(C2[6])
        c12.addOutpoint(C1[7])
        c7.addInpoint(C2[7])
        cArray = points2List(c15, c22, c5)
        C1, C2 = controlPoints('sleeve_seam1', cArray)
        c15.addOutpoint(C1[0])
        c22.addInpoint(C2[0])
        c22.addOutpoint(C1[1])
        c5.addInpoint(C2[1])
        cArray = points2List(c7, c23, c16)
        C1, C2 = controlPoints('sleeve_seam2', cArray)
        c7.addOutpoint(C1[0])
        c23.addInpoint(C2[0])
        c23.addOutpoint(C1[1])
        c16.addInpoint(C2[1])
        #b/w c16 front wrist & c15 back wrist
        c16.addOutpoint(polar(c16, distance(c16, c15)/3.0, angleOfLine(c16.inpoint, c16) + ANGLE90)) #handle is perpendicular to sleeve seam
        c15.addInpoint(polar(c15, distance(c16, c15)/3.0, angleOfLine(c15.outpoint, c15) - ANGLE90)) #handle is perpendicular to sleeve seam
        #cArray = points2List(c3, c21, c15)
        #C1, C2 = controlPoints('sleeve_placket', cArray)
        #c3.addOutpoint(C1[0])
        #c21.addInpoint(C2[0])
        #c21.addOutpoint(C1[1])
        #c15.addInpoint(C2[1])
        #b/w c16 front wrist & c3 mid wrist
        #c16.addOutpoint(polar(c16, distance(c16, c3)/6.0, angleOfLine(c16.inpoint, c16) + angleOfVector(c15.outpoint, c15, c15.inpoint))) #short control handle forms line with control handle c15-c15.inpoint at back wrist
        #c3.addInpoint(polar(c3, distance(c16, c3)/6.0, angleOfLine(c3.outpoint, c3))) #short control handle forms line with control handle c3.oupoint-c3 at mid-wrist

        #draw Bodice Front A
        pnt1 = dPnt(midPoint(a7, a8))
        A.setLabelPosition((pnt1))
        A.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)

        aG1 = dPnt(left(a8, distance(a8, pnt1)/4.0))
        aG2 = dPnt(down(aG1, distance(a1, a2)/2.0))
        A.addGrainLine(aG1, aG2)

        A.addGridLine(['M', a1, 'L', a2, 'L', a5, 'M', a8, 'L', a9, 'M', a1, 'L', a5, 'M', a3, 'L', a4, 'M', a2, 'L', a12, 'M', a4, 'L', a6, 'L', a7, 'M', a11, 'L', a15, 'M', a4, 'L', a10, 'M', a14, 'L', a4, 'L', a13])

        A.addDartLine(['M', ac1.ic, 'L', ac1, 'L', ac1.oc, 'M', aD2.ic, 'L', aD2, 'L', aD2.oc])

        pth = (['M', a1, 'L', a2, 'L', ac1.i, 'L', ac1.m, 'L', ac1.o, 'C', a16, 'L', aD2.o, 'L', aD2.m, 'L', aD2.i, 'L', a11, 'C', a7, 'C', a5, 'L', a6, 'C', a1])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        #draw Bodice Back B
        pnt1 = dPnt((distance(b3, b6)/2.0, distance(b1, b8)/2.0))
        B.setLabelPosition((pnt1))
        B.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)

        bG1 = dPnt((distance(b3, b6)/4.0, distance(b1, b8)/4.0))
        bG2 = dPnt(down(bG1, distance(b1, b2)/2.0))
        B.addGrainLine(bG1, bG2)

        B.addGridLine(['M', b6, 'L', b3, 'L', b2, 'L', b4, 'M', b1, 'L', b5, 'M', b2, 'L', b5, 'M', b6, 'L', b7, 'M', b8, 'L', b9, 'M',  bc1, 'L', b12])

        B.addDartLine(['M', bc1.ic, 'L', bc1, 'L', bc1.oc])

        pth = (['M', b1, 'L', b2, 'L', bc1.i, 'L', bc1.m, 'L', bc1.o, 'C', b11, 'L', b10, 'C', b7, 'C', b5, 'L', b6, 'C', b1])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        # Shirt Sleeve C
        Cg1 = dPnt((c2.x, c2.y))
        Cg2 = dPnt((Cg1.x, c3.y - 8*CM))
        C.addGrainLine(Cg1, Cg2)
        C.setLetter((c10.x, c24.y), scaleby=15.0)
        C.setLabelPosition((c10.x, c24.y + 2*CM))

        C.addGridLine(['M', c1,'L', c3, 'M', c7, 'L', c8, 'M', c5, 'L', c6, 'M', c5, 'L', c1, 'L',  c7, 'M', c5, 'L', c17, 'M', c22, 'L', c15, 'M', c7, 'L', c18, 'M', c23, 'L', c16, 'M', c5, 'L', c7,  'M', c22, 'L', c23, 'M', c6, 'L', c8])

        pth = (['M', c5, 'C', c9, 'C', c10, 'C', c11, 'C', c1, 'C', c14, 'C', c13, 'C', c12, 'C', c7, 'C', c23, 'C', c16, 'C', c15, 'C', c22, 'C', c5])
        C.addSeamLine(pth)
        C.addCuttingLine(pth)

        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

