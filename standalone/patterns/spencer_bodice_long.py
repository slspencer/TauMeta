#!/usr/bin/env python
# patternName: Womens Long Bodice Block - Spencer
# patternNumber: Block_W_Bodice-Long_Spencer

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
        self.setInfo('patternNumber', 'Block_W_Bodice-Long_Spencer')
        self.setInfo('patternTitle', 'Womens Long Bodice Block - Spencer')
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
        updatePoint(FD1, down(FD1, distance(FD1, FD1.i)/7.0)) #adjust FD1 & FD2 away from FBP bust point
        #finalize front waist side
        remainingWaistSegment = distance(FWC, t1_FWS) - distance(FWC, FD1.i)
        FWS = A.addPoint('FWS', left(FD1.o, remainingWaistSegment)) #front waist side
        #bust dart
        FD2 = A.addPoint('FD2', (FBP)) #bust dart point
        FD2.i = A.addPoint('FD2.i', intersectLineRay(t_FUS, FBS, FBP, ANGLE180 + bustDartAngle/2.0)) #bust dart inside leg
        remainingSideSegment = distance(FUS, t2_FWS) - distance(FUS, FD2.i)
        FD2.o = A.addPoint('FD2.o', leftmostP(intersectCircles(FWS, remainingSideSegment, FBP, distance(FBP, FD2.i))))
        foldDart(FD2, FUS) #creates FD2.m,FD2.oc,FD2.ic; dart folds up toward underarm side FUS
        updatePoint(FD2, left(FD2, distance(FD2, FD2.i)/7.0))
        #hip extension
        FHC = A.addPoint('FHC', down(FWC, CD.front_hip_height)) #front hip center
        FHM = A.addPoint('FHM', (FD1.x, FHC.y)) #lower waist dart point on hip line
        t_FHS = A.addPoint('t_FHS', left(FHC, CD.front_hip/2.0)) #temporary front hip side
        FHS = A.addPoint('FHS', leftmostP(intersectCircles(FHM, CD.front_hip/2.0 - distance(FHC, FHM), FWS, CD.side_hip_height)))
        FD1.d = A.addPoint('FD1.d', up(FHM, CD.front_hip_height/7.0)) #front waist dart point at hip

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
        BSH = B.addPoint('BSH', up(BWC, CD.back_shoulder_height)) #shoulder height reference point
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
        # back shoulder dart
        t_BD2 = B.addPoint('t_BD2', onLineAtLength(BNS, BST, distance(BNS, BST)/3.0)) # dart is 1/3 from BNS to BST
        BD2 = B.addPoint('BD2', onRayAtX(t_BD2, angleOfLine(BST, BNS) - ANGLE90, B_APEX.x)) # shoulder dart point
        BD2.i = B.addPoint('BD2.i', (t_BD2))
        BD2.o = B.addPoint('BD2.o', (t_BD2))
        slashAndSpread(BD2, angleOfDegree(-8), BD2.i, BNS)
        ##adjustDartLength(BNS, BD2, BST, extension=1.0) #smooth shoulder seam from BNS to BST - no curve so extend dart maximum length (1)
        foldDart(BD2, BNS) # dart folds in towards BNS BNS, creates BD2.m on seam line

        #back hip extension
        BHC = B.addPoint('BHC', down(BWC, CD.back_hip_height)) #back hip center
        BHM = B.addPoint('BHM', (BD1.x, BHC.y)) # back waist dart at hip line
        t_BHS = B.addPoint('t_BHS', right(BHC, CD.back_hip/2.0)) #temporary back hip side
        BHS = B.addPoint('BHS', rightmostP(intersectCircles(BHM, CD.back_hip/2.0 - distance(BHC, BHM), BWS, CD.side_hip_height)))
        BD1.d = B.addPoint('BD1.d', up(BHM, CD.back_hip_height/7.0)) # back waist dart point at hip

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

        #---Shirt sleeve C---#
        #get front & back armcye length
        back_armscye_curve = points2List(BUS, BUS.outpoint, BAS.inpoint, BAS, BAS.outpoint, BST.inpoint, BST)
        back_armscye_curve_length = curveLength(back_armscye_curve, n=200)
        back_lower_armscye_curve = points2List(BUS, BUS.outpoint, BAS.inpoint, BAS)
        back_lower_armscye_curve_length = curveLength(back_lower_armscye_curve, n=200)
        back_upper_armscye_curve = points2List(BAS, BAS.outpoint, BST.inpoint, BST)
        back_upper_armscye_curve_length = curveLength(back_upper_armscye_curve, n=200)

        front_armscye_curve = points2List(FUS, FUS.outpoint, FAS.inpoint, FAS, FAS.outpoint, FST.inpoint, FST)
        front_armscye_curve_length = curveLength(front_armscye_curve, n=200)
        front_lower_armscye_curve = points2List(FUS, FUS.outpoint, FAS.inpoint, FAS)
        front_lower_armscye_curve_length = curveLength(front_lower_armscye_curve, n=200)
        front_upper_armscye_curve = points2List(FAS, FAS.outpoint, FST.inpoint, FST)
        front_upper_armscye_curve_length = curveLength(front_upper_armscye_curve, n=200)

        ARMSCYE_LENGTH = back_armscye_curve_length + front_armscye_curve_length
        SLEEVE_LENGTH = CD.oversleeve_length
        BICEP_WIDTH = 1.15 * CD.bicep #15% ease in bicep
        WRIST_WIDTH = 1.25 * CD.wrist #25% ease in wrist - to allow for hand
        ELBOW_WIDTH = 1.03 * CD.elbow #3% ease in elbow - there is already ease in elbow measurement

        SBB = C.addPoint('SBB', (-BICEP_WIDTH/2.0, 0.0)) #sleeve bicep back
        SBF = C.addPoint('SBF', (BICEP_WIDTH/2.0, 0.0)) #sleeve bicep front
        SBM = C.addPoint('SBM', midPoint(SBB, SBF)) #sleeve bicep middle

        SCM = C.addPoint('SCM', highestP(intersectCircles(SBB, 0.9 * distance(BUS, BAS) + distance(BAS, BST), SBF, 0.9 * distance(FUS, FAS) + distance(FAS, FST)))) #sleeve cap middle

        SWM = C.addPoint('SWM', down(SBM, CD.undersleeve_length)) #sleeve wrist middle
        SCB = C.addPoint('SCB', onLineAtLength(SBB, SCM, distance(BUS, BAS))) #sleeve cap back
        SCF = C.addPoint('SCF', onLineAtLength(SBF, SCM, distance(FUS, FAS))) #sleeve cap front
        SWB = C.addPoint('SWB', left(SWM, WRIST_WIDTH/2.0)) #sleeve wrist back
        SWF = C.addPoint('SWF', right(SWM, WRIST_WIDTH/2.0)) #wleeve wrist front
        SEF = C.addPoint('SEF', midPoint(SBF, SWF)) #sleeve elbow front
        SEB = C.addPoint('SEB', left(SEF, ELBOW_WIDTH)) #sleve elbow back

        #cap control points
        SCM.addInpoint(left(SCM, abs(SCM.x - SBB.x)/2.0))
        SCM.addOutpoint(right(SCM, abs(SCM.x - SBF.x)/2.0))

        #b/w SBB back underarm & SCB back cap curve point
        SBB.addOutpoint(right(SBB, distance(SBB, SCB)/3.33))
        SCB.addInpoint(polar(SCB, distance(SBB, SCB)/3.33, angleOfLine(SCM.inpoint, SCB)))
        adjustCurves(back_lower_armscye_curve, SBB, SBB.outpoint, SCB.inpoint, SCB)

        #b/w SCB back cap curve point & SCM top cap
        SCB.addOutpoint(polar(SCB, distance(SCB, SCM.inpoint)/3.33, angleOfLine(SCB, SCM.inpoint)))
        adjustCurves(back_upper_armscye_curve, SCB, SCB.outpoint, SCM.inpoint, SCM)

        #front sleeve cap
        SCF.addInpoint(polar(SCF, distance(SCM.outpoint, SCF)/3.33, angleOfLine(SCF, SCM.outpoint)))
        adjustCurves(front_upper_armscye_curve, SCM, SCM.outpoint, SCF.inpoint, SCF)
        SCF.addOutpoint(polar(SCF, distance(SCF, SBF)/3.33, angleOfLine(SCM.outpoint, SCF)))
        SBF.addInpoint(polar(SBF, distance(SCF, SBF)/3.33, angleOfLine(SEF, SBF) - ANGLE90))
        adjustCurves(front_lower_armscye_curve, SCF, SCF.outpoint, SBF.inpoint, SBF)

        #---------------------------------------------#
        #---all points defined, draw pattern pieces---#
        #---------------------------------------------#

        #draw Bodice Front A
        pnt1 = dPnt(midPoint(FAS, FUC))
        A.setLabelPosition((pnt1))
        A.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        aG1 = dPnt(left(FUC, distance(FUC, pnt1)/4.0))
        aG2 = dPnt(down(aG1, distance(FNC, FWC)/2.0))
        A.addGrainLine(aG1, aG2)
        A.addGridLine(['M', FNS, 'L', FSH, 'L', FWC, 'L', FST, 'M', FUC, 'L', t_FUS, 'M', FNC, 'L', FST, 'M', FBC, 'L', FBP, 'M', FWC, 'L', t1_FWS, 'M', FBP, 'L', FNS, 'L', FAS, 'M', FUS, 'L', t2_FWS, 'M', FBP, 'L', FBS, 'M', FBP, 'L', FHM, 'M', FHC, 'L', t_FHS, 'M', FWS, 'L', FD1.o, 'L', FWS, 'M', FHS, 'L', FWS])
        A.addDartLine(['M', FD1.i, 'L', FD1, 'L', FD1.o, 'L', FD1.d, 'L', FD1.i, 'M', FD2.ic, 'L', FD2, 'L', FD2.oc])
        pth = (['M', FNC, 'L', FHC, 'L', FHM, 'L', FHS, 'L', FWS, 'L', FD2.o, 'L', FD2.m, 'L', FD2.i, 'L', FUS, 'C', FAS, 'C', FST, 'L', FNS, 'C', FNC])
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
        B.addDartLine(['M', BD1.i, 'L', BD1, 'L', BD1.o, 'L', BD1.d, 'L', BD1.i, 'M', BD2.i, 'L', BD2, 'L', BD2.o])
        pth = (['M', BNC, 'L', BHC, 'L', BHM, 'L', BHS, 'L', BWS, 'L', BUS, 'C', BAS, 'C', BST, 'L', BD2.o, 'L', BD2.m, 'L', BD2.i, 'L', BNS, 'C', BNC])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        #draw Shirt Sleeve C
        C.setLetter((SCB.outpoint.x, SEF.y), scaleby=12.0)
        C.setLabelPosition((SCB.outpoint.x, SEF.y + 2*CM))
        cG1 = dPnt((SCM.outpoint.x, SBB.y))
        cG2 = down(cG1, 0.75 * CD.undersleeve_length)
        C.addGrainLine(cG1, cG2)

        C.addGridLine(['M', SBB, 'L', SBF, 'M', SBM, 'L', SWM, 'M', SEB, 'L', SEF])
        pth = (['M', SCM, 'C', SCF, 'C', SBF, 'L', SEF, 'L', SWF, 'L', SWB, 'L', SEB, 'L', SBB, 'C', SCB, 'C', SCM])
        C.addSeamLine(pth)
        C.addCuttingLine(pth)

        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

