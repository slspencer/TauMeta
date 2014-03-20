#!/usr/bin/env python
# patternName: Block_Women_Bodice_Short_Fitted_WaistDart_NeckDart_Pivnick/Spencer
# patternNumber: BL_W_Skirt_Short_A-line_Pivnick_Spencer

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
        self.setInfo('patternNumber', 'BL_W_Skirt_A-line_Pivnick_Spencer')
        self.setInfo('patternTitle', 'Block/Women/Skirt - Short A-line - Pivnick and Spencer')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'Ester Pivnick')
        self.setInfo('patternmakerName', 'S. L. Spencer')
        self.setInfo('description', """Women's short A-line skirt block with front & back waist darts, includes major changes to Ester Pivnick's original forumalas.""")
        #TODO: add new category 'Block Patterns'
        self.setInfo('category', 'Block')
        self.setInfo('type', 'Skirt')
        self.setInfo('gender', 'F') # 'M',  'F',  or ''
        #
        # The next group are all optional
        #
        self.setInfo('recommendedFabric', '')
        self.setInfo('recommendedNotions', '')
        #
        self.setInfo('yearstart', '1930' )
        #self.setInfo('yearend', '')
        self.setInfo('culture', 'Modern')
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
        A = bodice.addPiece('Front', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = bodice.addPiece('Back', 'B', fabric = 2, interfacing = 0, lining = 0)

        #---new measurements---
        #90px / 1 in - Inkscape default
        #2.54cm / 1 in
        #90 / 2.54  = px / cm

        #---Front A---#
        SKIRT_LENGTH = 0.5 * CD.hip_to_floor
        front_half_waist = CD.front_waist / 2.0
        front_half_hip = CD.front_hip / 2.0
        front_half_abdomen = CD.front_abdomen / 2.0
        FWC = A.addPoint('FWC', (0, 0)) #front waist center
        FHC = A.addPoint('FHC', down(FWC, CD.front_hip_height)) #front hip center
        FHEMC = A.addPoint('FHEMC', down(FHC, SKIRT_LENGTH)) #front hem center
        FHEMS1 = A.addPoint('FHEMS1', right(FHEMC, front_half_hip)) #front hem side
        FHEMS2 = A.addPoint('FHEMS2', right(FHEMS1, 0.045 * CD.hip)) #extend hem to side by 4.5% of full hip girth for minimal walking room
        FHS = A.addPoint('FHS', up(FHEMS1, SKIRT_LENGTH)) #front hip side
        FHEMS = A.addPoint('FHEMS', onLineAtLength(FHS, FHEMS2, distance(FHS, FHEMS1))) #keep side hem the right length
        FWS1 = A.addPoint('FWS1', up(FHS, CD.side_hip_height)) #front waist side 1
        front_dart_width = 0.13 * front_half_waist
        FWS = A.addPoint('FWS', rightmostP(intersectCircles(FWC, front_half_waist + front_dart_width, FHS, CD.side_hip_height))) #front waist side - includes 6.5% for dart width
         #approx 3/4" for 24" waist
        #front waist dart
        FD1 = A.addPoint('FD1', right(FWC, 0.7 * front_half_waist)) #front waist dart - will be updated later
        FD1.o = A.addPoint('FD1.o', FD1) #front waist dart outside leg
        FD1.i = A.addPoint('FD1.i', left(FD1.o, front_dart_width)) #front waist dart inside leg
        FD1.m = midPoint(FD1.i, FD1.o)
        updatePoint(FD1, down(FD1.m, 0.8 * CD.side_hip_height)) #front waist dart point
        extendDart(FWS, FD1, FWC)
        foldDart(FD1, FWC)
        #front abdoment adjustment
        FABC = A.addPoint('FABC', down(FWC, 0.33 * CD.front_hip_height)) #front abdomen center
        FABC1 = A.addPoint('FABC1', intersectLineRay(FD1, FD1.i, FABC, angleOfLine(FWC, FWS))) #front abdomen line at dart inside leg
        FABS1 = A.addPoint('FABS1', onLineAtY(FD1, FD1.o, FABC1.y)) # front abdomen line at dart outside leg
        FABS2 = A.addPoint('FABS2', polar(FABS1, front_half_abdomen - distance(FABC,  FABC1), angleOfLine(FWC, FWS))) #front abdomen line at skirt side
        #FABS front abdomen side shouldn't be inside the line from FHS to FWS else the side seam at abdomen line would be concave :(
        FABS3 = A.addPoint('FABS3', intersectLines(FWS, FHS, FABS1, FABS2))
        if distance(FABS1, FABS2) < distance(FABS1, FABS3):
            FABS = A.addPoint('FABS', FABS3)
        else:
            FABS = A.addPoint('FABS', FABS2)
        #front control handles
        #b/w FHEMS1 front hem side 1 & FHEMS front hem side
        FHEMS1.addOutpoint(right(FHEMS1, distance(FHEMS1, FHEMS) / 6.0)) #short control handle
        FHEMS.addInpoint(polar(FHEMS, distance(FHEMS1, FHEMS) / 6.0, angleOfLine(FHS, FHEMS) + ANGLE90)) #short control handle
        #b/w FHEMS front hem side & FHS front hip side
        FHEMS.addOutpoint(polar(FHEMS, distance(FHEMS, FHS) / 6.0, angleOfLine(FHEMS, FHS))) #short control handle
        FHS.addInpoint(polar(FHS, distance(FHEMS, FHS) / 6.0,  angleOfLine(FABS, FHEMS))) #short control handle
        #b/w FHS front hip side & FABS front abdomen side
        FHS.addOutpoint(polar(FHS, distance(FHS, FABS) / 6.0, angleOfLine(FHEMS, FABS))) #short control handle
        FABS.addInpoint(polar(FABS, distance(FHS, FABS) / 6.0, angleOfLine(FWS, FHS))) #short control handle
        #b/w FABS front abdomen side & FWS front waist side
        FABS.addOutpoint(polar(FABS, distance(FABS, FWS) / 6.0, angleOfLine(FHS, FWS))) #short control handle
        FWS.addInpoint(polar(FWS, distance(FABS, FWS) / 6.0, angleOfLine(FWS, FABS.outpoint))) #short control handle
        #b/w FWS front waist side & FD1.o front dart outside leg
        FWS.addOutpoint(polar(FWS, distance(FWS, FD1.o) / 6.0, angleOfLine(FWS, FWS.inpoint) + ANGLE90)) #short control handle
        FD1.o.addInpoint(polar(FD1.o, distance(FWS, FD1.o) / 6.0, angleOfLine(FD1, FD1.o) + ANGLE90)) #short control handle
        #b/w FD1.i front waist dart inside leg & FWC front waist center
        FD1.i.addOutpoint(polar(FD1.i, distance(FD1.i, FWC) / 6.0, angleOfLine(FD1.i, FD1) + ANGLE90)) #short control handle
        FWC.addInpoint(right(FWC, distance(FD1.i, FWC) / 6.0)) #short control handle

        #---Back B---#
        back_half_waist = CD.back_waist / 2.0
        back_half_hip = CD.back_hip / 2.0
        back_half_abdomen = CD.back_abdomen / 2.0
        BWS1 = B.addPoint('BWS1', FWS1) #back waist side - same as front waist side
        BHS = B.addPoint('BHS', FHS) #back hip side - same as front hip side
        BHEMS1 = B.addPoint('BHEMS1', FHEMS1) #back hem side - same as front hem side
        BHEMS2 = B.addPoint('BHEMS2', left(BHEMS1, distance(FHEMS1, FHEMS2))) #extend back hem width, equal to front hem width extension
        BHEMS = B.addPoint('BHEMS', onLineAtLength(BHS, BHEMS2, distance(BHS, BHEMS1))) #keep side hem the correct length
        BHEMC = B.addPoint('BHEMC', right(BHEMS1, back_half_hip)) #back hem center
        BHC = B.addPoint('BHC', up(BHEMC, SKIRT_LENGTH)) #back hip center
        BWC = B.addPoint('BWC', up(BHC, CD.back_hip_height)) #back waist center
        #back waist dart
        total_back_dart_width = back_half_hip - back_half_waist
        back_dart_width = (2 / 3.0) * total_back_dart_width
        #back waist dart
        BD1 = B.addPoint('BD1', onLineAtLength(BWC, BWS1, 0.6 * back_half_waist))
        BD1.i = B.addPoint('BD1.i', BD1) #back waist dart inside leg
        BD1.o = B.addPoint('BD1.o', left(BD1.i, back_dart_width)) #back waist dart outside leg
        BD1.m = midPoint(BD1.i, BD1.o)
        updatePoint(BD1, down(BD1.m, 0.9 * CD.back_hip_height))
        BWS = B.addPoint('BWS', highestP(intersectCircles(BHS, CD.side_hip_height, BD1.o, back_half_waist - distance(BWC, BD1.i)))) #back waist side
        #extendDart(BWS, BD1, BWC)
        foldDart(BD1, BWC)
        #back abdomen adjustment
        BABC = B.addPoint('BABC', down(BWC, 0.3 * CD.back_hip_height)) #back abdomen center
        BABC1 = B.addPoint('BABC1', intersectLineRay(BD1, BD1.i, BABC, angleOfLine(BWC, BWS))) #back abdomen line at dart inside leg
        BABS1 = B.addPoint('BABS1', onLineAtY(BD1, BD1.o, BABC1.y)) #back abdomen line at dart outside leg
        BABS2 = B.addPoint('BABS2', polar(BABS1, back_half_abdomen - distance(BABC,  BABC1), angleOfLine(BD1.o, BWS))) #back abdomen line at skirt side
        #BABS back abdomen side shouldn't be inside the line from BHS to BWS else the side seam at abdomen line would be concave :(
        BABS3 = B.addPoint('BABS3', intersectLines(BWS, BHS, BABS1, BABS2))
        if distance(BABS1, BABS2) < distance(BABS1, BABS3):
            BABS = B.addPoint('BABS', BABS3)
        else:
            BABS = B.addPoint('BABS', BABS2)
        #back control handles
        #b/w BHEMS1 back hem side 1 & BHEMS back hem side
        BHEMS1.addOutpoint(left(BHEMS1, distance(BHEMS1, BHEMS) / 3.0))
        BHEMS.addInpoint(polar(BHEMS, distance(BHEMS1, BHEMS) / 3.0, angleOfLine(BHEMS, BHS) + ANGLE90))
        #b/w BHEMS back hem side & BHS back hip side
        BHEMS.addOutpoint(polar(BHEMS, distance(BHEMS, BHS) / 3.0, angleOfLine(BHEMS, BHS)))
        BHS.addInpoint(polar(BHS, distance(BHEMS, BHS) / 3.0, angleOfLine(BABS, BHEMS)))
        #b/w BHS back hip side & BABS back abdomen side
        BHS.addOutpoint(polar(BHS, distance(BHS, BABS) / 3.0, angleOfLine(BHEMS, BABS)))
        BABS.addInpoint(polar(BABS, distance(BHS, BABS) / 3.0, angleOfLine(BWS, BHS)))
        #b/w BABS back abdomen side & BWS back waist side
        BABS.addOutpoint(polar(BABS, distance(BABS, BWS) / 3.0, angleOfLine(BHS, BWS)))
        BWS.addInpoint(polar(BWS, distance(BABS, BWS) / 3.0, angleOfLine(BWS, BABS.outpoint)))
        #b/w BWS back waist side & BD1.o back dart outside leg
        BWS.addOutpoint(polar(BWS, distance(BWS, BD1.o) / 6.0, angleOfLine(BWS.inpoint, BWS) + ANGLE90)) #short control handle
        BD1.o.addInpoint(polar(BD1.o, distance(BWS, BD1.o) / 6.0, angleOfLine(BD1.o, BD1) + ANGLE90)) #short control handle
        #b/w FD1.i front waist dart inside leg & FWC front waist center
        BD1.i.addOutpoint(polar(BD1.i, distance(BD1.i, BWC) / 6.0, angleOfLine(BD1, BD1.i) + ANGLE90)) #short control handle
        BWC.addInpoint(left(BWC, distance(BD1.i, BWC) / 6.0)) #short control handle


        print('CD.front_waist/2.0 =', CD.front_waist/2.0  / CM)
        print('pattern front waist/2.0 =', distance(FWS, FD1.o) + distance(FD1.i, FWC)  / CM)
        print('CD.back_waist/2.0 =', CD.back_waist/2.0  / CM)
        print('pattern back waist/2.0 =', distance(BWS, BD1.o) + distance(BD1.i, BWC)  / CM)

        print('CD.front_hip/2.0 =', CD.front_hip/2.0   / CM)
        print('pattern front hip/2.0 =', distance(FHS, FHC)   / CM)
        print('CD.back_hip/2.0 =', CD.back_hip/2.0   / CM)
        print('pattern back hip/2.0 =', distance(BHS, BHC)   / CM)

        #draw Skirt Front A
        pnt1 = dPnt((FWC.x + 0.25 * abs(FWC.x - FWS.x), FHC.y + 0.25 * abs(FHEMC.y - FHC.y)))
        A.setLabelPosition((pnt1.x, pnt1.y))
        A.setLetter(up(pnt1, 0.5 * IN), scaleby=10.0)
        AG1 = dPnt((FD1.x, FHC.y))
        AG2 = dPnt(down(AG1, 0.8 * distance(FHC, FHEMC)))
        A.addGrainLine(AG1, AG2)
        A.addGridLine(['M', FWC, 'L', FHEMC, 'L', FHEMS1, 'L', FWS1, 'M', FHS, 'L', FWS, 'L', FWC, 'M', FHC, 'L', FHS, 'M', FABC, 'L', FABC1, 'L', FABS1, 'L', FABS])
        A.addDartLine(['M', FD1.ic, 'L', FD1, 'L', FD1.oc])
        pth = (['M', FWC, 'L', FHEMC, 'L',  FHEMS1, 'C', FHEMS, 'C', FHS, 'C', FABS, 'C', FWS, 'C', FD1.o, 'L', FD1.m, 'L', FD1.i, 'C', FWC])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        #draw Skirt Back B
        pnt1 = dPnt((BWS.x + 0.5 * distance(BWS, BD1.o), BHC.y + 0.25 * distance(BHC, BHEMC)))
        B.setLabelPosition((pnt1.x, pnt1.y))
        B.setLetter(up(pnt1, 0.5 * IN), scaleby=10.0)
        BG1 = dPnt((BD1.x, BHC.y))
        BG2 = dPnt(down(BG1, 0.8 * distance(BHC, BHEMC)))
        B.addGrainLine(BG1, BG2)
        B.addDartLine(['M', BD1.ic, 'L', BD1, 'L', BD1.oc])
        B.addGridLine(['M', BWC, 'L', BHEMC, 'L', BHEMS1, 'L', BWS1, 'M', BHS, 'L', BWS, 'L', BWC, 'M', BHC, 'L', BHS, 'M', BABC, 'L', BABC1, 'L', BABS1, 'L', BABS])
        pth = (['M', BWC, 'L', BHEMC, 'L', BHEMS1, 'C', BHEMS, 'C', BHS, 'C', BABS, 'C', BWS, 'C', BD1.o, 'L', BD1.m, 'L', BD1.i, 'C', BWC])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

