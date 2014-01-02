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
        self.setInfo('patternNumber', 'Coat_W_Topper_MRohr_p7')
        self.setInfo('patternTitle', 'Topper Coat - MRohr (p7)')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'S.L.Spencer')
        self.setInfo('patternmakerName', 'S.L.Spencer')
        self.setInfo('description', """This is a test pattern for Seamly Patterns""")
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
        a1 = A.addPoint('a1', (0.0, 0.0)) #front neck center
        a2 = A.addPoint('a2', down(a1, CD.front_waist_length)) #front waist center
        a3 = A.addPoint('a3', up(a2, CD.bust_length)) #bust center
        a4 = A.addPoint('a4', left(a3, CD.bust_distance/2.0)) #bust point
        a5 = A.addPoint('a5', leftmostP(intersectCircles(a2, CD.front_shoulder_balance, a1, CD.front_shoulder_width))) #front shoulder point
        a6 = A.addPoint('a6', highestP(intersectCircles(a5, CD.shoulder, a4, CD.bust_balance))) #front neck point
        a7 = A.addPoint('a7', lowestP(onCircleAtX(a6, CD.front_underarm_balance, a1.x - CD.across_chest/2.0))) #front underarm point
        a8 = A.addPoint('a8', (a1.x, a7.y)) #front undearm center
        a9 = A.addPoint('a9', left(a8, CD.front_underarm/2.0)) #front underarm side
        #TODO: create function onCircleAtTangentOfPoint()
        a10 = A.addPoint('a10', leftmostP(onCircleTangentFromOutsidePoint(a4, CD.front_bust/2.0 - distance(a3, a4), a9))) #bust side is where line from bust point is perpendicular to line through a9
        a11 = A.addPoint('a11', onLineAtLength(a9, a10, 0.13 * CD.side)) #adjusted front underarm side on line a9-10
        a12 = A.addPoint('a12', left(a2, CD.front_waist/2.0)) #temporary front waist side 1 - on waist line
        a13 = A.addPoint('a13', dPnt((a4.x, a2.y))) #below bust point at waist
        a14 = A.addPoint('a14', intersectLines(a3, a4, a10, a11)) #intersect bust line & side seam
        a15 = A.addPoint('a15', onLineAtLength(a9, a10, CD.side)) #temporary front waist side 2 - on side seam

        #front waist dart
        totalDartAngle = abs(angleOfVector(a12, a4, a15))
        frontWaistDartAngle = totalDartAngle/2.0
        bustDartAngle = totalDartAngle/2.0
        aD1 = A.addPoint('aD1', (a4)) #front waist dart point
        aD1.i = A.addPoint('aD1.i', onRayAtY(a4, ANGLE90 - frontWaistDartAngle/2.0, a2.y)) #front waist dart inside leg
        aD1.o = A.addPoint('aD1.o', onRayAtY(a4, ANGLE90 + frontWaistDartAngle/2.0, a2.y)) #front waist dart outside leg
        #bust dart
        aD2 = A.addPoint('aD2', (a4)) #bust dart point
        aD2.i = A.addPoint('aD2.i', intersectLineRay(a9, a10, a4, ANGLE180 + bustDartAngle/2.0)) #bust dart inside leg
        aD2.o = A.addPoint('aD2.o', polar(a4, distance(a4, aD2.i), ANGLE180 - bustDartAngle/2.0)) #bust dart outside leg
        #TODO: create function pivot(pivot_point, rotation_angle, point_to_pivot)

        #finalize front waist side
        remainingSideSegment = distance(a11, a15) - distance(a11, aD2.i)
        remainingWaistSegment = distance(a2, a12) - distance(a2, aD1.i)
        a16 = A.addPoint('a16', leftmostP(intersectCircles(aD2.o, remainingSideSegment, aD1.o, remainingWaistSegment))) #front waist side created after all darts defined

        #create curve at dart base
        ##adjustDartLength(a16, aD1, a2, extension=0.25) #smooth waistline curve from a16 to a2 at dart
        foldDart2(aD1, a2) #creates aD1.m,aD1.oc,aD1.ic; dart folds in toward waist center a2
        #do not call adjustDartLength(a12,aD2,a11) -- bust dart aD2 is not on a curve
        foldDart2(aD2, a11) #creates aD2.m,aD2.oc,aD2.ic; dart folds up toward underarm side a11
        #adjust aD1 & aD2 away from a4 bust point
        (aD1.x, aD1.y) = down(aD1, distance(aD1, aD1.i)/7.0)
        (aD2.x, aD2.y) = left(aD2, distance(aD2, aD2.i)/7.0)

        #Bodice Lower Front A hip extension
        a17 = A.addPoint('a17', down(a2, CD.front_hip_height)) #front hip center
        a18 = A.addPoint('a18', left(aD1.o, distance(aD1.o, a16))) #front waist side
        a19 = A.addPoint('a19', (aD1.x, a17.y)) #reflect waist dart point on hip line for 'fish dart'
        a20 = A.addPoint('a20', left(a17, CD.front_hip/2.0)) #temporary front hip side
        a21 = A.addPoint('a21', polar(aD1.o, distance(aD1.o, a20), angleOfLine(aD1.o, a20) + angleOfVector(a18, aD1.o, a16))) #final front hip side
        a22 = A.addPoint('a22', onLineAtLength(a16, a21, CD.side_hip_height)) #front hip side
        aD1.d = A.addPoint('aD1.d', up(a19, distance(a19, a13)/7.0)) #front waist dart point at hip

        #adjust block to coat points
        a23 = A.addPoint('a23', down(a1, 0.03*CD.front_waist_length)) #new front neck center
        a24 = A.addPoint('a24', onLineAtLength(a6, a5, distance(a1, a23))) #new front neck point
        a25 = A.addPoint('a25', left(a5, distance(a1, a23))) #new shoulder point
        a26 = A.addPoint('a26', left(a7, distance(a1, a23))) #new armscye curve
        a27 = A.addPoint('a27', onLineAtLength(a10, a4, -0.05*CD.front_bust)) #new underarm point - out 0.5in & down 1in
        a28 = A.addPoint('a28', onLineAtLength(aD2.i, a4, -distance(a10, a27))) #new bust dart inside
        a29 = A.addPoint('a29', onLineAtLength(aD2.o, a4, -distance(a10, a27))) #new bust dart outside
        a30 = A.addPoint('a30', onLineAtLength(a16, aD1.o, -distance(a10, a27))) #new waist side
        a31 = A.addPoint('a31', onLineAtLength(a22, a19, -distance(a10, a27))) #new hip side

        #Bodice Lower Front A control points
        #b/w a6 front neck point & a1 front neck center
        a6.addOutpoint(down(a6, abs(a1.y - a6.y)/2.0))
        a1.addInpoint(left(a1, 0.75 * abs(a1.x - a6.x)))
        #b/w aD1.o waist dart outside leg & a16 front waist side - short control handles
        aD1.o.addOutpoint(polar(aD1.o, distance(aD1.o, a16)/6.0, angleOfLine(aD1.o, aD1) - (angleOfLine(aD1.i, aD1) - ANGLE180))) #control handle forms line with a2,aD1.i
        a16.addInpoint(polar(a16, distance(aD1.o, a16)/6.0, angleOfLine(a16, aD1.o.outpoint))) #a16 control handle points to aD1.o control handle
        #b/w a7 front underarm point & a5 front shoulder point
        a5.addInpoint(polar(a5, distance(a7, a5)/6.0, angleOfLine(a5, a6) + ANGLE90)) #short control handle perpendicular to shoulder seam
        a7.addOutpoint(polar(a7, distance(a7, a5)/3.0, angleOfLine(a7, a6))) #control handle points to front neck point
        #b/w a11 front underarm side & a7 front underarm point
        a7.addInpoint(polar(a7, distance(a11, a7)/3.0, angleOfLine(a6, a7)))
        a11.addOutpoint(polar(a11, distance(a11, a7)/3.0, angleOfLine(aD2.i, a11) + ANGLE90)) #control handle is perpendicular to side seam at underarm
        #b/w a24 new neck point & a23 new front neck center
        a23.addInpoint(left(a23, 0.75 * abs(a23.x - a24.x)))
        a24.addOutpoint(polar(a24, abs(a23.y - a24.y)/2.0, angleOfLine(a25, a24) + ANGLE90))
        #b/w a27 new underarm & a26 armscye curve & a25 new shoulder tip
        a27.addOutpoint(polar(a27, distance(a27, a26)/3.0, angleOfLine(a28, a27) + ANGLE90))
        a26.addInpoint(polar(a26, distance(a27, a26)/3.0, angleOfLine(a24, a26)))
        a26.addOutpoint(polar(a26, distance(a26, a25)/3.0, angleOfLine(a26, a24)))
        a25.addInpoint(polar(a25, distance(a7, a25)/6.0, angleOfLine(a24, a25) - ANGLE90)) #short control handle, perpendicular to shoulder seam

        #---Bodice Back B---#
        b1 = B.addPoint('b1', (0.0, 0.0)) #back neck center
        b2 = B.addPoint('b2', down(b1, CD.back_waist_length)) #back waist center
        b3 = B.addPoint('b3', up(b2, CD.back_shoulder_height)) #shoulder height reference point
        b4 = B.addPoint('b4', right(b2, CD.back_waist/2.0)) #back waist side reference point
        b5 = B.addPoint('b5', rightmostP(intersectCircles(b2, CD.back_shoulder_balance, b1, CD.back_shoulder_width))) #back shoulder point
        b6 = B.addPoint('b6', leftmostP(onCircleAtY(b5, CD.shoulder, b3.y))) #back neck point
        b7 = B.addPoint('b7', lowestP(onCircleAtX(b6, CD.back_underarm_balance, b1.x + CD.across_back/2.0))) #back underarm point
        b8 = B.addPoint('b8', (b1.x, b7.y)) #back undearm center
        b9 = B.addPoint('b9', right(b8, CD.back_underarm/2.0)) #back underarm side reference point
        b10 = B.addPoint('b10', down(b9, distance(a9, a11))) #adjusted back underarm side
        bD1 = B.addPoint('bD1', intersectLines(b2, b5, b8, b9)) #back waist dart point is at underarm height
        b12 = B.addPoint('b12', dPnt((bD1.x, b2.y))) # below dart point at waist
        bD1.i = B.addPoint('bD1.i', left(b12, distance(b2, b12)/5.0)) #dart inside leg
        bD1.o = B.addPoint('bD1.o', right(b12, distance(b12, bD1.i))) #dart outside leg
        b11 = B.addPoint('b11',  rightmostP(intersectCircles(b10, distance(a11, aD2.i) + distance(aD2.o, a16), bD1.o, CD.back_waist/2.0 - distance(b2, bD1.i)))) #back waist side

        #create curve at dart base
        ##adjustDartLength(a16, aD1, a2, extension=0.25) #smooth waistline curve from a16 to a2 at dart
        foldDart2(bD1, b2) #creates bD1.m, bD1.oc, bD1.ic; dart folds toward waist center b2

        b13 = B.addPoint('b13', down(b2, CD.back_hip_height)) #back hip center
        b14 = B.addPoint('b14', right(bD1.o, distance(bD1.o, b11))) #back waist side
        b15 = B.addPoint('b15', (bD1.x, b13.y)) # back waist dart at hip line
        b16 = B.addPoint('b16', right(b13, CD.back_hip/2.0)) #temporary back hip side
        b17 = B.addPoint('b17', polar(bD1.o, distance(bD1.o, b16), angleOfLine(bD1.o, b16) - angleOfVector(b14, bD1.o, b11))) #temporary back waist side
        b18 = B.addPoint('b18', onLineAtLength(b11, b17, CD.side_hip_height)) #back hip side
        bD1.d = B.addPoint('bD1.d', up(b15, distance(b15, b12)/7.0)) # back waist dart point at hip

        #adjust block to topper points
        b19 = B.addPoint('b19', down(b1, 0.03*CD.back_waist_length)) #new back neck center
        b20 = B.addPoint('b20', onLineAtLength(b6, b5, distance(a1, a23))) #new back neck point
        b21 = B.addPoint('b21', right(b5, distance(a1, a23))) #new shoulder point
        b22 = B.addPoint('b22', right(b7, distance(a1, a23))) #new armscye curve
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
        b11.addInpoint(polar(b11, distance(bD1.o, b11)/3.0, angleOfLine(b10, b11) + angleOfVector(aD2.o, a16, a16.inpoint))) #forms line with control handle for a16 front waist
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
        a32 = A.addPoint('a32', polar(a24, curveLength(back_neck_curve), angleOfLine(a24.outpoint, a24))) #front neck extension point 1
        a33 = A.addPoint('a33', polar(a32, 0.13 * CD.front_waist_length, angleOfLine(a24, a32) + ANGLE90)) #front neck extension point 2
        front_neck_curve = points2List(a23, a23.inpoint, a24.outpoint, a24)
        curve_length = curveLength(front_neck_curve)
        a34 = A.addPoint('a34', curvePointAtLength(front_neck_curve, curve_length/3.0)) #divide front neck curve 1/3rd along length
        a35 = A.addPoint('a35', dPnt(a34)) #a35 won't rotate
        a36 = A.addPoint('a36', polar(a33, distance(a24, a32), angleOfLine(a32, a24))) #front neckextension point 3
        a37 = A.addPoint('a37', right(a23, 0.1 * CD.front_waist_length)) #right of a23 front neck center
        a38 = A.addPoint('a38', right(a17, distance(a23, a37))) #right of a17 front hip center
        a49 = A.addPoint('a49', a24) #copy neck point to use in collar
        #b/w a24 neck point, a34/a35 split point, a23 front neck center
        (a23.inpoint.x, a23.inpoint.y) = left(a23, distance(a23, a34)/3.0) #adjust a23.inpoint
        (a24.outpoint.x, a24.outpoint.y) = polar(a24, distance(a24, a34)/3.0, angleOfLine(a25, a24) + ANGLE90) #adjust a23.inpoint
        a49.addInpoint(a24.outpoint)
        a49.addOutpoint(polar(a49, distance(a49, a32)/3.0, angleOfLine(a49.inpoint, a49)))
        a32.addInpoint(polar(a32, distance(a49, a32)/3.0, angleOfLine(a32, a33) + ANGLE90))

        a34.addInpoint(polar(a34, distance(a34, a24)/3.0, angleOfLine(a23.inpoint, a24.outpoint)))
        a35.addOutpoint(a34.inpoint)
        #b/w a33 extended collar top corner & a36 extended collar top midpoint
        a33.addOutpoint(polar(a33, distance(a33, a36)/3.0, angleOfLine(a32, a33) + ANGLE90))
        a36.addInpoint(polar(a36, distance(a33, a36)/3.0, angleOfLine(a49, a49.outpoint)))
        #b/w a36 extended collar midpoint & a37 extended collar neck point
        a36.addOutpoint(polar(a36, distance(a36, a37)/3.0, angleOfLine(a49.outpoint, a49)))
        a37.addInpoint(up(a37, distance(a36, a37)/3.0))
        #a35.addOutpoint(polar(a35, distance(a35, a23)/3.0, angleOfLine(a34.inpoint, a34)))

        #close bust dart
        pivot = a4
        angle = angleOfVector(a28, a4, a29)
        slashAndSpread(pivot, -angle, a28, a27, a27.outpoint, a26.inpoint, a26, a26.outpoint, a25.inpoint, a25, a24, a24.outpoint, a34.inpoint, a34) #rotate counterclockwise, so angle < 0
        #lower underarm
        LOWER_LENGTH = 0.2 * distance(a27, a30) #20% side length
        a39 = A.addPoint('a39', (a27.x - 0.07 * CD.front_underarm, a27.y + LOWER_LENGTH)) #new front underarm - out 7% front underarm, down 40% side length
        #extend side seam
        a40 = A.addPoint('a40', left(a31, 2 * abs(a39.x - a27.x))) #push out hem side
        a41 = A.addPoint('a41', extendLine(a39, a40, 1.5 * LOWER_LENGTH)) #extend hem side down
        #extend front center line
        pnt = intersectLines(a40, a41, a1, a17) # find point where center line & side seam intersect
        a42 = A.addPoint('a42', onLineAtLength(pnt, a1, distance(pnt, a41))) #new front hem center
        #split front into 2 pieces
        WELT_HEIGHT = 0.15 * CD.front_waist_length
        a43 = A.addPoint('a43', onLineAtLength(a35, a4, a2.y + WELT_HEIGHT)) #pocket corner point
        a44 = A.addPoint('a44', onLineAtLength(a40, a39, distance(a31, a30)/3.0)) #side split point
        #collar
        a45 = A.addPoint('a45', (a38.x, a42.y)) #extend center hem out for collar
        #welt
        a46 = A.addPoint('a46', onLineAtLength(a43, a4, WELT_HEIGHT)) #welt top left
        a47 = A.addPoint('a47', intersectLineRay(a44, a40, a46, angleOfLine(a43, a44))) #welt top rright
        #pocket
        a48 = A.addPoint('a48', (a20.x, a41.y)) #bottom of pocket curve

        #adjust control points
        #b/w a39 underarm & a26 armscye curve # a25 shoulder tip
        a39.addOutpoint(polar(a39, distance(a39, a26)/3.0, angleOfLine(a40, a39) + ANGLE90))
        (a26.inpoint.x, a26.inpoint.y) = polar(a26, distance(a26, a39)/3.0, angleOfLine(a26.outpoint, a26))
        #b/w a42 hem center & a41 hem side
        a42.addOutpoint(left(a42, distance(a42, a41)/3.33))
        a41.addInpoint(polar(a41, distance(a42, a41)/3.33, angleOfLine(a40, a41) - ANGLE90))
        #b/w a44 pocket outside & a48 pocket bottom & a43 pocket inside
        a44.addOutpoint(down(a44, 0.7 * distance(a44, a48)))
        a48.addInpoint(left(a48, 0.7 * abs(a44.x - a48.x)))
        a48.addOutpoint(right(a48, 0.7 * abs(a48.x - a43.x)))
        a43.addInpoint(down(a43, 0.7 * abs(a48.y - a43.y)))

        #facing
        hem_curve = points2List(a42, a42.outpoint, a41.inpoint, a41)
        a50 = A.addPoint('a50', onCurveAtX(hem_curve, a35.x)) #facing hem
        new_curve = splitCurveAtPoint(hem_curve, a50)
        (a42.outpoint.x, a42.outpoint.y) = new_curve[1]
        a50.addInpoint(new_curve[2])
        a50.addOutpoint(new_curve[4])
        (a41.inpoint.x, a41.inpoint.y) = new_curve[5]

        #Adjust Back B
        #lower underarm
        b26 = B.addPoint('b26', (b23.x + 0.07 * CD.back_underarm, b23.y + LOWER_LENGTH)) #new back underarm - out 7% back underarm, down 40% side length
        #extend side seam
        b27 = B.addPoint('b27', right(b25, 2 * abs(b26.x - b23.x))) #push out hem side
        b28 = B.addPoint('b28', onLineAtLength(b26, b27, distance(a39, a41))) #make back side seam length equal to front side seam length
        #extend back center line
        b29 = B.addPoint('b29', down(b19, 1.5 * LOWER_LENGTH)) #begin back center line angle below back neck center
        b30 = B.addPoint('b30', left(b13, distance(b25, b27))) #push out hem center
        pnt = intersectLines(b27, b28, b29, b30) # find point where center & side seam intersect
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
        #front_armscye = points2List(a11, a11.outpoint, a7.inpoint, a7, a7.outpoint, a5.inpoint, a5)
        front_armscye = points2List(a39, a39.outpoint, a26.inpoint, a26, a26.outpoint, a25.inpoint, a25)
        back_armscye_length = curveLength(back_armscye)
        front_armscye_length = curveLength(front_armscye)
        ARMSCYE_LENGTH = back_armscye_length + front_armscye_length
        CAP_HEIGHT = ARMSCYE_LENGTH/3.0 # + distance(a11, a39)
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

        back_armscye_length = distance(a25, a26) + distance(a26, a39)
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
        pnt1 = dPnt((a43.x, a40.y))
        A.setLabelPosition(pnt1)
        A.setLetter((a43.x, a44.y), scaleby=10.0)
        aG1 = dPnt(a8)
        aG2 = dPnt(a17)
        A.addGrainLine(aG1, aG2)
        A.addGridLine(['M', a1, 'L', a2, 'L', a5, 'M', a8, 'L', a9, 'M', a1, 'L', a5, 'M', a3, 'L', a4, 'M', a2, 'L', a12, 'M', a4, 'L', a6, 'L', a7, 'M', a11, 'L', a15, 'M', a4, 'L', a10, 'M', a14, 'L', a4, 'L', a19, 'M', a17, 'L', a20, 'M', a18, 'L', aD1.o, 'L', a16, 'M', a21, 'L', a16, 'M', a1, 'L', a17, 'L', a19, 'L', a22, 'L', a16, 'L', aD2.o, 'L', aD2.m, 'L', aD2.i, 'L', a11, 'C', a7, 'C', a5, 'L', a6, 'C', a1, 'M', aD1.i, 'L', aD1, 'L', aD1.o, 'L', aD1.d, 'L', aD1.i, 'M', aD2.ic, 'L', aD2, 'L', aD2.oc, 'M', a23, 'L', a17, 'L', a19, 'L', a31, 'L', a30, 'L', a29, 'L', a28, 'L', a27, 'C', a26, 'C', a25, 'L', a24, 'C', a34, 'L', a4, 'L', a35, 'C', a23, 'M', a39, 'C', a26, 'C', a25, 'L', a24, 'C', a34, 'L', a4, 'M', a44, 'C', a48, 'C', a43, 'M', a35, 'L', a50])
        #pth = (['M', a23, 'L', a17, 'L', a19, 'L', a31, 'L', a30, 'L', a29, 'L', a28, 'L', a27, 'C', a26, 'C', a25, 'L', a24, 'C', a34, 'L', a4, 'L', a35, 'C', a23])
        pth = (['M', a37, 'L', a45, 'L', a42, 'C', a50, 'C', a41, 'L', a44, 'L', a43 , 'L', a35, 'C', a49, 'C', a32, 'L', a33, 'C', a36, 'C', a37])
        A.addDartLine(['M', a35, 'L', a43, 'L', a44])
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
        D.setLetter((a47.x + distance(a46, a47)/4.0, (a47.y + a44.y)/2.0), scaleby=5.0)
        D.setLabelPosition((a47.x + distance(a46, a47)/2.0, a46.y + abs(a46.y - a44.y)/3.0))
        dG1 = dPnt((a47.x + 0.75 * distance(a46, a47), a46.y + distance(a46, a43)/2.0))
        dG2 = down(dG1, 0.7 * distance(a46, a43))
        D.addGrainLine(dG1, dG2)
        pth =(['M', a46, 'L', a43, 'L', a44, 'L', a47, 'L', a46])
        D.addSeamLine(pth)
        D.addCuttingLine(pth)

        #draw Pocket E
        pnt1 = dPnt((a44.x + distance(a44, a43)/3.0, a44.y + distance(a44, a48)/4.0))
        E.setLetter((pnt1.x, pnt1.y), scaleby=10.0)
        E.setLabelPosition(down(pnt1, abs(a44.y - a48.y)/3.0))
        eG1 = dPnt((a44.x + 0.75 * distance(a44, a43), a43.y + abs(a44.y - a43.y)/4.0))
        eG2 = down(eG1, 0.75 * distance(a44, a48))
        E.addGrainLine(eG1, eG2)
        pth =(['M', a44, 'C', a48, 'C', a43, 'L', a44])
        E.addSeamLine(pth)
        E.addCuttingLine(pth)

        #draw Front Facing F
        F.setLetter((a23.x, a8.y), scaleby=8.0)
        F.setLabelPosition((a23.x - 25, a8.y + 50))
        fG1 = dPnt(onLineAtLength(a35, a37, distance(a35, a37)/4.0))
        fG2 = down(fG1, 0.75 * distance(a35, a50))
        F.addGrainLine(fG1, fG2)
        pth =(['M', a35, 'C', a49, 'C', a32, 'L', a33, 'C', a36, 'C', a37, 'L', a45, 'L', a42, 'C', a50, 'L', a35])
        F.addSeamLine(pth)
        F.addCuttingLine(pth)

        #draw Upper Front G
        pnt1 = dPnt(midPoint(a26, a4))
        G.setLetter((pnt1.x, pnt1.y), scaleby=10.0)
        G.setLabelPosition((pnt1.x, pnt1.y + 50))
        gG1 = dPnt((pnt1.x - 50, a7.y))
        gG2 = down(gG1, 0.75 * distance(a7, a43))
        G.addGrainLine(gG1, gG2)
        pth =(['M', a34, 'L', a4, 'L', a43, 'L', a44, 'L', a39, 'C', a26, 'C', a25, 'L', a24, 'C', a34])
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

