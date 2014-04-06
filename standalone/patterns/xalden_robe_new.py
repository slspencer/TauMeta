#!/usr/bin/env python
# patternName: Xaldin_Robe
# patternNumber: C_KH_Xaldin

from tmtpl.designbase import *
from tmtpl.document import *
from tmtpl.pattern import *
from tmtpl.patternmath import *
from tmtpl.constants import *
from tmtpl.utils import *

class Design(designBase):

    def pattern(self):

        # The designer must supply certain information to allow
        #   tracking and searching of patterns
        #
        # This group is all mandatory
        #
        self.setInfo('patternNumber', 'C_KH_Xaldin')
        self.setInfo('patternTitle', 'Xaldin Robe')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'S.L.Spencer')
        self.setInfo('patternmakerName', 'S.L.Spencer')
        self.setInfo('description', 'Long-sleeved robe with front zipper closing, inset hip-level pockets, oversized hood, and sleeves widened towards wrists. Based on Xaldin character from Kingdom Hearts.')
        self.setInfo('category', 'Coat')
        self.setInfo('type', 'pattern')
        self.setInfo('gender', 'U') # 'M',  'F', 'U', or 'N'
        #
        # The next group are all optional
        #
        self.setInfo('recommendedFabric', 'Leather, pleather, sweatshirt fabric, or any medium- to heavy-weight fabric with good drape characteristics.')
        self.setInfo('recommendedNotions', 'Oversized #30 molded plastic zipper specially made by YKK for Nobody characters in Kingdom Hearts.')
        #
        #Historical/Vintage
        #self.setInfo('yearstart',1940 )
        #self.setInfo('yearend', 1949)
        #
        #Re-enactment
        #self.setInfo('culture', 'European')
        #self.setInfo('wearer', 'serf')
        #
        #Cosplay
        self.setInfo('source', 'Kingdom Hearts')
        self.setInfo('characterName', 'Xaldin')
        #
        #get client data
        CD = self.CD #client data is prefaced with CD
        #
        #create pattern called 'coat'
        coat = self.addPattern('coat')
        #
        #create pattern pieces
        A = coat.addPiece('Back', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = coat.addPiece('Lower Front', 'B', fabric = 2, interfacing = 0, lining = 0)
        C = coat.addPiece('Upper Front', 'C', fabric = 2, interfacing = 0, lining = 0)
        D = coat.addPiece('Sleeve', 'D', fabric = 2, interfacing = 0, lining = 0)
        E = coat.addPiece('Pocket Welt', 'E', fabric = 2, interfacing = 0, lining = 0)
        F = coat.addPiece('Pocket', 'F', fabric = 2, interfacing = 0, lining = 0)
        G = coat.addPiece('Hood', 'G', fabric = 2, interfacing = 0, lining = 0)

        #---Coat Back B---#
        BNC = B.addPoint('BNC', (0, 0)) # back neck center
        BWC = B.addPoint('BWC', down(BNC, CD.back_waist_length)) #back waist center
        BSH = B.addPoint('BSH', up(BWC, CD.back_shoulder_height)) #back shoulder height
        t1_BST = dPnt(highestP(onCircleAtX(BWC, CD.back_shoulder_balance, BNC.x + CD.back_shoulder_width/2.0 )))
        t2_BST = dPnt(right(t1_BST, 0.1*CD.shoulder))
        BST = B.addPoint('BST', polar(t2_BST, 0.2*CD.shoulder, angleOfDegree(315))) #back Shoulder Tip
        BNS = B.addPoint('BNS', leftmostP(onCircleAtY(BST, CD.shoulder, BSH.y))) #back neck side
        BAS = B.addPoint('BAS', lowestP(onCircleAtX(BNS, CD.back_underarm_balance, BNC.x + CD.across_back/2.0))) #back armscye
        BUC = B.addPoint('BUC', (BNC.x, BAS.y)) #back undearm center
        BUS = B.addPoint('BUS', right(BUC, 0.55*CD.back_underarm)) #back undearm side
        t1_BWS = dPnt(lowestP(intersectCircles(BUS, CD.side, BWC, CD.back_waist/2.0))) #temp back waist side
        BWS = B.addPoint('BWS', right(t1_BWS, 0.07*CD.back_waist/2.0)) #back waist side
        BHemC = B.addPoint('BHemC', polar(BWC, CD.back_hip_height + CD.hip_to_floor, angleOfDegree(105))) #back hem center
        BHemS = B.addPoint('BHemS', polar(BWS, distance(BWC, BHemC), angleOfDegree(70))) #back hem side
        t1_BHC = B.addPoint('t1_BHC', down(BWC, CD.back_hip_height)) #temp back hip center
        BHC = B.addPoint('BHC', onLineAtLength(BWC, BHemC, CD.back_hip_height)) #back hip center

        t1_BHS = B.addPoint('t1_BHS', lowestP(onCircleAtX(t1_BWS, CD.side_hip_height, BNC.x + CD.back_hip/2.0))) #temp back hip side
        BHS = B.addPoint('BHS', onLineAtLength(BWS, BHemS, CD.side_hip_height)) #back hip side

        #control points
        #b/w back neck side & back neck center
        BNS.addOutpoint(polar(BNS, abs(BNS.y - BNC.y)/6.0, angleOfLine(BST, BNS) - ANGLE90)) #short control handle
        BNC.addInpoint(right(BNC, abs(BNC.x - BNS.x)/2.0)) #long control handle
        #b/w back waist center & back hip center
        BWC.addOutpoint(down(BWC, distance(BWC, BHC)/6.66)) #short control handle
        BHC.addInpoint(polar(BHC, distance(BWC, BHC)/6.66, angleOfLine(BHemC, BHC))) #short control handle
        #b/w back hem center & back hem side
        BHemC.addOutpoint(polar(BHemC, distance(BHemC, BHemS)/3.33, angleOfLine(BHC, BHemC) - ANGLE90))
        BHemS.addInpoint(polar(BHemS, distance(BHemS, BHemC)/3.33, angleOfLine(BHS, BHemS) + ANGLE90))
        #b/w back hip side & back waist side
        BHS.addOutpoint(polar(BHS, distance(BHS, BWS)/3.33, angleOfLine(BHemS, BHS)))
        BWS.addInpoint(down(BWS, distance(BHS, BWS)/6.66)) #short control handle at waist
        #b/w back waist side & back bust side
        BWS.addOutpoint(up(BWS, distance(BWS, BUS)/6.66)) #short control handle at waist
        BUS.addInpoint(polar(BUS, distance(BWS, BUS)/3.33, angleOfLine(BUS, BWS)))
        #b/w back bust side, back across side, & back shoulder tip
        BUS.addOutpoint(polar(BUS, distance(BUS, BAS)/3.33, angleOfLine(BUS.inpoint, BUS) - ANGLE90))
        BAS.addInpoint(polar(BAS, distance(BUS, BAS)/3.33, angleOfLine(BNS, BAS)))
        BAS.addOutpoint(polar(BAS, distance(BAS, BST)/3.33, angleOfLine(BAS, BNS)))
        BST.addInpoint(polar(BST, distance(BAS, BST)/3.33, angleOfLine(BNS, BST) + ANGLE90))

        #draw Back B
        pnt1 = dPnt(midPoint(BUC, BAS))
        B.setLabelPosition(pnt1)
        B.setLetter(down(pnt1, 0.5*IN), scaleby=10.0)
        bG1 = dPnt(((BNC.x + BNS.x)/2.0, BUC.y))
        bG2 = dPnt(down(bG1, 0.5 * distance(BNC, BHemC)))
        B.addGrainLine(bG1, bG2)
        pth = (['M', BNC, 'L', BWC, 'C', BHC, 'L', BHemC, 'C', BHemS, 'L', BHS, 'C', BWS, 'C', BUS, 'C', BAS, 'C', BST, 'L', BNS, 'C', BNC])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)



        # call draw once for the entire pattern
        self.draw()
        return
#vi=set ts=4 sw=4 expandta2:

