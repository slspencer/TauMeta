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
        self.setInfo('patternNumber', 'Coat_W_Topper')
        self.setInfo('patternTitle', 'Topper Coat')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'S.L.Spencer')
        self.setInfo('patternmakerName', 'S.L.Spencer')
        self.setInfo('description', """TTopper Coat""")
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
        A = coat.addPiece('Lower Front', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = coat.addPiece('Back', 'B', fabric = 2, interfacing = 0, lining = 0)
        C = coat.addPiece('Sleeve Back', 'C', fabric = 2, interfacing = 0, lining = 0)
        D = coat.addPiece('Welt', 'D', fabric = 2, interfacing = 0, lining = 0)
        E = coat.addPiece('Pocket', 'E', fabric = 2, interfacing = 0, lining = 0)
        F = coat.addPiece('Front Facing', 'F', fabric = 2, interfacing = 0, lining = 0)
        G = coat.addPiece('Upper Front', 'G', fabric = 2, interfacing = 0, lining = 0)
        H = coat.addPiece('Sleeve Front', 'H', fabric = 2, interfacing = 0, lining = 0)
        I = coat.addPiece('Sleeve Facing', 'I', fabric = 2, interfacing = 0, lining = 0)

        #---Bodice Lower Front A---#
        FNC = A.addPoint('FNC', (0.0, 0.0)) #front neck center
        FWC = A.addPoint('FWC', down(FNC, CD.front_waist_length)) #front waist center
        FBC = A.addPoint('FBC', up(FWC, CD.bust_length)) #bust center
        FBP = A.addPoint('FBP', left(FBC, CD.bust_distance/2.0)) #bust point
        #FSP = A.addPoint('FSP', leftmostP(intersectCircles(FWC, CD.front_shoulder_balance, FNC, CD.front_shoulder_width))) #front shoulder point
        FSP = A.addPoint('FSP', highestP(onCircleAtX(FWC, CD.front_shoulder_balance, FNC.x - CD.front_shoulder_width/2.0))) #front shoulder tip
        FNS = A.addPoint('FNS', highestP(intersectCircles(FSP, CD.shoulder, FBP, CD.bust_balance))) #front neck point
        FAS = A.addPoint('FAS', lowestP(onCircleAtX(FNS, CD.front_underarm_balance, FNC.x - CD.across_chest/2.0))) #front underarm point
        FAC = A.addPoint('FAC', (FNC.x, FAS.y)) #front undearm center
        FUS1 = A.addPoint('FUS1', left(FAC, CD.front_underarm/2.0)) #front underarm side
        #TODO: create function onCircleAtTangentOfPoint()
        FBS = A.addPoint('FBS', leftmostP(onCircleTangentFromOutsidePoint(FBP, CD.front_bust/2.0 - distance(FBC, FBP), FUS1))) #bust side is where line from bust point is perpendicular to line through FUS1
        FUS = A.addPoint('FUS', onLineAtLength(FUS1, FBS, 0.13 * CD.side)) #adjusted front underarm side on line FUS1-10
        FWS1 = A.addPoint('FWS1', left(FWC, CD.front_waist/2.0)) #temporary front waist side 1 - on waist line
        FWS2 = A.addPoint('FWS2', onLineAtLength(FUS1, FBS, CD.side)) #temporary front waist side 2 - on side seam

        #front waist dart
        totalDartAngle = abs(angleOfVector(FWS1, FBP, FWS2))
        frontWaistDartAngle = totalDartAngle/2.0
        bustDartAngle = totalDartAngle/2.0
        FD1 = A.addPoint('FD1', (FBP)) #front waist dart point
        FD1.i = A.addPoint('FD1.i', onRayAtY(FBP, ANGLE90 - frontWaistDartAngle/2.0, FWC.y)) #front waist dart inside leg
        FD1.o = A.addPoint('FD1.o', onRayAtY(FBP, ANGLE90 + frontWaistDartAngle/2.0, FWC.y)) #front waist dart outside leg
        #FD1.m = A.addPoint('FD1.m', dPnt((FBP.x, FWC.y))) #below bust point at waist
        FD1.m = A.addPoint('FD1.m', midPoint(FD1.i, FD1.o)) #below bust point at waist
        #bust dart
        FD2 = A.addPoint('FD2', (FBP)) #bust dart point
        FD2.i = A.addPoint('FD2.i', intersectLineRay(FUS1, FBS, FBP, ANGLE180 + bustDartAngle/2.0)) #bust dart inside leg
        FD2.o = A.addPoint('FD2.o', polar(FBP, distance(FBP, FD2.i), ANGLE180 - bustDartAngle/2.0)) #bust dart outside leg
        FD2.m = A.addPoint('FD2.m', intersectLines(FBC, FBP, FBS, FUS)) #intersect bust line & side seam
        #TODO: create function pivot(pivot_point, rotation_angle, point_to_pivot)

        #finalize front waist side
        remainingSideSegment = distance(FUS, FWS2) - distance(FUS, FD2.i)
        remainingWaistSegment = distance(FWC, FWS1) - distance(FWC, FD1.i)
        FWS = A.addPoint('FWS', leftmostP(intersectCircles(FD2.o, remainingSideSegment, FD1.o, remainingWaistSegment))) #front waist side created after all darts defined

        #create curve at dart base
        ##adjustDartLength(FWS, FD1, FWC, extension=0.25) #smooth waistline curve from FWS to FWC at dart
        foldDart(FD1, FWC) #creates FD1.m,FD1.oc,FD1.ic; dart folds in toward waist center FWC
        #do not call adjustDartLength(FWS1,FD2,FUS) -- bust dart FD2 is not on a curve
        foldDart(FD2, FUS) #creates FD2.m,FD2.oc,FD2.ic; dart folds up toward underarm side FUS
        #adjust FD1 & FD2 away from FBP bust point
        (FD1.x, FD1.y) = down(FD1, distance(FD1, FD1.i)/7.0)
        (FD2.x, FD2.y) = left(FD2, distance(FD2, FD2.i)/7.0)

        #Bodice Lower Front A hip extension
        FHC = A.addPoint('FHC', down(FWC, CD.front_hip_height)) #front hip center
        FWS3 = A.addPoint('FWS3', left(FD1.o, distance(FD1.o, FWS))) #front waist side
        FHM = A.addPoint('FHM', (FD1.x, FHC.y)) #reflect waist dart point on hip line for 'fish dart'
        FHS1 = A.addPoint('FHS1', left(FHC, CD.front_hip/2.0)) #front hip side 1
        FHS2 = A.addPoint('FHS2', polar(FD1.o, distance(FD1.o, FHS1), angleOfLine(FD1.o, FHS1) + angleOfVector(FWS2, FD1.o, FWS))) #front hip side 2
        FHS = A.addPoint('FHS', onLineAtLength(FWS, FHS2, CD.side_hip_height)) #front hip side
        FD1.d = A.addPoint('FD1.d', up(FHM, distance(FHM, FD1.m)/7.0)) #front waist dart point at hip

        #adjust block to coat points
        a1 = A.addPoint('a1', down(FNC, 0.03*CD.front_waist_length)) #new front neck center
        a2 = A.addPoint('a2', onLineAtLength(FNS, FSP, distance(FNC, a1))) #new front neck point
        a3 = A.addPoint('a3', left(FSP, distance(FNC, a1))) #new shoulder point
        a4 = A.addPoint('a4', left(FAS, distance(FNC, a1))) #new armscye curve
        a5 = A.addPoint('a5', onLineAtLength(FBS, FBP, -0.05*CD.front_bust)) #new underarm point - out 0.5in & down 1in
        a6 = A.addPoint('a6', onLineAtLength(FD2.i, FBP, -distance(FBS, a5))) #new bust dart inside
        a7 = A.addPoint('a7', onLineAtLength(FD2.o, FBP, -distance(FBS, a5))) #new bust dart outside
        a8 = A.addPoint('a8', onLineAtLength(FWS, FD1.o, -distance(FBS, a5))) #new waist side
        a9 = A.addPoint('a9', onLineAtLength(FHS, FHM, -distance(FBS, a5))) #new hip side

        #Bodice Lower Front A control points
        #b/w FNS front neck point & FNC front neck center
        FNS.addOutpoint(down(FNS, abs(FNC.y - FNS.y)/2.0))
        FNC.addInpoint(left(FNC, 0.75 * abs(FNC.x - FNS.x)))
        #b/w FD1.o waist dart outside leg & FWS front waist side - short control handles
        FD1.o.addOutpoint(polar(FD1.o, distance(FD1.o, FWS)/6.0, angleOfLine(FD1.o, FD1) - (angleOfLine(FD1.i, FD1) - ANGLE180))) #control handle forms line with FWC,FD1.i
        FWS.addInpoint(polar(FWS, distance(FD1.o, FWS)/6.0, angleOfLine(FWS, FD1.o.outpoint))) #FWS control handle points to FD1.o control handle
        #b/w FAS front underarm point & FSP front shoulder point
        FSP.addInpoint(polar(FSP, distance(FAS, FSP)/6.0, angleOfLine(FSP, FNS) + ANGLE90)) #short control handle perpendicular to shoulder seam
        FAS.addOutpoint(polar(FAS, distance(FAS, FSP)/3.0, angleOfLine(FAS, FNS))) #control handle points to front neck point
        #b/w FUS front underarm side & FAS front underarm point
        FAS.addInpoint(polar(FAS, distance(FUS, FAS)/3.0, angleOfLine(FNS, FAS)))
        FUS.addOutpoint(polar(FUS, distance(FUS, FAS)/3.0, angleOfLine(FD2.i, FUS) + ANGLE90)) #control handle is perpendicular to side seam at underarm
        #b/w a2 new neck point & a1 new front neck center
        a1.addInpoint(left(a1, 0.75 * abs(a1.x - a2.x)))
        a2.addOutpoint(polar(a2, abs(a1.y - a2.y)/2.0, angleOfLine(a3, a2) + ANGLE90))
        #b/w a5 new underarm & a4 armscye curve & a3 new shoulder tip
        a5.addOutpoint(polar(a5, distance(a5, a4)/3.0, angleOfLine(a6, a5) + ANGLE90))
        a4.addInpoint(polar(a4, distance(a5, a4)/3.0, angleOfLine(a2, a4)))
        a4.addOutpoint(polar(a4, distance(a4, a3)/3.0, angleOfLine(a4, a2)))
        a3.addInpoint(polar(a3, distance(FAS, a3)/6.0, angleOfLine(a2, a3) - ANGLE90)) #short control handle, perpendicular to shoulder seam

        #---Bodice Back B---#
        b1 = B.addPoint('b1', (0.0, 0.0)) #back neck center
        b2 = B.addPoint('b2', down(b1, CD.back_waist_length)) #back waist center
        b3 = B.addPoint('b3', up(b2, CD.back_shoulder_height)) #shoulder height reference point
        b4 = B.addPoint('b4', right(b2, CD.back_waist/2.0)) #back waist side reference point
        #b5 = B.addPoint('b5', rightmostP(intersectCircles(b2, CD.back_shoulder_balance, b1, CD.back_shoulder_width))) #back shoulder point
        b5 = B.addPoint('b5', highestP(onCircleAtX(b2, CD.back_shoulder_balance, b1.x + CD.back_shoulder_width/2.0))) #back shoulder tip
        b6 = B.addPoint('b6', leftmostP(onCircleAtY(b5, CD.shoulder, b3.y))) #back neck point
        b7 = B.addPoint('b7', lowestP(onCircleAtX(b6, CD.back_underarm_balance, b1.x + CD.across_back/2.0))) #back underarm point
        b8 = B.addPoint('b8', (b1.x, b7.y)) #back undearm center
        b9 = B.addPoint('b9', right(b8, CD.back_underarm/2.0)) #back underarm side reference point
        b10 = B.addPoint('b10', down(b9, distance(FUS1, FUS))) #adjusted back underarm side
        bD1 = B.addPoint('bD1', intersectLines(b2, b5, b8, b9)) #back waist dart point is at underarm height
        b12 = B.addPoint('b12', dPnt((bD1.x, b2.y))) # below dart point at waist
        bD1.i = B.addPoint('bD1.i', left(b12, distance(b2, b12)/5.0)) #dart inside leg
        bD1.o = B.addPoint('bD1.o', right(b12, distance(b12, bD1.i))) #dart outside leg
        b11 = B.addPoint('b11',  rightmostP(intersectCircles(b10, distance(FUS, FD2.i) + distance(FD2.o, FWS), bD1.o, CD.back_waist/2.0 - distance(b2, bD1.i)))) #back waist side

        #create curve at dart base
        ##adjustDartLength(FWS, FD1, FWC, extension=0.25) #smooth waistline curve from FWS to FWC at dart
        foldDart(bD1, b2) #creates bD1.m, bD1.oc, bD1.ic; dart folds toward waist center b2

        b13 = B.addPoint('b13', down(b2, CD.back_hip_height)) #back hip center
        b14 = B.addPoint('b14', right(bD1.o, distance(bD1.o, b11))) #back waist side
        b15 = B.addPoint('b15', (bD1.x, b13.y)) # back waist dart at hip line
        b16 = B.addPoint('b16', right(b13, CD.back_hip/2.0)) #temporary back hip side
        b17 = B.addPoint('b17', polar(bD1.o, distance(bD1.o, b16), angleOfLine(bD1.o, b16) - angleOfVector(b14, bD1.o, b11))) #temporary back waist side
        b18 = B.addPoint('b18', onLineAtLength(b11, b17, CD.side_hip_height)) #back hip side
        bD1.d = B.addPoint('bD1.d', up(b15, distance(b15, b12)/7.0)) # back waist dart point at hip

        #adjust block to topper points
        b19 = B.addPoint('b19', down(b1, 0.03*CD.back_waist_length)) #new back neck center
        b20 = B.addPoint('b20', onLineAtLength(b6, b5, distance(FNC, a1))) #new back neck point
        b21 = B.addPoint('b21', right(b5, distance(FNC, a1))) #new shoulder point
        b22 = B.addPoint('b22', right(b7, distance(FNC, a1))) #new armscye curve
        b23 = B.addPoint('b23', polar(b10, 0.05*CD.back_underarm, angleOfLine(b11, b10) + ANGLE90)) #new underarm side
        b24 = B.addPoint('b24', onLineAtLength(b11, bD1.o, -distance(b23, b10))) #new waist side
        b25 = B.addPoint('b25', onLineAtLength(b18, b15, -distance(b23, b10))) #new hip side

        #Bodice Back B control points
        #b/w b6 back neck point & b1 back neck center
        b1.addInpoint(right(b1, 0.75 * abs(b1.x - b6.x)))
        b6.addOutpoint(polar(b6, abs(b6.y - b1.y)/2.0, angleOfLine(b6, b5) + ANGLE90)) #perpendicular to shoulder seam
        #b/w b10 underarm point & b7 underarm curve
        b10.addOutpoint(polar(b10, distance(b10, b7)/3.0, angleOfLine(b10, b11) + ANGLE90)) #perpendicular to side seam
        b7.addInpoint(polar(b7, distance(b10, b7)/3.0, angleOfLine(b6, b7)))
        #b/w b7 underarm curve & b6 shoulder point
        b7.addOutpoint(polar(b7, distance(b7, b5)/3.0, angleOfLine(b7, b6)))
        b5.addInpoint(polar(b5, distance(b7, b5)/6.0, angleOfLine(b6, b5) + ANGLE90)) #short control handle, perpendicular to shoulder seam
        #b/w bD1.o waist dart outside leg & b11 waist side
        bD1.o.addOutpoint(polar(bD1.o, distance(bD1.o, b11)/6.0, angleOfLine(bD1.o, bD1) + ANGLE180 - angleOfVector(b2, bD1.i, bD1))) #short control handle, forms line with control handle for inside leg
        b11.addInpoint(polar(b11, distance(bD1.o, b11)/3.0, angleOfLine(b10, b11) + angleOfVector(FD2.o, FWS, FWS.inpoint))) #forms line with control handle for FWS front waist
        #b/w b19 new neck point & b20 new front neck center
        b19.addInpoint(right(b19, 0.75 * abs(b19.x - b20.x)))
        b20.addOutpoint(polar(b20, abs(b19.y - b20.y)/2.0, angleOfLine(b20, b19.inpoint)))
        #b/w b23 new underarm & b22 armscye curve & b21 new shoulder tip
        b23.addOutpoint(polar(b23, distance(b23, b22)/3.0, angleOfLine(b24, b23) - ANGLE90))
        b22.addInpoint(polar(b22, distance(b23, b22)/3.0, angleOfLine(b20, b22)))
        b22.addOutpoint(polar(b22, distance(b22, b21)/3.0, angleOfLine(b22, b20)))
        b21.addInpoint(polar(b21, distance(b22, b21)/6.0, angleOfLine(b20, b21) + ANGLE90)) #short control handle, perpendicular to shoulder seam

        #Adjust Lower Front A
        #extend front collar
        back_neck_curve = points2List(b19, b19.inpoint, b20.outpoint, b20)
        a10 = A.addPoint('a10', polar(a2, curveLength(back_neck_curve), angleOfLine(a2.outpoint, a2))) #front neck extension point 1
        a11 = A.addPoint('a11', polar(a10, 0.13 * CD.front_waist_length, angleOfLine(a2, a10) + ANGLE90)) #front neck extension point 2
        front_neck_curve = points2List(a1, a1.inpoint, a2.outpoint, a2)
        curve_length = curveLength(front_neck_curve)
        a12 = A.addPoint('a12', onCurveAtLength(front_neck_curve, curve_length/3.0)) #divide front neck curve 1/3rd along length
        a13 = A.addPoint('a13', dPnt(a12)) #a13 won't rotate
        a14 = A.addPoint('a14', polar(a11, distance(a2, a10), angleOfLine(a10, a2))) #front neckextension point 3
        a15 = A.addPoint('a15', right(a1, 0.1 * CD.front_waist_length)) #right of a1 front neck center
        a16 = A.addPoint('a16', right(FHC, distance(a1, a15))) #right of FHC front hip center
        a17 = A.addPoint('a17', a2) #copy neck point to use in collar

        #b/w a2 neck point, a12/a13 split point, a1 front neck center
        (a1.inpoint.x, a1.inpoint.y) = left(a1, distance(a1, a12)/3.0) #adjust a1.inpoint
        (a2.outpoint.x, a2.outpoint.y) = polar(a2, distance(a2, a12)/3.0, angleOfLine(a3, a2) + ANGLE90) #adjust a1.inpoint
        a17.addInpoint(a2.outpoint)
        a17.addOutpoint(polar(a17, distance(a17, a10)/3.0, angleOfLine(a17.inpoint, a17)))
        a10.addInpoint(polar(a10, distance(a17, a10)/3.0, angleOfLine(a10, a11) + ANGLE90))
        a12.addInpoint(polar(a12, distance(a12, a2)/3.0, angleOfLine(a1.inpoint, a2.outpoint)))
        a13.addOutpoint(a12.inpoint)
        #b/w a11 extended collar top corner & a14 extended collar top midpoint
        a11.addOutpoint(polar(a11, distance(a11, a14)/3.0, angleOfLine(a10, a11) + ANGLE90))
        a14.addInpoint(polar(a14, distance(a11, a14)/3.0, angleOfLine(a17, a17.outpoint)))
        #b/w a14 extended collar midpoint & a15 extended collar neck point
        a14.addOutpoint(polar(a14, distance(a14, a15)/3.0, angleOfLine(a17.outpoint, a17)))
        a15.addInpoint(up(a15, distance(a14, a15)/3.0))
        #a13.addOutpoint(polar(a13, distance(a13, a1)/3.0, angleOfLine(a12.inpoint, a12)))

        #close bust dart
        pivot = FBP
        angle = angleOfVector(a6, FBP, a7)
        slashAndSpread(pivot, -angle, a6, a5, a5.outpoint, a4.inpoint, a4, a4.outpoint, a3.inpoint, a3, a2, a2.outpoint, a12.inpoint, a12) #rotate counterclockwise, so angle < 0
        #lower underarm
        LOWER_LENGTH = 0.2 * distance(a5, a8) #20% side length
        a18 = A.addPoint('a18', (a5.x - 0.07 * CD.front_underarm, a5.y + LOWER_LENGTH)) #new front underarm - out 7% front underarm, down 40% side length
        #extend side seam
        a19 = A.addPoint('a19', left(a9, 2 * abs(a18.x - a5.x))) #push out hem side
        a20 = A.addPoint('a20', extendLine(a18, a19, 1.5 * LOWER_LENGTH)) #extend hem side down
        #extend front center line
        pnt = dPnt(intersectLines(a19, a20, FNC, FHC)) # find point where center line & side seam intersect
        a21 = A.addPoint('a21', onLineAtLength(pnt, FNC, distance(pnt, a20))) #new front hem center
        #split front into 2 pieces
        WELT_HEIGHT = 0.15 * CD.front_waist_length
        a22 = A.addPoint('a22', onLineAtLength(a13, FBP, FWC.y + WELT_HEIGHT)) #pocket corner point
        a23 = A.addPoint('a23', onLineAtLength(a19, a18, distance(a9, a8)/3.0)) #side split point
        #collar
        a24 = A.addPoint('a24', (a16.x, a21.y)) #extend center hem out for collar
        #welt
        a25 = A.addPoint('a25', onLineAtLength(a22, FBP, WELT_HEIGHT)) #welt top left
        a26 = A.addPoint('a26', intersectLineRay(a23, a19, a25, angleOfLine(a22, a23))) #welt top rright
        #pocket
        a27 = A.addPoint('a27', (FHS1.x, a20.y)) #bottom of pocket curve

        #adjust control points
        #b/w a18 underarm & a4 armscye curve # a3 shoulder tip
        a18.addOutpoint(polar(a18, distance(a18, a4)/3.0, angleOfLine(a19, a18) + ANGLE90))
        (a4.inpoint.x, a4.inpoint.y) = polar(a4, distance(a4, a18)/3.0, angleOfLine(a4.outpoint, a4))
        #b/w a21 hem center & a20 hem side
        a21.addOutpoint(left(a21, distance(a21, a20)/3.33))
        a20.addInpoint(polar(a20, distance(a21, a20)/3.33, angleOfLine(a19, a20) - ANGLE90))
        #b/w a23 pocket outside & a27 pocket bottom & a22 pocket inside
        a23.addOutpoint(down(a23, 0.7 * distance(a23, a27)))
        a27.addInpoint(left(a27, 0.7 * abs(a23.x - a27.x)))
        a27.addOutpoint(right(a27, 0.7 * abs(a27.x - a22.x)))
        a22.addInpoint(down(a22, 0.7 * abs(a27.y - a22.y)))

        #facing
        hem_curve = points2List(a21, a21.outpoint, a20.inpoint, a20)
        a50 = A.addPoint('a50', onCurveAtX(hem_curve, a13.x)) #facing hem
        new_curve = splitCurveAtPoint(hem_curve, a50)
        (a21.outpoint.x, a21.outpoint.y) = new_curve[1]
        a50.addInpoint(new_curve[2])
        a50.addOutpoint(new_curve[4])
        (a20.inpoint.x, a20.inpoint.y) = new_curve[5]

        #Adjust Back B
        #lower underarm
        b26 = B.addPoint('b26', (b23.x + 0.07 * CD.back_underarm, b23.y + LOWER_LENGTH)) #new back underarm - out 7% back underarm, down 40% side length
        #extend side seam
        b27 = B.addPoint('b27', right(b25, 2 * abs(b26.x - b23.x))) #push out hem side
        b28 = B.addPoint('b28', onLineAtLength(b26, b27, distance(a18, a20))) #make back side seam length equal to front side seam length
        #extend back center line
        b29 = B.addPoint('b29', down(b19, 1.5 * LOWER_LENGTH)) #begin back center line angle below back neck center
        b30 = B.addPoint('b30', left(b13, distance(b25, b27))) #push out hem center
        pnt = dPnt(intersectLines(b27, b28, b29, b30)) # find point where center & side seam intersect
        b31 = B.addPoint('b31', onLineAtLength(pnt, b30, distance(pnt, b28))) #new front hem center
        #adjust control points
        #b/w b26 underarm & b22 armscye curve & b21 shoulder point
        b26.addOutpoint(polar(b26, distance(b26, b22)/3.0, angleOfLine(b26, b27) + ANGLE90))
        (b22.inpoint.x, b22.inpoint.y) = polar(b22, distance(b26, b22)/3.0, angleOfLine(b21, b26))
        (b22.outpoint.x, b22.outpoint.y) = polar(b22, distance(b22, b21)/3.0, angleOfLine(b26, b21))
        #b/w b31 hem center and b28 hem side
        b31.addOutpoint(polar(b31, distance(b31, b28)/3.33, angleOfLine(b30, b31) - ANGLE90))
        b28.addInpoint(polar(b28, distance(b31, b28)/3.33, angleOfLine(b27, b28) + ANGLE90))
        #b/w b29 flex point center & b31 hem center
        b29.addOutpoint(down(b29, distance(b29, b31)/8.0))
        b31.addInpoint(polar(b31, distance(b29, b31)/8.0, angleOfLine(b31, b29.outpoint)))

        #---Shirt sleeve C---#
        #get front & back armcye length
        #back_armscye = points2List(b10, b10.outpoint, b7.inpoint, b7, b7.outpoint, b5.inpoint, b5)
        back_armscye = points2List(b26, b26.outpoint, b22.inpoint, b22, b22.outpoint, b21.inpoint, b21)
        #front_armscye = points2List(FUS, FUS.outpoint, FAS.inpoint, FAS, FAS.outpoint, FSP.inpoint, FSP)
        front_armscye = points2List(a18, a18.outpoint, a4.inpoint, a4, a4.outpoint, a3.inpoint, a3)
        back_armscye_length = curveLength(back_armscye)
        front_armscye_length = curveLength(front_armscye)
        ARMSCYE_LENGTH = back_armscye_length + front_armscye_length
        CAP_HEIGHT = ARMSCYE_LENGTH/3.0 # + distance(FUS, a18)
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

        back_armscye_length = distance(a3, a4) + distance(a4, a18)
        front_armscye_length = distance(b21, b22) + distance(b22, b26)
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
        c21 = C.addPoint('c21', symmetricPoint(c19, c8))
        c21.addOutpoint(symmetricPoint(c19.inpoint, c8))
        c21.addInpoint(symmetricPoint(c19.outpoint, c8))
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
        #---Pocket E---#
        #---Front Facing F---#
        #---Upper Front G---#
        #---Sleeve Front H---#

        #---Sleeve Facing I---#
        i1 = C.addPoint('i1', up(c2, distance(c7, c9)/4.0)) #top left facing point
        i2 = C.addPoint('i2', up(c4, distance(c7, c9)/4.0)) #top right facing point

        #---------------------------------------------#
        #---all points defined, draw pattern pieces---#
        #---------------------------------------------#

        #draw Lower Front A
        pnt1 = dPnt((a22.x, a19.y))
        A.setLabelPosition(pnt1)
        A.setLetter((a22.x, a23.y), scaleby=10.0)
        aG1 = dPnt(FAC)
        aG2 = dPnt(FHC)
        A.addGrainLine(aG1, aG2)
        A.addGridLine(['M', FNC, 'L', FWC, 'L', FSP, 'M', FAC, 'L', FUS1, 'M', FNC, 'L', FSP, 'M', FBC, 'L', FBP, 'M', FWC, 'L', FWS3, 'M', FBP, 'L', FNS, 'L', FAS, 'M', FUS, 'L', FWS2, 'M', FBP, 'L', FBS, 'M', FD2.m, 'L', FBP, 'L', FHM, 'M', FHC, 'L', FHS1, 'M', FD1.o, 'L', FWS, 'M', FHS2, 'L', FWS, 'M', FNC, 'L', FHC, 'L', FHM, 'L', FHS, 'L', FWS, 'L', FD2.o, 'L', FD2.m, 'L', FD2.i, 'L', FUS, 'C', FAS, 'C', FSP, 'L', FNS, 'C', FNC, 'M', FD1.i, 'L', FD1, 'L', FD1.o, 'L', FD1.d, 'L', FD1.i, 'M', FD2.ic, 'L', FD2, 'L', FD2.oc, 'M', a1, 'L', FHC, 'L', FHM, 'L', a9, 'L', a8, 'L', a7, 'L', a6, 'L', a5, 'C', a4, 'C', a3, 'L', a2, 'C', a12, 'L', FBP, 'L', a13, 'C', a1, 'M', a18, 'C', a4, 'C', a3, 'L', a2, 'C', a12, 'L', FBP, 'M', a23, 'C', a27, 'C', a22, 'M', a13, 'L', a50])
        #pth = (['M', a1, 'L', FHC, 'L', FHM, 'L', a9, 'L', a8, 'L', a7, 'L', a6, 'L', a5, 'C', a4, 'C', a3, 'L', a2, 'C', a12, 'L', FBP, 'L', a13, 'C', a1])
        pth = (['M', a15, 'L', a24, 'L', a21, 'C', a50, 'C', a20, 'L', a23, 'L', a22 , 'L', a13, 'C', a17, 'C', a10, 'L', a11, 'C', a14, 'C', a15])
        A.addDartLine(['M', a13, 'L', a22, 'L', a23])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        #draw Back B
        pnt1 = dPnt((distance(b3, b6)/2.0, distance(b1, b8)/2.0))
        B.setLabelPosition((pnt1))
        B.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)
        bG1 = dPnt((distance(b3, b6)/4.0, b8.y))
        bG2 = dPnt(down(bG1, distance(b1, b13)/2.0))
        B.addGrainLine(bG1, bG2)
        B.addGridLine(['M', b6, 'L', b3, 'L', b2, 'L', b14, 'M', bD1.o, 'L', b11, 'M', b1, 'L', b5, 'M', b2, 'L', b5, 'M', b6, 'L', b7, 'M', b8, 'L', b9, 'M',  bD1, 'L', b15, 'L', b16, 'M', b17, 'L', b11, 'M', b1, 'L', b13, 'L', b15, 'L', b18, 'L', b11, 'L', b10, 'C', b7, 'C', b5, 'L', b6, 'C', b1, 'M', b18, 'L', b25, 'L', b24, 'L', b23])
        pth = (['M', b19, 'L', b29, 'C', b31, 'C', b28, 'L', b26, 'C', b22, 'C', b21, 'L', b20, 'C', b19])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        #draw Sleeve Back C
        pnt1 = dPnt(down(c5, distance(c7, c9)/6.0))
        C.setLetter((pnt1.x, pnt1.y), scaleby=15.0)
        C.setLabelPosition(down(pnt1, distance(pnt1, c9)/6.0))
        cG1 = dPnt((c13.x, c11.y))
        cG2 = down(cG1, 0.75 * distance(c7, c9))
        C.addGrainLine(cG1, cG2)
        C.addGridLine(['M', c1, 'L', c2, 'L', c4, 'L', c3, 'L', c1, 'M', c13, 'L', c16, 'M', c5, 'L', c6, 'M', c8, 'L', c9])
        pth = (['M', c19, 'C', c20, 'L', c9, 'L', c2, 'C', c17, 'C', c13, 'C', c19])
        C.addSeamLine(pth)
        C.addCuttingLine(pth)

        #draw Welt D
        D.setLetter((a26.x + distance(a25, a26)/4.0, (a26.y + a23.y)/2.0), scaleby=5.0)
        D.setLabelPosition((a26.x + distance(a25, a26)/2.0, a25.y + abs(a25.y - a23.y)/3.0))
        dG1 = dPnt((a26.x + 0.75 * distance(a25, a26), a25.y + distance(a25, a22)/2.0))
        dG2 = down(dG1, 0.7 * distance(a25, a22))
        D.addGrainLine(dG1, dG2)
        pth =(['M', a25, 'L', a22, 'L', a23, 'L', a26, 'L', a25])
        D.addSeamLine(pth)
        D.addCuttingLine(pth)

        #draw Pocket E
        pnt1 = dPnt((a23.x + distance(a23, a22)/3.0, a23.y + distance(a23, a27)/4.0))
        E.setLetter((pnt1.x, pnt1.y), scaleby=10.0)
        E.setLabelPosition(down(pnt1, abs(a23.y - a27.y)/3.0))
        eG1 = dPnt((a23.x + 0.75 * distance(a23, a22), a22.y + abs(a23.y - a22.y)/4.0))
        eG2 = down(eG1, 0.75 * distance(a23, a27))
        E.addGrainLine(eG1, eG2)
        pth =(['M', a23, 'C', a27, 'C', a22, 'L', a23])
        E.addSeamLine(pth)
        E.addCuttingLine(pth)

        #draw Front Facing F
        F.setLetter((a1.x, FAC.y), scaleby=8.0)
        F.setLabelPosition((a1.x - 25, FAC.y + 50))
        fG1 = dPnt(onLineAtLength(a13, a15, distance(a13, a15)/4.0))
        fG2 = down(fG1, 0.75 * distance(a13, a50))
        F.addGrainLine(fG1, fG2)
        pth =(['M', a13, 'C', a17, 'C', a10, 'L', a11, 'C', a14, 'C', a15, 'L', a24, 'L', a21, 'C', a50, 'L', a13])
        F.addSeamLine(pth)
        F.addCuttingLine(pth)

        #draw Upper Front G
        pnt1 = dPnt(midPoint(a4, FBP))
        G.setLetter((pnt1.x, pnt1.y), scaleby=10.0)
        G.setLabelPosition((pnt1.x, pnt1.y + 50))
        gG1 = dPnt((pnt1.x - 50, FAS.y))
        gG2 = down(gG1, 0.75 * distance(FAS, a22))
        G.addGrainLine(gG1, gG2)
        pth =(['M', a12, 'L', FBP, 'L', a22, 'L', a23, 'L', a18, 'C', a4, 'C', a3, 'L', a2, 'C', a12])
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
        pnt2 = dPnt((pnt1.x + distance(i1, i2)/4.0, pnt1.y))
        I.setLabelPosition((pnt2.x, pnt2.y))
        hG1 = dPnt((i1.x + 0.75 * distance(i1, i2), (i1.y + distance(i1, c2)/4.0)))
        hG2 = down(hG1, 0.5 * distance(i1, c2))
        I.addGrainLine(hG1, hG2)
        pth = (['M', i1, 'L', i2, 'L', c4, 'L', c2, 'L', i1])
        I.addSeamLine(pth)
        I.addCuttingLine(pth)



        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

