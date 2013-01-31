#!/usr/bin/env python
# This file is part of the tmtp (Tau Meta Tau Physica) project.
# For more information, see http://www.taumeta.org/
#
# Copyright (C) 2010, 2011, 2012 Susan Spencer, Steve Conklin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. Attribution must be given in
# all derived works.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

# SamplePattern.py

from math import asin
from pysvg.builders import path

from tmtpl.constants import *
from tmtpl.pattern import *
from tmtpl.document  import *

class PatternDesign():

    def __init__(self):
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
        CD = self.CD    #client data is prefaced with CD

        #TODO: add function to select printer/page size
        printer = '36" wide carriage plotter'
        # TODO: add function to select company/designerpatternmaker name
        companyName = 'Company Name'  # mandatory
        designerName = 'Designer Name' # mandatory
        patternmakerName = 'Patternmaker Name'

        # this info is specific to this file
        patternName = 'Pattern Name or Short Description' # mandatory
        # TODO: lookup/generate next available pattern number
        patternNumber = 'Pattern Number' # mandatory

        # create document
        doc = setupPattern(self, CD, printer, companyName, designerName, patternName, patternNumber)

        # create pattern object, add to document
        # TODO: make update styledefs & markerdefs transparent
        # TODO: rewrite as: bodice = pattern(doc, 'bodice') so that update(self.styledefs) and update(self.markerdefs) is automatic
        bodice = Pattern('bodice')
        bodice.styledefs.update(self.styledefs)
        bodice.markerdefs.update(self.markerdefs)
        doc.add(bodice)

        # create pattern pieces, add to pattern object
        # TODO: rewrite as:  A = patternPiece(bodice, 'A', 'front', fabric=2, interfacing=0, lining=0) so that A = bodice.front is automatic
        bodice.add(PatternPiece('pattern', 'front', 'A', fabric=2, interfacing=0, lining=0))
        bodice.add(PatternPiece('pattern', 'back', 'B', fabric=2, interfacing=0, lining=0))
        A = bodice.front
        B = bodice.back

        # bodice Front A
        BUST_EASE = (CD.bust_circumference/10.0)/4.0
        WAIST_EASE = (CD.waist_circumference/12.0)/4.0
        # pattern points
        a = rPoint(A, 'a', 0.0, 0.0) # center neck
        b = rPoint(A, 'b', 0.0, CD.front_waist_length) # center waist
        c = rPoint(A, 'c',  0.0, a.y + CD.front_waist_length/5.0) # center across chest
        d = rPoint(A, 'd', a.x + CD.across_chest/2.0, c.y) # side across chest
        e = rPoint(A, 'e', 0.0, b.y - CD.front_shoulder_height) # front shoulder height
        f = rPoint(A, 'f', a.x + CD.front_shoulder_width/2.0, e.y) # front shoulder width
        h = rPoint(A, 'h', a.x + CD.neck_width/2.0, e.y) # side neck
        # find shoulder tip given shoulder length (CD.shoulder), height of triangle (from h.y to f.y)
        height = abs(distanceP(h, f))
        hypoteneuse = CD.shoulder
        base = (abs(hypoteneuse**2.0 - height**2.0))**0.5
        g = rPoint(A, 'g', f.x, f.y + base) # shoulder tip
        j = rPoint(A, 'j', a.x, b.y - CD.side - (11/8.0)*IN) # chest center
        k = rPointP(A, 'k', rightPointP(j, CD.front_bust_width/2.0 + BUST_EASE)) # chest side
        m = rPoint(A, 'm', d.x, k.y) # armscye corner
        n = rPointP(A, 'n', polarPointP(m, 1*IN, angleOfDegree(315.0))) # armscye curve

        # front dart
        # TODO: use lib2geom python library to find robust more precise intersection between two circles
        FRONT_WAIST_DART_LENGTH = distanceP(c, b)/2.0
        FRONT_WAIST_DART_WIDTH = CD.front_waist_width/6.0
        aD1 = PntP(name='aD1') # group to hold all dart points - aD1.a, aD1.i, aD1.o, aD1.m aD1.ic, aD1.oc
        aD1.i = rPointP(A, 'aD1.i', rightPointP(b, (CD.front_bust_points_distance + BUST_EASE - FRONT_WAIST_DART_WIDTH)/2.0)) # dart inside leg
        aD1.a = rPoint(A, 'aD1.a', aD1.i.x + FRONT_WAIST_DART_WIDTH/2.0, aD1.i.y - FRONT_WAIST_DART_LENGTH) # dart apex
        aD1.o = rPoint(A, 'aD1.o', aD1.i.x + FRONT_WAIST_DART_WIDTH, aD1.i.y ) # dart outside leg
        # find waist side
        pnts = pntIntersectCirclesP(k, CD.side, aD1.o, (CD.front_waist_width/2.0 + WAIST_EASE) - distanceP(aD1.i, b))
        # pnts.intersection is the number of intersections found (0, 1, or 2); Pnts.p1 is 1st intersection, Pnts.p2 is 2nd intersection.
        if (pnts.intersections != 0):
            if (pnts.p1.x > aD1.o.x): # choose the intersection to the right of aD1.o
                pnt = pnts.p1
            else:
                pnt = pnts.p2
            l = rPointP(A, 'l', pnt) # side waist
        else:
            print 'no intersection found'
        # control points b/w l & aD1.o
        length = distanceP(aD1.o, l)/3.0
        aD1.o.c1 = cPointP(A, 'aD1.o.c1', polarPointP(l, length, angleOfLineP(k, l) + ANGLE90))
        aD1.o.c2 = cPointP(A, 'aD1.o.c2', polarPointP(aD1.o, length, angleOfLineP(aD1.a, aD1.o) - ANGLE90))
        # shape dart at seamline & cuttingline to allow folding towards center, use nearest point towards center 'b'
        addDartFold(A, aD1, b) # adds aD1.m, aD1.ic, ad1.oc -- midpoint on seamline (.m), inside leg on cutting line (.ic) & outside leg on cutting line (.oc)

        # front  neck control points
        # b/w a & h
        angle = angleOfLineP(h, g) + ANGLE90
        length = distanceP(a, h)/3.0
        h.c2 = cPointP(A, 'h.c2', polarPointP(h, length, angle)) # control point is perpendicular to line h-g shoulder seam
        pnt1 = rightPointP(a, 1*IN) # arbitrary point right of point a
        h.c1 = cPointP(A, 'h.c1', pntIntersectLinesP(a, pnt1, h, h.c2)) # control point is horizontal to a, intersecting with line of h & h.c2. Gives appropriate width to neck opening

        # front armscye control points
        angle1 = angleOfLineP(n, g) # angle from d to d.c2
        length1 = distanceP(g, d)/3.0
        d.c2 = cPointP(A, 'd.c2', polarPointP(d, length1, angle1))
        d.c1 = cPointP(A, 'd.c1', polarPointP(g, length1, angleOfLineP(g, d.c2)))

        length2 = distanceP(n, k)/3.0
        angle2 = (angleOfLineP(n, d) + angleOfLineP(k, n))/2.0
        n.c1 = cPointP(A, 'n.c1', polarPointP(d, length2, angleOfLineP(d.c2, d)))
        n.c2 =cPointP(A, 'n.c2', polarPointP(n, length2, angle2))

        length3 = distanceP(k, n)/3.0
        angle3 = angleOfLineP(k, l) + ANGLE90
        k.c2= cPointP(A, 'k.c2',polarPointP(k, length3, angle3))
        k.c1 = cPointP(A, 'k.c1', polarPointP(n, length3, angle2 - ANGLE180))

        # bodice Back B
        # back pattern points
        aa = rPoint(B, 'aa', 0.0, 0.0) #nape
        aa2 = rPointP(B, 'aa2', aa) # copy of nape - use this in grid to view how much aa moved
        # slant waist center inwards a small bit
        bb = rPointP(B, 'bb', downPointP(aa, CD.back_waist_length)) # waist center
        cc = rPointP(B, 'cc', downPointP(aa, CD.back_waist_length/4.0)) # across back center
        dd = rPointP(B, 'dd', leftPointP(cc, CD.across_back/2.0)) # across-back side
        ee = rPointP(B, 'ee', upPointP(bb, CD.back_shoulder_height))#shoulder height center
        ff = rPointP(B, 'ff', leftPointP(ee, CD.back_shoulder_width/2.0)) # # shoulder height width
        hh = rPointP(B, 'hh', leftPointP(ee, CD.neck_width/2.0)) # neck side
        height = abs(distanceP(hh, ff))
        hypoteneuse = CD.shoulder
        base = (abs(hypoteneuse**2.0 - height**2.0))**0.5
        gg = rPointP(B, 'gg', downPointP(ff, base))#shoulder tip
        jj = rPointP(B, 'jj', upPointP(bb, CD.side - .25*IN)) #chest center
        kk = rPointP(B, 'kk', leftPointP(jj, CD.back_bust_width/2.0 + BUST_EASE)) #chest side
        ll = rPointP(B, 'll', downPointP(kk, CD.side))#waist side - marker
        nn = rPoint(B, 'nn', dd.x, jj.y) #armscye corner
        oo = rPointP(B, 'oo', polarPointP(nn, (9/8.0)*IN, angleOfDegree(225))) #armscye curve

        # back control points
        # back center seam control points - b/w bb & aa
        length = distanceP(bb, aa)/3.0
        aa.c1 = cPointP(B, 'aa.c1', upPointP(bb, length))
        aa.c2 = cPointP(B, 'aa.c2', downPointP(aa, length/2.0))
        # back neck control points - b/w aa & hh
        angle = angleOfLineP(hh, gg) - ANGLE90
        length = distanceP(aa, hh)/3.0
        hh.c2 =  cPointP(B, 'hh.c2', polarPointP(hh, length,  angle) )
        pnt1 = leftPointP(aa, 1*IN) # arbitrary point left of nape
        hh.c1 =  cPointP(B, 'hh.c1', pntIntersectLinesP(aa, pnt1, hh, hh.c2))

        # back waist dart
        BACK_WAIST_DART_LENGTH = distanceP(jj, bb)*(5/6.0)
        BACK_WAIST_DART_WIDTH = CD.back_waist_width/8.0
        bD1 = PntP(name='bD1') # group to hold all dart points - bD1.a, bD1.i, bD1.o, bD1.m bD1.ic, bD1.oc
        pnt1 = pntMidPointP(kk, jj)
        pnt2 = downPointP(pnt1, distanceP(jj, bb)/6.0)
        bD1.a = rPointP(B, 'bD1.a', pnt2) # dart apex
        bD1.i = rPoint(B, 'bD1.i', bD1.a.x + BACK_WAIST_DART_WIDTH/2.0, bb.y) # dart inside leg
        bD1.o = rPoint(B, 'bD1.o', bD1.a.x - BACK_WAIST_DART_WIDTH/2.0, bb.y) # dart outside leg
        # TODO: use lib2geom python bindings to find most accurate intersection between line & curve,
        # TODO: create better fail mechanism
        Pnts = pntIntersectCirclesP(kk, CD.side, bD1.o, CD.back_waist_width/2.0 + WAIST_EASE - distanceP(bb, bD1.i))
        if (Pnts.intersections > 0):
            if (Pnts.p1.x < Pnts.p2.x):
                pnt = Pnts.p1
            else:
                pnt = Pnts.p2
            # remove back waist dart
            mm = rPointP(B, 'mm', pnt)
        else:
            print 'no intersection found'
        # back waist control points
        length = distanceP(bD1.o, mm)/3.0
        bD1.o.c1 = cPointP(B, 'bD1.o.c1', polarPointP(mm, length, angleOfLineP(kk, mm) - ANGLE90))
        bD1.o.c2 = cPointP(B, 'bD1.o.c2', polarPointP(bD1.o, length, angleOfLineP(bD1.a, bD1.o) + ANGLE90))
        # create points for dart folded towards bb (waist darts are folded towards center)
        # creates points on cutting line - bD1.ic = inside dart leg, bD1.oc= outside dart leg, bD1.m= middle point on cutting line
        addDartFold(B, bD1, bb)

        # back neck dart
        back_neck_curve = pointList(aa, hh.c1, hh.c2, hh)
        back_neck_curve_length = curveLength(back_neck_curve)
        position = back_neck_curve_length/3.0 # dart is at 1/3 length of curve
        NECK_DART_LENGTH = distanceP(aa, cc)*(1/2.0)
        NECK_DART_WIDTH = back_neck_curve_length/7.0
        # split neck curve into two parts, find dart apex
        bD2 = PntP(name='bD2') # group to hold dart points  bD2.a, bD2.i, bD2.o, bD2.m, bD2.ic, bD2.oc

        # TODO: create addNeckDart(parent, dart object, dart width, dart length, position, curve) to replace the next 9 lines
        dart_apex,  curve1,  curve2 = neckDart(B, NECK_DART_WIDTH, NECK_DART_LENGTH, position, back_neck_curve)
        bD2.a = rPointP(B, 'bD2.a', dart_apex) # dart apex point
        updatePoint(aa, curve1[0]) # update existing nape point
        bD2.i.c1 = cPointP(B, 'bD2.i.c1', curve1[1])
        bD2.i.c2 = cPointP(B, 'bD2.i.c2', curve1[2])
        bD2.i = rPointP(B, 'bD2.i', curve1[3]) # dart inside leg
        bD2.o = rPointP(B, 'bD2.o', curve2[0]) # dart outside leg
        updatePoint(hh.c1, curve2[1])
        updatePoint(hh.c2, curve2[2])


        # hh is last point in curve2 & was not changed
        # add fold points for dart - adds bD2.m,bD2.ic, bD2.oc - if dart were wider then we'd calculate some control points b/w bD2.i & bD2.m to match curve from bD2.i to aa
        addDartFold(B, bD2, bD2.i.c2) # create points for dart folded towards bD2.i.c2 - all folds either fold upwards or fold towards center
        # rotate aa.c2 control point
        slashAndSpread(bD2.a, aa.c2)

        # back armscye control points
        # from gg to dd
        length1 = distanceP(gg, dd)/3.0
        angle1 = angleOfLineP(oo, gg) # angle from d to d.c2
        dd.c2 = cPointP(B, 'dd.c2', polarPointP(dd, length1, angle1))
        dd.c1 = cPointP(B, 'dd.c1', polarPointP(gg, length1, angleOfLineP(gg, dd.c2)))
        # from dd to oo
        length2 = distanceP(dd, oo)/3.0
        angle2 = (angleOfLineP(oo, dd) + angleOfLineP(kk, oo))/2.0
        oo.c1 = cPointP(B, 'oo.c1', polarPointP(dd, length2, angleOfLineP(dd.c2, dd)))
        oo.c2 =cPointP(B, 'oo.c2', polarPointP(oo, length2, angle2))
        # from oo to kk
        length3 = distanceP(oo, kk)/3.0
        angle3 = angleOfLineP(kk, mm) - ANGLE90
        kk.c2= cPointP(B, 'kk.c2',polarPointP(kk, length3, angle3))
        kk.c1 = cPointP(B, 'kk.c1', polarPointP(oo, length3, angle2 - ANGLE180))

        # ---- all pattern points have been created for front A & back B
        # ---- now create pattern paths & labels with these points
        # TODO: write functions to make this section more encapsulated

        # front A  paths & labels
        # grainline
        Ag1 = rPoint(A,  'Ag1', a.x + 2*IN, a.y + 2*IN)
        Ag2 = rPoint(A, 'Ag2', Ag1.x, b.y - 2*IN)
        addGrainLine(A, Ag1, Ag2)

        # Set letter location and size
        # TODO: make setLetter a better function that accepts the parent object as an argument
        anchor_pnt = Pnt(Ag1.x + 2*IN, (Ag1.y + Ag2.y)/3.0)
        A.setLetter(anchor_pnt.x, anchor_pnt.y, scaleby=7.0)

        # label
        # TODO: make label points a function
        A.label_x,  A.label_y = anchor_pnt.x, anchor_pnt.y +0.5*IN

        # TODO: make diamond markers to place along cuttingLine - single, double and triple
        # TODO: replace addGridLine(), addDartLine(), addSeamLine(), addCuttingLine(), and addGrainLine() with one command: addLine(parent, 'linetype', args*)
        # TODO: combine grid=path() and addGridLine(A,grid) commands
        # grid
        grid = path()
        addToPath(grid, 'M', b, 'L', e, 'L', f, 'L', g, 'M', c, 'L', d, 'M', j, 'L', k, 'M', m, 'L', n,  'M', m, 'L', d)
        addGridLine(A, grid)
        # dart
        dart = path()
        addToPath(dart, 'M', aD1.ic, 'L', aD1.a, 'L', aD1.oc)
        addDartLine(A, dart)
        # seamline & cuttingline
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine:
            addToPath(P, 'M', a, 'C', h.c1, h.c2, h, 'L', g, 'C', d.c1, d.c2, d,  'C',  n.c1, n.c2,  n, 'C', k.c1, k.c2,  k)
            addToPath(P, 'L', l, 'C', aD1.o.c1, aD1.o.c2, aD1.o, 'L', aD1.m, 'L', aD1.i, 'L', b, 'L', a)
        addSeamLine(A, seamLine)
        addCuttingLine(A, cuttingLine)

        # B back bodice paths and labels
        # grainline
        Bg1 = rPoint(B,  'Bg1', a.x - 2*IN, bD2.a.y + 1*IN)
        Bg2 = rPoint(B, 'Bg2', Bg1.x, b.y - 2*IN)
        addGrainLine(B, Bg1, Bg2)
        # letter location and size
        anchor = Pnt(Bg1.x - 3.5*IN, (Bg1.y + Bg2.y)/3.0)
        B.setLetter(anchor.x, anchor.y, scaleby=7.0)
        # label
        B.label_x,  B.label_y = anchor.x, anchor.y + 0.5*IN
        # dartline
        dartLine = path()
        addToPath(dartLine, 'M', bD1.ic, 'L', bD1.a, 'L', bD1.oc) # back waist dart
        addToPath(dartLine, 'M', bD2.ic, 'L', bD2.a, 'L', bD2.oc) # back neck dart
        addDartLine(B, dartLine)
        # grid
        grid = path()
        addToPath(grid, 'M', bb, 'L', ee, 'L', ff, 'L', gg, 'M', cc, 'L', dd, 'M', jj, 'L', kk, 'M', nn, 'L', oo,  'M', nn, 'L', dd,  'M', kk, 'L', ll, 'L', mm)
        addGridLine(B, grid)
        # seamline & cuttingline
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine:
            addToPath(P, 'M', aa, 'C', bD2.i.c1, bD2.i.c2, bD2.i, 'L', bD2.m, 'L', bD2.o, 'C', hh.c1, hh.c2, hh, 'L', gg) # nape, neck dart, shoulder, shoulder tip
            addToPath(P, 'C', dd.c1, dd.c2, dd,'C',  oo.c1, oo.c2,  oo, 'C', kk.c1, kk.c2,  kk) # armscye
            addToPath(P, 'L', mm, 'C', bD1.o.c1, bD1.o.c2, bD1.o, 'L', bD1.m, 'L', bD1.i, 'L', bb) # side, waist dart, waist center
            addToPath(P, 'C', aa.c1, aa.c2, aa) # back center seam to nape
        addSeamLine(B, seamLine)
        addCuttingLine(B, cuttingLine)

        # call draw once for the entire pattern
        doc.draw()
        return

# vi:set ts=4 sw=4 expandtab:

