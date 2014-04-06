# !/usr/bin/python
#
# mrohr_fitted_bodice_special_measurement.py
# Inkscape extension - Effects - Sewing Patterns - Shirt Waist Allington
# Copyright (C) 2010, 2011, 2012 Susan Spencer, Steve Conklin <www.taumeta.org>

'''
Licensing paragraph :

1. CODE LICENSE :  GPL 2.0 +
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT FNY WARRFNTY; without even the implied warranty of
MERCHFNTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111 - 1307  USA

2. PATTERN LICENSE :  CC BY - NC 3.0
The output of this code is a pattern and is considered a
visual artwork. The pattern is licensed under
Attribution - NonCommercial 3.0 (CC BY - NC 3.0)
<http : //creativecommons.org/licenses/by - nc/3.0/>
Items made from the pattern may be sold;
the pattern may not be sold.

End of Licensing paragraph.
'''

from tmtpl.designbase import *
from tmtpl.document import *
from tmtpl.pattern import *
from tmtpl.patternmath import *
from tmtpl.constants import *
from tmtpl.utils import *

class Design(designBase):

    def pattern(self) :
        """
        Method defining a pattern design. This is where the designer places
        all elements of the design definition
        """

        # The designer must supply certain information to allow
        #   tracking and searching of patterns
        #
        # This group is all mandatory
        #
        self.setInfo('patternNumber', 'MR_B1')
        self.setInfo('patternTitle', 'Spencer Bodice - Short')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'S.L.Spencer')
        self.setInfo('patternmakerName', 'S.L.Spencer')
        self.setInfo('description', """This is a bodice block pattern which contains minimum fit ease.""")
        self.setInfo('category', 'Shirt/TShirt/Blouse')
        self.setInfo('type', 'Block')
        #
        # The next group are all optional
        #
        self.setInfo('gender', 'F') # 'M',  'F',  or ''
        self.setInfo('yearstart', '1900')
        self.setInfo('yearend', '')
        self.setInfo('culture', 'European')
        self.setInfo('wearer', '')
        self.setInfo('source', '')
        self.setInfo('characterName', '')
        self.setInfo('recommendedFabric', '')
        self.setInfo('recommendedNotions', '')

        #get client data
        CD = self.CD #client data is prefaced with CD

        #create a pattern named 'bodice'
        bodice = self.addPattern('bodice')

        #create pattern pieces,  assign an id lettercd ..
        A = bodice.addPiece('Bodice Front', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = bodice.addPiece('Bodice Back', 'B', fabric = 2, interfacing = 0, lining = 0)
        C = bodice.addPiece('Sleeve', 'C', fabric = 2, interfacing = 0, lining = 0)

        #pattern points
        # x, y coordinates are always passed as a two-item list like this: (23.6, 67.0)
        # points are always in the 'reference' group, and always have style='point_style'

        #---Front A---#
        FNC = A.addPoint('FNC', (0.0, 0.0)) #front neck center
        FWC = A.addPoint('FWC', down(FNC, CD.front_waist_length)) #front waist center
        FWO = A.addPoint('FWO', right(FWC, 0.03 * CD.front_waist)) #front waist offset
        FSH = A.addPoint('FSH', up(FWC, CD.front_shoulder_height)) #front shoulder height
        FSW = A.addPoint('FSW', right(FSH, 0.5 * CD.front_shoulder_width)) #front shoulder width
        FSP = A.addPoint('FSP', highestP(onCircleAtX(FWO, CD.front_shoulder_balance, FSW.x))) #front shoulder point
        FNS = A.addPoint('FNS', leftmostP(onCircleAtY(FSP, CD.shoulder, FSH.y))) #front neck side
        FAP2 = A.addPoint('FAP2', rightmostP(onCircleAtX(FNS, CD.front_underarm_balance, 0.5 * CD.across_chest))) #front armscye point 2
        FUC = A.addPoint('FUC', (FNC.x, FAP2.y)) #front underarm center
        FUS4 = A.addPoint('FUS4', right(FUC, 0.5 * CD.front_underarm)) #front underarm side 4 - inline with front underarm center & front armscye

        bust_ease = 0.04 * CD.bust/4.0
        FBP = A.addPoint('FBP', rightmostP(onCircleAtX(FNS, CD.bust_balance + bust_ease, 0.5 * CD.bust_distance))) #bust point
        FBC = A.addPoint('FBC', (FNC.x, FBP.y)) #bust center
        FBS = A.addPoint('FBS', rightmostP(onCircleTangentFromOutsidePoint(FBP, (0.5 * CD.front_bust) - distance(FBC, FBP), FUS4))) #front bust side

        FUS3 = A.addPoint('FUS3', polar(FAP2, distance(FAP2, FUS4), angleOfLine(FBP, FBS))) #front underarmside 3 - parallel to bustline
        FAP = A.addPoint('FAP', polar(FAP2, bust_ease, angleOfLine(FBP, FBS))) #front armscye point - incl. bust ease parallel to bustline
        FUS2 = A.addPoint('FUS2', intersectLines(FUS3, FBS, FUC, FUS4)) # front underarm side 2 - parallel to underarmline
        FUS = A.addPoint('FUS', polar(FUS2, bust_ease, angleOfLine(FUC, FUS4))) # front underarm side - incl. bust ease parallel to underarmline
        FWS2 = A.addPoint('FWS2', onLineAtLength(FUS3, FBS, CD.side + distance(FWC, FWO))) #front waist side 2 - extend side by waist offset (FWO pushes bodice up at shoulder tip)
        FWS = A.addPoint('FWS', polar(FWS2, bust_ease, angleOfLine(FUC, FUS4))) #front waist side - incl. bust_ease parallel to underarmline

        #front waist dart 1
        full_bust = 'false'
        FD1 = A.addPoint('FD1', FBP) #front dart point
        FD1.i = A.addPoint('FD1.i', right(FWC, 0.4 * CD.bust_distance)) #dart inside leg
        FD1.o = A.addPoint('FD1.o', lowestP(intersectCircles(FBP, distance(FBP, FD1.i), FWS, 0.5 * CD.front_waist - distance(FWC, FD1.i)))) #dart outside leg
        updatePoint(FD1, polar(FBP, 0.12 * distance(FBP, FD1.i), angleOfLine(FBP, FD1.i) - 0.5 * angleOfVector(FD1.o, FBP, FD1.i))) #lower front waist dart 1 point

        #create front waist dart 2 if full bust
        total_dart_angle = angleOfVector(FD1.i, FBP, FD1.o)
        total_dart_width = distance(FD1.i, FD1.o)
        max_dart_width = CD.front_bust/6.0 #1/3 of half front bust
        if total_dart_width > max_dart_width: #if waist dart width > 1/3 of half front bust
            full_bust = 'true'
            #change 1st bust dart width to 2/3 total_dart_width
            updatePoint(FD1.o, polar(FBP, distance(FBP, FD1.i), angleOfLine(FBP, FD1.i) - 2/3.0 * total_dart_angle))
            updatePoint(FD1, polar(FBP, 0.12 * distance(FBP, FD1.i), angleOfLine(FBP, FD1.i) - 0.5 * angleOfVector(FD1.o, FBP, FD1.i))) #lower front waist dart 1 point with new narrower dart width
            #add second bust dart
            FBP2 = A.addPoint('FBP2', onLineAtLength(FBP, FBS, 1.5 * distance(FBP, FD1))) #2nd bust point
            FD2 = A.addPoint('FD2', FBP2) #2nd dart point
            pnt_m = intersectLineRay(FD1.o, FWS, FD2, angleOfLine(FBP, FBS) + ANGLE90)
            FD2.i = A.addPoint('FD2.i', intersectLineRay(FD1.o, FWS, FD2, angleOfLine(FD2, pnt_m) + total_dart_angle/6.0)) #2nd dart inside leg is parallel to 1st dart outside leg
            FD2.o = A.addPoint('FD2.o', polar(FD2, distance(FD2, FD2.i), angleOfLine(FD2, FD2.i) - total_dart_angle/3.0))
            updatePoint(FD2, polar(FBP2, distance(FBP, FD1), angleOfLine(FD2, FD2.i) - total_dart_angle/6.0)) #lower 2nd dart point - needed for rotation
            #rotate 2nd dart to appear parallel to 1st dart
            pivot = FD2
            rotation_angle = angleOfLine(FD2, FD2.i) - angleOfLine(FD1, FD1.o)
            slashAndSpread(pivot, -rotation_angle, FD2.i, FD2.o)
            updatePoint(FD2.i, intersectLines(FD2, FD2.i, FD1.o, pnt_m))
            updatePoint(FD2.o, intersectLines(FD2, FD2.o, FD1.o, pnt_m))
            updatePoint(FD2, polar(FD2, distance(FBP, FD1), angleOfLine(FD2, FD2.i) - total_dart_angle/6.0)) #lower 2nd dart point after rotation
            #lower 2nd dart point


        #front control points
        #b/w FNS & FNC
        FNC.addInpoint(right(FNC, 0.6 * abs(FNC.x - FNS.x)))
        FNS.addOutpoint(polar(FNS, 0.5 * abs(FNC.y - FNS.y), angleOfLine(FNS, FNC.inpoint)))
        #b/w FUS & FAP
        FUS.addOutpoint(polar(FUS, 0.4 * distance(FUS, FAP), angleOfLine(FUS, FWS) + ANGLE90))
        FAP.addInpoint(polar(FAP, 0.33 * distance(FUS, FAP), angleOfLine(FNS, FAP)))
        #b/w FAP & FSP
        FAP.addOutpoint(polar(FAP, 0.3 * distance(FAP, FSP), angleOfLine(FAP, FNS)))
        FSP.addInpoint(polar(FSP, 0.15 * distance(FAP, FSP), angleOfLine(FSP, FNS) - ANGLE90))
        #b/w FWC & FD1.i
        FWC.addOutpoint(right(FWC, 0.33 * distance(FWC, FD1.i)))
        FD1.i.addInpoint(left(FD1.i, 0.5 * distance(FWC, FD1.i)))
        #b/w FD1.o & FWS ... or FD1.o & FD2.i
        if full_bust == 'true':
             #b/w FD2.o & FWS
            FD2.o.addOutpoint(onLineAtLength(FD2.o, FWS, 0.33 * distance(FD2.o, FWS)))
            FWS.addInpoint(polar(FWS, 0.15 * distance(FD2.i, FWS), angleOfLine(FWS, FD2.o)))
        else:
            #b/w FD1.o & FWS
            FD1.o.addOutpoint(onLineAtLength(FD1.o, FWS, 0.33 * distance(FD1.o, FWS)))
            FWS.addInpoint(polar(FWS, 0.33 * distance(FD1.o, FWS), angleOfLine(FWS, FD1.o)))
        #extend front waist dart 1 for smoother waistline
        theta = angleOfVector(FD1.i.inpoint, FD1.i, FD1) - ANGLE90
        r = distance(FD1.i.inpoint, FD1.i)
        updatePoint(FD1.i, dPnt(extendLine(FD1, FD1.i, r * sin(theta))))
        updatePoint(FD1.o, dPnt(extendLine(FD1, FD1.o, r * sin(theta))))
        #extend fold length to meet seamline when folded toward front waist center
        foldDart(FD1, FWC) #creates FD1.m for seamline, FD1.ic & FD1.oc for dartline
        if full_bust == 'true':
            #extend front waist dart 2 for smoother waistline
            theta = angleOfVector(FD1.o, FD2.i, FD2) - ANGLE90
            r = distance(FD1.o, FD2.i)
            updatePoint(FD2.i, dPnt(extendLine(FD2, FD2.i, r * sin(theta))))
            updatePoint(FD2.o, dPnt(extendLine(FD2, FD2.o, r * sin(theta))))
            #extend dart fold length to meet seamline when folded toward FWC front waist center
            foldDart(FD2, FD1.o) #creates BD1.m for seamline, BD1.ic & BD1.oc for dartline

        #---Back B---#
        BNC = B.addPoint('BNC', (0.0, 0.0)) #back neck center
        BWC = B.addPoint('BWC', down(BNC, CD.back_waist_length)) #back waist center
        BWO = B.addPoint('BWO', left(BWC, 0.03 * CD.back_waist)) #back waist offset - 3% of back waist
        BSH = B.addPoint('BSH', up(BWC, CD.back_shoulder_height)) #back shoulder height
        BSW = B.addPoint('BSW', left(BSH, 0.5 * CD.back_shoulder_width)) #back shoulder width
        BSP = B.addPoint('BSP', highestP(onCircleAtX(BWO, CD.back_shoulder_balance, BSW.x))) #back shoulder point
        BNS = B.addPoint('BNS', rightmostP(onCircleAtY(BSP, 1.06 * CD.shoulder, BSH.y))) #back neck side
        BAP2 = B.addPoint('BAP2', lowestP(onCircleAtX(BNS, CD.back_underarm_balance, BNC.x - 0.5 * CD.across_back))) #back armscye point 2
        BAP = B.addPoint('BAP', left(BAP2, bust_ease)) #back armscye point - incl. ease
        BUC = B.addPoint('BUC', (BNC.x, BAP.y)) #back underarm center
        BUS3 = B.addPoint('BUS3', left(BUC, 0.5 * CD.back_underarm)) #back underarm side 3
        BUS2 = B.addPoint('BUS2', down(BUS3, distance(FUS3, FUS4))) #back underarm side 2 - lowered same as front
        BUS = B.addPoint('BUS', left(BUS2, bust_ease)) #back underarm side (6% ease)
        #back waist dart

        #BD1 = B.addPoint('BD1', up(b_apex, 0.5 * distance(b_apex, intersectLines(BWO, BSP, BAP, BNS)))) #back waist dart point
        BD1 = B.addPoint('BD1', intersectLines(BWO, BSP, BUC, BAP2)) #back waist dart point
        pnt_m = (BD1.x, BWC.y) #dart midpoint at waist
        BD1.i = B.addPoint('BD1.i', right(pnt_m, 0.1 * distance(pnt_m, BWC))) #dart inside point on waistline
        BD1.o = B.addPoint('BD1.o', left(pnt_m, distance(pnt_m, BD1.i))) #dart outside point on waistline
        updatePoint(BD1, down(BD1, 0.1 * distance(BD1, BD1.o))) #lowered dart point
        #back waist
        BWS2 = B.addPoint('BWS2', lowestP(intersectCircles(BUS2, distance(FUS2, FWS2), BD1.o, 0.5 * CD.back_waist - distance(BWC, BD1.i)))) #back waist side
        BWS = B.addPoint('BWS', left(BWS2, bust_ease)) #back underarm side - incl. bust_ease
        #smooth dart at waist
        extendDart(BWC, BD1, BWS)
        foldDart(BD1, BWC)

        #back shoulder dart
        dart_width = distance(BSP, BNS) - distance(FSP, FNS)
        pnt_m = midPoint(BSP, BNS) #midpoint of shoulder dart at shoulder seam
        pnt_p = intersectLineRay(BNS, BAP, pnt_m, angleOfLine(BSP, BNS) + ANGLE90)
        BD2 = B.addPoint('BD2', onLineAtLength(pnt_m, pnt_p, 0.75 * distance(pnt_m, pnt_p))) #back shoulder dart point
        BD2.i = B.addPoint('BD2.i', onLineAtLength(pnt_m, BNS, 0.5 * dart_width)) #back shoulder dart inside leg
        BD2.o = B.addPoint('BD2.o', onLineAtLength(pnt_m, BSP, 0.5 * dart_width)) #back shoulder dart outside leg
        extendDart(BSP, BD2, BNS, extension=1) #smooth shoulder seam at dart
        foldDart(BD2, BNS) #fold dart toward BNS

        #back control points
        #b/w BNS & BNC
        BNC.addInpoint(left(BNC, 0.75 * abs(BNC.x - BNS.x)))
        BNS.addOutpoint(polar(BNS, 0.5 * abs(BNC.y - BNS.y), angleOfLine(BNS, BNC.inpoint)))
        #b/w BUS & BAP
        BUS.addOutpoint(polar(BUS, 0.5 * abs(BUS.x - BAP.x), angleOfLine(BWS, BUS) + ANGLE90))
        BAP.addInpoint(polar(BAP, 0.5 * abs(BUS.y - BAP.y), angleOfLine(BNS, BAP2)))
        #b/w BAP & BSP
        BAP.addOutpoint(polar(BAP, 0.33 * distance(BAP, BSP), angleOfLine(BAP2, BNS)))
        BSP.addInpoint(polar(BSP, 0.15 * distance(BAP, BSP), angleOfLine(BSP, BNS) + ANGLE90))
        #b/w FWC & FD1.i
        BWC.addOutpoint(left(BWC, 0.33 * distance(BWC, BD1.i)))
        BD1.i.addInpoint(right(BD1.i, 0.33 * distance(BWC, BD1.i)))
        #b/w FD1.o & FWS
        BD1.o.addOutpoint(onLineAtLength(BD1.o, BWS, distance(BD1.i, BD1.i.inpoint)))
        BWS.addInpoint(polar(BWS, 0.15 * distance(BD1.o, BWS), angleOfLine(BUS, BWS) - angleOfVector(FWS.inpoint, FWS, FUS)))
        #extend front waist dart legs for smoother waistline
        theta = angleOfVector(BD1.i.inpoint, BD1.i, BD1) - ANGLE90
        r = distance(BD1.i.inpoint, BD1.i)
        updatePoint(BD1.i, dPnt(extendLine(BD1, BD1.i, r * sin(theta))))
        updatePoint(BD1.o, dPnt(extendLine(BD1, BD1.o, r * sin(theta))))
        #extend dart fold length to meet seamline when folded toward BWC back waist center
        foldDart(BD1, BWC) #creates BD1.m for seamline, BD1.ic & BD1.oc for dartline

        #---Sleeve C---#
        #get front & back armcye length
        back_armscye = points2List(BUS, BUS.outpoint, BAP.inpoint, BAP, BAP.outpoint, BSP.inpoint, BSP)
        front_armscye = points2List(FUS, FUS.outpoint, FAP.inpoint, FAP, FAP.outpoint, FSP.inpoint, FSP)
        ARMSCYE_LENGTH = curveLength(back_armscye) + curveLength(front_armscye)
        SCM = C.addPoint('SCM', (0.0, 0.0)) #sleeve cap midpoint - top of sleeve
        SUM = C.addPoint('SUM', (SCM.x, SCM.y + ARMSCYE_LENGTH / 4.0 + 1.5 * CM)) #sleeve underarm midpoint
        SWM = C.addPoint('SWM', (SCM.x, SCM.y + CD.oversleeve_length + 6 * CM)) #sleeve wrist midpoint
        SEM = C.addPoint('SEM', midPoint(SUM, SWM)) #sleeve elbow midpoint
        SUB = C.addPoint('SUB', (SUM.x + (ARMSCYE_LENGTH / 2.0 - 0.5 * CM), SUM.y)) #sleeve underarm back
        SWB1 = C.addPoint('SWB1', (SUB.x, SWM.y)) #back wrist line
        SUF = C.addPoint('SUF', (SUM.x - (ARMSCYE_LENGTH / 2.0 - 0.5 * CM), SUM.y)) #sleeve underarm front
        CWF1 = C.addPoint('CWF1', (SUF.x, SWM.y)) #front wrist line
        #back armscye points
        SCB1 = C.addPoint('SCB1', onLineAtLength(SUB, SCM, distance(SUB, SCM) / 4.0)) #sleeve cap back 1
        SCB2 = C.addPoint('SCB2', polar(midPoint(SUB, SCM), 1 * CM, angleOfLine(SUB, SCM) + ANGLE90)) #sleeve cap back 2
        pnt = onLineAtLength(SUB, SCM, 0.75 * distance(SUB, SCM))
        SCB3 = C.addPoint('SCB3', polar(pnt, 2 * CM, angleOfLine(SUB, SCM) + ANGLE90)) #sleeve cap back 3
        #front armscye points
        pnt = onLineAtLength(SUF, SCM, distance(SUF, SCM) / 4.0)
        SCF1 = C.addPoint('SCF1', polar(pnt, 1 * CM, angleOfLine(SUF, SCM) + ANGLE90)) #sleeve cap front 1
        SCF2 = C.addPoint('SCF2', midPoint(SUF, SCM)) #sleeve cap front 2
        pnt = onLineAtLength(SUF, SCM, 0.75 *  distance(SUF, SCM))
        SCF3 = C.addPoint('SCF3', polar(pnt, 1 * CM, angleOfLine(SUF, SCM) - ANGLE90)) #sleeve cap front 3
        SWB3 = C.addPoint('SWB3', onLineAtLength(SWM, SWB1, 0.7 * CD.wrist)) #back wrist point
        SWF = C.addPoint('SWF', onLineAtLength(SWM, CWF1, 0.7 * CD.wrist)) #sleeve wrist front
        SWB2 = C.addPoint('SWB2', midPoint(SWB1, SWB3)) #wristline reference point
        SWF2 = C.addPoint('SWF2', midPoint(CWF1, SWF)) #wristline reference point
        SEB = C.addPoint('SEB', right(SEM, 0.65 * CD.elbow)) #sleeve elbow back
        SEF = C.addPoint('SEF', left(SEM, 0.55 * CD.elbow)) #sleeve elbow front

        #Sleeve C control points
        cArray = points2List(SUB, SCB1, SCB2, SCB3, SCM, SCF3, SCF2, SCF1, SUF)
        C1, C2 = controlPoints('sleeve_cap', cArray)
        SUB.addOutpoint(C1[0])
        SCB1.addInpoint(C2[0])
        SCB1.addOutpoint(C1[1])
        SCB2.addInpoint(C2[1])#
        SCB2.addOutpoint(C1[2])
        SCB3.addInpoint(C2[2])
        SCB3.addOutpoint(C1[3])
        SCM.addInpoint(C2[3])
        SCM.addOutpoint(C1[4])
        SCF3.addInpoint(C2[4])
        SCF3.addOutpoint(C1[5])
        SCF2.addInpoint(C2[5])
        SCF2.addOutpoint(C1[6])
        SCF1.addInpoint(C2[6])
        SCF1.addOutpoint(C1[7])
        SUF.addInpoint(C2[7])
        cArray = points2List(SWB3, SEB, SUB)
        C1, C2 = controlPoints('sleeve_seam1', cArray)
        SWB3.addOutpoint(C1[0])
        SEB.addInpoint(C2[0])
        SEB.addOutpoint(C1[1])
        SUB.addInpoint(C2[1])
        cArray = points2List(SUF, SEF, SWF)
        C1, C2 = controlPoints('sleeve_seam2', cArray)
        SUF.addOutpoint(C1[0])
        SEF.addInpoint(C2[0])
        SEF.addOutpoint(C1[1])
        SWF.addInpoint(C2[1])
        #elbow dart & lower sleeve control points
        SD1 = C.addPoint('SD1',  midPoint(SEB, SEM)) #elbow dart point
        SD1.i = C.addPoint('SD1.i', (SEB)) #elbow dart inside leg
        SD1.o = C.addPoint('SD1.o', onLineAtLength(SEB, SEB.inpoint, CD.oversleeve_length/20.0)) #elbow dart outside leg
        SD1.i.addOutpoint(SEB.outpoint)
        SD1.o.addInpoint((SEB.inpoint))
        foldDart(SD1, SEB.outpoint) #creates SD1.m, SD1.oc, SD1.ic; dart folds up toward sleeve cap
        #extend sleeve wrist back
        SWB = C.addPoint('SWB', polar(SWB3, CD.oversleeve_length/20.0, angleOfLine(SWB3.outpoint, SWB3))) #sleeve extended at back wrist to allow for elbow dart
        #control points b/w SWF front wrist & SWB back wrist
        SWF.addOutpoint(polar(SWF, distance(SWF, SWB)/3.0, angleOfLine(SWF.inpoint, SWF) - ANGLE90)) #handle is perpendicular to sleeve seam
        SWB.addInpoint(polar(SWB, distance(SWF, SWB)/3.0, angleOfLine(SWB3, SWB) + ANGLE90)) #handle is perpendicular to sleeve seam

        #Bodice Front A
        pnt1 = dPnt((FNC.x + abs(FNC.x - FSP.x)/2.0, FNC.y + abs(FUC.y - FNC.y)/2.0))
        A.setLabelPosition(pnt1)
        pnt2 = up(pnt1, 0.5*IN)
        A.setLetter(pnt2, scaleby = 10.0)
        AG1 = dPnt((FNC.x + abs(FNS.x - FNC.x)/2.0, abs(FUC.y - FNC.y)/2.0))
        AG2 = down(AG1, 0.75 * CD.back_waist_length)
        A.addGrainLine(AG1, AG2)
        A.addGridLine(['M', FWO, 'L', FSP, 'L', FSW, 'L', FSH, 'L', FWC, 'M', FAP2, 'L', FNS, 'L', FBP, 'M', FBC, 'L', FBP, 'L', FBS, 'M', FUC, 'L', FUS4, 'L', FUS,'M', FAP2,'L', FUS3])

        if full_bust == 'true':
            A.addDartLine(['M', FD1.oc, 'L', FD1, 'L', FD1.ic, 'M', FD2.oc, 'L', FD2, 'L', FD2.ic])
            pth = (['M', FNC, 'L', FWC, 'C', FD1.i, 'L', FD1.m, 'L', FD1.o, 'L', FD2.i, 'L', FD2.m, 'L', FD2.o, 'C', FWS, 'L', FUS, 'C', FAP, 'C', FSP, 'L', FNS, 'C', FNC])
            A.addSeamLine(pth)
            A.addCuttingLine(pth)
        else:
            A.addDartLine(['M', FD1.oc, 'L', FD1, 'L', FD1.ic])
            pth = (['M', FNC, 'L', FWC, 'C', FD1.i, 'L', FD1.m, 'L', FD1.o, 'C', FWS, 'L', FUS, 'C', FAP, 'C', FSP, 'L', FNS, 'C', FNC])
            A.addSeamLine(pth)
            A.addCuttingLine(pth)

        #Bodice Back B
        pnt1 = dPnt((BNC.x - abs(BNC.x - BSP.x)/2.0, BNC.y + abs(BUC.y - BNC.y)/2.0))
        B.setLabelPosition(pnt1)
        pnt2 = up(pnt1, 0.5*IN)
        B.setLetter(pnt2, scaleby = 10.0)
        BG1 = dPnt((BNC.x - abs(BNS.x - BNC.x)/2.0, abs(BUC.y - BNC.y)/3.0))
        BG2 = down(BG1, 0.75 * CD.back_waist_length)
        B.addGrainLine(BG1, BG2)
        B.addGridLine(['M', BSP, 'L', BSW, 'L', BSH, 'L', BUC, 'L', BUS3, 'L', BUS2, 'M', BNS, 'L', BAP2, 'M', BWO, 'L', BSP])
        B.addDartLine(['M', BD1.oc, 'L', BD1, 'L', BD1.ic, 'M', BD2.oc, 'L', BD2, 'L', BD2.ic])
        pth = (['M', BNC, 'L', BWC, 'C', BD1.i, 'L', BD1.m, 'L', BD1.o, 'C', BWS, 'L', BUS, 'C', BAP, 'C', BSP, 'L', BD2.o, 'L', BD2.m, 'L', BD2.i, 'L', BNS, 'C', BNC])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        #Sleeve C
        Cg1 = dPnt((SUM.x, SUM.y))
        Cg2 = dPnt((Cg1.x, SWM.y - 8*CM))
        C.addGrainLine(Cg1, Cg2)
        pnt1 = dPnt(midPoint(SUM, SEM))
        C.setLetter((SCB2.x, pnt1.y), scaleby=15.0)
        C.setLabelPosition((SCB2.x, pnt1.y + 2.0 * CM))
        C.addGridLine(['M', SCM,'L', SWM, 'M', SUF, 'L', CWF1, 'M', SUB, 'L', SWB1, 'M', SUB, 'L', SCM, 'L',  SUF, 'M', SUB, 'L', SWB2, 'M', SEB, 'L', SWB3, 'M', SUF, 'L', SWF2, 'M', SEF, 'L', SWF, 'M', SUB, 'L', SUF,  'M', SEB, 'L', SEF, 'M', SWB1, 'L', CWF1])
        C.addDartLine(['M', SD1.ic, 'L', SD1, 'L', SD1.oc])
        pth = (['M', SUB, 'C', SCB1, 'C', SCB2, 'C', SCB3, 'C', SCM, 'C', SCF3, 'C', SCF2, 'C', SCF1, 'C', SUF, 'C', SEF, 'C', SWF, 'C', SWB, 'L', SWB3, 'C', SD1.o, 'L', SD1.m, 'L', SD1.i, 'C', SUB])
        C.addSeamLine(pth)
        C.addCuttingLine(pth)

        #call draw() to generate svg file
        self.draw()

        return

