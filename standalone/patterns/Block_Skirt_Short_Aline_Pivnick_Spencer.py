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
        self.setInfo('patternTitle', 'Block/Women/Skirt - Short A-line - Pivnick & Spencer')
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
        #90px / 1 in
        #2.54cm / 1 in
        #90 / 2.54  = px / cm

        #---Front A---#
        FRONT_DART = 'false'
        SKIRT_LENGTH = 0.5 * CD.hip_to_floor
        FWC = A.addPoint('FWC', (0, 0)) #front waist center
        FHC = A.addPoint('FHC', down(FWC, CD.front_hip_height)) #front hip center
        FHEMC = A.addPoint('FHEMC', down(FHC, SKIRT_LENGTH)) #front hem center
        FHEMS = A.addPoint('FHEMS', right(FHEMC, 0.5 * CD.front_hip)) #front hem side
        FHS = A.addPoint('FHS', up(FHEMS, SKIRT_LENGTH)) #front hip side
        FWS1 = A.addPoint('FWS1', up(FHS, CD.side_hip_height)) #front waist side 1
        front_dart_width = 0.065 * CD.front_waist
        FWS = A.addPoint('FWS', rightmostP(intersectCircles(FWC, 0.5 * CD.front_waist + front_dart_width, FHS, CD.side_hip_height))) #front waist side - includes 6.5% for dart width
         #approx 3/4" for 24" waist
        #front waist dart
        FD1 = A.addPoint('FD1', left(FWS, 0.33 * CD.front_waist / 2.0)) #front waist dart - will be updated later
        FD1.o = A.addPoint('FD1.o', FD1) #front waist dart outside leg
        FD1.i = A.addPoint('FD1.i', left(FD1.o, front_dart_width)) #front waist dart inside leg
        FD1.m = midPoint(FD1.i, FD1.o)
        updatePoint(FD1, down(FD1.m, 0.75 * CD.side_hip_height)) #front waist dart point
        extendDart(FWS, FD1, FWC)
        foldDart(FD1, FWC)
        #front abdoment adjustment
        FABC = A.addPoint('FABC', down(FWC, 0.4 * CD.front_hip_height)) #front abdomen center
        FABC1 = A.addPoint('FABC1', intersectLineRay(FD1, FD1.i, FABC, angleOfLine(FWC, FWS))) #front abdomen line at dart inside leg
        FABS1 = A.addPoint('FABS1', onLineAtY(FD1, FD1.o, FABC1.y)) # front abdomen line at dart outside leg
        FABS = A.addPoint('FABS', polar(FABS1, CD.front_abdomen / 2.0 - distance(FABC,  FABC1), angleOfLine(FWC, FWS))) #front abdomen line at skirt side
        #front control handles
        #b/w FHS front hip side & FabS front abdomen side
        FHS.addOutpoint(up(FHS, distance(FHS, FABS) / 3.0))
        FABS.addInpoint(polar(FABS, distance(FHS, FABS) / 3.0, angleOfLine(FWS, FHS)))
        #b/w FABS front abdomen side & FWS front waist side
        FABS.addOutpoint(polar(FABS, distance(FABS, FWS) / 3.0, angleOfLine(FHS, FWS)))
        FWS.addInpoint(polar(FWS, distance(FABS, FWS) / 3.0, angleOfLine(FWS, FABS.outpoint)))

        #---Back B---#
        BWS1 = B.addPoint('BWS1', FWS1) #back waist side - same as front waist side
        BHS = B.addPoint('BHS', FHS) #back hip side - same as front hip side
        BHEMS = B.addPoint('BHEMS', FHEMS) #back hem side - same as front hem side
        BHEMC = B.addPoint('BHEMC', right(BHEMS, 0.5 * CD.back_hip)) #back hem center
        BHC = B.addPoint('BHC', up(BHEMC, SKIRT_LENGTH)) #back hip center
        BWC = B.addPoint('BWC', up(BHC, CD.back_hip_height)) #back waist center
        #back waist dart
        total_back_dart_width = 0.5 * (CD.back_hip - CD.back_waist)
        back_dart_width = (2 / 3.0) * total_back_dart_width
        #back waist dart
        BD1 = B.addPoint('BD1', onLineAtLength(BWC, BWS1, 0.25 * CD.back_waist))
        BD1.i = B.addPoint('BD1.i', BD1) #back waist dart inside leg
        BD1.o = B.addPoint('BD1.o', left(BD1.i, back_dart_width)) #back waist dart outside leg
        BD1.m = midPoint(BD1.i, BD1.o)
        updatePoint(BD1, down(BD1.m, 0.9 * CD.back_hip_height))
        BWS = B.addPoint('BWS', highestP(intersectCircles(BHS, CD.side_hip_height, BD1.o, 0.25 * CD.back_waist))) #back waist side
        extendDart(BWS, BD1, BWC)
        foldDart(BD1, BWC)
        #back abdomen adjustment
        BABC = B.addPoint('BABC', down(BWC, 0.4 * CD.back_hip_height)) #back abdomen center
        BABC1 = B.addPoint('BABC1', intersectLineRay(BD1, BD1.i, BABC, angleOfLine(BWC, BWS))) #back abdomen line at dart inside leg
        BABS1 = B.addPoint('BABS1', onLineAtY(BD1, BD1.o, BABC1.y)) #back abdomen line at dart outside leg
        BABS = B.addPoint('BABS', polar(BABS1, CD.back_abdomen / 2.0 - distance(BABC,  BABC1), angleOfLine(BWC, BWS))) #back abdomen line at skirt side
        #back control handles
        #b/w BHS back hem side & BABS back abdomen side
        BHS.addOutpoint(up(BHS, distance(BHS, BABS) / 3.0))
        BABS.addInpoint(polar(BABS, distance(BHS, BABS) / 3.0, angleOfLine(BWS, BHS)))
        #b/w BABS back abdomen side & BWS back waist side
        BABS.addOutpoint(polar(BABS, distance(BABS, BWS) / 3.0, angleOfLine(BHS, BWS)))
        BWS.addInpoint(polar(BWS, distance(BABS, BWS) / 3.0, angleOfLine(BWS, BABS.outpoint)))

        #draw Skirt Front A
        pnt1 = dPnt((FWC.x + 0.25 * abs(FWC.x - FWS.x), FHC.y + 0.25 * abs(FHEMC.y - FHC.y)))
        A.setLabelPosition((pnt1.x, pnt1.y))
        A.setLetter(up(pnt1, 0.5 * IN), scaleby=10.0)
        AG1 = dPnt((FD1.x, FHC.y))
        AG2 = dPnt(down(AG1, 0.8 * distance(FHC, FHEMC)))
        A.addGrainLine(AG1, AG2)
        A.addGridLine(['M', FWC, 'L', FHEMC, 'L', FHEMS, 'L', FWS1, 'M', FHS, 'L', FWS, 'L', FWC, 'M', FHC, 'L', FHS, 'M', FABC, 'L', FABC1, 'L', FABS1, 'L', FABS])
        A.addDartLine(['M', FD1.ic, 'L', FD1, 'L', FD1.oc])
        pth = (['M', FWC, 'L', FHEMC, 'L', FHEMS, 'L', FHS, 'C', FABS, 'C', FWS, 'L', FD1.o, 'L', FD1.m, 'L', FD1.i, 'L', FWC])
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
        B.addGridLine(['M', BWC, 'L', BHEMC, 'L', BHEMS, 'L', BWS1, 'M', BHS, 'L', BWS, 'L', BWC, 'M', BHC, 'L', BHS, 'M', BABC, 'L', BABC1, 'L', BABS1, 'L', BABS])
        pth = (['M', BWC, 'L', BHEMC, 'L', BHEMS, 'L', BHS, 'C', BABS, 'C', BWS, 'L', BD1.o, 'L', BD1.m, 'L', BD1.i, 'L', BWC])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

