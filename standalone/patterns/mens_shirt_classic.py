#!/usr/bin/env python
# patternName: mens_shirt_classic
# patternNumber: M-S-S-1

from pysvg.builders import path
from tmtpl.document import *
from tmtpl.pattern import *
from tmtpl.constants import *
from tmtpl.utils import *

class PatternDesign():

    def _init__(self):
        self.styledefs = {}
        self.markerdefs = {}
        return

    def pattern(self):
        """
        Method defining a pattern design. This is where the designer places
        all elements of the design definition
        """
        # All measurements are converted to pixels
        # x increases towards right, y increases towards bottom of drawing - Quadrant is 'upside down'
        # All angles are in radians
        # angles start with 0 at '3:00', & move clockwise b/c quadrant is 'upside down'

        CD = self.CD #client data is prefaced with CD
        printer = '36" wide carriage plotter'
        patternData = { 'companyName' : 'Seamly Patterns', # mandatory
            'designerName' : 'Winifred Aldrich',  # mandatory
            'patternTitle'  :'Mens Classic Shirt', # mandatory
            'patternNumber' : 'M-S-S-1' # mandatory
        }
        #create document
        doc = setupPattern(self,  CD,  printer,  patternData)

        # create pattern object, add to document
        shirt = Pattern('shirt')
        shirt.styledefs.update(self.styledefs)
        shirt.markerdefs.update(self.markerdefs)
        doc.add(shirt)

        # create pattern pieces, add to pattern object
        shirt.add(PatternPiece('pattern', 'yoke', 'A', fabric=2, interfacing=0, lining=0))
        shirt.add(PatternPiece('pattern', 'back', 'B', fabric=2, interfacing=0, lining=0))
        shirt.add(PatternPiece('pattern', 'front', 'C', fabric=2, interfacing=0, lining=0))
        shirt.add(PatternPiece('pattern', 'sleeve', 'D', fabric=2, interfacing=0, lining=0))
        shirt.add(PatternPiece('pattern', 'cuff', 'E', fabric=2, interfacing=0, lining=0))
        shirt.add(PatternPiece('pattern', 'collarstand', 'F', fabric=2, interfacing=0, lining=0))
        shirt.add(PatternPiece('pattern', 'collar', 'G', fabric=2, interfacing=0, lining=0))
        A = shirt.yoke
        B = shirt.back
        C = shirt.front
        D = shirt.sleeve
        E = shirt.cuff
        F = shirt.collarstand
        G = shirt.collar

        SHIRT_LENGTH = 80*CM
        CUFF_WIDTH = 25.5*CM
        CUFF_HEIGHT = 7.5*CM

        a1 = Pnt(0.0, 0.0) # nape
        a2 = down(a1, CD.back_armfold_balance/5.0) # yoke center
        a3 = Pnt(a1.x + CD.back_armfold_distance/2.0 + 4*CM, a2.y) #yoke side
        a4 = Pnt(a3.x, a1.y) # yoke reference point
        a5 = Pnt(a3.x + 0.75*CM, a4.y - 2*CM) #yoke shoulder point
        a6 = Pnt(a1.x + (CD.neck/5.0 - 0.5*CM), a1.y) #back neck reference point
        a7 = Pnt(a6.x, a6.y - 4.5*CM) #back neck side
        a8 = polar(a6, 2*CM, angleOfDegree(225))

        b1 = PntP(a2)
        b2 = down(a1, CD.back_armfold_balance) #back underarm point
        b3 = down(a1, CD.back_waist_length + 2.54*CM + 3*CM) #back waist lies at 2.54CM below waistline plus 3CM ease
        b4 = down(a1, SHIRT_LENGTH + 8*CM) #back hem center
        b19 = left(b1, 2*CM) #back center tuck extension
        b5 = midPoint(b19, a3) # midpoint b/w b19 (tuck center) & a3 (yoke side)
        b6 = Pnt(a3.x, a3.y + 0.75*CM) #back armscye side #1
        b7 = Pnt(b6.x, b2.y) #back armscye reference point
        b8 = Pnt(b1.x + CD.bust/4.0 + 6.5*CM, b2.y) #back underarm point
        b9 = Pnt(b8.x, b3.y) #back waist side reference point
        b10 = Pnt(b8.x, b4.y) #back hem side reference point #1
        b11 = Pnt(b10.x, b10.y - 20*CM) #back hem side reference point #2
        b12 = left(b9, 2*CM) #back waist side
        b13 = left(b11, 1*CM) #back hem side
        b14 = polar(b7, 3*CM, angleOfDegree(315)) #back armscye curve
        b15 = down(b6, 0.75*CM) #back armscye side #2 - necessary???
        b16 = midPoint(b15, b7) #back armscye side #3
        b17 = midPoint(b4,b10) #back hem curve
        b18 = Pnt(b19.x, b4.y) #back hem tuck extension

        c1 = Pnt(a1.x + CD.bust/2.0 + 12*CM, a1.y + CD.neck/5.0 - 2.5*CM)
        c2 = Pnt(c1.x, b2.y)
        c3 = Pnt(c1.x, b4.y)

        c5 = onLineAtLength(c3, b10, distance(c3,b10)/2.0)
        c6 = Pnt(c5.x, c5.y - 4*CM)
        c4 = Pnt(c1.x, c6.y)
        c7 = PntP(b10)
        c8 = PntP(b8)
        c9 = PntP(b9)
        c10 = Pnt(c9.x + 2*CM, c9.y)
        c11 = PntP(b11)
        c12 = Pnt(c11.x + 1*CM, c11.y)
        c13 = Pnt(b1.x + CD.bust/3.0 + 4.5*CM, c2.y)
        c14 = polar(c13, 1.75*CM, angleOfDegree(225))
        c15 = Pnt(c13.x, c13.y - 3*CM)
        c16 = Pnt(c2.x - CD.neck/5.0 - 1*CM, a1.y + 4.5*CM)
        pnts = onCircleAtY(c16, distance(a7, a5) + 0.5*CM, b15.y)
        if (pnts[0].x < c16.x): # if 1st intersection is to the left of c16
            c17 = PntP(pnts[0])
        else:
            c17 = PntP(pnts[1])
        c18 = Pnt(c1.x + 1.5*CM, c1.y)
        c19 = Pnt(c18.x + 3.5*CM, c1.y)
        c20 = Pnt(c18.x, c6.y)
        c21 = Pnt(c19.x, c6.y)
        c22 = Pnt(c2.x, a1.y + 4.5*CM)
        c23 = Pnt(c1.x, a1.y)


        #pnt = midPoint(c15, c17)




        # control points for A yoke
        a8.c1 = Pnt(a1.x + distance(a1, a8)/3.0, a1.y)
        a8.c2 = polar(a8, distance(a1, a8)/3.0, angleOfDegree(135))
        a7.c1 = polar(a8, distance(a8, a7)/3.0, angleOfDegree(315))
        a7.c2 = polar(a7, distance(a8, a7)/3.0, angleOfLine(a7, a5) + ANGLE90) #c2 is perpendicular to shoulder seam
        length1 = distance(a3, a5)/3.0
        a3.c2 = onLineAtLength(a3, a4, length1)
        a3.c1 = onLineAtLength(a5, a3.c2, length1)
        #control points for B back
        b14.c1 = onLineAtLength(b16, b7, distance(b16, b14)/3.0)
        #b14.c2 = cPoint(B, 'b14.c2', onLineAtLength(b14, b14.c1, distance(b16, b14)/3.0))
        b14.c2 = polar(b14, distance(b16, b14)/3.0, angleOfDegree(225))
        b8.c2 = onLineAtLength(b8, b7, distance(b8, b14)/3.0)
        b8.c1 = polar(b14, distance(b8, b14)/3.0, angleOfDegree(45))
        #b8.c1 = cPoint(B, 'b8.c1', onLineAtLength(b14, b8.c2, distance(b8, b14)/3.0))
        cArray = pointList(b8, b12, b13)
        C1, C2 = controlPoints('back_side_seam_control_points', cArray)
        b12.c1 = C1[0]
        b12.c2 = C2[0]
        b13.c1 = C1[1]
        b13.c2 = C2[1]
        b17.c1 = Pnt(b13.x - distance(b13, b17)/3.0, b13.y)
        b17.c2 = Pnt(b17.x + distance(b13, b17)/3.0, b17.y)
        b6.c1 = Pnt(b5.x + distance(b5, b6)/3.0, b5.y)
        b6.c2 = polar(b6, distance(b5, b6)/3.0, angleOfLine(b6, b6.c1))


        #control points for C front
        c17.c1 = polar(c14, distance(c14, c17)/3.0, angleOfDegree(325))
        c17.c2 = polar(c17, distance(c14, c17)/3.0, angleOfLine(c17, c17.c1))
        c1.c1 = polar(c16, distance(c16, c1)/3.0, angleOfLine(c17, c16) + ANGLE90)
        c1.c2 = Pnt(c1.x - distance(c16, c1)/3.0 + 1*CM,  c1.y)
        c8.c1 = polar(c10, distance(c10, b8)/3.0, angleOfLine(c12, c8))
        c8.c2 = polar(b8, distance(c10, b8)/3.0, angleOfLine(c8, c8.c1))
        c10.c2 = polar(c10, distance(c12, c10)/3.0, angleOfLine(c8, c12))
        c10.c1 = polar(c12, distance(c12, c10)/3.0, angleOfLine(c12, c10.c2))
        c12.c1 = polar(c6, distance(c6, c12)/3.0, ANGLE180)
        c12.c2 = polar(c12, distance(c6, c12)/3.0, angleOfDegree(0))
        c14.c1 = Pnt(b8.x + distance(b8, c14)/3.0, b8.y)
        c14.c2 = polar(c14, distance(b8, c14)/3.0, angleOfDegree(135))

        # D - sleeve, based on A,B,C points
        cArray1 = pointList(b16, b14.c1, b14.c2, b14,  b8.c1, b8.c2, b8, c14.c1, c14.c2, c17)
        cArray2 = pointList(a5, a3.c1, a3.c2, a3)
        armscyeLength = curveLength(cArray1) + curveLength(cArray2)

        d1 = Pnt(0.0, 0.0)
        d2 = Pnt(d1.x, d1.y + armscyeLength/4.0 + 1.5*CM)
        d3 = Pnt(d1.x, d1.y + CD.oversleeve_length + 6*CM - CUFF_HEIGHT )
        d4 = midPoint(d2, d3)
        d5 = Pnt(d2.x - (armscyeLength/2.0 - 0.5*CM), d2.y)
        d6 = Pnt(d5.x, d3.y)
        d7 = Pnt(d2.x + (armscyeLength/2.0 - 0.5*CM), d2.y)
        d8 = Pnt(d7.x, d3.y)

        angle = angleOfLine(d5, d1)
        pnt = onLineAtLength(d5, d1, distance(d5, d1)/4.0)
        d9 = onLineAtLength(d5, d1, distance(d5, d1)/4.0)
        pnt = onLineAtLength(d5, d1, distance(d5, d1)/2.0)
        d10 = polar(pnt, 1*CM, angle + angleOfDegree(-90))
        pnt = onLineAtLength(d5, d1, 0.75*distance(d5, d1))
        d11 = polar(pnt, 2*CM, angle + angleOfDegree(-90))

        angle = angleOfLine(d7, d1)
        pnt = onLineAtLength(d7, d1, distance(d7, d1)/4.0)
        d12 = polar(pnt, 1*CM, angle + angleOfDegree(-90))
        d13 = onLineAtLength(d7, d1, distance(d7, d1)/2.0)
        pnt = onLineAtLength(d7, d1, 0.75*distance(d7, d1))
        d14 = polar(pnt, 1*CM, angle + ANGLE90)

        d15 = onLineAtLength(d6, d3, distance(d6, d3)/3.0)
        d16 = onLineAtLength(d8, d3, distance(d8, d3)/3.0)
        d17 = midPoint(d6,d15)
        d18 = midPoint(d8,d16)
        d19 = midPoint(d3,d15)
        d20 = Pnt(d19.x, d19.y - 15*CM)
        d21 = Pnt(d19.x, d19.y + 1*CM)
        d22 = onLineAtY(d5, d17, d4.y)
        d23 = onLineAtY(d7, d18, d4.y)
        d24 = midPoint(d2, d4)
        # control points for sleeve
        cArray = pointList(d5, d9, d10, d11, d1, d14, d13, d12, d7)
        C1, C2 = controlPoints('sleeve_cap', cArray)
        d9.c1, d9.c2 = C1[0], C2[0]
        d10.c1, d10.c2 = C1[1], C2[1]
        d11.c1,  d11.c2 = C1[2], C2[2]
        d1.c1, d1.c2 = C1[3], C2[3]
        d14.c1,  d14.c2 = C1[4], C2[4]
        d13.c1, d13.c2 = C1[5], C2[5]
        d12.c1,  d12.c2 = C1[6], C2[6]
        d7.c1, d7.c2 = C1[7], C2[7]
        cArray = pointList(d15, d22, d5)
        C1, C2 = controlPoints('sleeve_seam1', cArray)
        d22.c1, d22.c2 = C1[0], C2[0]
        d5.c1, d5.c2 = C1[1], C2[1]
        cArray = pointList(d7, d23, d16)
        C1, C2 = controlPoints('sleeve_seam2', cArray)
        d23.c1, d23.c2 = C1[0], C2[0]
        d16.c1, d16.c2 = C1[1], C2[1]
        cArray = pointList(d3, d21, d15)
        C1, C2 = controlPoints('sleeve_placket', cArray)
        d21.c1, d21.c2 = C1[0], C2[0]
        d15.c1, d15.c2 = C1[1], C2[1]

        # E - cuff
        e1 = Pnt(0.0, 0.0)
        e2 = right(e1, CUFF_WIDTH)
        e3 = left(e1, 3*CM) #3CM cuff width ease & overlap
        e4 = right(e2, 3*CM) #3CM cuff width ease & overlap
        e5 = down(e1, CUFF_HEIGHT)
        e6 = down(e2, CUFF_HEIGHT)
        e7 = down(e3, CUFF_HEIGHT/2.0) #cuff curve #1
        e8 = down(e4, CUFF_HEIGHT/2.0) #cuff curve point #2
        # control points for cuff
        e6.c1 = Pnt(e8.x, e8.y + distance(e8, e6)/3.0)
        e6.c2 = Pnt(e6.x + distance(e8, e6)/3.0, e6.y)
        e7.c1 = Pnt(e5.x - distance(e5, e7)/3.0, e5.y)
        e7.c2 = Pnt(e7.x, e7.y + distance(e5, e7)/3.0)

        # F & G --> collar stand & collar -  G is drawn from points on F
        f1 = Pnt(0.0, 0.0)
        curve1 = pointList(a1, a7.c1, a7.c2,  a7)
        curve2 = pointList(c16, c1.c1, c1.c2, c1)
        f2 = Pnt(f1.x + (curveLength(curve1) + curveLength(curve2)), f1.y)
        f3 = Pnt(f2.x + (1.5*CM + 1.25*CM), f1.y)
        f4 = Pnt(f1.x + (distance(f1, f2)*3/4.0), f1.y)
        f5 = Pnt(f1.x, f1.y - (8*CM + 2*CM))
        f6 = midPoint(f1, f5)
        f7 = Pnt(f2.x, f6.y)
        f8 = Pnt(f3.x, f6.y)
        f9 = Pnt(f8.x - (1*CM), f6.y)
        f10 = onLineAtLength(f3, f9, 0.75*CM)
        f11 = onLineAtLength(f9, f3, 0.75*CM)
        f12 = Pnt(f1.x, f1.y - 0.5*CM)
        f13 = midPoint(f6, f7)
        f14 = Pnt(f7.x, f7.y + 1*CM)
        f15 = onLineAtLength(f11, f3, 1*CM)
        f16 = Pnt(f7.x + 1*CM, f5.y - 1*CM)
        f17 = Pnt(f13.x, f5.y)
        #f18 = pntOnCurveX(b4,a2,b1.x)
        f18 = Pnt(f2.x, f10.y + 0.4*CM)
        # control points for collar
        cArray = pointList(f12, f4, f18, f10)
        C1, C2 = controlPoints('collar_stand_bottom', cArray)
        f4.c1, f4.c2 = C1[0], C2[0]
        f18.c1, f18.c2 = C1[1], C2[1]
        f10.c1, f10.c2 = C1[2], C2[2]

        cArray = pointList(f15, f14, f13)
        C1, C2 = controlPoints('collar_stand_top', cArray)
        f14.c2 = Pnt(f13.x + distance(f14, f13)/2.0, f13.y)
        f14.c1 = onLineAtLength(f14, f14.c2, distance(f14, f14.c2)/2.0)
        f15.c2 = onLineAtLength(f14, f14.c2, -distance(f15, f14)/3.0)
        f15.c1 = onLineAtLength(f15, f15.c2, distance(f15, f14)/3.0)
        f17.c1 = Pnt(f17.x + distance(f17, f16)/3.0, f17.y)
        f17.c2 = polar(f16, distance(f17, f16)/3.0, angleOfLine(f16, f17.c1))

        # ------------------------------------------------ #
        # ----- all points defined, now define paths ----- #
        # ------------------------------------------------ #

        # shirt Yoke A
        drawPoints(A, locals())
        #grainline coords
        Ag1 = Pnt(a6.x + 1*CM, a6.y - 2*CM)
        Ag2 = Pnt(Ag1.x, a2.y - 1*CM)
        (A.label_x, A.label_y) = (Ag1.x + 1*CM, Ag1.y + 1*CM)

        # set letter location and size
        # optional arguments to setLetter:
        # style = 'letter_text_style' (defaults to default_letter_text_style)
        # text = 'D' (or whetever you want. Defaults to the letter set when creating the pattern piee4)
        # scaleby = a factor to scale the letter by
        A.setLetter(x = Ag1.x + 7*CM, y = Ag2.y, scaleby=10.0)

        # gridline
        grid = path()
        addToPath(grid, 'M', a1, 'L', a2, 'L', a3, 'L', a4, 'L', a1, 'M', a7, 'L', a6, 'L', a8)
        #seamline & cuttingline
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine:
            addToPath(P, 'M', a1, 'C', a8.c1, a8.c2, a8,'C', a7.c1, a7.c2,  a7, 'L',  a5, 'C', a3.c1, a3.c2, a3, 'L', a2, 'L', a1)
        # add grid, grainline, seamline & cuttingline paths to pattern
        addGrainLine(A, Ag1, Ag2)
        addGridLine(A, grid)
        addSeamLine(A, seamLine)
        addCuttingLine(A, cuttingLine)

        # shirt Back B
        drawPoints(B, locals())
        #grainline points
        Bg1 = Pnt(a7.x,  b1.y + 8*CM)
        Bg2 = Pnt(Bg1.x, b4.y - 8*CM)
        # label points
        B.label_x,  B.label_y = Bg1.x + 3*CM, Bg1.y  + 3*CM
        # set letter location and size
        B.setLetter(x = b5.x, y = b12.c2.y, scaleby=15.0)
        # gridline
        grid = path()
        addToPath(grid, 'M', b1, 'L', b4, 'M', b19, 'L', b18, 'M', b6, 'L', b7, 'L', b14, 'M', b8, 'L', b10) #vertical
        addToPath(grid, 'M', b19, 'L', a3, 'M', b2, 'L', b8, 'M', b3, 'L', b9, 'M', b18, 'L', b10) #horizontal
        # foldLine
        foldLine = path()
        addToPath(foldLine, 'M', b19, 'L', b18)
        #seamline & cuttingline
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine:
            addToPath(P, 'M', b19, 'L', b5, 'C', b6.c1, b6.c2, b6, 'L', b16, 'C', b14.c1, b14.c2, b14, 'C', b8.c1, b8.c2, b8)
            addToPath(P, 'C', b12.c1, b12.c2, b12, 'C', b13.c1, b13.c2, b13, 'C', b17.c1, b17.c2, b17, 'L',  b18, 'L', b19)
        # add grid, grainline, seamline & cuttingline paths to pattern
        addGrainLine(B, Bg1, Bg2)
        addGridLine(B, grid)
        addFoldLine(B, foldLine)
        addSeamLine(B, seamLine)
        addCuttingLine(B, cuttingLine)

        # shirt Front C
        drawPoints(C, locals())
        #grainline points
        Cg1 = Pnt(c16.x - 1*CM, c16.y + 8*CM)
        Cg2 = Pnt(Cg1.x, c3.y - 8*CM)
        # label points
        C.label_x,  C.label_y = Cg1.x - 8*CM, Cg1.y + 3*CM
        # set letter location and size
        C.setLetter(x = c17.c1.x, y = c10.y, scaleby=15.0)
        # grid
        grid = path()
        addToPath(grid, 'M', b8, 'L', b10, 'M', c17, 'L', c15, 'L', c13, 'L', c14,'M', c6, 'L', c5, 'M', c23, 'L', c3, 'M', c18, 'L', c20, 'M', c19, 'L', c21) #vertical
        addToPath(grid, 'M', c23, 'M', c16, 'L', c22, 'M', c1, 'L', c19, 'M', b8, 'L', c2, 'M', b9, 'L', c10, 'M', b11, 'L', c12, 'M', b10, 'L', c3) #horizontal
        # fold line
        foldLine = path()
        addToPath(foldLine, 'M', c18, 'L', c20)
        # marking line
        markingLine = path()
        addToPath(markingLine, 'M', c1, 'L', c4)
        #seam line & cutting line
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine:
            addToPath(P, 'M', c16, 'C', c1.c1, c1.c2, c1, 'L', c18, 'L', c19, 'L', c21, 'L', c6, 'C', c12.c1, c12.c2, c12, 'C', c10.c1, c10.c2, c10, 'C', c8.c1, c8.c2, c8, 'C', c14.c1, c14.c2, c14, 'C', c17.c1, c17.c2, c17, 'L', c16)
        # add grid, grainLine, seamLine & cuttingLine paths to pattern
        addGrainLine(C, Cg1, Cg2)
        addGridLine(C, grid)
        addFoldLine(C, foldLine)
        addMarkingLine(C, markingLine)
        addSeamLine(C, seamLine)
        addCuttingLine(C, cuttingLine)

        # shirt Sleeve D
        drawPoints(D, locals())
        #grainline points
        Dg1 = Pnt(d2.x, d2.y)
        Dg2 = Pnt(Dg1.x, d3.y - 8*CM)
        # label points
        D.label_x,  D.label_y = Dg1.x + 3*CM, Dg1.y + 8*CM
        # set letter location and size
        D.setLetter(x = d10.c1.x, y = d24.y, scaleby=15.0)
        # gridline
        grid = path()
        addToPath(grid, 'M',d1,'L', d3, 'M', d7, 'L', d8, 'M', d5, 'L', d6, 'M', d20,  'L', d21) # vertical
        addToPath(grid, 'M', d5, 'L', d1, 'L',  d7, 'M', d5, 'L', d17, 'M', d22, 'L', d15, 'M', d7, 'L', d18, 'M', d23, 'L', d16) #diagonal
        addToPath(grid, 'M', d5, 'L', d7,  'M', d22, 'L', d23, 'M', d6, 'L', d8) #horizontal
        # marking line
        markingLine = path()
        addToPath(markingLine, 'M', d20, 'L', d21)
        # seamline & cuttingline
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine:
            addToPath(P, 'M', d5, 'C', d9.c1, d9.c2, d9, 'C', d10.c1, d10.c2, d10, 'C', d11.c1, d11.c2, d11, 'C', d1.c1, d1.c2, d1)
            addToPath(P, 'C', d14.c1, d14.c2, d14, 'C', d13.c1, d13.c2, d13, 'C', d12.c1, d12.c2, d12, 'C', d7.c1, d7.c2, d7)
            addToPath(P,  'C', d23.c1, d23.c2, d23, 'C', d16.c1, d16.c2, d16, 'L', d3, 'C', d21.c1, d21.c2, d21, 'C', d15.c1, d15.c2, d15)
            addToPath(P, 'C', d22.c1, d22.c2, d22, 'C', d5.c1, d5.c2, d5)
        # add grid, grainline, seamline & cuttingline paths to pattern
        addGridLine(D, grid)
        addGrainLine(D, Dg1, Dg2)
        addMarkingLine(D, markingLine)
        addSeamLine(D, seamLine)
        addCuttingLine(D, cuttingLine)

        # shirt Cuff E
        drawPoints(E, locals())
        #grainline points
        Eg1 = Pnt(e1.x + 2*CM,  e1.y + 2*CM)
        Eg2 = Pnt(e2.x - 2*CM, Eg1.y)
        # label points
        E.label_x,  E.label_y = Eg1.x + 3*CM, Eg1.y + 1*CM
        # set letter location and size
        E.setLetter(x = (Eg1.x+Eg2.x)/2.0, y = (e7.c1.y+e7.c2.y)/2.0, scaleby=7.0)
        # gridline
        grid = path()
        addToPath(grid, 'M', e3,'L', e7, 'M', e1, 'L', e5, 'M', e2, 'L', e6, 'M', e4,  'L', e8) # vertical
        addToPath(grid, 'M', e3, 'L', e4,  'M', e5, 'L', e6) #horizontal
        #seamline & cuttingline
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine:
            addToPath(P, 'M', e3, 'L', e4, 'L', e8, 'C', e6.c1, e6.c2, e6, 'L', e5, 'C', e7.c1, e7.c2, e7, 'L', e3)
        # add grid, grainline, seamline & cuttingline paths to pattern
        addGrainLine(E, Eg1, Eg2)
        addGridLine(E, grid)
        addSeamLine(E, seamLine)
        addCuttingLine(E, cuttingLine)

        # shirt Collar Stand F
        drawPoints(F, locals())
        #grainline points
        Fg1 = Pnt(f1.x + 2*CM, f1.y - 1*CM)
        Fg2 = Pnt(f2.x - 2*CM, Fg1.y)
        # label points
        F.label_x,  F.label_y = Fg1.x + 1*CM, f6.y + 1*CM
        # set letter location and size
        F.setLetter(x = f13.x, y = Fg1.y - 1*CM, scaleby=5.0)
        # gridline
        grid = path()
        addToPath(grid, 'M', f5,'L', f1, 'M', f7, 'L', f2, 'M', f8, 'L', f3) # vertical
        addToPath(grid, 'M', f12, 'L', f4, 'L', f18, 'L',f10,'M', f3, 'L', f9, 'M', f15, 'L', f14, 'L', f13, 'M', f17, 'L', f16, 'L', f14)
        addToPath(grid, 'M', f5, 'L', f17,  'M', f6, 'L', f8, 'M', f1, 'L', f3) #horizontal
        # fold line
        foldLine = path()
        addToPath(foldLine, 'M', f6, 'L', f12)
        #seamline & cuttingline
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine:
            addToPath(P, 'M', f6, 'L', f12, 'C', f4.c1, f4.c2, f4, 'C', f18.c1, f18.c2, f18, 'C', f10.c1, f10.c2, f10, 'L', f15, 'C', f15.c1, f15.c2, f14, 'C', f14.c1, f14.c2, f13, 'L', f6)
        # add grid, grainline, seamline & cuttingline paths to pattern
        addGrainLine(F, Fg1, Fg2)
        addGridLine(F, grid)
        addFoldLine(F, foldLine)
        addSeamLine(F, seamLine)
        addCuttingLine(F, cuttingLine)

        # shirt Collar G
        drawPoints(G, locals())
        #grainline points
        Gg1 = Pnt(f5.x + 1*CM, f5.y + 1*CM)
        Gg2 = Pnt(f7.x - 1*CM, Gg1.y)
        # label points
        G.label_x,  G.label_y = Gg1.x + 1*CM, Gg1.y + 1*CM
        # set letter location and size
        G.setLetter(x = (Gg1.x+Gg2.x)/2.0, y = Gg1.y + 3*CM, scaleby=5.0)
        # fold line
        foldLine = path()
        addToPath(foldLine, 'M', f5, 'L', f6)
        #seamline & cuttingline
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine:
            addToPath(P, 'M', f6, 'L', f5, 'L', f17, 'C', f17.c1, f17.c2, f16, 'L', f14, 'C', f14.c1, f14.c2, f13, 'L', f6)
        # add grid, grainline, seamline & cuttingline paths to pattern
        addGrainLine(G, Gg1, Gg2)
        # no grid for collar, included in collar stand pattern piece F
        addFoldLine(G, foldLine)
        addSeamLine(G, seamLine)
        addCuttingLine(G, cuttingLine)

        # call draw once for the entire pattern
        doc.draw()
        return
# vi:test ts=4 sw=4 expandtab:

