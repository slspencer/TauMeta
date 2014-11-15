#!/usr/bin/env python
# patternName: Topper Coat - MRohr (p7)
# patternNumber: Coat_W_Topper_MRohr_p7

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
        self.setInfo('patternNumber', 'topper_coat')
        self.setInfo('patternTitle', 'Topper Coat')
        self.setInfo('companyName', 'Epic Mode')
        self.setInfo('designerName', 'S.L.Spencer')
        self.setInfo('patternmakerName', 'S.L.Spencer')
        self.setInfo('description', """Topper Coat""")
        self.setInfo('category', 'Coat')
        self.setInfo('type', 'pattern')
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
        #create pattern called 'coat'
        coat = self.addPattern('coat')
        #
        #create pattern pieces
        A = coat.addPiece('Front Lower', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = coat.addPiece('Back', 'B', fabric = 2, interfacing = 0, lining = 2)
        C = coat.addPiece('Sleeve Back', 'C', fabric = 2, interfacing = 0, lining = 2)
        D = coat.addPiece('Welt', 'D', fabric = 2, interfacing = 2, lining = 0)
        E = coat.addPiece('Pocket', 'E', fabric = 2, interfacing = 0, lining = 0)
        F = coat.addPiece('Front Facing', 'F', fabric = 4, interfacing = 0, lining = 0)
        G = coat.addPiece('Front Upper', 'G', fabric = 2, interfacing = 0, lining = 0)
        H = coat.addPiece('Sleeve Front', 'H', fabric = 2, interfacing = 0, lining = 2)
        I = coat.addPiece('Sleeve Cuff', 'I', fabric = 2, interfacing = 0, lining = 0)
        J = coat.addPiece('Front Lining', 'J', fabric = 0, interfacing = 0, lining = 2)

        #---Bodice Lower Front A---#
        FNC = A.addPoint('FNC', (0.0, 0.0)) #front neck center
        FWC = A.addPoint('FWC', down(FNC, CD.front_waist_length)) #front waist center
        FBC = A.addPoint('FBC', up(FWC, CD.bust_length)) #bust center
        FBP = A.addPoint('FBP', left(FBC, CD.bust_distance/2.0)) #bust point
        FSP = A.addPoint('FSP', highestP(onCircleAtX(FWC, CD.front_shoulder_balance, FNC.x - CD.front_shoulder_width/2.0))) #front shoulder tip
        FNS = A.addPoint('FNS', highestP(intersectCircles(FSP, CD.shoulder, FBP, CD.bust_balance))) #front neck point
        FAP = A.addPoint('FAP', lowestP(onCircleAtX(FNS, CD.front_underarm_balance, FNC.x - CD.across_chest/2.0))) #front underarm point
        FUC = A.addPoint('FUC', (FNC.x, FAP.y)) #front undearm center
        FUS1 = A.addPoint('FUS1', left(FUC, CD.front_underarm/2.0)) #front underarm side
        FBS = A.addPoint('FBS', leftmostP(onCircleTangentFromOutsidePoint(FBP, CD.front_bust/2.0 - distance(FBC, FBP), FUS1))) #line from FBP is perpendicular to line through FUS1
        FUS = A.addPoint('FUS', onLineAtLength(FUS1, FBS, 0.13 * CD.side)) #adjusted front underarm side on line FUS1-10
        FWS1 = A.addPoint('FWS1', left(FWC, CD.front_waist/2.0)) #temporary front waist side 1 - on waist line
        FWS2 = A.addPoint('FWS2', onLineAtLength(FUS1, FBS, CD.side)) #temporary front waist side 2 - on side seam
        FHC = A.addPoint('FHC', down(FWC, CD.front_hip_height)) #front hip center        
        FHS1 = A.addPoint('FHS1', left(FHC, CD.front_hip/2.0)) #front hip side 1        
        #front waist dart
        totalDartAngle = abs(angleOfVector(FWS1, FBP, FWS2))
        bustDartAngle = totalDartAngle/2.0
        #Bodice Lower Front A control points
        #b/w FNS front neck point & FNC front neck center
        FNS.addOutpoint(down(FNS, abs(FNC.y - FNS.y)/2.0))
        FNC.addInpoint(left(FNC, 0.75 * abs(FNC.x - FNS.x)))        
        #b/w FAP front underarm point & FSP front shoulder point
        FSP.addInpoint(polar(FSP, distance(FAP, FSP)/6.0, angleOfLine(FSP, FNS) + ANGLE90)) #short control handle perpendicular to shoulder seam
        FAP.addOutpoint(polar(FAP, distance(FAP, FSP)/3.0, angleOfLine(FAP, FNS))) #control handle points to front neck point
        #b/w FUS front underarm side & FAP front underarm point
        FAP.addInpoint(polar(FAP, distance(FUS, FAP)/3.0, angleOfLine(FNS, FAP)))
        FUS.addOutpoint(polar(FUS, distance(FUS, FAP)/3.0, angleOfLine(FWS2, FUS) + ANGLE90)) #control handle is perpendicular to side seam at underarm                
        
        #lower front coat points
        a1 = A.addPoint('a1', down(FNC, 0.03*CD.front_waist_length)) #new front neck center        
        a2 = A.addPoint('a2', onLineAtLength(FNS, FSP, distance(FNC, a1))) #new front neck point                            
        #control points
        #b/w a2 & a4 new         
        a2.addInpoint(polar(a2, distance(a2, a1)/3.0, angleOfLine(FSP, a2) + ANGLE90))
        a2.addOutpoint(polar(a2, distance(a2, a2.inpoint)/3.0, angleOfLine(a2.inpoint, a2)))
                
        #split neck curve
        front_neck_curve = points2List(FNS, FNS.outpoint, FNC.inpoint, FNC)
        curve_length = curveLength(front_neck_curve)
        a3 = A.addPoint('a3', onCurveAtLength(front_neck_curve, 2 * curve_length/3.0)) #divide front neck curve 2/3rd along length
        a4 = A.addPoint('a4', left(a3, distance(a3, FNC)/2.0)) #break point
        a5 = A.addPoint('a5', onLineAtLength(FBP, a3, distance(FBP, a4)/6.0))
        #control points
        a4.addInpoint(down(a4, distance(a4, a5) / 3.0))
        a4.addOutpoint(up(a4, distance(a4, a2) / 3.0))
        a5.addOutpoint(onLineAtLength(a5, a3, distance(a5, a4) / 3.0)) 

        #extend front center line        
        a6 = A.addPoint('a6', right(a1, 0.1 * CD.front_waist_length)) #right of a1 front neck center
        a7 = A.addPoint('a7', right(FHC, 0.1 * CD.front_waist_length)) #right of FHC front hip center                        
 
        #upper front coat points       
        g1 = A.addPoint('g1', a2) #new front neck point
        g2 = A.addPoint('g2', a4) #break point 
        g3 = A.addPoint('g3', a5) #front curve point
        LOWER_LENGTH = 0.2 * CD.side #20% side length        
        pnt = onLineAtLength(FUS, FWS2, 0.2 * CD.side)
        g4 = A.addPoint('g4', polar(pnt, 0.12 * CD.front_underarm, angleOfLine(FBP, FBS))) #new front underarm - out 7% front underarm, down 40% side length                        
        g5 = A.addPoint('g5', left(FAP, distance(FNS, a2))) #new armscye curve        
        g6 = A.addPoint('g6', left(FSP, distance(FNS, a2))) #new shoulder point
        
        #extend side seam
        a8 = A.addPoint('a8', left(FHS1, 0.6 * CD.front_hip/2.0)) #extend side
        #extend side seam hem
        a9 = A.addPoint('a9', extendLine(g4, a8, 1.5 * LOWER_LENGTH)) #extend side hem
        #extend front center line
        pnt = dPnt(intersectLines(a8, a9, FNC, FHC)) # find point where center line & side seam intersect
        a10 = A.addPoint('a10', onLineAtLength(pnt, FNC, distance(pnt, a9))) #new front hem center 
        
        #create pocket line
        WELT_HEIGHT = 0.15 * CD.front_waist_length
        a11 = A.addPoint('a11', onLineAtLength(a3, FBP, FWC.y + WELT_HEIGHT)) #pocket center
        a12 = A.addPoint('a12', extendLine(a9, a8, distance(a9, a8))) #pocket side
        #front facing/collar
        a13 = A.addPoint('a13', (a7.x, a10.y)) #extend center hem out for facing/collar
        
        #hem facing
        #b/w a10 hem center & a9 hem side
        a10.addOutpoint(left(a10, distance(a10, a9)/3.33))
        a9.addInpoint(polar(a9, distance(a10, a9)/3.33, angleOfLine(a8, a9) - ANGLE90))        
        hem_curve1 = points2List(a10, a10.outpoint, a9.inpoint, a9)
        a14 = A.addPoint('a14', onCurveAtX(hem_curve1, a4.x)) #facing hem
        new_curve = splitCurveAtPoint(hem_curve1, a14)
        (a10.outpoint.x, a10.outpoint.y) = new_curve[1]
        a14.addInpoint(new_curve[2])
        a14.addOutpoint(new_curve[4])
        (a9.inpoint.x, a9.inpoint.y) = new_curve[5]                       
                
        #control points      
        g1.addOutpoint(polar(g1, distance(g1, g2)/3.0, angleOfLine(g6, g1) + ANGLE90))
        g2.addInpoint(a4.outpoint) # reverse direction       
        g2.addOutpoint(a4.inpoint) # reverse direction 
        g3.addInpoint(a5.outpoint)  #reverse direction 
        #b/w g4 underarm & g5 armscye point
        g4.addOutpoint(polar(g4, distance(g4, g5)/3.0, angleOfLine(a8, g4) + ANGLE90))                       
        g5.addInpoint(polar(g5, distance(g4, g5)/3.0, angleOfLine(g1, g5)))
        #b/w g5 armscye point & g6 shoulder point
        g5.addOutpoint(polar(g5, distance(g5, g6)/3.0, angleOfLine(g5, g1)))
        g6.addInpoint(polar(g6, distance(FAP, g6)/6.0, angleOfLine(g1, g6) - ANGLE90)) #short control handle, perpendicular to shoulder seam  

        #rotate upper front coat points counterclockwise
        updatePoint(g1.outpoint, polar(g1, distance(g1, g2)/3.0, angleOfLine(g1, g1.outpoint)))
        pivot = FBP          
        slashAndSpread(pivot, -bustDartAngle, g4, g4.outpoint, g5.inpoint, g5, g5.outpoint, g6.inpoint, g6, g1, g1.outpoint, g2, g2.inpoint, g2.outpoint, g3, g3.inpoint) #rotate counterclockwise, so angle < 0 
                                                      
        #---Bodice Back B---#
        backBustEase = 0.0825 * CD.back_underarm / 2.0
        #backWaistEase = 0.0825 * CD.back_waist / 2.0
        #backHipEase = 0.0625 * CD.back_hip / 2.0        
        BNC = B.addPoint('BNC', (0.0, 0.0)) #back neck center
        BWC = B.addPoint('BWC', down(BNC, CD.back_waist_length)) #back waist center
        BSH = B.addPoint('BSH', up(BWC, CD.back_shoulder_height)) #shoulder height reference point
        BWS = B.addPoint('BWS', right(BWC, CD.back_waist/2.0)) #back waist side reference point
        BSP = B.addPoint('BSP', highestP(onCircleAtX(BWC, CD.back_shoulder_balance, BNC.x + CD.back_shoulder_width/2.0))) #back shoulder point
        BNS = B.addPoint('BNS', leftmostP(onCircleAtY(BSP, CD.shoulder, BSH.y))) #back neck side
        BAP = B.addPoint('BAP', lowestP(onCircleAtX(BNS, CD.back_underarm_balance, BNC.x + CD.across_back/2.0 + backBustEase/2.0))) #back underarm point
        BUC = B.addPoint('BUC', (BNC.x, BAP.y)) #back undearm center
        BUS1 = B.addPoint('BUS1', right(BUC, CD.back_underarm/2.0)) #back underarm side reference point
        BUS = B.addPoint('BUS', down(BUS1, distance(FUS1, FUS))) #adjusted back underarm side        
        BHC = B.addPoint('BHC', down(BWC, CD.back_hip_height)) #back hip center
        BHS = B.addPoint('BHS', right(BHC, CD.back_hip/2.0)) #temporary back hip side        

        #adjust block to topper points
        backBustEase = 0.0825*CD.back_underarm
        backWaistEase = 0.0625*CD.back_waist
        backHipEase = 0.0825*CD.back_hip
        b1 = B.addPoint('b1', down(BNC, 0.03*CD.back_waist_length)) #new back neck center
        b2 = B.addPoint('b2', onLineAtLength(BNS, BSP, distance(FNS, a2))) #new back neck side
        b3 = B.addPoint('b3', right(BSP, distance(FNS, a2))) #new shoulder point
        #BUS = B.addPoint('BUS', right(BUS, backBustEase)) #new underarm side
        #b24 = B.addPoint('b24', right(BWS, backWaistEase)) #new waist side
        #b25 = B.addPoint('b25', right(BHS, backHipEase)) #new hip side

        #Bodice Back B control points
        #b/w BNS back neck point & BNC back neck center
        BNC.addInpoint(right(BNC, 0.75 * abs(BNC.x - BNS.x)))
        BNS.addOutpoint(polar(BNS, abs(BNS.y - BNC.y)/2.0, angleOfLine(BNS, BSP) + ANGLE90)) #perpendicular to shoulder seam
        #b/w BUS underarm point & BAP underarm curve
        BUS.addOutpoint(left(BUS, distance(BUS, BAP)/3.0)) #perpendicular to side seam
        BAP.addInpoint(polar(BAP, distance(BUS, BAP)/3.0, angleOfLine(BNS, BAP)))
        #b/w BAP underarm curve & BNS shoulder point
        BAP.addOutpoint(polar(BAP, distance(BAP, BSP)/3.0, angleOfLine(BAP, BNS)))
        BSP.addInpoint(polar(BSP, distance(BAP, BSP)/6.0, angleOfLine(BNS, BSP) + ANGLE90)) #short control handle, perpendicular to shoulder seam        
        #b/w b1 new neck point & b2 new front neck center
        b1.addInpoint(right(b1, 0.75 * abs(b1.x - b2.x)))
        b2.addOutpoint(polar(b2, abs(b1.y - b2.y)/2.0, angleOfLine(b2, b1.inpoint)))
        #b/w BUS new underarm & BAP armscye curve & b3 new shoulder tip
        b3.addInpoint(polar(b3, distance(BAP, b3)/6.0, angleOfLine(b2, b3) + ANGLE90)) #short control handle, perpendicular to shoulder seam

        #extend front collar
        back_neck_curve = points2List(b1, b1.inpoint, b2.outpoint, b2)
        a15 = A.addPoint('a15', polar(a2, curveLength(back_neck_curve), angleOfLine(a2, a2.outpoint))) #front neck extension point 1
        a16 = A.addPoint('a16', polar(a15, 0.13 * CD.front_waist_length, angleOfLine(a2, a15) + ANGLE90)) #front neck extension point 2        
        a17 = A.addPoint('a17', polar(a16, distance(a2, a15), angleOfLine(a15, a2))) #front neckextension point 3
        #control points        
        #b/w g1 neck point, a12/a3 split point, a1 front neck center        
        a15.addInpoint(polar(a15, distance(a2, a15)/3.0, angleOfLine(a15, a16) + ANGLE90))      
        #b/w a16 extended collar top corner & a17 extended collar top midpoint
        a16.addOutpoint(polar(a16, distance(a16, a17)/3.0, angleOfLine(a15, a16) + ANGLE90))
        a17.addInpoint(polar(a17, distance(a16, a17)/3.0, angleOfLine(a2, a2.outpoint)))
        #b/w a17 extended collar midpoint & a6 extended collar neck point
        a17.addOutpoint(polar(a17, distance(a17, a6)/3.0, angleOfLine(a2.outpoint, a2)))
        a6.addInpoint(up(a6, distance(a17, a6)/3.0))  

        #Adjust Back B
        #lower underarm       
        pnt = down(BUS, 0.2 * CD.side)        
        b4 = B.addPoint('b4', right(pnt, 0.12 * CD.back_underarm))
        #extend side seam
        b5 = B.addPoint('b5', right(BHS, 0.4 * CD.back_hip/2.0)) #push out hem side
        b6 = B.addPoint('b6', onLineAtLength(b4, b5, distance(g4, a9))) #make back side equal to front side length
        #extend back center line
        b7 = B.addPoint('b7', down(b1, 1.5 * LOWER_LENGTH)) #begin back center line angle below back neck center
        b8 = B.addPoint('b8', left(BHC, 0.2 * CD.back_hip/2.0)) #push out hem center
        pnt = dPnt(intersectLines(b5, b6, b7, b8)) # find point where center & side seam intersect
        b9 = B.addPoint('b9', onLineAtLength(pnt, b8, distance(pnt, b6))) #new front hem center
        #adjust control points
        #b/w b4 underarm & BAP armscye curve & b3 shoulder point
        b4.addOutpoint(polar(b4, distance(b4, BAP)/3.0, angleOfLine(b4, b5) + ANGLE90))
        (BAP.inpoint.x, BAP.inpoint.y) = polar(BAP, distance(b4, BAP)/3.0, angleOfLine(b3, b4))
        (BAP.outpoint.x, BAP.outpoint.y) = polar(BAP, distance(BAP, b3)/3.0, angleOfLine(b4, b3))
        #b/w b9 hem center and b6 hem side
        b9.addOutpoint(polar(b9, distance(b9, b6)/3.33, angleOfLine(b8, b9) - ANGLE90))
        b6.addInpoint(polar(b6, distance(b9, b6)/3.33, angleOfLine(b5, b6) + ANGLE90))
        #b/w b7 flex point center & b9 hem center
        b7.addOutpoint(down(b7, distance(b7, b9)/8.0))
        b9.addInpoint(polar(b9, distance(b7, b9)/8.0, angleOfLine(b9, b7.outpoint)))

        #---Shirt sleeve C---#
        #get front & back armcye length
        back_armscye = points2List(b4, b4.outpoint, BAP.inpoint, BAP, BAP.outpoint, b3.inpoint, b3)
        front_armscye = points2List(g4, g4.outpoint, g5.inpoint, g5, g5.outpoint, g6.inpoint, g6)
        back_armscye_length = curveLength(back_armscye)
        front_armscye_length = curveLength(front_armscye)
        ARMSCYE_LENGTH = back_armscye_length + front_armscye_length
        CAP_HEIGHT = ARMSCYE_LENGTH/3.0 # + distance(FUS, g4)
        BICEP_WIDTH = 1.15 * CD.bicep #15% ease in bicep
        SLEEVE_LENGTH = CD.oversleeve_length
        WRIST_WIDTH = 1.15 * CD.wrist #15% ease in wrist

        c1 = C.addPoint('c1', (0,0)) #back top  - A
        c2 = C.addPoint('c2', down(c1, CD.oversleeve_length)) #back wrist- B

        c3 = C.addPoint('c3', right(c1, BICEP_WIDTH)) #front top  - C
        c4 = C.addPoint('c4', down(c3, CD.oversleeve_length)) #front wrist -D

        c5 = C.addPoint('c5', up(c2, CD.undersleeve_length)) #back bicep - E
        c6 = C.addPoint('c6', up(c4, CD.undersleeve_length)) #front bicep - F
        c7 = C.addPoint('c7', midPoint(c5, c6)) #mid bicep - J

        c8 = C.addPoint('c8', midPoint(c1, c3)) #mid top - G
        c9 = C.addPoint('c9', midPoint(c2, c4)) #mid wrist - H

        c11 = C.addPoint('c11', right(c5, 0.25 * distance(c5, c7))) #back cap reference - I
        c12 = C.addPoint('c12', left(c8, 0.25 * distance(c8, c1))) #back cap reference - K
        c13 = C.addPoint('c13', midPoint(c11, c12)) #back cap reference - L

        c14 = C.addPoint('c14', left(c6, 0.25 * distance(c6, c7))) #front cap reference - M
        c15 = C.addPoint('c15', right(c8, 0.25 * distance(c8, c3))) #front cap reference - N
        c16 = C.addPoint('c16', midPoint(c14, c15)) #front cap reference - O

        back_armscye_length = distance(g6, g5) + distance(g5, g4)
        front_armscye_length = distance(b3, BAP) + distance(BAP, b4)
        c17 = C.addPoint('c17', leftmostP(onCircleAtY(c13, back_armscye_length - distance(c8, c13), c7.y))) #extend back bicep
        c18 = C.addPoint('c18', rightmostP(onCircleAtY(c16, front_armscye_length - distance(c8, c16), c7.y))) #extend front bicep

        #Sleeve C control points
        #cap curve = c17,c13,c8,c16,c8
        #b/w c1 sleeve cap to c20 front armcap to c10 front underarm
        c8.addInpoint(c12)
        c8.addOutpoint(c15)
        c13.addOutpoint(polar(c13, distance(c13, c8)/3.0, angleOfLine(c13, c8.inpoint)))
        c13.addInpoint(polar(c13, distance(c13, c17)/3.0, angleOfLine(c13.outpoint, c13)))
        c17.addOutpoint(right(c17, distance(c17, c13)/3.0))
        c16.addInpoint(polar(c16, distance(c16, c8)/3.0, angleOfLine(c16, c8.outpoint)))
        c16.addOutpoint(polar(c16, distance(c16, c18)/3.0, angleOfLine(c16.inpoint, c16)))
        c18.addInpoint(left(c18, distance(c18, c16)/3.0))
        #b/w c2 back wrist & c17 back bicep
        c2.addOutpoint(up(c2, distance(c2, c17)/2.0))
        c17.addInpoint(polar(c17, distance(c2, c17)/3.0, angleOfLine(c17, c2.outpoint)))
        #b/w c4 front wrist & c18 front bicep
        c4.addInpoint(up(c4, distance(c4, c18)/2.0))
        c18.addOutpoint(polar(c18, distance(c4, c18)/3.0, angleOfLine(c18, c4.inpoint)))

        #Split Sleeve
        c20 = C.addPoint('c20', (c8.x, c13.y))
        c20.addInpoint(up(c20, 0.75 * distance(c20, c8)))
        c20.addOutpoint(c20.inpoint)
        #rotate c8 counterclockwise as c19
        c19 = C.addPoint('c19', c8)
        c19.addInpoint(c8.inpoint)
        c19.addOutpoint(down(c8, distance(c8, c20)/4.0))
        slashAndSpread(c13, angleOfDegree(-15), c19.outpoint, c19, c19.inpoint, c13.outpoint)
        #rotate c8 clockwise as c21
        c21 = C.addPoint('c21', mirror(c19, c8))
        c21.addOutpoint(mirror(c19.inpoint, c8))
        c21.addInpoint(mirror(c19.outpoint, c8))
        slashAndSpread(c16, angleOfVector(c8, c16, c21), c16.inpoint)

        #smooth cap curves
        updatePoint(c13, intersectLines(c20, c13, c13.inpoint, c13.outpoint))
        updatePoint(c16, intersectLines(c20, c16, c16.inpoint, c16.outpoint))

        #check sleeve cap length
        curve = points2List(c17, c17.outpoint, c13.inpoint, c13, c13.outpoint, c19.inpoint, c19)
        back_cap_length = curveLength(curve)
        curve = points2List(c21, c21.outpoint, c16.inpoint, c16, c16.outpoint, c18.inpoint, c18)
        front_cap_length = curveLength(curve)
        back_diff = back_cap_length - back_armscye_length
        front_diff = front_cap_length - front_armscye_length
        if back_diff > 0.0:
            print 'shorten back'
            back_curve = points2List(c17, c17.outpoint, c13.inpoint, c13)
            new_curve = splitCurveAtLength(back_curve, back_diff)
            updatePoint(c17, new_curve[3])
            updatePoint(c17.outpoint, new_curve[4])
            updatePoint(c13.inpoint, new_curve[5])
        elif back_diff < 0.0:
            print 'lengthen back'
            pnt1 = dPnt(extendLine(c17.outpoint, c17, back_diff))
            updatePoint(c17, pnt1)
        front_curve = points2List(c18, c18.inpoint, c16.outpoint, c16)
        if front_diff > 0.0:
            print 'shorten front'
            front_curve = points2List(c18, c18.inpoint, c16.outpoint, c16)
            new_curve = splitCurveAtLength(front_curve, front_diff)
            updatePoint(c18, new_curve[3])
            updatePoint(c18.inpoint, new_curve[4])
            updatePoint(c16.outpoint, new_curve[5])
        elif front_diff < 0.0:
            print 'lengthen front'
            pnt1 = dPnt(extendLine(c18.inpoint, c18, front_diff))
            updatePoint(c18, pnt1)

        #check sleeve length
        back_curve = points2List(c2, c2.outpoint, c17.inpoint, c17)
        back_sleeve_length = curveLength(back_curve)
        front_curve = points2List(c4, c4.inpoint, c18.outpoint, c18)
        front_sleeve_length = curveLength(front_curve)
        diff = back_sleeve_length - front_sleeve_length
        if diff < 0.0:
            print 'lengthen sleeve back'
            updatePoint(c2, down(c2, -diff))
            updatePoint(c9, intersectLines(c7, c9, c2, c4))
        elif diff > 0.0:
            print 'lengthen sleeve front'
            updatePoint(c4, down(c4, diff))
            updatePoint(c9, intersectLines(c7, c9, c2, c4))

        #---Welt D---#
        d4 = A.addPoint('d4', onLineAtLength(a11, FBP, WELT_HEIGHT)) #welt top right
        d1 = A.addPoint('d1', intersectLineRay(a12, a8, d4, angleOfLine(a11, a12))) #welt top left
        angle1 = angleOfVector(a12, d1, d4) #left upper corner angle
        angle2 = angleOfVector(a11, d4, d1) #right upper corner angle
        d2 = A.addPoint('d2', polar(d1, distance(a12, d1), angleOfLine(d1, d4) - angle1))     
        d3 = A.addPoint('d3', polar(d4, distance(a11, d4), angleOfLine(d4, d1) + angle2))
        
        #---Pocket E---#
        #pocket     
        e1 = A.addPoint('e1', (a11.x, a7.y)) #lower right pocket corner         

        #---Front Facing F---#
        #---Upper Front G---#
        #---Sleeve Front H---#

        #---Sleeve Facing I---#
        i1 = C.addPoint('i1', up(c2, distance(c7, c9)/4.0)) #top left facing point
        i2 = C.addPoint('i2', up(c4, distance(c7, c9)/4.0)) #top right facing point
        i3 = C.addPoint('i3', down(c4, distance(c7, c9)/4.0)) #lower right facing point        
        i4 = C.addPoint('i4', down(c2, distance(c7, c9)/4.0)) #lower left facing point
        
        
        #---Front Lining J---#
        angle1 = angleOfVector(a5, FBP, g3)               
        jD1 = J.addPoint('jD1', onLineAtLength(FBP, g5, distance(FBP, g5)/5.0)) #new dartpoint
        jD1.i = J.addPoint('jD1.i', rotate(FBP, g5, angle1))
        jD1.i.addOutpoint(rotate(FBP, g5.outpoint, angle1)) 
        jD1.o = J.addPoint('jD1.o', g5) #rotated copy of jD1.o to create new bust dart along side seam
        jD1.o.addInpoint(g5.inpoint)       
        j5 = J.addPoint('j5', rotate(FBP, g6, angle1)) #rotate g6 shoulder tip
        j5.addInpoint(rotate(FBP, g6.inpoint, angle1))
        j6 = J.addPoint('j6', rotate(FBP, g1, angle1)) #rotate g1 neck front side
        j6.addOutpoint(rotate(FBP, g1.outpoint, angle1))
        j7 = J.addPoint('j7', rotate(FBP, g2, angle1)) #rotate g2 facing curve break point
        j7.addInpoint(rotate(FBP, g2.inpoint, angle1))        

        foldDart(jD1, j5)
         

        #---------------------------------------------#
        #---all points defined, draw pattern pieces---#
        #---------------------------------------------#

        #draw Lower Front A
        pnt1 = dPnt((a11.x, a8.y))
        A.setLabelPosition(pnt1)
        A.setLetter((a11.x, a12.y), scaleby=10.0)
        aG1 = dPnt(FUC)
        aG2 = dPnt(FHC)
        A.addGrainLine(aG1, aG2)
        A.addGridLine(['M', FUC, 'L', FUS1, 'M', FBC, 'L', FBP, 'L', FBS, 'M', FWC, 'L', FWS1, 'M', FUS, 'L', FWS2, 'M', FNC, 'L', FHC, 'L', FHS1, 'M', FUS, 'C', FAP, 'C', FSP, 'L', FNS, 'C', FNC, 'M', a12, 'L', g4, 'C', g5, 'C', g6, 'L', g1, 'C', g2, 'C', g3, 'M', a4, 'L', a14, 'M', a11, 'L', e1, 'M', d1, 'L', d2, 'L', d3, 'L', d4, 'L', d1])
        pth = (['M', a6, 'L', a13, 'L', a10, 'C', a14, 'C', a9, 'L', a12, 'L', a11 , 'L', FBP, 'L', a5, 'C', a4, 'C', a2, 'C', a15, 'L', a16, 'C', a17, 'C', a6])
        A.addDartLine(['M', a3, 'L', a11, 'L', a12])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        #draw Back B
        pnt1 = dPnt((distance(BSH, BNS)/2.0, distance(BNC, BUC)/2.0))
        B.setLabelPosition((pnt1))
        B.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        bG1 = dPnt((distance(BSH, BNS)/4.0, BUC.y))
        bG2 = dPnt(down(bG1, distance(BNC, BHC)/2.0))
        B.addGrainLine(bG1, bG2)
        B.addGridLine(['M', BNS, 'L', BSH, 'L', BWC, 'L', BWS, 'M', BUC, 'L', BUS1, 'M', BNC, 'L', BHC, 'L', BHS, 'L', BWS, 'L', BUS, 'C', BAP, 'C', BSP, 'L', BNS, 'C', BNC])
        pth = (['M', b1, 'L', b7, 'C', b9, 'C', b6, 'L', b4, 'C', BAP, 'C', b3, 'L', b2, 'C', b1])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        #draw Sleeve Back C
        pnt1 = dPnt(down(c5, distance(c7, c9)/6.0))
        C.setLetter((pnt1.x, pnt1.y), scaleby=15.0)
        C.setLabelPosition(down(pnt1, distance(pnt1, c9)/6.0))
        cG1 = dPnt((c13.x, c11.y))
        cG2 = down(cG1, 0.75 * distance(c7, c9))
        C.addGrainLine(cG1, cG2)
        C.addGridLine(['M', c1, 'L', c2, 'L', c4, 'L', c3, 'L', c1, 'M', c13, 'L', c16, 'M', c5, 'L', c6, 'M', c8, 'L', c9, 'M', i1, 'L', i2, 'L', i3, 'L', i4, 'L', i1])
        pth = (['M', c19, 'C', c20, 'L', c9, 'L', c2, 'C', c17, 'C', c13, 'C', c19])
        C.addSeamLine(pth)
        C.addCuttingLine(pth)

        #draw Welt D
        D.setLetter((d1.x + distance(d1, d4) / 5.0, d1.y), scaleby=5.0)
        D.setLabelPosition((d1.x + distance(d1, d4) / 3.0, d2.y))
        dG1 = dPnt((d2.x + 0.25 * distance(d1, d4), d2.y + (abs(d2.y - d1.y) / 6.0)))
        dG2 = dPnt(polar(dG1, 0.75 * distance(d1, d4), angleOfLine(d1, d4)))
        D.addGrainLine(dG1, dG2)
        pth = (['M', d1, 'L', d4])
        D.addFoldLine(pth)
        pth =(['M', a12, 'L', d1, 'L', d2, 'L', d3, 'L', d4, 'L', a11, 'L', a12])
        D.addSeamLine(pth)
        D.addCuttingLine(pth)

        #draw Pocket E
        pnt1 = dPnt((a12.x + distance(a12, a11)/5.0, a12.y + distance(a12, a8)/2.0))
        E.setLetter((pnt1.x, pnt1.y), scaleby=10.0)
        E.setLabelPosition((a12.x + distance(a12, a11) / 2.0, a12.y + abs(a12.y - e1.y) / 6.0))
        eG1 = dPnt((a12.x + 0.75 * distance(a12, a11), a11.y + abs(a11.y - e1.y) / 4.0))
        eG2 = down(eG1, 0.6 * distance(a11, e1))
        E.addGrainLine(eG1, eG2)
        pth =(['M', a11, 'L', e1, 'L', a8, 'L', a12, 'L', a11])
        E.addSeamLine(pth)
        E.addCuttingLine(pth)

        #draw Front Facing F
        F.setLetter((FNC.x, FUC.y), scaleby=8.0)
        F.setLabelPosition((FNC.x - 25, FUC.y + 50))
        fG1 = dPnt(onLineAtLength(a3, a6, distance(a3, a6)/4.0))
        fG2 = down(fG1, 0.75 * distance(a3, a14))
        F.addGrainLine(fG1, fG2)
        pth =(['M', a4, 'C', a2, 'C', a15, 'L', a16, 'C', a17, 'C', a6, 'L', a13, 'L', a10, 'C', a14, 'L', a4])
        F.addSeamLine(pth)
        F.addCuttingLine(pth)

        #draw Upper Front G
        pnt1 = dPnt(midPoint(g5, FBP))
        G.setLetter((pnt1.x, pnt1.y), scaleby=10.0)
        G.setLabelPosition((pnt1.x, pnt1.y + 50))
        gG1 = dPnt((pnt1.x - 50, FAP.y))
        gG2 = down(gG1, 0.75 * distance(FAP, a11))
        G.addGrainLine(gG1, gG2)        
        pth =(['M', g2, 'C', g3, 'L', FBP, 'L', a11, 'L', e1, 'L',  a8, 'L', a12, 'L', g4, 'C', g5, 'C', g6, 'L', g1, 'C', g2])
        G.addSeamLine(pth)
        G.addCuttingLine(pth)

        #draw Sleeve Front H
        pnt1 = dPnt((c16.x, c6.y + distance(c7, c9)/6.0))
        H.setLetter((pnt1.x, pnt1.y), scaleby=15.0)
        H.setLabelPosition(down(pnt1, distance(c7, c9)/6.0))
        pnt2 = dPnt((c15.x, c6.y))
        hG1 = dPnt((pnt2.x, pnt2.y))
        hG2 = down(hG1, 0.75 * distance(c7, c9))
        H.addGrainLine(hG1, hG2)
        pth = (['M', c21, 'C', c16, 'C', c18, 'C', c4, 'L', c9, 'L', c20, 'C', c21])
        H.addSeamLine(pth)
        H.addCuttingLine(pth)

        #draw Sleeve Facing I
        pnt1 = dPnt((i1.x + distance(i1, i2)/4.0, (i1.y + distance(i1, c2)/2.0)))
        I.setLetter((pnt1.x, pnt1.y), scaleby=8.0)
        pnt2 = dPnt((pnt1.x + distance(i1, i2)/6.0, pnt1.y))
        I.setLabelPosition((pnt2.x, pnt2.y))
        iG1 = dPnt((i1.x + 0.75 * distance(i1, i2), (i1.y + distance(i1, c2)/4.0)))
        iG2 = down(iG1, 0.75 * distance(i1, i4))
        I.addGrainLine(iG1, iG2)
        pth = (['M', c4, 'L', c2])
        I.addFoldLine(pth)
        pth = (['M', i1, 'L', i2, 'L', i3, 'L', i4, 'L', i1])
        I.addSeamLine(pth)
        I.addCuttingLine(pth)
        
        #draw Front Lining J
        pnt1 = dPnt((jD1.x, jD1.i.y))
        J.setLetter((pnt1.x, pnt1.y), scaleby=10.0)
        J.setLabelPosition((pnt1.x, pnt1.y + 100))
        jG1 = dPnt((j6.x, jD1.o.y))
        jG2 = down(jG1, 0.75 * distance(jD1.o, a8))
        J.addGrainLine(jG1, jG2)
        J.addDartLine(['M', jD1.oc, 'L', jD1, 'L', jD1.ic])        
        pth =(['M', j7, 'L', a14, 'C', a9, 'L', g4, 'C', jD1.o, 'L', jD1.m, 'L', jD1.i, 'C', j5, 'L', j6, 'C', j7])
        J.addSeamLine(pth)
        J.addCuttingLine(pth)        


        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

