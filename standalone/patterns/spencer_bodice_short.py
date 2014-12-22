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
        #FAP = A.addPoint('FAP', right(FUC, CD.across_chest / 2.0 + f_bust_ease / 2.0 )) #temp front armscye point
        #FAP = A.addPoint('FAP', right(FUC, CD.across_chest / 2.0)) #temp front armscye point
        f10 = A.addPoint('f10', right(FUC, CD.across_chest / 2.0)) #temp front armscye point
        FAC = A.addPoint('FAC', midPoint(FNC, FUC))  
        FAP = A.addPoint('FAP', right(FAC, 0.95 * CD.across_chest / 2.0)) #front armscye point 
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
        #b/w FUS & FAP
        FUS.addOutpoint(polar(FUS, 0.4 * distance(FUS, FAP), angleOfLine(FBS, FBP)))
        FAP.addInpoint(down(FAP, 0.5 * distance(FUS, FAP)))
        #b/w FAP & FSP
        FAP.addOutpoint(up(FAP, 0.33 * distance(FAP, FSP)))
        FSP.addInpoint(polar(FSP, 0.15 * distance(FAP, FSP), angleOfLine(FSP, FNS) - ANGLE90))
                          
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
        BAP = B.addPoint('BAP', up(b7, distance(b7, BSP) / 3.0)) #back armscye point
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
        BD2 = B.addPoint('BD2', intersectLineRay(BNS, BAP, pnt_m, angleOfLine(BSP, BNS) + ANGLE90)) #back shoulder dart point        
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
        #b/w BUS & BAP
        BUS.addOutpoint(polar(BUS, 0.33 * abs(BUS.x - BAP.x), angleOfLine(BWS, BUS) + ANGLE90))
        #BAP.addInpoint(polar(BAP, 0.5 * abs(BUS.y - BAP.y), angleOfLine(BNS, BAP)))
        #BAP.addInpoint(intersectLineRay(BUS, BUS.outpoint, BAP, angleOfLine(BNS, BAP)))
        BAP.addInpoint(b7)
        #b/w BAP & BSP
        BAP.addOutpoint(up(BAP, 0.33 * distance(BAP, BSP)))
        BSP.addInpoint(polar(BSP, 0.15 * distance(BAP, BSP), angleOfLine(BSP, BNS) + ANGLE90))
        
        #---Sleeve C---#
        #get front & back armcye length
        bl_armscye_length = curveLength(points2List(BUS, BUS.outpoint, BAP.inpoint, BAP))
        upper_back_curve_length = curveLength(points2List(BAP, BAP.outpoint, BSP.inpoint, BSP))
        back_curve_length = bl_armscye_length + upper_back_curve_length        
        fl_armscye_length = curveLength(points2List(FUS, FUS.outpoint, FAP.inpoint, FAP))
        upper_front_curve_length = curveLength(points2List(FAP, FAP.outpoint, FSP.inpoint, FSP))
        front_curve_length = fl_armscye_length + upper_front_curve_length                           
        bodice_armscye_length = front_curve_length + back_curve_length
        print('bodice_armscye_length / 3.0 =', bodice_armscye_length / 3.0)
        print('oversleeve_length - undersleeve_length =', CD.oversleeve_length - CD.undersleeve_length)        
        
        SUM = C.addPoint('SUM', (0, 0)) #sleeve underarm midPoint 
        SUB = C.addPoint('SUB', right(SUM, 0.55 * CD.bicep)) #back underarm point plus 5% eash
        SUF = C.addPoint('SUF', left(SUM, 0.55 * CD.bicep)) #front underarm point plus 5% ease
      
        SWM = C.addPoint('SWM', down(SUM, CD.undersleeve_length)) #sleeve wrist midPoint         
        SCM = C.addPoint('SCM', up(SUM, 1.20 * (CD.oversleeve_length - CD.undersleeve_length))) #sleeve cap middle - top of sleeve with some extra heightease        
        SCM1 = C.addPoint('SCM1',  up(SUM, CD.oversleeve_length - CD.undersleeve_length)) #sleeve cap middle with no height ease  
        SCF = C.addPoint('SCF', left(SCM1, 1.05 * CD.bicep/2.0)) #front cap width front 
        SCF1 = C.addPoint('SCF1', midPoint(SCM1, SCF)) #sleeve cap midPoint front
        SCB = C.addPoint('SCB', right(SCM1, 1.05 * CD.bicep/2.0)) #front cap width back
        SCB1 = C.addPoint('SCB1', midPoint(SCM1, SCB))  #sleeve cap midPoint back        
        s1 = C.addPoint('s1', highestP(intersectCircles(SUB, distance(BUS, BAP), SCM1, distance(BSP, BAP)))) #back sleeve cap point            
        s2 = C.addPoint('s2', highestP(intersectCircles(SUF, distance(FUS, FAP), SCM1, distance(FSP, FAP)))) #front sleeve cap point 

        SEM = C.addPoint('SEM', down(SUM, 0.53 * distance(SUM, SWM))) #sleeve elbow midPoint, 3% lower than sleeve midlength
        SEB = C.addPoint('SEB', right(SEM, 0.55 * CD.elbow)) #sleeve elbow back plus 5% ease
        #SEF = C.addPoint('SEF', left(SEM, 0.5 * CD.elbow)) #sleeve elbow front
                                     
                                                               
        #SCM = C.addPoint('SCM', (0.0, 0.0)) #sleeve cap middle - top of sleeve
        #SWM = C.addPoint('SWM', down(SCM, CD.oversleeve_length)) #sleeve wrist midPoint
        #SUM = C.addPoint('SUM', down(SCM, bodice_armscye_length / 4.0)) #sleeve underarm midPoint
        #SWM = C.addPoint('SWM', down(SCM, CD.oversleeve_length)) #sleeve wrist midPoint                                
        #SCF = C.addPoint('SCF', left(SCM, 1.05 * CD.bicep/2.0)) #front cap width front
        #SCF1 = C.addPoint('SCF1', midPoint(SCM, SCF)) #sleeve cap midPoint front                
        #SCB = C.addPoint('SCB', right(SCM, 1.05 * CD.bicep/2.0)) #front cap width back
        #SCB1 = C.addPoint('SCB1', midPoint(SCM, SCF))  #sleeve cap midPoint back
        #SUB = C.addPoint('SUB', rightmostP(onCircleAtY(SCM, distance(BSP, BAP) + distance(BAP, BUS), SUM.y))) #back underarm point
        #SUF = C.addPoint('SUF', leftmostP(onCircleAtY(SCM, distance(FSP, FAP) + distance(FAP, FUS), SUM.y))) #front underarm point                
        #s1 = C.addPoint('s1', onLineAtLength(SCM, SUB, distance(BSP, BAP))) #back sleeve cap point
        #s2 = C.addPoint('s2', onLineAtLength(SUF, SCM, distance(FUS, FAP))) #front sleeve cap point        
        #SEM = C.addPoint('SEM', midPoint(SUM, SWM)) #sleeve elbow midPoint
      
        #wrist points
        s3 = C.addPoint('s3', right(SWM, CD.wrist / 2.0)) #back wrist reference point        
        s4 = C.addPoint('s4', right(SWM, distance(SWM, s3) / 3.0)) #back wrist middle reference point
        s5 = C.addPoint('s5', left(s3, 1.3 * CD.wrist)) #front wrist reference point plus 30% ease
        s6 = C.addPoint('s6', right(s5, distance(s5, SWM) / 3.0)) #front wrist middle reference point                       

        #elbow dart
        SD1 = C.addPoint('SD1',  left(SEB, 0.3 * distance(SEB, SEM))) #elbow dart point
        pnt = intersectLineRay(SUB, SEB, SD1, angleOfLine(SUB, SEB) - ANGLE90)
        SD1.i = C.addPoint('SD1.i', intersectLineRay(SUB, SEB, SD1, angleOfLine(SD1, pnt) - angleOfDegree(8))) #elbow dart inside leg
        SD1.o = C.addPoint('SD1.o', intersectLineRay(SUB, SEB, SD1, angleOfLine(SD1, pnt) + angleOfDegree(8))) #elbow dart outside leg 
        foldDart(SD1, SEB) #creates SD1.m, SD1.oc, SD1.ic; dart folds up towards elbow                   

        #Sleeve C control points
        SCM.addInpoint(right(SCM, 0.33 * distance(SUM, s1)))
        s1.addOutpoint(polar(s1, 0.33 * distance(s1, SCM.inpoint), angleOfLine(s1, SCM.inpoint)))
        s1.addInpoint(polar(s1, 0.33 * distance(SUB, s1), angleOfLine(SCM.inpoint, s1)))
        SCM.addOutpoint(left(SCM, 0.33 * distance(SUM, s2)))                              
        s2.addInpoint(polar(s2, 0.33 * distance(s2, SCM.outpoint), angleOfLine(s2, SCM.outpoint)))
        s2.addOutpoint(polar(s2, 0.33 * distance(s2, SUF), angleOfLine(SCM.outpoint, s2)))                        
                 
        #adjust back lower sleeve cap
        SUB.addOutpoint(left(SUB, distance(SUB, s1) / 3.0))                                   
        bl_sleevecap_length = curveLength(points2List(SUB, SUB.outpoint, s1.inpoint, s1))
        bl_diff = bl_armscye_length - bl_sleevecap_length
        while (abs(bl_diff) > 1.0):
            print("bl_diff=", bl_diff)                
            updatePoint(SUB, right(SUB, bl_diff)) #will move left if bl_diff < 0
            updatePoint(SUB.outpoint, left(SUB, distance(SUB, s1) / 3.0))
            updatePoint(s1.inpoint, polar(s1, distance(s1, SUB) / 3.0, angleOfLine(SCM.inpoint, s1)))
            bl_sleevecap_length = curveLength(points2List(SUB, SUB.outpoint, s1.inpoint, s1))        
            bl_diff = bl_armscye_length - bl_sleevecap_length        
        print("bl_diff final=", bl_diff)                                
                 
        #adjust front lower sleeve cap
        SUF.addInpoint(right(SUF, distance(SUF, s2) / 3.0))         
        fl_sleevecap_length = curveLength(points2List(s2, s2.outpoint, SUF.inpoint, SUF))
        fl_diff = fl_armscye_length - fl_sleevecap_length                        
        while (abs(fl_diff) > 1.0):
            print("fl_diff=", fl_diff)        
            updatePoint(SUF, left(SUF, fl_diff))
            updatePoint(SUF.inpoint, right(SUF, distance(SUF, s2) / 3.0))
            updatePoint(s2.outpoint, polar(s2, distance(SUF, s2) / 3.0, angleOfLine(SCM.outpoint, s2)))
            fl_sleevecap_length = curveLength(points2List(s2, s2.outpoint, SUF.inpoint, SUF))            
            fl_diff = fl_armscye_length - fl_sleevecap_length                 
        print("fl_diff final=", fl_diff)                      
 
        #front & back wrist
        SWB = C.addPoint('SWB', intersectLineRay(SD1.o, s3, s4, angleOfLine(SD1.o, s3) - ANGLE90)) #sleeve wrist back        
        SWF = C.addPoint('SWF', onLineAtLength(SUF, s5, distance(SUB, SD1.i) + distance(SD1.o, SWB))) #sleeve wrist front 
        #front elbow
        SEF = C.addPoint('SEF', onLineAtY(SUF, s5, SEM.y)) #sleeve elbow front                  

        #control points b/w SWF front wrist & SWB back wrist
        SWF.addOutpoint(polar(SWF, distance(SWF, SWB)/3.0, angleOfLine(SEF, SWF) - ANGLE90)) #handle is perpendicular to sleeve seam
        SWB.addInpoint(s4) #handle is perpendicular to sleeve seam    
        
        #Sleeve C
        Cg1 = dPnt((SUM.x, SUM.y))
        Cg2 = dPnt((Cg1.x, SWM.y - 8.0 * CM))
        C.addGrainLine(Cg1, Cg2)
        pnt1 = dPnt(midPoint(SUM, SEM))
        C.setLetter((s2.x, pnt1.y), scaleby=15.0)
        C.setLabelPosition((s2.x, pnt1.y + 2.0 * CM))
        C.addGridLine(['M', SUF, 'L', s2, 'L', SCM, 'L', s1, 'L', SUB, 'L', SCB, 'L', SCF, 'L', SUF, 'M', SCM, 'L', SWM, 'M', SUF, 'L', SUB, 'M', SEF, 'L', SEB, 'L', s3, 'L', s5, 'L', SUF])     
        C.addDartLine(['M', SD1.ic, 'L', SD1, 'L', SD1.oc])
        pth = (['M', SUB, 'C', s1, 'C', SCM, 'C', s2, 'C', SUF, 'L', SWF, 'C', SWB, 'L', SD1.o, 'L', SD1.m, 'L', SD1.i, 'L', SUB])
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
        A.addGridLine(['M', FWC, 'L', FSP, 'L', FSW, 'L', FSH, 'L', FNC, 'M', FBC, 'L', FBP, 'L', FBS, 'M', FUC, 'L', f1, 'L', f7, 'L', f6, 'L', f3, 'L', f1, 'M', FWC, 'L', f4, 'L', FBP, 'L', f5, 'L', f3, 'M', FBP, 'L', FD2])
        A.addDartLine(['M', FD1.ic, 'L', FD1, 'L', FD1.oc, 'M', FD2.ic, 'L', FD2, 'L', FD2.oc])
        pth = (['M', FNC, 'L', FWC, 'C', FD1.i, 'L', FD1.m, 'L', FD1.o, 'C', FWS, 'L', FD2.o, 'L', FD2.m, 'L', FD2.i, 'L', FUS, 'C', FAP, 'C', FSP, 'L', FNS, 'C', FNC])
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
        B.addGridLine(['M', BWC, 'L', BSP, 'L', BSW, 'L', BSH, 'L', BUC, 'L', b6, 'L', BUS, 'M', b1, 'L', b5, 'L', BWS])
        B.addDartLine(['M', BD1.oc, 'L', BD1, 'L', BD1.ic, 'M', BD2.oc, 'L', BD2, 'L', BD2.ic])
        pth = (['M', BNC, 'L', BWC, 'C', BD1.i, 'L', BD1.m, 'L', BD1.o, 'C', BWS, 'L', BUS, 'C', BAP, 'C', BSP, 'L', BD2.o, 'L', BD2.m, 'L', BD2.i, 'L', BNS, 'C', BNC])
        B.addSeamLine(pth)
        B.addCuttingLine(pth) 
        
              

        #call draw() to generate svg file
        self.draw()

        return

