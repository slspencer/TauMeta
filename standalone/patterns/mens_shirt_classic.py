#!/usr/bin/env python
# patternName: mens_shirt_classic
# patternNumber: M-S-S-1

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
        self.setInfo('patternNumber', 'M-S-S-1')
        self.setInfo('patternTitle', 'Mens Shirt Classic')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'Winifred Aldrich')
        self.setInfo('patternmakerName', 'S.L.Spencer')
        self.setInfo('description', """This is a test pattern for Seamly Patterns""")
        self.setInfo('category', 'Shirt/TShirt/Blouse')
        self.setInfo('type', 'streetwear')
        self.setInfo('gender', 'M') # 'M',  'F',  or ''
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
        #create pattern called 'shirt'
        shirt = self.addPattern('shirt')
        #
        #create pattern pieces
        A = shirt.addPiece('yoke', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = shirt.addPiece('back', 'B', fabric = 2, interfacing = 0, lining = 0)
        C = shirt.addPiece('front', 'C', fabric = 2, interfacing = 0, lining = 0)
        D = shirt.addPiece('sleeve', 'D', fabric = 2, interfacing = 0, lining = 0)
        E = shirt.addPiece('cuff', 'E', fabric = 2, interfacing = 1, lining = 0)
        F = shirt.addPiece('collarstand', 'F', fabric = 2, interfacing = 1, lining = 0)
        G = shirt.addPiece('collar', 'G', fabric = 2, interfacing = 1, lining = 0)

        #pattern global values
        SHIRT_LENGTH = 80*CM
        CUFF_WIDTH = 25.5*CM
        CUFF_HEIGHT = 7.5*CM

        #pattern points
        # x, y coordinates are always passed as a two-item list like this: (23.6, 67.0)

        a1 = A.addPoint('a1', (0.0, 0.0)) # nape
        a2 = A.addPoint('a2', down(a1, CD.back_armfold_balance/5.0)) # yoke center
        a3 = A.addPoint('a3', (a1.x + CD.back_armfold_distance/2.0 + 4*CM, a2.y)) #yoke side
        a4 = A.addPoint('a4', (a3.x, a1.y)) # yoke reference point
        a5 = A.addPoint('a5', (a3.x + 0.75*CM, a4.y - 2*CM)) #yoke shoulder point
        a6 = A.addPoint('a6', (a1.x + CD.neck/5.0 - 0.5*CM, a1.y)) #back neck reference point
        a7 = A.addPoint('a7', (a6.x, a6.y - 4.5*CM)) #back neck side
        a8 = A.addPoint('a8', polar(a6, 2*CM, angleOfDegree(225)))

        b1 = B.addPoint('b1', a2.xy) #back top center
        b2 = B.addPoint('b2', down(a1, CD.back_armfold_balance)) #back underarm point
        b3 = B.addPoint('b3', down(a1, CD.back_waist_length + 2.54*CM + 3*CM)) #back waist lies at 2.54CM below waistline plus 3CM ease
        b4 = B.addPoint('b4', down(a1, SHIRT_LENGTH + 8*CM)) #back hem center
        b19 = B.addPoint('b19', left(b1, 2*CM)) #back center tuck extension
        b5 = B.addPoint('b5', midPoint(b19, a3)) # midpoint b/w b19 (tuck center) & a3 (yoke side)
        b6 = B.addPoint('b6', (a3.x, a3.y + 0.75*CM)) #back armscye side #1
        b7 = B.addPoint('b7', (b6.x, b2.y)) #back armscye reference point
        b8 = B.addPoint('b8', (b1.x + CD.bust/4.0 + 6.5*CM, b2.y)) #back underarm point
        b9 = B.addPoint('b9', (b8.x, b3.y)) #back waist side reference point
        b10 = B.addPoint('b10', (b8.x, b4.y)) #back hem side reference point #1
        b11 = B.addPoint('b11', (b10.x, b10.y - 20*CM)) #back hem side reference point #2
        b12 = B.addPoint('b12', left(b9, 2*CM)) #back waist side
        b13 = B.addPoint('b13', left(b11, 1*CM)) #back hem side
        b14 = B.addPoint('b14', polar(b7, 3*CM, angleOfDegree(315))) #back armscye curve
        b15 = B.addPoint('b15', down(b6, 0.75*CM)) #back armscye side #2 - necessary???
        b16 = B.addPoint('b16', midPoint(b15, b7)) #back armscye side #3
        b17 = B.addPoint('b17', midPoint(b4,b10)) #back hem curve
        b18 = B.addPoint('b18', (b19.x, b4.y)) #back hem tuck extension

        c1 = C.addPoint('c1', (a1.x + CD.bust/2.0 + 12*CM, a1.y + CD.neck/5.0 - 2.5*CM))
        c2 = C.addPoint('c2', (c1.x, b2.y))
        c3 = C.addPoint('c3', (c1.x, b4.y))
        c5 = C.addPoint('c5', onLineAtLength(c3, b10, distance(c3, b10)/2.0))
        c6 = C.addPoint('c6', (c5.x, c5.y - 4*CM))
        c4 = C.addPoint('c4', (c1.x, c6.y))
        c7 = C.addPoint('c7', b10)
        c8 = C.addPoint('c8', b8)
        c9 = C.addPoint('b9', b9)
        c10 = C.addPoint('c10', (c9.x + 2*CM, c9.y))
        c11 = C.addPoint('c11', b11)
        c12 = C.addPoint('c12', (c11.x + 1*CM, c11.y))
        c13 = C.addPoint('c13', (b1.x + CD.bust/3.0 + 4.5*CM, c2.y))
        c14 = C.addPoint('c14', polar(c13, 1.75*CM, angleOfDegree(225)))
        c15 = C.addPoint('c15', (c13.x, c13.y - 3*CM))
        c16 = C.addPoint('c16', (c2.x - CD.neck/5.0 - 1*CM, a1.y + 4.5*CM))
        pnts = onCircleAtY(c16, distance(a7, a5) + 0.5*CM, b15.y)
        if (pnts[0].x < c16.x): # if 1st intersection is to the left of c16
            c17 = C.addPoint('c17', pnts[0])
        else:
            c17 = C.addPoint('c17', pnts[1])
        c18 = C.addPoint('c18', (c1.x + 1.5*CM, c1.y))
        c19 = C.addPoint('c19', (c18.x + 3.5*CM, c1.y))
        c20 = C.addPoint('c20', (c18.x, c6.y))
        c21 = C.addPoint('c21', (c19.x, c6.y))
        c22 = C.addPoint('c22', (c2.x, a1.y + 4.5*CM))
        c23 = C.addPoint('c23', (c1.x, a1.y))

        #control points for Shirt Yoke A
        #control points b/w a8 & a7
        a8.addOutpoint(polar(a8, distance(a8, a7)/3.0, angleOfDegree(315)))
        a7.addInpoint(polar(a7, distance(a8, a7)/3.0, angleOfLine(a7, a5) + ANGLE90))
        #control points b/w a1 & a8
        a1.addOutpoint(right(a1, distance(a1, a8)/3.0))
        a8.addInpoint(onLineAtY(a8.outpoint, a8, a1.y))
        #control points b/w a5 & a3
        length = distance(a3, a5)/3.0
        a3.addInpoint(up(a3, length ))
        a5.addOutpoint(polar(a5, length, angleOfLine(a7, a5) + ANGLE90))

        #control points for B back
        #b/w b5 & b6 top of yoke
        b5.addOutpoint(right(b5, distance(b5, b6)/3.0))
        b6.addInpoint(polar(b6, distance(b5, b6)/3.0, angleOfLine(b6, b5.outpoint)))
        #b/w b16 &b14 armscye
        b16.addOutpoint(down(b16, distance(b16, b14)/3.0))
        b14.addInpoint(polar(b14, distance(b16, b14)/3.0, angleOfDegree(225)))
        #b/w b14 & b8 armscye
        b14.addOutpoint(polar(b14, distance(b14, b8)/3.0, angleOfDegree(45)))
        b8.addInpoint(left(b8, distance(b14, b8)/3.0))
        #b/w b8 & b12 side
        length = distance(b8, b12)/3.0
        b12.addInpoint(up(b12, length))
        b8.addOutpoint(polar(b8, length, angleOfLine(b8, b12.inpoint)))
        #b/w b12 & b13 side
        length = distance(b12, b13)/3.0
        b12.addOutpoint(down(b12, length))
        b13.addInpoint(polar(b13, length, angleOfLine(b13, b12.outpoint)))
        #b/w 13 & 17 hem
        length = distance(b13, b17)/3.0
        b13.addOutpoint(left(b13, length))
        b17.addInpoint(right(b17, length))

        #control points for Shirt Front C
        #b/w c6 & c12 hem
        length = distance(c6, c12)/3.0
        c6.addOutpoint(left(c6,length))
        c12.addInpoint(right(c12, length))
        #b/w c12 & c10 side
        length = distance(c12, c10)/3.0
        c10.addInpoint(down(c10, length))
        c12.addOutpoint(polar(c12, length, angleOfLine(c12, c10.inpoint)))
        #b/w c10 & c8 side
        length = distance(c10, c8)/3.0
        c10.addOutpoint(up(c10, length))
        c8.addInpoint(polar(b8, length, angleOfLine(c8, c10.outpoint)))
        #b/w c14 & c17
        length = distance(c14, c17)/3.0
        c17.addInpoint(polar(c17, length/2.0, angleOfLine(c17, c16) + ANGLE90))
        c14.addOutpoint(polar(c14, length, angleOfDegree(325)))
        #b/w c8 & c14 armscye
        length = distance(c8, c14)/3.0
        c8.addOutpoint(right(c8, length))
        c14.addInpoint(onLineAtY(c14.outpoint, c14, c8.y))
        #b/w c16 & c1 neck
        length = distance(c16, c1)/3.0
        c16.addOutpoint(polar(c16, length, angleOfLine(c17, c16) + ANGLE90))
        c1.addInpoint(left(c1, distance(c16, c1)/3.0))

        # D - sleeve, based on A,B,C points
        #get front & back armcye length
        back_armscye = points2List(b16, b16.outpoint, b14.inpoint, b14, b14.outpoint, b8.inpoint, b8, b8.outpoint, c17.inpoint, c17)
        front_armscye = points2List(a5, a5.outpoint, a3.inpoint, a3)
        ARMSCYE_LENGTH = curveLength(back_armscye) + curveLength(front_armscye)

        d1 = D.addPoint('d1', (0.0, 0.0)) #midpoint of sleevecap - top of sleeve
        d2 = D.addPoint('d2', (d1.x, d1.y + ARMSCYE_LENGTH/4.0 + 1.5*CM)) #middle bicep line
        d3 = D.addPoint('d3', (d1.x, d1.y + CD.oversleeve_length + 6*CM - CUFF_HEIGHT)) #middle cuff line
        d4 = D.addPoint('d4', midPoint(d2, d3)) #middle elbow line
        d5 = D.addPoint('d5', (d2.x - (ARMSCYE_LENGTH/2.0 - 0.5*CM), d2.y)) #back bicep line
        d6 = D.addPoint('d6', (d5.x, d3.y)) #back cuff line
        d7 = D.addPoint('d7', (d2.x + (ARMSCYE_LENGTH/2.0 - 0.5*CM), d2.y)) #front bicep line
        d8 = D.addPoint('d8', (d7.x, d3.y)) #front cuff line
        #back armscye points
        d9 = D.addPoint('d9', onLineAtLength(d5, d1, distance(d5, d1)/4.0)) #back armscye point 1
        d10 = D.addPoint('d10', polar(midPoint(d5, d1), 1*CM, angleOfLine(d5, d1) - ANGLE90)) #back armscye point 2
        pnt = onLineAtLength(d5, d1, 0.75*distance(d5, d1))
        d11 = D.addPoint('d11', polar(pnt, 2*CM, angleOfLine(d5, d1) - ANGLE90)) #back armcye point 3
        print 'd11', d11.x,  d11.y
        #front armscye points
        pnt = onLineAtLength(d7, d1, distance(d7, d1)/4.0)
        d12 = D.addPoint('d12', polar(pnt, 1*CM, angleOfLine(d7, d1) - ANGLE90)) #front armscye point 1
        d13 = D.addPoint('d13', midPoint(d7, d1)) #front armscye point 2
        pnt = onLineAtLength(d7, d1, 0.75*distance(d7, d1))
        d14 = D.addPoint('d14', polar(pnt, 1*CM, angleOfLine(d7, d1) + ANGLE90)) #front armscye point 3

        d15 = D.addPoint('d15', onLineAtLength(d6, d3, distance(d6, d3)/3.0)) #back cuff point
        d16 = D.addPoint('d16', onLineAtLength(d8, d3, distance(d8, d3)/3.0)) #front cuff point
        d17 = D.addPoint('d17', midPoint(d6,d15)) #cuffline reference point
        d18 = D.addPoint('d18', midPoint(d8,d16)) #cuffline reference point
        d19 = D.addPoint('d19', midPoint(d3,d15)) #slashline reference point
        d20 = D.addPoint('d20', (d19.x, d19.y - 15*CM)) #top of slashline
        d21 = D.addPoint('d21', (d19.x, d19.y + 1*CM)) #bottom of slashline
        d22 = D.addPoint('d22', onLineAtY(d5, d17, d4.y)) #back elbow
        d23 = D.addPoint('d23', onLineAtY(d7, d18, d4.y)) #front elbow
        d24 = D.addPoint('d24', midPoint(d2, d4)) #middle of sleeve - label reference point
        d25 = D.addPoint('d25', down(d21, SEAM_ALLOWANCE)) #extend slashline out to cuttingline

        # control points for sleeve
        cArray = points2List(d5, d9, d10, d11, d1, d14, d13, d12, d7)
        C1, C2 = controlPoints('sleeve_cap', cArray)
        d5.addOutpoint(C1[0])
        d9.addInpoint(C2[0])
        d9.addOutpoint(C1[1])
        d10.addInpoint(C2[1])
        d10.addOutpoint(C1[2])
        d11.addInpoint(C2[2])
        d11.addOutpoint(C1[3])
        d1.addInpoint(C2[3])
        d1.addOutpoint(C1[4])
        d14.addInpoint(C2[4])
        d14.addOutpoint(C1[5])
        d13.addInpoint(C2[5])
        d13.addOutpoint(C1[6])
        d12.addInpoint(C2[6])
        d12.addOutpoint(C1[7])
        d7.addInpoint(C2[7])
        cArray = points2List(d15, d22, d5)
        C1, C2 = controlPoints('sleeve_seam1', cArray)
        d15.addOutpoint(C1[0])
        d22.addInpoint(C2[0])
        d22.addOutpoint(C1[1])
        d5.addInpoint(C2[1])
        cArray = points2List(d7, d23, d16)
        C1, C2 = controlPoints('sleeve_seam2', cArray)
        d7.addOutpoint(C1[0])
        d23.addInpoint(C2[0])
        d23.addOutpoint(C1[1])
        d16.addInpoint(C2[1])
        cArray = points2List(d3, d21, d15)
        C1, C2 = controlPoints('sleeve_placket', cArray)
        d3.addOutpoint(C1[0])
        d21.addInpoint(C2[0])
        d21.addOutpoint(C1[1])
        d15.addInpoint(C2[1])

        # E - cuff
        e1 = E.addPoint('e1', (0.0, 0.0))
        e2 = E.addPoint('e2', right(e1, CUFF_WIDTH))
        e3 = E.addPoint('e3', left(e1, 3*CM)) #3CM cuff width ease & overlap
        e4 = E.addPoint('e4', right(e2, 3*CM)) #3CM cuff width ease & overlap
        e5 = E.addPoint('e5', down(e1, CUFF_HEIGHT))
        e6 = E.addPoint('e6', down(e2, CUFF_HEIGHT))
        e7 = E.addPoint('e7', down(e3, 0.7*CUFF_HEIGHT)) #cuff curve #1
        e8 = E.addPoint('e8', down(e4, 0.7*CUFF_HEIGHT)) #cuff curve point #2
        print 'e8', e8.x,  e8.y
        # control points for cuff
        e8.addOutpoint(down(e8, distance(e8, e6)/3.0))
        e6.addInpoint(right(e6, distance(e8, e6)/3.0))
        e5.addOutpoint(left(e5, distance(e5, e7)/3.0))
        e7.addInpoint(down(e7, distance(e5, e7)/3.0))

        # F & G - collar stand & collar -  G is drawn from points on F
        f1 = F.addPoint('f1', (0.0, 0.0))
        curve1 = points2List(a1, a1.outpoint, a7.inpoint,  a7)
        curve2 = points2List(c16, c16.outpoint, c1.inpoint, c1)
        f2 = F.addPoint('f2', (f1.x + (curveLength(curve1) + curveLength(curve2)), f1.y))
        f3 = F.addPoint('f3', (f2.x + (1.5*CM + 1.25*CM), f1.y))
        f4 = F.addPoint('f4', (f1.x + (distance(f1, f2)*3/4.0), f1.y))
        f5 = F.addPoint('f5', (f1.x, f1.y - (8*CM + 2*CM)))
        f6 = F.addPoint('f6', midPoint(f1, f5))
        f7 = F.addPoint('f7', (f2.x, f6.y))
        f8 = F.addPoint('f8', (f3.x, f6.y))
        f9 = F.addPoint('f9', (f8.x - (1*CM), f6.y))
        f10 = F.addPoint('f10', onLineAtLength(f3, f9, 0.75*CM))
        f11 = F.addPoint('f11', onLineAtLength(f9, f3, 0.75*CM))
        f12 = F.addPoint('f12', (f1.x, f1.y - 0.5*CM))
        f13 = F.addPoint('f13', midPoint(f6, f7))
        f14 = F.addPoint('f14', (f7.x, f7.y + 1*CM))
        f15 = F.addPoint('f15', onLineAtLength(f11, f3, 1*CM))
        f16 = F.addPoint('f16', (f7.x + 1*CM, f5.y - 1*CM))
        f17 = F.addPoint('f17', (f13.x, f5.y))
        f18 = F.addPoint('f18', (f2.x, f10.y + 0.4*CM))
        # control points for collar
        cArray = points2List(f12, f4, f18, f10)
        C1, C2 = controlPoints('collar_stand_bottom', cArray)
        f12.addOutpoint(C1[0])
        f4.addInpoint(C2[0])
        f4.addOutpoint(C1[1])
        f18.addInpoint(C2[1])
        f18.addOutpoint(C1[2])
        f10.addInpoint(C2[2])

        #b/w f15 & f14
        f15.addOutpoint(polar(f15, abs(f14.y - f15.y)/2.0, angleOfLine(f10, f15)))
        f14.addInpoint(polar(f14, distance(f15, f14)/3.0, angleOfLine(f14, f15.outpoint)))
        #b/w f14 & f13
        f14.addOutpoint(polar(f14, distance(f14, f13)/3.0, angleOfLine(f14.inpoint, f14)))
        f13.addInpoint(right(f13, distance(f14, f13)/3.0))
        #b/w f17 & f16
        f17.addOutpoint(right(f17, distance(f17, f16)/3.0))
        f16.addInpoint(polar(f16, distance(f17, f16)/3.0, angleOfLine(f16, f17.outpoint)))

        # ------------------------------------------------ #
        # ----- all points defined, now define paths ----- #
        # ------------------------------------------------ #

        # shirt Yoke A
        Ag1 = dPnt((a6.x + 1*CM, a6.y - 2*CM))
        Ag2 = dPnt((Ag1.x, a2.y - 1*CM))
        A.addGrainLine(Ag1, Ag2)
        A.setLabelPosition((Ag1.x + 1*CM, Ag1.y + 1*CM))
        A.setLetter((Ag1.x + 7*CM, Ag2.y), scaleby=10.0)
        gpth = (['M', a1, 'L', a2, 'L', a3, 'L', a4, 'L', a1, 'M', a7, 'L', a6, 'L', a8])
        A.addGridLine(gpth)
        pth = (['M', a1, 'C', a8,'C', a7, 'L', a5, 'C', a3, 'L', a2, 'L', a1])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)

        # shirt Back B
        Bg1 = dPnt((a7.x,  b1.y + 8*CM))
        Bg2 = dPnt((Bg1.x, b4.y - 8*CM))
        B.addGrainLine(Bg1, Bg2)
        B.setLabelPosition((Bg1.x + 3*CM, Bg1.y  + 3*CM))
        B.setLetter((b5.x, b8.inpoint.y), scaleby=15.0)
        B.addGridLine(['M', b1, 'L', b4, 'M', b19, 'L', b18, 'M', b6, 'L', b7, 'L', b14, 'M', b8, 'L', b10, 'M', b19, 'L', a3, 'M', b2, 'L', b8, 'M', b3, 'L', b9, 'M', b18, 'L', b10])
        B.addFoldLine(['M', b19, 'L', b18])
        pth = (['M', b19, 'L', b5, 'C', b6, 'L', b16, 'C', b14, 'C', b8, 'C', b12, 'C', b13, 'C', b17, 'L',  b18, 'L', b19])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        # shirt Front C
        Cg1 = dPnt((c16.x - 1*CM, c16.y + 8*CM))
        Cg2 = dPnt((Cg1.x, c3.y - 8*CM))
        C.addGrainLine(Cg1, Cg2)
        C.setLabelPosition((Cg1.x - 8*CM, Cg1.y + 3*CM))
        C.setLetter((c14.outpoint.x, c10.y), scaleby=15.0)
        C.addGridLine(['M', b8, 'L', b10, 'M', c17, 'L', c15, 'L', c13, 'L', c14,'M', c6, 'L', c5, 'M', c23, 'L', c3, 'M', c18, 'L', c20, 'M', c19, 'L', c21, 'M', c23, 'M', c16, 'L', c22, 'M', c1, 'L', c19, 'M', b8, 'L', c2, 'M', b9, 'L', c10, 'M', b11, 'L', c12, 'M', b10, 'L', c3])
        C.addFoldLine(['M', c18, 'L', c20])
        C.addMarkingLine(['M', c1, 'L', c4])
        pth = (['M', c16, 'C', c1, 'L', c18, 'L', c19, 'L', c21, 'L', c6, 'C', c12, 'C', c10, 'C', c8, 'C', c14, 'C', c17, 'L', c16])
        C.addSeamLine(pth)
        C.addCuttingLine(pth)

        # Shirt Sleeve D
        Dg1 = dPnt((d2.x, d2.y))
        Dg2 = dPnt((Dg1.x, d3.y - 8*CM))
        D.addGrainLine(Dg1, Dg2)
        D.setLabelPosition((Dg1.x + 3*CM, Dg1.y + 8*CM))
        D.setLetter((d9.outpoint.x, d24.y), scaleby=15.0)
        D.addGridLine(['M',d1,'L', d3, 'M', d7, 'L', d8, 'M', d5, 'L', d6, 'M', d20,  'L', d21, 'M', d5, 'L', d1, 'L',  d7, 'M', d5, 'L', d17, 'M', d22, 'L', d15, 'M', d7, 'L', d18, 'M', d23, 'L', d16, 'M', d5, 'L', d7,  'M', d22, 'L', d23, 'M', d6, 'L', d8])
        D.addMarkingLine(['M', d20, 'L', d25])
        pth = (['M', d5, 'C', d9, 'C', d10, 'C', d11, 'C', d1, 'C', d14, 'C', d13, 'C', d12, 'C', d7, 'C', d23, 'C', d16, 'L', d3, 'C', d21, 'C', d15, 'C', d22, 'C', d5])
        D.addSeamLine(pth)
        D.addCuttingLine(pth)

        # shirt Cuff E
        Eg1 = dPnt((e1.x + 2*CM,  e1.y + 2*CM))
        Eg2 = dPnt((e2.x - 2*CM, Eg1.y))
        E.addGrainLine(Eg1, Eg2)
        E.setLabelPosition((Eg1.x + 3*CM, Eg1.y + 1*CM))
        E.setLetter(((Eg1.x+Eg2.x)/2.0, (e5.outpoint.y + e7.inpoint.y)/2.0), scaleby=7.0)
        E.addGridLine(['M', e3,'L', e7, 'M', e1, 'L', e5, 'M', e2, 'L', e6, 'M', e4,  'L', e8, 'M', e3, 'L', e4,  'M', e5, 'L', e6])
        pth = (['M', e3, 'L', e4, 'L', e8, 'C', e6, 'L', e5, 'C', e7, 'L', e3])
        E.addSeamLine(pth)
        E.addCuttingLine(pth)

        # shirt Collar Stand F
        Fg1 = dPnt((f1.x + 2*CM, f1.y - 1*CM))
        Fg2 = dPnt((f2.x - 2*CM, Fg1.y))
        F.addGrainLine(Fg1, Fg2)
        F.setLabelPosition((Fg1.x + 1*CM, f6.y + 1*CM))
        F.setLetter((f13.x, Fg1.y - 1*CM), scaleby=5.0)
        F.addGridLine(['M', f5,'L', f1, 'M', f7, 'L', f2, 'M', f8, 'L', f3, 'M', f12, 'L', f4, 'L', f18, 'L',f10,'M', f3, 'L', f9, 'M', f15, 'L', f14, 'L', f13, 'M', f17, 'L', f16, 'L', f14, 'M', f5, 'L', f17,  'M', f6, 'L', f8, 'M', f1, 'L', f3])
        F.addFoldLine(['M', f6, 'L', f12])
        pth = (['M', f6, 'L', f12, 'C', f4, 'C', f18, 'C', f10, 'L', f15, 'C', f14, 'C', f13, 'L', f6])
        F.addSeamLine(pth)
        F.addCuttingLine(pth)

        # Shirt Collar G
        Gg1 = dPnt((f5.x + 1*CM, f5.y + 1*CM))
        Gg2 = dPnt((f7.x - 1*CM, Gg1.y))
        G.addGrainLine(Gg1, Gg2)
        G.setLabelPosition((Gg1.x + 1*CM, Gg1.y + 1*CM))
        G.setLetter(((Gg1.x+Gg2.x)/2.0, Gg1.y + 3*CM), scaleby=5.0)
        G.addFoldLine(['M', f5, 'L', f6])
        pth = (['M', f6, 'L', f5, 'L', f17, 'C', f16, 'L', f14, 'C', f13, 'L', f6])
        G.addSeamLine(pth)
        G.addCuttingLine(pth)

        # call draw once for the entire pattern
        self.draw()
        return
# vi:test ts=4 sw=4 expandtab:

