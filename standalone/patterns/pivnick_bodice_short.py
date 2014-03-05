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
        FAP = A.addPoint('FAP', midPoint(FSP, FAP1)) #front armscye point - on armscye curve
        FWS = A.addPoint('FWS', lowestP(onCircleAtX(FNC, FRONT_WAIST_BALANCE, FBS.x))) #front waist side
        FUS1 = A.addPoint('FUS1', onLineAtLength(FWS, FBS, CD.side)) #front underarm side 1
        FAP2 = A.addPoint('FAP2', onLineAtY(FSP, FAP1, FUS1.y)) #front armscye point 2 - at FUS1 height
        FUS2 = A.addPoint('FUS2', extendLine(FAP2, FUS1, 0.06 * CD.front_bust / 2.0)) # front underarm side 2 - includes 6% bust ease
        FUS = A.addPoint('FUS', onLineAtLength(FWS, FUS2, CD.side)) #front undearm side
        FWM = A.addPoint('FDM', onRayAtX(FWC, angleOfLine(FWC, FNC) + ANGLE90, FBP.x)) #front waist middle point - under FBP
        FD1 = A.addPoint('FD1', FBP) #front waist dart
        dart_width = CD.front_waist / 2.0 - distance(FWC, FWM) - distance(FWM, FWS)
        FD1.i = A.addPoint('FD1.i', onLineAtLength(FWM, FWC, dart_width / 2.0)) #waist dart inside leg
        FD1.o = A.addPoint('FD1.o', onLineAtLength(FWM, FWS, dart_width / 2.0)) #waist dart outside leg


        #---front control handles
        #b/w FUS front underar side & FAP front armscye point
        FUS.addOutpoint(polar(FUS, 0.5 * abs(FUS.x - FAP.x), angleOfLine(FUS, FWS) + ANGLE90))
        FAP.addInpoint(polar(FAP, 0.5 * abs(FUS.y - FAP.y), angleOfLine(FSP, FUS)))
        #b/w FAP front armscye point & FSP front shoulder point
        FAP.addOutpoint(polar(FAP, 0.33 * distance(FAP, FSP), angleOfLine(FUS, FSP)))
        FSP.addInpoint(polar(FSP, 0.33 * distance(FAP, FSP), angleOfLine(FNS, FSP) + ANGLE90))
        #b/w FNS front neck side & FNC front neck center
        FNC.addInpoint(polar(FNC, 0.5 * abs(FNS.x - FNC.x), angleOfLine(FWC, FNC) + ANGLE90))
        FNS.addOutpoint(polar(FNS, 0.5 * abs(FNS.y - FNC.y), angleOfLine(FNS, FSP) + ANGLE90))

        #draw Front A
        pnt1 = dPnt((FNS.x, FUC.y))
        A.setLabelPosition((pnt1.x, pnt1.y))
        A.setLetter(up(pnt1, 0.5 * IN), scaleby=10.0)
        #aG1 = dPnt(left(FUC, distance(FUC, pnt1)/4.0))
        #aG2 = dPnt(down(aG1, 0.75 * distance(FNC, FWC)))
        #A.addGrainLine(aG1, aG2)
        A.addGridLine(['M', FAP1, 'L', FSW, 'L', FSH, 'L', FWC, 'M', FBC1, 'L', FUC1, 'L', FUC,  'M', FBC, 'L', FBP, 'M', FBC1, 'L', FBS, 'M', FWC, 'L', FSP, 'M', FNC, 'L', FWS, 'M', FAP2, 'L', FUS1, 'M', FBP, 'L', FWM, 'M', FD1.i, 'L', FD1, 'L', FD1.o, 'M', FWS, 'L', FUS1])
        pth = (['M', FNC, 'L', FWC, 'L', FWM, 'L', FWS, 'L', FUS, 'C', FAP, 'C', FSP, 'L', FNS, 'C', FNC])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)


        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

