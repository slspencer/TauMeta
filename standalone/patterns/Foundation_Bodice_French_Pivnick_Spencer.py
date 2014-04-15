#!/usr/bin/env python
# patternName: Block_Women_Bodice_French_Pivnick/Spencer
# patternNumber: BL_W_Bodice_French_Pivnick_Spencer

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
        self.setInfo('patternNumber', 'BL_W_Bodice_French_Pivnick_Spencer')
        self.setInfo('patternTitle', 'Block_Women_Bodice_French_Pivnick_Spencer')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'Ester Pivnick')
        self.setInfo('patternmakerName', 'S. L. Spencer')
        self.setInfo('description', """Women's french lining block, includes major changes to Ester Pivnick's original forumalas.""")
        #TODO: add new category 'Block Patterns'
        self.setInfo('category', 'Block')
        self.setInfo('type', 'French')
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
        A = bodice.addPiece('Front Center', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = bodice.addPiece('Front Side', 'B', fabric = 2, interfacing = 0, lining = 0)
        C = bodice.addPiece('Back ', 'C', fabric = 2, interfacing = 0, lining = 0)
        D = bodice.addPiece('Back Side', 'D', fabric = 2, interfacing = 0, lining = 0)
        E = bodice.addPiece('Sleeve', 'E', fabric = 2, interfacing = 0, lining = 0)

        #---new measurements---
        #90px / 1 in
        #2.54cm / 1 in
        #90 / 2.54  = px / cm


        #---Front Center A---#
        #replace these when these fields are added to php script on www.sewbuzzed.com/tools
        FRONT_WAIST_BALANCE = 42.0 * 90.0 / 2.54
        BACK_WAIST_BALANCE = 45.0 * CM
        FRONT_UNDERARM_HEIGHT = 9.0 * CM
        BACK_UNDERARM_HEIGHT = 18.0 * CM
        FRONT_BUST_HEIGHT = 18.0 * CM
        #---
        front_half_bust = CD.front_bust / 2.0
        front_half_waist = CD.front_waist / 2.0
        front_half_hip = CD.front_hip / 2.0
        front_half_abdomen = CD.front_abdomen / 2.0
        front_half_shoulder = CD.front_shoulder_width / 2.0
        FBC1 = A.addPoint('FBC1', (0.0, 0.0)) #front bust center 1
        FBS = A.addPoint('FBS', right(FBC1, front_half_bust)) #front bust side
        FUC1 = A.addPoint('FUC1', up(FBC1, FRONT_BUST_HEIGHT - FRONT_UNDERARM_HEIGHT)) #front underarm center offset
        FUC = A.addPoint('FUC', right(FUC1, front_half_bust - CD.front_underarm / 2.0)) #front underarm center
        FBP = A.addPoint('FBP', right(FBC1, CD.bust_distance / 2.0)) #front bust point
        angle1 = angleOfVector(FBP, FBC1, FUC)
        theta = ANGLE90 - angle1
        FBC = A.addPoint('FBC', intersectLineRay(FBC1, FUC, FBP, angleOfLine(FBP, FBC1) + theta)) #front bust center
        FSH = A.addPoint('FSH', onLineAtLength(FBC, FUC, CD.bust_balance)) #front shoulder height
        FWC = A.addPoint('FWC', onLineAtLength(FSH, FBC, CD.front_shoulder_height)) #front waist center
        FNC = A.addPoint('FNC', onLineAtLength(FWC, FBC, CD.front_waist_length)) #front neck center
        FSW = A.addPoint('FSW', polar(FSH, front_half_shoulder, angleOfLine(FBC, FSH) + ANGLE90))
        FAP1 = A.addPoint('FAP1', intersectLineRay(FBP, FBS, FSW, angleOfLine(FSH, FBC))) #front armscye point 1 - on bust line to define armscye curve
        FSP = B.addPoint('FSP', highestP(intersectLineCircle(FAP1, FSW, FWC, FRONT_WAIST_BALANCE))) #front shoulder point
        FNS = A.addPoint('FNS', leftmostP(intersectLineCircle(FSH, FSW, FSP, CD.shoulder))) #front neck side
        FSM1 = A.addPoint('FSM1', midPoint(FNS, FSP)) #front shoulder midpoint 1
        FSM2 = B.addPoint('FSM2', FSM1) #front shoulder midpoint 2
        FWS1 = A.addPoint('FWS1', lowestP(onCircleAtX(FNC, FRONT_WAIST_BALANCE, FBS.x))) #front waist side 1
        FUS1 = A.addPoint('FUS1', onLineAtLength(FWS1, FBS, CD.side)) #front underarm side 1
        FAP2 = A.addPoint('FAP2', onLineAtY(FSP, FAP1, FUS1.y)) #front armscye point 2 - at FUS1 height
        FAP = B.addPoint('FAP', onLineAtLength(FSP, FAP2, 0.75 * distance(FSP, FAP2))) #front armscye point - on armscye curve
        FUS2 = A.addPoint('FUS2', extendLine(FAP2, FUS1, 0.04 * front_half_bust)) # front underarm side 2 - includes 4% bust ease
        FUS = B.addPoint('FUS', onLineAtLength(FWS1, FUS2, CD.side)) #front undearm side
        FWS2 = A.addPoint('FWS2', FWS1) #front waist side 2
        slashAndSpread(FBP, -(angleOfLine(FUC, FAP2) - angleOfLine(FBP, FBS)), FWS2) #rotate FWS2 counterclockwise around FBP to work with underarm line
        FWS = A.addPoint('FWS', onLineAtLength(FUS, FWS2, CD.side)) #front waist side - inline with extended front underarm side
        FD1 = A.addPoint('FD1', onRayAtX(FWC, angleOfLine(FWC, FNC) + ANGLE90, FBP.x)) #front waist middle point - under FBP
        dart_width = distance(FWC, FD1) + distance(FD1, FWS) - front_half_waist
        FD1.i = A.addPoint('FD1.i', onLineAtLength(FD1, FWC, dart_width / 2.0)) #waist dart inside leg
        FD1.o = B.addPoint('FD1.o', onLineAtLength(FD1, FWS, dart_width / 2.0)) #waist dart outside leg
        updatePoint(FD1, FBP) #move front waist dart point up to bustline
        FD12 = B.addPoint('FD12', right(FD1, 0.5 * distance(FUS2, FUS))) #copy of FD1 for pattern piece B, moved right a small amount to account for added curve when split into 2 pattern pieces
        #extendDart(FWS, FD1, FWC)
        foldDart(FD1, FWC)
        #---extend lining to hip
        skirt_length = 0.1 * CD.front_hip_height
        FExtWC = A.addPoint('FExtWC', down(FNC, CD.front_waist_length)) #front hip extension waist center
        FAbC = A.addPoint('FAbC', down(FExtWC, 0.33 * CD.front_hip_height)) #front abdomen center
        FHC = A.addPoint('FHC', down(FExtWC, CD.front_hip_height)) #front hip center
        FHemC = A.addPoint('FHemC', extendLine(FExtWC, FHC, skirt_length)) #front hem center

        front_hip_dart_width = 0.13 * front_half_waist
        #front waist dart
        FD2 = A.addPoint('FD2', right(FExtWC, distance(FWC, FD1.i))) #front waist dart - will be updated later
        FD2.i = A.addPoint('FD2.i', FD2) #front waist dart outside leg
        FD2.o = B.addPoint('FD2.o', right(FD2.i, front_hip_dart_width)) #front waist dart inside leg
        FD2.m = midPoint(FD2.i, FD2.o)
        updatePoint(FD2, down(FD2.m, 0.8 * CD.side_hip_height)) #front waist dart point
        #extendDart(FExtWS, FD2, FWC)
        foldDart(FD2, FExtWC)

        FWM1 = A.addPoint('FWM1', FD2.i) #front waist middle 1
        FAbC1 = A.addPoint('FAbC1', intersectLineRay(FD2, FD2.i, FAbC, angleOfLine(FWC, FD2.i))) #front abdomen line at dart inside leg
        FAbM1 = onLineAtY(FD2.i, FD2, FAbC.y) #front abdomen middle 1
        FHM1 = A.addPoint('FHM1', intersectLineRay(FWM1, FAbM1, FHC, angleOfLine(FAbC, FAbM1))) #front hip middle 1
        FHemM1 = A.addPoint('FHemM1', (FD2.x, FHemC.y)) #front hem middle 1

        FHemS = B.addPoint('FHemS', right(FHemC, front_half_hip)) #front hem side
        FHS = B.addPoint('FHS', up(FHemS, skirt_length)) #front hip side
        FExtWS = B.addPoint('FExtWS', rightmostP(intersectCircles(FD2.o, distance(FD1.o, FWS), FHS, CD.side_hip_height))) #front extension waist side - includes 6.5% for dart width
        FHemM2 = B.addPoint('FHemM2', FHemM1) #front hem middle 2
        FD22 = B.addPoint('FD22', FD2) #copy of FD2
        FAbS1 = B.addPoint('FAbS1', onLineAtLength(FD2, FD2.o, distance(FD2, FAbC1))) # front abdomen line at dart outside leg
        FAbS2 = B.addPoint('FAbS2', polar(FAbS1, front_half_abdomen - distance(FAbC,  FAbC1), angleOfLine(FWC, FExtWS))) #front abdomen line at skirt side
        #FAbS front abdomen side shouldn't lie inside the line from FHS to FExtWS or else the side seam at abdomen line would be concave :(
        pnt = intersectLines(FExtWS, FHS, FAbS1, FAbS2)
        if distance(FAbS1, FAbS2) < distance(FAbS1, pnt):
            FAbS = B.addPoint('FAbS', pnt)
        else:
            FAbS = B.addPoint('FAbS', FAbS2)

        #connect front hip center with front bodice center
        connector_pnts = points2List(FWC, FD1.i)
        old_pnts = points2List(FExtWC, FD2.i, FAbC1, FD2, FHM1, FHemM1, FHemC, FHC, FAbC)
        r_pnts = connectObjects(connector_pnts, old_pnts)
        i = 0
        for pnt in FExtWC, FD2.i, FAbC1, FD2, FHM1, FHemM1, FHemC, FHC, FAbC:
            updatePoint(pnt, r_pnts[i])
            i += 1

        #connect front hip side to front bodice side
        connector_pnts = points2List(FD1.o, FWS)
        old_pnts = points2List(FD2.o, FExtWS, FAbS, FHS, FHemS, FHemM2, FD22, FAbS1)
        r_pnts = connectObjects(connector_pnts, old_pnts)
        i = 0
        for pnt in FD2.o, FExtWS, FAbS, FHS, FHemS, FHemM2, FD22, FAbS1:
            updatePoint(pnt, r_pnts[i])
            i += 1

        #---front bodice control handles
        #b/w FD2 & FD1.i
        FD2.addOutpoint(polar(FD2, distance(FD2, FD1.i) / 6.0, angleOfLine(FWC, FNC)))
        FD1.i.addInpoint(polar(FD1.i, distance(FD2, FD1.i) / 6.0, angleOfLine(FNC, FWC)))
        #b/w FD1.i front waist dart inside leg  & FD1 front bust dart point
        FD1.i.addOutpoint(polar(FD1.i, distance(FD1.i, FD1) / 6.0, angleOfLine(FWC, FNC)))
        FD1.addInpoint(polar(FD1, distance(FD1.i, FD1) / 6.0, angleOfLine(FSM1, FD1.i)))
        #b/w FD1 front bust dart point & FSM1 front shoulder midpoint1
        FD1.addOutpoint(polar(FD1, distance(FD1, FSM1) / 6.0, angleOfLine(FD1.i, FSM1)))
        FSM1.addInpoint(polar(FSM1, distance(FD1, FSM1) / 6.0, angleOfLine(FSM1, FD1)))

        #b/w FSM2 front shoulder midpoint2 & FD12 front bust dart point b
        FSM2.addOutpoint(polar(FSM2, distance(FSM2, FD12) / 6.0, angleOfLine(FSM2, FD12)))
        FD12.addInpoint(polar(FD12, distance(FSM2, FD12) / 6.0, angleOfLine(FD1.o, FSM2)))
        #b/w FD12 front bust dart point b & FD1.o front bust dart point outside leg
        FD12.addOutpoint(polar(FD12, distance(FD12, FD1.o) / 6.0, angleOfLine(FSM2, FD1.o)))
        FD1.o.addInpoint(polar(FD1.o, distance(FD12, FD1.o) / 6.0, angleOfLine(FD1.o, FWS) - ANGLE90))
        #b/w FD1.o & FD22
        FD1.o.addOutpoint(polar(FD1.o, distance(FD1.o, FD22) / 6.0, angleOfLine(FD1.o, FWS) + ANGLE90))
        FD22.addInpoint(polar(FD22, distance(FD22, FD1.o) / 6.0,  angleOfLine(FHemM2, FD22)))

        #b/w FUS front underarm side & FAP front armscye point
        FUS.addOutpoint(polar(FUS, distance(FUS, FAP) / 3.0, angleOfLine(FUS, FWS) + ANGLE90))
        FAP.addInpoint(polar(FAP, distance(FUS, FAP) / 3.0, angleOfLine(FSP, FUS)))
        #b/w FAP front armscye point & FSP front shoulder point
        FAP.addOutpoint(polar(FAP, 0.33 * distance(FAP, FSP), angleOfLine(FUS, FSP)))
        FSP.addInpoint(polar(FSP, 0.33 * distance(FAP, FSP), angleOfLine(FNS, FSP) + ANGLE90))
        #b/w FNS front neck side & FNC front neck center
        FNC.addInpoint(polar(FNC, 0.5 * abs(FNS.x - FNC.x), angleOfLine(FWC, FNC) + ANGLE90))
        FNS.addOutpoint(polar(FNS, 0.5 * abs(FNS.y - FNC.y), angleOfLine(FNS, FSP) + ANGLE90))
        #---front hip extension control handles
        #b/w FHemS front hem side & FHS front hip side
        FHemS.addOutpoint(polar(FHemS, distance(FHemS, FHS) / 6.0, angleOfLine(FHemS, FHS))) #short control handle
        FHS.addInpoint(polar(FHS, distance(FHemS, FHS) / 6.0,  angleOfLine(FAbS, FHemS))) #short control handle
        #b/w FHS front hip side & FAbS front abdomen side
        FHS.addOutpoint(polar(FHS, distance(FHS, FAbS) / 6.0, angleOfLine(FHemS, FAbS))) #short control handle
        FAbS.addInpoint(polar(FAbS, distance(FHS, FAbS) / 6.0, angleOfLine(FExtWS, FHS))) #short control handle
        #b/w FAbS front abdomen side & FExtWS front waist side hips extension
        FAbS.addOutpoint(polar(FAbS, distance(FAbS, FExtWS) / 6.0, angleOfLine(FHS, FExtWS))) #short control handle
        FExtWS.addInpoint(polar(FExtWS, distance(FAbS, FExtWS) / 6.0, angleOfLine(FUS, FAbS))) #short control handle
        #b/w FExtWS front waist side hip extension & FUS front underarm side
        FExtWS.addOutpoint(polar(FExtWS, distance(FExtWS, FUS) / 6.0, angleOfLine(FAbS, FUS))) #short control handle
        FUS.addInpoint(polar(FUS, distance(FExtWS, FUS) / 6.0, angleOfLine(FUS, FExtWS))) #short control handle

        #---Back D---#
        back_half_waist = CD.back_waist / 2.0
        back_half_hip = CD.back_hip / 2.0
        back_half_abdomen = CD.back_abdomen / 2.0
        back_half_shoulder = CD.back_shoulder_width / 2.0
        back_half_underarm = CD.back_underarm / 2.0
        back_half_waist = CD.back_waist / 2.0
        #---
        BSH = D.addPoint('BSH', (0.0, 0.0)) #back shoulder height
        BSW = D.addPoint('BSW', left(BSH, back_half_shoulder)) #back shoulder width
        BUW = D.addPoint('BUW', left(BSH, back_half_underarm)) #back undearm width
        BWC = D.addPoint('BWC', down(BSH, CD.back_shoulder_height)) #back waist center
        BNC = D.addPoint('BNC', up(BWC, CD.back_waist_length)) #back neck center
        BSP1 = D.addPoint('BSP1', highestP(onCircleAtX(BWC, CD.back_shoulder_balance, BSW.x))) #back shoulder point 1
        BNS = D.addPoint('BNS', rightmostP(onCircleAtY(BSP1, CD.shoulder, BSH.y))) #back neck side
        BSP = D.addPoint('BSP', extendLine(BNS, BSP1, 0.07 * CD.shoulder)) #BSP - incl. 7% ease for shoulder dart
        BAP = D.addPoint('BAP', down(BSP1, 1.1 * distance(FSP, FAP))) #back armscye point
        BWS1 = D.addPoint('BWS1', lowestP(onCircleAtX(BNC, BACK_WAIST_BALANCE, BUW.x))) #back waist side
        #back waist dart
        back_bust_dart_width = (distance(BWS1, BWC) - back_half_waist) / 2.0
        BWS2 = D.addPoint('BWS2', onLineAtLength(BWS1, BWC, back_bust_dart_width)) #back waist side 2
        BD1 = D.addPoint('BD1', midPoint(BWS2, BWC)) #back waist dart point - on waist line, will be updated later
        BD1.i = D.addPoint('BD1.i', onLineAtLength(BD1, BWC, back_bust_dart_width / 2.0)) #back waist dart inside leg
        BD1.o = D.addPoint('BD1.o', onLineAtLength(BD1, BWS2, back_bust_dart_width / 2.0)) #back waist dart outside leg
        BWS3 = D.addPoint('BWS3', onLineAtLength(BAP, BWS2, distance(BAP, BWS1))) #back waist side
        BUS1 = D.addPoint('BUS1', highestP(onCircleAtX(BWS3, CD.side, BUW.x))) #back underarm side 1
        BUC = D.addPoint('BUC', (BNC.x, BUS1.y)) #back underarm center
        BUS2 = D.addPoint('BUS2', extendLine(BUC, BUS1, 0.04 * back_half_underarm)) #back underarm side 2 - inc. 4% bust ease
        BUS3 = D.addPoint('BUS3', onLineAtLength(BWS3, BUS2, CD.side)) #back underarm side
        BUS = D.addPoint('BUS', BUS3)
        updatePoint(BD1, (BD1.x, BUC.y)) #move BD1 dart point up to underarm line
        slashAndSpread(BD1, -angleOfVector(BD1.i, BD1, BD1.o), BUS)
        BWS = D.addPoint('BWS', onLineAtLength(BUS, BWS3, CD.side))
        extendDart(BWS, BD1, BWC, extension=0.5)
        foldDart(BD1, BWC)
        #back shoulder dart
        BD2 = D.addPoint('BD2', midPoint(BNS, BSP))
        BD2.i = D.addPoint('BD2.i', onLineAtLength(BD2, BNS, 0.035 * CD.shoulder)) #back shoulder dart inside leg
        BD2.o = D.addPoint('BD2.o', onLineAtLength(BD2, BSP, 0.035 * CD.shoulder)) #back shoulder dart outside leg
        updatePoint(BD2, polar(BD2, distance(BSP, BAP) / 2.0, angleOfLine(BD2.o, BD2.i) + ANGLE90)) #move BD2 dart point
        extendDart(BSP, BD2, BNS)
        foldDart(BD2, BNS)
        BD1b = D.addPoint('BD1b', BD1) #copy of BD1
        BD2b = D.addPoint('BD2b', BD2) #copy of BD2

        #---back control handles D
        #b/w BD1.i & BD1
        BD1.i.addOutpoint(polar(BD1.i, distance(BD1.i, BD1) / 6.0, angleOfLine(BD1.i, BD1)))
        BD1.addInpoint(polar(BD1, distance(BD1.i, BD1) / 6.0, angleOfLine(BD2, BD1.i)))
        #b/w BD1 & BD2
        BD1.addOutpoint(polar(BD1, distance(BD1, BD2) / 6.0, angleOfLine(BD1.i, BD2)))
        BD2.addInpoint(polar(BD2, distance(BD1, BD2) / 6.0, angleOfLine(BD2.i, BD1)))
        #b/w BD2 & BD2.i
        BD2.addOutpoint(polar(BD2, distance(BD2, BD2.i) / 6.0, angleOfLine(BD1, BD2.i)))
        BD2.i.addInpoint(polar(BD2.i, distance(BD2, BD2.i) / 6.0, angleOfLine(BD2.i, BD2)))

        #---back control handles C
        #b/w BD2.o & BD2b
        BD2.o.addOutpoint(polar(BD2.o, distance(BD2.o, BD2b) / 6.0, angleOfLine(BD2.o, BD2b)))
        BD2b.addInpoint(polar(BD2b, distance(BD2.o, BD2b) / 6.0, angleOfLine(BD1b, BD2.o)))
        #b/w BD2b & BD1b
        BD2b.addOutpoint(polar(BD2b, distance(BD2b, BD1b) / 6.0, angleOfLine(BD2.o, BD1b)))
        BD1b.addInpoint(polar(BD1b, distance(BD2b, BD1b) / 6.0, angleOfLine(BD1.o, BD2b)))
        #b/w BD1b & BD1.o
        BD1b.addOutpoint(polar(BD1b, distance(BD1b, BD1.o) / 6.0, angleOfLine(BD2b, BD1.o)))
        BD1.o.addInpoint(polar(BD1.o, distance(BD1b, BD1.o) / 6.0, angleOfLine(BD1.o, BD1b)))
        #b/w BUS back underarm side & BAP back armscye point
        BUS.addOutpoint(polar(BUS, 0.5 * abs(BUS.x - BAP.x), angleOfLine(BWS, BUS) + ANGLE90))
        BAP.addInpoint(polar(BAP, 0.5 * abs(BUS.y - BAP.y), angleOfLine(BSP, BUS)))
        #b/w BAP back armscye point & BSP back shoulder point
        BAP.addOutpoint(polar(BAP, 0.33 * distance(BAP, BSP), angleOfLine(BUS, BSP)))
        BSP.addInpoint(polar(BSP, 0.33 * distance(BAP, BSP), angleOfLine(BSP, BNS) + ANGLE90))
        #b/w BNS back neck side & bNC back neck center
        BNC.addInpoint(polar(BNC, 0.5 * abs(BNS.x - BNC.x), angleOfLine(BNC, BWC) + ANGLE90))
        BNS.addOutpoint(polar(BNS, 0.5 * abs(BNS.y - BNC.y), angleOfLine(BSP, BNS) + ANGLE90))

        #---Sleeve E---#
        SCM = E.addPoint('SCM',(0, 0) ) #sleeve cap middle
        SWM = E.addPoint('SWM', down(SCM, CD.oversleeve_length)) #sleeve wrist middle
        SBM1 = E.addPoint('SBM1', up(SWM, CD.undersleeve_length)) #sleeve bicep middle
        SEM = E.addPoint('SEM', down(SBM1, 0.45 * CD.undersleeve_length)) #sleeve elbow middle

        SBF1 = E.addPoint('SBF1', left(SBM1, 0.5 * CD.bicep)) #sleeve bicep front 1
        SBB1 = E.addPoint('SBB1', right(SBM1, 0.5 * CD.bicep)) #sleeve bicep back 1

        SBM = E.addPoint('SBM', up(SBM1, 0.15 * distance(SBM1, SCM))) #sleeve bicep middle
        SBF = E.addPoint('SBF', leftmostP(onCircleAtY(SCM, distance(SCM, SBF1), SBM.y))) #sleeve bicep front
        SBB = E.addPoint('SBB', rightmostP(onCircleAtY(SCM, distance(SCM, SBB1), SBM.y))) #sleeve bicep front

        SCF1 = E.addPoint('SCF1', right(SBF, 0.25 * distance(SBF, SBM))) #sleeve cap front 1
        SCF4 = E.addPoint('SCF4', left(SCM, distance(SBF, SCF1))) #sleeve cap front 4 - to left of SCM
        SCF2 = E.addPoint('SCF2', onLineAtLength(SCF1, SCF4, distance(SBF, SCF1))) #sleeve cap front 2
        SCF3 = E.addPoint('SCF3', onLineAtLength(SCF4, SCF1, distance(SCM, SCF4))) #sleeve cap front 3

        SCB4 = E.addPoint('SCB4', left(SBB, 0.5 * distance(SBF, SCF1))) #sleeve cap back 4
        SCB1 = E.addPoint('SCB1', right(SCM, distance(SBF, SCF1) + distance(SBB, SCB4))) # sleeve cap back 1 - ro right of SCM
        SCB2 = E.addPoint('SCB2', onLineAtLength(SCB1, SCB4, distance(SCM, SCB1))) # sleeve cap back 2
        SCB3 = E.addPoint('SCB3', onLineAtLength(SCB4, SCB1, distance(SBB, SCB4))) #sleeve cap back 3

        SEF = E.addPoint('SEF', left(SEM, 0.5 * CD.elbow)) #sleeve elbow front
        SEB = E.addPoint('SEB', right(SEM, 0.5 * CD.elbow)) #sleeve elbow back
        SEB1 = E.addPoint('SEB1', midPoint(SEM, SEB)) #midpoint b/w SEM & SEB

        SWF1 = E.addPoint('SWF1', left(SWM, 0.5 * CD.wrist)) #sleeve wrist forward 1
        SWM1 = E.addPoint('SWM1', rightmostP(onCircleTangentFromOutsidePoint(SWF1, 0.5 * CD.wrist, SEB1))) #sleeve wrist middle 1 - extend down wrist middle point
        SWB = E.addPoint('SWB', extendLine(SWF1, SWM1, 0.25 * CD.wrist)) #sleeve wrist back
        SWF2 = E.addPoint('SWF2', midPoint(SWF1, SWM1)) #sleeve wrist front 2 - begin wrist curve
        SWF = E.addPoint('SWF', leftmostP(onCircleAtY(SWF1, 0.25 * CD.wrist, SWF2.y))) #sleeve wrist front
        #sleeve elow darts
        sleeve_diff = (distance(SBB, SEB) + distance(SEB, SWB)) - (distance(SBF, SEF) + distance(SEF, SWF))
        dart_width = sleeve_diff / 3.0
        dart_length = 0.4 * distance(SEB, SEM)
        SD1 = E.addPoint('SD1', onLineAtLength(SEB, SBB, 2 * dart_width))
        SD2 = E.addPoint('SD2', onLineAtLength(SEB, SWB, 0.5 * dart_width))
        SD3 = E.addPoint('SD3', onLineAtLength(SEB, SWB, 2.5 * dart_width))
        SD1.i = E.addPoint('SD1.i', SD1)
        SD1.o = E.addPoint('SD1.o', onLineAtLength(SD1.i, SEB, dart_width))
        SD1.m = midPoint(SD1.i, SD1.o)
        updatePoint(SD1, polar(SD1.m, dart_length, angleOfLine(SD1.i, SD1.o) + ANGLE90))
        extendDart(SEB, SD1, SBB)
        foldDart(SD1, SBB)
        SD2.i = E.addPoint('SD2.i', SD2)
        SD2.o = E.addPoint('SD2.o', onLineAtLength(SD2.i, SWB, dart_width))
        SD2.m = midPoint(SD2.i, SD2.o)
        updatePoint(SD2, polar(SD2.m, dart_length, angleOfLine(SD2.i, SD2.o) + ANGLE90))
        extendDart(SWB, SD2, SD1.o)
        foldDart(SD2, SD1.o)
        SD3.i = E.addPoint('SD3.i', SD3)
        SD3.o = E.addPoint('SD3.o', onLineAtLength(SD3.i, SWB, dart_width))
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



        #draw Front Center A
        pnt1 = dPnt((FSH.x, FNC.y + 0.75 * distance(FNC, FUC)))
        A.setLabelPosition((pnt1.x, pnt1.y))
        A.setLetter(up(pnt1, 0.5 * IN), scaleby=10.0)
        AG1 = dPnt(polar(FUC, distance(FUC, pnt1)/2.0, angleOfLine(FWC, FD1.i)))
        AG2 = dPnt(polar(AG1, 0.75 * distance(FNC, FWC), angleOfLine(FNC, FWC)))
        A.addGrainLine(AG1, AG2)
        A.addGridLine(['M', FAP1, 'L', FSW, 'L', FSH, 'L', FWC, 'L', FD1.i, 'M', FBC1, 'L', FUC1, 'L', FUC,  'M', FBC, 'L', FBP, 'M', FBC1, 'L', FBS, 'M', FWC, 'L', FSP, 'L', FSM1, 'M', FNC, 'L', FWS1, 'M', FAP2, 'L', FUS1, 'M', FBP, 'L', FD1.o, 'L', FWS, 'L', FUS, 'M', FUS1, 'L', FWS1, 'M', FUC, 'L', FAP2, 'L', FUS, 'M', FWC, 'L', FHemC, 'M', FAbC, 'L', FAbC1, 'M', FAbS1, 'L', FAbS, 'M', FD1.o, 'L', FAbS1, 'L', FD22, 'L', FHemM2, 'L', FHemS, 'L', FHS, 'L', FAbS, 'L', FWS])
        pth = (['M', FNC, 'L', FWC, 'L', FHemC, 'L',  FHemM1, 'L', FD2, 'C', FD1.i, 'C', FD1, 'C', FSM1, 'L', FNS, 'C', FNC])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        #draw Front Side B
        pnt1 = dPnt((FNS.x, FBC.y))
        B.setLabelPosition((pnt1.x, pnt1.y))
        B.setLetter(up(pnt1, 0.5 * IN), scaleby=10.0)
        #BG1 = dPnt(right(FD1, 0.75 * distance(FD1, FUS)))
        BG1 = dPnt((FAP.x, pnt1.y))
        BG2 = dPnt(polar(BG1, 0.75 * distance(FD1, FHemM1), angleOfLine(FD1.o, FWS) + ANGLE90))
        B.addGrainLine(BG1, BG2)
        pth = (['M', FD1.o, 'L', FWS, 'M', FAbS1, 'L', FAbS])
        B.addGridLine(pth)
        pth = (['M', FSM2, 'C', FD12, 'C', FD1.o, 'C', FD22, 'L', FHemM2, 'L', FHemS, 'C', FHS, 'C', FAbS, 'C', FExtWS, 'L', FUS, 'C', FAP, 'C', FSP, 'L', FSM2])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        #draw Back Side C
        pnt1 = dPnt((BD2.o.x - (0.5 * abs(BSP.x - BD2.o.x)), BUC.y))
        C.setLabelPosition((pnt1.x, pnt1.y))
        C.setLetter(up(pnt1, 0.5 * IN), scaleby=10.0)
        #BG1 = dPnt(right(BD1, 0.75 * distance(BD1, BUS)))
        CG1 = dPnt((BAP.x, pnt1.y))
        CG2 = dPnt(down(CG1, 0.5 * distance(BNC, BWC)))
        C.addGrainLine(CG1, CG2)
        pth = (['M', BD2.o, 'C', BD2b, 'C', BD1b, 'C', BD1.o, 'L', BWS, 'L', BUS, 'C', BAP, 'C', BSP, 'L', BD2.o])
        C.addSeamLine(pth)
        C.addCuttingLine(pth)

        #draw Back D
        pnt1 = dPnt((BSH.x - abs(BSH.x - BSP.x) / 2.0, BSH.y + abs(BSH.y - BWC.y) / 3.0 ))
        D.setLabelPosition((pnt1.x, pnt1.y))
        D.setLetter(up(pnt1, 0.5 * IN), scaleby=10.0)
        #DG1 = dPnt(left(BUC, distance(BUC, pnt1)/4.0))
        #DG2 = dPnt(down(DG1, 0.75 * distance(BNC, BWC)))
        #D.addGrainLine(BG1, BG2)
        D.addGridLine(['M', BUW, 'L', BSH, 'L', BWC, 'L', BSP1, 'L', BSW, 'M', BSP1, 'L', BAP, 'L', BWS, 'M', BAP, 'L', BWS1, 'M', BUS2, 'L', BUC, 'M', BUW, 'L', BWS1, 'M', BNC, 'L', BWS1])
        pth = (['M', BNC, 'L', BWC, 'L', BD1.i, 'C', BD1, 'C', BD2, 'C', BD2.i, 'L', BNS, 'C', BNC])
        D.addSeamLine(pth)
        D.addCuttingLine(pth)

        #draw Sleeve E
        pnt1 = dPnt((SCF2.x, SBF.y + abs(SBF.y - SEF.y) / 2.0 ))
        E.setLabelPosition((pnt1.x, pnt1.y))
        E.setLetter(up(pnt1, 0.5 * IN), scaleby=10.0)
        CG1 = dPnt((SBM1.x, SBM1.y))
        CG2 = dPnt(down(CG1, 0.75 * distance(SBM1, SWM)))
        E.addGrainLine(CG1, CG2)
        E.addDartLine(['M', SD1.ic, 'L', SD1, 'L', SD1.oc, 'M', SD2.ic, 'L', SD2, 'L', SD2.oc, 'M', SD3.ic, 'L', SD3, 'L', SD3.oc])
        E.addGridLine(['M', SCM, 'L', SWM, 'M', SBF, 'L', SBB, 'M', SEF, 'L', SEB, 'M', SWF1, 'L', SWB, 'M', SEB1, 'L', SWM1, 'M', SCF1, 'L', SCF4, 'L', SCB1, 'L', SCB4])
        pth = (['M', SBF, 'C', SCM, 'C', SCB3, 'C', SBB, 'L', SD1.i, 'L', SD1.m, 'L', SD1.o, 'L', SD2.i, 'L', SD2.m, 'L', SD2.o, 'L', SD3.i, 'L', SD3.m, 'L', SD3.o, 'L', SWB, 'L', SWF2, 'C', SWF, 'L', SEF, 'L', SBF])
        E.addSeamLine(pth)
        E.addCuttingLine(pth)

        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

