#!/usr/bin/env python
# This file is part of the tmtp (Tau Meta Tau Physica) project.
# For more information, see http://www.sew-brilliant.org/
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
# This is a pattern block to be used to make other patterns.

from math import asin

from pysvg.filter import *
from pysvg.gradient import *
from pysvg.linking import *
from pysvg.script import *
from pysvg.shape import *
from pysvg.structure import *
from pysvg.style import *
from pysvg.text import *
from pysvg.builders import *

from tmtpl.constants import *
from tmtpl.pattern   import *
from tmtpl.document   import *

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
        bodice = Pattern('bodice')
        bodice.styledefs.update(self.styledefs)
        bodice.markerdefs.update(self.markerdefs)
        doc.add(bodice)

        # create pattern pieces, add to pattern object
        bodice.add(PatternPiece('pattern', 'front', 'A', fabric=2, interfacing=0, lining=0))
        bodice.add(PatternPiece('pattern', 'back', 'B', fabric=2, interfacing=0, lining=0))
        A = bodice.front
        B = bodice.back

        # bodice Front A
        BUST_EASE= CD.bust_circumference/9.0
        WAIST_EASE = CD.waist_circumference/12.0
        # pattern points
        a = rPoint(A, 'a', 0.0, 0.0) # center neck
        b = rPoint(A, 'b', 0., CD.front_waist_length) # center waist
        c = rPoint(A, 'c',  0., a.y + CD.front_waist_length/5.0) # center across chest
        d = rPoint(A, 'd', a.x + CD.across_chest/2.0, c.y) # side across chest
        e = rPoint(A, 'e', 0., b.y - CD.front_shoulder_height) # front shoulder height
        f = rPoint(A, 'f', a.x + CD.front_shoulder_width/2.0, e.y) # front shoulder width
        h = rPoint(A, 'h', a.x + CD.neck_width/2.0, e.y) # side neck
        height = abs(distanceP(h, f))
        hypoteneuse = CD.shoulder
        base = (abs(hypoteneuse**2.0 - height**2.0))**0.5
        g = rPoint(A, 'g', f.x, f.y + base) # shoulder tip
        j = rPoint(A, 'j', 0., b.y - CD.side - (11/8.0)*IN) # center chest
        k = rPoint(A, 'k', a.x + (CD.front_bust_width)/2.0 , j.y) # side chest
        l = rPoint(A, 'l', k.x, k.y + CD.side) # side waist
        m = rPoint(A, 'm', d.x, k.y) # armscye corner
        pnt = polarPointP(m, 1*IN, angleOfDegree(315.0))
        n = rPointP(A, 'n', pnt) # armscye curve

        # front dart
        o = rPoint(A, 'o', 0., c.y + distanceP(c, b)/2.0) # dart apex height
        p = rPoint(A, 'p', a.x + distanceP(e, f)/2.0, o.y) # dart apex
        q = rPoint(A, 'q', p.x - 0.5*IN, b.y) # dart inside leg
        length1 = distanceP(p, q) # dart leg length
        length2 = CD.front_waist_width/2.0 - distanceP(b, q) # length of pattern between dart outside leg & side seam
        # TODO: use lib2geom python library to find accurate intersection between two circles
        Pnts = pntIntersectCirclesP(p, length1, l, length2)
        # Pnts.intersection is the number of intersections found (0, 1, or 2); Pnts.p1 is 1st intersection, Pnts.p2 is 2nd intersection.
        if (Pnts.intersections != 0):
            if (Pnts.p1.y > p.y): # choose the intersection below dart apex p
                pnt = Pnts.p1
            else:
                pnt = Pnts.p2
        else:
            print 'no intersection found'
        r = rPointP(A, 'r', pnt) # dart leg outside at waist

        #front  neck control points
        # b/w a & h
        angle = angleOfLineP(h, g) + ANGLE90
        length = distanceP(a, h)/3.0
        h_c2 = cPointP(A, 'h_c2', polarPointP(h, length, angle)) # control point is perpendicular to line h-g shoulder seam
        pnt1 = rightPointP(a, 1*IN) # arbitrary point right of point a
        h_c1 = cPointP(A, 'h_c1', pntIntersectLinesP(a, pnt1, h, h_c2)) # control point is horizontal to a, intersecting with line of h & h_c2. Gives appropriate width to neck opening

        # front armscye control points
        # b/w g & d
        length1 =  distanceP(d, g)/3.0
        d_c1 = cPointP(A, 'd_c1', polarPointP(g, length1, angleOfLineP(h, g) + ANGLE90))
        d_c2 = cPointP(A, 'd_c2', upPointP(d, length1))
        # b/w d & n - 1st control point
        length2 = distanceP(d, n)/3.0
        n_c1 = cPointP(A, 'n_c1', downPointP(d, length2))
        # b/w n & k - 2nd control point
        length3 = distanceP(n, k)/3.0
        k_c2 = cPointP(A, 'k_c2', polarPointP(k, length3, angleOfLineP(k, l) + ANGLE90))
        # b/w d & n - 2nd control point
        angleD = angleOfLineP(n, n_c1)
        angleK = angleOfLineP(k, n)
        angle = (angleD + angleK)/2.0
        pnt = polarPointP(n, length2, angle)
        n_c2 = cPointP(A, 'n_c2', pntIntersectLinesP(n, pnt, d, n_c1))
        # b/w n & k - 1st control point
        pnt = polarPointP(n, length3, angleOfLineP(n_c2, n))
        k_c1 = cPointP(A, 'k_c1', pntIntersectLinesP(n, pnt, k, k_c2))

        # generate front pattern svg info
        # grainline points
        Ag1 = rPoint(A,  'Ag1', a.x + 2*IN, a.y + 2*IN)
        Ag2 = rPoint(A, 'Ag2', Ag1.x, b.y - 2*IN)
        addGrainLine(A, Ag1, Ag2)
        # TODO: make label points a function
        # TODO: make setLetter a better function that accepts the parent object as an argument, separate from the parent object
        # Set letter location and size
        anchor_pnt = Pnt(Ag1.x + 3.5*IN, (Ag1.y + Ag2.y)/3.0)
        A.setLetter(anchor_pnt.x, anchor_pnt.y, scaleby=7.0)
        # label points
        A.label_x,  A.label_y = anchor_pnt.x, anchor_pnt.y +0.5*IN
        # TODO: make diamond markers to place along cuttingLine - single, double and triple
        # TODO: replace addGridLine(), addDartLine(), addSeamLine(), addCuttingLine(), and addGrainLine() with one command: addToPath(parent, 'nameofline', args*)
        # TODO: details: addToPath() to be addToPath(A, 'gridLine', args*) not addToPath(varname, args*) -> this would remove grid=path() and addGridLine(A,grid) commands
        # grid path
        grid = path()
        addToPath(grid, 'M', b, 'L', e, 'L', f, 'L', g, 'M', c, 'L', d, 'M', j, 'L', k, 'M', o, 'L', p,  'M', m, 'L', n,  'M', m, 'L', d)
        addGridLine(A, grid)
        # seamline & cuttingline paths
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine:
            addToPath(P, 'M', a, 'C', h_c1, h_c2, h, 'L', g, 'C', d_c1, d_c2, d,  'C',  n_c1, n_c2,  n, 'C', k_c1, k_c2,  k)
            addToPath(P, 'L', l, 'L', r, 'L', p, 'L', q, 'L', b, 'L', a)
        addSeamLine(A, seamLine)
        addCuttingLine(A, cuttingLine)

        # bodice Back B
        # back pattern points
        aa = rPoint(B, 'aa', 0., 0.) #aa: nape
        bb = rPoint(B, 'bb', 0., CD.back_waist_length) # bb: center waist
        cc = rPoint(B, 'cc', 0., CD.back_waist_length/4.0) #cc: center across back
        dd = rPoint(B, 'dd', aa.x - CD.across_back/2.0, cc.y) #dd: side across back
        ee = rPoint(B, 'ee', 0.,  bb.y - CD.back_shoulder_height) #ee: center shoulder height,
        ff = rPoint(B, 'ff', aa.x - CD.back_shoulder_width/2.0, ee.y) # #ff : side shoulder width
        hh = rPoint(B, 'hh', aa.x - CD.neck_width/2.0, ee.y) #hh: side neck
        height = abs(distanceP(hh, ff))
        hypoteneuse = CD.shoulder
        base = (abs(hypoteneuse**2.0 - height**2.0))**0.5
        gg = rPoint(B, 'gg', ff.x, ff.y + base) #gg: shoulder tip
        jj = rPoint(B, 'jj', 0., bb.y - CD.side + .25*IN) #jj: center chest
        kk = rPoint(B, 'kk', aa.x - (CD.back_underarm_width)/2.0 , jj.y) #kk: side chest
        ll = rPoint(B, 'll', kk.x, kk.y + CD.side) #ll: side waist marker
        mm = rPoint(B, 'mm', ll.x + .75*IN, ll.y) #mm: side waist
        nn = rPoint(B, 'nn', aa.x - distanceP(jj, kk)/2.0, bb.y) #nn: dart legt outside
        oo = rPoint(B, 'oo', dd.x, jj.y) #oo: armscye corner
        pp = rPointP(B, 'pp', polarPointP(oo, (9/8.)*IN, angleOfDegree(225))) # #pp: armscye curve
        qq = rPoint(B, 'qq', aa.x - (CD.back_waist_width/2.0 - distanceP(mm, nn)), bb.y) #qq: dart leg inside,
        rr = rPoint(B, 'rr',  nn.x + distanceP(nn, qq)/2.0, jj.y) #rr: dart apex,
        length1 = distanceP(pp, qq) # dart leg
        length2 = CD.back_waist_width/2.0 - distanceP(bb, qq)

        # back neck control points
        # b/w hh & aa
        angle = angleOfLineP(hh, gg) - ANGLE90
        length = distanceP(aa, hh)/3.0
        hh_c2 =  cPointP(B, 'hh_c2', polarPointP(hh, length,  angle) )
        pnt1 = leftPointP(aa, 1*IN) # arbitrary point left of nape
        hh_c1 =  cPointP(B, 'hh_c1', pntIntersectLinesP(aa, pnt1, hh, hh_c2))

        # slant back center seam
        bb2 = rPoint(B, 'bb2', bb.x - .5*IN,  bb.y)
        # TODO: use lib2geom python bindings to find accurate intersection between line & curve
        Pnts = pntIntersectCirclesP(kk, CD.side, bb2, CD.back_waist_width*0.5)
        if (Pnts.intersections > 0):
            if (Pnts.p1.x < Pnts.p2.x):
                pnt = Pnts.p1
            else:
                pnt = Pnts.p2
            # remove back waist dart
            mm2 = rPointP(B, 'mm2', pnt)
        else:
            print 'no intersection found' # TODO - make this more robust, or have a better fail mechanism

        # create neck dart
        NECK_DART_LENGTH = 3*IN
        NECK_DART_WIDTH = 0.25*IN
        back_neck_curve = pointList(aa, hh_c1, hh_c2, hh)
        length = curveLength(back_neck_curve)/3.0 # dart is at 1/3rd length of curve
        dart_apex,  curve1,  curve2 = neckDart(B, NECK_DART_WIDTH, NECK_DART_LENGTH, length, back_neck_curve)

        # read in new curve points
        bD2 = Pnt(name = 'bD2') # group to hold dart points  bD2.a, bD2.i, bD2.o
        bD2.a = rPointP(B, 'bD2.a', dart_apex) # dart apex point
        updatePoint(aa, curve1[0]) # update existing nape point
        bD2.i_c1 = cPointP(B, 'bD2.i_c1', curve1[1])
        bD2.i_c2 = cPointP(B, 'bD2.i_c2', curve1[2])
        bD2.i = rPointP(B, 'bD2.i', curve1[3]) # dart inside leg
        bD2.o = rPointP(B, 'bD2.o', curve2[0]) # dart outside leg
        updatePoint(hh_c1, curve2[1])
        updatePoint(hh_c2, curve2[2])
        # hh is last point in curve2 & was not changed

        # add fold points for dart - adds bD2.m,bD2.ic, bD2.oc - if dart were wider then we'd calculate some control points b/w bD2.i & bD2.m to match curve from bD2.i to aa
        addDartFold(B, bD2, bD2.i_c2) # create points for dart folded towards bD2.i_c2 - all folds either fold upwards or fold towards center

        # back armscye control points
        # b/w gg & dd
        length1 =  distanceP(gg, dd)/3.0
        dd_c1 = cPointP(B, 'dd_c1', polarPointP(gg, length1, angleOfLineP(hh, gg) - ANGLE90))
        dd_c2 = cPointP(B, 'dd_c2', upPointP(dd, length1))
        # b/w dd & pp - 1st control point
        length2 = distanceP(dd, pp)/3.0
        pp_c1 = cPointP(B, 'pp_c1', downPointP(dd, length2))
        # b/w pp & kk - 2nd control point
        length3 = distanceP(pp, kk)/3.0
        kk_c2 = cPointP(B,  'kk_c2', polarPointP(kk, length3, angleOfLineP(kk, mm2) - ANGLE90))
        # b/w dd & pp - 2nd control point
        angleDD = angleOfLineP(pp, pp_c1)
        angleKK = angleOfLineP(kk, pp)
        angle = (angleDD + angleKK)/2.0
        pnt = polarPointP(pp, length2, angle)
        pp_c2 = cPointP(B, 'pp_c2', pntIntersectLinesP(pp, pnt, dd, pp_c1))
        # b/w pp & kk - 1st control point
        pnt = polarPointP(pp, length3, angleOfLineP(pp_c2, pp))
        kk_c1 = cPointP(B, 'kk_c1', pntIntersectLinesP(pp, pnt, kk, kk_c2))

        # generate back pattern svg info
        #grainline
        Bg1 = rPoint(B,  'Bg1', aa.x - 2*IN, bD2.a.y + 1*IN)
        Bg2 = rPoint(B, 'Bg2', Bg1.x, bb.y - 2*IN)
        addGrainLine(B, Bg1, Bg2)
        # letter location and size
        anchor = Pnt(Bg1.x - 3.5*IN, (Bg1.y + Bg2.y)/3.0)
        B.setLetter(anchor.x, anchor.y, scaleby=7.0)
        # label
        B.label_x,  B.label_y = anchor.x, anchor.y + 0.5*IN
        # dartline - draw from cuttingline points bD2.ic & bD2.oc to apex bD2 .a
        dartLine = path()
        addToPath(dartLine, 'M', bD2.ic, 'L', bD2.a, 'L', bD2.oc)
        addDartLine(B, dartLine)
        # grid
        grid = path()
        addToPath(grid, 'M', bb, 'L', ee, 'L', ff, 'L', gg, 'M', cc, 'L', dd, 'M', jj, 'L', kk, 'M', oo, 'L', pp,  'M', oo, 'L', dd,  'M', kk, 'L', ll, 'L', mm)
        addGridLine(B, grid)
        # seamline & cuttingline
        seamLine = path()
        cuttingLine = path()
        for P in seamLine, cuttingLine:
            addToPath(P, 'M', aa, 'C', bD2.i_c1, bD2.i_c2, bD2.i, 'L', bD2.m, 'L', bD2.o, 'C', hh_c1, hh_c2, hh, 'L', gg, 'C', dd_c1, dd_c2, dd)
            addToPath(P, 'C',  pp_c1, pp_c2,  pp, 'C', kk_c1, kk_c2,  kk,'L', mm2, 'L', bb2, 'L', aa)
        addSeamLine(B, seamLine)
        addCuttingLine(B, cuttingLine)

        # call draw once for the entire pattern
        doc.draw()
        return

# vi:set ts=4 sw=4 expandtab:

