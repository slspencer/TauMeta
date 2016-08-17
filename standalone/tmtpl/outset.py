#!/usr/bin/python
#
# This file is part of the tmtp (Tau Meta Tau Physica) project.
# For more information, see http://www.taumeta.org/
#
# Copyright (C) 2010 - 2013 Susan Spencer and Steve Conklin
#
# This program is free software:you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version. Attribution must be given in
# all derived works.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see < http://www.gnu.org/licenses/ > .

#
# This file contains methods which mostly act only on points, which may be supplies as tuples of x,y values
# or as an object which contains x and y attributes. In addition, some functions deal with svg paths, in
# text form.
# Methods which access other internals of classes used in the project do not belong in this file
#

import math
import re
import numpy
from math import sin, cos, sqrt, asin
from constants import *

def outsetPath(path, outset_width, outset_angle, closed='true'):
    #accepts array path[] which contains the path of a pattern ['M', p1, 'C', p2, 'L', p3]
    #
    #i = 0
    #outset_path = []
    #Parse path
    #for i, item in path:
    #    if item == 'M':
    #       i = i + 2
    #    elif item == 'C':
    #       pnt1 = item[i - 1]
    #       pnt2 = item[i + 1]
    #       orig_curve = points2List(pnt1, pnt1.outpoint, pnt2.inpoint, pnt2)
    #       split_curve = splitCurveAtLength(orig_curve, curveLength(orig_curve)/2.0)
    #       curve1 = [split_curve[0], split_curve[1], split_curve[2], split_curve[3]]
    #       curve2 = [split_curve[4], split_curve[5], split_curve[6], split_curve[7]]
    #       for crv in curve1, curve2:
    #           outset_crv = outsetCurve(crv, outset_angle, outset_width)
    #           outset_path.append([item, outset_crv]) # append array ['C', [P1, C1, C2, P2]]  
    #       i = i+2
    #    elif item == 'L':
    #       p1, p2 = outsetLine(item[i - 1], item[i + 1],  outset_width, outset_angle)
    #       outset_path.append([item, [p1, p2]]) #append array ['L', [p1, p2]]
    #
    return
    
def outsetLine(P1, P2, outset_width, outset_angle):
    outset_line = []
    angle1 = angleOfLine(P1, P2) + outset_angle
    p1 = polar(P1, outset_width, angle1)
    p2 = polar(P2, outset_width, angle1)
    for item in [p1, p2]:
        outset_line.append(item)      
    return outset_line

def outsetCurve(curve, outset_width, outset_angle):
    #accepts array curve[] which contains cubic bezier [P1, C1, C2, P2], and the angle of outset (ANGLE90 or -ANGLE90)
    outset_curve = []
    P1 = curve[0]
    C1 = curve[1]
    C2 = curve[2]
    C3 = curve[3]
    #get angles
    angle1 = angleOfLine(P1, C1) + outset_angle 
    angle2 = angleOfLine(C2, P2) + outset_angle 
    #get initial outset curve points
    p1 = polar(P1, outset_width, angle1)
    c1_tmp = polar(C1, outset_width, angle1)
    c2_tmp = polar(C2, outset_width, angle2)
    p2 = polar(P2, outset_width, angle2)
    #calculate intersection of control handles
    c1 = intersectLines(p1, c1_tmp, c1_tmp, c2_tmp) #intersect line p1-c1_tmp with line c1_tmp-c2_tmp
    c2 = intersectLines(c1_tmp, c2_tmp, c2_tmp, p2) #intersect line c1_tmp-c2_tmp with line c2_tmp-p2
    for item in [p1, c1, c2, p2]:
        outset_curve.append(item)  
    return outset_curve
    
