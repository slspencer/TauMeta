# !/usr/bin/python
#
# spencer_bodice_short.py
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
        self.setInfo('patternTitle', 'Spencer Bodice Short')
        self.setInfo('companyName', 'Next Patterns')
        self.setInfo('designerName', 'S.L.Spencer')
        self.setInfo('patternmakerName', 'S.L.Spencer')
        self.setInfo('description', """Women's bodice block pattern with minimum ease, includes long sleeve with elbow dart.""")
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

        #create pattern pieces,  assign an id lettercd 
        A = bodice.addPiece('Bodice Front', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = bodice.addPiece('Bodice Back', 'B', fabric = 2, interfacing = 0, lining = 0)
        C = bodice.addPiece('Bodice Sleeve', 'C', fabric = 2, interfacing = 0, lining = 0)

        #pattern points
        # x, y coordinates are always passed as a two-item list like this: (23.6, 67.0)
        # points are always in the 'reference' group, and always have style='point_style'

        #---Front A---#
        #f_bust_ease = 0.083 * CD.bust/4.0 #3" for 36" bust
        #f_bust_ease = 0.07 * CD.bust/4.0 #2.5" for 36" bust
        f_bust_ease = 0.035 * CD.bust/4.0 #1.25" for 36" bust
        b_bust_ease = f_bust_ease
        #f_waist_ease = 0.0625 * CD.waist/4.0 #1.5" for 24" waist
        f_waist_ease = 0.03125 * CD.waist/4.0 #.75" for 24" waist
        b_waist_ease = f_waist_ease
        
        f_underarm_height = 9.0 * CM
        f_bust_height = 18 * CM
        b_underarm_height = 18.0 * CM
            
        FNC = A.addPoint('FNC', (0.0, 0.0)) #front neck center
        FWC = A.addPoint('FWC', down(FNC, CD.front_waist_length)) #front waist center
        FSH = A.addPoint('FSH', up(FWC, CD.front_shoulder_height)) #front shoulder height
        FSW = A.addPoint('FSW', right(FSH, 0.5 * CD.front_shoulder_width)) #front shoulder width
        FSP = A.addPoint('FSP', highestP(onCircleAtX(FWC, CD.front_shoulder_balance, FSW.x))) #front shoulder point
        FNS = A.addPoint('FNS', leftmostP(onCircleAtY(FSP, CD.shoulder, FSH.y))) #front neck side
        FUC = A.addPoint('FUC', down(FNC, f_underarm_height)) #front underarm center
        FBC = A.addPoint('FBC', down(FNC, f_bust_height)) #bust center
        FBP = A.addPoint('FBP', right(FBC, 0.5 * CD.bust_distance)) #bust point
        #FAS = A.addPoint('FAS', right(FUC, CD.across_chest / 2.0 + f_bust_ease / 2.0 )) #temp front armscye point
        #FAS = A.addPoint('FAS', right(FUC, CD.across_chest / 2.0)) #temp front armscye point
        f10 = A.addPoint('f10', right(FUC, CD.across_chest / 2.0)) #temp front armscye point
        FAC = A.addPoint('FAC', midPoint(FNC, FUC))  
        FAS = A.addPoint('FAS', right(FAC, 0.95 * CD.across_chest / 2.0)) #front armscye point 
        f1 = A.addPoint('f1', right(FUC, CD.front_underarm / 2.0)) #temp front underarm side               
        f2 = A.addPoint('f2', rightmostP(onCircleTangentFromOutsidePoint(FBP, (CD.front_bust - CD.bust_distance) / 2.0, f1))) #temp front bust side
        f3 = A.addPoint('f3', onLineAtLength(f1, f2, CD.side)) #temp front waist side
        f4 = A.addPoint('f4', (FBP.x, FWC.y)) #temp dart inside leg
        f5 = A.addPoint('f5', lowestP(intersectCircles(FBP, distance(FBP, f4), f3, CD.front_waist/2.0 - distance(FWC, f4)))) #temp dart outside leg
        
        f6 = A.addPoint('f6', polar(f3, f_waist_ease, angleOfLine(FBP, f2))) #temp front waist side, incl. ease
        f7 = A.addPoint('f7', polar(f1, f_bust_ease, angleOfLine(FBP, f2))) #temp front underarm side, incl. ease                                              
        FBS = A.addPoint('FBS', intersectLines(f7, f6, FBP, f2)) #front bust side, incl. ease 
        FUS = A.addPoint('FUS', onLineAtLength(f7, FBS, 0.15 * CD.side)) #front underarm side        
        #rotate waist point
        total_dart_angle = angleOfVector(f5, FBP, f4)        
        FWS = A.addPoint('FWS', rotate(FBP, f6, total_dart_angle / 2.0)) #front waist side
        #create bust side dart
        FD2 = A.addPoint('FD2', FBP) #set to be FBP temporarily
        FD2.i = A.addPoint('FD2.i', onLineAtY(f6, f7, FBP.y)) #bust side dart inside leg - fold up toward FUS
        FD2.o = A.addPoint('FD2.o', rotate(FBP, FD2.i, total_dart_angle / 2.0)) #bust side dart outside leg
        updatePoint(FD2, polar(FBP, 0.12 * distance(FBP, FD2.o), angleOfVector(FD2.o, FBP, FD2.i) / 2.0)) #move FD2
        #reduce & rotate bust waist point
        f8 = A.addPoint('f8', intersectLineRay(FWC, f4, FBP, ANGLE90 + total_dart_angle / 4.0))
        f9 = A.addPoint('f9', intersectLineRay(FWC, f4, FBP, ANGLE90 - total_dart_angle / 4.0))
        FD1 = A.addPoint('FD1', down(FBP, 0.12 * abs(FBP.y - FWC.y))) #front dart point        
        FD1.i = A.addPoint('FD1.i', f8) #bust waist dart inside leg - fold in toward FWC
        FD1.o = A.addPoint('FD1.o', f9) #bust waist dart outside leg
        #extend leg lengths to smooth seamline at dart, then extend middle length so foldline meets seamline
        extendDart(FWC, FD1, FWS)
        foldDart(FD1, FWC) #creates FD1.m for seamline, FD1.ic & FD1.oc for dartline
        extendDart(FUS, FD2, FWS)
        foldDart(FD2, FUS) #creates FD2.m for seamline, FD2.ic & FD2.oc for dartline    
       
        #front control points
        #b/w FNS & FNC
        FNS.addOutpoint(polar(FNS, 0.5 * abs(FNC.y - FNS.y), angleOfLine(FNS, FSP) + ANGLE90))        
        FNC.addInpoint(right(FNC, 0.6 * abs(FNC.x - FNS.x)))
        #b/w FWC & FD1.i
        FWC.addOutpoint(right(FWC, 0.33 * distance(FWC, FD1.i)))
        FD1.i.addInpoint(intersectLineRay(FWC, f8, FD1.i, angleOfLine(FD1, FD1.i) + ANGLE90))
        #b/w FD1.o & FWS
        FD1.o.addOutpoint(intersectLineRay(FWS, f9, FD1.o, angleOfLine(FD1.o, FD1) + ANGLE90))
        FWS.addInpoint(polar(FWS, 0.33 * distance(FD1.o, FWS), angleOfLine(FUS, FWS) + ANGLE90))        
        #b/w FUS & FAS
        FUS.addOutpoint(polar(FUS, 0.4 * distance(FUS, FAS), angleOfLine(FBS, FBP)))
        FAS.addInpoint(down(FAS, 0.5 * distance(FUS, FAS)))
        #b/w FAS & FSP
        FAS.addOutpoint(up(FAS, 0.33 * distance(FAS, FSP)))
        FSP.addInpoint(polar(FSP, 0.15 * distance(FAS, FSP), angleOfLine(FSP, FNS) - ANGLE90))
                          
        #---Back B---#
        BNC = B.addPoint('BNC', (0.0, 0.0)) #back neck center
        BWC = B.addPoint('BWC', down(BNC, CD.back_waist_length)) #back waist center
        BSH = B.addPoint('BSH', up(BWC, CD.back_shoulder_height)) #back shoulder height
        BSW = B.addPoint('BSW', left(BSH, 0.5 * CD.back_shoulder_width)) #back shoulder width
        BSP = B.addPoint('BSP', highestP(onCircleAtX(BWC, CD.back_shoulder_balance, BSW.x))) #back shoulder point
        BNS = B.addPoint('BNS', rightmostP(onCircleAtY(BSP, CD.shoulder, BSH.y))) #back neck side
        BUC = B.addPoint('BUC', down(BNC, b_underarm_height)) #back underarm center 
        b7 = B.addPoint('b7', left(BUC, CD.across_back / 2.0 + b_bust_ease / 2.0))
        BAC = B.addPoint('BAC', up(BUC, distance(BUC, BNC) / 3.0)) #back armscye center        
        BAS = B.addPoint('BAS', up(b7, distance(b7, BSP) / 3.0)) #back armscye point
        b1 = B.addPoint('b1', left(BUC, CD.back_underarm / 2.0)) #temp back underarm side               
        #back waist dart        
        BD1 = B.addPoint('BD1', onLineAtY(BWC, BSP, BUC.y)) #back waist dart point
        b2 = B.addPoint('b2', (BD1.x, BWC.y)) #temp dart midPoint at waist
        b3 = B.addPoint('b3', right(b2, 0.2 * abs(BD1.x - BWC.x))) #temp back waist dart inside leg
        b4 = B.addPoint('b4', left(b2, 0.2 * abs(BD1.x - BWC.x))) #temp back waist dart inside leg
        BD1.i = B.addPoint('BD1.i', b3) #back waist dart inside leg
        BD1.o = B.addPoint('BD1.o', b4) #back waist dart outside leg
        #back waist side & bust side
        b5 = B.addPoint('b5', lowestP(intersectCircles(b1, CD.side, BD1.o, CD.back_waist / 2.0 - distance(BWC, BD1.i)))) #temp back waist side
        b6 = B.addPoint('b6', left(b1, b_bust_ease)) #temp back underarm side
        BWS = B.addPoint('BWS', left(b5, b_waist_ease)) #temp back waist side
        BUS = B.addPoint('BUS', onLineAtLength(b6, BWS, 0.15 * CD.side))
        #smooth dart at waist
        extendDart(BWC, BD1, BWS)
        foldDart(BD1, BWC)
        
        #back shoulder dart
        dart_width = distance(BSP, BNS) - distance(FSP, FNS)
        print("shoulder ease =",dart_width)
        pnt_m = midPoint(BSP, BNS) #midPoint of shoulder dart at shoulder seam
        BD2 = B.addPoint('BD2', intersectLineRay(BNS, BAS, pnt_m, angleOfLine(BSP, BNS) + ANGLE90)) #back shoulder dart point        
        BD2.i = B.addPoint('BD2.i', pnt_m) #back shoulder dart inside leg
        BD2.o = B.addPoint('BD2.o', rotate(BD2, pnt_m, angleOfDegree(-9))) #back shoulder dart outside leg
        updatePoint(BSP, rotate(BD2, BSP, angleOfDegree(-9)))
        extendDart(BSP, BD2, BNS, extension=1) #smooth shoulder seam at dart
        print("dart_width=",distance(BD2.i, BD2.o))
        print("front shoulder length =",distance(FNS, FSP))
        print("back shoulder width =", distance(BNS, BD2.i) + distance(BD2.o, BSP))
        foldDart(BD2, BNS) #fold dart toward BNS
        
        #back control points
        #b/w BNS & BNC
        BNC.addInpoint(left(BNC, 0.75 * abs(BNC.x - BNS.x)))
        BNS.addOutpoint(polar(BNS, 0.5 * abs(BNC.y - BNS.y), angleOfLine(BNS, BNC.inpoint)))
        #b/w BWC & BD1.i
        BWC.addOutpoint(left(BWC, 0.33 * distance(BWC, BD1.i)))
        BD1.i.addInpoint(intersectLineRay(BWC, b3, BD1.i, angleOfLine(BD1.i, BD1) + ANGLE90))
        #b/w BD1.o & BWS
        BD1.o.addOutpoint(intersectLineRay(BWS, b4, BD1.o, angleOfLine(BD1, BD1.o) + ANGLE90))
        BWS.addInpoint(polar(BWS, 0.33 * distance(BD1.o, BWS), angleOfLine(BWS, b4)))                 
        #b/w BUS & BAS
        BUS.addOutpoint(polar(BUS, 0.33 * abs(BUS.x - BAS.x), angleOfLine(BWS, BUS) + ANGLE90))
        #BAS.addInpoint(polar(BAS, 0.5 * abs(BUS.y - BAS.y), angleOfLine(BNS, BAS)))
        #BAS.addInpoint(intersectLineRay(BUS, BUS.outpoint, BAS, angleOfLine(BNS, BAS)))
        BAS.addInpoint(b7)
        #b/w BAS & BSP
        BAS.addOutpoint(up(BAS, 0.33 * distance(BAS, BSP)))
        BSP.addInpoint(polar(BSP, 0.15 * distance(BAS, BSP), angleOfLine(BSP, BNS) + ANGLE90))
        
        #---Sleeve C---#
        #get front & back armcye length
        bl_armscye_length = curveLength(points2List(BUS, BUS.outpoint, BAS.inpoint, BAS)) #back lower armscye length
        print 'bl_armscye_length', bl_armscye_length
        bu_armscye_length = curveLength(points2List(BAS, BAS.outpoint, BSP.inpoint, BSP)) #back upper armscye length
        b_armscye_length = bl_armscye_length + bu_armscye_length #back armscye length        
        fl_armscye_length = curveLength(points2List(FUS, FUS.outpoint, FAS.inpoint, FAS)) #front lower armscye length
        print 'fl_armscye_length', fl_armscye_length
        fu_armscye_length = curveLength(points2List(FAS, FAS.outpoint, FSP.inpoint, FSP)) #front upper armscye length
        f_armscye_length = fl_armscye_length + fu_armscye_length # front armscye length                        
        armscye_length = f_armscye_length + b_armscye_length #total armscye length
        print('armscye_length / 3.0 =', armscye_length / 3.0)
        print('oversleeve_length - undersleeve_length =', CD.oversleeve_length - CD.undersleeve_length)        
  
        #based on Hillhouse & Mansfield
        SCM = C.addPoint('SCM', (0,0)) #sleeve cap middle - top of sleeve
        SWM = C.addPoint('SWM', down(SCM, CD.oversleeve_length)) #sleeve wrist middle                
        SUM = C.addPoint('SUM', up(SWM, CD.undersleeve_length)) #temp sleeve underarm middle
        SUM1 = C.addPoint('SUM1', down(SUM, 0.75*IN)) #sleeve underarm midPoint 
        SEM1 = C.addPoint('SEM1', midPoint(SUM, SWM)) #temp sleeve elbow middle
        SEM = C.addPoint('SEM', up(SEM1, 1*IN)) #sleeve elbow middle
        SEF1 = C.addPoint('SEF1', right(SEM, (CD.elbow) / 4.0)) #sleeve elbow front        
        SEB1 = C.addPoint('SEB1', left(SEM, (CD.elbow) / 4.0)) #sleeve elbow back
        SUF1 = C.addPoint('SUF1', right(SUM1, (CD.bicep + 2.0*IN) / 4.0)) #front underarm point
        SUB1 = C.addPoint('SUB1', left(SUM1, (CD.bicep + 2.0*IN) / 4.0)) #front underarm point        
        SCF = C.addPoint('SCF', onLineAtY(SUF1, SEF1, SCM.y))
        SCB = C.addPoint('SCB', onLineAtY(SUB1, SEB1, SCM.y))
        SWF1 = C.addPoint('SWF1', onLineAtY(SUF1, SEF1, SWM.y))
        SWB1 = C.addPoint('SWB1', onLineAtY(SUB1, SEB1, SWM.y))
        s1 = C.addPoint('s1', midPoint(SUF1, SCF))
        s2 = C.addPoint('s2', onLineAtLength(s1, SCF, 0.75*IN))
        s3 = C.addPoint('s3', midPoint(SUB1, SCB)) 
        s4 = C.addPoint('s4', onLineAtLength(s3, SCB, 0.75*IN))
        s5 = C.addPoint('s5', midPoint(SCM, SCF))
        s6 = C.addPoint('s6', midPoint(SCM, SCB))
        s7 = C.addPoint('s7', midPoint(SUM1, SUF1))
        s8 = C.addPoint('s8', left(SUM1, 1*IN)) 
        s9 = C.addPoint('s9', midPoint(s2, s5))
        s10 = C.addPoint('s10', onLineAtLength(s4, s6, (distance(s4, s6) / 2.0) - (1/8.0)*IN)) 
        s11 = C.addPoint('s11', midPoint(s2, s7))
        s12 = C.addPoint('s12', midPoint(s4, s8))
        SUF = C.addPoint('SUF', reflect(s2, angleOfLine(s2, s1), SUM))        
        SUB = C.addPoint('SUB', reflect(s4, angleOfLine(s4, s3), SUM))
        SUF2 = C.addPoint('SUF2', reflect(s2, angleOfLine(s2, s1), SUM1))        
        SUB2 = C.addPoint('SUB2', reflect(s4, angleOfLine(s4, s3), SUM1))
        SEF = C.addPoint('SEF', reflect(s2, angleOfLine(s2, s1), SEM))        
        SEB = C.addPoint('SEB', reflect(s4, angleOfLine(s4, s3), SEM))
        SWF2 = C.addPoint('SWF2', reflect(s2, angleOfLine(s2, s1), SWM))        
        SWB2 = C.addPoint('SWB2', reflect(s4, angleOfLine(s4, s3), SWM))
        
        wrist_diff = distance(SWF2, SWF1) + distance(SWF1, SWM) + distance(SWM, SWB1) + distance(SWB1, SWB2) - (CD.wrist + 1.0*IN)
        SWF = C.addPoint('SWF', onLineAtLength(SWF2, SWF1, wrist_diff / 2.0))
        SWB = C.addPoint('SWB', onLineAtLength(SWB2, SWB1, wrist_diff / 2.0))
        
        #slash and spread lower half of sleeve
        rotation_angle = angleOfChord(-1.5*IN, distance(SEF, SEB))
        s13 = C.addPoint('s13', rotate(SEF, SEF1, rotation_angle)) 
        s14 = C.addPoint('s14', rotate(SEF, SEM, rotation_angle))
        s15 = C.addPoint('s15', rotate(SEF, SEB1, rotation_angle))
        s16 = C.addPoint('s16', rotate(SEF, SEB, rotation_angle))
        s17 = C.addPoint('s17', rotate(SEF, SWF, rotation_angle))
        s18 = C.addPoint('s18', rotate(SEF, SWF1, rotation_angle))
        s19 = C.addPoint('s19', rotate(SEF, SWM, rotation_angle))
        s20 = C.addPoint('s20', rotate(SEF, SWB1, rotation_angle))
        s21 = C.addPoint('s21', rotate(SEF, SWB, rotation_angle)) 
        
        #elbow dart
        SD1 = C.addPoint('SD1', midPoint(SEB1, s15))
        SD1.i = C.addPoint('SD1.i', SEB)
        SD1.o = C.addPoint('SD1.o', s16)
        foldDart(SD1, SUB) 
        
        #control points
        #front sleeve cap
        SCM.addOutpoint(midPoint(SCM, s5))
        pnt1 = midPoint(SCM.outpoint, s5)
        pnt2 = midPoint(pnt1, s5)
        s9.addInpoint(polar(s9, distance(s9, SCM)  / 2.0, angleOfLine(s9, pnt2)))
        s9.addOutpoint(polar(s9, distance(s9, s2) / 3.0, angleOfLine(s9.inpoint, s9)))
        SUF.addInpoint(polar(SUF, distance(SUF2, SUF1) / 2.0, angleOfLine(SUF2, SUF1)))
        angle1 = angleOfLine(s9, s9.inpoint)
        angle2 = angleOfLine(SUF.inpoint, s2)
        angle3 = (angle1 + angle2) / 2.0
        s2.addInpoint(polar(s2, distance(s9, s2) / 3.0, angle3))
        s2.addOutpoint(polar(s2, distance(s2, SUF) / 3.0, angle3 + ANGLE180))        
        #back sleeve cap      
        SUB.addOutpoint(polar(SUB, distance(SUB, s4) / 3.0, angleOfLine(SUB2, SUB1)))
        s4.addInpoint(polar(s4, distance(SUB, s4) / 3.0, angleOfLine(s6, s4)))
        s4.addOutpoint(midPoint(s10, s6))
        SCM.addInpoint(midPoint(s6, SCM))

        ##adjust front upper sleeve cap      
        #fu_sleevecap_length = curveLength(points2List(SCM, SCM.outpoint, s9.inpoint, s9, s9.outpoint, s2.inpoint, s2))
        #fu_diff = fu_sleevecap_length - fu_armscye_length                    
        #while (abs(fu_diff) > 2):
        #    # armscye length cannot be greater than sleevecap length ( < 0)
        #    # sleevecap length can be from 0 to 2 pixels longer than armscye length ( > 2)      
        #    print("fu_diff=", fu_diff)
        #    angle = angleOfLine(s2, s2.inpoint)
        #    print 's2', s2.x, s2.y       
        #    updatePoint(s2, polar(s2, fu_diff, angle))
        #    print 's2 new', s2.x, s2.y
        #    print 'SUF', SUF.x, SUF.y
        #    length = distance(s2, SUF)
        #    print 'distance(s2, SUF)', length
        #    updatePoint(s2.outpoint, polar(s2, distance(s2, SUF) / 3.0, angle))            
        #    fu_sleevecap_length = curveLength(points2List(SCM, SCM.outpoint, s9.inpoint, s9, s9.outpoint, s2.inpoint, s2))            
        #    fu_diff = fu_armscye_length - fu_sleevecap_length            
        #print("fu_diff final=", fu_diff)

        #adjust front upper sleeve cap           
        fu_sleevecap_length = curveLength(points2List(SCM, SCM.outpoint, s9.inpoint, s9, s9.outpoint, s2.inpoint, s2))
        fu_diff = fu_sleevecap_length - fu_armscye_length                    
        while (abs(fu_diff) > 2.0):
            print 'fu_diff=', fu_diff
            print '  s2', s2.x, s2.y
            pnt = onLineAtLength(s2, s2.inpoint, fu_diff) #move s2 towards s2.inpoint if sleevecap is too big              
            updatePoint(s2, pnt)
            print '  s2 new', s2.x, s2.y
            fu_sleevecap_length = curveLength(points2List(SCM, SCM.outpoint, s9.inpoint, s9, s9.outpoint, s2.inpoint, s2))
            fu_diff = fu_sleevecap_length - fu_armscye_length                    
            print '  fu_sleevecap_length new', fu_sleevecap_length               
        print("fu_diff final=", fu_diff)

        #adjust front lower sleeve cap           
        fl_sleevecap_length = curveLength(points2List(s2, s2.outpoint, SUF.inpoint, SUF))
        fl_diff = fl_sleevecap_length - fl_armscye_length                       
        while (abs(fl_diff) > 2.0):
            print 'fl_diff=', fl_diff
            print '  SUF', SUF.x, SUF.y
            pnt = onLineAtLength(SUF, SUF.inpoint, fl_diff) #move SUF towards SUF.inpoint if sleevecap is too big            
            updatePoint(SUF, pnt)
            print '  SUF new', SUF.x, SUF.y
            #print 'SUF.inpoint', SUF.inpoint.x, SUF.inpoint.y           
            #pnt = polar(SUF, distance(SUF, s2) / 3.0, angleOfLine(SUF, SUF.inpoint))
            #updatePoint(SUF.inpoint, pnt)
            #print 'SUF.inpointnew', SUF.inpoint.x, SUF.inpoint.y
            fl_sleevecap_length = curveLength(points2List(s2, s2.outpoint, SUF.inpoint, SUF))           
            fl_diff = fl_sleevecap_length - fl_armscye_length
            print '  fl_sleevecap_length new', fl_sleevecap_length               
        print("fl_diff final=", fl_diff)
        
        #adjust back upper sleeve cap           
        bu_sleevecap_length = curveLength(points2List(s4, s4.outpoint, SCM.inpoint, SCM))
        bu_diff = bu_sleevecap_length - bu_armscye_length                    
        while (abs(bu_diff) > 2.0):
            print 'bu_diff=', bu_diff
            print '  s4', s4.x, s4.y
            pnt = onLineAtLength(s4, s4.outpoint, bu_diff) #move s4 towards s4.outpoint if sleevecap is too big     
            updatePoint(s4, pnt)
            print '  s4 new', s4.x, s4.y
            bu_sleevecap_length = curveLength(points2List(s4, s4.outpoint, SCM.inpoint, SCM))
            bu_diff = bu_sleevecap_length - bu_armscye_length                    
            print '  bu_sleevecap_length new', bu_sleevecap_length               
        print("bu_diff final=", bu_diff)       
        
        #b_sleevecap_length = bu_sleevecap_length + bl_sleevecap_length
        #print 'b_diff', b_sleevecap_length - b_armscye_length
                          
        #Sleeve C
        Cg1 = dPnt((s8.x, s8.y))
        Cg2 = dPnt((Cg1.x, SWM.y - 8.0 * CM))
        C.addGrainLine(Cg1, Cg2)
        pnt1 = dPnt(midPoint(SUM1, SEM))
        C.setLetter((SCM.x, pnt1.y), scaleby=15.0)
        C.setLabelPosition((SCM.x, pnt1.y + 2.0 * CM))
        C.addGridLine(['M', SEB1, 'L', SCB, 'L', SCF, 'L', SEF1,
                       'M', SCM, 'L', SEM,        
                       'M', s7, 'L', s2, 'L', s5, 
                       'M', s8, 'L', s4, 'L', s6,
                       'M', s4, 'L', SUM, 'L', s2,                               
                       'M', SUB2, 'L', SUB1, 'L', SUF1, 'L', SUF2,
                       'M', SEB, 'L', SEB1, 'L', SEF1, 'L', SEF,                       
                       'M', s16, 'L', s15, 'L', s14, 'L', s13, 'L', SEF,
                       'M', SWB2, 'L', SWB1, 'L', SWM, 'L', SWF1, 'L', SWF2,
                       'M', SUF, 'L', SEF, 'L', SWF,
                       'M', SUB, 'L', SEB, 'L', SWB,                       
                       'M', s4, 'L', SEB1,
                       'M', s15, 'L', s20,
                       'M', s14, 'L', s19,
                       'M', s2, 'L', SEF1,
                       'M', s13, 'L', s18])
        C.addDartLine(['M', SD1.oc, 'L', SD1, 'L', SD1.ic])     
        pth = (['M', SCM, 'C', s9, 'C', s2, 'C', SUF, 'L', SEF, 'L', s17, 'L', s18, 'L', s19, 'L', s20, 'L', s21, 'L', SD1.o, 'L', SD1.m, 'L', SD1.i, 'L', SUB, 'C', s4, 'C', SCM])
        C.addSeamLine(pth)
        C.addCuttingLine(pth)         

        #Bodice Front A
        pnt1 = dPnt((FNC.x + abs(FNC.x - FSP.x)/2.0, FNC.y + abs(FUC.y - FNC.y)/2.0))
        A.setLabelPosition(pnt1)
        pnt2 = up(pnt1, 0.5*IN)
        A.setLetter(pnt2, scaleby = 10.0)
        AG1 = dPnt((FNC.x + abs(FNS.x - FNC.x)/2.0, abs(FUC.y - FNC.y)/2.0))
        AG2 = down(AG1, 0.75 * CD.front_waist_length)
        A.addGrainLine(AG1, AG2)
        A.addGridLine(['M', FWC, 'L', FSP, 'L', FSW, 'L', FSH, 'L', FNC, 
                       'M', FBC, 'L', FBP, 'L', FBS, 
                       'M', FUC, 'L', f1, 'L', f7, 'L', f6, 'L', f3, 'L', f1, 
                       'M', FWC, 'L', f4, 'L', FBP, 'L', f5, 'L', f3, 
                       'M', FBP, 'L', FD2, 
                       'M', FAC, 'L', FAS])
        A.addDartLine(['M', FD1.ic, 'L', FD1, 'L', FD1.oc, 
                       'M', FD2.ic, 'L', FD2, 'L', FD2.oc])
        pth = (['M', FNC, 'L', FWC, 'C', FD1.i, 'L', FD1.m, 'L', FD1.o, 'C', FWS, 'L', FD2.o, 'L', FD2.m, 'L', FD2.i, 'L', FUS, 'C', FAS, 'C', FSP, 'L', FNS, 'C', FNC])
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
        B.addGridLine(['M', BWC, 'L', BSP, 'L', BSW, 'L', BSH, 'L', BUC, 'L', b6, 'L', BUS, 
                       'M', b1, 'L', b5, 'L', BWS, 
                       'M', BAC, 'L', BAS])
        B.addDartLine(['M', BD1.oc, 'L', BD1, 'L', BD1.ic, 
                       'M', BD2.oc, 'L', BD2, 'L', BD2.ic])
        pth = (['M', BNC, 'L', BWC, 'C', BD1.i, 'L', BD1.m, 'L', BD1.o, 'C', BWS, 'L', BUS, 'C', BAS, 'C', BSP, 'L', BD2.o, 'L', BD2.m, 'L', BD2.i, 'L', BNS, 'C', BNC])
        B.addSeamLine(pth)
        B.addCuttingLine(pth) 
        
              

        #call draw() to generate svg file
        self.draw()

        return

