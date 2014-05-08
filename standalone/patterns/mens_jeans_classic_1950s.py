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
        B = jeans.addPiece('Front Pocket Lining', 'B', fabric = 2, interfacing = 0, lining = 2)
        C = jeans.addPiece('Back', 'C', fabric = 2, interfacing = 0, lining = 0)
        D = jeans.addPiece('Front Waist Corner', 'D', fabric = 2, interfacing = 0, lining = 0)
        E = jeans.addPiece('Fly', 'E', fabric = 2, interfacing = 2, lining = 2)
        F = jeans.addPiece('Front Waistband', 'F', fabric = 2, interfacing = 2, lining = 2)
        G = jeans.addPiece('Back Waistband', 'G', fabric = 2, interfacing = 2, lining = 2)

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

        FCM = A.addPoint('FCM', (0, 0)) #front crotchline middle
        FWM = A.addPoint('FWM', up(FCM, CD.rise))
        FHemM = A.addPoint('FHemM', down(FCM, CD.inseam)) #front hem middle
        FKM = A.addPoint('FKM', down(FCM, 0.44 * CD.inseam)) #front knee middle
        p5 = A.addPoint('p5', left(FCM, front_scale / 6.0)) #point on crotchline 1
        FCC = A.addPoint('FCC', left(p5, 0.0375 * front_scale)) #front crotch center (not crotch point)
        FCP = A.addPoint('FCP', left(FCC, 0.127 * front_scale)) #front crotch point
        FCS = A.addPoint('FCS', right(FCM, 0.308 * front_scale)) #front hip side

        p1 = A.addPoint('p1', up(FCC, distance(FCM, FWM))) #p1 - calculates FWC
        FWS = A.addPoint('FWS', right(p1, 1.032 * front_half_waist)) #front waist side
        FWC = A.addPoint('FWC', right(p1, 0.063 * front_half_waist)) #front waist center
        FLY1 = A.addPoint('FLY1', (FCC.x - distance(p1, FWC), FCC.y - 2 * distance(p1, FWC))) #fly point 1
        FLY2 = A.addPoint('FLY2', polar(FLY1, 3 * distance(p1, FWC), angleOfLine(FWC, FLY1) + ANGLE90)) #fly point 2
        FLY3 = A.addPoint('FLY3', polar(FLY2, distance(FWC, FLY1), angleOfLine(FLY1, FWC)))
        FLY4 = A.addPoint('FLY4', midPoint(FLY1, FLY2))
        FLY5 = A.addPoint('FLY5', onLineAtLength(FLY2, FLY3, 2 * distance(FLY2, FLY4)))
        p2 = A.addPoint('p2', midPoint(FCP, FCC)) #point on hip line midway b/w FCP front crotch point & FCC front hem middle 2
        FHemC = A.addPoint('FHemC', left(FHemM, 0.283 * CD.calf)) #front hem center
        FHemS = A.addPoint('FHemS', right(FHemM, 0.283 * CD.calf)) #front hem center
        p3 = A.addPoint('p3', onLineAtY(p2, FHemC, FKM.y)) #p3 on front knee line
        p4 = A.addPoint('p4', onLineAtY(FCS, FHemS, FKM.y)) #p4 on front knee line
        FKC = A.addPoint('FKC', right(p3, 0.017 * CD.calf)) #front knee center
        FKS = A.addPoint('FKS', left(p4, 0.017 * CD.calf)) #front knee side
        FHC = A.addPoint('FHC', down(p1, CD.front_hip_height)) #front hip center
        FHS = A.addPoint('FHS', (FCS.x, FHC.y)) #front hip side

        #waistline
        #lower waistline by 33% rise
        waistband_width = 0.15 * CD.rise
        w1 = A.addPoint('w1', onLineAtLength(FWC, FLY1, 0.33 * CD.rise)) #front waistline center
        pnt1 = dPnt((FHS.x, w1.y)) #side point to calc waistline side
        pnt2 = onLineAtY(FHS, FWS, pnt1.y) #side point to calc waistline side
        w2 = A.addPoint('w2', midPoint(pnt1, pnt2)) #front waistline side

        pnt1 = dPnt((w2.x, w2.y - waistband_width)) #side point to calc waistline side
        pnt2 = onLineAtY(w2, FWS, pnt1.y) #side point to calc waistline side
        w3 = A.addPoint('w3', midPoint(pnt1, pnt2)) #front waistline side
        w4 = A.addPoint('w4', up(w1, waistband_width)) #front waistline center

        #front pocket
        pnt1 = dPnt((FHS.x, w2.y + distance(w2, FHS) / 2.0)) #side point to calc waistline side
        pnt2 = onLineAtY(FHS, w2, pnt1.y) #side point to calc waistline side
        FP1 = A.addPoint('FP1', midPoint(pnt1, pnt2)) #front waistline side
        FP2 = A.addPoint('FP2', FP1) #copy FP1 to create curve to FWS
        FPoc4 = A.addPoint('FPoc4', left(w2, 0.75 * distance(w2, w1))) #front pocket 4 - at waist
        FPoc3 = A.addPoint('FPoc3', (FPoc4.x, FCS.y)) #front pocket 3 - pocket inside corner
        FPoc5 = A.addPoint('FPoc5', (FPoc4.x, FHS.y)) #front pocket 5 - jeans material stops at this line, lining begins
        FPoc6 = B.addPoint('FPoc6', extendLine(FPoc5, FPoc3, distance(FPoc3, FPoc5)))
        FPoc7 = B.addPoint('FPoc7', extendLine(FHS, FCS, distance(FPoc3, FPoc5)))
        FPoc8 = A.addPoint('FPoc8', (FPoc3.x, FWC.y))
        FPoc9 = A.addPoint('FPoc9', (FWM.x, FPoc4.y))

        #jeans Front control points
        #b/w FLY5 & FLY4
        FLY5.addOutpoint(midPoint(FLY5, FLY2))
        FLY4.addInpoint(FLY2)
        #b/w FLY1 & FCP front crotch point
        FLY1.addOutpoint(extendLine(FWC, FLY1, 0.25 * (FCP.y - FLY1.y)))
        FCP.addInpoint(extendLine(FWC, FLY1, 0.75 * (FCP.y - FLY1.y)))
        #b/w FCP & FKC front knee center
        FKC.addInpoint(polar(FKC, 0.33 * distance(FCP, FKC), angleOfLine(FHemC, FKC)))
        FCP.addOutpoint(polar(FCP, 0.33 * distance(FCP, FKC), angleOfLine(FCP, FKC.inpoint)))

        #b/w FKS & FCS front crotch side
        FKS.addOutpoint(polar(FKS, 0.33 * distance(FKS, FCS), angleOfLine(FHemS, FKS)))
        FCS.addInpoint(polar(FCS, 0.33 * distance(FKS, FCS), angleOfLine(FHS, FKS)))
        #b/w FCS & FHS front hip side
        FCS.addOutpoint(polar(FCS, 0.33 * distance(FCS, FHS), angleOfLine(FCS.inpoint, FCS)))
        FHS.addInpoint(polar(FHS, 0.33 * distance(FCS, FHS), angleOfLine(FP1, FCS)))
        #b/w FHS & FP1 front pocket 1
        FHS.addOutpoint(polar(FHS, 0.33 * distance(FHS, FP1), angleOfLine(FHS.inpoint, FHS)))
        FP1.addInpoint(polar(FP1, 0.33 * distance(FHS, FP1), angleOfLine(FP1, FHS.outpoint)))
        #b/w FP1 & FWM
        FP1.addOutpoint(left(FP1, 0.5 * abs(FPoc9.x - FP1.x)))
        FPoc9.addInpoint(down(FPoc9, abs(FPoc9.y - FP1.y)))

        #b/w FHS & FP2 duplicate of FP1
        #FHS outpoint is same as above
        FP2.addInpoint(FP1.inpoint)
        # b/ FP2 & w2
        FP2.addOutpoint(polar(FP2, 0.33 * distance(FP2, w2), angleOfLine(FP2.inpoint, FP2)))
        w2.addInpoint(polar(w2, 0.33 * distance(FP2, w2), angleOfLine(w2, FP2.inpoint)))

        #---jeans Back C ---
        back_scale = CD.back_hip
        back_half_waist = CD.back_waist / 2.0
        back_half_hip = CD.back_hip / 2.0
        p6 = C.addPoint('p6', up(p5, 0.33 * front_scale)) #directly above p5
        p7 = C.addPoint('p7', up(p5, front_half_waist)) #directly above p6
        p8 = C.addPoint('p8', midPoint(p6, p7)) #midpoint b/w p6 & p7 - used to find back hip center
        BHC = C.addPoint('BHC', onLineAtY(p2, p8, FHC.y)) #back hip center
        BWC = C.addPoint('BWC', onLineAtLength(BHC, p8, CD.back_hip_height)) #back waist center
        BWS = C.addPoint('BWS', rightmostP(onCircleAtY(BWC, 1.16 * back_half_waist, FWS.y)))
        BCS = C.addPoint('BCS', right(FCS, 0.0375 * back_scale)) #back crotch side
        BHS = C.addPoint('BHS', highestP(intersectCircles(BHC, back_half_hip, BCS, distance(FCS, FHS)))) #back hip side
        p11 = C.addPoint('p11', left(FCP, 0.121 * back_scale))
        BCP = C.addPoint('BCP', down(p11, 0.0125 * back_scale)) #back crotch point
        BKC = C.addPoint('BKC', left(FKC, 2.5 * distance(FKC, p3))) #back knee center
        BKS = C.addPoint('BKS', right(FKS, 2.5 * distance(FKS, p4))) #back knee side
        BHemC = C.addPoint('BHemC', left(FHemC, 2 * distance(FKC, p3))) #back hem center
        BHemS = C.addPoint('BHemS', right(FHemS, 2 * distance(FKS, p4))) #back hem side

        #b/w BHC back hem center & BCP back crotch point
        BHC.addOutpoint(extendLine(BWC, BHC, 0.33 * distance(BHC, BCP)))
        BCP.addInpoint(right(BCP, 0.33 * distance(BHC, BCP)))
        #b/w BCP & BKC back knee center
        BKC.addInpoint(polar(BKC, 0.33 * distance(BCP, BKC), angleOfLine(BHemC, BKC)))
        BCP.addOutpoint(polar(BCP, 0.33 * distance(BCP, BKC), angleOfLine(BCP, BKC.inpoint)))
        #b/w BKS back knee side & BCS back crotch side
        BKS.addOutpoint(polar(BKS, 0.33 * distance(BKS, BCS), angleOfLine(BHemS, BKS)))
        BCS.addInpoint(polar(BCS, 0.33 * distance(BKS, BCS), angleOfLine(BHS, BKS)))
        #b/w BCS & BHS back hip side
        BCS.addOutpoint(polar(BCS, 0.33 * distance(BCS, BHS), angleOfLine(BKS, BHS)))
        BHS.addInpoint(polar(BHS, 0.33 * distance(BCS, BHS), angleOfLine(BWS, BCS)))
        #b/w BHS & BWS back waist side
        BHS.addOutpoint(polar(BHS, 0.33 * distance(BHS, BWS), angleOfLine(BCS, BWS)))
        BWS.addInpoint(polar(BWS, 0.33 * distance(BHS, BWS), angleOfLine(BWS, BHS.outpoint)))

        #back waistband
        back_hip_curve_orig = points2List(BHS, BHS.outpoint, BWS.inpoint, BWS)
        w6 = C.addPoint('w6', onCurveAtLength(back_hip_curve_orig, curveLength(points2List(FHS, FHS.outpoint, FP2.inpoint, FP2, FP2.outpoint, w2.inpoint, w2))))
        back_hip_curve_new = splitCurveAtPoint(back_hip_curve_orig, w6)
        updatePoint(BHS.outpoint, back_hip_curve_new[1])
        w6.addInpoint(back_hip_curve_new[2])
        w6.addOutpoint(back_hip_curve_new[4])
        updatePoint(BWS.inpoint, back_hip_curve_new[5])
        
        w7 = C.addPoint('w7', intersectLineRay(BWC, BHC, w6, angleOfLine(BWS, BWC)))
        w8 = C.addPoint('w8', polar(w6, waistband_width, angleOfLine(BWS, BWC) + ANGLE90))
        w9 = C.addPoint('w9', polar(w7, waistband_width, angleOfLine(BWS, BWC) + ANGLE90))
        
        back_hip_curve_orig = points2List(w6, w6.outpoint, BWS.inpoint, BWS)
        w10 = C.addPoint('w10', intersectLineCurve(w8, w9, back_hip_curve_orig))
        w11 = C.addPoint('w11', intersectLines(w8, w9, BWC, BHC))
        
        back_hip_curve_new = splitCurveAtPoint(back_hip_curve_orig, w10)
        updatePoint(w6.outpoint, back_hip_curve_new[1])
        w10.addInpoint(back_hip_curve_new[2])
        w10.addOutpoint(back_hip_curve_new[4])
        updatePoint(BWS.inpoint, back_hip_curve_new[5])

        #draw Jeans Front A
        pnt1 = dPnt((FCM.x, FPoc3.y))
        A.setLabelPosition((pnt1.x, pnt1.y))
        A.setLetter(up(pnt1, 0.5 * IN), scaleby=10.0)
        AG1 = dPnt(down(FCM, 2 * IN))
        AG2 = dPnt(down(AG1, 0.75 * distance(FCM, FHemM)))
        A.addGrainLine(AG1, AG2)
        pth = (['M', FCP, 'L', FCS, 'M', p1, 'L', FCC, 'M', FWC, 'L', FWM, 'L', FWS, 'L', FP1, 'M', FWC, 'L', FLY1, 'M', p2, 'L', FHemC, 'M', FCS, 'L', FHemS, 'M', p3, 'L', p4, 'M', FHC, 'L', FHS])
        pth += (['M', FP1, 'L', FCS, 'L', FPoc3, 'L', FPoc4, 'L', FPoc9, 'L', FP1]) #pocket
        A.addGridLine(pth)
        pth = (['M', w1, 'L', FLY1, 'C', FCP, 'C', FKC, 'L', FHemC, 'L', FHemS, 'L', FKS, 'C', FCS, 'C', FHS, 'C', FP1, 'C', FPoc9, 'L', w1])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        #draw Jeans Front Pocket Lining B
        pnt1 = dPnt(((pnt1.x + FWS.x)/2.0, FCS.y))
        B.setLabelPosition((pnt1.x, pnt1.y))
        B.setLetter(up(pnt1, 0.5 * IN), scaleby=7.0)
        BG1 = dPnt((FPoc9.x, FP1.y))
        BG2 = dPnt(down(BG1, 0.75 * distance(FWC, FCM)))
        B.addGrainLine(BG1, BG2)
        B.addGridLine(['M', FPoc3, 'L', FCS]) #foldline
        pth = (['M', FPoc4, 'L', FPoc6, 'L', FPoc7, 'L', FHS, 'C', FP1, 'C', FPoc9, 'L', FPoc4]) #pocket
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        #draw Jeans Back C
        pnt1 = dPnt((FWM.x + 0.25 * (FPoc4.x + FWM.x), p6.y))
        C.setLabelPosition((pnt1.x, pnt1.y))
        C.setLetter(up(pnt1, 0.5 * IN), scaleby=10.0)
        CG1 = dPnt((pnt1.x, BCP.y))
        CG2 = dPnt(down(CG1, 0.8 * distance(BCP, BHemC)))
        C.addGrainLine(CG1, CG2)
        pth = (['M', BHC, 'L', BHS, 'M', BKC, 'L', BKS, 'M', BWC, 'L', p2, 'M', p11, 'L', BCS, 'M', p5, 'L', p7])
        C.addGridLine(pth)
        pth =(['M', BWC, 'L', BHC, 'C', BCP, 'C', BKC, 'L', BHemC, 'L', BHemS, 'L', BKS, 'C', BCS, 'C', BHS, 'C', w6, 'C', BWS, 'L', BWC])
        C.addSeamLine(pth)
        C.addCuttingLine(pth)

        #draw Jeans Front Waist Corner D
        pnt1 = dPnt(((pnt1.x + FWS.x)/2.0, FP2.y))
        D.setLabelPosition((pnt1.x, pnt1.y))
        D.setLetter(up(pnt1, 0.5 * IN), scaleby=5.0)
        DG1 = dPnt((FPoc9.x, (w2.y + FP2.y)/2.0))
        DG2 = dPnt(down(DG1, 0.5 * distance(w2, FHS)))
        D.addGrainLine(DG1, DG2)
        pth = (['M', FPoc4, 'L', FPoc5, 'L', FHS, 'C', FP2, 'L', w2, 'L', FPoc9, 'L', FPoc4])
        D.addSeamLine(pth)
        D.addCuttingLine(pth)

        #draw Jeans Fly E
        pnt1 = dPnt(down(FLY3, 0.2 * distance(FWC, FLY1)))
        E.setLetter((pnt1.x, pnt1.y), scaleby=5.0)
        E.setLabelPosition(polar(pnt1, 0.5*IN, angleOfLine(FWC, FLY1)))
        EG1 = dPnt(down(pnt1, 0.2 * distance(FWC, FLY1)))
        EG2 = dPnt(polar(EG1, 0.5 * distance(FWC, FLY1), angleOfLine(FWC, FLY1)))
        E.addGrainLine(EG1, EG2)
        pth = (['M', FWC, 'L', FLY3, 'L', FLY5, 'C', FLY4, 'L', FLY1, 'L', FWC])
        E.addSeamLine(pth)
        E.addCuttingLine(pth)

        #draw Jeans Front Waistband F
        pnt1 = dPnt((w1.x + 0.5 * distance(w1, w2), w4.y + 0.75 * distance(w4, w1)))
        pnt2 = dPnt((w1.x + 0.75 * distance(w1, w2), w4.y + 0.25 * distance(w4, w1)))
        F.setLetter((pnt1.x, pnt1.y), scaleby=6.0)
        F.setLabelPosition((pnt2.x, pnt2.y))
        FG1 = dPnt((w1.x + 0.25 * distance(w1, w2), w1.y))
        FG2 = dPnt(polar(FG1, 0.9 * distance(w1, w4), angleOfLine(w2, w1) + ANGLE45))
        F.addGrainLine(FG1, FG2)
        pth = (['M', w1, 'L', w2, 'L', w3, 'L', w4, 'L', w1])
        F.addSeamLine(pth)
        F.addCuttingLine(pth)
        
        #draw Jeans Front Waistband G
        pnt1 = dPnt((w7.x + 0.5 * distance(w6, w7), w7.y))
        pnt2 = dPnt((w7.x + 0.75 * distance(w6, w7), w7.y - 0.25 * abs(w7.y - w11.y)))
        pnt3 = dPnt((w7.x + 0.25 * distance(w6, w7), w7.y))
        G.setLetter((pnt1.x, pnt1.y), scaleby=6.0)
        G.setLabelPosition((pnt2.x, pnt2.y))
        GG1 = dPnt((pnt3.x, pnt3.y))
        GG2 = dPnt(polar(GG1, 0.75 * distance(w7, w11), angleOfLine(w6, w7) + ANGLE45))
        G.addGrainLine(GG1, GG2)
        pth = (['M', w6, 'C', w10, 'L', w11, 'L', w7, 'L', w6])
        G.addSeamLine(pth)
        G.addCuttingLine(pth)        

        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

