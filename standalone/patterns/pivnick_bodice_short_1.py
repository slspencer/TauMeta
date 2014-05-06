#!/usr/bin/env python
# patternName: Block_Women_Bodice_Short_Pivnick
# patternNumber: Bl_W_Bodice_Short_Pivnick

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
        self.setInfo('patternNumber', 'Bl_W_Bodice_Short_Pivnick')
        self.setInfo('patternTitle', 'Womens Bodice Block - Short - Pivnick')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'Ester Pivnick')
        self.setInfo('patternmakerName', 'S. L. Spencer')
        self.setInfo('description', """Women's short bodice block""")
        #TODO: add new category 'Block Patterns'
        self.setInfo('category', 'Block')
        self.setInfo('type', 'block')
        self.setInfo('gender', 'F') # 'M',  'F',  or ''
        #
        # The next group are all optional
        #
        self.setInfo('recommendedFabric', '')
        self.setInfo('recommendedNotions', '')
        #
        #self.setInfo('yearstart', '1950' )
        #self.setInfo('yearend', '1959')
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
        FWS = A.addPoint('FWS', lowestP(onCircleAtX(FNC, FRONT_WAIST_BALANCE, FBS.x))) #front waist side
        FUS1 = A.addPoint('FUS1', onLineAtLength(FWS, FBS, CD.side)) #front underarm side 1
        FAP2 = A.addPoint('FAP2', onLineAtY(FSP, FAP1, FUS1.y)) #front armscye point 2 - at FUS1 height
        FAP = A.addPoint('FAP', onLineAtLength(FSP, FAP2, 0.75 * distance(FSP, FAP2))) #front armscye point - on armscye curve
        FUS2 = A.addPoint('FUS2', extendLine(FAP2, FUS1, 0.06 * CD.front_bust / 2.0)) # front underarm side 2 - includes 6% bust ease
        FUS3 = A.addPoint('FUS3', onLineAtLength(FWS, FUS2, CD.side)) #front undearm side
        FUS = A.addPoint('FUS', intersectLines(FUC, FAP2, FUS3, FWS))
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
        BWS = B.addPoint('BWS', onLineAtLength(BAP, BWS2, distance(BAP, BWS1))) #back waist side
        BUS1 = B.addPoint('BUS1', highestP(onCircleAtX(BWS, CD.side, BUW.x))) #back underarm side 1
        BUC = B.addPoint('BUC', (BNC.x, BUS1.y)) #back underarm center
        BUS2 = B.addPoint('BUS2', extendLine(BUC, BUS1, 0.06 * CD.back_underarm / 2.0)) #back underarm side 2 - inc. 6% bust ease
        BUS = B.addPoint('BUS', onLineAtLength(BWS, BUS2, CD.side)) #back underarm side
        updatePoint(BD1, (BD1.x, BUC.y)) #move BD1 dart point up to underarm line
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

        #draw Front A
        pnt1 = dPnt((FNS.x, FUC.y))
        A.setLabelPosition((pnt1.x, pnt1.y))
        A.setLetter(up(pnt1, 0.5 * IN), scaleby=10.0)
        #AG1 = dPnt(left(FUC, distance(FUC, pnt1)/4.0))
        #AG2 = dPnt(down(AG1, 0.75 * distance(FNC, FWC)))
        #A.addGrainLine(AG1, AG2)
        A.addDartLine(['M', FD1.ic, 'L', FD1, 'L', FD1.oc])
        A.addGridLine(['M', FAP1, 'L', FSW, 'L', FSH, 'L', FWC, 'M', FBC1, 'L', FUC1, 'L', FUC,  'M', FBC, 'L', FBP, 'M', FBC1, 'L', FBS, 'M', FWC, 'L', FSP, 'M', FNC, 'L', FWS, 'M', FAP2, 'L', FUS1, 'M', FBP, 'L', FD1.m, 'M', FWS, 'L', FUS1, 'M', FUC, 'L', FUS])
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

        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

