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

        #---Front A---#
        FNC = A.addPoint('FNC', (0.0, 0.0)) #front neck center
        FWC = A.addPoint('FWC', down(FNC, CD.front_waist_length)) #front waist center
        FSH = A.addPoint('FSH', up(FWC, CD.front_full_length)) #front shoulder height
        FSW = A.addPoint('FSW', left(FSH, CD.front_shoulder_width/2.0)) #front shoulder width
        FAW = A.addPoint('FAW', left(FSH, CD.across_chest/2.0)) #front acrosschest width
        FBW = A.addPoint('FBW', left(FSH, CD.bust/2.0)) #full front (bust) width
        FBP = A.addPoint('FBP', lowestP(onCircleAtX(FSH, CD.neck_to_bust_point, FNC.x - CD.bust_distance/2.0))) #bust center
        FBC = A.addPoint('FBC', (FNC.x, FBP.y)) #bust point
        FUC = A.addPoint('FUC', up(FBC, 2.0*IN)) #front underarm center
        FFS = A.addPoint('FFS', right(FUC, 0.5 * (CD.bust_width - CD.f_full_width)/2.0)) # front fullbust side determines slope of line from bust point to side seam
        FBS = A.addPoint('FBS', polar(FBP, CD.bust_width/2.0 - distance(FBC, FBP), angleOfLine(FFC2, FBC) + ANGLE90)) #bust side
        FST = A.addPoint('FST', highestP(onCircleAtX(FWC, CD.f_shoulder_slope, FNC.x - CD.f_cross_shoulders_width))) #front shoulder tip
        FNS = A.addPoint('FNS', rightmostP(onCircleAtY(FST, CD.shoulder_length, FSH.y))) #front neck side
        t_FSM = A.addPoint('t_FSM', midPoint(FST, FNS)) #temporary front shoulder midpoint
        FSM = A.addPoint('FSM', polar(t_FSM, 0.018 * CD.shoulder_length, angleOfLine(FST, FNS) + ANGLE90)) #front shoulder middle, lowered 1.8% of CD.shoulder_length (~1/8" for 7" shoulder)
        FCC = A.addPoint('FCC', down(FNC, 0.25 * distance(FNC, FBC))) #front across center
        FCS = A.addPoint('FCS', (FNC.x - CD.f_cross_shoulders_width, FNC.y + distance(FNC, FFC)/3.0) ) #front across side
        t_FWS = A.addPoint('t_FWS', intersectRayCircle(FBS, angleOfLine(FFS, FFC), FCS, CD.shoulder_to_side_seam - distance(FST, FCS))) #temporary front waist side
        FUS1 = A.addPoint('FUS1', onLineAtLength(t_FWS, FBS, CD.armscye_to_waist)) #front underarm side point1
        FUS2 = A.addPoint('FUS2', slashAndSpread(t_FWS, -angleOfChord(0.038 * CD.bust_width, CD.armscye_to_waist), FUS1)) #front underarm side point2 with 3.38% ease - 3/4" for 20" front bust or 36" bust
        t_FWM = A.addPoint('t_FWM', (FBP.x, FWC.y)) #temporary front waist middle - under front bust point
        front_waist_total = distance(t_FWS, t_FWM) + distance(t_FWM, FWC)
        front_dart_width = front_waist_total - CD.f_waist/2.0
        FD1 = A.addPoint('FNC', down(FBP, distance(FBP, t_FWM)/7.0)) #front waist dart point
        FD1.i = A.addPoint('FD1.i', right(t_FWM, 0.25 * front_dart_width)) #front waist dart inside leg
        t_FD1o = A.addPoint('t_FD1o', onLineAtLength(FDM, (0.75 * front_dart_width) - (0.021 * CD.f_waist))) #front waist dart outside leg with 2.1% waist ease (1/4" for 12" front_waist or 24" waist)
        FD1.o = A.addPoint('FD1.o', onLineAtLength(FBP, t_FD1o, distance(FBP, FD1.i))) #
        foldDart(FD1, FWC) #create FD1.m for seamline, FD1.oc and FD1.ic for dartline
        FWM = A.addPoint('FWM', polar(FD1.o, distance(FD1.i, t_FWM), angleOfLine(FD1.o, FBP) - angleOfVector(t_FWM, FD1.i, FBP))) #front waist middle - will be under bust point when dart is sewn

        #Front A control points
        #b/w FNS front neck point & FNC front neck center
        FNS.addOutpoint(polar(FNS, abs(FNC.y - FNS.y)/4.0, angleOfLine(FST, FNS) + ANGLE90))
        FNC.addInpoint(left(FNC, 0.75 * abs(FNC.x - FNS.x)))
        #b/w FUS1 front undearm side & FCS front across chest side
        FUS1.addOutpoint(polar(FUS1, distance(FUS1, FCS)/3.0, angleOfLine(FUS2, FUS1)))
        FCS.addInpoint(polar(FCS, distance(FUS1, FCS)/3.0, angleOfLine(FST, FCS)))


        #---Back B---#
        BNC = B.addPoint('BNC', (0.0, 0.0)) #back neck center
        BWC = B.addPoint('BWC', down(BNC, CD.b_center_waist_length)) #back waist center
        BSH = B.addPoint('BSH', up(BWC, CD.b_full_waist_length)) #back shoulder height
        BSW = B.addPoint('BSW', right(BSH, CD.b_shoulder_width/2.0)) #back shoulder width
        BAW = B.addPoint('BAW', right(BSH, CD.b_across_width/2.0)) #back acrossback width
        BFW = B.addPoint('BFW', right(BSH, CD.b_full_width/2.0)) #full back width
        BWW = B.addPoint('BWW', right(BWC, CD.b_waist/2.0))

        BST = B.addPoint('BST', highestP(onCircleAtX(BWC, CD.b_shoulder_slope, BNC.x + CD.b_cross_shoulders_width))) #back shoulder tip
        BNS = B.addPoint('BNS', leftmostP(onCircleAtY(BST, CD.b_shoulder_length, BSH.y))) #back neck side
        t_BSM = B.addPoint('t_BSM', midPoint(BST, BNS)) #temporary back shoulder midpoint
        BSM = B.addPoint('BSM', polar(t_BSM, 0.018 * CD.shoulder_length, angleOfLine(BST, BNS) - ANGLE90)) #back shoulder middle, lowered 1.8% of CD.shoulder_length (~1/8" for 7" shoulder)

        t_BWS1 = B.addPoint('t_BWS', (BFW.x, BWC.y)) #temporary back waist side1
        t_BUS1 = B.addPoint('t_BUS', up(t_BWS1, CD.side_length)) #temporary underarm side
        BCC = B.addPoint('BCC', (BNC.x, (t_BUS.y - BST.y)/2.0)) #back across center
        BCS = B.addPoint('BCS', (BCW.x, BCC.y)) #back across side

        t_BWS2 = B.addPoint('t_BWS2', intersectLineCircle(BWW, t_BWS1, BCS, CD.b_shoulder_to_side_seam - distance(BST, BCS))) #temporary back waist side2
        t_BUS2 = B.addPoint('t_BUS2', up(t_BWSw, CD.armscye_to_waist)) #back underarm side1
        t_BUS3 = B.addPoint('t_BUS3', right(BUS1, 0.038 * CD.b_full_back_width)) #temporary back underarm side2 w/ 3.8% ease
        BUC = B.addPoint('BUC', (BNC.x, BUS1.y)) #back underarm center

        back_waist_total = distance(BWC, t_BWS1)
        back_dart_width = back_waist_total - CD.b_waist/2.0
        t_BWS3 = left(t_BWS1, back_dart_width/2.0) #temporary back waist side3
        BWM = B.addPoint('BWM', midPoint(BWC, t_BWS3)) #back waist middle
        BWS = B.addPoint('BWS', onLineAtLength(BCS, t_BWS3, distance(BCS, t_BWS2))) #back waist side
        BUS = B.addPoint('BUS', onLineAtLength(BWS, t_BUS3, CD.armscye_to_waist)) #back underarm side

        BD1 = B.addPoint('BD1', (BWM.x, BUC.y)) #back waist dart point
        BD1.i = B.addPoint('BD1.i', left(BWM, 0.25 * back_dart_width)) #back waist dart inside leg
        t_BD1o = B.addPoint('t_BD1o', onLineAtLength(BWM, BWS, (0.25 * back_dart_width) - (0.021 * CD.b_waist))) #back waist dart outside leg with 2.1% waist ease (1/4" for 12" back_waist or 24" waist)
        BD1.o = B.addPoint('BD1.o', onLineAtLength(BD1, t_BD1o, distance(BD1.o, BD1.i))) #back dart outside leg
        foldDart(BD1, BWC) #create BD1.m for seamline, BD1.oc and BD1.ic for dartline

        #Back B control points
        #b/w BNS back neck point & BNC back neck center
        BNC.addInpoint(right(BNC, 0.75 * abs(BNC.x - BNS.x)))
        BNS.addOutpoint(polar(BNS, abs(BNC.y - BNS.y)/4.0, angleOfLine(BNS, BNC.inpoint)))

        #b/w BUS back undearm side & BCS cross back side
        BUS.addOutpoint(left(BUS, distance(BUS, BCS)/3.0))
        BCS.addInpoint(polar(BCS, distance(BUS, BCS)/3.0, angleOfLine(BST, BCS)))

        #b/w BD1.o back waist dart outside leg & BWS back waist side
        BD1.o.addOutpoint(polar(BD1.o, distance(BD1.o, BWM), angleOfLine(BD1.o, BD1) + angleOfVector(BWM, BD1.i, BD1))) #back waist middle
        BWS.addInpoint(polar(BWS, angleOfLine(BWS, BD1.o)))

        #back neck dart
        neck_curve = points2List(BNS, BNS.outpoint, BNC.inpoint, BNC)
        curve_length = curveLength(neck_curve)
        neck_dart_width = curve_length - CD.b_neck_base/2.0
        split_curve = splitCurveAtLength(neck_curve, 0.5 * total_curve_length)
        split_point = split_curve[3]
        upper_curve = points2List(BNS, split_curve[1], split_curve[2], split_point)
        lower_curve = points2List(split_point, split_curve[4], split_curve[5], BNC)
        BD2 = down(split_point, 0.5 * distance(BNC, BCC))
        BD2.i = onCurveAtLength(lower_curve, neck_dart_width/2.0)
        BD2.o = onCurveAtLength(upper_curve, curveLength(upper_curve) - neck_dart_width/2.0)
        foldDart(BD2, BNC) #fold dart towards BNC - creates BD2.m for seamline, BD2.ic & BD2.oc for dartline

        #---Sleeve C---#
        upperarm_width = (0.1 * CD.upperarm_width) + (0.038 * CD.bust)
        SCM = C.addPoint('SCC', (0.0, 0.0)) #sleeve cap middle
        SWM = C.addPoint('SWM', down(SCM, CD.shoulder_to_wrist)) #sleeve wrist middle
        SUM = C.addPoint('SUM', up(SWM, CD.underarm_length)) #sleeve underarm middle
        SEM = C.addPoint('SEM', down(SCM, CD.shouler_to_elbow_length)) #sleeve elbow middle

        SUF1 = C.addPoint('SUF1', right(SUM, upper_arm_width)) #sleeve underarm front
        SUF2 = C.addPoint('SUF2', midPoint(SUF1, SUM)) #midpoint b/w undearm front & underarm middle
        SUF3 = C.addPoint('SUF3', midPoint(SUF2, SUF3)) #sleeve cap back 1

        SCF1 = C.addPoint('SCF1', right(SCM, distance(SUF3, SUF1))) #sleeve cap front 1
        SCF2 = C.addPoint('SCF2', onLineAtLength(SCF1, SUB3, distance(SCF1, SCM))) #sleeve cap front 2
        SCF3 = C.addPoint('SCF3', onLineAtLength(SUF3, distance(SUF1, SUF3))) #sleeve cap front 3

        SUB1 = C.addPoint('SUB1', left(SUM, upper_arm_width)) #sleeve underarm back
        SUB2 = C.addPoint('SUB2', midPoint(SUB1, SUM)) #midpoint b/w underarm back & underarm middle
        SUB3 = C.addPoint('SUB3', 0.5 * distance(SUF3, SUF1)) #sleeve cap back 1

        SCB1 = C.addPoint('SCB1', left(SCM, distance(SUF3, SUF1))) #sleeve cap back 1
        SCB2 = C.addPoint('SCB2', onLineAtLength(SCB1, SUB3, distance(SCM, SCB1))) #sleeve cap back 2
        SCB3 = C.addPoint('SCB3', onLineAtLength(SUB3, distance(SUB3, SUB1))) #sleeve cap back 3

        SEB1 = C.addPoint('SEB1', left(SEM, CD.elbow_width/2.0)) #sleeve elbow back
        SEB2 = C.addPoint('SEB2', midPoint(SEB1, SEM)) #midpoint b/w elbow back & elbow middle
        SEF1 = C.addPoint('SEF1', right(SEM, CD.elbow_width/2.0)) #sleeve elbow front
        SEF2 = C.addPoint('SEF2', midPoint(SEF1, SEM)) #midpoint b/w elbow front & elbow middle
        SWF2 = C.addPoint('SWF2', polar(SWM, CD.wrist_width/2.0, angleOfLine(SEB2, SWM) - ANGLE90)) #sleeve wrist front 2
        SWF3 = C.addPoint('SWF3', midPoint(SWM, SWF2)) #sleeve wrist front 3
        SWF1 = C.addPoint('SWF1', intersectRayCircle(SWF2, angleOfLine(SEF2, SWF2) - ANGLE90, SWF1, distance(SWF1, SWF2))) #sleeve wrist front
        SWB = C.addPoint('SWB', extendLine(SWF2, SWM, distance(SWF2, SWM))) #sleeve wrist back

        #Sleeve C control points
        #b/w SCM sleeve cap middle & SCF2 sleeve cap front 2
        SCM.addOutpoint((SCF1))
        SCF2.addInpoint((SCF1))
        SCF3.addOutpoint((SUB3))
        SUB1.addInpoint((SUB3))
        SUB1.addOutpoint((SEF1))
        SWF1.addInpoint((SEF1))
        SWF1.addOutpoint((SWF2))
        SWF3.addInpoint((SWF2))

        #sleeve elbow dart
        front_sleeve_length =curveLength(points2List(SUF1, SEF1, SEF1, SWF1))
        back_sleeve_length = distance(SUB1, SEB1) + distance(SEB1, SWB)
        elbow_dart_width = back_sleeve_length - front_sleeve_length
        SD1 = C.addPoint('SD1', (SEB2)) #elbow dart point
        SD1.o = C.addPoint('SD1.o', (SEB1)) #elbow inside leg
        SD1.i = C.addPoint('SD1.i', onLineAtLength(SEB1, SWB, elbow_dart_width))


        #draw Front A
        pnt1 = midPoint(FCC, FCS)
        A.setLabelPosition((pnt1))
        A.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        aG1 = dPnt(left(FUC, distance(FUC, pnt1)/4.0))
        aG2 = dPnt(down(aG1, 0.75 * distance(FNC, FWC)))
        A.addGrainLine(aG1, aG2)
        A.addGridLine(['M', FBW, 'L', FSH, 'L', FSH, 'L', FWC, 'L', FWS, 'M', FUS, 'L', FUS2, 'M', FAC, 'L', FAS, 'M', FBC, 'L', FBP, 'L', FBS, 'M', FWC, 'L', t1_FWS, 'M', FBP, 'L', FNS, 'M', FUS2, 'L', t2_FWS])
        A.addDartLine(['M', FD1.ic, 'L', FD1, 'L', FD1.oc])
        pth = (['M', FNC, 'L', FWC, 'L', FD1.i, 'L', FD1.m, 'L', FD1.o,  'L', FWS, 'L', FUS2, 'C', FCS, 'L', FST, 'L', FNS, 'C', FNC])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        #draw Back B
        pnt1 = midPoint(BCC, BCS)
        B.setLabelPosition((pnt1))
        B.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        bG1 = dPnt((distance(BSH, BNS)/2.0, distance(BNC, BUC)/4.0))
        bG2 = dPnt(down(bG1, 0.75 * distance(BNC, BWC)))
        B.addGrainLine(bG1, bG2)
        B.addGridLine(['M', BFW, 'L', BSH, 'L', BWC, 'L', BST, 'L', BNC, 'M', BWC, 'L', t_BWS, 'M', BD1.o, 'L', BWS, 'M', BCC, 'L', BCS, 'M', BUS, 'L', BUC])
        B.addDartLine(['M', BD1.ic, 'L', BD1, 'L', BD1.oc])
        pth = (['M', BNC, 'L', BWC, 'L', BD1.i, 'L', BD1.m, 'L', BD1.o, 'L', BWS, 'L', BUS, 'C', BBS, 'L', BST, 'L', BNS, 'C', BNC])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)


        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

