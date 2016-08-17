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
        ##	CD.arm_wrist_circ

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
        try:
            tangentOnCircleFromPoint(FBP, CD.bust_arc_f/2.0 - distance(FBC, FBP), FUS1)
        except:
        FBS = A.addPoint('FBS', leftmostP(tangentOnCircleFromPoint(FBP, CD.bust_arc_f/2.0 - distance(FBC, FBP), FUS1))) #line from FBP is perpendicular to line through FUS1
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
        
        #split front lower hem curve at a4.x (front facing line)
        orig_curve = points2List(a_H1, a_H1.outpoint, a_H2.inpoint, a_H2)  
        a_H3 = A.addPoint('a_H3', onCurveAtX(orig_curve, a4.x)) #facing hem
        new_curve = splitCurveAtPoint(orig_curve, a_H3)
        updatePoint(a_H1.outpoint, new_curve[1])
        a_H3.addInpoint(new_curve[2])
        a_H3.addOutpoint(new_curve[4])                     
        updatePoint(a_H2.inpoint, new_curve[5])
       
        #split front lower hem curve from a_H3 to a_H2 at a11.x (pocket front line)
        orig_curve = points2List(a_H3, a_H3.outpoint, a_H2.inpoint, a_H2)
        new_curves = splitCurveAtX(orig_curve, a11.x)
        updatePoint(a_H3.outpoint, new_curves[1])
        a_H4 = A.addPoint('a_H4', new_curves[3])
        a_H4.addInpoint(new_curves[2])
        a_H4.addOutpoint(new_curves[4])
        updatePoint(a_H2.inpoint, new_curves[5])
        #extend front lower hem curve to front facing edge
        a_H5 = A.addPoint('a_H5', (a7.x, a_H1.y))           
            
        #split front upper hem curve at a4.x (front facing line)
        orig_curve = points2List(a_h1, a_h1.outpoint, a_h2.inpoint, a_h2)           
        new_curves = splitCurveAtX(orig_curve, a4.x) #return [p1, c1, c2, p2, c3, c4, p3]
        updatePoint(a_h1.outpoint, new_curves[1])
        a_h3 = A.addPoint('a_h3', new_curves[3])
        a_h3.addInpoint(new_curves[2])
        a_h3.addOutpoint(new_curves[4])
        updatePoint(a_h2.inpoint, new_curves[5]) 
        
        #create front lining hem curve from front upper hem curve a_h3 to a_h2 
        LINING_HEM_DEPTH = 0.75 * HEM_DEPTH
        orig_curve = points2List(a_h3, a_h3.outpoint, a_h2.inpoint, a_h2)
        outset_curve = outsetCurve(orig_curve, LINING_HEM_DEPTH, ANGLE90)
        a_l1 = A.addPoint('a_l1', outset_curve[0])
        a_l1.addOutpoint(outset_curve[1])
        a_l2 = A.addPoint('a_l2', outset_curve[3])
        a_l2.addInpoint(outset_curve[2])      
        
        #split front upper hem curve from a_h3 to a_h2 at a11.x (pocket front line)
        orig_curve = points2List(a_h3, a_h3.outpoint, a_h2.inpoint, a_h2)
        new_curves = splitCurveAtX(orig_curve, a11.x)
        updatePoint(a_h3.outpoint, new_curves[1])
        a_h4 = A.addPoint('a_h4', new_curves[3])
        a_h4.addInpoint(new_curves[2])
        a_h4.addOutpoint(new_curves[4])
        updatePoint(a_h2.inpoint, new_curves[5])
        #extend front upper hem curve to facing edge
        outset_line = outsetLine(a_H1, a_H5, HEM_DEPTH, -ANGLE90) #returns outset_line[p1, p2]
        a_h5 = A.addPoint('a_h5', outset_line[1])
        
        #create front pocket hem curve from front upper hem curve a_h4 to a_h2  
        orig_curve = points2List(a_h4, a_h4.outpoint, a_h2.inpoint, a_h2)
        outset_curve = outsetCurve(orig_curve, HEM_DEPTH, ANGLE90)
        a_p1 = A.addPoint('a_p1', outset_curve[0])
        a_p1.addOutpoint(outset_curve[1])
        a_p2 = A.addPoint('a_p2', outset_curve[3])
        a_p2.addInpoint(outset_curve[2])
        #split front pocket hem curve at a11.x
        orig_curve = points2List(a_p1, a_p1.outpoint, a_p2.inpoint, a_p2)
        new_curves = splitCurveAtX(orig_curve, a11.x)
        updatePoint(a_p1.outpoint, new_curves[1])
        a_p3 = A.addPoint('a_p3', new_curves[3])
        a_p3.addInpoint(new_curves[2])
        a_p3.addOutpoint(new_curves[4])
        updatePoint(a_p2.inpoint, new_curves[5])        
         
        

                                                      
        #---Bodice Back B---#
        backBustEase = 0.0825 * CD.highbust_arc_b / 2.0
        #backWaistEase = 0.0825 * CD.waist_arc_b / 2.0
        #backHipEase = 0.0625 * CD.hip_arc_b / 2.0        
        BNC = B.addPoint('BNC', (0.0, 0.0)) #back neck center
        BWC = B.addPoint('BWC', down(BNC, CD.neck_back_to_waist_b)) #back waist center
        BSH = B.addPoint('BSH', up(BWC, CD.neck_side_to_waist_b)) #shoulder height reference point
        BWS = B.addPoint('BWS', right(BWC, CD.waist_arc_b/2.0)) #back waist side reference point
        BSP = B.addPoint('BSP', highestP(onCircleAtX(BWC, CD.shoulder_tip_to_waist_back, BNC.x + CD.shoulder_tip_to_shoulder_tip_b/2.0))) #back shoulder point
        BNS = B.addPoint('BNS', leftmostP(onCircleAtY(BSP, CD.shoulder_length, BSH.y))) #back neck side
        BAP1 = B.addPoint('BAP1', )
        #BAP1 = B.addPoint('BAP1', lowestP(onCircleAtX(BNS, CD.neck_side_to_armfold_b, BNC.x + CD.across_back_b/2.0 + backBustEase/2.0))) #back underarm point      
        BUC = B.addPoint('BUC', (BNC.x, BAP1.y)) #back undearm center
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
        pnt = down(BUS, 0.2 * CD.armpit_to_waist_side)        
        b4 = B.addPoint('b4', right(pnt, 0.12 * CD.highbust_arc_b))
        #extend side seam
        b5 = B.addPoint('b5', right(BHS, 0.4 * CD.hip_arc_b/2.0)) #push out hem side
        b_H2 = B.addPoint('b_H2', onLineAtLength(b4, b5, distance(g4, a_H2))) #make back side equal to front side length
        #extend back center line
        b7 = B.addPoint('b7', down(b1, 1.5 * LOWER_LENGTH)) #begin back center line angle below back neck center
        b8 = B.addPoint('b8', left(BHC, 0.2 * CD.hip_arc_b/2.0)) #push out hem center
        #control points b/w b7 flex point center & b8 hem center
        b7.addOutpoint(down(b7, distance(b7, b8)/8.0))
        b8.addInpoint(polar(b8, distance(b7, b8), angleOfLine(b8, b7.outpoint)))        
        #new back hem center
        pnt = dPnt(intersectLines(b5, b_H2, b8, b8.inpoint)) # find point where center & side seam intersect
        b_H1 = B.addPoint('b_H1', onLineAtLength(pnt, b8, distance(pnt, b_H2))) #new back hem center
                      
               
        #adjust control points
        #b/w b4 underarm & BAP armscye curve & b3 shoulder point
        b4.addOutpoint(polar(b4, distance(b4, BAP)/2.0, angleOfLine(b4, b5) + ANGLE90))
        (BAP.inpoint.x, BAP.inpoint.y) = polar(BAP, distance(b4, BAP)/3.0, angleOfLine(BAP, BAP.inpoint))
        (BAP.outpoint.x, BAP.outpoint.y) = polar(BAP, distance(BAP, b3)/3.0, angleOfLine(BAP, BAP.outpoint))
        #create lower hem curve to Back B
        b_H1.addOutpoint(polar(b_H1, distance(b_H1, b_H2)/3.0, angleOfLine(b8, b_H1) - ANGLE90))
        b_H2.addInpoint(polar(b_H2, distance(b_H1, b_H2)/3.0, angleOfLine(b5, b_H2) + ANGLE90))
        #split lower hem curve
        orig_curve = points2List(b_H1, b_H1.outpoint, b_H2.inpoint, b_H2) 
        new_curves = splitCurveAtLength(orig_curve, curveLength(orig_curve)/2.0)
        updatePoint(b_H1.outpoint, new_curves[1])
        updatePoint(b_H2.inpoint, new_curves[5])
        b_H3 = B.addPoint('b_H3', new_curves[3])
        b_H3.addInpoint(new_curves[2])
        b_H3.addOutpoint(new_curves[4])
        
        #add upper hem curve to Back B        
        #create 1st half of upper hem curve
        first_curve = points2List(b_H1, b_H1.outpoint, b_H3.inpoint, b_H3)  
        outset_curve1 = outsetCurve(first_curve, HEM_DEPTH, -ANGLE90)
        b_h1 = B.addPoint('b_h1', outset_curve1[0])
        b_h2 = B.addPoint('b_h2', outset_curve1[3])
        b_h1.addOutpoint(outset_curve1[1])
        b_h2.addInpoint(outset_curve1[2]) 
        #create 2nd half of upper hem curve 
        second_curve = points2List(b_H3, b_H3.outpoint, b_H2.inpoint, b_H2)               
        outset_curve2 = outsetCurve(second_curve, HEM_DEPTH, -ANGLE90)
        b_h2.addOutpoint(outset_curve2[1])        
        b_h3 = B.addPoint('b_h3', outset_curve2[3])
        b_h3.addInpoint(outset_curve2[2]) 
        
        #add lining hem curve to Back B
        LINING_HEM_DEPTH = 0.75 * HEM_DEPTH
        first_curve = points2List(b_h1, b_h1.outpoint, b_h2.inpoint, b_h2)
        second_curve = points2List(b_h2, b_h2.outpoint, b_h3.inpoint, b_h3)
        #create 1st half of back lining hem curve
        outset_curve1 = outsetCurve(first_curve, LINING_HEM_DEPTH, -ANGLE90)
        b_l1 = B.addPoint('b_l1', outset_curve1[0])
        b_l2 = B.addPoint('b_l2', outset_curve1[3])
        b_l1.addOutpoint(outset_curve1[1])
        b_l2.addInpoint(outset_curve1[2])
        #create 2nd half of back lining hem curve                
        outset_curve2 = outsetCurve(second_curve, LINING_HEM_DEPTH, -ANGLE90)
        b_l2.addOutpoint(outset_curve2[1])     
        b_l3 = B.addPoint('b_l3', outset_curve2[3])
        b_l3.addInpoint(outset_curve2[2])
        
        #split back upper hem curve at lining width (b_l1.x)
        new_curves = splitCurveAtX(points2List(b_h1, b_h1.outpoint, b_h2.inpoint, b_h2), b_l1.x)
        updatePoint(b_h1.outpoint, new_curves[1])
        b_h4 = B.addPoint('b_h4', new_curves[3])        
        b_h4.addInpoint(new_curves[2])
        b_h4.addOutpoint(new_curves[4])
        updatePoint(b_h2.inpoint, new_curves[5])
        
        #create back tuck points for back lining
        tuck_depth = abs(b1.x - b_l1.x)
        back_neck_curve = points2List(b1, b1.inpoint, b2.outpoint, b2)
        b10 = B.addPoint('b10', onCurveAtX(back_neck_curve, b1.x + tuck_depth/2.0)) #split back neck curve at tuck depth
        b11 = B.addPoint('b11', mirror(b1, b10, type='vertical'))
        b12 = B.addPoint('b12', mirror(b11, b1, type='vertical'))
        b13 = B.addPoint('b13', midPoint(b1, b7)) #bottom of back lining tuck stitching      
        #extend back neck curve for back lining tuck
        new_back_neck_curve = splitCurveAtPoint(back_neck_curve, b10)
        b1.addOutpoint(mirror(b1, new_back_neck_curve[1], type='vertical'))
        b11.addInpoint(mirror(b1, new_back_neck_curve[2], type='vertical'))
        b11.addOutpoint(mirror(b11, b11.inpoint, type='vertical'))
        b12.addInpoint(mirror(b11, b1.outpoint, type='vertical'))             

        #---Shirt sleeve C---#
        #get front & back armcye length
        BACK_ARMSCYE_POINTS = points2List(b4, b4.outpoint, BAP.inpoint, BAP, BAP.outpoint, b3.inpoint, b3)
        FRONT_ARMSCYE_POINTS = points2List(g4, g4.outpoint, g5.inpoint, g5, g5.outpoint, g6.inpoint, g6)
        BACK_ARMSCYE_LENGTH = curveLength(BACK_ARMSCYE_POINTS)
        FRONT_ARMSCYE_LENGTH = curveLength(FRONT_ARMSCYE_POINTS)
        ARMSCYE_LENGTH = BACK_ARMSCYE_LENGTH + FRONT_ARMSCYE_LENGTH
        
        CAP_HEIGHT = ARMSCYE_LENGTH/3.0 #proportional 
        BICEP_CIRC = 1.2 * CD.arm_upper_circ #20% ease in bicep
        WRIST_CIRC = 1.15 * CD.arm_wrist_circ #15% ease in wrist        
        OVERSLEEVE_LENGTH = CD.arm_shoulder_tip_to_wrist #no ease
        UNDERSLEEVE_LENGTH = CD.arm_armpit_to_wrist #no ease

        c1 = C.addPoint('c1', (0,0)) #left side, top line, sleevecap back  - A
        c2 = C.addPoint('c2', down(c1, OVERSLEEVE_LENGTH)) #left side, wrist line, wrist back - B

        c3 = C.addPoint('c3', right(c1, BICEP_CIRC)) #right side, top line, sleevecap front  - C
        c4 = C.addPoint('c4', down(c3, OVERSLEEVE_LENGTH)) #right side, wrist line, wrist front -D

        c5 = C.addPoint('c5', up(c2, UNDERSLEEVE_LENGTH)) #left side, bicep line, bicep back - E
        c6 = C.addPoint('c6', up(c4, UNDERSLEEVE_LENGTH)) #right side, bicep line, bicep front - F
        c7 = C.addPoint('c7', midPoint(c5, c6)) #center of bicep line - J

        c8 = C.addPoint('c8', right(c1, BICEP_CIRC/2.0)) #center of top line - G
        c9 = C.addPoint('c9', dPnt((c7.x, c2.y))) #mid wrist - H

        c11 = C.addPoint('c11', right(c5, 0.25 * distance(c5, c7))) #left side, bicep line, back armscye reference - I
        c12 = C.addPoint('c12', left(c8, 0.5 * distance(c8, c1))) #left side, top line, back armscye reference - K
        c13 = C.addPoint('c13', midPoint(c11, c12)) #left side, midbicep line, back armscye reference - L

        c14 = C.addPoint('c14', left(c6, 0.25 * distance(c6, c7))) #front cap reference - M
        c15 = C.addPoint('c15', right(c8, 0.5 * distance(c8, c3))) #front cap reference - N
        c16 = C.addPoint('c16', midPoint(c14, c15)) #front cap reference - O

        c17 = C.addPoint('c17', leftmostP(onCircleAtY(c13, BACK_ARMSCYE_LENGTH - distance(c8, c13), c7.y))) #extend back bicep
        c18 = C.addPoint('c18', rightmostP(onCircleAtY(c16, FRONT_ARMSCYE_LENGTH - distance(c8, c16), c7.y))) #extend front bicep

        #Sleeve C control points
        c8.addInpoint(left(c8, distance(c8,c12)/2.0))
        c8.addOutpoint(right(c8, distance(c8,c15)/2.0))
        c13.addOutpoint(polar(c13, distance(c13, c8)/3.0, angleOfLine(c13, c8.inpoint)))
        c13.addInpoint(polar(c13, distance(c13, c17)/3.0, angleOfLine(c13.outpoint, c13)))
        c17.addOutpoint(right(c17, distance(c17, c13)/3.0))
        c16.addInpoint(polar(c16, distance(c16, c8)/3.0, angleOfLine(c16, c8.outpoint)))
        c16.addOutpoint(polar(c16, distance(c16, c18)/3.0, angleOfLine(c16.inpoint, c16)))
        c18.addInpoint(left(c18, distance(c18, c16)/3.0))

        #Split Sleeve
        c20 = C.addPoint('c20', (c8.x, c13.y))
        #c20.addInpoint(up(c20, 0.75 * distance(c20, c8)))
        #c20.addOutpoint(c20.inpoint)
        c7.addInpoint((c20))
        c7.addOutpoint((c20))
        #rotate c8 counterclockwise as c19
        c19 = C.addPoint('c19', c8)
        c19.addInpoint(c8.inpoint)
        #c19.addOutpoint(down(c8, distance(c8, c20)/4.0))
        c19.addOutpoint(down(c8, distance(c8, c20)))
        slashAndSpread(c13, angleOfDegree(-15), c19.outpoint, c19, c19.inpoint, c13.outpoint)
        #rotate c8 clockwise as c21
        c21 = C.addPoint('c21', mirror(c8, c19, type='vertical'))
        c21a = C.addPoint('c21a', mirror(c8, c19, type='vertical'))
        c21.addOutpoint(mirror(c8, c19.inpoint, type='vertical')) #reverse
        c21.addInpoint(mirror(c8, c19.outpoint, type='vertical')) #reverse
        slashAndSpread(c16, angleOfVector(c8, c16, c21), c16.inpoint)
        
        c22 = C.addPoint('c22', up(c2, distance(c7, c9)/4.0)) #straighten out sleeve under cuff area on left
        c23 = C.addPoint('c23', up(c4, distance(c7, c9)/4.0)) #straighten out sleeve under cuff area on right
        #b/w c22 back cuff line & c17 back bicep
        c22.addOutpoint(up(c22, distance(c22, c17)/2.0))
        c17.addInpoint(polar(c17, distance(c22, c17)/3.0, angleOfLine(c17, c22.outpoint))) 
        #b/w c23 front cuff line & c18 front bicep
        c23.addInpoint(up(c23, distance(c23, c18)/2.0))
        c18.addOutpoint(polar(c18, distance(c23, c18)/3.0, angleOfLine(c18, c23.inpoint)))

        #smooth cap curves
        updatePoint(c13, intersectLines(c20, c13, c13.inpoint, c13.outpoint))
        updatePoint(c16, intersectLines(c20, c16, c16.inpoint, c16.outpoint))

        #check sleeve cap length
        curve = points2List(c17, c17.outpoint, c13.inpoint, c13, c13.outpoint, c19.inpoint, c19)
        back_cap_length = curveLength(curve)
        curve = points2List(c21, c21.outpoint, c16.inpoint, c16, c16.outpoint, c18.inpoint, c18)
        front_cap_length = curveLength(curve)
        back_diff = back_cap_length - BACK_ARMSCYE_LENGTH
        front_diff = front_cap_length - FRONT_ARMSCYE_LENGTH
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
        back_curve = points2List(c22, c22.outpoint, c17.inpoint, c17)
        back_sleeve_length = distance(c2, c22) + curveLength(back_curve)
        front_curve = points2List(c23, c23.inpoint, c18.outpoint, c18)
        front_sleeve_length = distance(c4, c23) + curveLength(front_curve)
        diff = back_sleeve_length - front_sleeve_length
        if diff < 0.0:
            print 'lengthen sleeve back'
            updatePoint(c2, down(c2, -diff))
            updatePoint(c9, intersectLines(c7, c9, c2, c4))
        elif diff > 0.0:
            print 'lengthen sleeve front'
            updatePoint(c4, down(c4, diff))
            updatePoint(c9, intersectLines(c7, c9, c2, c4))
            
        #create the sleeve lining curve
        outset_line = outsetLine(c2, c4, LINING_HEM_DEPTH, -ANGLE90)
        c_l1 = C.addPoint('c_l1', outset_line[0])
        c_l2 = C.addPoint('c_l2', outset_line[1])
        #split line at c2.x
        c_l3 = C.addPoint('c_l3', onLineAtX(c_l1, c_l2, c2.x))
        #split line at c9.x
        c_l4 = C.addPoint('c_l4', onLineAtX(c_l1, c_l2, c9.x))        
        #split line at c4.x
        c_l5 = C.addPoint('c_l5', onLineAtX(c_l1, c_l2, c4.x))      
        
        
        #---Back Lining D---#
        #---Pocket E---#    
        #---Front Facing F---#
        #---Upper Front G---#
        #---Sleeve Front H---#

        #---Sleeve Facing I---#
        CUFF_HEIGHT = distance(c2, c22)
        CUFF_WIDTH = distance(c2, c4)
        CUFF_EASE = distance(c2, c22)/10.0
        i1 = C.addPoint('i1', c22) #top left facing point
        i2 = C.addPoint('i2', right(i1, CUFF_WIDTH)) #top right facing point
        i3 = C.addPoint('i3', c4) #middle right
        i4 = C.addPoint('i4', down(i3, CUFF_HEIGHT))
        i5 = C.addPoint('i5', right(i4, CUFF_EASE)) #bottom right
        i6 = C.addPoint('i6', left(i4, CUFF_WIDTH))
        i7 = C.addPoint('i7', left(i6, CUFF_EASE)) #bottom left
        i8 = C.addPoint('i8', left(i3, CUFF_WIDTH)) #middle left      
        
        #---Front Lining J---#        
        j1 = J.addPoint('j1', a2) #neck front side, pre-rotation
        j1.addOutpoint(a2.inpoint)         
        j2 = J.addPoint('j2', onLineAtLength(FSP, a2, distance(a2, FSP)/3.0))        
        angle1 = angleOfVector(a4, FBP, g2)         
        jD1 = J.addPoint('jD1', FBP) #new dartpoint        
        jD1.o = J.addPoint('jD1.o', onLineAtLength(g6, g1, distance(g6, g1)/3.0)) #1/3 along shoulder
        jD1.i = J.addPoint('jD1.i', rotate(FBP, jD1.o, angle1))
        foldDart(jD1, j1) #creates jD1.m as midpoint of tuck                     
        tuck_length = distance(jD1.i, FBP)/5.0
        j4 = J.addPoint('j4', onLineAtLength(jD1.i, jD1, tuck_length))
        j5 = J.addPoint('j5', onLineAtLength(jD1.o, jD1, tuck_length)) 
        j6 = J.addPoint('j6', a4) #Facing curve break point a4
        j6.addInpoint(a4.outpoint)        
    
        #---Front Outer Pocket K---#
           
        #---------------------------------------------#
        #---all points defined, create notches     ---#
        #---------------------------------------------#
        #notch 1 - Front Upper G armscye & Front Lining J armscye to Sleeve Front H sleevecap 
        notchG1 = G.addNotch('1', g5, angleOfLine(g5.inpoint, g5) - ANGLE90) 
        notchJ1 = J.addNotch('1', g5, angleOfLine(g5.inpoint, g5) - ANGLE90)
        new_curves = splitCurveAtLength(points2List(c18, c18.inpoint, c16.outpoint, c16, c16.inpoint, c21.outpoint, c21), curveLength(points2List(g4, g4.outpoint, g5.inpoint, g5)))
        notchH1 = H.addNotch('1', new_curves[3], angleOfLine(new_curves[2], new_curves[3]) + ANGLE90) 
        #notch 2 - Back B armscye & Back Lining D to Sleeve Back C sleevecap
        notchB2 = B.addNotch('2', BAP, angleOfLine(BAP.inpoint, BAP) + ANGLE90)
        notchD2 = D.addNotch('2', BAP, angleOfLine(BAP.inpoint, BAP) + ANGLE90)
        new_curves = splitCurveAtLength(points2List(c17, c17.outpoint, c13.inpoint, c13, c13.outpoint, c19.inpoint, c19), curveLength(points2List(b4, b4.outpoint, BAP.inpoint, BAP)))
        notchC2 = C.addNotch('2', new_curves[3], angleOfLine(new_curves[2], new_curves[3]) - ANGLE90)
        #notch 3 = Front Upper G shoulder & Front Lining J to Back B shoulder & Back Lining D shoulder
        length = 0.3 * distance(g1, g6)
        notchG3 = G.addNotch('3', onLineAtLength(g1, g6, length), angleOfLine(g1, g6) + ANGLE90) #Front Upper G shoulder
        notchJ3 = J.addNotch('3', onLineAtLength(j1, jD1.i, length), angleOfLine(j1, jD1.i) + ANGLE90) #Front Lining J shoulder
        notchB3 = B.addNotch('3', onLineAtLength(b2, b3, length), angleOfLine(b2, b3) - ANGLE90) #Back B shoulder
        notchD3 = D.addNotch('3', onLineAtLength(b2, b3, length), angleOfLine(b2, b3) - ANGLE90) #Back Lining D shoulder
        #notch 4 - Front Upper G dart & Front A upper chest curve, Front Lining J & Front Facing F
        notchG4 = G.addNotch('4', g2, angleOfLine(g2, g2.outpoint) - ANGLE90) #Front Upper G upper chest curve
        notchA4 = A.addNotch('4', a4, angleOfLine(a4, a4.outpoint) - ANGLE90) #Front A upper chest curve
        notchJ4 = J.addNotch('4', j6, angleOfLine(j6.inpoint, j6) - ANGLE90) #Front Lining J upper chest curve 
        notchF4 = F.addNotch('4', a4, angleOfLine(a4, a4.outpoint) - ANGLE90) #Front Facing F upper chest curve        
        #notch 5 - Front Upper G FBP & Front A FBP
        angle = angleOfLine(FBP, FBP.outpoint)
        notchG5 = G.addNotch('5', FBP, angle + ANGLE90) #Front Upper G FBP
        notchA5 = A.addNotch('5', FBP, angle - ANGLE90) #Front A FBP
        #notch 6 - Front A facing edge & Front Facing F edge
        notchA6 = A.addNotch('6', a17, angleOfLine(a17, a17.inpoint) + ANGLE90)
        notchF6 = F.addNotch('6', a17, angleOfLine(a17, a17.inpoint) + ANGLE90)
        #notch 7 = Front A facing edge & Front Facing F edge
        notchA7 = A.addNotch('7', a6, angleOfLine(a6, a6.inpoint) + ANGLE90)
        notchF7 = F.addNotch('7', a6, angleOfLine(a6, a6.inpoint) + ANGLE90) 
        #notch 8 = Front A facing edge & Front Facing F edge
        pnt = onLineAtLength(a6, a7, distance(a6, a7)/2.0)
        notchA8 = A.addNotch('8', pnt, angleOfLine(a6, a6.inpoint) + ANGLE90)
        notchF7 = F.addNotch('8', pnt, angleOfLine(a6, a6.inpoint) + ANGLE90)               
        #notch 9 = Front Upper G  & Front Lining J side to Back B  & Back Lining D side
        length = distance(b4, b5)/2.0
        pnt1 = onLineAtLength(b4, b5, length)
        angle1 = angleOfLine(b4, b5) - ANGLE90
        notchB9 = B.addNotch('9', pnt1, angle1)
        notchD9 = D.addNotch('9', pnt1, angle1)
        pnt2 = onLineAtLength(g4, g7, length)
        angle2 = angleOfLine(g4, g7) + ANGLE90
        notchG9 = G.addNotch('9', pnt2, angle2)
        notchJ9 = J.addNotch('9', pnt2, angle2)
        #notch 10 - Back B to Back B
        curve = points2List(b7, b7.outpoint, b8.inpoint, b8) 
        length = curveLength(curve)/2.0
        new_curves = splitCurveAtLength(curve, length)
        angle = angleOfLine(new_curves[2], new_curves[3]) + ANGLE90
        notchB10 = B.addNotch('10', new_curves[3], angle)
        #notch 11 - Sleeve Back C to Sleeve Front H at curve in center line
        angle = angleOfLine(c7, c7.inpoint)
        notchC11 = C.addNotch('11', c7, angle + ANGLE90)
        notchH11 = H.addNotch('11', c7, angle - ANGLE90)
        #notch 12 = Sleeve Back C to Sleeve Front H along underarm seam
        curve1 = points2List(c17, c17.inpoint, c22.outpoint, c22) 
        length = curveLength(curve1)/2.0
        new_curves1 = splitCurveAtLength(curve1, length)
        angle1 = angleOfLine(new_curves1[2], new_curves1[3])
        curve2 = points2List(c18, c18.outpoint, c23.inpoint, c23)         
        new_curves2 = splitCurveAtLength(curve2, length)
        angle2 = angleOfLine(new_curves2[2], new_curves2[3])        
        notchC12 = C.addNotch('12', new_curves1[3], angle1 + ANGLE90)
        notchH12 = H.addNotch('12', new_curves2[3], angle2 - ANGLE90)
        #notch 13 = Sleeve Back C to Cuff L at wrist
        length = distance(c2, c9)/2.0
        pnt = onLineAtLength(c2, c9, length)
        angle = angleOfLine(c2, c9) 
        notchC13 = C.addNotch('13', onLineAtLength(c2, c9, length), angleOfLine(c2, c9) + ANGLE90)
        notchL13 = L.addNotch('13', onLineAtLength(i8, i3, length), angleOfLine(i8, i3) - ANGLE90)
        #notch 14 = Sleeve Front H to Inner Cuff L at wrist
        notchH14 = H.addNotch('14', onLineAtLength(c4, c9, length), angleOfLine(c4, c9) - ANGLE90)
        notchL14 = L.addNotch('14', onLineAtLength(i3, i8, length), angleOfLine(i3, i8) + ANGLE90)
        #notch 15 = Inner Cuff L to Outer Cuff I at cuff edge
        notchL15 = L.addNotch('15', dPnt(midPoint(i4, i6)), angleOfLine(i4, i6) - ANGLE90)
        notchI15 = I.addNotch('15', midPoint(i4, i6), angleOfLine(i4, i6) - ANGLE90)     
        

        #---------------------------------------------#
        #---all points defined, draw pattern pieces---#
        #---------------------------------------------#

        #draw Front A
        pnt1 = dPnt(midPoint(a11, FWC))
        A.setLabelPosition(pnt1)
        A.setLetter(up(pnt1, distance(a11, FWC)/4.0), scaleby=10.0)
        aG1 = dPnt(FUC)
        aG2 = dPnt(FHC)
        A.addGrainLine(aG1, aG2)
        A.addGridLine(['M', FUC, 'L', FUS1, 'M', FBC, 'L', FBP, 'L', FBS, \
        'M', FWC, 'L', FWS1, 'M', FUS, 'L', FWS2, \
        'M', FNC, 'L', FHC, 'L', FHS, \
        'M', FUS, 'L', FAP, 'L', FSP, \
        'L', FNS, 'C', FNC, 'L', a_H1, 'C', a_H3, 'C', a_H4, 'C', a_H2, \
        'M', FBP, 'L', a3, \
        'M', a_H2, 'L', a12, 'L', g4, 'C', g5, 'C', g6, 'L', g1, 'C', g2, 'C', FBP, 'L', a11, 'L', a12, \
        'M', a4, 'L', a_H3, \
        'M', a11, 'L', a_h4, 'C', a_h2, \
        'M', a_p1, 'C', a_p3, 'C', a_p2, \
        'M', a_l1, 'C', a_l2])
        A.addFoldLine(['M', a_h3, 'C', a_h4])
        pth = (['M', a6, 'L', a_h5, 'L', a_h1, 'C', a_h3, 'L', a_H3, 'C', a_H4, 'L', a11 , 'L', FBP, 'C', a4, 'C', a2, 'C', a15, 'L', a16, 'C', a17, 'C', a6])     
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        #draw Back B
        pnt1 = dPnt((distance(BSH, BNS)/2.0, distance(BNC, BUC)/2.0))
        B.setLabelPosition((pnt1))
        B.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        bG1 = dPnt((distance(BSH, BNS)/4.0, BUC.y))
        bG2 = dPnt(down(bG1, distance(BNC, BHC)/2.0))
        B.addGrainLine(bG1, bG2)
        B.addGridLine(['M', BNS, 'L', BSH, 'L', BWC, 'L', BWS, \
        'M', BUC, 'L', BUS1, \
        'M', BNC, 'L', BHC, 'L', BHS, 'L', BWS, 'L', BUS, 'C', BAP, 'C', BSP, 'L', BNS, 'C', BNC, \
        'M', b_l1, 'C', b_l2, 'C', b_l3])
        pth = (['M', b1, 'L', b7, 'C', b8, 'L', b_H1, 'C', b_H3, 'C', b_H2, 'L', b4, 'C', BAP, 'C', b3, 'L', b2, 'C', b1])
        B.addFoldLine(['M', b_h1, 'C', b_h4, 'C', b_h2, 'C', b_h3])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        #draw Sleeve Back C
        pnt1 = dPnt(down(c5, distance(c7, c9)/6.0))
        C.setLetter((pnt1.x, pnt1.y), scaleby=10.0)
        C.setLabelPosition(down(pnt1, distance(pnt1, c9)/6.0))
        cG1 = dPnt((c19.inpoint.x, c11.y))
        cG2 = down(cG1, 0.75 * distance(c7, c9))
        C.addGrainLine(cG1, cG2)
        C.addGridLine(['M', c1, 'L', c2, 'L', c4, 'L', c3, 'L', c1, \
        'M', c13, 'L', c16, \
        'M', c5, 'L', c6, \
        'M', c8, 'L', c9, \
        'M', i1, 'L', i2, 'L', i3, 'L', i5, 'L', i7, 'L', i8, 'L', i1, \
        'M', c_l3, 'L', c_l4, 'L', c_l5])
        pth = (['M', c19, 'C', c7, 'L', c9, 'L', c2, 'L', c22, 'C', c17, 'C', c13, 'C', c19])
        C.addFoldLine(['M', c_l3, 'L', c_l4])
        C.addSeamLine(pth)
        C.addCuttingLine(pth)
        
        #draw Back Lining D
        pnt1 = dPnt((distance(BSH, BNS)/2.0, distance(BNC, BUC)/2.0))
        D.setLabelPosition((pnt1))
        D.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        dG1 = dPnt((distance(BSH, BNS)/4.0, BUC.y))
        dG2 = dPnt(down(dG1, 0.5 * distance(BNC, BHC)))
        D.addGrainLine(dG1, dG2)
        D.addFoldLine(['M', b1, 'L', b13, \
        'M', b_l1, 'C', b_l2, 'C', b_l3])
        pth = (['M', b1, 'C', b11, 'C', b12, 'L', b_h4, 'C', b_h2, 'C', b_h3, 'L', b4, 'C', BAP, 'C', b3, 'L', b2, 'C', b1])
        D.addSeamLine(pth)
        D.addCuttingLine(pth)        

        #draw Pocket Lining E
        pnt1 = dPnt((a12.x + distance(a12, a11)/5.0, a12.y + distance(a12, a_h2)/2.0))
        E.setLetter((pnt1.x, pnt1.y), scaleby=10.0)
        E.setLabelPosition((a12.x + distance(a12, a11) / 2.0, a12.y + abs(a12.y - a_h1.y) / 6.0))
        eG1 = dPnt((a12.x + 0.75 * distance(a12, a11), a11.y + abs(a11.y - a_h1.y) / 4.0))
        eG2 = down(eG1, 0.45 * distance(a11, a_h4))
        E.addGrainLine(eG1, eG2)
        pth =(['M', a11, 'L', a_p3, 'C', a_p2, 'L', a12, 'L', a11])
        E.addSeamLine(pth)
        E.addCuttingLine(pth)

        #draw Front Facing F
        F.setLetter((FNC.x, FUC.y), scaleby=8.0)
        F.setLabelPosition((FNC.x - 25, FUC.y + 50))
        fG1 = dPnt(onLineAtLength(a3, a6, distance(a3, a6)/4.0))
        fG2 = down(fG1, 0.75 * distance(a3, a_H1))
        F.addGrainLine(fG1, fG2)
        pth =(['M', a4, 'C', a2, 'C', a15, 'L', a16, 'C', a17, 'C', a6, 'L', a_h5, 'L', a_h1, 'C', a_h3, 'L', a4])
        F.addSeamLine(pth)
        F.addCuttingLine(pth)

        #draw Upper Front G
        pnt1 = dPnt(midPoint(g5, FBP))
        G.setLetter((pnt1.x, pnt1.y), scaleby=10.0)
        G.setLabelPosition((pnt1.x, pnt1.y + 50))
        gG1 = dPnt((pnt1.x - 50, FAP.y))
        gG2 = down(gG1, 0.75 * distance(FAP, a11))
        G.addGrainLine(gG1, gG2)        
        pth =(['M', g2, 'C', FBP, 'L', a11, 'L', a_p3, 'C',  a_p2, 'L', a12, 'L', g4, 'C', g5, 'C', g6, 'L', g1, 'C', g2])
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
        pth = (['M', c21, 'C', c16, 'C', c18, 'C', c23, 'L', c4, 'L', c9, 'L', c7, 'C', c21])
        H.addFoldLine(['M', c_l4, 'L', c_l5])
        H.addSeamLine(pth)
        H.addCuttingLine(pth)

        #draw Sleeve - Outser Cuff I
        offsety = distance(i1, i8)/3.0
        offsetx = distance(i1, i2)/8.0
        pnt1 = dPnt((i8.x + offsetx, i8.y + 2 * offsety))
        pnt2 = dPnt((i8.x + 2 * offsetx, i8.y + offsety))
        pnt3 = dPnt((i8.x + 4 * offsetx, i8.y + offsety))
        I.setLetter((pnt1.x, pnt1.y), scaleby=8.0)
        I.setLabelPosition(pnt2)
        iG1 = pnt3
        iG2 = down(iG1, 0.5 * distance(i8, i6))
        I.addGrainLine(iG1, iG2)
        pth = (['M', i3, 'L', i8])
        I.addFoldLine(pth)
        pth = (['M', i1, 'L', i2, 'L', i3, 'L', i5, 'L', i7, 'L', i8, 'L', i1])
        I.addSeamLine(pth)
        I.addCuttingLine(pth)
        
        #draw Front Lining J
        pnt1 = dPnt((jD1.i.x,FBP.y))
        J.setLetter((pnt1.x, pnt1.y), scaleby=10.0)
        J.setLabelPosition((pnt1.x, pnt1.y + 100))
        jG1 = dPnt((jD1.o.x, FBP.y))
        jG2 = down(jG1, 0.75 * distance(FBP, a_h2))
        J.addGrainLine(jG1, jG2) 
        J.addFoldLine(['M', jD1.o, 'L', j5, 'M', jD1.i, 'L', j4, \
        'M', a_l1, 'C', a_l2])
        pth =(['M', j1, 'C', j6, 'L', a_h3, 'C', a_h4, 'C', a_h2, 'L', g4, 'C', g5, 'C', g6, 'L', jD1.o, 'L', jD1.m, 'L', jD1.i, 'L', j1])
        J.addSeamLine(pth)
        J.addCuttingLine(pth)  
        
        #draw Lower Front K
        pnt1 = dPnt(midPoint(a12, FHS))
        K.setLetter((pnt1.x, pnt1.y), scaleby=10.0)           
        K.setLabelPosition(down(pnt1, distance(pnt1, a12)/2.0))
        kG1 = dPnt(right(a12, 0.75 * distance(a12, a11)))
        kG2 = dPnt(down(kG1, distance(a12, a_H2)))
        K.addGrainLine(kG1, kG2)
        K.addFoldLine(['M', a_h4, 'C', a_h2])
        pth = (['M', a11, 'L', a_H4, 'C', a_H2, 'L', a12, 'L', a11])
        K.addSeamLine(pth)
        K.addCuttingLine(pth) 
               
        #draw Sleeve - Inner Cuff L
        offsety = distance(i8, i6)/3.0
        offsetx = distance(i8, i3)/8.0
        pnt1 = dPnt((i8.x + offsetx, i8.y + 2 * offsety))
        pnt2 = dPnt((i8.x + 2 * offsetx, i8.y + offsety))
        pnt3 = dPnt((i8.x + 4 * offsetx, i8.y + offsety))
        L.setLetter((pnt1.x, pnt1.y), scaleby=8.0)
        L.setLabelPosition(pnt2)
        lG1 = pnt3
        lG2 = down(lG1, 0.5 * distance(i8, i6))
        L.addGrainLine(lG1, lG2)
        pth = (['M', i8, 'L', i3, 'L', i5, 'L', i7, 'L', i8])
        L.addSeamLine(pth)
        L.addCuttingLine(pth)      


        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

