#!/usr / bin / env python
#Spencer_block_Bodice_Fitted_14.py

# This file is part of the tmtp (Tau Meta Tau Physica) project.
# For more information,  see http://www.taumeta.org /
#
# Copyright (C) 2010,  2011,  2012,  2013,  2014 Susan Spencer,  Steve Conklin
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation,  either version 3 of the License,  or
# (at your option) any later version. Attribution must be given in
# all derived works.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not,  see <http://www.gnu.org / licenses/>.
#

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

        #front
        front_waist_balance = 42.0 * CM
        back_waist_balance = 45.0 * CM
        front_underarm_height = 9.0 * CM
        back_underarm_height = 18.0 * CM
        front_bust_height = 18.0 * CM

        FNC = A.addPoint('FNC', (0.0, 0.0)) #front neck center
        FWC = A.addPoint('FWC', down(FNC, CD.front_waist_length)) #front waist center
        FSH = A.addPoint('FSH', up(FWC, CD.front_shoulder_height)) #front shoulder height
        FSW = A.addPoint('FSW', right(FSH, CD.front_shoulder_width / 2.0)) #front shoulder width

        FUC = A.addPoint('FUC', down(FNC, front_underarm_height)) #front underarm center
        FUS = A.addPoint('FUS', right(FUC, CD.front_underarm / 2.0)) #front underarm side
        #FAC = down(FNC, distance(FNC,  FUC) / 2.0) #front across chest center
        FAC = A.addPoint('FAC', down(FNC, 0.75 * distance(FNC,  FUC))) #front across chest center - 3 / 4ths of FNC to  FUC
        FAS = A.addPoint('FAS', right(FAC, CD.across_chest / 2.0)) #front across chest side
        FSP = A.addPoint('FSP', highestP(onCircleAtX(FWC, CD.front_shoulder_balance, FSW.x))) #front shoulder point

        FNS = A.addPoint('FNS', highestP(intersectCircles(FSP, CD.shoulder, FWC, CD.front_shoulder_balance))) #front neck side
        FAP = A.addPoint('FAP', (FAS.x, FUC.y)) #front armscye point
        FBC = A.addPoint('FBC', down(FNC, front_bust_height)) #front bust center
        FBP = A.addPoint('FBP', right(FBC, CD.bust_distance / 2.0))
        FBS1 = A.addPoint('FBS1', right(FBC, CD.front_bust / 2.0)) #front bust side 1
        FBS = A.addPoint('FBS', polar(FBP, distance(FBP, FBS1), -angleOfVector(FUS, FBP, FBS1) / 2.0))  #front bust side - adjusted up by 1/2 angle of front dart apex to underarm...angle sweeps counterclockwise

        for pnt in FBP, FNC,  FWC,  FUC, FUS, FAC, FAS, FNS, FSP, FAP, FBC, FBS:
            print pnt.id, pnt.x, pnt.y

        FWS1 = A.addPoint('FWS1', lowestP(intersectCircles(FNC, front_waist_balance, FBS, CD.side - distance(FUS, FBS)))) #front waist side
        #FWS1 = A.addPoint('FWS1', lowestP(intersectLineCircle(FUS, FBS, FNC, front_waist_balance))) #front waist side
        FWS = A.addPoint('FWS', FWS1)
        FD2.b1 = A.addPoint('FD2.b1', intersectLines(FNC, FWS, FBP, FBS)) #point on inside leg of bust dart where it crosses front waist balance
        FD2.b2 = A.addPoint('FD2.b2', FD2.b1) #copy of FD2.b1

        #front waist dart
        FD1 = A.addPoint('FD1', down(FBP, abs(FBP.y - FWC.y) / 7.0)) #front dart point is lower than FBP
        FWM = A.addPoint('FWM', (FD1.x,  FWC.y)) #below dart point at waist
        FD1.i = A.addPoint('FD1.i', left(FWM, distance(FWC, FWM) / 5.0)) #dart inside leg
        FD1.o = A.addPoint('FD1.o', lowestP(intersectCircles(FD1, distance(FD1, FD1.i), FWS, CD.front_waist / 2.0 - distance(FWC, FD1.i)))) #dart outside leg

        #front bust dart
        FD2 = A.addPoint('FD2', FBP) #bust dart point
        FD2.i = A.addPoint('FD2.i', intersectLines(FUS, FWS, FBP, FBS)) #bust dart inside leg
        FD2.o = A.addPoint('FD2.o', right(FBP, distance(FBP, FD2.i))) #bust dart outside leg
        #updatePoint(FD2, right(FBP, distance(FBP, FD1))) #bust dart point is to the right of FBP,  same distance away from FBP as FD1
        updatePoint(FD2, polar(FBP, distance(FBP, FD1), angleOfLine(FBP, FD2.i) + 0.5 * angleOfVector(FD2.i, FBP, FD2.o))) #bust dart point is to the right of FBP,  same distance away from FBP as FD1
        slashAndSpread(FBP, angleOfVector(FD2.i, FBP, FD2.o), FWS, FD2.b2, FD1.o)
        updatePoint(FD2.b1, intersectLines(FNC, FD2.b1, FD2, FD2.i))
        updatePoint(FD2.b2, onLineAtLength(FD2, FD2.o, distance(FD2, FD2.b1)))
        updatePoint(FWS, lowestP(intersectCircles(FD2.o, distance(FD2.o, FWS), FD2.b2, front_waist_balance - distance(FNC, FD2.b1))))
        updatePoint(FD1.o, lowestP(intersectCircles(FD1, distance(FD1, FD1.i),FWS, CD.front_waist / 2.0-distance( FWC, FD1.i))))

        #create curve at dart base,  then shape dart fold to match curve
        extendDart(FWS, FD1, FWC, extension = 0.5)
        updatePoint(FD1.o, lowestP(intersectCircles(FD1, distance(FD1, FD1.o),FWS, CD.front_waist / 2.0 - distance( FWC, FD1.i))))
        foldDart(FD1, FWC) #creates FD1.m, FD1.oc, FD1.ic; dart folds in toward pattern center  FWC
        #do not call adjustDartLength(FWS, FD2, FUS) -- dart FD2 is not on a curve
        foldDart(FD2, FUS) #creates FD2.m, FD2.oc, FD2.ic; dart folds up toward underarm FUS

        #front control points
        #front armscye control points
        #b/w FSP & FAS, b/w FAS & FUS
        length1 = distance(FSP, FAS) / 3.0
        length2 = distance(FAS, FUS) / 3.0
        FSP.addOutpoint(polar(FSP, length1, angleOfLine(FNS, FSP) + ANGLE90))
        angle = angleOfLine(FUS, FSP)
        angle2 = angleOfLine(FAS, FSP.outpoint)
        angle3 = (angle + angle2) / 2.0
        #FUS.c2 = polar(FUS, length2, angleOfLine(FUS, FWS)+ANGLE90)
        FUS.addInpoint(polar(FUS, length2, angleOfLine(FD2.i, FBP)))
        FAS.addInpoint(polar(FAS, length1, angle3))
        FAS.addOutpoint(polar(FAS, length2, angle3-ANGLE180))

        #front waist control points b/w FWS & FD1.o
        length = distance(FWS, FD1.o) / 6.0 #from FWS to FD1.o
        #FD1.o.c1 = polar(FWS, length, angleOfLine(FWS, FD1.o))
        FWS.addOutpoint(polar(FWS, length, angleOfLine(FWS, FD1.o)))
        #FD1.o.c2 = polar(FD1.o, length, angleOfLine(FD1.o, FWS))
        #FD1.o.c2 = polar(FD1.o, length, angleOfLine(FD1.m, FD1.o))
        FD1.o.addInpoint(polar(FD1.o, length, angleOfLine(FD1.m, FD1.o)))

        #b/w FD1.i & FWC
        #FWC.c2 = right(FWC, distance(FWC, FD1.i) / 2.0)
        #FWC.c1 = polar(FD1.i, distance( FWC, FD1.i) / 6.0, angleOfLine(FD1.i,  FWC.c2))
        FWC.addInpoint(right(FWC, distance(FWC, FD1.i) / 2.0))
        FD1.i.addOutpoint(polar(FD1.i, distance(FWC, FD1.i) / 6.0, angleOfLine(FD1.i,  FWC.inpoint)))

        #front neck control points b/w FNC & FNS
        #FNS.c1 = right(FNC, abs(FNC.x - FNS.x)*4 / 5.0)
        #FNS.c2 = polar(FNS, distance(FNS, FNS.c1) / 2.0, angleOfLine(FNS, FNS.c1))
        #FRONT_NECK_ANGLE = angleOfVector(FSP, FNS, FNS.c2)
        FNC.addOutpoint(right(FNC, 0.75 * abs(FNC.x - FNS.x)))
        FNS.addInpoint(polar(FNS, distance(FNS, FNC.outpoint) / 2.0, angleOfLine(FNS, FNC.outpoint)))

        #back
        BNC = B.addPoint('BNC', (0.0, 0.0)) #back neck center
        BWC = B.addPoint('BWC', down(BNC, CD.back_waist_length)) #back waist center
        BSH = B.addPoint('BSH', up(BWC, CD.back_shoulder_height)) #back shoulder height
        BSW = B.addPoint('BSW', left(BSH, CD.back_shoulder_width / 2.0)) #back shoulder width

        BUC = B.addPoint('BUC', down(BNC, back_underarm_height)) #back underarm center
        BUS = B.addPoint('BUS', left(BUC, CD.back_underarm / 2.0)) #back underarm side
        #BAC = down(BNC, distance(BNC, BUC)*2 / 3.0) #back across chest center
        BAC = B.addPoint('BAC', down(BNC, 0.75 * distance(BNC, BUC))) #back across chest center - 3 / 4ths distance BNC to BUC
        BAS = B.addPoint('BAS', left(BAC, CD.across_chest / 2.0)) #back across chest side
        BSP = B.addPoint('BSP', highestP(onCircleAtX(BWC, CD.back_shoulder_balance, BSW.x))) #back shoulder point
        BNS = B.addPoint('BNS', rightmostP(onCircleAtY(BSP, CD.shoulder, BSH.y))) #back neck side
        BAP = B.addPoint('BAP', (BAS.x, BUC.y)) #back armscye point
        BBC = B.addPoint('BBC', down(BUC, distance(FUS, FBS))) #back bust center
        BBS = B.addPoint('BBS', left(BBC, CD.back_bust / 2.0)) #back bust side

        #back waist dart
        dart_width = CD.back_waist / 12.0 #based on 24" waist with 1" back waist darts
        BWS1 = B.addPoint('BWS1', leftmostP(intersectCircles(BNC, back_waist_balance, BWC, CD.back_waist / 2.0))) #back waist side 1
        BD1 = B.addPoint('BD1', intersectLines(BNC, BWS1, BWC, BSP)) #back dart
        B_APEX = B.addPoint('B_APEX', (BD1.x, BUC.y)) #bodice back apex is below dart point on bust line
        BWM = B.addPoint('BWM', intersectLines(BD1, B_APEX, BWC, BWS1)) #back dart midline intersected with line BWC-BWS1
        mid_pnt = dPnt((BD1.x, (BWC.y + BWM.y)/2.0)) #halfway b/w pnt1.y & BWC.y
        #mid_pnt = intersectLines(BD1, B_APEX, BWC, BWS1) #back dart midline intersected with line BWC-BWS1
        BD1.i = B.addPoint('BD1.i', right(mid_pnt, dart_width / 2.0))
        BD1.o = B.addPoint('BD1.o', left(mid_pnt, dart_width / 2.0))
        #update BUS if needed
        if isAbove(BUC, BD1): #if BD1 is above BUC
            b13 = intersectLines(BD1, BD1.i, BUC, BUS)
            b14 = intersectLines(BD1, BD1.o, BUC, BUS)
            pnt1 = intersectLineAtLength(BUC, BUS, distance(BUC, BUS) + distance(b13, b14))
            updatePoint(BUS, pnt1)
        #update BBS if needed
        if isAbove(BBC, BD1): #if BD1 is above BBC
            b15 = intersectLines(BD1, BD1.i, BBC, BBS)
            b16 = intersectLines(BD1, BD1.o, BBC, BBS)
            pnt1 = dPnt(onLineAtLength(BBC, BBS, distance(BBC, BBS) + distance(b15, b16)))
            updatePoint(BBS, pnt1)
        #BWS - back waist side
        BWS = B.addPoint('BWS', lowestP(intersectCircles(BUS, distance(FUS, FWS1), BD1.o, CD.back_waist / 2.0 - distance(BWC, BD1.i)))) #bak waist side
        #adjust dart for waist curve
        extendDart(BWS, BD1, BWC, extension = 0.3)
        #create dart fold to match waist curve
        foldDart(BD1, BWC) #creates BD1.m, BD1.oc, BD1.ic; dart folds toward pattern center

        #back control points
        #b/w BD1.i & BWC
        BD1.i.addOutpoint(polar(BD1.i, distance(BD1.i, BWC) / 6.0, angleOfLine(BD1, BD1.i) - ANGLE90))
        BWC.addInpoint(left(BWC, distance(BD1.i, BWC) / 6.0))
        #b/w BWS & BD1.o
        BWS.addOutpoint(polar(BWS, distance(BWS, BD1.o) / 6.0, angleOfLine(BWS, BD1.o)))
        BD1.o.addInpoint(polar(BD1.o, distance(BWS, BD1.o) / 6.0, angleOfLine(BD1, BD1.o) + ANGLE90))
        #b/w BSP & BAS
        BSP.addOutpoint(polar(BSP, distance(BSP, BAS) / 3.0, angleOfLine(BNS, BSP) - ANGLE90))
        BAS.addInpoint(polar(BAS, distance(BSP, BAS) / 3.0, angleOfLine(BUS, BSP)))
        #b/w BAS & BUS
        BAS.addOutpoint(polar(BAS, distance(BAS, BUS) / 3.0, angleOfLine(BSP, BUS)))
        BUS.addInpoint(polar(BUS, distance(BAS, BUS) / 3.0, angleOfLine(BUS, BWS) - ANGLE90))
        #b/w BNC & BNS
        length1 = abs(BNS.x-FNC.x) * 2 / 3.0
        BNC.addOutpoint(left(BNC, length1))
        BNS.addInpoint(polar(BNS, distance(BNS, BNC.outpoint) / 2.0, (angleOfLine(BNS, BNC.outpoint) + ANGLE90) / 2.0)) #angle1 is halfway b / w vertical line & angle to 1st control point

        #draw Bodice Front A
        pnt1 = dPnt(midPoint(FAP, FUC))
        A.setLabelPosition((pnt1))
        A.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        AG1 = dPnt((FNC.x + distance(FNC, FNS) / 2.0,  FNC.y + distance(FNC, FUC) / 4.0))
        AG2  = dPnt(down(AG1, 0.8 * distance(FNC, FWC)))
        A.addGrainLine(AG1, AG2)
        A.addGridLine(['M', FSP, 'L', FSW, 'L', FSH, 'L', FWC, 'M', FWC, 'L', FSP, 'M', FUC, 'L', FUS, 'M', FBC, 'L', FBP, 'L', FBS1, 'M', FBP, 'L', FBS, 'M', FWC, 'M', FAC, 'L', FAS, 'M', FNC, 'L', FWS1, 'L', FUS, 'M', FD2.b2, 'L', FWS])
        A.addDartLine(['M', FD1.ic, 'L', FD1, 'L', FD1.oc, 'M', FD2.ic, 'L', FD2, 'L', FD2.oc])
        pth = (['M', FNC, 'C', FNS, 'L', FSP, 'C', FAS, 'C', FUS, 'L', FD2.i, 'L', FD2.m, 'L', FD2.o, 'L', FWS, 'C', FD1.o, 'L', FD1.m, 'L', FD1.i, 'C', FWC, 'L', FNC])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        #draw Bodice Back B
        pnt1 = dPnt((BNS.x - distance(BNS, BSP)/2.0, BNC.y + distance(BNC, BUC)/2.0))
        B.setLabelPosition((pnt1))
        B.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        BG1 = dPnt((BNC.x - distance(BUC, BNC)/4.0, BNC.y + distance(BNC, BUC)/4.0))
        BG2 = dPnt(down(BG1, 0.8 * distance(BNC, BWC)))
        B.addGrainLine(BG1, BG2)
        B.addGridLine(['M', BSP, 'L', BSW, 'L', BSH, 'L', BWC, 'L', BWS1, 'M', BWC, 'L', BSP, 'M', BUC, 'L', BUS, 'M', BAC, 'L', BAS])
        B.addDartLine(['M', BD1.ic, 'L', BD1, 'L', BD1.oc])
        pth = (['M', BNC, 'C', BNS, 'L', BSP, 'C', BAS, 'C', BUS, 'L', BWS, 'C', BD1.o, 'L', BD1.m, 'L', BD1.i, 'C', BWC, 'L', BNC])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        # call draw once for the entire pattern
        self.draw()
        return


#vi:set ts = 4 sw = 4 expandta2:

