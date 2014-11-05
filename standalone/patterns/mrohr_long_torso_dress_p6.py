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
        A = dress.addPiece('Bodice Front', 'A', fabric = 2, interfacing = 0, lining = 2)
        B = dress.addPiece('Bodice Back', 'B', fabric = 2, interfacing = 0, lining = 2)
        C = dress.addPiece('Skirt Front', 'C', fabric = 2, interfacing = 0, lining = 0)
        D = dress.addPiece('Skirt Back', 'D', fabric = 2, interfacing = 0, lining = 0)

        #---Bodice Front A---#
        FNC = A.addPoint('FNC', (0.0, 0.0)) #front neck center
        FWC = A.addPoint('FWC', down(FNC, CD.front_waist_length)) #front waist center
        FSH = A.addPoint('FSH', up(FWC, CD.front_shoulder_height)) #front shoulder height
        FSW = A.addPoint('FSW', left(FSH, CD.front_shoulder_width/2.0)) #front shoulder width
        FAW = A.addPoint('FAW', left(FSH, CD.across_chest/2.0)) #front across chest width
        FBC = A.addPoint('FBC', up(FWC, CD.bust_length)) #bust center
        FBP = A.addPoint('FBP', left(FBC, CD.bust_distance/2.0)) #bust point
        FSP = A.addPoint('FSP', highestP(onCircleAtX(FWC, CD.front_shoulder_balance, FSW.x))) #front shoulder point
        FNS = A.addPoint('FNS', rightmostP(onCircleAtY(FSP, CD.shoulder, FSH.y))) #front neck side
        FAP = A.addPoint('FAP', lowestP(onCircleAtX(FNS, CD.front_underarm_balance, FAW.x))) #front armscye point
        FUC = A.addPoint('FUC', (FNC.x, FAP.y)) #front undearm center
        FUS1 = A.addPoint('FUS1', left(FUC, CD.front_underarm/2.0)) #front underarm side 1
        FBS = A.addPoint('FBS', leftmostP(onCircleTangentFromOutsidePoint(FBP, CD.front_bust/2.0 - distance(FBC, FBP), FUS1))) #bust side is where line from bust point is perpendicular to line through FUS1
        FUS = A.addPoint('FUS', onLineAtLength(FUS1, FBS, 0.13 * CD.side)) #adjusted front underarm side on line FUS1-10
        FWS1 = A.addPoint('FWS1', left(FWC, 0.55 * CD.front_waist)) #front waist side 1 - on waist line - 5% ease
        FWS2 = A.addPoint('FWS2', onLineAtLength(FUS1, FBS, CD.side)) #front waist side 2 - on side seam
        #front waist dart
        totalDartAngle = abs(angleOfVector(FWS1, FBP, FWS2))
        frontWaistDartAngle = totalDartAngle/2.0
        bustDartAngle = totalDartAngle/2.0
        FD1 = A.addPoint('FD1', (FBP)) #front waist dart point
        FD1.i = A.addPoint('FD1.i', onRayAtY(FBP, ANGLE90 - frontWaistDartAngle/2.0, FWC.y)) #front waist dart inside leg
        FD1.o = A.addPoint('FD1.o', onRayAtY(FBP, ANGLE90 + frontWaistDartAngle/2.0, FWC.y)) #front waist dart outside leg
        updatePoint(FD1, down(FD1, distance(FD1, FD1.i)/7.0)) #adjust FD1 away from FBP bust point
        #finalize front waist side
        remainingWaistSegment = distance(FWC, FWS1) - distance(FWC, FD1.i)
        FWS = A.addPoint('FWS', left(FD1.o, remainingWaistSegment)) #front waist side
        #bust dart
        FD2 = A.addPoint('FD2', (FBP)) #bust dart point
        FD2.i = A.addPoint('FD2.i', intersectLineRay(FUS1, FBS, FBP, ANGLE180 + bustDartAngle/2.0)) #bust dart inside leg
        remainingSideSegment = distance(FUS, FWS2) - distance(FUS, FD2.i)
        FD2.o = A.addPoint('FD2.o', leftmostP(intersectCircles(FWS, remainingSideSegment, FBP, distance(FBP, FD2.i))))
        updatePoint(FD2, left(FD2, distance(FD2, FD2.i)/7.0))
        foldDart(FD2, FUS) #creates FD2.m,FD2.oc,FD2.ic; dart folds up toward underarm side FUS
        #hip extension
        FHC = A.addPoint('FHC', down(FWC, CD.front_hip_height)) #front hip center
        FHM = A.addPoint('FHM', (FD1.x, FHC.y)) #lower waist dart point on hip line
        FHS1 = A.addPoint('FHS1', left(FHC, CD.front_hip/2.0)) #temporary front hip side 1
        FHS = A.addPoint('FHS', leftmostP(intersectCircles(FHM, max(CD.front_hip, CD.front_waist)/2.0 - distance(FHC, FHM), FWS, CD.side_hip_height))) #front hip side
        #redesign neck, armscye & hip
        a1 = A.addPoint('a1', midPoint(FNC, FUC)) #new front neck center
        a2 = A.addPoint('a2', midPoint(FWC, FHC)) #new front hip center
        if (FWS.x < FHS.x):
            a3 = A.addPoint('a3', dPnt(extendLine(FD2.o, FWS, CD.side_hip_height / 2.0)))
        else:
            a3 = A.addPoint('a3', dPnt(midPoint(FWS, FHS)))
        a4 = A.addPoint('a4', midPoint(FD2.i, FUS)) #new front underarm
        a5 = A.addPoint('a5', onLineAtLength(FNS, FSP, distance(FNS, FSP)/4.0)) #new front neck side
        a6 = A.addPoint('a6', polar(a5, 1.25 * distance(a5, FSP), angleOfLine(FNS, FSP) + angleOfDegree(15))) #new shoulder tip
        a7 = A.addPoint('a7', onRayAtY(a5, angleOfLine(FSP, FNS) + ANGLE90, a1.y)) #neck corner

        #front lower waist dart FD3
        FD3 = A.addPoint('FD3', up(FHM, distance(FWC, FHC)/7.0)) #lower waist dart point
        #FD3.i = A.addPoint('FD3.i', onLineAtY(FD1.i, FD3, a2.y)) #lower waist dart inside
        dart_half_width = ((CD.front_hip / 2.0) - abs(FD1.x - a3.x)) / 2.0
        FD3.i = A.addPoint('FD3.i', dPnt((FD1.x + dart_half_width , a2.y))) #lower waist dart inside
        #FD3.o = A.addPoint('FD3.o', onLineAtY(FD1.o, FD3, a2.y)) #lower waist dart outside
        FD3.o = A.addPoint('FD3.o', dPnt((FD1.x - dart_half_width , a2.y))) #lower waist dart outside
        #foldReverseDart(FD3, FWC) #creates FD3.m, FD3.oc, FD3.ic; dart folds towards FWC front waist center
        #extendReverseDart(a2, FD3, a3)        
        FD3.ic = dPnt(extendLine(FD1.i, FD3.i, SEAM_ALLOWANCE))
        FD3.oc = dPnt(extendLine(FD1.o, FD3.o, SEAM_ALLOWANCE))
        angle_fold = ANGLE90 - angleOfLine(FD1.i, FD3.i)
        angle_apex = A.addPoint('angle_apex', dPnt(onLineAtX(FD1.i, FD3.i, FD1.x)))
        intersect_fold = A.addPoint('intersect_fold', dPnt(onRayAtY(angle_apex, ANGLE90 - (2 * angle_fold), a2.y)))
        FD3.m = A.addPoint('FD3.m', dPnt(down(angle_apex, distance(angle_apex, intersect_fold))))


        #Bodice Front A control points
        #b/w FNS front neck point & FNC front neck center
        FNS.addOutpoint(polar(FNS, abs(FNC.y - FNS.y)/4.0, angleOfLine(FSP, FNS) + ANGLE90))
        FNC.addInpoint(left(FNC, 0.75 * abs(FNC.x - FNS.x)))
        #b/w FAP front underarm point & FSP front shoulder point
        FSP.addInpoint(polar(FSP, distance(FAP, FSP)/6.0, angleOfLine(FSP, FNS) + ANGLE90)) #short control handle perpendicular to shoulder seam
        FAP.addOutpoint(polar(FAP, distance(FAP, FSP)/3.0, angleOfLine(FAP, FNS))) #control handle points to front neck point
        #b/w FUS front underarm side & FAP front underarm point
        FAP.addInpoint(polar(FAP, distance(FUS, FAP)/3.0, angleOfLine(FNS, FAP)))
        FUS.addOutpoint(polar(FUS, distance(FUS, FAP)/3.0, angleOfLine(FD2.i, FUS) + ANGLE90)) #control handle is perpendicular to side seam at underarm

        #---Bodice Back B---#
        BNC = B.addPoint('BNC', (0.0, 0.0)) #back neck center
        BWC = B.addPoint('BWC', down(BNC, CD.back_waist_length)) #back waist center
        BSH = B.addPoint('BSH', up(BWC, CD.back_shoulder_height)) #back shoulder height
        BSW = B.addPoint('BSW', right(BSH, CD.back_shoulder_width / 2.0)) #back shoulder width
        BAW = B.addPoint('BAW', right(BSH, CD.across_back / 2.0)) #across back width
        BWS1 = B.addPoint('BWS1', right(BWC, 0.55 * CD.back_waist)) #back waist side 1 - incl. 5% ease
        BSP = B.addPoint('BSP', highestP(onCircleAtX(BWC, CD.back_shoulder_balance, BSW.x))) #back shoulder point
        BNS = B.addPoint('BNS', leftmostP(onCircleAtY(BSP, 1.04 * CD.shoulder, BSH.y))) #back neck point - 4% ease in back shoulder seam
        BAP = B.addPoint('BAP', lowestP(onCircleAtX(BNS, CD.back_underarm_balance, BAW.x))) #back armscye point
        BUC = B.addPoint('BUC', (BNC.x, BAP.y)) #back undearm center
        BUS1 = B.addPoint('BUS1', right(BUC, CD.back_underarm / 2.0)) #back underarm side reference point
        BUS = B.addPoint('BUS', down(BUS1, distance(FUS1, FUS))) #adjusted back underarm side
        B_APEX = B.addPoint('B_APEX', intersectLines(BWC, BSP, BUC, BUS1)) #back apex - dart reference point
        BD1 = B.addPoint('BD1', (B_APEX.x, BUS.y)) #back waist dart point is at underarm height
        BD1.i = B.addPoint('BD1.i', right(BWC, 0.8 * distance(BUC, B_APEX))) #dart inside leg
        BD1.o = B.addPoint('BD1.o', right(BD1.i, 0.4 * distance(BUC, B_APEX))) #dart outside leg
        BWS = B.addPoint('BWS', right(BD1.o, distance(BWC, BWS1) - distance(BWC, BD1.i))) #back waist side
        updatePoint(BUS, onLineAtLength(BWS, BUS1, distance(FUS, FWS2)))
        # back shoulder dart BD2
        pnt1 = dPnt(onLineAtLength(BNS, BSP, distance(BNS, BSP) / 3.0)) # dart is 1/3 from BNS to BSP
        BD2 = B.addPoint('BD2', intersectLineRay(BNS, BAP, pnt1, angleOfLine(BSP, BNS))) # shoulder dart point
        BD2.i = B.addPoint('BD2.i', (pnt1))
        BD2.o = B.addPoint('BD2.o', (pnt1))
        slashAndSpread(BD2, angleOfDegree(-8.0), BD2.i, BNS)
        foldDart(BD2, BNS) #creates BD2.m, BD2.oc, BD2.ic; dart folds toward BNS back neck side
        #back hip extension
        BHC = B.addPoint('BHC', down(BWC, CD.back_hip_height)) #back hip center
        BHM = B.addPoint('BHM', (BD1.x, BWC.y + CD.back_hip_height)) # back waist dart at hip line
        BHS1 = B.addPoint('BHS1', right(BHC, CD.back_hip/2.0)) #temporary back hip side
        BHS = B.addPoint('BHS', rightmostP(intersectCircles(BHM, CD.back_hip/2.0 - distance(BHC, BHM), BWS, CD.side_hip_height)))
        #back shoulder extension
        b1 = B.addPoint('b1', down(BNC, distance(BNC, BUC)/8.0)) #new back neck center
        b2 = B.addPoint('b2', onLineAtLength(BNS, BSP, distance(FNS, a5))) #new back neck side
        b3 = B.addPoint('b3', down(BWC, 0.66 * distance(BNS, b2))) #new back neck center
        b4 = B.addPoint('b4', onLineAtLength(BUS, BUS1, distance(FUS, a4))) #new back underarm
        b5 = B.addPoint('b5', polar(b2, 1.05 * distance(a5, a6), angleOfLine(BNS, BSP) - angleOfDegree(15))) #new shoulder tip, with 0.05 fullness for ease in lieu of back shoulder dart 
        b6 = B.addPoint('b6', (b2.x, b1.y)) #back neck corner
        #shorten hip extension
        b7 = B.addPoint('b7', midPoint(BWC, BHC)) #new back hip center
        b8 = B.addPoint('b8', midPoint(BWS, BHS)) #new back hip side
        #lower waist dart BD3
        BD3 = B.addPoint('BD3', up(BHM, distance(BWC, BHC)/7.0)) # back waist dart point at hip
        BD3.i = B.addPoint('BD3.i', onLineAtY(BD1.i, BD3, b7.y)) #new lower waist dart inside
        BD3.o = B.addPoint('BD3.o', onLineAtY(BD1.o, BD3, b7.y)) #new lower waist dart outside
        foldReverseDart(BD3, b7) #creates BD3.m, BD3.oc, BD3.ic; dart folds towards b7 new back hip center
        extendReverseDart(b7, BD3, b8) #smooth curve at dart
        #Bodice Back B control points
        #b/w BNS back neck point & BNC back neck center
        BNC.addInpoint(right(BNC, 0.65 * abs(BNC.x - BNS.x)))
        BNS.addOutpoint(polar(BNS, abs(BNS.y - BNC.y)/4.0, angleOfLine(BNS, BNC.inpoint)))
        #b/w BUS underarm point & BAP underarm curve
        BUS.addOutpoint(polar(BUS, distance(BUS, BAP)/3.0, angleOfLine(BUS, BWS) + ANGLE90)) #perpendicular to side seam
        BAP.addInpoint(polar(BAP, distance(BUS, BAP)/3.0, angleOfLine(BNS, BAP)))
        #b/w BAP underarm curve & BSP shoulder point
        BAP.addOutpoint(polar(BAP, distance(BAP, BSP)/3.0, angleOfLine(BAP, BNS)))
        BSP.addInpoint(polar(BSP, distance(BAP, BSP)/6.0, angleOfLine(BNS, BSP) + ANGLE90)) #short control handle, perpendicular to shoulder seam

        #---Skirt Front C---#
        c1 = C.addPoint('c1', (0, 0)) #front skirt waist center
        c2 = C.addPoint('c2', right(c1, (2 * CD.back_waist_length) - distance(BWC, b7))) #front skirt hem center - length from waistline to hem is 2*back_waist_length
        c3 = C.addPoint('c3', down(c2, 3 * (distance(a2, FD3.i) + distance(FD3.o, a3)))) #front skirt waist side - skirt width is 3 * front hipline width
        c4 = C.addPoint('c4', left(c3, distance(c1, c2))) #front skirt hem side

        #---Skirt Back D---#
        d1 = D.addPoint('d1', (0, 0)) #back skirt waist center
        d2 = D.addPoint('d2', right(d1, distance(c1, c2))) #back skirt hem center
        d3 = D.addPoint('d3', down(d2, 3 * CD.back_hip/2.0)) #back skirt waist side - skirt width is 3 * back hipline width
        d4 = D.addPoint('d4', left(d3, distance(c1, c2))) #back skirt hem side

        #---------------------------------------------#
        #---all points defined, draw pattern pieces---#
        #---------------------------------------------#

        #draw dress Front A
        pnt1 = dPnt((a7.x, a4.y))
        A.setLabelPosition((pnt1))
        A.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        aG1 = dPnt(left(FUC, distance(FUC, pnt1)/4.0))
        aG2 = dPnt(down(aG1, 0.75 * distance(FNC, a2)))
        A.addGrainLine(aG1, aG2)
        A.addGridLine(['M', FSP, 'L', FSW, 'L', FSH, 'L', FHC, 'M', FWC, 'L', FSP, 'M', FUC, 'L', FUS1, 'M', FBC, 'L', FBP, 'M', FWC, 'L', FWS1, 'M', FBP, 'L', FNS, 'L', FAP, 'M', FUS, 'L', FWS2, 'M', FBP, 'L', FBS, 'M', FBP, 'L', FHM, 'M', FHC, 'L', FHS1, 'M', FWS, 'L', FD1.o, 'L', FWS, 'M', FHS, 'L', FWS, 'M', FUS, 'C', FAP, 'C', FSP, 'L', FNS, 'C', FNC])
        A.addDartLine(['M', FD3.i, 'L', FD1.i, 'L', FD1, 'L', FD1.o,  'L', FD3.o, 'M', FD2.i, 'L', FD2, 'L', FD2.oc])
        pth = (['M', a1, 'L', a2, 'L', FD3.i, 'L', FD3.m, 'L', FD3.o,  'L', a3, 'L', FWS, 'L', FD2.o, 'L', FD2.m, 'L', FD2.i, 'L', FUS, 'L', a6, 'L', a5, 'L', a7, 'L', a1])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        #draw Bodice Back B
        pnt1 = dPnt((distance(b1, b6)/2.0, 0.75 * distance(b1, BUC)))
        B.setLabelPosition((pnt1))
        B.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        bG1 = dPnt((distance(BSH, BNS)/3.0, distance(BNC, BUC)/4.0))
        bG2 = dPnt(down(bG1, 0.75 * distance(b1, b7)))
        B.addGrainLine(bG1, bG2)
        B.addGridLine(['M', BSP, 'L', BSW, 'L', BSH, 'L', BHC, 'L', BHM, 'L', BHS1, 'M', BWC, 'L', BWS1, 'M', BD1.o, 'L', BWS, 'M', BHS, 'L', BWS, 'L', BUS, 'C', BAP, 'C', BSP, 'L', BD2.o, 'L', BD2.m, 'L', BD2.i, 'L', BNS, 'C', BNC, 'M', BWC, 'L', BSP, 'M', BNS, 'L', BAP, 'M', BUC, 'L', BUS1, 'M',  BD1, 'L', BHM, 'M', BD2.ic, 'L', BD2, 'L', BD2.oc])
        B.addDartLine(['M', BD3.ic, 'L', BD1.i, 'L', BD1, 'L', BD1.o, 'L', BD3.oc])
        pth = (['M', b1, 'L', b7, 'L', BD3.i, 'L', BD3.m, 'L', BD3.o, 'L', b8, 'L', BWS, 'L', BUS, 'L', b5, 'L', b2, 'L', b6, 'L', b1])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        #draw Skirt Front C
        pnt1 = dPnt((abs(c1.x - c2.x)/2.0, abs(c1.y - c4.y)/3.0))
        C.setLetter((pnt1.x, pnt1.y), scaleby=10.0)
        C.setLabelPosition((pnt1.x, pnt1.y + 3*CM))
        cG1 = dPnt((abs(c1.x - c2.x)/8.0, abs(c1.y - c4.y)/8.0 ))
        cG2 = dPnt(right(cG1, 0.75 * distance(c1, c2)))
        C.addGrainLine(cG1, cG2)
        pth = (['M', c1, 'L', c2, 'L', c3, 'L', c4, 'L', c1])
        C.addSeamLine(pth)
        C.addCuttingLine(pth)

        #draw Skirt Back D
        pnt1 = dPnt((abs(d1.x - d2.x)/2.0, abs(c1.y - c4.y)/3.0))
        D.setLetter((pnt1.x, pnt1.y), scaleby=10.0)
        D.setLabelPosition((pnt1.x, pnt1.y + 3*CM))
        dG1 = dPnt((abs(d1.x - d2.x)/8.0, abs(d1.y - d4.y)/8.0))
        dG2 = dPnt(right(dG1, 0.75 * distance(d1, d2)))
        D.addGrainLine(dG1, dG2)
        pth = (['M', d1, 'L', d2, 'L', d3, 'L', d4, 'L', d1])
        D.addSeamLine(pth)
        D.addCuttingLine(pth)




        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

