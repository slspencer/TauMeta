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
        ## measurements required by this pattern
        ##	CD.across_back_b
        ##	CD.across_chest_f
        ##	CD.hip_arc_b
        ##	CD.waist_to_hip_b
        ##	CD.shoulder_tip_to_waist_back
        ##	CD.neck_side_to_waist_b
        ##	CD.shoulder_tip_to_shoulder_tip_b
        ##	CD.highbust_arc_b
        ##	CD.neck_side_to_armfold_b
        ##	CD.waist_arc_b
        ##	CD.neck_back_to_waist_b
        ##	CD.arm_upper_circ
        ##	CD.neck_side_to_bust_side_f
        ##	CD.bustpoint_to_bustpoint
        ##	CD.bustpoint_to_neck_side
        ##	CD.bust_arc_f
        ##	CD.bust_arc_f
        ##	CD.hip_arc_f
        ##	CD.waist_to_hip_f
        ##	CD.shoulder_tip_to_waist_front
        ##	CD.shoulder_tip_to_shoulder_tip_f
        ##	CD.highbust_arc_f
        ##	CD.neck_side_to_armpit_f
        ##	CD.waist_arc_f
        ##	CD.neck_front_to_waist_f
        ##	CD.arm_shoulder_tip_to_wrist
        ##	CD.shoulder_length
        ##	CD.armpit_to_waist_side
        ##	CD.arm_wrist_circ$

        #
        #create pattern pieces
        A = coat.addPiece('Front', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = coat.addPiece('Back', 'B', fabric = 2, interfacing = 0, lining = 2)
        C = coat.addPiece('Sleeve - Back', 'C', fabric = 2, interfacing = 0, lining = 2)
        D = coat.addPiece('Lining - Back', 'D', fabric = 0, interfacing = 0, lining = 2)        
        E = coat.addPiece('Pocket', 'E', fabric = 2, interfacing = 0, lining = 0)
        F = coat.addPiece('Lining - Facing', 'F', fabric = 2, interfacing = 2, lining = 0)
        G = coat.addPiece('Front - Upper', 'G', fabric = 2, interfacing = 0, lining = 0)
        H = coat.addPiece('Sleeve - Front', 'H', fabric = 2, interfacing = 0, lining = 2)
        I = coat.addPiece('Sleeve - Outer Cuff', 'I', fabric = 2, interfacing = 2, lining = 0)
        J = coat.addPiece('Lining - Front', 'J', fabric = 0, interfacing = 0, lining = 2)
        K = coat.addPiece('Front - Lower', 'K', fabric = 2, interfacing = 0, lining = 0)
        L = coat.addPiece('Sleeve - Inner Cuff', 'L', fabric = 2, interfacing = 0, lining = 0)

        #---Bodice Front A---#
        FSC = A.addPoint('FSC', (0.0, 0.0)) #front shoulder center
        FSW = A.addPoint('FSW', left(FSC, CD.shoulder_tip_to_shoulder_tip_f/2.0)) #front shoulder width
        FWC = A.addPoint('FWC', down(FSC, CD.neck_side_to_waist_f)) #front waist center
        FNC = A.addPoint('FNC', up(FWC, CD.neck_front_to_waist_f)) #front neck center        
        FBC = A.addPoint('FBC', up(FWC, CD.bustpoint_to_neck_side)) #bust center
        FBP = A.addPoint('FBP', left(FBC, CD.bustpoint_to_bustpoint/2.0)) #bust point
        FSP = A.addPoint('FSP', highestP(onCircleAtX(FWC, CD.shoulder_tip_to_waist_front, FSW.x))) #front shoulder tip
        FNS = A.addPoint('FNS', highestP(onCircleAtY(FSP, CD.shoulder_length, FSC.y))) #front neck side
        FUC = A.addPoint('FUC', down(FNC, CD.neck_front_to_highbust_f)) #front highbust/underarm center
        FAP = A.addPoint('FAP', left(FUC, CD.armfold_to_armfold_f/2.0)) #front armfold point 
        #FAP = A.addPoint('FAP', lowestP(onCircleAtX(FNS, CD.neck_side_to_armpit_f, FNC.x - CD.across_chest_f/2.0))) #front underarm point
        #FUC = A.addPoint('FUC', (FNC.x, FAP.y)) #front undearm center
        FUS1 = A.addPoint('FUS1', left(FUC, CD.highbust_arc_f/2.0)) #front underarm side
        FBS = A.addPoint('FBS', leftmostP(tangentPointOnCircle(FBP, CD.bust_arc_f/2.0 - distance(FBC, FBP), FUS1))) #line from FBP is perpendicular to line through FUS1
        FUS = A.addPoint('FUS', onLineAtLength(FUS1, FBS, 0.13 * CD.armpit_to_waist_side)) #adjusted front underarm side on line FUS1-10
        FWS1 = A.addPoint('FWS1', left(FWC, CD.waist_arc_f/2.0)) #temporary front waist side 1 - on waist line
        FWS2 = A.addPoint('FWS2', onLineAtLength(FUS1, FBS, CD.armpit_to_waist_side)) #temporary front waist side 2 - on side seam
        FHC = A.addPoint('FHC', down(FWC, CD.waist_to_hip_f)) #front hip center        
        FHS = A.addPoint('FHS', left(FHC, CD.hip_arc_f/2.0)) #front hip side 1        
        #front waist dart
        totalDartAngle = abs(angleOfVector(FWS1, FBP, FWS2))
        bustDartAngle = totalDartAngle/2.0
        #Bodice Lower Front A control points
        #b/w FNS front neck point & FNC front neck center
        FNS.addOutpoint(polar(FNS, abs(FNC.y - FNS.y)/2.0, angleOfLine(FSP, FNS)+ ANGLE90))
        FNC.addInpoint(onLineAtY(FNS, FNS.outpoint, FNC.y))               
        #b/w FAP front underarm point & FSP front shoulder point
        FSP.addInpoint(polar(FSP, distance(FAP, FSP)/6.0, angleOfLine(FSP, FNS) + ANGLE90)) #short control handle perpendicular to shoulder seam
        FAP.addOutpoint(polar(FAP, distance(FAP, FSP)/3.0, angleOfLine(FAP, FNS))) #control handle points to front neck point
        #b/w FUS front underarm side & FAP front underarm point
        FAP.addInpoint(polar(FAP, distance(FUS, FAP)/3.0, angleOfLine(FNS, FAP)))
        FUS.addOutpoint(polar(FUS, distance(FUS, FAP)/3.0, angleOfLine(FWS2, FUS) + ANGLE90)) #control handle is perpendicular to side seam at underarm                        
        #lower front coat points
        a1 = A.addPoint('a1', down(FNC, 0.03*CD.neck_front_to_waist_f)) #new front neck center        
        a2 = A.addPoint('a2', onLineAtLength(FNS, FSP, distance(FNC, a1))) #new front neck point                            
        #control points
        #b/w a2 & a4 new         
        a2.addInpoint(polar(a2, distance(a2, a1)/3.0, angleOfLine(FSP, a2) + ANGLE90))
        a2.addOutpoint(polar(a2, distance(a2, a2.inpoint)/3.0, angleOfLine(a2.inpoint, a2)))
                
        #split neck curve
        front_neck_curve = points2List(FNS, FNS.outpoint, FNC.inpoint, FNC)
        curve_length = curveLength(front_neck_curve)
        a3 = A.addPoint('a3', onCurveAtLength(front_neck_curve, 2 * curve_length/3.0)) #divide front neck curve 2/3rd along length
        a4a = A.addPoint('a4a', down(FNC, 0.25 * distance(FNC, FUC)))
        a4 = A.addPoint('a4', dPnt((FNS.x, a4a.y))) #break point for lapel at collar
        a5 = A.addPoint('a5', onLineAtLength(FBP, a3, distance(FBP, a4)/6.0))
        #control points
        a4.addInpoint(down(a4, distance(a4, a5) / 3.0))
        a4.addOutpoint(up(a4, distance(a4, a2) / 3.0))
        a5.addOutpoint(onLineAtLength(a5, a3, distance(a5, a4) / 3.0)) 

        #extend front center line        
        a6 = A.addPoint('a6', right(a1, 0.1 * CD.neck_front_to_waist_f)) #right of a1 front neck center
        a7 = A.addPoint('a7', right(FHC, 0.1 * CD.neck_front_to_waist_f)) #right of FHC front hip center                        
  
        #----Upper Front G coat points -------  
        #need these to create Front A side points     
        g1 = A.addPoint('g1', a2) #new front neck point
        g2 = A.addPoint('g2', a4) #break point         
        #g3 = A.addPoint('g3', a5) #front curve point
        
        g1.addOutpoint(polar(g1, distance(g1, g2)/3.0, angleOfLine(FSP, FNS) + ANGLE90))
        g2.addInpoint(a4.outpoint) # reverse direction       
        g2.addOutpoint(a4.inpoint) # reverse direction  
        FBP.addInpoint(a5)
        FBP.addOutpoint(a5.outpoint)        
        
        LOWER_LENGTH = 0.2 * CD.armpit_to_waist_side #20% side length        
        pnt = onLineAtLength(FUS, FWS2, 0.2 * CD.armpit_to_waist_side)
        g4 = A.addPoint('g4', polar(pnt, 0.12 * CD.highbust_arc_f, angleOfLine(FBP, FBS))) #new front underarm - out 7% front underarm, down 40% side length                        
        g5 = A.addPoint('g5', left(FAP, distance(FNS, a2))) #new armscye curve        
        g6 = A.addPoint('g6', left(FSP, distance(FNS, a2))) #new shoulder point
        
        pivot = FBP          
        slashAndSpread(pivot, -bustDartAngle, g1, g1.outpoint, g2, g2.inpoint, g2.outpoint, g4, g5, g6) #rotate counterclockwise, so angle < 0
        g7 = A.addPoint('g7', left(FHS, 0.3 * CD.hip_arc_f)) #30% front hip ease at hip line        
        
        #control points       
        #b/w g4 underarm & g5 armscye point
        g4.addOutpoint(polar(g4, distance(g4, g5)/2.0, angleOfLine(g7, g4) + ANGLE90))                       
        g5.addInpoint(polar(g5, distance(g4, g5)/3.0, angleOfLine(g1, g5)))
        #b/w g5 armscye point & g6 shoulder point
        g5.addOutpoint(polar(g5, distance(g5, g6)/3.0, angleOfLine(g5, g1)))
        g6.addInpoint(polar(g6, distance(FAP, g6)/6.0, angleOfLine(g1, g6) - ANGLE90)) #short control handle, perpendicular to shoulder seam          
        #----end Upper Front G coat points -------         

        #create front lower hem curve   
        #extend front side seam to front lower hem
        a_H2 = A.addPoint('a_H2', extendLine(g4, g7, 0.3 * CD.armpit_to_waist_side)) #extend coat side seam below hip line by 30% of side length
        
        #create pocket line
        a11 = A.addPoint('a11', onLineAtLength(a3, FBP, FWC.y + (0.15 * CD.neck_front_to_waist_f))) #pocket center
        a12 = A.addPoint('a12', onLineAtLength(a_H2, g4, distance(FWC, FHC))) #pocket side 
                 
        #extend front center line to front lower hem
        pnt = dPnt(intersectLines(g4, a_H2, FNC, FHC)) # find point where center line & side seam intersect
        a_H1 = A.addPoint('a_H1', onLineAtLength(pnt, FNC, distance(pnt, a_H2))) #new front hem center 
        #control points
        a_H1.addOutpoint(left(a_H1, distance(a_H1, a_H2)/3.33))
        a_H2.addInpoint(polar(a_H2, distance(a_H1, a_H2)/3.33, angleOfLine(a_H2, g4) + ANGLE90))
              
        #create front upper hem curve as offset to front lower hem curve
        HEM_DEPTH = 0.2 * CD.armpit_to_waist_side  #hem deth is 20% side length      
        orig_curve = points2List(a_H1, a_H1.outpoint, a_H2.inpoint, a_H2)
        outset_curve = outsetCurve(orig_curve, HEM_DEPTH, ANGLE90) #returns outset_curve[p1, c1, c2, p2]
        a_h1 = A.addPoint('a_h1', outset_curve[0])
        a_h1.addOutpoint(outset_curve[1])      
        a_h2 = A.addPoint('a_h2', outset_curve[3])        
        a_h2.addInpoint(outset_curve[2])                     
         









        

        #---Bodice Back B---#
        backBustEase = 0.0825 * CD.highbust_arc_b / 2.0
        #backWaistEase = 0.0825 * CD.waist_arc_b / 2.0
        #backHipEase = 0.0625 * CD.hip_arc_b / 2.0
        BSH = B.addPoint('BSH', (0.0, 0.0)) #shoulder height reference point
        BSW = B.addPoint('BSW', right(BSH, CD.shoulder_tip_to_shoulder_tip_b/2.0)) #back shoulder sidth 
        BWC = B.addPoint('BWC', down(BSH, CD.neck_side_to_waist_b)) #back waist center
        BNC = B.addPoint('BNC', up(BWC,CD.neck_back_to_waist_b)) #back neck center
        BSP = B.addPoint('BSP', highestP(onCircleAtX(BWC, CD.shoulder_tip_to_waist_back, BSW.x))) #back shoulder point
        BNS = B.addPoint('BNS', leftmostP(onCircleAtY(BSP, CD.shoulder_length, BSH.y))) #back neck side
        
        BWS = B.addPoint('BWS', right(BWC, CD.waist_arc_b/2.0)) #back waist side reference point
        BUC = B.addPoint('BUC', down(BNC, CD.neck_back_to_highbust_b)) #back highbust/underarm center
        BAP1 = B.addPoint('BAP1', right(BUC, CD.armfold_to_armfold_b/2.0)) #back underarm point              
        #BAP1 = B.addPoint('BAP1', lowestP(onCircleAtX(BNS, CD.neck_side_to_armfold_b, BNC.x + CD.across_back_b/2.0 + backBustEase/2.0))) #back underarm point      
        #BUC = B.addPoint('BUC', (BNC.x, BAP1.y)) #back undearm center
        BUS1 = B.addPoint('BUS1', right(BUC, CD.highbust_arc_b/2.0)) #back underarm side reference point
        BUS = B.addPoint('BUS', down(BUS1, distance(FUS1, FUS))) #adjusted back underarm side        
        BHC = B.addPoint('BHC', down(BWC, CD.waist_to_hip_b)) #back hip center
        BHS = B.addPoint('BHS', right(BHC, CD.hip_arc_b/2.0)) #temporary back hip side        

        #adjust block to topper points
        backBustEase = 0.0825*CD.highbust_arc_b
        backWaistEase = 0.0625*CD.waist_arc_b
        backHipEase = 0.0825*CD.hip_arc_b
        b1 = B.addPoint('b1', down(BNC, 0.03*CD.neck_back_to_waist_b)) #new back neck center
        b2 = B.addPoint('b2', onLineAtLength(BNS, BSP, distance(FNS, a2))) #new back neck side
        b3 = B.addPoint('b3', right(BSP, distance(FNS, a2))) #new shoulder point
        BAP = B.addPoint('BAP', right(BUC, 0.95 * distance(b1, b3))) #new armscye curve         

        #Bodice Back B control points
        #b/w BNS back neck point & BNC back neck center
        BNC.addInpoint(right(BNC, 0.75 * abs(BNC.x - BNS.x)))
        BNS.addOutpoint(polar(BNS, abs(BNS.y - BNC.y)/2.0, angleOfLine(BNS, BSP) + ANGLE90)) #perpendicular to shoulder seam
        #b/w BUS underarm point & BAP underarm curve
        BUS.addOutpoint(left(BUS, distance(BUS, BAP)/3.0)) #perpendicular to side seam
        BAP.addInpoint(polar(BAP, distance(BAP, BUS)/3.0, angleOfLine(BSP, BUS)))
        #b/w BAP underarm curve & BNS shoulder point
        BAP.addOutpoint(polar(BAP, distance(BAP, BSP)/3.0, angleOfLine(BUS, BSP)))
        BSP.addInpoint(polar(BSP, distance(BAP, BSP)/6.0, angleOfLine(BNS, BSP) + ANGLE90)) #short control handle, perpendicular to shoulder seam        
        #b/w b1 new neck point & b2 new front neck center
        b1.addInpoint(right(b1, 0.75 * abs(b1.x - b2.x)))
        b2.addOutpoint(polar(b2, abs(b1.y - b2.y)/2.0, angleOfLine(b2, b1.inpoint)))
        #b/w BUS new underarm & BAP armscye curve & b3 new shoulder tip
        b3.addInpoint(polar(b3, distance(BAP, b3)/6.0, angleOfLine(b2, b3) + ANGLE90)) #short control handle, perpendicular to shoulder seam

        #extend front collar around back of neck
        back_neck_curve = points2List(b1, b1.inpoint, b2.outpoint, b2)
        a15 = A.addPoint('a15', polar(a2, curveLength(back_neck_curve), angleOfLine(a2, a2.outpoint))) #front neck extension point 1
        a16 = A.addPoint('a16', polar(a15, 0.13 * CD.neck_front_to_waist_f, angleOfLine(a2, a15) + ANGLE90)) #front neck extension point 2        
        a17 = A.addPoint('a17', polar(a16, distance(a2, a15), angleOfLine(a15, a2))) #front neckextension point 3
         
        

        #---------------------------------------------#
        #---all points defined, draw pattern pieces---#
        #---------------------------------------------#

        #draw Front A
        A.setLabelPosition(FWC)
        A.setLetter(up(FWC, distance(FWC, FNC)/4.0), scaleby=10.0)
        aG1 = dPnt(FUC)
        aG2 = dPnt(FAP)
        A.addGrainLine(aG1, aG2)
        pth = (['M', a6, 'L', a_H1, 'L', a_H2, 'L', a11 , 'L', FBP, 'L', a4, 'L', a2, 'L', a15, 'L', a16, 'L', a17, 'L', a6])     
        A.addSeamLine(pth)
        A.addCuttingLine(pth)  


        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

