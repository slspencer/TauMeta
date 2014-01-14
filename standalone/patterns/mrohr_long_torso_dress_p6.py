#!/usr/bin/env python
# patternName: Dress_Long_Torso_MRohr
# patternNumber: D_Long_Torso_MRohr

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
        self.setInfo('patternNumber', 'D_Long_Torso_MRohr')
        self.setInfo('patternTitle', 'Long Torso Dress - MRohr')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'M. Rohr')
        self.setInfo('patternmakerName', 'S.L.Spencer')
        self.setInfo('description', """Sleeveless fitted dress with square neckline, dropped waist and gathered skirt""")
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
        self.setInfo('yearstart', '1950' )
        self.setInfo('yearend', '1959')
        self.setInfo('culture', 'European')
        #self.setInfo('wearer', '')
        #self.setInfo('source', '')
        #self.setInfo('characterName', '')
        #
        #get client data
        CD = self.CD #client data is prefaced with CD
        #
        #create pattern called 'dress'
        dress = self.addPattern('dress')
        #
        #create pattern pieces
        A = dress.addPiece('Bodice Front', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = dress.addPiece('Bodice Back', 'B', fabric = 2, interfacing = 0, lining = 0)
        C = dress.addPiece('Skirt Front', 'C', fabric = 2, interfacing = 0, lining = 0)
        D = dress.addPiece('Skirt Back', 'D', fabric = 2, interfacing = 0, lining = 0)

        #---Bodice Front A---#
        FNC = A.addPoint('FNC', (0.0, 0.0)) #front neck center
        FWC = A.addPoint('FWC', down(FNC, CD.front_waist_length)) #front waist center
        FSH = A.addPoint('FSH', up(FWC, CD.front_shoulder_height)) #front shoulder height
        FBC = A.addPoint('FBC', up(FWC, CD.bust_length)) #bust center
        FBP = A.addPoint('FBP', left(FBC, CD.bust_distance/2.0)) #bust point
        FST = A.addPoint('FST', leftmostP(intersectCircles(FWC, CD.front_shoulder_balance, FNC, CD.front_shoulder_width))) #front shoulder point
        FNS = A.addPoint('FNS', highestP(intersectCircles(FST, CD.shoulder, FBP, CD.bust_balance))) #front neck point
        FAS = A.addPoint('FAS', lowestP(onCircleAtX(FNS, CD.front_underarm_balance, FNC.x - CD.across_chest/2.0))) #front underarm point
        FUC = A.addPoint('FUC', (FNC.x, FAS.y)) #front undearm center
        t_FUS = A.addPoint('t_FUS', left(FUC, CD.front_underarm/2.0)) #temp front underarm side
        FBS = A.addPoint('FBS', leftmostP(onCircleTangentFromOutsidePoint(FBP, CD.front_bust/2.0 - distance(FBC, FBP), t_FUS))) #bust side is where line from bust point is perpendicular to line through t_FUS
        FUS = A.addPoint('FUS', onLineAtLength(t_FUS, FBS, 0.13 * CD.side)) #adjusted front underarm side on line t_FUS-10
        t1_FWS = A.addPoint('t1_FWS', left(FWC, 0.53 * CD.front_waist)) #temporary front waist side 1 - on waist line - 3% ease
        t2_FWS = A.addPoint('t2_FWS', onLineAtLength(t_FUS, FBS, CD.side)) #temporary front waist side 2 - on side seam
        #front waist dart
        totalDartAngle = abs(angleOfVector(t1_FWS, FBP, t2_FWS))
        frontWaistDartAngle = totalDartAngle/2.0
        bustDartAngle = totalDartAngle/2.0
        FD1 = A.addPoint('FD1', (FBP)) #front waist dart point
        FD1.i = A.addPoint('FD1.i', onRayAtY(FBP, ANGLE90 - frontWaistDartAngle/2.0, FWC.y)) #front waist dart inside leg
        FD1.o = A.addPoint('FD1.o', onRayAtY(FBP, ANGLE90 + frontWaistDartAngle/2.0, FWC.y)) #front waist dart outside leg
        updatePoint(FD1, down(FD1, distance(FD1, FD1.i)/7.0)) #adjust FD1 away from FBP bust point
        #finalize front waist side
        remainingWaistSegment = distance(FWC, t1_FWS) - distance(FWC, FD1.i)
        FWS = A.addPoint('FWS', left(FD1.o, remainingWaistSegment)) #front waist side
        #bust dart
        FD2 = A.addPoint('FD2', (FBP)) #bust dart point
        FD2.i = A.addPoint('FD2.i', intersectLineRay(t_FUS, FBS, FBP, ANGLE180 + bustDartAngle/2.0)) #bust dart inside leg
        remainingSideSegment = distance(FUS, t2_FWS) - distance(FUS, FD2.i)
        FD2.o = A.addPoint('FD2.o', leftmostP(intersectCircles(FWS, remainingSideSegment, FBP, distance(FBP, FD2.i))))
        updatePoint(FD2, left(FD2, distance(FD2, FD2.i)/7.0))
        foldDart2(FD2, FUS) #creates FD2.m,FD2.oc,FD2.ic; dart folds up toward underarm side FUS
        #hip extension
        FHC = A.addPoint('FHC', down(FWC, CD.front_hip_height)) #front hip center
        FHM = A.addPoint('FHM', (FD1.x, FHC.y)) #lower waist dart point on hip line
        t_FHS = A.addPoint('t_FHS', left(FHC, CD.front_hip/2.0)) #temporary front hip side
        FHS = A.addPoint('FHS', leftmostP(intersectCircles(FHM, CD.front_hip/2.0 - distance(FHC, FHM), FWS, CD.side_hip_height)))
        #redesign neck, armscye & hip
        a1 = A.addPoint('a1', midPoint(FNC, FUC)) #new front neck center
        a2 = A.addPoint('a2', midPoint(FWC, FHC)) #new front hip center
        a3 = A.addPoint('a3', midPoint(FWS, FHS)) #new front hip side
        a4 = A.addPoint('a4', midPoint(FD2.i, FUS)) #new front underarm
        a5 = A.addPoint('a5', onLineAtLength(FNS, FST, distance(FNS, FST)/3.0)) #new front neck side
        a6 = A.addPoint('a6', polar(a5, 2 * distance(a5, FST), angleOfLine(FNS, FST) + angleOfDegree(6))) #new shoulder tip
        a7 = A.addPoint('a7', onRayAtY(a5, angleOfLine(FST, FNS) + ANGLE90, a1.y)) #neck corner
        #front lower waist dart FD3
        FD3 = A.addPoint('FD3', up(FHM, distance(FWC, FHC)/7.0)) #lower waist dart point
        FD3.i = A.addPoint('FD3.i', onLineAtY(FD1.i, FD3, a2.y)) #lower waist dart inside
        FD3.o = A.addPoint('FD3.o', onLineAtY(FD1.o, FD3, a2.y)) #lower waist dart outside
        foldDart2(FD3, FWC) #creates FD3.m, FD3.oc, FD3.ic; dart folds towards FWC front waist center
        #create seam allowance for lower darts
        FD3.ic = A.addPoint('FD3.ic', onLineAtLength(FD3.i, FD3, SEAM_ALLOWANCE))
        FD3.oc = A.addPoint('FD3.oc', onLineAtLength(FD3.o, FD3, SEAM_ALLOWANCE))

        #Bodice Front A control points
        #b/w FNS front neck point & FNC front neck center
        FNS.addOutpoint(polar(FNS, abs(FNC.y - FNS.y)/4.0, angleOfLine(FST, FNS) + ANGLE90))
        FNC.addInpoint(left(FNC, 0.75 * abs(FNC.x - FNS.x)))
        #b/w FAS front underarm point & FST front shoulder point
        FST.addInpoint(polar(FST, distance(FAS, FST)/6.0, angleOfLine(FST, FNS) + ANGLE90)) #short control handle perpendicular to shoulder seam
        FAS.addOutpoint(polar(FAS, distance(FAS, FST)/3.0, angleOfLine(FAS, FNS))) #control handle points to front neck point
        #b/w FUS front underarm side & FAS front underarm point
        FAS.addInpoint(polar(FAS, distance(FUS, FAS)/3.0, angleOfLine(FNS, FAS)))
        FUS.addOutpoint(polar(FUS, distance(FUS, FAS)/3.0, angleOfLine(FD2.i, FUS) + ANGLE90)) #control handle is perpendicular to side seam at underarm

        #---Bodice Back B---#
        BNC = B.addPoint('BNC', (0.0, 0.0)) #back neck center
        BWC = B.addPoint('BWC', down(BNC, CD.back_waist_length)) #back waist center
        BSH = B.addPoint('BSH', up(BWC, CD.back_shoulder_height)) #back shoulder height reference point
        t_BWS = B.addPoint('t_BWS', right(BWC, 0.53 * CD.back_waist)) #back waist side reference point - 3% ease
        BST = B.addPoint('BST', rightmostP(intersectCircles(BWC, CD.back_shoulder_balance, BNC, CD.back_shoulder_width))) #back shoulder point
        BNS = B.addPoint('BNS', leftmostP(onCircleAtY(BST, 1.04 * CD.shoulder, BSH.y))) #back neck point - 4% ease in back shoulder seam
        BAS = B.addPoint('BAS', lowestP(onCircleAtX(BNS, CD.back_underarm_balance, BNC.x + CD.across_back/2.0))) #back underarm point
        BUC = B.addPoint('BUC', (BNC.x, BAS.y)) #back undearm center
        t_BUS = B.addPoint('t_BUS', right(BUC, CD.back_underarm/2.0)) #back underarm side reference point
        BUS = B.addPoint('BUS', down(t_BUS, distance(t_FUS, FUS))) #adjusted back underarm side
        B_APEX = B.addPoint('B_APEX', intersectLines(BWC, BST, BUC, t_BUS)) #back apex - dart reference point
        BD1 = B.addPoint('BD1', (B_APEX.x, BUS.y)) #back waist dart point is at underarm height
        BD1.i = B.addPoint('BD1.i', right(BWC, 0.8 * distance(BUC, B_APEX))) #dart inside leg
        BD1.o = B.addPoint('BD1.o', right(BD1.i, 0.4 * distance(BUC, B_APEX))) #dart outside leg
        BWS = B.addPoint('BWS', right(BD1.o, distance(BWC, t_BWS) - distance(BWC, BD1.i))) #back waist side
        updatePoint(BUS, onLineAtLength(BWS, t_BUS, distance(FUS, t2_FWS)))
        # back shoulder dart BD2
        t_BD2 = B.addPoint('t_BD2', onLineAtLength(BNS, BST, distance(BNS, BST)/3.0)) # dart is 1/3 from BNS to BST
        BD2 = B.addPoint('BD2', onRayAtX(t_BD2, angleOfLine(BST, BNS) - ANGLE90, B_APEX.x)) # shoulder dart point
        BD2.i = B.addPoint('BD2.i', (t_BD2))
        BD2.o = B.addPoint('BD2.o', (t_BD2))
        slashAndSpread(BD2, angleOfDegree(-8), BD2.i, BNS)
        foldDart2(BD2, BNS) #creates BD2.m, BD2.oc, BD2.ic; dart folds toward BNS back neck side
        #back hip extension
        BHC = B.addPoint('BHC', down(BWC, CD.back_hip_height)) #back hip center
        BHM = B.addPoint('BHM', (BD1.x, BWC.y + CD.back_hip_height)) # back waist dart at hip line
        t_BHS = B.addPoint('t_BHS', right(BHC, CD.back_hip/2.0)) #temporary back hip side
        BHS = B.addPoint('BHS', rightmostP(intersectCircles(BHM, CD.back_hip/2.0 - distance(BHC, BHM), BWS, CD.side_hip_height)))
        #back shoulder extension
        b18 = B.addPoint('b18', onLineAtLength(BNS, BST, distance(BNS, BST)/3.0)) #move neck point 1/3 down shoulder seam
        b19 = B.addPoint('b19', down(BWC, 0.66 * distance(BNS, b18))) #new back neck center
        b20 = B.addPoint('b20', onLineAtLength(t_BUS, BUS, distance(FUS, a4))) #new back underarm
        b21 = B.addPoint('b21', polar(b18, distance(a5, a6), angleOfLine(BNS, BST) - angleOfDegree(6))) #new shoulder tip
        #shorten hip extension
        b22 = B.addPoint('b22', midPoint(BWC, BHC)) #new back hip center
        b23 = B.addPoint('b23', midPoint(BWS, BHS)) #new back hip side
        #Back lower waist dart BD3
        BD3 = B.addPoint('BD3', up(BHM, distance(BWC, BHC)/7.0)) # back waist dart point at hip
        BD3.i = B.addPoint('BD3.i', onLineAtY(BD1.i, BD2, b22.y)) #new lower waist dart inside
        BD3.o = B.addPoint('BD3.o', onLineAtY(BD1.o, BD2, b22.y)) #new lower waist dart outside
        foldDart2(BD3, b22) #creates BD3.m, BD3.oc, BD3.ic; dart folds b22 new back hip center
        #create seam allowance for lower dart
        BD3.ic = B.addPoint('BD3.ic', onLineAtLength(BD3.i, BD3, SEAM_ALLOWANCE))
        BD3.oc = B.addPoint('BD3.oc', onLineAtLength(BD3.o, BD3, SEAM_ALLOWANCE))

        #Bodice Back B control points
        #b/w BNS back neck point & BNC back neck center
        BNC.addInpoint(right(BNC, 0.65 * abs(BNC.x - BNS.x)))
        BNS.addOutpoint(polar(BNS, abs(BNS.y - BNC.y)/4.0, angleOfLine(BNS, BNC.inpoint)))
        #b/w BUS underarm point & BAS underarm curve
        BUS.addOutpoint(polar(BUS, distance(BUS, BAS)/3.0, angleOfLine(BUS, BWS) + ANGLE90)) #perpendicular to side seam
        BAS.addInpoint(polar(BAS, distance(BUS, BAS)/3.0, angleOfLine(BNS, BAS)))
        #b/w BAS underarm curve & BST shoulder point
        BAS.addOutpoint(polar(BAS, distance(BAS, BST)/3.0, angleOfLine(BAS, BNS)))
        BST.addInpoint(polar(BST, distance(BAS, BST)/6.0, angleOfLine(BNS, BST) + ANGLE90)) #short control handle, perpendicular to shoulder seam

        #---Skirt Front C---#
        c1 = C.addPoint('c1', (0, 0)) #front skirt waist center
        c2 = C.addPoint('c2', down(c1, (2 * CD.back_waist_length) - distance(BWC, b22))) #front skirt hem center - length from waistline to hem is 2*back_waist_length
        c3 = C.addPoint('c3', left(c1, 3 * (distance(a2, FD3.i) + distance(FD3.o, a3)))) #front skirt waist side - skirt width is 3 * front hipline width
        c4 = C.addPoint('c4', down(c3, distance(c1, c2))) #front skirt hem side

        #---Skirt Back D---#
        d1 = D.addPoint('d1', (0, 0)) #back skirt waist center
        d2 = D.addPoint('d2', down(d1, distance(c1, c2))) #back skirt hem center
        d3 = D.addPoint('d3', right(d1, 3 * CD.back_hip/2.0)) #back skirt waist side - skirt width is 3 * back hipline width
        d4 = D.addPoint('d4', down(d3, distance(c1, c2))) #back skirt hem side

        #---------------------------------------------#
        #---all points defined, draw pattern pieces---#
        #---------------------------------------------#

        #draw dress Front A
        pnt1 = midPoint(FAS, FUC)
        A.setLabelPosition((pnt1))
        A.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        aG1 = dPnt(left(FUC, distance(FUC, pnt1)/4.0))
        aG2 = dPnt(down(aG1, distance(FNC, FWC)/2.0))
        A.addGrainLine(aG1, aG2)
        A.addGridLine(['M', FNS, 'L', FSH, 'L', FWC, 'L', FST, 'M', FUC, 'L', t_FUS, 'M', FNC, 'L', FST, 'M', FBC, 'L', FBP, 'M', FWC, 'L', t1_FWS, 'M', FBP, 'L', FNS, 'L', FAS, 'M', FUS, 'L', t2_FWS, 'M', FBP, 'L', FBS, 'M', FBP, 'L', FHM, 'M', FHC, 'L', t_FHS, 'M', FWS, 'L', FD1.o, 'L', FWS, 'M', FHS, 'L', FWS])
        A.addDartLine(['M', FD3.ic, 'L', FD1.i, 'L', FD1, 'L', FD1.o,  'L', FD3.oc, 'M', FD2.ic, 'L', FD2, 'L', FD2.oc])
        pth = (['M', a1, 'L', a2, 'L', FD3.i, 'L', FD3.m, 'L', FD3.o,  'L', a3, 'L', FWS, 'L', FD2.o, 'L', FD2.m, 'L', FD2.i, 'L', a4, 'L', a6, 'L', a5, 'L', a7, 'L', a1])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        #draw Bodice Back B
        pnt1 = dPnt((distance(BSH, BNS)/2.0, distance(BNC, BUC)/2.0))
        B.setLabelPosition((pnt1))
        B.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        bG1 = dPnt((distance(BSH, BNS)/4.0, distance(BNC, BUC)/4.0))
        bG2 = dPnt(down(bG1, distance(BNC, BWC)/2.0))
        B.addGrainLine(bG1, bG2)
        B.addGridLine(['M', BNS, 'L', BSH, 'L', BWC, 'L', BWS, 'M', BD1.o, 'L', BWS, 'M', BNC, 'L', BST, 'M', BWC, 'L', BST, 'M', BNS, 'L', BAS, 'M', BUC, 'L', t_BUS, 'M',  BD1, 'L', BHM, 'L', t_BHS, 'M', BHS, 'L', BWS])
        B.addDartLine(['M', BD3.i, 'L', BD1.i, 'L', BD1, 'L', BD1.o, 'L', BD3.o, 'M', BD2.i, 'L', BD2, 'L', BD2.o])
        pth = (['M', BNC, 'L', BHC, 'L', BHM, 'L', BHS, 'L', BWS, 'L', BUS, 'C', BAS, 'C', BST, 'L', BD2.o, 'L', BD2.m, 'L', BD2.i, 'L', BNS, 'C', BNC])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        #draw Skirt Front C
        C.setLetter(((c3.x - c1.x)/3.0, (c2.y - c1.y)/3.0), scaleby=10.0)
        C.setLabelPosition(((c3.x - c1.x)/3.0, (c2.y - c1.y)/2.0))
        cG1 = dPnt(( (c3.x - c1.x)/4.0, (c2.y - c1.y)/4.0 ))
        cG2 = dPnt(down(cG1, 0.75 * distance(c1, c2)))
        C.addGrainLine(cG1, cG2)
        pth = (['M', c1, 'L', c2, 'L', c4, 'L', c3, 'L', c1])
        C.addSeamLine(pth)
        C.addCuttingLine(pth)

        #draw Skirt Back D
        D.setLetter(((d3.x - d1.x)/3.0, (d2.y - d1.y)/3.0), scaleby=10.0)
        D.setLabelPosition(((d3.x - d1.x)/3.0, (d2.y - d1.y)/2.0))
        dG1 = dPnt(((d3.x - d1.x)/4.0, (d2.y - d1.y)/4.0))
        dG2 = dPnt(down(dG1, 0.75 * distance(d1, d2)))
        D.addGrainLine(dG1, dG2)
        pth = (['M', d1, 'L', d2, 'L', d4, 'L', d3, 'L', d1])
        D.addSeamLine(pth)
        D.addCuttingLine(pth)



        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

