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
        self.setInfo('description', 'Long-sleeved robe with front zipper closing, inset hip-level pockets, oversized hood, and sleeves widened towards wrists. BAPed on Xaldin character from Kingdom Hearts.')
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
        BUS = B.addPoint('BUS', down(t1_BUS, 0.13 * CD.side)) #final back underarm side
        BD1 = B.addPoint('BD1', intersectLines(BWC, BSP, BUC, t1_BUS)) #back waist dart point
        BD1.m = B.addPoint('BD1.m', dPnt((BD1.x, BWC.y))) # below dart point at waist
        BD1.i = B.addPoint('BD1.i', left(BD1.m, distance(BWC, BD1.m)/5.0)) #dart inside leg
        BD1.o = B.addPoint('BD1.o', right(BD1.m, distance(BD1.m, BD1.i))) #dart outside leg
        BWS = B.addPoint('BWS',  rightmostP(intersectCircles(BUS, CD.side - distance(t1_BUS, BUS), BD1.o, CD.back_waist/2.0 - distance(BWC, BD1.i)))) #back waist side
        #Bodice Back hip extension
        BHC = B.addPoint('BHC', down(BWC, CD.back_hip_height)) #back hip center
        t2_BWS = B.addPoint('t2_BWS', right(BD1.o, distance(BD1.o, BWS))) #temp back waist side 2
        BHM = B.addPoint('BHM', (BD1.x, BHC.y)) # back waist dart at hip line - back hip mid-point
        t1_BHS = B.addPoint('t1_BHS', right(BHC, CD.back_hip/2.0)) #temporary back hip side
        BHS = B.addPoint('BHS', rightmostP(intersectCircles(BHM, distance(BHM, t1_BHS), BWS, CD.side_hip_height))) #back hip side
        #complete Back waist dart
        BD1.d = B.addPoint('BD1.d', up(BHM, distance(BHM, BD1.m)/7.0)) # back waist dart point at hip
        #create curve at dart BAPe
        foldDart(BD1, BWC) #creates BD1.m, BD1.oc, BD1.ic; dart folds toward waist center BWC

        #back design points
        b1 = B.addPoint('b1', right(BSP, 0.1 * CD.shoulder))
        b2 = B.addPoint('b2', polar(b1, 0.2 * CD.shoulder, angleOfDegree(315))) #back shoulder point
        BHemC = B.addPoint('BHemC', polar(BWC, CD.back_hip_height + CD.hip_to_floor, angleOfDegree(105))) #back hem center
        BHemS = B.addPoint('BHemS', polar(BWS, distance(BWC, BHemC), angleOfDegree(70))) #back hem side
        b3 = B.addPoint('b3', right(BUS, 0.05 * CD.back_underarm / 2.0)) #design back underarm side
        b4 = B.addPoint('b4', extendLine(BHM, BHS, 0.05 * CD.back_hip / 2.0)) #design back hip side
        b5 = B.addPoint('b5', onLineAtLength(BWC, BHemC, CD.back_hip_height)) #design back hip center
        b6 = B.addPoint('b6', right(BAP, 0.05 * CD.across_back / 2.0)) #design across back point)

        #Bodice Back B control points
        #b/w BNS back neck point & BNC back neck center
        BNC.addInpoint(right(BNC, 0.5 * abs(BNC.x - BNS.x)))
        BNS.addOutpoint(polar(BNS, abs(BNS.y - BNC.y) / 6.0, angleOfLine(BNS, BSP) + ANGLE90)) #perpendicular to orig. shoulder seam
        #b/w back waist center & b5
        BWC.addOutpoint(down(BWC, distance(BWC, b5)/6.66)) #short control handle
        b5.addInpoint(polar(b5, distance(BWC, b5)/6.66, angleOfLine(BHemC, b5))) #short control handle
        #b/w back hem center & back hem side
        BHemC.addOutpoint(polar(BHemC, distance(BHemC, BHemS)/3.33, angleOfLine(BHC, BHemC) - ANGLE90))
        BHemS.addInpoint(polar(BHemS, distance(BHemS, BHemC)/3.33, angleOfLine(BHS, BHemS) + ANGLE90))
        #b/w b4 & back waist side
        b4.addOutpoint(polar(b4, distance(b4, BWS)/3.33, angleOfLine(BHemS, b4)))
        BWS.addInpoint(down(BWS, distance(b4, BWS)/6.66)) #short control handle at waist
        #b/w back waist side & b3
        BWS.addOutpoint(up(BWS, distance(BWS, b3)/6.66)) #short control handle at waist
        b3.addInpoint(polar(b3, distance(BWS, b3)/3.33, (ANGLE90 + angleOfLine(b3, BWS)) / 2.0))
        #b/w b3, b6
        b3.addOutpoint(polar(b3, distance(b3, b6)/3.33, angleOfLine(b3.inpoint, b3) - ANGLE90))
        b6.addInpoint(polar(b6, distance(b3, b6)/3.33, angleOfLine(BNS, b6)))
        #b/w across back point & b2
        b6.addOutpoint(polar(b6, distance(b6, b2)/3.33, angleOfLine(b6, BNS)))
        b2.addInpoint(polar(b2, distance(b6, b2)/3.33, angleOfLine(BNS, b2) + ANGLE90))

        #draw Back B
        pnt1 = dPnt(midPoint(BUC, BAP))
        B.setLetter(up(pnt1, 0.3 * IN), scaleby=10.0)
        B.setLabelPosition((pnt1.x, BUS.y))
        bG1 = dPnt(((BNC.x + BNS.x)/2.0, BUC.y))
        bG2 = dPnt(down(bG1, 0.5 * distance(BNC, BHemC)))
        B.addGrainLine(bG1, bG2)
        pth = (['M', BNC, 'L', BWC, 'C', b5, 'L', BHemC, 'C', BHemS, 'L', b4, 'C', BWS, 'C', b3, 'C', b6, 'C', b2, 'L', BNS, 'C', BNC])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)



        # call draw once for the entire pattern
        self.draw()
        return
#vi=set ts=4 sw=4 expandta2:

