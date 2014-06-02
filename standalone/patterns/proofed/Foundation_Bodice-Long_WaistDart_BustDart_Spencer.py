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
        FNC = A.addPoint('FNC', (0.0, 0.0)) #front neck center
        FWC = A.addPoint('FWC', down(FNC, CD.front_waist_length)) #front waist center
        FSH = A.addPoint('FSH', up(FWC, CD.front_shoulder_height)) #front shoulder height
        FSW = A.addPoint('FSW', left(FSH, CD.front_shoulder_width / 2.0)) #front shoulder width
        FUW = A.addPoint('FUW', left(FSH, CD.front_underarm / 2.0)) #front shoulder width
        FAW = A.addPoint('FAW', left(FSH, CD.across_chest / 2.0)) #front across chest width
        FBC = A.addPoint('FBC', up(FWC, CD.bust_length)) #bust center
        FBP = A.addPoint('FBP', left(FBC, CD.bust_distance/2.0)) #bust point
        FSP = A.addPoint('FSP', highestP(onCircleAtX(FWC, CD.front_shoulder_balance, FNC.x - CD.front_shoulder_width/2.0))) #front shoulder point
        FNS = A.addPoint('FNS', highestP(intersectCircles(FSP, CD.shoulder, FBP, CD.bust_balance))) #front neck side
        FAP = A.addPoint('FAP', lowestP(onCircleAtX(FNS, CD.front_underarm_balance, FAW.x))) #front across chest point
        FUC = A.addPoint('FUC', (FNC.x, FAP.y)) #front undearm center
        t1_FUS = A.addPoint('t1_FUS', left(FUC, CD.front_underarm/2.0)) #temp front underarm side
        FBS = A.addPoint('FBS', leftmostP(onCircleTangentFromOutsidePoint(FBP, CD.front_bust/2.0 - distance(FBC, FBP), t1_FUS))) #bust side is where line from bust point is perpendicular to line through t1_FUS
        FUS = A.addPoint('FUS', onLineAtLength(t1_FUS, FBS, 0.13 * CD.side)) #final front underarm side along line t1_FUS - FBS
        t1_FWS = A.addPoint('t1_FWS', left(FWC, CD.front_waist/2.0)) #temporary front waist side 1 - on waist line


        t2_FWS = A.addPoint('t2_FWS', onLineAtLength(t1_FUS, FBS, CD.side)) #temporary front waist side 2 - on side seam

        #---darts---
        #Front A waist dart
        totalDartAngle = abs(angleOfVector(t1_FWS, FBP, t2_FWS))
        frontWaistDartAngle = totalDartAngle/2.0
        bustDartAngle = totalDartAngle/2.0
        FD1 = A.addPoint('FD1', (FBP)) #front waist dart point
        FD1.i = A.addPoint('FD1.i', onRayAtY(FBP, ANGLE90 - frontWaistDartAngle/2.0, FWC.y)) #front waist dart inside leg
        FD1.o = A.addPoint('FD1.o', onRayAtY(FBP, ANGLE90 + frontWaistDartAngle/2.0, FWC.y)) #front waist dart outside leg
        FD1.m = A.addPoint('FD1.m', dPnt((FBP.x, FWC.y))) #below bust point at waist
        #Front A bust dart
        FD2 = A.addPoint('FD2', (FBP)) #bust dart point
        FD2.i = A.addPoint('FD2.i', intersectLineRay(t1_FUS, FBS, FBP, ANGLE180 + bustDartAngle/2.0)) #bust dart inside leg
        FD2.o = A.addPoint('FD2.o', polar(FBP, distance(FBP, FD2.i), ANGLE180 - bustDartAngle/2.0)) #bust dart outside leg
        FD2.m = A.addPoint('FD2.m', intersectLines(FBC, FBP, FBS, FUS)) #intersect bust line & side seam

        #TODO: create function pivot(pivot_point, rotation_angle, point_to_pivot) for slash_and_spread
        #finalize front waist side
        remainingSideSegment = distance(FUS, t2_FWS) - distance(FUS, FD2.i)
        remainingWaistSegment = distance(FWC, t1_FWS) - distance(FWC, FD1.i)
        FWS = A.addPoint('FWS', leftmostP(intersectCircles(FD2.o, remainingSideSegment, FD1.o, remainingWaistSegment))) #front waist side
        #Front A hip extension
        t3_FWS = A.addPoint('t3_FWS', left(FD1.o, distance(FD1.o, FWS))) #temporary extension waist side
        FHC = A.addPoint('FHC', down(FWC, CD.front_hip_height)) #front hip center
        t1_FHS = A.addPoint('t1_FHS', left(FHC, CD.front_hip/2.0)) #front hip side
        FHM = A.addPoint('FHM', (FD1.x, FHC.y)) #waist dart point on hip line
        #finalize extension waist side
        FHS = A.addPoint('FHS', leftmostP(intersectCircles(FHM, distance(FHM, t1_FHS), FWS, CD.side_hip_height))) #front hip side
        #finalize waist dart
        FD1.d = A.addPoint('FD1.d', up(FHM, distance(FHM, FD1.m)/7.0)) #front waist dart point at hip

        #create curve at dart base
        ##adjustDartLength(FWS, FD1, FWC, extension=0.25) #smooth waistline curve from FWS to FWC at dart
        foldDart(FD1, FWC) #creates FD1.m,FD1.oc,FD1.ic; dart folds in toward waist center FWC
        #do not call adjustDartLength(t1_FWS,FD2,FUS) -- bust dart FD2 is not on a curve
        foldDart(FD2, FUS) #creates FD2.m,FD2.oc,FD2.ic; dart folds up toward underarm side FUS
        #adjust FD1 & FD2 away from FBP bust point
        (FD1.x, FD1.y) = down(FD1, distance(FD1, FD1.i)/7.0)
        (FD2.x, FD2.y) = left(FD2, distance(FD2, FD2.i)/7.0)

        #Bodice Front A control points
        #b/w FNS front neck point & FNC front neck center
        FNS.addOutpoint(down(FNS, abs(FNC.y - FNS.y)/2.0))
        FNC.addInpoint(left(FNC, 0.75 * abs(FNC.x - FNS.x)))
        #b/w FD1.o waist dart outside leg & FWS front waist side - short control handles
        FD1.o.addOutpoint(polar(FD1.o, distance(FD1.o, FWS)/6.0, angleOfLine(FD1.o, FD1) - (angleOfLine(FD1.i, FD1) - ANGLE180))) #control handle forms line with FWC,FD1.i
        FWS.addInpoint(polar(FWS, distance(FD1.o, FWS)/6.0, angleOfLine(FWS, FD1.o.outpoint))) #FWS control handle points to FD1.o control handle
        #b/w FAP front underarm point & FSP front shoulder point
        FSP.addInpoint(polar(FSP, distance(FAP, FSP)/6.0, angleOfLine(FSP, FNS) + ANGLE90)) #short control handle perpendicular to shoulder seam
        FAP.addOutpoint(polar(FAP, distance(FAP, FSP)/3.0, angleOfLine(FAP, FNS))) #control handle points to front neck point
        #b/w FUS front underarm side & FAP front underarm point
        FAP.addInpoint(polar(FAP, distance(FUS, FAP)/3.0, angleOfLine(FNS, FAP)))
        FUS.addOutpoint(polar(FUS, distance(FUS, FAP)/3.0, angleOfLine(FD2.i, FUS) + ANGLE90)) #control handle is perpendicular to side seam at underarm

        #Bodice Back B
        BNC = B.addPoint('BNC', (0.0, 0.0)) #back neck center
        BWC = B.addPoint('BWC', down(BNC, CD.back_waist_length)) #back waist center
        BSH = B.addPoint('BSH', up(BWC, CD.back_shoulder_height)) #back shoulder height
        BSW = B.addPoint('BSW', right(BSH, CD.back_shoulder_width / 2.0 )) #back shoulder width
        BAW = B.addPoint('BAW', right(BSH, CD.across_back / 2.0)) #across back width
        BUW = B.addPoint('BUW', right(BSH, CD.back_underarm / 2.0)) #back underarm width
        t1_BWS = B.addPoint('t1_BWS', right(BWC, CD.back_waist/2.0)) #back waist side reference point
        BSP = B.addPoint('BSP', highestP(onCircleAtX(BWC, CD.back_shoulder_balance, BNC.x + CD.back_shoulder_width/2.0))) #back shoulder point
        BNS = B.addPoint('BNS', leftmostP(onCircleAtY(BSP, CD.shoulder, BSH.y))) #back neck side
        BAP = B.addPoint('BAP', lowestP(onCircleAtX(BNS, CD.back_underarm_balance, BNC.x + CD.across_back/2.0))) #across back point
        BUC = B.addPoint('BUC', (BNC.x, BAP.y)) #back undearm center
        t1_BUS = B.addPoint('t1_BUS', right(BUC, CD.back_underarm/2.0)) #temp back under side
        BUS = B.addPoint('BUS', down(t1_BUS, distance(t1_FUS, FUS))) #final back underarm side
        BD1 = B.addPoint('BD1', intersectLines(BWC, BSP, BUC, t1_BUS)) #back waist dart point
        BD1.m = B.addPoint('BD1.m', dPnt((BD1.x, BWC.y))) # below dart point at waist
        BD1.i = B.addPoint('BD1.i', left(BD1.m, distance(BWC, BD1.m)/5.0)) #dart inside leg
        BD1.o = B.addPoint('BD1.o', right(BD1.m, distance(BD1.m, BD1.i))) #dart outside leg
        BWS = B.addPoint('BWS',  rightmostP(intersectCircles(BUS, distance(FUS, FD2.i) + distance(FD2.o, FWS), BD1.o, CD.back_waist/2.0 - distance(BWC, BD1.i)))) #back waist side
        #Bodice Back hip extension
        BHC = B.addPoint('BHC', down(BWC, CD.back_hip_height)) #back hip center
        t2_BWS = B.addPoint('t2_BWS', right(BD1.o, distance(BD1.o, BWS))) #temp back waist side 2
        BHM = B.addPoint('BHM', (BD1.x, BHC.y)) # back waist dart at hip line - back hip mid-point
        t1_BHS = B.addPoint('t1_BHS', right(BHC, CD.back_hip/2.0)) #temporary back hip side
        BHS = B.addPoint('BHS', rightmostP(intersectCircles(BHM, distance(BHM, t1_BHS), BWS, CD.side_hip_height))) #back hip side
        #complete Back waist dart
        BD1.d = B.addPoint('BD1.d', up(BHM, distance(BHM, BD1.m)/7.0)) # back waist dart point at hip
        #create curve at dart base
        foldDart(BD1, BWC) #creates BD1.m, BD1.oc, BD1.ic; dart folds toward waist center BWC

        #Bodice Back B control points
        #b/w BNS back neck point & BNC back neck center
        BNC.addInpoint(right(BNC, 0.75 * abs(BNC.x - BNS.x)))
        BNS.addOutpoint(polar(BNS, abs(BNS.y - BNC.y)/2.0, angleOfLine(BNS, BSP) + ANGLE90)) #perpendicular to shoulder seam
        #b/w BUS underarm point & BAP underarm curve
        BUS.addOutpoint(polar(BUS, distance(BUS, BAP)/3.0, angleOfLine(BUS, BWS) + ANGLE90)) #perpendicular to side seam
        BAP.addInpoint(polar(BAP, distance(BUS, BAP)/3.0, angleOfLine(BNS, BAP)))
        #b/w BAP underarm curve & BNS shoulder point
        BAP.addOutpoint(polar(BAP, distance(BAP, BSP)/3.0, angleOfLine(BAP, BNS)))
        BSP.addInpoint(polar(BSP, distance(BAP, BSP)/6.0, angleOfLine(BNS, BSP) + ANGLE90)) #short control handle, perpendicular to shoulder seam
        #b/w BD1.o waist dart outside leg & BWS waist side
        BD1.o.addOutpoint(polar(BD1.o, distance(BD1.o, BWS)/6.0, angleOfLine(BD1.o, BD1) + ANGLE180 - angleOfVector(BWC, BD1.i, BD1))) #short control handle, forms line with control handle for inside leg
        BWS.addInpoint(polar(BWS, distance(BD1.o, BWS)/3.0, angleOfLine(BUS, BWS) + angleOfVector(FD2.o, FWS, FWS.inpoint))) #forms line with control handle for FWS front waist

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
        SWM1 = C.addPoint('SWM1', rightmostP(onCircleTangentFromOutsidePoint(SWF1, 0.5 * CD.wrist, SEB1))) #sleeve wrist middle 1 - extend down wrist middle point
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
        pnt1 = dPnt(midPoint(FAP, FUC))
        A.setLabelPosition((pnt1))
        A.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        aG1 = dPnt(left (FNC, distance(FNC, FNS)/3.0))
        aG2 = dPnt(down(aG1, distance(FNC, FHC)/2.0))
        A.addGrainLine(aG1, aG2)
        A.addGridLine(['M', FUW, 'L', FSH, 'L', FHC, 'L', t1_FHS, 'M', FUC, 'L', t1_FUS, 'M', FNC, 'L', FSP, 'M', FBC, 'L', FBP, 'M', FWC, 'L', t3_FWS, 'M', FBP, 'L', FNS, 'L', FAP, 'M', FUS, 'L', t2_FWS, 'M', FBP, 'L', FBS, 'M', FD2.m, 'L', FBP, 'L', FHM, 'M', FHC, 'L', t1_FHS, 'M', t3_FWS, 'L', FD1.o, 'L', FWS, 'M', FHS, 'L', FWS, 'M', FUS, 'C', FAP, 'C', FSP, 'L', FNS, 'C', FNC])
        A.addDartLine(['M', FD1.i, 'L', FD1, 'L', FD1.o, 'L', FD1.d, 'L', FD1.i, 'M', FD2.ic, 'L', FD2, 'L', FD2.oc])
        #pth = (['M', FNC, 'L', FHC, 'L', FHM, 'L', FHS, 'L', FWS, 'L', FD2.o, 'L', FD2.m, 'L', FD2.i, 'L', FUS, 'C', FAP, 'C', FSP, 'L', FNS, 'C', FNC])
        pth = (['M', FNC, 'L', FHC, 'L', FHM, 'L', FHS, 'L', FWS, 'L', FD2.o, 'L', FD2.m, 'L', FD2.i, 'L', FUS, 'C', FAP, 'C', FSP, 'L', FNS, 'C', FNC])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        #draw Bodice Back B
        pnt1 = dPnt((distance(BSH, BNS)/2.0, distance(BNC, BUC)/2.0))
        B.setLabelPosition((pnt1))
        B.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        bG1 = dPnt(right(pnt1, distance(BNC, BNS)/3.0))
        bG2 = dPnt(down(bG1, distance(BNC, BWC)/2.0))
        B.addGrainLine(bG1, bG2)
        B.addGridLine(['M', BUW, 'L', BSH, 'L', BHC, 'L', t1_BHS, 'M', BWC, 'L', t2_BWS, 'M', BD1.o, 'L', BWS, 'M', BNC, 'L', BSP, 'M', BWC, 'L', BSP, 'M', BNS, 'L', BAP, 'M', BUC, 'L', t1_BUS, 'M',  BD1, 'L', BHM, 'L', t1_BHS, 'M', BHS, 'L', BWS])
        B.addDartLine(['M', BD1.i, 'L', BD1, 'L', BD1.o, 'L', BD1.d, 'L', BD1.i])
        pth = (['M', BNC, 'L', BHC, 'L', BHM, 'L', BHS, 'L', BWS, 'L', BUS, 'C', BAP, 'C', BSP, 'L', BNS, 'C', BNC])
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

