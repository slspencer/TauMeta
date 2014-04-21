#!/usr/bin/env python
# patternName: Mens_Jeans_Classic_1950s
# patternNumber: M_J_Classic_1950s

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
        self.setInfo('patternNumber', 'M_J_Classic_1950s')
        self.setInfo('patternTitle', 'Mens_Jeans_Classic_1950s')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'S. L. Spencer')
        self.setInfo('patternmakerName', 'S. L. Spencer')
        self.setInfo('description', """Men's Jeans - Classic 1950s cut""")
        #TODO: add new category 'Block Patterns'
        self.setInfo('category', 'Pants')
        self.setInfo('type', 'Jeans')
        self.setInfo('gender', 'M') # 'M',  'F',  or ''
        #
        # The next group are all optional
        #
        self.setInfo('recommendedFabric', 'denim')
        self.setInfo('recommendedNotions', 'zipper, heavy topstitch thread')
        #
        self.setInfo('yearstart', '1940' )
        #self.setInfo('yearend', '')
        self.setInfo('culture', 'Modern')
        #self.setInfo('wearer', '')
        #self.setInfo('source', '')
        #self.setInfo('characterName', '')
        #
        #get client data
        CD = self.CD #client data is prefaced with CD
        #
        #create pattern called 'jeans'
        jeans = self.addPattern('jeans')
        #
        #create pattern pieces
        A = jeans.addPiece('Front', 'A', fabric = 2, interfacing = 0, lining = 0)

        #---new measurements---
        #90px / 1 in - Inkscape default
        #2.54cm / 1 in
        #90 / 2.54  = px / cm

        #---Front A---#
        #quick measurements
        front_scale = CD.front_hip
        front_half_waist = CD.front_waist / 2.0
        front_half_hip = CD.front_hip / 2.0
        waistband_stand = 0.15 * CD.rise #front height of waistband - 2*waistband_stand + 2*seam allowances = actual waistband width

        FHM = A.addPoint('FHM', (0, 0)) #front hip middle
        FWM = A.addPoint('FWM', up(FHM, CD.rise - waistband_stand))
        FHemM = A.addPoint('FHemM', down(FHM, CD.inseam)) #front hem middle
        FKM = A.addPoint('FKM', down(FHM, 0.44 * CD.inseam)) #front knee middle
        FHM1 = A.addPoint('FHM1', left(FHM, front_scale / 6.0)) #point on hip line 1
        FHM2 = A.addPoint('FHM2', left(FHM1, 0.0375 * front_scale)) #point on hip line 2
        FCP = A.addPoint('FCP', left(FHM2, 0.127 * front_scale)) #front crotch point
        FHS = A.addPoint('FHS', right(FHM, 0.308 * front_scale)) #front hip side

        p1 = A.addPoint('p1', up(FHM2, distance(FHM, FWM))) #p1 - calculates FWC
        FWS = A.addPoint('FWS', right(p1, 1.032 * front_half_waist)) #front waist side
        FWC = A.addPoint('FWC', right(p1, 0.063 * front_half_waist)) #front waist center
        FLY1 = A.addPoint('FLY1', (FHM2.x - distance(p1, FWC), FHM2.y - 2 * distance(p1, FWC))) #fly point 1
        FLY2 = A.addPoint('FLY2', polar(FLY1, 3 * distance(p1, FWC), angleOfLine(FWC, FLY1) + ANGLE90)) #fly point 2
        FLY3 = A.addPoint('FLY3', polar(FLY2, distance(FWC, FLY1), angleOfLine(FLY1, FWC)))
        p2 = A.addPoint('p2', midPoint(FCP, FHM2)) #point on hip line midway b/w FCP front crotch point & FHM2 front hem middle 2
        FHemC = A.addPoint('FHemC', left(FHemM, 0.283 * CD.calf)) #front hem center
        FHemS = A.addPoint('FHemS', right(FHemM, 0.283 * CD.calf)) #front hem center
        p3 = A.addPoint('p3', onLineAtY(p2, FHemC, FKM.y)) #p3 on front knee line
        p4 = A.addPoint('p4', onLineAtY(FHS, FHemS, FKM.y)) #p4 on front knee line
        FKC = A.addPoint('FKC', right(p3, 0.017 * CD.calf)) #front knee center
        FKS = A.addPoint('FKS', left(p4, 0.017 * CD.calf)) #front knee side

        p5 = A.addPoint('p5', up(FHM1, 0.33 * front_scale)) #directly above FHM1
        p6 = A.addPoint('p6', up(FHM1, front_half_waist)) #directly above p5
        p7 = A.addPoint('p7', midPoint(p5, p6)) #midpoint b/w p5 & p6
        p8 = A.addPoint('p8', onLineAtLength(FWS, FHS, 0.45 * distance(FWS, FHS)))
        p9 = A.addPoint('p9', (FHS.x, p8.y)) #directly above FHS - for finding FPoc1 pocket side 1
        FPoc1 = A.addPoint('FPoc1', midPoint(p8, p9)) #FPoc1 front pocket 1 - at side
        FPoc2 = A.addPoint('FPoc2', (FHS.x, FLY1.y)) #front pocket 2 - at side
        FPoc4 = A.addPoint('FPoc4', midPoint(FWC, FWM)) #front pocket 4 - at waist
        FPoc3 = A.addPoint('FPoc3', (FPoc4.x, FPoc2.y)) #front pocket 3 - pocket inside corner





        #draw Jeans Front A
        pnt1 = FHM
        A.setLabelPosition((pnt1.x, pnt1.y))
        A.setLetter(up(pnt1, 0.5 * IN), scaleby=10.0)
        AG1 = dPnt(down(FHM, 2 * IN))
        AG2 = dPnt(down(AG1, 0.75 * distance(FHM, FHemM)))
        A.addGrainLine(AG1, AG2)
        pth = (['M', FCP, 'L', FHS, 'M', p1, 'L', FHM2, 'M', FWS, 'L', FHS, 'M', FWC, 'L', FLY1, 'M', p2, 'L', FHemC, 'M', FHS, 'L', FHemS, 'M', p3, 'L', p4])
        pth += (['M', FPoc1, 'L', FPoc2, 'L', FPoc3, 'L', FPoc4, 'L', FWM, 'L', FPoc1]) #pocket
        A.addGridLine(pth)
        pth = (['M', FWC, 'L', FWM, 'L', FWS, 'L', FPoc1, 'L', FHS, 'L', FKS, 'L', FHemS, 'L', FHemC, 'L', FKC, 'L', FCP, 'L', FLY1, 'L', FLY2, 'L', FLY3, 'L', FWC, 'M', FHM1, 'L', p6])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

