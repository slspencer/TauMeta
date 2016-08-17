#!/usr/bin/env python
# patternName: Block Women Bodice-Long - Spencer
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
        self.setInfo('patternTitle', 'Block Women Bodice-Long - Spencer')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'S.L.Spencer')
        self.setInfo('patternmakerName', 'S.L.Spencer')
        self.setInfo('description', """Bodice block, extended to hipline, with sleeves""")
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
        self.setInfo('yearstart', '1920' )
        self.setInfo('yearend', '')
        self.setInfo('culture', 'European')
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
        A = bodice.addPiece('Bodice Front', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = bodice.addPiece('Bodice Back', 'B', fabric = 2, interfacing = 0, lining = 0)
        C = bodice.addPiece('Sleeve', 'C', fabric = 2, interfacing = 0, lining = 0)

        #Bodice Front (Waist  Bust Darts) A
        a1 = A.addPoint('a1', (0.0, 0.0)) #front neck center
        a2 = A.addPoint('a2', down(a1, CD.front_waist_length)) #front waist center
        a3 = A.addPoint('a3', up(a2, CD.bust_length)) #bust center
        a4 = A.addPoint('a4', left(a3, CD.bust_distance/2.0)) #bust point
        a5 = A.addPoint('a5', highestP(onCircleAtX(a2, CD.front_shoulder_balance, a1.x - CD.front_shoulder_width/2.0))) #front shoulder tip
        a6 = A.addPoint('a6', highestP(intersectCircles(a5, CD.shoulder, a4, CD.bust_balance))) #front neck point
        a7 = A.addPoint('a7', lowestP(onCircleAtX(a6, CD.front_underarm_balance, a1.x - CD.across_chest/2.0))) #front underarm point
        a8 = A.addPoint('a8', (a1.x, a7.y)) #front undearm center
        a9 = A.addPoint('a9', left(a8, CD.front_underarm/2.0)) #front underarm side
        a10 = A.addPoint('a10', leftmostP(tangentPointOnCircle(a4, CD.front_bust/2.0 - distance(a3, a4), a9))) #bust side is where line from bust point is perpendicular to line through a9
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
        #finalize waist dart
        aD1.d = A.addPoint('aD1.d', up(a20, distance(a20, a13)/7.0)) #front waist dart point at hip

        #create curve at dart base
        ##adjustDartLength(a16, aD1, a2, extension=0.25) #smooth waistline curve from a16 to a2 at dart
        foldDart(aD1, a2) #creates aD1.m,aD1.oc,aD1.ic; dart folds in toward waist center a2
        #do not call adjustDartLength(a12,aD2,a11) -- bust dart aD2 is not on a curve
        foldDart(aD2, a11) #creates aD2.m,aD2.oc,aD2.ic; dart folds up toward underarm side a11
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
        b5 = B.addPoint('b5', highestP(onCircleAtX(b2, CD.back_shoulder_balance, b1.x + CD.back_shoulder_width/2.0))) #back shoulder tip
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
        #Bodice Back hip extension
        b13 = B.addPoint('b13', down(b2, CD.back_hip_height)) #back hip center
        b14 = B.addPoint('b14', right(bD1.o, distance(bD1.o, b11))) #back waist side
        b15 = B.addPoint('b15', (bD1.x, b13.y)) # back waist dart at hip line
        b16 = B.addPoint('b16', right(b13, CD.back_hip/2.0)) #temporary back hip side
        b17 = B.addPoint('b17', rightmostP(intersectCircles(b15, distance(b15, b16), b11, CD.side_hip_height))) #back waist side
        #complete Back waist dart
        bD1.d = B.addPoint('bD1.d', up(b15, distance(b15, b12)/7.0)) # back waist dart point at hip
        #create curve at dart base
        foldDart(bD1, b2) #creates bD1.m, bD1.oc, bD1.ic; dart folds toward waist center b2

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

        #---Sleeve C---#
        SCM = C.addPoint('SCM',(0, 0) ) #sleeve cap middle
        SWM = C.addPoint('SWM', down(SCM, CD.oversleeve_length)) #sleeve wrist middle
        SBM1 = C.addPoint('SBM1', up(SWM, CD.undersleeve_length)) #sleeve bicep middle
        SEM = C.addPoint('SEM', down(SBM1, 0.45 * CD.undersleeve_length)) #sleeve elbow middle

        SBF1 = C.addPoint('SBF1', left(SBM1, 0.5 * CD.bicep)) #sleeve bicep front 1
        SBB1 = C.addPoint('SBB1', right(SBM1, 0.5 * CD.bicep)) #sleeve bicep back 1

        SBM = C.addPoint('SBM', up(SBM1, 0.15 * distance(SBM1, SCM))) #sleeve bicep middle
        SBF = C.addPoint('SBF', leftmostP(onCircleAtY(SCM, distance(SCM, SBF1), SBM.y))) #sleeve bicep front
        SBB = C.addPoint('SBB', rightmostP(onCircleAtY(SCM, distance(SCM, SBB1), SBM.y))) #sleeve bicep front

        SCF1 = C.addPoint('SCF1', right(SBF, 0.25 * distance(SBF, SBM))) #sleeve cap front 1
        SCF4 = C.addPoint('SCF4', left(SCM, distance(SBF, SCF1))) #sleeve cap front 4 - to left of SCM
        SCF2 = C.addPoint('SCF2', onLineAtLength(SCF1, SCF4, distance(SBF, SCF1))) #sleeve cap front 2
        SCF3 = C.addPoint('SCF3', onLineAtLength(SCF4, SCF1, distance(SCM, SCF4))) #sleeve cap front 3

        SCB4 = C.addPoint('SCB4', left(SBB, 0.5 * distance(SBF, SCF1))) #sleeve cap back 4
        SCB1 = C.addPoint('SCB1', right(SCM, distance(SBF, SCF1) + distance(SBB, SCB4))) # sleeve cap back 1 - ro right of SCM
        SCB2 = C.addPoint('SCB2', onLineAtLength(SCB1, SCB4, distance(SCM, SCB1))) # sleeve cap back 2
        SCB3 = C.addPoint('SCB3', onLineAtLength(SCB4, SCB1, distance(SBB, SCB4))) #sleeve cap back 3

        SEF = C.addPoint('SEF', left(SEM, 0.5 * CD.elbow)) #sleeve elbow front
        SEB = C.addPoint('SEB', right(SEM, 0.5 * CD.elbow)) #sleeve elbow back
        SEB1 = C.addPoint('SEB1', midPoint(SEM, SEB)) #midpoint b/w SEM & SEB

        SWF1 = C.addPoint('SWF1', left(SWM, 0.5 * CD.wrist)) #sleeve wrist forward 1
        SWM1 = C.addPoint('SWM1', rightmostP(tangentPointOnCircle(SWF1, 0.5 * CD.wrist, SEB1))) #sleeve wrist middle 1 - extend down wrist middle point
        SWB = C.addPoint('SWB', extendLine(SWF1, SWM1, 0.25 * CD.wrist)) #sleeve wrist back
        SWF2 = C.addPoint('SWF2', midPoint(SWF1, SWM1)) #sleeve wrist front 2 - begin wrist curve
        SWF = C.addPoint('SWF', leftmostP(onCircleAtY(SWF1, 0.25 * CD.wrist, SWF2.y))) #sleeve wrist front
        #sleeve elow darts
        sleeve_diff = (distance(SBB, SEB) + distance(SEB, SWB)) - (distance(SBF, SEF) + distance(SEF, SWF))
        dart_width = sleeve_diff / 3.0
        dart_length = 0.4 * distance(SEB, SEM)
        SD1 = C.addPoint('SD1', onLineAtLength(SEB, SBB, 2 * dart_width))
        SD2 = C.addPoint('SD2', onLineAtLength(SEB, SWB, 0.5 * dart_width))
        SD3 = C.addPoint('SD3', onLineAtLength(SEB, SWB, 2.5 * dart_width))
        SD1.i = C.addPoint('SD1.i', SD1)
        SD1.o = C.addPoint('SD1.o', onLineAtLength(SD1.i, SEB, dart_width))
        SD1.m = midPoint(SD1.i, SD1.o)
        updatePoint(SD1, polar(SD1.m, dart_length, angleOfLine(SD1.i, SD1.o) + ANGLE90))
        extendDart(SEB, SD1, SBB)
        foldDart(SD1, SBB)
        SD2.i = C.addPoint('SD2.i', SD2)
        SD2.o = C.addPoint('SD2.o', onLineAtLength(SD2.i, SWB, dart_width))
        SD2.m = midPoint(SD2.i, SD2.o)
        updatePoint(SD2, polar(SD2.m, dart_length, angleOfLine(SD2.i, SD2.o) + ANGLE90))
        extendDart(SWB, SD2, SD1.o)
        foldDart(SD2, SD1.o)
        SD3.i = C.addPoint('SD3.i', SD3)
        SD3.o = C.addPoint('SD3.o', onLineAtLength(SD3.i, SWB, dart_width))
        SD3.m = midPoint(SD3.i, SD3.o)
        updatePoint(SD3, polar(SD3.m, dart_length, angleOfLine(SD3.i, SD3.o) + ANGLE90))
        extendDart(SWB, SD3, SD2.o)
        foldDart(SD3, SD2.o)

        #---sleeve control points
        #b/w SBF & SCM - front sleeve cap
        SBF.addOutpoint(right(SBF, 0.4 * abs(SBF.x - SCM.x)))
        SCM.addInpoint(left(SCM, 0.5 * abs(SBF.x - SCM.x)))
        #b/w SCM & SCB3 - upper back sleeve cap
        SCM.addOutpoint(right(SCM, 0.3 * distance(SCM, SCB3)))
        SCB3.addInpoint(onLineAtLength(SCB3, SCB1, 0.3 * distance(SCM, SCB3)))
        #b/w SCB3 & SBB - lower back sleeve cap
        SCB3.addOutpoint(SCB4)
        SBB.addInpoint(SCB4)
        #b/w SWF2 & SWF - front wrist curve
        SWF2.addOutpoint(onLineAtLength(SWF2, SWF1, distance(SWF2, SWF) / 3.0))
        SWF.addInpoint(onLineAtLength(SWF, SWF1, distance(SWF2, SWF) / 3.0))

        #draw Bodice Front A
        pnt1 = dPnt(midPoint(a7, a8))
        A.setLabelPosition((pnt1))
        A.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        aG1 = dPnt(left (a1, distance(a1, a6)/3.0))
        aG2 = dPnt(down(aG1, distance(a1, a18)/2.0))
        A.addGrainLine(aG1, aG2)
        A.addGridLine(['M', a1, 'L', a2, 'L', a5, 'M', a8, 'L', a9, 'M', a1, 'L', a5, 'M', a3, 'L', a4, 'M', a2, 'L', a12, 'M', a4, 'L', a6, 'L', a7, 'M', a11, 'L', a15, 'M', a4, 'L', a10, 'M', a14, 'L', a4, 'L', a20, 'M', a18, 'L', a19, 'M', a17, 'L', aD1.o, 'L', a16, 'M', a21, 'L', a16, 'M', a11, 'C', a7, 'C', a5, 'L', a6, 'C', a1])
        A.addDartLine(['M', aD1.i, 'L', aD1, 'L', aD1.o, 'L', aD1.d, 'L', aD1.i, 'M', aD2.ic, 'L', aD2, 'L', aD2.oc])
        #pth = (['M', a1, 'L', a18, 'L', a20, 'L', a21, 'L', a16, 'L', aD2.o, 'L', aD2.m, 'L', aD2.i, 'L', a11, 'C', a7, 'C', a5, 'L', a6, 'C', a1])
        pth = (['M', a1, 'L', a18, 'L', a20, 'L', a21, 'L', a16, 'L', aD2.o, 'L', aD2.m, 'L', aD2.i, 'L', a11, 'C', a7, 'C', a5, 'L', a6, 'C', a1])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        #draw Bodice Back B
        pnt1 = dPnt((distance(b3, b6)/2.0, distance(b1, b8)/2.0))
        B.setLabelPosition((pnt1))
        B.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        bG1 = dPnt(right(pnt1, distance(b1, b6)/3.0))
        bG2 = dPnt(down(bG1, distance(b1, b2)/2.0))
        B.addGrainLine(bG1, bG2)
        B.addGridLine(['M', b6, 'L', b3, 'L', b2, 'L', b14, 'M', bD1.o, 'L', b11, 'M', b1, 'L', b5, 'M', b2, 'L', b5, 'M', b6, 'L', b7, 'M', b8, 'L', b9, 'M',  bD1, 'L', b15, 'L', b16, 'M', b17, 'L', b11])
        B.addDartLine(['M', bD1.i, 'L', bD1, 'L', bD1.o, 'L', bD1.d, 'L', bD1.i])
        pth = (['M', b1, 'L', b13, 'L', b15, 'L', b17, 'L', b11, 'L', b10, 'C', b7, 'C', b5, 'L', b6, 'C', b1])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        #draw Sleeve C
        pnt1 = dPnt((SCF2.x, SBF.y + abs(SBF.y - SEF.y) / 2.0 ))
        C.setLabelPosition((pnt1.x, pnt1.y))
        C.setLetter(up(pnt1, 0.5 * IN), scaleby=10.0)
        CG1 = dPnt((SBM1.x, SBM1.y))
        CG2 = dPnt(down(CG1, 0.75 * distance(SBM1, SWM)))
        C.addGrainLine(CG1, CG2)
        C.addDartLine(['M', SD1.ic, 'L', SD1, 'L', SD1.oc, 'M', SD2.ic, 'L', SD2, 'L', SD2.oc, 'M', SD3.ic, 'L', SD3, 'L', SD3.oc])
        C.addGridLine(['M', SCM, 'L', SWM, 'M', SBF, 'L', SBB, 'M', SEF, 'L', SEB, 'M', SWF1, 'L', SWB, 'M', SEB1, 'L', SWM1, 'M', SCF1, 'L', SCF4, 'L', SCB1, 'L', SCB4])
        pth = (['M', SBF, 'C', SCM, 'C', SCB3, 'C', SBB, 'L', SD1.i, 'L', SD1.m, 'L', SD1.o, 'L', SD2.i, 'L', SD2.m, 'L', SD2.o, 'L', SD3.i, 'L', SD3.m, 'L', SD3.o, 'L', SWB, 'L', SWF2, 'C', SWF, 'L', SEF, 'L', SBF])
        C.addSeamLine(pth)
        C.addCuttingLine(pth)



        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

