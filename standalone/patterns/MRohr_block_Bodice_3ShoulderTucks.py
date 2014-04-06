#!/usr/bin/env python
# MRohr_block_Bodice_3ShoulderTucks.py
# This is a library pattern to be used to make other patterns

from tmtpl.constants import *
from tmtpl.pattern   import *
from tmtpl.document   import *
from tmtpl.client   import Client

import pysvg.builders as PYB
import MRohr.blocks.MRohr_block_Bodice_Fitted as BB

"""
"""

def pattern(doc, A, B, CD):
        """
        Method defining a pattern design. This is where the designer places
        all elements of the design definition
        """

        # call bodice block function in library_Block_Bodice_Fitted_SingleDart_MRohr. Update locals() with values from BB.pattern()
        BB_locals, BB_globals = BB.pattern(doc, A, B, CD)
        globals().update(BB_locals)
        globals().update(BB_globals)

        # bodice Front A
        #aa : 'center neck',
        #ab : 'center waist',
        #ab.c1: 'front center waist control point',
        #ab.c2: ''front center waist control point',
        #ac : 'across chest center ',
        #ad : 'across chest side ',
        #ad.c1 : 'armscye across chest control point',
        #ad.c2 : 'armscye across chest control point',
        #ae : 'front shoulder height',
        #af : 'front shoulder width',
        #ag : 'shoulder tip',
        #ah : 'side neck',
        #ah.c1 : 'neck control point',
        #ah.c2 : 'neck control point',
        #ai : 'center chest',
        #aj : 'side chest',
        #aj.c1 : 'front armscye end control point',
        #aj.c2 : 'front armscye end control point'
        #ak : 'front side waist',
        #al : 'front armscye corner',
        #am : 'front armscye curve',
        #am.c1 : 'front armscye curve control point',
        #am.c2 : 'front armscye curve control point',
        #an : 'front center dart apex height',
        #ao:	'front chest width',
        #ap:	'front center reference point',
        ##as: python reserved word,
        #aD1 : 'front dart apex',
        #aD1.i : 'front dart leg inside at waist',
        #aD1.i.c1: 'front dart leg inside control point',
        #aD1.i.c2: 'front dart leg inside control point',
        #aD1.o : 'front dart leg outside at waist',
        #aD1.o.c1 : 'front dart leg outside at waist control point',
        #aD1.o.c2 : 'front dart leg outside at waist control point',
        #aD1.m: 'front dart center at waist',
        #aD1.m.c1 : 'front dart center at waist control point',
        #aD1.m.c2 : 'front dart center at waist control point',
        # aD1.oc: 'front dart leg extension towards seam allowance',
        # aD1.ic: 'front dart leg extension towards seam allowance',

        # bodice back points
        #ba: nape,
        #bb: center waist,
        # bb.c1: center waist control point,
        # bb.c2: center waist control point,
        #bc: center across back,
        #bd: side across back,
        #bd.c1: armscye 'across back' control point,
        #bd.c2: armscye 'across back' control point,
        #be: center shoulder height,
        #bf : side shoulder width,
        #bg: shoulder tip,
        #bh: side neck,
        #bh.c1: neck control point,
        #bh.c2: neck control point,
        #bi: center chest,
        #bj: side chest,
        #bj.c1: armscye end control point,
        #bj.c2: armscye end control point,
        #bk: side waist,
        #bl: armscye corner,
        #bm: armscye curve,
        #bD1: dart apex,
        #bD1.o: dart leg outside,
        #bD1.o.c1: dart leg outside control point,
        #bD1.o.c2: dart leg outside control point,
        #bD1.o2: 'back dart leg extension towards seam allowance',
        #bD1.i: dart leg inside,
        #bD1.ic: 'back dart leg extension towards seam allowance',
        #bD1.m: 'back dart center at waist',
        #bD1.m.c1: 'back dart center at waist control point',
        #bD1.m.c2: 'back dart center at waist control point',

        # adjustments for 3 shoulder tucks
        midpoint = pntMidPointP(aD1.i, aD1.o) # midpoint of original dart at waist
        dartwidth = distanceP(aD1.i, aD1.o)/3.0 # new dart width is 1/3 of original waist dart
        rotate_angle = abs(angleOfVectorP(aD1.i, aD1, aD1.o))/3.0 # new dart angle is 1/3 of original dart angle
        dartwidth_half = dartwidth/2.0

        # 3 shoulder darts, base of 1st dart is current dart apex, base of 2nd dart is 1" right, 3rd dart 1" right
        # keep current aD1
        aD2, aD3 = Pnt(name='aD2'),  Pnt(name='aD3')
        aD2 = rPointP(A, 'aD2', rightPointP(aD1, 1*IN))
        aD3 = rPointP(A, 'aD3', rightPointP(aD2, 1*IN))

        # slash & spread the waist darts.o to.i
        # 1st create two svg points at end of each slashline
        aD2.o = rPointP(A, 'aD2.o', pntMidPointP(ah, ag))  # middle tuck is at midpoint on shoulder
        aD2.i = rPointP(A, 'aD2.i', aD2.o)

        pnt = pntOnLineP(aD2.o, ah, 1*IN) # first tuck is 1IN up from middle tuck
        updatePoint(aD1.o, pnt)
        updatePoint(aD1.i, pnt)

        aD3.o = rPointP(A, 'aD3.o', pntOnLineP(aD2.o, ag, 1*IN)) # third tuck is 1IN down from middle tuck
        aD3.i = rPointP(A, 'aD3.i', aD3.o)

        # rotate around aD1
        # keep aD1, aD1.i
        rotate_pnt = Pnt()
        slashAndSpread(aD1, rotate_angle, aD1.o, aD2.i, aD2.o, aD3.i, aD3.o, ag, ad.c1, ad.c2, ad, am.c1, am.c2, am)
        slashAndSpread(aD1, rotate_angle, aj.c1, aj.c2, aj,  ao, ak, aD3, aD2)

        # rotate around aD2
        # keep aD2, aD2.i
        slashAndSpread(aD2, rotate_angle, aD2.o, aD3.i, aD3.o, ag, ad.c1, ad.c2, ad, am.c1, am.c2, am, aj.c1, aj.c2, aj,  ao, ak, aD3, aD2)

        # rotate around aD3
        # keep aD3, aD3.i 
        slashAndSpread(aD3, rotate_angle, aD3.o, ag, ad.c1, ad.c2, ad, am.c1, am.c2, am, aj.c1, aj.c2, aj,  ao, ak, aD3)

        # add tuck midpoints ..
        addDartFold(A, aD1, ah)
        addDartFold(A, aD2, aD1.o)
        addDartFold(A, aD3, aD2.o)

        # find points where dart lines intersect 'across chest' line to determine where tucks end

        aD1.h1 = rPointP(A, 'aD1.h1', pntIntersectLinesP(aD1.o, aD1, ac, ad))
        aD1.h2 = rPointP(A, 'aD1.h2', pntOnLineP(aD1.i, aD1, distanceP(aD1.o, aD1.h1)))
        aD2.h1 = rPointP(A, 'aD2.h1', pntIntersectLinesP(aD2.o, aD2, ac, ad))
        aD2.h2 = rPointP(A, 'aD2.h2', pntOnLineP(aD2.i, aD2, distanceP(aD2.o, aD2.h1)))
        aD3.h1 = rPointP(A, 'aD3.h1', pntIntersectLinesP(aD3.o, aD3, ac, ad))
        aD3.h2 = rPointP(A, 'aD3.h2', pntOnLineP(aD3.i, aD3, distanceP(aD3.o, aD3.h1)))

        # adjust front waist control points
        pnt = polarPointP(ak, distanceP(ak, ab)/3.0, angleOfLineP(aj, ak) + ANGLE90)
        updatePoint(ab.c1, pnt)
        pnt = rightPointP(ab, distanceP(ak, ab)/3.0)
        updatePoint(ab.c2, pnt)


        # bodice Back B

        # adjust back waist control points
        pnt = polarPointP(bk, distanceP(bk, bD1.o)/3.0, angleOfLineP(bj, bk) - ANGLE90)
        updatePoint(bD1.o.c1, pnt)

        # clean up svg
        for pnt in aD1.o.c1, aD1.o.c2, aD1.m.c1, aD1.m.c2, aD1.i.c1, aD1.i.c2:
            updatePoint(pnt, ap)
            pnt.name = ''


        return locals(), globals()

# vi:set ts=4 sw=4 expandtab:

