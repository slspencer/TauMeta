#!/usr/bin/env python
# patternName: Spencer_bodice
# patternNumber: W_Bl_B_1

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
        self.setInfo('patternNumber', 'W_Block_Bodice_1')
        self.setInfo('patternTitle', 'Spencer Bodice Block')
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
        A = bodice.addPiece('front', 'A', fabric = 2, interfacing = 0, lining = 0)
        #front
        a1 = A.addPoint('a1', (0.0, 0.0)) #front neck center
        a2 = A.addPoint('a2', down(a1, CD.front_waist_length)) #front waist center
        a3 = A.addPoint('a3', up(a2, CD.bust_length)) #bust center
        a4 = A.addPoint('a4', left(a3, CD.bust_distance/2.0)) #bust point
        a5 = A.addPoint('a5', leftmostP(intersectCircles(a2, CD.front_shoulder_balance, a1, CD.front_shoulder_width))) #front shoulder point
        a6 = A.addPoint('a6', highestP(intersectCircles(a5, CD.shoulder, a4, CD.bust_balance))) #front neck point
        a7 = A.addPoint('a7', lowestP(onCircleAtX(a6, CD.front_armfold_balance, a1.x - CD.front_armfold_distance/2.0))) #front underarm point
        a8 = A.addPoint('a8', (a1.x, a7.y)) #front undearm center
        a9 = A.addPoint('a9', left(a8, CD.front_underarm/2.0)) #front underarm side
        #TODO: create function onCircleAtTangentOfPoint()
        #a10 = A.addPoint('a10', onCircleAtTangentOfPoint(c=aD2, r=CD.front_bust/2.0 - distance(a3, a4), pnt=a9) #bust side - point where line from bust point is perpendicular to line through a9
        #a11 = A.addPoint('a11', onLineAtLength(a9, a10, CD.side/10.0)) # adjusted front underarm side
        a11 = A.addPoint('a11', down(a9, 0.15 * CD.side)) #adjusted front underarm side - Should be on line a9-10. Fix this when a10 is created
        a12 = A.addPoint('a12', left(a2, CD.front_waist/2.0)) #temporary front waist side 1 -  to the left of the front waist center

        #front waist dart
        aD1 = A.addPoint('aD1', (a4)) #waist dart point
        aD1.i = A.addPoint('aD1.i', left(a2, 0.9 * CD.bust_distance/2.0)) #waist dart inside leg
        aD1.o = A.addPoint('aD1.o', polar(a4, distance(aD1, aD1.i), angleOfLine(aD1, aD1.i) + angleOfDegree(30))) #temporary waist dart outside leg - front waist dart is 20 degrees - TODO: fix this when a10 is created
        a13 = A.addPoint('a13', lowestP(intersectCircles(a11, CD.side, aD1.o, CD.front_waist/2.0 - distance(a2, aD1.i)))) #temporary waist side 2 - adjusted after creation of waist dart

        #bust dart
        aD2 = A.addPoint('aD2', (a4)) #bust dart point
        aD2.angle = angleOfVector(aD1.i, aD1, aD1.o)/2.0
        aD2.i = A.addPoint('aD2.i', intersectLines(a3, a4, a11, a13)) #bust dart inside leg
        aD2.o = A.addPoint('aD2.o', polar(aD2, distance(aD2, aD2.i), angleOfLine(aD2, aD2.i) - aD2.angle)) #bust dart outside leg
        #TODO: create function pivot(pivot_point, rotation_angle, point_to_pivot)
        a14 = A.addPoint('a14', polar(aD2, distance(aD2, a13), angleOfLine(aD2, a13) - aD2.angle)) #final front waist side - adjusted after creation of bust dart
        (aD1.o.x, aD1.o.y) = polar(aD1, distance(aD1, aD1.o), angleOfLine(aD1, aD1.o) - aD2.angle) #pivot aD1.o down

        #create curve at dart base
        ##adjustDartLength(a14, aD1, a2, extension=0.25) #smooth waistline curve from a14 to a2 at dart
        foldDart2(aD1, a2) #creates aD1.m,aD1.oc,aD1.ic; dart folds in toward waist center a2
        #do not call adjustDartLength(a12,aD2,a11) -- bust dart aD2 is not on a curve
        foldDart2(aD2, a11) #creates aD2.m,aD2.oc,aD2.ic; dart folds up toward underarm side a11

        #Bodice Front A control points
        #b/w a6 front neck point & a1 front neck center
        a6.addOutpoint(down(a6, abs(a1.y - a6.y)/2.0))
        a1.addInpoint(left(a1, 0.75 * abs(a1.x - a6.x)))
        #b/w aD1.o waist dart outside leg & a14 front waist side - short control handles
        aD1.o.addOutpoint(polar(aD1.o, distance(aD1.o, a14)/6.0, angleOfLine(aD1.o, aD1) - (angleOfLine(aD1.i, aD1) - ANGLE180))) #control handle foms line with a2,aD1.i
        a14.addInpoint(polar(a14, distance(aD1.o, a14)/6.0, angleOfLine(a14, aD2.o) + ANGLE90)) #control handle is perpendicular to side seam at waist
        #b/w a7 front underarm point & a5 front shoulder point
        a5.addInpoint(polar(a5, distance(a7, a5)/6.0, angleOfLine(a5, a6) + ANGLE90)) #short control handle perpendicular to shoulder seam
        a7.addOutpoint(polar(a7, distance(a7, a5)/3.0, angleOfLine(a7, a6))) #control handle points to front neck point
        #b/w a11 front underarm side & a7 front underarm point
        a7.addInpoint(polar(a7, distance(a11, a7)/3.0, angleOfLine(a6, a7)))
        a11.addOutpoint(polar(a11, distance(a11, a7)/3.0, angleOfLine(aD2.i, a11) + ANGLE90)) #control handle is perpendicular to side seam at underarm

        #draw Bodice Front A
        pnt1 = dPnt(midPoint(a7, a8))
        A.setLabelPosition((pnt1))
        A.setLetter(up(pnt1, 0.5*IN), scaleby=10.0)

        aG1 = dPnt(left(a8, distance(a8, pnt1)/4.0))
        aG2 = dPnt(down(aG1, distance(a1, a2)/2.0))
        A.addGrainLine(aG1, aG2)

        A.addGridLine(['M', a1, 'L', a2, 'L', a5, 'M', a8, 'L', a9, 'M', a1, 'L', a5, 'M', a3, 'L', a4, 'M', a2, 'L', a12, 'M', a4, 'L', a6, 'L', a7, 'M', a11, 'L', a13])

        A.addDartLine(['M', aD1.ic, 'L', aD1, 'L', aD1.oc, 'M', aD2.ic, 'L', aD2, 'L', aD2.oc])

        pth = (['M', a1, 'L', a2, 'L', aD1.i, 'L', aD1.m, 'L', aD1.o, 'C', a14, 'L', aD2.o, 'L', aD2.m, 'L', aD2.i, 'L', a11, 'C', a7, 'C', a5, 'L', a6, 'C', a1])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

