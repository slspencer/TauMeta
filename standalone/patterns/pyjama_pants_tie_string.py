#!/usr/bin/env python
# patternName: pyjama_pants_tie_waist
# patternNumber: pyjama_pants_tie_waist

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
        self.setInfo('patternNumber', 'pyjama_pants_tie_waist')
        self.setInfo('patternTitle', 'pyjama_pants_tie_waist')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'S. L. Spencer')
        self.setInfo('patternmakerName', 'S. L. Spencer')
        self.setInfo('description', """Pyjama pants with tie waist""")
        self.setInfo('category', 'Loungewear')
        self.setInfo('type', 'Pyjamas')
        self.setInfo('gender', '') # 'M',  'F',  or ''
        #
        # The next group are all optional
        #
        self.setInfo('recommendedFabric', 'Cotton, Flannel')
        self.setInfo('recommendedNotions', 'Bias tape for tie waist')
        #
        self.setInfo('yearstart', '1910' )
        #self.setInfo('yearend', '')
        self.setInfo('culture', 'Modern')
        #self.setInfo('wearer', '')
        #self.setInfo('source', '')
        #self.setInfo('characterName', '')
        #
        #get client data
        CD = self.CD #client data is prefaced with CD
        #
        #create pattern called 'pants'
        pants = self.addPattern('pants')
        #
        #create pattern pieces
        A = pants.addPiece('Pants', 'A', fabric = 2, interfacing = 0, lining = 0)
        elastic_width = 1 * IN
        casement_width = 2 * elastic_width
        hem_width = 2 * IN
        
        #---Front points---#
        front_half_hip = 0.503 * CD.front_hip
        FWS = A.addPoint('FWS', (0,0)) #front waist side
        FWC = A.addPoint('FWC', right(FWS, front_half_hip)) #front waist center
        FCS = A.addPoint('FHS', down(FWS, CD.rise)) #front crotch side
        FCC = A.addPoint('FCC', (FWC.x, FCS.y)) #front crotch center
        FCP = A.addPoint('FCP', right(FCC, 0.25 * front_half_hip)) #front crotch point
        FHemS = A.addPoint('FHemS', down(FWS, CD.outseam)) #front hem side
        FHemC = A.addPoint('FHemC', right(FHemS, 0.9 * front_half_hip)) #front hem center
        a1 = A.addPoint('a1', up(FWS, casement_width)) #front waist casing side
        a2 = A.addPoint('a2', (FCC.x, a1.y)) #front waist casing side
        a3 = A.addPoint('a3', up(FCC, distance(FCC, FCP))) #front pattern point along curve
        a4 = A.addPoint('a4', up(FHemC, hem_width)) #pattern point to allow smooth hem
        a5 = A.addPoint('a5', down(FHemS, hem_width)) #pattern point to add hem width, side
        a6 = A.addPoint('a6', down(FHemC, hem_width)) #pattern point to add hem width, center
        #front control points, clockwise
        #b/w a3 & FCP
        a3.addOutpoint(down(a3, 0.5 * abs(a3.y - FCP.y)))
        FCP.addInpoint(left(FCP, 0.5 * abs(a3.x - FCP.x)))
        #b/w FCP & a4
        FCP.addOutpoint(onLineAtLength(FCP, FHemC, 0.33 * distance(FCP, a4))) #point to FHemC to give more thigh room
        a4.addInpoint(up(a4, 0.1 * distance(FCP, a4)))  #short control handle   
        
        #---Back points---#
        back_half_hip = 0.503 * CD.back_hip
        BCC = A.addPoint('BCC', left(FCS, back_half_hip)) #back crotch center 
        BCP = A.addPoint('BCP', left(BCC, 0.25 * back_half_hip)) #back crotch point               
        a7 = A.addPoint('a7', left(FWS, back_half_hip)) #pattern point to calculate back waist center
        a8 = A.addPoint('a8', right(a7, 0.1 * back_half_hip)) #pattern point to calculate back waist center
        a9 = A.addPoint('a9', midPoint(a8, BCC)) #back pattern point along curve
        BWC = A.addPoint('BWC', extendLine(a9, a8, 0.1 * back_half_hip)) #back waist center        
        BHemC = A.addPoint('BHemC', left(FHemS, 1.1 * distance(FHemC, FHemS))) #back hem side
        a10 = A.addPoint('a10', up(BHemC, distance(FHemC, a4))) #pattern point to allow smooth hem
        a11 = A.addPoint('a11', down(BHemC, distance(FHemC, a6))) #pattern point to add hem width, center
        angle1 = angleOfLine(BWC, a8) - ANGLE90
        angle2 = ANGLE270 - angle1
        a12 = A.addPoint('a12', up(BWC, casement_width)) #back waist casing pattern point
        a13 = A.addPoint('a13', intersectLineRay(a12, FWS, BWC, angle2)) #back waist casing center
        #back control points, clockwise
        #b/w a10 & BCP
        a10.addOutpoint(up(a10, 0.1 * distance(a10, BCP)))  #short control handle 
        BCP.addInpoint(onLineAtLength(BCP, BHemC, 0.33 * distance(a10, BCP))) #point to BHemC to give more thigh room        
        #b/w BCP & a9
        BCP.addOutpoint(midPoint(BCP, BCC))      
        a9.addInpoint(midPoint(a9, BCC))

        #draw Front A
        pnt1 = dPnt(midPoint(FCS, FCC))
        pnt2 = dPnt((pnt1.x, a3.y))
        A.setLabelPosition((pnt1.x, pnt1.y))
        A.setLetter((pnt2.x, pnt2.y), scaleby=10.0)
        AG1 = dPnt(down(pnt1, 0.1 * distance(FCS, FHemS)))
        AG2 = dPnt(down(AG1, 0.75 * distance(FCS, FHemS)))
        A.addGrainLine(AG1, AG2)
        pth = (['M', BWC, 'L', FWS, 'L', FWC])
        A.addFoldLine(pth)
        A.addGridLine(['M', BCC, 'L', a7, 'L', FWC, 'L', FCC, 'M', BHemC, 'L', BCP, 'L', FCP, 'L', FHemC, 'M', FWS, 'L', a5])
        pth = (['M', a1, 'L', a2, 'L', a3, 'C', FCP, 'C', a4, 'L', a6, 'L', a11, 'L', a10, 'C', BCP, 'C', a9, 'L', BWC, 'L', a13, 'L', a1])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

