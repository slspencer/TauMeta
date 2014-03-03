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
        FNC = A.addPoint('FNC', (0.0, 0.0)) #front neck center
        FWC = A.addPoint('FWC', down(FNC, CD.front_waist_length)) #front waist center
        FSH = A.addPoint('FSH', up(FWC, CD.front_shoulder_height)) #front shoulder height
        FSW = A.addPoint('FSW', left(FSH, CD.front_shoulder_width / 2.0)) #front shoulder width
        FBC = A.addPoint('FBC', up(FWC, CD.bust_length)) #bust center
        FBP = A.addPoint('FBP', left(FBC, CD.bust_distance / 2.0)) #bust point
        FSP = A.addPoint('FSP', highestP(onCircleAtX(FWC, CD.front_shoulder_balance, FSW.x))) #front shoulder point
        FNS = A.addPoint('FNS', rightmostP(onCircleAtY(FSP, CD.shoulder, FSH.y))) #front neck side
        FAP = A.addPoint('FAP', lowestP(onCircleAtX(FNS, CD.front_underarm_balance, FNC.x - CD.across_chest / 2.0))) #front armscye point
        FUC = A.addPoint('FUC', (FNC.x, FAP.y)) #front undearm center
        FUS1 = A.addPoint('FUS1', left(FUC, CD.front_underarm / 2.0)) #front underarm side 1
        FBS1 = A.addPoint('FBS1', leftmostP(onCircleTangentFromOutsidePoint(FBP, CD.front_bust / 2.0 - distance(FBC, FBP), FUS1))) #bust side is where line from bust point is perpendicular to line through FUS1
        FUS = A.addPoint('FUS', onLineAtLength(FUS1, FBS1, 0.13 * CD.side)) #lowered front underarm side on line FUS1-FBS1
        FWS1 = A.addPoint('FWS1', left(FWC, CD.front_waist / 2.0)) #temporary front waist side 1 - on waist line
        FWM = A.addPoint('FWM', dPnt((FBP.x, FWC.y))) #below bust point at waist - front waist middle
        FBS = A.addPoint('FBS', intersectLines(FBC, FBP, FUS, FBS1)) #intersect bust line & side seam
        FWS2 = A.addPoint('FWS2', onLineAtLength(FUS, FBS1, CD.side)) #temporary front waist side 2 - on side seam

        #---darts---
        #front waist dart
        totalDartAngle = abs(angleOfVector(FWS1, FBP, FWS2))
        frontWaistDartAngle = totalDartAngle / 2.0
        bustDartAngle = totalDartAngle / 2.0
        FD1 = A.addPoint('FD1', (FBP)) #front waist dart point
        FD1.i = A.addPoint('FD1.i', onRayAtY(FBP, ANGLE90 - frontWaistDartAngle / 2.0, FWC.y)) #front waist dart inside leg
        FD1.o = A.addPoint('FD1.o', onRayAtY(FBP, ANGLE90 + frontWaistDartAngle / 2.0, FWC.y)) #front waist dart outside leg
        #bust dart
        FD2 = A.addPoint('FD2', (FBP)) #bust dart point
        FD2.i = A.addPoint('FD2.i', intersectLineRay(FUS, FBS1, FBP, ANGLE180 + bustDartAngle / 2.0)) #bust dart inside leg
        FD2.o = A.addPoint('FD2.o', polar(FBP, distance(FBP, FD2.i), ANGLE180 - bustDartAngle / 2.0)) #bust dart outside leg
        #TODO: create function pivot(pivot_point, rotation_angle, point_to_pivot)

        #finalize front waist side
        remainingSideSegment = distance(FUS, FWS2) - distance(FUS, FD2.i)
        remainingWaistSegment = distance(FWC, FWS1) - distance(FWC, FD1.i)
        FWS = A.addPoint('FWS', leftmostP(intersectCircles(FD2.o, remainingSideSegment, FD1.o, remainingWaistSegment))) #front waist side created after all darts defined

        #create curve at dart base
        ##adjustDartLength(FWS, FD1, FWC, extension=0.25) #smooth waistline curve from FWS to FWC at dart
        foldDart(FD1, FWC) #creates FD1.m,FD1.oc,FD1.ic; dart folds in toward waist center FWC
        #do not call adjustDartLength(FWS1,FD2,FUS) -- bust dart FD2 is not on a curve
        foldDart(FD2, FUS) #creates FD2.m,FD2.oc,FD2.ic; dart folds up toward underarm side FUS
        #adjust FD1 & FD2 away from FBP bust point
        (FD1.x, FD1.y) = down(FD1, distance(FD1, FD1.i) / 7.0)
        (FD2.x, FD2.y) = left(FD2, distance(FD2, FD2.i) / 7.0)

        #Bodice Front A control points
        #b/w FNS front neck side & FNC front neck center
        FNS.addOutpoint(down(FNS, abs(FNC.y - FNS.y) / 2.0))
        FNC.addInpoint(left(FNC, 0.75 * abs(FNC.x - FNS.x)))
        #b/w FD1.o waist dart outside leg & FWS front waist side - short control handles
        FD1.o.addOutpoint(polar(FD1.o, distance(FD1.o, FWS) / 6.0, angleOfLine(FD1.o, FD1) - (angleOfLine(FD1.i, FD1) - ANGLE180))) #control handle forms line with FWC,FD1.i
        FWS.addInpoint(polar(FWS, distance(FD1.o, FWS) / 6.0, angleOfLine(FWS, FD1.o.outpoint))) #FWS control handle points to FD1.o control handle
        #b/w FAP front armscye point & FSP front shoulder point
        FSP.addInpoint(polar(FSP, distance(FAP, FSP) / 6.0, angleOfLine(FSP, FNS) + ANGLE90)) #short control handle perpendicular to shoulder seam
        FAP.addOutpoint(polar(FAP, distance(FAP, FSP) / 3.0, angleOfLine(FAP, FNS))) #control handle points to front neck side
        #b/w FUS front underarm side & FAP front armscye point
        FAP.addInpoint(polar(FAP, distance(FUS, FAP) / 3.0, angleOfLine(FNS, FAP)))
        FUS.addOutpoint(polar(FUS, distance(FUS, FAP) / 3.0, angleOfLine(FD2.i, FUS) + ANGLE90)) #control handle is perpendicular to side seam at underarm

        #Bodice Back B
        BNC = B.addPoint('BNC', (0.0, 0.0)) #back neck center
        BWC = B.addPoint('BWC', down(BNC, CD.back_waist_length)) #back waist center
        BSH = B.addPoint('BSH', up(BWC, CD.back_shoulder_height)) #back shoulder height
        BSW = B.addPoint('BSW', right(BSH, CD.back_shoulder_width / 2.0)) #back shoulder width
        BWS1 = B.addPoint('BWS1', right(BWC, CD.back_waist / 2.0)) #back waist side 1
        BSP = B.addPoint('BSP', highestP(onCircleAtX(BWC, CD.back_shoulder_balance, BSW.x))) #back shoulder point
        BNS = B.addPoint('BNS', leftmostP(onCircleAtY(BSP, CD.shoulder, BSH.y))) #back neck side
        BAP = B.addPoint('BAP', lowestP(onCircleAtX(BNS, CD.back_underarm_balance, BNC.x + CD.across_back / 2.0))) #back armscye point
        BUC = B.addPoint('BUC', (BNC.x, BAP.y)) #back undearm center
        BUS1 = B.addPoint('BUS1', right(BUC, CD.back_underarm / 2.0)) #back underarm side 1
        BUS = B.addPoint('BUS', down(BUS1, distance(FUS, FUS1))) #final back underarm side
        BD1 = B.addPoint('BD1', intersectLines(BWC, BSP, BUC, BUS1)) #back waist dart point is at underarm height
        BWM = B.addPoint('BWM', dPnt((BD1.x, BWC.y))) # below dart point at waist - back waist middle
        BD1.i = B.addPoint('BD1.i', left(BWM, distance(BWC, BWM) / 5.0)) #dart inside leg
        BD1.o = B.addPoint('BD1.o', right(BWM, distance(BWM, BD1.i))) #dart outside leg
        BWS = B.addPoint('BWS',  rightmostP(intersectCircles(BUS, distance(FUS, FD2.i) + distance(FD2.o, FWS), BD1.o, CD.back_waist / 2.0 - distance(BWC, BD1.i)))) #back waist side
        #create curve at dart base
        ##adjustDartLength(FWS, FD1, FWC, extension=0.25) #smooth waistline curve from FWS to FWC at dart
        foldDart(BD1, BWC) #creates BD1.m, BD1.oc, BD1.ic; dart folds toward waist center BWC

        #Bodice Back B control points
        #b/w BNS back neck side & BNC back neck center
        BNC.addInpoint(right(BNC, 0.75 * abs(BNC.x - BNS.x)))
        BNS.addOutpoint(polar(BNS, abs(BNS.y - BNC.y) / 2.0, angleOfLine(BNS, BSP) + ANGLE90)) #perpendicular to shoulder seam
        #b/w BUS armscye point & BAP underarm curve
        BUS.addOutpoint(polar(BUS, distance(BUS, BAP) / 3.0, angleOfLine(BUS, BWS) + ANGLE90)) #perpendicular to side seam
        BAP.addInpoint(polar(BAP, distance(BUS, BAP) / 3.0, angleOfLine(BNS, BAP)))
        #b/w BAP underarm curve & BNS shoulder point
        BAP.addOutpoint(polar(BAP, distance(BAP, BSP) / 3.0, angleOfLine(BAP, BNS)))
        BSP.addInpoint(polar(BSP, distance(BAP, BSP) / 6.0, angleOfLine(BNS, BSP) + ANGLE90)) #short control handle, perpendicular to shoulder seam
        #b/w BD1.o waist dart outside leg & BWS waist side
        BD1.o.addOutpoint(polar(BD1.o, distance(BD1.o, BWS) / 6.0, angleOfLine(BD1.o, BD1) + ANGLE180 - angleOfVector(BWC, BD1.i, BD1))) #short control handle, forms line with control handle for inside leg
        BWS.addInpoint(polar(BWS, distance(BD1.o, BWS) / 3.0, angleOfLine(BUS, BWS) + angleOfVector(FD2.o, FWS, FWS.inpoint))) #forms line with control handle for FWS front waist

        # Shirt sleeve C
        #get front & back armcye length
        back_armscye = points2List(BUS, BUS.outpoint, BAP.inpoint, BAP, BAP.outpoint, BSP.inpoint, BSP)
        front_armscye = points2List(FUS, FUS.outpoint, FAP.inpoint, FAP, FAP.outpoint, FSP.inpoint, FSP)
        ARMSCYE_LENGTH = curveLength(back_armscye) + curveLength(front_armscye)

        SCM = C.addPoint('SCM', (0.0, 0.0)) #sleeve cap midpoint - top of sleeve
        SUM = C.addPoint('SUM', (SCM.x, SCM.y + ARMSCYE_LENGTH / 4.0 + 1.5 * CM)) #sleeve underarm midpoint
        SWM = C.addPoint('SWM', (SCM.x, SCM.y + CD.oversleeve_length + 6 * CM)) #sleeve wrist midpoint
        SEM = C.addPoint('SEM', midPoint(SUM, SWM)) #sleeve elbow midpoint
        SUB = C.addPoint('SUB', (SUM.x - (ARMSCYE_LENGTH / 2.0 - 0.5 * CM), SUM.y)) #sleeve underarm back
        SWB1 = C.addPoint('SWB1', (SUB.x, SWM.y)) #back wrist line
        SUF = C.addPoint('SUF', (SUM.x + (ARMSCYE_LENGTH / 2.0 - 0.5 * CM), SUM.y)) #sleeve underarm front
        CWF1 = C.addPoint('CWF1', (SUF.x, SWM.y)) #front wrist line
        #back armscye points
        SCB1 = C.addPoint('SCB1', onLineAtLength(SUB, SCM, distance(SUB, SCM) / 4.0)) #sleeve cap back 1
        SCB2 = C.addPoint('SCB2', polar(midPoint(SUB, SCM), 1 * CM, angleOfLine(SUB, SCM) - ANGLE90)) #sleeve cap back 2
        pnt = onLineAtLength(SUB, SCM, 0.75 * distance(SUB, SCM))
        SCB3 = C.addPoint('SCB3', polar(pnt, 2 * CM, angleOfLine(SUB, SCM) - ANGLE90)) #sleeve cap back 3
        #front armscye points
        pnt = onLineAtLength(SUF, SCM, distance(SUF, SCM) / 4.0)
        SCF1 = C.addPoint('SCF1', polar(pnt, 1 * CM, angleOfLine(SUF, SCM) - ANGLE90)) #sleeve cap front 1
        SCF2 = C.addPoint('SCF2', midPoint(SUF, SCM)) #sleeve cap front 2
        pnt = onLineAtLength(SUF, SCM, 0.75 *  distance(SUF, SCM))
        SCF3 = C.addPoint('SCF3', polar(pnt, 1 * CM, angleOfLine(SUF, SCM) + ANGLE90)) #sleeve cap front 3
        SWB3 = C.addPoint('SWB3', onLineAtLength(SWM, SWB1, 0.7 * CD.wrist)) #back wrist point
        SWF = C.addPoint('SWF', onLineAtLength(SWM, CWF1, 0.7 * CD.wrist)) #sleeve wrist front
        SWB2 = C.addPoint('SWB2', midPoint(SWB1, SWB3)) #wristline reference point
        c18 = C.addPoint('c18', midPoint(CWF1, SWF)) #wristline reference point
        SEB = C.addPoint('SEB', left(SEM, 0.65 * CD.elbow)) #sleeve elbow back
        SEF = C.addPoint('SEF', right(SEM, 0.55 * CD.elbow)) #sleeve elbow front
        c24 = C.addPoint('c24', midPoint(SUM, SEM)) #middle of sleeve - label reference point

        #Shirt Sleeve C control points
        cArray = points2List(SUB, SCB1, SCB2, SCB3, SCM, SCF3, SCF2, SCF1, SUF)
        C1, C2 = controlPoints('sleeve_cap', cArray)
        SUB.addOutpoint(C1[0])
        SCB1.addInpoint(C2[0])
        SCB1.addOutpoint(C1[1])
        SCB2.addInpoint(C2[1])#
        SCB2.addOutpoint(C1[2])
        SCB3.addInpoint(C2[2])
        SCB3.addOutpoint(C1[3])
        SCM.addInpoint(C2[3])
        SCM.addOutpoint(C1[4])
        SCF3.addInpoint(C2[4])
        SCF3.addOutpoint(C1[5])
        SCF2.addInpoint(C2[5])
        SCF2.addOutpoint(C1[6])
        SCF1.addInpoint(C2[6])
        SCF1.addOutpoint(C1[7])
        SUF.addInpoint(C2[7])
        cArray = points2List(SWB3, SEB, SUB)
        C1, C2 = controlPoints('sleeve_seam1', cArray)
        SWB3.addOutpoint(C1[0])
        SEB.addInpoint(C2[0])
        SEB.addOutpoint(C1[1])
        SUB.addInpoint(C2[1])
        cArray = points2List(SUF, SEF, SWF)
        C1, C2 = controlPoints('sleeve_seam2', cArray)
        SUF.addOutpoint(C1[0])
        SEF.addInpoint(C2[0])
        SEF.addOutpoint(C1[1])
        SWF.addInpoint(C2[1])

        #elbow dart & lower sleeve control points
        SD1 = C.addPoint('SD1',  midPoint(SEB, SEM)) #elbow dart point
        SD1.i = C.addPoint('SD1.i', (SEB)) #elbow dart inside leg
        SD1.o = C.addPoint('SD1.o', onLineAtLength(SEB, SEB.inpoint, CD.oversleeve_length/20.0)) #elbow dart outside leg
        SD1.i.addOutpoint(SEB.outpoint)
        SD1.o.addInpoint((SEB.inpoint))
        foldDart(SD1, SEB.outpoint) #creates SD1.m, SD1.oc, SD1.ic; dart folds up toward sleeve cap

        SWB = C.addPoint('SWB', polar(SWB3, CD.oversleeve_length/20.0, angleOfLine(SWB3.outpoint, SWB3))) #sleeve extended at back wrist to allow for elbow dart

        #control points b/w SWF front wrist & SWB back wrist
        SWF.addOutpoint(polar(SWF, distance(SWF, SWB)/3.0, angleOfLine(SWF.inpoint, SWF) + ANGLE90)) #handle is perpendicular to sleeve seam
        SWB.addInpoint(polar(SWB, distance(SWF, SWB)/3.0, angleOfLine(SWB3, SWB) - ANGLE90)) #handle is perpendicular to sleeve seam
        #cArray = points2List(SWM, c21, SWB3)
        #C1, C2 = controlPoints('sleeve_placket', cArray)
        #SWM.addOutpoint(C1[0])
        #c21.addInpoint(C2[0])
        #c21.addOutpoint(C1[1])
        #SWB3.addInpoint(C2[1])
        #b/w SWF front wrist & SWM mid wrist
        #SWF.addOutpoint(polar(SWF, distance(SWF, SWM)/6.0, angleOfLine(SWF.inpoint, SWF) + angleOfVector(SWB3.outpoint, SWB3, SWB3.inpoint))) #short control handle forms line with control handle SWB3-SWB3.inpoint at back wrist
        #SWM.addInpoint(polar(SWM, distance(SWF, SWM)/6.0, angleOfLine(SWM.outpoint, SWM))) #short control handle forms line with control handle SWM.oupoint-SWM at mid-wrist



        #draw Bodice Front A
        pnt1 = dPnt(midPoint(FAP, FUC))
        A.setLabelPosition((pnt1))
        A.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)

        aG1 = dPnt(left(FUC, distance(FUC, pnt1)/4.0))
        aG2  = dPnt(down(aG1, distance(FNC, FWC)/2.0))
        A.addGrainLine(aG1, aG2)

        A.addGridLine(['M', FSP, 'L', FSW, 'L', FSH, 'L', FWC, 'L', FSP, 'M', FUC, 'L', FUS1, 'L', FUS, 'M', FBC, 'L', FBP, 'M', FWC, 'L', FWS1, 'M', FBP, 'L', FNS, 'L', FAP, 'M', FUS, 'L', FWS2, 'M', FBP, 'L', FBS1, 'M', FBS, 'L', FBP, 'L', FWM])

        A.addDartLine(['M', FD1.ic, 'L', FD1, 'L', FD1.oc, 'M', FD2.ic, 'L', FD2, 'L', FD2.oc])

        pth = (['M', FNC, 'L', FWC, 'L', FD1.i, 'L', FD1.m, 'L', FD1.o, 'C', FWS, 'L', FD2.o, 'L', FD2.m, 'L', FD2.i, 'L', FUS, 'C', FAP, 'C', FSP, 'L', FNS, 'C', FNC])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        #draw Bodice Back B
        pnt1 = dPnt((distance(BSH, BNS)/2.0, distance(BNC, BUC)/2.0))
        B.setLabelPosition((pnt1))
        B.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)

        bG1 = dPnt((distance(BSH, BNS)/4.0, distance(BNC, BUC)/4.0))
        bG2 = dPnt(down(bG1, distance(BNC, BWC)/2.0))
        B.addGrainLine(bG1, bG2)

        B.addGridLine(['M', BSP, 'L', BSW, 'L', BSH, 'L', BWC, 'L', BWS1, 'M', BWC, 'L', BSP, 'M', BNS, 'L', BAP, 'M', BUC, 'L', BUS1, 'M',  BD1, 'L', BWM])

        B.addDartLine(['M', BD1.ic, 'L', BD1, 'L', BD1.oc])

        pth = (['M', BNC, 'L', BWC, 'L', BD1.i, 'L', BD1.m, 'L', BD1.o, 'C', BWS, 'L', BUS, 'C', BAP, 'C', BSP, 'L', BNS, 'C', BNC])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        # Shirt Sleeve C
        Cg1 = dPnt((SUM.x, SUM.y))
        Cg2 = dPnt((Cg1.x, SWM.y - 8*CM))
        C.addGrainLine(Cg1, Cg2)
        C.setLetter((SCB2.x, c24.y), scaleby=15.0)
        C.setLabelPosition((SCB2.x, c24.y + 2*CM))

        C.addGridLine(['M', SCM,'L', SWM, 'M', SUF, 'L', CWF1, 'M', SUB, 'L', SWB1, 'M', SUB, 'L', SCM, 'L',  SUF, 'M', SUB, 'L', SWB2, 'M', SEB, 'L', SWB3, 'M', SUF, 'L', c18, 'M', SEF, 'L', SWF, 'M', SUB, 'L', SUF,  'M', SEB, 'L', SEF, 'M', SWB1, 'L', CWF1])

        #TODO: change function def to addDartLine(SD1) -- only one parameter needed
        C.addDartLine(['M', SD1.ic, 'L', SD1, 'L', SD1.oc])

        pth = (['M', SUB, 'C', SCB1, 'C', SCB2, 'C', SCB3, 'C', SCM, 'C', SCF3, 'C', SCF2, 'C', SCF1, 'C', SUF, 'C', SEF, 'C', SWF, 'C', SWB, 'L', SWB3, 'C', SD1.o, 'L', SD1.m, 'L', SD1.i, 'C', SUB])
        C.addSeamLine(pth)
        C.addCuttingLine(pth)

        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

