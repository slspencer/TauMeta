#!/usr/bin/python
#
# This file is part of the tmtp (Tau Meta Tau Physica) project.
# For more information, see http://www.sew-brilliant.org/
#
# Copyright (C) 2010, 2011, 2012 Susan Spencer and Steve Conklin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. Attribution must be given in
# all derived works.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#python libs
import math
import string
import re
import random
import inspect
from math import sin, cos, pi, sqrt
#pysvg libs
import pysvg.builders as PYB
# tmtp libs
from pattern import *
from constants import *
from utils import debug


# collars

def collarEton(parent, front_curve, back_curve, FRONT_STAND, FRONT_WIDTH, BACK_STAND, BACK_WIDTH):
        '''Accepts parent pattern piece, array with front neck curve P0 C11 C12 P1  and back neck curve P2 C21 C22 P3,
        width of collar at front, width of collar at back, and collar stand (how high it stands above back nape)'''
        COLLAR_ANGLE = 80.0
        # inside curve
        # front curve stays the same, becomes 1st half of inside curve
        inside_curve = front_curve
        # back curve is translated to meet 1st half of inside curve - angle of control lines form a straight line b/w front curve & back curve
        angle1 = angleOfLineP(front_curve[2], front_curve[3])
        angle2 = angleOfLineP(back_curve[0], back_curve[1])
        rotation_angle = angle2 - angle1
        i = 1
        while i < len(back_curve):
            length = distanceP(back_curve[0], back_curve[i])
            back_angle = angleOfLineP(back_curve[0], back_curve[i])
            rotated_point = polarPointP(front_curve[3], length, back_angle - rotation_angle)
            inside_curve.append(rotated_point)
            i = i + 1
        # middle curve
        P0a = polarPointP(inside_curve[0], FRONT_WIDTH, angleOfLineP(inside_curve[0], inside_curve[1]) + angleOfDegree(COLLAR_ANGLE))
        P1a = polarPointP(inside_curve[3], (FRONT_WIDTH + BACK_WIDTH)/2.0, angleOfLineP(inside_curve[2], inside_curve[3])+ angleOfDegree(90))
        P2a = polarPointP(inside_curve[6], BACK_WIDTH, angleOfLineP(inside_curve[5], inside_curve[6]) + angleOfDegree(90))
        # middle curve control points
        middle_curve = []
        length = distanceP(P0a, P1a)/3.0
        C11a = rightPointP(P0a, distanceP(P0a, P1a)/3.0)
        C12a = polarPointP(P1a, length, angleOfLineP(inside_curve[3], inside_curve[2]))
        length = distanceP(P1a, P2a)/3.0
        C21a = polarPointP(P1a, length, angleOfLineP(inside_curve[3], inside_curve[4]))
        C22a = polarPointP(P2a, length, angleOfLineP(inside_curve[6], inside_curve[5]))
        for pnt in P0a, C11a, C12a, P1a, C21a, C22a, P2a:
            middle_curve.append(pnt)
        # outside curve
        stand = FRONT_STAND
        width = FRONT_WIDTH
        #length = stand+ sqrt(stand**2 + width**2)
        length = 2*stand + width
        angle = angleOfLineP(inside_curve[0], inside_curve[1]) + angleOfDegree(COLLAR_ANGLE) # collar point not on center front line
        P0b = polarPointP(inside_curve[0], length, angle)

        stand = (FRONT_STAND + BACK_STAND)/2.0
        width = (FRONT_WIDTH + BACK_WIDTH)/2.0
        #length = stand + sqrt(stand**2 + width**2)
        length = 2*stand + width
        angle = angleOfLineP(inside_curve[2], inside_curve[3])+ angleOfDegree(90) # outer shoulder point 90degrees from inner shoulder point
        P1b = polarPointP(inside_curve[3], length, angle)

        stand = BACK_STAND
        width = BACK_WIDTH
        #length = stand + sqrt(stand**2 + width**2)
        length = 2*stand + width
        angle = angleOfLineP(inside_curve[5], inside_curve[6]) + angleOfDegree(90) # outer back point 90 degrees from inner collar point
        P2b = polarPointP(inside_curve[6], length, angle)

        # outside curve control points
        outside_curve = []
        length = distanceP(P0b, P1b)/3.0
        C11b = rightPointP(P0b, length)
        C12b = polarPointP(P1b, length, angleOfLineP(inside_curve[3], inside_curve[2]))
        length = distanceP(P1b, P2b)/3.0
        C21b = polarPointP(P1b, length, angleOfLineP(inside_curve[3], inside_curve[4]))
        C22b = polarPointP(P2b, length, angleOfLineP(inside_curve[6], inside_curve[5]))
        for pnt in P0b, C11b, C12b, P1b, C21b, C22b, P2b:
            outside_curve.append(pnt)

        # slash & fold - divide (outside_curve length - middle curve length) by 10 --> 5 folds
        collar_length = curveLength(middle_curve)
        outside_length = curveLength(outside_curve)
        fold_length = (outside_length - collar_length)/10.0 # fold amount
        radial_pnt = pntIntersectLinesP(inside_curve[0], outside_curve[0], inside_curve[6], outside_curve[6])
        inside_interp = interpolateCurveList(inside_curve)
        outside_interp = interpolateCurveList(outside_curve)
        inside_slash, outside_slash = [], []

        begin_inside_curve_length = curveLength(inside_curve)
        begin_outside_curve_length = curveLength(outside_curve)

        # slash & spread (or in this case, fold) at 5 lines across collar -
        # divide collar at 2 points on front, then at shoulder, then at 2 points on back neck
        # easy division at control points and at shoulder point - if inside curve is P0 C11 C12 P1 C21 C22 P2
        # then intersect curve at C11, C12, C21, & C22
        # The radial_pnt defined above provides the central point to define the slash
        # Slash&Spread: The line from the radial_pnt to C11 intersects inside_curve & outside_curve to define pnt11 & pnt12
        #    Fold pnt12 back 1/10 of the difference between outside_curve length & middle_curve length to get pnt13
        #    The angle pnt12, radial_pnt, pnt13 is the amount to fold all points above pnt11 & pnt12.
        #    Keep pnt11 & pnt13 as new points on inside_curve & outside_curve.
        # Repeat Slash & Spread for remaining 4 divisions: radial_pnt-C12, radial_pnt-P1, radial_pnt-C21, radial_pnt-C22

        inside_collar, middle_collar, outside_collar = [], [], []

        # save 1st points in output arrays:
        inside_collar.append(inside_curve[0])
        middle_collar.append(middle_curve[0])
        outside_collar.append(outside_curve[0])

        # 1st slash division
        pnts1 = intersectLineCurve(radial_pnt, inside_curve[1], inside_curve) # inside collar slash point
        pnts2 = intersectLineCurve(radial_pnt, inside_curve[1], outside_curve) # outside collar slash point
        pnt11, pnt12 = pnts1[0], pnts2[0]
        # find fold result
        length = interpolatedCurveLengthAtPoint(pnt12, outside_interp)
        pnt13 = interpolatedCurvePointAtLength(length - fold_length, outside_interp)
        # store new inside & outside points
        inside_collar.append(pnt11)
        outside_collar.append(pnt13)
        #fold remaining points
        pivot = pnt11
        angle = angleOfVectorP(pnt12, radial_pnt, pnt13)
        i = 2
        for curve in inside_curve, middle_curve, outside_curve:
            while i < len(curve):
                slashAndSpread(pivot, angle, curve[i])
                i = i + 1
        # store
        inside_collar.append(inside_curve[2])
        middle_collar.append(middle_curve[2])
        outside_collar.append(outside_curve[2])

        # 2nd slash division
        pnts1 = intersectLineCurve(radial_pnt, inside_curve[2], inside_curve) # inside collar slash point
        pnts2 = intersectLineCurve(radial_pnt, inside_curve[2], outside_curve) # outside collar slash point
        pnt21, pnt22 = pnts1[0], pnts2[0]
        # find fold result
        length = interpolatedCurveLengthAtPoint(pnt22, outside_interp)
        pnt23 = interpolatedCurvePointAtLength(length - fold_length, outside_interp)
        # store new inside & outside points
        inside_collar.append(pnt21)
        outside_collar.append(pnt23)
        # fold remaining collar points
        pivot = pnt21
        angle = angleOfVectorP(pnt22, radial_pnt, pnt23)
        i = 3
        for curve in inside_curve, middle_curve, outside_curve:
            while i < len(curve):
                slashAndSpread(pivot, angle, curve[i])
                i = i + 1

        # 3rd slash division
        pnt31 = inside_curve[3] # inside collar slash point - shoulder - no need to intersect curve to find point
        pnt32 = outside_curve[3] # outside collar slash point - shoulder - no need to intersect curve to find point
        # find fold result
        length = interpolatedCurveLengthAtPoint(pnt32, outside_interp)
        pnt33 = interpolatedCurvePointAtLength(length - fold_length, outside_interp)
        # store new inside & outside points
        inside_collar.append(pnt31)
        outside_collar.append(pnt33)
        # fold remaining collar points
        pivot = pnt31
        angle = angleOfVectorP(pnt33, radial_pnt, pnt32)
        i = 4
        for curve in inside_curve, middle_curve, outside_curve:
            while i < len(curve):
                slashAndSpread(pivot, angle, curve[i])
                i = i + 1

        # 4th slash division
        pnts1 = intersectLineCurve(radial_pnt, inside_curve[4], inside_curve) # inside collar slash point
        pnts2 = intersectLineCurve(radial_pnt, inside_curve[4], outside_curve) # outside collar slash point
        pnt41, pnt42 = pnts1[0], pnts2[0]
        # find fold result
        length = interpolatedCurveLengthAtPoint(pnt42, outside_interp)
        pnt43 = interpolatedCurvePointAtLength(length - fold_length, outside_interp)
        # store new inside & outside points
        inside_collar.append(pnt41)
        outside_collar.append(pnt43)
        # fold remaining collar points
        pivot = pnt41
        angle = angleOfVectorP(pnt43, radial_pnt, pnt42)
        i = 5
        for curve in inside_curve, middle_curve, outside_curve:
            while i < len(curve):
                slashAndSpread(pivot, angle, curve[i])
                i = i + 1

        # 5th slash division
        pnts1 = intersectLineCurve(radial_pnt, inside_curve[5], inside_curve) # inside collar slash point
        pnts2 = intersectLineCurve(radial_pnt, inside_curve[5], outside_curve) # outside collar slash point
        pnt51, pnt52 = pnts1[0], pnts2[0]
        # find fold result
        length = interpolatedCurveLengthAtPoint(pnt52, outside_interp)
        pnt53 = interpolatedCurvePointAtLength(length - fold_length, outside_interp)
        # store new inside & outside points
        inside_collar.append(pnt51)
        outside_collar.append(pnt53)
        # fold remaining collar points
        pivot = pnt51
        angle = angleOfVectorP(pnt53, radial_pnt, pnt52)
        i = 6
        for curve in inside_curve, middle_curve, outside_curve:
            while i < len(curve):
                slashAndSpread(pivot, angle, curve[i])
                i = i + 1

        end_inside_curve_length = curveLength(inside_collar)
        end_outside_curve_length =  curveLength(outside_collar)

        print 'begin inside & outside length:', begin_inside_curve_length, begin_outside_curve_length
        print 'end inside & outside curve length:', end_inside_curve_length, end_outside_curve_length

        return (inside_collar, outside_collar)




