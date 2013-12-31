#!/usr/bin/env python
# patternName: Block Patterns - Women's - Spencer
# patternNumber: Blocks_W_Sp

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
        self.setInfo('patternNumber', 'Block_W_All_Spencer')
        self.setInfo('patternTitle', 'Blocks Women All - Spencer')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'S.L.Spencer')
        self.setInfo('patternmakerName', 'S.L.Spencer')
        self.setInfo('description', """Women's Block Patterns & variations""")
        #TODO: add new category 'Block Patterns'
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
        A = bodice.addPiece('Front_Waist_Bust_Darts', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = bodice.addPiece('Back', 'B', fabric = 2, interfacing = 0, lining = 0)
        C = bodice.addPiece('Sleeve', 'C', fabric = 2, interfacing = 0, lining = 0)
        D = bodice.addPiece('Front_Long', 'D', fabric = 2, interfacing = 0, lining = 0)
        E = bodice.addPiece('Back_Long', 'E', fabric = 2, interfacing = 0, lining = 0)
        F = bodice.addPiece('Front_Waist_Dart', 'F', fabric = 2, interfacing = 0, lining = 0)

        #Bodice Front (Waist  Bust Darts) A
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
        #TODO: create function pivot(pivot_point, rotation_angle, point_to_pivot) for slash_and_spread
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
        bD1 = B.addPoint('bD1', intersectLines(b2, b5, b8, b9)) #back waist dart point is at underarm height
        b12 = B.addPoint('b12', dPnt((bD1.x, b2.y))) # below dart point at waist
        bD1.i = B.addPoint('bD1.i', left(b12, distance(b2, b12)/5.0)) #dart inside leg
        bD1.o = B.addPoint('bD1.o', right(b12, distance(b12, bD1.i))) #dart outside leg
        b11 = B.addPoint('b11',  rightmostP(intersectCircles(b10, distance(a11, aD2.i) + distance(aD2.o, a16), bD1.o, CD.back_waist/2.0 - distance(b2, bD1.i)))) #back waist side
        #create curve at dart base
        ##adjustDartLength(a16, aD1, a2, extension=0.25) #smooth waistline curve from a16 to a2 at dart
        foldDart2(bD1, b2) #creates bD1.m, bD1.oc, bD1.ic; dart folds toward waist center b2

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
        #b/w bD1.o waist dart outside leg & b11 waist side
        bD1.o.addOutpoint(polar(bD1.o, distance(bD1.o, b11)/6.0, angleOfLine(bD1.o, bD1) + ANGLE180 - angleOfVector(b2, bD1.i, bD1))) #short control handle, forms line with control handle for inside leg
        b11.addInpoint(polar(b11, distance(bD1.o, b11)/3.0, angleOfLine(b10, b11) + angleOfVector(aD2.o, a16, a16.inpoint))) #forms line with control handle for a16 front waist

        # Shirt sleeve C
        #get front & back armcye length
        back_armscye = points2List(b10, b10.outpoint, b7.inpoint, b7, b7.outpoint, b5.inpoint, b5)
        front_armscye = points2List(a11, a11.outpoint, a7.inpoint, a7, a7.outpoint, a5.inpoint, a5)
        ARMSCYE_LENGTH = curveLength(back_armscye) + curveLength(front_armscye)
        CAP_HEIGHT = ARMSCYE_LENGTH/3.0
        BICEP_WIDTH = 1.15 * CD.bicep #15% ease in bicep
        SLEEVE_LENGTH = CD.oversleeve_length
        WRIST_WIDTH = 1.15 * CD.wrist #15% ease in wrist

        c1 = C.addPoint('c1', (0,0)) #top of sleeve cap - A
        c2 = C.addPoint('c2', down(c1, SLEEVE_LENGTH)) #bottom of sleeve, mid-cuff - B
        c3 = C.addPoint('c3', down(c1, CAP_HEIGHT)) #bicep line - H
        c4 = C.addPoint('c4', midPoint(c3, c2))  #temporary elbow line - C
        c5 = C.addPoint('c5', up(c4, SLEEVE_LENGTH/20.0)) #elbow line
        c6 = C.addPoint('c6', right(c2, BICEP_WIDTH/2.0)) #back wrist reference - D
        c7 = C.addPoint('c7', left(c2, BICEP_WIDTH/2.0)) #font wrist reference - E
        c10 = C.addPoint('c10', right(c3, BICEP_WIDTH/2.0)) #back underarm - J
        c12 = C.addPoint('c12', left(c3, BICEP_WIDTH/2.0)) #front underarm - L
        #wrist
        c16 = C.addPoint('c16', left(c6, WRIST_WIDTH/4.0)) #temporary back wrist
        c17 = C.addPoint('c17', right(c7, WRIST_WIDTH/4.0)) #temporary front wrist
        c20 = C.addPoint('c20', polar(c10, distance(a10, a7), angleOfLine(c10, c16) + angleOfVector(a10, a11, a7)))
        c21 = C.addPoint('c21', polar(c12, distance(b10, b7), angleOfLine(c12, c17) - angleOfVector(b11, b10, b7)))
        #elbow
        c26 = C.addPoint('c26', onLineAtY(c10, c16, c5.y)) #back elbow
        c27 = C.addPoint('c27', onLineAtY(c12, c17, c5.y)) #front elbow 1
        c28 = C.addPoint('c28', polar(c26, distance(c26, c27), angleOfLine(c26, c27) - angleOfDegree(5))) #front elbow 2
        c29 = C.addPoint('c29', polar(c26, distance(c26, c17), angleOfLine(c26, c17) - angleOfDegree(5))) #front wrist
        c30 = C.addPoint('c30', polar(c26, distance(c26, c16), angleOfLine(c26, c16) - angleOfDegree(5))) #back wrist
        c31 = C.addPoint('c31', midPoint(c5, c27)) # elbow dart point
        #elbow dart
        cD1 = C.addPoint('cD1', dPnt(c31)) #elbow dart point
        cD1.i = C.addPoint('cD1.i', dPnt(c27)) #elbow dart inside
        cD1.o = C.addPoint('cD1.o', onLineAtLength(c31, c28, distance(c31, c27))) #elbow dart outside
        foldDart2(cD1, c12) #elbow dart folds up towards c12 back underarm point

        #Sleeve C control points
        #b/w c1 sleeve cap to c20 front armcap to c10 front underarm
        c1.addOutpoint(right(c1, abs(c10.x - c1.x)/3.0))
        c10.addInpoint(polar(c10, distance(c20, c10)/3.0, angleOfLine(c26, c10) - ANGLE90))
        c20.addOutpoint(polar(c20, distance(c20, c10)/3.0, angleOfLine(c20, c10.inpoint)))
        c20.addInpoint(polar(c20, distance(c20, c1)/3.0, angleOfLine(c20.outpoint, c20)))
        #b/w c12 back underarm to c9 back armcap to c1 sleeve cap
        c1.addInpoint(left(c1, abs(c12.x - c1.x)/3.0))
        c21.addOutpoint(polar(c21, distance(c21, c1)/3.0, angleOfLine(c21, c1.inpoint)))
        c21.addInpoint(polar(c21, distance(c12, c21)/3.0, angleOfLine(c21.outpoint, c21)))
        c12.addOutpoint(polar(c12, distance(c12, c21)/3.0, angleOfLine(cD1.i, c12) + ANGLE90))

        #Bodice (Long) Front D
        d1 = D.addPoint('d1', down(a2, CD.front_hip_height)) #front hip center
        d2 = D.addPoint('d2', left(aD1.o, distance(aD1.o, a16))) #front waist side
        d3 = D.addPoint('d3', (aD1.x, d1.y)) #reflect waist dart point on hip line for 'fish dart'
        d4 = D.addPoint('d4', left(d1, CD.front_hip/2.0)) #temporary front hip side
        d5 = D.addPoint('d5', leftmostP(intersectCircles(d3, distance(d3, d4), a16, CD.side_hip_height))) #front hip side
        dD1 = D.addPoint('dD1', aD1) #front waist dart point at bust
        dD1.i = D.addPoint('dD1.i', (aD1.i)) #front waist dart inside at waist
        dD1.o = D.addPoint('dD1.o', (aD1.o)) #front waist dart outside at waist
        dD1.d = D.addPoint('dD1.d', up(d3, distance(d3, a13)/7.0)) #front waist dart point at hip

        #Bodice Back (Long) E
        e1 = E.addPoint('e1', down(b2, CD.back_hip_height)) #back hip center
        e2 = E.addPoint('e2', right(bD1.o, distance(bD1.o, b11))) #back waist side
        e3 = E.addPoint('e3', (bD1.x, e1.y)) # back waist dart at hip line
        e4 = E.addPoint('e4', right(e1, CD.back_hip/2.0)) #temporary back hip side
        e5 = E.addPoint('e5', rightmostP(intersectCircles(e3, distance(e3, e4), b11, CD.side_hip_height))) #back waist side
        eD1 = E.addPoint('eD1', (bD1)) #back waist dart point at underarm
        eD1.i = E.addPoint('eD1.i', (bD1.i)) #back waist dart inside at waist
        eD1.o = E.addPoint('eD1.o', (bD1.o)) #back waist dart outside at waist
        eD1.d = E.addPoint('eD1.d', up(e3, distance(e3, b12)/7.0)) # back waist dart point at hip

        #Bodice Front (Waist Dart) F
        #---dart---
        #front waist dart
        totalDartAngle = abs(angleOfVector(a12, a4, a15))
        frontWaistDartAngle = totalDartAngle
        fD1 = F.addPoint('fD1', (a4)) #front waist dart point
        fD1.i = F.addPoint('fD1.i', onRayAtY(a4, ANGLE90 - frontWaistDartAngle/3.0, a2.y)) #front waist dart inside leg
        fD1.o = F.addPoint('fD1.o', onRayAtY(a4, ANGLE90 + 2 * frontWaistDartAngle/3.0, a2.y)) #front waist dart outside leg
        f16 = F.addPoint('f16', a15) #front waist side created after all darts defined
        #create curve at dart base
        ##adjustDartLength(f16, fD1, a2, extension=0.25) #smooth waistline curve from f16 to a2 at dart
        foldDart2(fD1, a2) #creates fD1.m, fD1.oc, fD1.ic; dart folds in toward waist center a2
        #adjust fD1 away from a4 bust point
        (fD1.x, fD1.y) = down(a4, distance(fD1, fD1.i)/7.0)

        #Bodice Front F control points
        #b/w fD1.o waist dart outside leg & f16 front waist side - short control handles
        fD1.o.addOutpoint(polar(fD1.o, distance(fD1.o, f16)/6.0, angleOfLine(fD1.o, fD1) - (angleOfLine(fD1.i, fD1) - ANGLE180))) #control handle forms line with a2,fD1.i
        f16.addInpoint(polar(f16, distance(fD1.o, f16)/6.0, angleOfLine(f16, fD1.o.outpoint))) #f16 control handle points to fD1.o control handle

        #draw Bodice Front (Waist & Bust Darts) A
        pnt1 = dPnt(midPoint(a7, a8))
        A.setLabelPosition((pnt1))
        A.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        aG1 = dPnt(left(a8, distance(a8, pnt1)/4.0))
        aG2 = dPnt(down(aG1, distance(a1, a2)/2.0))
        A.addGrainLine(aG1, aG2)
        A.addGridLine(['M', a1, 'L', a2, 'L', a5, 'M', a8, 'L', a9, 'M', a1, 'L', a5, 'M', a3, 'L', a4, 'M', a2, 'L', a12, 'M', a4, 'L', a6, 'L', a7, 'M', a11, 'L', a15, 'M', a4, 'L', a10, 'M', a14, 'L', a4, 'L', a13])
        A.addDartLine(['M', aD1.ic, 'L', aD1, 'L', aD1.oc, 'M', aD2.ic, 'L', aD2, 'L', aD2.oc])
        pth = (['M', a1, 'L', a2, 'L', aD1.i, 'L', aD1.m, 'L', aD1.o, 'C', a16, 'L', aD2.o, 'L', aD2.m, 'L', aD2.i, 'L', a11, 'C', a7, 'C', a5, 'L', a6, 'C', a1])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        #draw Bodice Back B
        pnt1 = dPnt((distance(b3, b6)/2.0, distance(b1, b8)/2.0))
        B.setLabelPosition((pnt1))
        B.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        bG1 = dPnt((distance(b3, b6)/4.0, distance(b1, b8)/4.0))
        bG2 = dPnt(down(bG1, distance(b1, b2)/2.0))
        B.addGrainLine(bG1, bG2)
        B.addGridLine(['M', b6, 'L', b3, 'L', b2, 'L', b4, 'M', b1, 'L', b5, 'M', b2, 'L', b5, 'M', b6, 'L', b7, 'M', b8, 'L', b9, 'M',  bD1, 'L', b12])
        B.addDartLine(['M', bD1.ic, 'L', bD1, 'L', bD1.oc])
        pth = (['M', b1, 'L', b2, 'L', bD1.i, 'L', bD1.m, 'L', bD1.o, 'C', b11, 'L', b10, 'C', b7, 'C', b5, 'L', b6, 'C', b1])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        # Shirt Sleeve C
        cG1 = dPnt((c3))
        cG2 = down(cG1, SLEEVE_LENGTH/2.0)
        C.addGrainLine(cG1, cG2)
        C.setLetter((c21.x, c3.y), scaleby=15.0)
        C.setLabelPosition((c21.x, c3.y + 2*CM))
        C.addGridLine(['M', c1, 'L', c2, 'M', c10, 'L', c12, 'M', c26, 'L', c27, 'M', c6, 'L', c7, 'M', c16,  'L', c10,  'L', c6, 'M', c17, 'L', c12, 'L', c7])
        #TODO: change function def to addDartLine(cD1) -- only one parameter needed
        C.addDartLine(['M', cD1.ic, 'L', cD1, 'L', cD1.oc])
        #pth = (['M', c10, 'L', c13, 'L', c15, 'L', c17, 'L', c1, 'L', c21, 'L', c21, 'L', c23, 'L', c12,  'L', cD1.i,  'L', cD1.m,  'L', cD1.o, 'L', c29,  'L', c30,  'L',  c26, 'L', c10])
        pth = (['M', c1, 'C', c20, 'C', c10, 'L', c26, 'L', c30, 'L', c29, 'L', cD1.o, 'L', cD1.m, 'L', cD1.i,  'L', c12,  'C', c21,  'C', c1])
        C.addSeamLine(pth)
        C.addCuttingLine(pth)

        #draw Bodice (Long) Front D
        pnt1 = dPnt(midPoint(a7, a8))
        D.setLabelPosition((pnt1))
        D.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        dG1 = dPnt((aG1))
        dG2 = dPnt(down(dG1, distance(a1, e1)/2.0))
        D.addGrainLine(dG1, dG2)
        D.addGridLine(['M', a1, 'L', a2, 'L', a5, 'M', a8, 'L', a9, 'M', a1, 'L', a5, 'M', a3, 'L', a4, 'M', a2, 'L', a12, 'M', a4, 'L', a6, 'L', a7, 'M', a11, 'L', a15, 'M', a4, 'L', a10, 'M', a14, 'L', a4, 'L', d3, 'M', d1, 'L', d4, 'M', d2, 'L', dD1.o, 'L', a16, 'M', d5, 'L', a16])
        D.addDartLine(['M', dD1.i, 'L', dD1, 'L', dD1.o, 'L', dD1.d, 'L', dD1.i, 'M', aD2.ic, 'L', aD2, 'L', aD2.oc])
        pth = (['M', a1, 'L', d1, 'L', d3, 'L', d5, 'L', a16, 'L', aD2.o, 'L', aD2.m, 'L', aD2.i, 'L', a11, 'C', a7, 'C', a5, 'L', a6, 'C', a1])
        D.addSeamLine(pth)
        D.addCuttingLine(pth)

        #draw Bodice (Long) Back E
        pnt1 = dPnt((distance(b3, b6)/2.0, distance(b1, b8)/2.0))
        E.setLabelPosition((pnt1))
        E.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        eG1 = dPnt(bG1)
        eG2 = dPnt(down(eG1, distance(b1, e1)/2.0))
        E.addGrainLine(eG1, eG2)
        E.addGridLine(['M', b6, 'L', b3, 'L', b2, 'L', e2, 'M', bD1.o, 'L', b11, 'M', b1, 'L', b5, 'M', b2, 'L', b5, 'M', b6, 'L', b7, 'M', b8, 'L', b9, 'M',  bD1, 'L', e3, 'L', e4, 'M', e5, 'L', b11])
        E.addDartLine(['M', eD1.i, 'L', eD1, 'L', eD1.o, 'L', eD1.d, 'L', eD1.i])
        pth = (['M', b1, 'L', e1, 'L', e3, 'L', e5, 'L', b11, 'L', b10, 'C', b7, 'C', b5, 'L', b6, 'C', b1])
        E.addSeamLine(pth)
        E.addCuttingLine(pth)

        #draw Bodice Front (Waist Dart) F
        pnt1 = dPnt(midPoint(a7, a8))
        F.setLabelPosition((pnt1))
        F.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        fG1 = dPnt(left(a8, distance(a8, pnt1)/4.0))
        fG2 = dPnt(down(fG1, distance(a1, a2)/2.0))
        F.addGrainLine(fG1, fG2)
        F.addGridLine(['M', a1, 'L', a2, 'L', a5, 'M', a8, 'L', a9, 'M', a1, 'L', a5, 'M', a3, 'L', a4, 'M', a2, 'L', a12, 'M', a4, 'L', a6, 'L', a7, 'M', a11, 'L', a15, 'M', a4, 'L', a10, 'M', a14, 'L', a4, 'L', a13])
        F.addDartLine(['M', fD1.ic, 'L', fD1, 'L', fD1.oc])
        pth = (['M', a1, 'L', a2, 'L', fD1.i, 'L', fD1.m, 'L', fD1.o, 'C', f16, 'L', a11, 'C', a7, 'C', a5, 'L', a6, 'C', a1])
        F.addSeamLine(pth)
        F.addCuttingLine(pth)

        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

