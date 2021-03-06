#!/usr/bin/env python
# patternName: Block_Women_Bodice_Short_Fitted_WaistDart_NeckDart_Pivnick/Spencer
# patternNumber: BL_W_Bodice_Short_Pivnick_Spencer

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
        self.setInfo('patternNumber', 'BL_W_Bodice_Short_Fitted_1_Pivnick_Spencer')
        self.setInfo('patternTitle', 'Block_Women_Bodice_Short_Fitted_WaistDart_NeckDart_Pivnick_Spencer')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'Ester Pivnick')
        self.setInfo('patternmakerName', 'S. L. Spencer')
        self.setInfo('description', """Women's short bodice block with front & back waist dart and back neck dart, includes major changes to Ester Pivnick's original forumalas.""")
        #TODO: add new category 'Block Patterns'
        self.setInfo('category', 'Block')
        self.setInfo('type', 'Bodice')
        self.setInfo('gender', 'F') # 'M',  'F',  or ''
        #
        # The next group are all optional
        #
        self.setInfo('recommendedFabric', '')
        self.setInfo('recommendedNotions', '')
        #
        self.setInfo('yearstart', '1930' )
        #self.setInfo('yearend', '')
        self.setInfo('culture', 'Modern')
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

        #---new measurements---
        #90px / 1 in
        #2.54cm / 1 in
        #90 / 2.54  = px / cm
        FRONT_WAIST_BALANCE = 42.0 * 90.0 / 2.54
        BACK_WAIST_BALANCE = 45.0 * CM
        FRONT_UNDERARM_HEIGHT = 9.0 * CM
        BACK_UNDERARM_HEIGHT = 18.0 * CM
        FRONT_BUST_HEIGHT = 18.0 * CM

        #---Front A---#
        FBC1 = A.addPoint('FBC1', (0.0, 0.0)) #front bust center 1
        FBS = A.addPoint('FBS', right(FBC1, CD.front_bust / 2.0)) #front bust side
        FUC1 = A.addPoint('FUC1', up(FBC1, FRONT_BUST_HEIGHT - FRONT_UNDERARM_HEIGHT)) #front underarm center offset
        FUC = A.addPoint('FUC', right(FUC1, CD.front_bust / 2.0 - CD.front_underarm / 2.0)) #front underarm center
        FBP = A.addPoint('FBP', right(FBC1, CD.bust_distance / 2.0)) #front bust point
        angle1 = angleOfVector(FBP, FBC1, FUC)
        theta = ANGLE90 - angle1
        FBC = A.addPoint('FBC', intersectLineRay(FBC1, FUC, FBP, angleOfLine(FBP, FBC1) + theta)) #front bust center
        FSH = A.addPoint('FSH', onLineAtLength(FBC, FUC, CD.bust_balance)) #front shoulder height
        FWC = A.addPoint('FWC', onLineAtLength(FSH, FBC, CD.front_shoulder_height)) #front waist center
        FNC = A.addPoint('FNC', onLineAtLength(FWC, FBC, CD.front_waist_length)) #front neck center
        FSW = A.addPoint('FSW', polar(FSH, CD.front_shoulder_width / 2.0, angleOfLine(FBC, FSH) + ANGLE90))
        FAP1 = A.addPoint('FAP1', intersectLineRay(FBP, FBS, FSW, angleOfLine(FSH, FBC))) #front armscye point 1 - on bust line to define armscye curve
        FSP = A.addPoint('FSP', highestP(intersectLineCircle(FAP1, FSW, FWC, FRONT_WAIST_BALANCE))) #front shoulder point
        FNS = A.addPoint('FNS', leftmostP(intersectLineCircle(FSH, FSW, FSP, CD.shoulder))) #front neck side
        FWS1 = A.addPoint('FWS1', lowestP(onCircleAtX(FNC, FRONT_WAIST_BALANCE, FBS.x))) #front waist side
        FUS1 = A.addPoint('FUS1', onLineAtLength(FWS1, FBS, CD.side)) #front underarm side 1
        FAP2 = A.addPoint('FAP2', onLineAtY(FSP, FAP1, FUS1.y)) #front armscye point 2 - at FUS1 height
        FAP = A.addPoint('FAP', onLineAtLength(FSP, FAP2, 0.75 * distance(FSP, FAP2))) #front armscye point - on armscye curve
        FUS2 = A.addPoint('FUS2', extendLine(FAP2, FUS1, 0.04 * CD.front_bust / 2.0)) # front underarm side 2 - includes 4% bust ease
        FUS = A.addPoint('FUS', onLineAtLength(FWS1, FUS2, CD.side)) #front undearm side
        FWS2 = A.addPoint('FWS2', FWS1) #front waist side 2
        slashAndSpread(FBP, -(angleOfLine(FUC, FAP2) - angleOfLine(FBP, FBS)), FWS2) #rotate FWS counterclockwise to work with underarm line
        FWS = A.addPoint('FWS', onLineAtLength(FUS, FWS2, CD.side)) #front waist side - inline with extended front underarm side
        FD1 = A.addPoint('FD1', onRayAtX(FWC, angleOfLine(FWC, FNC) + ANGLE90, FBP.x)) #front waist middle point - under FBP
        dart_width = distance(FWC, FD1) + distance(FD1, FWS) - CD.front_waist / 2.0
        FD1.i = A.addPoint('FD1.i', onLineAtLength(FD1, FWC, dart_width / 2.0)) #waist dart inside leg
        FD1.o = A.addPoint('FD1.o', onLineAtLength(FD1, FWS, dart_width / 2.0)) #waist dart outside leg
        updatePoint(FD1, FBP) #move front waist dart point up to bustline
        extendDart(FWS, FD1, FWC)
        foldDart(FD1, FWC)


        #---front control handles
        #b/w FUS front underar side & FAP front armscye point
        FUS.addOutpoint(polar(FUS, distance(FUS, FAP) / 3.0, angleOfLine(FUS, FWS) + ANGLE90))
        FAP.addInpoint(polar(FAP, distance(FUS, FAP) / 3.0, angleOfLine(FSP, FUS)))
        #b/w FAP front armscye point & FSP front shoulder point
        FAP.addOutpoint(polar(FAP, 0.33 * distance(FAP, FSP), angleOfLine(FUS, FSP)))
        FSP.addInpoint(polar(FSP, 0.33 * distance(FAP, FSP), angleOfLine(FNS, FSP) + ANGLE90))
        #b/w FNS front neck side & FNC front neck center
        FNC.addInpoint(polar(FNC, 0.5 * abs(FNS.x - FNC.x), angleOfLine(FWC, FNC) + ANGLE90))
        FNS.addOutpoint(polar(FNS, 0.5 * abs(FNS.y - FNC.y), angleOfLine(FNS, FSP) + ANGLE90))

        #---Back B---#
        BSH = B.addPoint('BSH', (0.0, 0.0)) #back shoulder height
        BSW = B.addPoint('BSW', left(BSH, CD.back_shoulder_width / 2.0)) #back shoulder width
        BUW = B.addPoint('BUW', left(BSH, CD.back_underarm / 2.0)) #back undearm width
        BWC = B.addPoint('BWC', down(BSH, CD.back_shoulder_height)) #back waist center
        BNC = B.addPoint('BNC', up(BWC, CD.back_waist_length)) #back neck center
        BSP1 = B.addPoint('BSP1', highestP(onCircleAtX(BWC, CD.back_shoulder_balance, BSW.x))) #back shoulder point 1
        BNS = B.addPoint('BNS', rightmostP(onCircleAtY(BSP1, CD.shoulder, BSH.y))) #back neck side
        BSP = B.addPoint('BSP', extendLine(BNS, BSP1, 0.07 * CD.shoulder)) #BSP - incl. 7% ease for shoulder dart
        BAP = B.addPoint('BAP', down(BSP1, 1.1 * distance(FSP, FAP))) #back armscye point
        BWS1 = B.addPoint('BWS1', lowestP(onCircleAtX(BNC, BACK_WAIST_BALANCE, BUW.x))) #back waist side
        #back waist dart
        dart_width = (distance(BWS1, BWC) - CD.back_waist / 2.0) / 2.0
        BWS2 = B.addPoint('BWS2', onLineAtLength(BWS1, BWC, dart_width)) #back waist side 2
        BD1 = B.addPoint('BD1', midPoint(BWS2, BWC)) #back waist dart point - on waist line, will be updated later
        BD1.i = B.addPoint('BD1.i', onLineAtLength(BD1, BWC, dart_width / 2.0)) #back waist dart inside leg
        BD1.o = B.addPoint('BD1.o', onLineAtLength(BD1, BWS2, dart_width / 2.0)) #back waist dart outside leg
        BWS3 = B.addPoint('BWS3', onLineAtLength(BAP, BWS2, distance(BAP, BWS1))) #back waist side
        BUS1 = B.addPoint('BUS1', highestP(onCircleAtX(BWS3, CD.side, BUW.x))) #back underarm side 1
        BUC = B.addPoint('BUC', (BNC.x, BUS1.y)) #back underarm center
        BUS2 = B.addPoint('BUS2', extendLine(BUC, BUS1, 0.04 * CD.back_underarm / 2.0)) #back underarm side 2 - inc. 4% bust ease
        BUS3 = B.addPoint('BUS3', onLineAtLength(BWS3, BUS2, CD.side)) #back underarm side
        BUS = B.addPoint('BUS', BUS3)
        updatePoint(BD1, (BD1.x, BUC.y)) #move BD1 dart point up to underarm line
        slashAndSpread(BD1, -angleOfVector(BD1.i, BD1, BD1.o), BUS)
        BWS = B.addPoint('BWS', onLineAtLength(BUS, BWS3, CD.side))
        extendDart(BWS, BD1, BWC, extension=0.5)
        foldDart(BD1, BWC)
        #back shoulder dart
        BD2 = B.addPoint('BD2', midPoint(BNS, BSP))
        BD2.i = B.addPoint('BD2.i', onLineAtLength(BD2, BNS, 0.035 * CD.shoulder)) #back shoulder dart inside leg
        BD2.o = B.addPoint('BD2.o', onLineAtLength(BD2, BSP, 0.035 * CD.shoulder)) #back shoulder dart outside leg
        updatePoint(BD2, polar(BD2, distance(BSP, BAP) / 2.0, angleOfLine(BD2.o, BD2.i) + ANGLE90)) #move BD2 dart point
        extendDart(BSP, BD2, BNS)
        foldDart(BD2, BNS)

        #---back control handles
        #b/w BUS back underarm side & BAP back armscye point
        BUS.addOutpoint(polar(BUS, 0.5 * abs(BUS.x - BAP.x), angleOfLine(BWS, BUS) + ANGLE90))
        BAP.addInpoint(polar(BAP, 0.5 * abs(BUS.y - BAP.y), angleOfLine(BSP, BUS)))
        #b/w BAP back armscye point & BSP back shoulder point
        BAP.addOutpoint(polar(BAP, 0.33 * distance(BAP, BSP), angleOfLine(BUS, BSP)))
        BSP.addInpoint(polar(BSP, 0.33 * distance(BAP, BSP), angleOfLine(BSP, BNS) + ANGLE90))
        #b/w BNS back neck side & bNC back neck center
        BNC.addInpoint(polar(BNC, 0.5 * abs(BNS.x - BNC.x), angleOfLine(BNC, BWC) + ANGLE90))
        BNS.addOutpoint(polar(BNS, 0.5 * abs(BNS.y - BNC.y), angleOfLine(BSP, BNS) + ANGLE90))

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



        #draw Front A
        pnt1 = dPnt((FNS.x, FUC.y))
        A.setLabelPosition((pnt1.x, pnt1.y))
        A.setLetter(up(pnt1, 0.5 * IN), scaleby=10.0)
        #AG1 = dPnt(left(FUC, distance(FUC, pnt1)/4.0))
        #AG2 = dPnt(down(AG1, 0.75 * distance(FNC, FWC)))
        #A.addGrainLine(AG1, AG2)
        A.addDartLine(['M', FD1.ic, 'L', FD1, 'L', FD1.oc])
        A.addGridLine(['M', FAP1, 'L', FSW, 'L', FSH, 'L', FWC, 'M', FBC1, 'L', FUC1, 'L', FUC,  'M', FBC, 'L', FBP, 'M', FBC1, 'L', FBS, 'M', FWC, 'L', FSP, 'M', FNC, 'L', FWS1, 'M', FAP2, 'L', FUS1, 'M', FBP, 'L', FD1.m, 'M', FWS, 'L', FUS1, 'M', FUC, 'L', FAP2, 'L', FUS])
        pth = (['M', FNC, 'L', FWC, 'L', FD1.i, 'L', FD1.m, 'L', FD1.o, 'L', FWS, 'L', FUS, 'C', FAP, 'C', FSP, 'L', FNS, 'C', FNC])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        #draw Back B
        pnt1 = dPnt((BSH.x - abs(BSH.x - BSP.x) / 2.0, BSH.y + abs(BSH.y - BWC.y) / 3.0 ))
        B.setLabelPosition((pnt1.x, pnt1.y))
        B.setLetter(up(pnt1, 0.5 * IN), scaleby=10.0)
        #BG1 = dPnt(left(FUC, distance(FUC, pnt1)/4.0))
        #BG2 = dPnt(down(BG1, 0.75 * distance(FNC, FWC)))
        #B.addGrainLine(BG1, BG2)
        B.addDartLine(['M', BD1.ic, 'L', BD1, 'L', BD1.oc, 'M', BD2.ic, 'L', BD2, 'L', BD2.oc])
        B.addGridLine(['M', BUW, 'L', BSH, 'L', BWC, 'L', BSP1, 'L', BSW, 'M', BSP1, 'L', BAP, 'L', BWS, 'M', BAP, 'L', BWS1, 'M', BUS2, 'L', BUC, 'M', BUW, 'L', BWS1, 'M', BNC, 'L', BWS1])
        pth = (['M', BNC, 'L', BWC, 'L', BD1.i, 'L', BD1.m, 'L', BD1.o, 'L', BWS, 'L', BUS, 'C', BAP, 'C', BSP, 'L', BD2.o, 'L', BD2.m, 'L', BD2.i, 'L', BNS, 'C', BNC])
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

