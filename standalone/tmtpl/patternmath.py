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
from math import sin, cos, sqrt, asin
from constants import *

    #TODO: write function to draw shortest line from point to line
    #TODO: write function to draw perpendicular line from point to line (with optional parameter to use a given angle)
#---

# most functions that operate on x,y coordinates will accept either an x,y tuple or an object that has x and y attributes
# but internally use the object. Convert input as required
class dPnt():
    '''Dumb point object, has only x and y and xy attributes'''
    def __init__(self, * args):
        # Accept only coordinates as input, either as a tuple or as separate arguments
        if len(args) != 1:
                raise ValueError("dPnt() can accept a single tuple with xy pairs, or an object with x and y attributes")
        if (isinstance(args[0], tuple) and (len(args[0]) == 2)):
            self.x = args[0][0]
            self.y = args[0][1]
        elif (hasattr(args[0], 'x') and hasattr(args[0], 'y')):
            self.x = args[0].x
            self.y = args[0].y
        else:
            raise ValueError("dPnt() can accept a single tuple with xy pairs, or an object with x and y attributes")

    @property
    def xy(self):
        return (self.x, self.y)
    @xy.setter
    def xy(self, value):
        self.x = value[0]
        self.y = value[1]

# ---transforms---

def transformPointXY(x, y, transform=''):
    """
    Apply an SVG transformation string to a 2D point and return the resulting x, y pair
    """
    #
    # -spc- TODO-use numpy to do a proper handling of all transformations in order
    # Postponing this until after the LGM workshop in order not to introduce
    # a new dependency-for now we will only handle a few transformation types
    #
    if transform == '':
        return x, y
    # Every transform in the list ends with a close paren
    transforms = re.split(r'\)', transform)
    for tr in transforms:
        # I don't know why we get an empty string at the end
        if tr == '':
            continue
        tr = tr.strip()
        trparts = re.split(r', |\(', tr)
        trtype = trparts[0].strip()
        if trtype == 'translate':
            #tx=float(trparts[1].strip()) #-- commented out by susan 26/08/11 -- was returning 'invalid literal for float():0 0' error message -- 0, 0 because the transform for 1st pattern is 0, 0
            splitx = re.split("( )", trparts[1].strip())  # added by susan 26/08/11 -- to split apart the two values in tx
            sx = splitx[0].strip() # strip one more time-susan 26/08/11
            tx = float(sx) # substituted sx for trparts[1].strip()-susan 26/08/11
            x = x + tx
            try:
                ty = float(trparts[2].strip())
                y = y + ty
            except IndexError:
                pass
        elif trtype == 'scale':
            sx = float(trparts[1].strip())
            try:
                sy = float(trparts[2].strip())
            except IndexError:
                sy = sx
            x = x * sx
            y = y * sy
        elif trtype == 'skewX':
            sx = float(trparts[1].strip())
            # now do the thing
            #TODO:skewX transform not handled yet
            raise NotImplementedError
        elif trtype == 'skewY':
            sy = float(trparts[1].strip())
            # now do the thing
            #TODO:skewY not handled yet
            raise NotImplementedError
        elif trtype == 'rotate':
            an = float(trparts[1].strip())
            try:
                rx = float(trparts[2].strip())
            except IndexError:
                rx = 0
                ry = 0
            try:
                ry = float(trparts[3].strip())
            except IndexError:
                ry = 0
            # now do the thing
            #TODO:rotate not handled yet
            raise NotImplementedError
        elif trtype == 'matrix':
            ma = float(trparts[1].strip())
            mb = float(trparts[2].strip())
            mc = float(trparts[3].strip())
            md = float(trparts[3].strip())
            me = float(trparts[3].strip())
            mf = float(trparts[3].strip())
            # now do the thing
            #TODO:matrix not handled yet
            raise NotImplementedError
        else:
            #TODO:Unexpected transformation %s' % trtype
            raise ValueError
    return x, y

def scaleAboutPointTransform(x, y, scale):
    """
    Return an SVG transform that scales about a specific x, y coordinate
    """
    sx = scale
    sy = scale
    return "matrix(%f, 0, 0, %f, %f, %f)" % (sx, sy, x-(sx*x), y-(sy*y))

# ---bounding box---

def getBoundingBox(path):
    # TODO:only use information from paths-cuttinLine, seamLine, foldLine, dartLine
    xlist = []
    ylist = []
    #print '=====Entered boundingBox ====='
    #print 'path=', path
    path_tokens = path.split() # split path into pieces, separating at each 'space'
    tok = iter(path_tokens)
    try:
        cmd = tok.next()
        if cmd  != 'M':
            raise ValueError("Unable to handle patches that don't start with an absolute move")
        currentx = float(tok.next())
        currenty = float(tok.next())
        beginx = currentx
        beginy = currenty
        xlist.append(currentx)
        ylist.append(currenty)
    except:
        raise ValueError("Can't handle a path string shorter than 3 tokens")
    while True:
        try:
            cmd = tok.next()
            #print 'processing ', cmd
            if cmd.islower():
                relative = True
            else:
                relative = False
            cmd=cmd.upper()
            if ((cmd == 'M') or (cmd == 'L') or (cmd == 'T')):
                # Note T is really for a Bezier curve, this is a simplification
                x = float(tok.next())
                y = float(tok.next())
                if relative:
                    currentx = currentx + x
                    currenty = currenty + y
                else:
                    currentx = x
                    currenty = y
                xlist.append(currentx)
                ylist.append(currenty)
            elif cmd == 'H':
                x = float(tok.next())
                if relative:
                    currentx = currentx + x
                else:
                    currentx = x
                xlist.append(currentx)
            elif cmd == 'V':
                y = float(tok.next())
                if relative:
                    currenty = currenty + y
                else:
                    currenty = y
                ylist.append(currenty)
            elif ((cmd == 'C') or (cmd == 'S') or (cmd == 'Q')):
                # Curve
                # TODO This could be innacurate, we are only basing on control points not the actual line
                # 'C' uses two control points, 'S' and 'Q' use one
                if cmd == 'C':
                    cpts = 2
                else:
                    cpts = 1
                # control points
                for i in range(0, cpts):
                    #print '  Control Point ',
                    x = float(tok.next())
                    y = float(tok.next())
                    #print 'xy=', x, y
                    if relative:
                        tmpx = currentx + x
                        tmpy = currenty + y
                    else:
                        tmpx = x
                        tmpy = y
                    xlist.append(tmpx)
                    ylist.append(tmpy)
                # final point is the real curve endpoint
                x = float(tok.next())
                y = float(tok.next())
                if relative:
                    currentx = currentx + x
                    currenty = currenty + y
                else:
                    currentx = x
                    currenty = y
                xlist.append(currentx)
                ylist.append(currenty)
            elif cmd == 'A':
                # TODO implement arcs-punt for now
                # See http://www.w3.org/TR/SVG/paths.html#PathElement
                raise ValueError('Arc commands in a path are not currently handled')
            elif cmd == 'Z':
                # No argumants to Z, and no new points
                # but we reset position to the beginning
                currentx = beginx
                currenty = beginy
                continue
            else:
                raise ValueError('Expected a command letter in path')
        except StopIteration:
            #print 'Done'
            # we're done
            break
    xmin = min(xlist)
    ymin = min(ylist)
    xmax = max(xlist)
    ymax = max(ylist)
    return xmin, ymin, xmax, ymax

def mergeBoundingBox(xmin1, ymin1, xmax1, ymax1, xmin2, ymin2, xmax2, ymax2):
    """
    Merge two sets of bounding box values, and return the set.
    if only one of a pair is 'None', return the valid one. If both 'None', return None
    """
    if xmin1 is None:
        rxmin = xmin2
    elif xmin2 is None:
        rxmin = xmin1
    else:
        rxmin = min(xmin1, xmin2)

    if ymin1 is None:
        rymin = ymin2
    elif ymin2 is None:
        rymin = ymin1
    else:
        rymin = min(ymin1, ymin2)

    if xmax1 is None:
        rxmax = xmax2
    elif xmax2 is None:
        rxmax = xmax1
    else:
        rxmax = min(xmax1, xmax2)

    if ymax1 is None:
        rymax = ymax2
    elif ymax2 is None:
        yxmax = ymax1
    else:
        rymax = min(ymax1, ymax2)

    return rxmin, rymin, rxmax, rymax

def transformBoundingBox(xmin, ymin, xmax, ymax, transform):
    """
    Take a set of points representing a bounding box, and
    put them through a supplied transform, returning the result
    """
    if transform == '':
        return xmin, ymin, xmax, ymax
    new_xmin, new_ymin=transformPointXY(xmin, ymin, transform)
    new_xmax, new_ymax=transformPointXY(xmax, ymax, transform)
    return new_xmin, new_ymin, new_xmax, new_ymax

#---functions to calculate points. These functions do not create SVG objects---

# -spc- TODO need this?
def updatePoint(p1, p2):
    '''Accepts p1 and p2 of class Point. Updates p1 with x & y values from p2'''
    #p2 might not have p2.xy,  so create p1.xy with p2.x & p2.y
    if isinstance(p2, list):
        p1.x = p2[0]
        p1.y = p2[1]
    else:
        p2 = dPnt(p2)
        p1.x = p2.x
        p1.y = p2.y
    #TODO: why does .xy = return 'cannot set attribute' error?
    #p1.xy = '(' + str(p2.x) + ', ' + str(p2.y) + ')'
    return

def right(p1, n):
    '''Accepts p1 of class Point, n of type float. Returns coordinate pair to the right of p1 at (p1.x+n,  p1.y)'''
    p1 = dPnt(p1)
    return (p1.x + n, p1.y)

def left(p1, n):
    '''Accepts p1 of class Point, n of type float. Returns coordinate pair to the left of p1 at (p1.x-n,  p1.y)'''
    p1 = dPnt(p1)
    return (p1.x - n, p1.y)

def up(p1, n):
    '''Accepts p1 of class Point, n of type float. Returns coordinate pair above p1 at (p1.x,  p1.y-n)'''
    p1 = dPnt(p1)
    return (p1.x, p1.y - n)

def down(p1, n):
    '''Accepts p1 of class Point, n of type float. Returns p2 of class Point below p1 at (p1.x,  p1.y+n)'''
    p1 = dPnt(p1)
    return (p1.x, p1.y + n)

def symmetricPoint(p1, p2, type='vertical'):
    """
    Accepts p1 and p2 of class Point,  and optional type is either 'vertical' or 'horizontal with default 'vertical'.
    Returns coordinate pair of "mirror image" of p1 relative to p2
    If type=='vertical': pnt is on opposite side of vertical line x=p2.x from p1
    If type=='horizontal': pnt is on opposite side of horizontal line y=p2.y from p1
    """
    p1 = dPnt(p1)
    p2 = dPnt(p2)
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    if (type == 'vertical'):
        return (p2.x + dx, p1.y)
    elif (type == 'horizontal'):
        return (p1.x, p2.y + dy)

def polar(p1, distance, angle):
    '''
    Adapted from http://www.teacherschoice.com.au/maths_library/coordinates/polar_-_rectangular_conversion.htm
    Accepts p1 as type Point, distance as float, angle as float. angle is in radians
    Returns p2 as type Point,  calculated at distance and angle from p1,
    Angles start at position 3:00 and move clockwise due to y increasing downwards on Cairo Canvas
    '''
    p1 = dPnt(p1)
    r = distance
    x = p1.x + (r * cos(angle))
    y = p1.y + (r * sin(angle))
    return (x, y)

def midPoint(p1, p2, n=0.5):
    '''Accepts p1 & p2 of class Point or coordinate pairs, and n where 0 < n < 1. Returns coordinate pair of midpoint b/w p1 & p2'''
    p1 = dPnt(p1)
    p2 = dPnt(p2)
    return((p1.x + p2.x) * n, (p1.y + p2.y) * n)

# ---length---

def distance(p1, p2):
    """Accepts p1 & p2 if class Point or coordinate pairs and returns distance between the points (type float)"""
    p1 = dPnt(p1)
    p2 = dPnt(p2)
    return math.sqrt(((p2.x - p1.x)**2) + ((p2.y - p1.y)**2))

def distanceXY(x1, y1, x2, y2):
    """Accepts four values x1, y1, x2, y2 and returns distance"""
    return math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

#---angles---

def degreeOfAngle(angle):
    return angle * 180.0/math.pi

def angleOfDegree(degree):
    return degree * math.pi/180.0

def angleOfSlope(p1, p2):
    """
    Accepts p1 & p2 of class Point or coordinate pairs
    Returns the angle in radians from p1 to p2
    Identical to function angleOfLine(); keep this function for educational purposes
    """
    p1 = dPnt(p1)
    p2 = dPnt(p2)
    rise = p2.y - p1.y
    run = p2.x - p1.x
    return math.atan2(rise, run)

def slopeOfAngle(radians):
    '''
    Accepts angle (radians)
    Returns the slope as tangent radians
    '''
    #get tangent of radians
    return math.tan(radians)

def angleOfLine(p1, p2):
    """
    Accepts p1 & p2 of class point or coordinate pairs
    Returns the angle in radians of the vector between them\
    """
    p1 = dPnt(p1)
    p2 = dPnt(p2)
    angle = math.atan2(p2.y - p1.y, p2.x - p1.x)
    #get the actual angle, don't return negative angles
    if angle < 0:
        angle = 2*pi + angle
    return angle

def angleOfVector(p1, v, p2):
    """
    Accepts p1,  v,  and p2 of class Point or coordinate pairs
    Returns the angle in radians between the vector v-to-p1 and vector v-to-p2
    """
    #L1=distance(p1, p2)
    #L2=distance(p1, p3)
    #L3=distance(p2, p3)
    #return math.acos((L1**2+L2**2-L3**2)/(2*L1*L2))
    p1 = dPnt(p1)
    p2 = dPnt(p2)
    angle1 = angleOfLine(v, p1)
    angle2 = angleOfLine(v, p2)
    #get the absolute angle
    angle = abs(angle1 - angle2)
    #get the smallest angle of the vector, should not be greater than a straight line
    if angle > pi:
        angle = 2*pi - angle
    return angle

def angleOfChord(chord_width, radius):
    """
    Find the angle between two points given center, radius, chordlength & starting point=2*asin(d/2r)
    Adapted from http://math.stackexchange.com/questions/164541/finding-a-point-having-the-radius-chord-length-and-another-point
    """
    d = chord_width # chord width-usage:could be the dart width
    r = radius # radius-usage:could be the dart length
    d_div_2r = d/(2.0 * r)
    angle = 2 * asin(d_div_2r) # angle-usage:could be the rotation angle used in slashAndSpread to create a dart
    return angle

#---slope---
def slopeOfLine(p1, p2):
    """ Accepts two point objects and returns the slope """
    p1 = dPnt(p1)
    p2 = dPnt(p2)
    if ((p2.x - p1.x) <>  0):
        m = (p2.y - p1.y)/(p2.x - p1.x)
    else:
        print 'Vertical Line'
        m = None
    return m

#---tests for position---
def isRight(pnt1,  pnt2):
    '''returns 1 if pnt2 is to the right of pnt1'''
    pnt1 = dPnt(pnt1)
    pnt2 = dPnt(pnt2)
    right = 0
    if pnt2.x > pnt1.x:
        right = 1
    return right

def isLeft(pnt1,  pnt2):
    '''returns 1 if pnt2 is to the left of pnt1'''
    pnt1 = dPnt(pnt1)
    pnt2 = dPnt(pnt2)
    left = 0
    if pnt2.x < pnt1.x:
        left = 1
    return left

def isAbove(pnt1,  pnt2):
    '''returns 1 if pnt2 is above pnt1'''
    pnt1 = dPnt(pnt1)
    pnt2 = dPnt(pnt2)
    up = 0
    if pnt2.y < pnt1.y:
        up = 1
    return up

def isBelow(pnt1,  pnt2):
    '''returns 1 if pnt2 is below pnt1'''
    pnt1 = dPnt(pnt1)
    pnt2 = dPnt(pnt2)
    down = 0
    if pnt2.y > pnt1.y:
        down = 1
    return down

def lowest(pnt1, pnt2):
    pnt1 = dPnt(pnt1)
    pnt2 = dPnt(pnt2)
    if pnt2.y > pnt1.y:
        return pnt2
    else:
        return pnt1

def lowestP(pnts):
    low_pnt = pnts[0]
    i = 1
    while i < len(pnts):
        low_pnt = lowest(low_pnt, pnts[i])
        i += 1
    return low_pnt

def highest(pnt1, pnt2):
    pnt1 = dPnt(pnt1)
    pnt2 = dPnt(pnt2)
    if pnt2.y < pnt1.y:
        return pnt2
    else:
        return pnt1

def highestP(pnts):
    high_pnt = pnts[0]
    i = 1
    while i < len(pnts):
        high_pnt = highest(high_pnt, pnts[i])
        i += 1
    return high_pnt

def leftmost(pnt1, pnt2):
    pnt1 = dPnt(pnt1)
    pnt2 = dPnt(pnt2)
    if pnt2.x < pnt1.x:
        return pnt2
    else:
        return pnt1

def leftmostP(pnts):
    left_pnt = pnts[0]
    i = 1
    while i < len(pnts):
        left_pnt = leftmost(left_pnt, pnts[i])
        i += 1
    return left_pnt

def rightmost(pnt1, pnt2):
    pnt1 = dPnt(pnt1)
    pnt2 = dPnt(pnt2)
    if pnt2.x > pnt1.x:
        return pnt2
    else:
        return pnt1

def rightmostP(pnts):
    right_pnt = pnts[0]
    i = 1
    while i < len(pnts):
        right_pnt = rightmost(right_pnt, pnts[i])
        i += 1
    return right_pnt

#---lines---#

def onLineAtLength(p1, p2, length, rotation=0):
    """
    Accepts points p1 and p2, distance,  and an optional rotation angle.
    Returns coordinate pair on the line at length measured from p1 towards p2
    If length is negative,  will return a coordinate pair at length measured
    from p1 in opposite direction from p2.
    The result is optionally rotated about the first point by the rotation angle in degrees
    """
    p1 = dPnt(p1)
    p2 = dPnt(p2)
    lineangle = angleOfLine(p1, p2)
    angle = lineangle + (rotation * (math.pi/180))
    x = (length * math.cos(angle)) + p1.x
    y = (length * math.sin(angle)) + p1.y
    return (x,y)

def extendLine(p1, p2, length, rotation=0):
    """
    Accepts two directed points of a line, and a length to extend the line
    Finds point along line at length from p2 in direction p1->p2
    """
    return onLineAtLength(p2, p1, -length)

def onLineAtX(p1, p2, x):
    #on line p1-p2, given x find y
    p1 = dPnt(p1)
    p2 = dPnt(p2)
    if (p1.x == p2.x):# vertical line
        print  'infinite values of y on vertical line'
        return None
    else:
        m = (p2.y - p1.y)/(p2.x - p1.x)
        b = p2.y - (m * p2.x)
        return (x, (m * x) + b)

def onLineAtY(p1, p2, y):
    #on line p1-p2, find x given y
    p1 = dPnt(p1)
    p2 = dPnt(p2)
    if (p1.y == p2.y): #if horizontal line
        raise ValueError('Points form a horizontal line, infinite answers possible')
    elif (p1.x == p2.x):# if vertical line
        return(p1.x, y)
    else:
        m = (p1.y - p2.y)/(p1.x - p2.x)
        b = p2.y - (m * p2.x)
        return ((y - b)/m, y)

def intersectLines(p1, p2, p3, p4):
    """
    Find intersection between two lines. Accepts p1, p2, p3, p4 as class Point. Returns coordinate
    pair at the intersection.
    Intersection does not have to be within the supplied line segments
    """
    p1 = dPnt(p1)
    p2 = dPnt(p2)
    p3 = dPnt(p3)
    p4 = dPnt(p4)
    x, y = 0.0, 0.0
    if (p1.x == p2.x): #if 1st line vertical, use slope of 2nd line
        x = p1.x
        m2 = slopeOfLine(p3, p4)
        b2 = p3.y - (m2 * p3.x)
        y = (m2 * x) + b2
    elif (p3.x == p4.x): #if 2nd line vertical,  use slope of 1st line
        x = p3.x
        m1 = slopeOfLine(p1, p2)
        b1 = p1.y - (m1 * p1.x)
        y = (m1 * x) + b1
    else: #otherwise use ratio of difference between slopes
        m1 = (p2.y - p1.y)/(p2.x - p1.x)
        m2 = (p4.y - p3.y)/(p4.x - p3.x)
        b1 = p1.y - (m1 * p1.x)
        b2 = p3.y - (m2 * p3.x)
        #if (abs(b1-b2) < 0.01) and (m1==m2):
        if (m1 == m2):
            raise ValueError('Parallel lines in intersectLines, no intersection!')
        else:
            x = (b2 - b1)/(m1 - m2)
            y = (m1 * x) + b1 # arbitrary choice, could have used m2 & b2
    return (x, y)

#---curves---
def intersectLineCurve(P1, P2, curve, n=100):
    '''
    Accepts two points of a line P1 & P2, and an array of connected bezier curves [P11, C11, C12, P12, C21, C22, P22, C31, C32, P32, ...], represented as x,y points
    Returns an array points_found[] of x, y coordinates where line intersected with the curve, and tangents_found[] of tangent angle at that point
    '''
    P1 = dPnt(P1)
    P2 = dPnt(P2)
    # get polar equation for line for P1-P2
    # point furthest away from 1st point in curve[] is the fixed point & sets the direction of the angle towards the curve
    #if distance(P1, curve[0]) >= distance(P2, curve[0] ):
    #   fixed_pnt=P1
    #   angle=angleOfLine(P1, P2)
    #else:
    #   fixed_pnt=P2
    #  angle=angleOfLine(P2, P1)
    fixed_pnt = P1
    angle = angleOfLine(P1, P2)
    #print 'P1 =', P1.x, P1.y
    #print 'P2 =', P2.x, P2.y
    #for pnt in curve:
        #print 'curve =', pnt.x, pnt.y
    intersections = 0
    points_found = []
    #tangents_found=[]
    j = 0
    while (j <= len(curve) - 4): # for each bezier curve in curveArray
        intersection_estimate = intersectLines(P1, P2, curve[j], curve[j + 3]) # is there an intersection?
        if (intersection_estimate != None) or (intersection_estimate != ''):
            interpolatedPoints = interpolateCurve(curve[j], curve[j + 1], curve[j + 2], curve[j + 3], n)
            k = 0
            while (k < len(interpolatedPoints) - 1):
                pnt_on_line = polar(fixed_pnt, distance(fixed_pnt, interpolatedPoints[k]), angle)
                # TODO:improve margin of error
                range = distance(interpolatedPoints[k], interpolatedPoints[k + 1])
                length = distance(pnt_on_line, interpolatedPoints[k])
                #print k, 'pntOnCurve', interpolatedPoints[k][0], interpolatedPoints[k][1], 'onLineAtLength', pnt_on_line.x, pnt_on_line.y, distance, range
                if (length <= range):
                    # its close enough!
                    #print 'its close enough!'
                    if k > 1:
                        if (interpolatedPoints[k - 1] not in points_found) and (interpolatedPoints[k - 2] not in points_found):
                            points_found.append(interpolatedPoints[k])
                            #tangents_found.append(angleOfLine(interpolatedPoints[k-1], interpolatedPoints[k+1]))
                            intersections = intersections+1
                    elif k == 1:
                        if (curve[0] not in intersections):
                            points_found.append(interpolatedPoints[1])
                            #tangents_found.append(angleOfLine(curve[0], interpolatedPoints[2]))
                            intersections = intersections+1
                    else:
                        intersections.append(curve[0])
                        #tangents_found.append(angleOfLine(curve[0], curve[1]))
                k = k+1
        j = j + 3 # skip j up to P3 of the current curve to be used as P0 start of next curve
        if intersections == 0:
            print 'no intersections found in intersectLineCurve(', P1.name, P2.name, ' and curve'
    #return points_found, tangents_found
    return points_found

# TODO test this after changes, not used by any patterns
def onCurveAtX(curve, x):
    '''
    Accepts an array 'curve' of bezier curves, returns list of points. Each bezier curve consists of  P0, P1, P2, P3 [eg knot1, controlpoint1, controlpoint2, knot2].
    P3 of one curve is P0 of the next curve. Minimum of one bezier curve in curveArray.
    Accepts value of x to find on curve.
    Returns 1st intersection found
    '''
    intersect_points = []
    xlist, ylist = [], []
    pnt = dPnt(("",""))
    j = 0
    while (j <= len(curve) - 4): # for each bezier curve in curveArray
        interpolatedPoints = interpolateCurve(curve[j], curve[j+1], curve[j+2], curve[j+3], 100)  #interpolate this bezier curve, n=100
        # get min & max for x & y for this bezier curve from its interpolated points
        i = 0
        while (i < len(interpolatedPoints)):
            xlist.append(interpolatedPoints[i][0])
            ylist.append(interpolatedPoints[i][1])
            i += 1
        xmin, ymin, xmax, ymax = min(xlist), min(ylist), max(xlist), max(ylist)
        #print 'xmin, xmax =', xmin, xmax, '...pattern.onCurveAtX()'
        #print 'ymin, ymax =', ymin, ymax, '...pattern.onCurveAtX()'
        #print 'x =', x, '...pattern.onCurveAtX()'
        i = 0
        if ((xmin <= x <= xmax)):
            while (i < len(interpolatedPoints) - 1):
                #if (x >= interpolatedPoints[i][0]) and (x <= interpolatedPoints[i + 1][0]):
                if ((interpolatedPoints[i][0] <= x <= interpolatedPoints[i + 1][0])) or ((interpolatedPoints[i][0] >= x >= interpolatedPoints[i + 1][0])):
                    pnt = dPnt(onLineAtX(interpolatedPoints[i], interpolatedPoints[i + 1], x))
                    intersect_points.append(pnt)
                i += 1
        j = j + 3 # skip j up to P3 of the current curve to be used as P0 start of next curve
    return intersect_points[0] # returns 1st found intersection

def onCurveAtY(curve, y):
    '''
    Accepts an array 'curve' of bezier curves, returns list of points. Each bezier curve consists of  P0, P1, P2, P3 [eg knot1, controlpoint1, controlpoint2, knot2].
    P3 of one curve is P0 of the next curve. Minimum of one bezier curve in curveArray.
    Accepts value of y to find on curve.
    Returns 1st intersection found
    '''
    intersect_points = []
    xlist, ylist = [], []
    pnt = dPnt(("",""))
    j = 0
    while (j <= len(curve) - 4): # for each bezier curve in curveArray
        interpolatedPoints = interpolateCurve(curve[j], curve[j+1], curve[j+2], curve[j+3], 100)  #interpolate this bezier curve, n=100
        # get min & max for x & y for this bezier curve from its interpolated points
        i = 0
        while (i < len(interpolatedPoints)):
            xlist.append(interpolatedPoints[i][0])
            ylist.append(interpolatedPoints[i][1])
            i += 1
        xmin, ymin, xmax, ymax = min(xlist), min(ylist), max(xlist), max(ylist)
        #print 'xmin, xmax =', xmin, xmax, '...pattern.onCurveAtX()'
        #print 'ymin, ymax =', ymin, ymax, '...pattern.onCurveAtX()'
        #print 'x =', x, '...pattern.onCurveAtX()'
        i = 0
        if ((ymin <= y <= ymax)):
            while (i < len(interpolatedPoints) - 1):
                if ((interpolatedPoints[i][1] <= y <= interpolatedPoints[i + 1][1])) or ((interpolatedPoints[i][1] >= y >= interpolatedPoints[i + 1][1])):
                    pnt = dPnt(onLineAtY(interpolatedPoints[i], interpolatedPoints[i + 1], y))
                    intersect_points.append(pnt)
                i += 1
        j = j + 3 # skip j up to P3 of the current curve to be used as P0 start of next curve
    return intersect_points[0] # returns 1st found intersection

def tangentOfCurveAtLine(P1, P2, curve):
    '''
    Accepts P1 & P2 of class Point,  and curve as 4-element array containing bezier curve points P0 C1 C2 P1 of type Point.
    P1 & P2 define a line that intersects the curve.
    Returns the first found intersection point and the angle of the tangent ray at that point directional down the path
    '''
    P1 = dPnt(P1)
    P2 = dPnt(P2)
    # determine whether P1 or P2 is the  furthest away from 1st point in curve[].
    # The point further away is considered the 'fixed point' & use this point to derive the angle of the line towards the curve
    if distance(P1, curve[0]) >= distance(P2, curve[0]):
        fixed_pnt = P1
        angle = angleOfLine(P1, P2)
    else:
        fixed_pnt = P2
        angle = angleOfLine(P2, P1)
    intersections = []
    found = 'false'
    j = 0
    while (j <= len(curve) -4) and (found  != 'true'): # for each bezier curve in curveArray until a point is found
        intersection_estimate = intersectLines(P1, P2, curve[j], curve[j + 3]) # is there an intersection?
        if (intersection_estimate != None) or (intersection_estimate != ''):
            interpolated_points = interpolateCurve(curve[j], curve[j + 1], curve[j + 2], curve[j + 3], 100)  #interpolate this bezier curve, n=100
            k = 0
            while (k < len(interpolated_points) - 1) and (found  != 'true'):
                pnt_on_line = polar(fixed_pnt, distance(fixed_pnt, interpolated_points[k]), angle)
                range = distance(interpolated_points[k], interpolated_points[k + 1]) # TODO:improve margin of error
                if (distance(pnt_on_line, interpolated_points[k]) < range):
                    # its close enough!
                    num = k
                    found = 'true'
                    if k > 1:
                        if (interpolated_points[k - 1] not in intersections) and (interpolated_points[k - 2] not in intersections):
                            intersections.append(interpolated_points[k])
                    elif k == 1:
                        if (interpolated_points[k - 1] not in intersections):
                            intersections.append(interpolated_points[k])
                    else:
                        intersections.append(interpolated_points[k])
                k = k + 1
        j = j + 3 # skip j up to P3 of the current curve to be used as P0 start of next curve
    if (found == 'true'):
        tangent_angle = angleOfLine(interpolated_points[num - 1], interpolated_points[num + 1])
    else:
        tangent_angle = None
    return interpolated_points[num], tangent_angle

def curveLength(curve, n = 100):
    #FIXME: this length should be calculated with math formulas
    '''
    Accepts curve array with a minimum of four Point objects P0, P1, P2, P3 (knot1, controlpoint1, controlpoint2, knot2).
    Each curve after the first will use P3 from the previous curve as it's P0, and use it's own P1, P2, P3
    n is the number to subdivide each curve for calculating the interpolated points and curve length.
    Adapted from http://www.planetclegg.com/projects/WarpingTextToSplines.html
    '''
    curveLength = 0.0
    j = 0
    while (j <= len(curve) - 4): # for each curve, get segmentLength & add to curveLength
        interpolatedPoints = interpolateCurve(curve[j], curve[j + 1], curve[j + 2], curve[j + 3], n)  #interpolate this curve
        # add up lengths between the interpolated points
        segmentLength = 0.0
        i = 1
        while (i <= n):
                segmentLength = segmentLength + distance(interpolatedPoints[i - 1], interpolatedPoints[i]) #length from previous point to current point
                i = i + 1
        curveLength = curveLength + segmentLength
        j = j + 3 # skip j up to P3 of the current curve to be used as P0 start of next curve
    return curveLength

def curveLengthAtPoint(curve, pnt, n=100):
    found = 0
    curve_length = 0.0
    j = 0
    while (j <= len(curve) - 4) and (found == 0): # for each curve, get segmentLength & add to curveLength
        interpolated_points = interpolateCurve(curve[j], curve[j + 1], curve[j + 2], curve[j + 3], n)  #interpolate this curve
        # add up lengths between the interpolated points
        current_curve_length, found = interpolatedCurveLengthAtPoint(interpolated_points, pnt, found)
        curve_length += current_curve_length
        j = j + 3 # skip j up to P3 of the current curve to be used as P0 start of next curve
    if curve_length == 0.0:
        print 'Point not found in curveLengthAtPoint'
    return curve_length

def interpolatedCurveLengthAtPoint(interpolatedPoints, pnt, found=0):
    # add up lengths between the interpolated points
    segment_length = 0.0
    i = 1
    while (i < len(interpolatedPoints)) and (found==0):
        current_length = distance(interpolatedPoints[i - 1], interpolatedPoints[i]) #length from previous point to current point
        segment_length = segment_length + current_length
        if (pnt == interpolatedPoints[i]) or (distance(pnt, interpolatedPoints[i]) <= current_length):
            found = 1
        i = i + 1
    return segment_length, found

def curvePointAtLength(curve, length, n=100):
    '''
    Accepts an array of curve points and length
    Returns point found on curve at length
    '''
    p1 = dPnt(("",""))
    j = 0
    while (j <= len(curve) - 4) and (p1.x == ""): # for each curve,  find pnt
        interpolated_points = interpolateCurve(curve[j], curve[j + 1], curve[j + 2], curve[j + 3], n)
        p1 = dPnt(interpolatedCurvePointAtLength(interpolated_points, length))
        j = j + 3 # skip j up to P3 of the current curve to be used as P0 start of next curve
    return p1

def interpolatedCurvePointAtLength(interpolatedPoints, length):
    p1 = dPnt(("",""))
    i = 1
    segmentLength = 0
    while (i <  len(interpolatedPoints)) and (p1.x == ''):
        segmentLength += distance(interpolatedPoints[i - 1], interpolatedPoints[i]) #length from previous point to current point
        if segmentLength >= length:
            p1 = dPnt((interpolatedPoints[i][0], interpolatedPoints[i][1]))
        i += 1
    return p1

def interpolateCurveList(curve, t=100):
    '''curve can have multiple cubic curves P0 C1 C2 P1 C1 C2 P3...'''
    interpolatedPoints = []
    j = 0
    while (j <= len(curve) - 4): #interpolate each cubic curve
        temp_list = interpolateCurve(curve[j], curve[j + 1], curve[j + 2], curve[j + 3], t)
        for coords in temp_list:
            interpolatedPoints.append(coords)
        j = j + 3
    return interpolatedPoints

def interpolateCurve(P0, C1, C2, P1, t=100):
    '''
    Accepts curve points P0, C1, C2, P1 & number of interpolations t
    Returns array of x, y coordinate pairs.
    Adapted from http://www.planetclegg.com/projects/WarpingTextToSplines.htm
    '''
    P0 = dPnt(P0)
    C1 = dPnt(C1)
    C2 = dPnt(C2)
    P1 = dPnt(P1)
    # calculate coefficients for two knot points P0 & P1 ;     C1 & C2 are the controlpoints.
    # x coefficients
    A = P1.x - (3 * C2.x) + (3 * C1.x) - P0.x
    B = (3 * C2.x) - (6 * C1.x) + (3 * P0.x)
    C = (3 * C1.x) - (3 * P0.x)
    D = P0.x
    # y coefficients
    E = P1.y - (3 * C2.y) + (3 * C1.y) - P0.y
    F = (3 * C2.y) - (6 * C1.y) + (3 * P0.y)
    G = (3 * C1.y) - (3 * P0.y)
    H = P0.y
    # calculate interpolated points
    interpolatedPoints = []
    maxPoint = float(t)
    i = 0
    while (i <= t):
            j = i/maxPoint # j can't be an integer, i/t is an integer..always 0.
            x = A * (j ** 3) + B * (j ** 2) + (C * j) + D
            y = E * (j ** 3) + F * (j ** 2) + (G * j) + H
            interpolatedPoints.append((x, y))
            i = i + 1
    return interpolatedPoints

def splitCurveAtLength(curve, length):
    '''Accepts a point on a curve, and a curve list with points P0 C1 C2 P1.
    Returns curve list with P0, split.c1, split.c2, split_pnt, new.c11, new.c12, P1'''
    # find split point
    interpolated_points = interpolateCurve(curve[0], curve[1], curve[2], curve[3])
    split_pnt = interpolatedCurvePointAtLength(interpolated_points, length) # split neck curve at this point
    # find tangent at split point
    pnt1 = interpolatedCurvePointAtLength(interpolated_points, length - 0.25*CM) # arbitrary .25cm - good enough for this application?
    pnt2 = interpolatedCurvePointAtLength(interpolated_points, length + 0.25*CM)
    forward_tangent_angle = angleOfLine(pnt1,  pnt2)
    backward_tangent_angle = angleOfLine(pnt2,  pnt1)
    # neck control points
    # b/w curve[0] and split_pnt
    length = distance(curve[0], split_pnt) / 3.0
    split_pnt.c1 = polar(curve[0], length, angleOfLine(curve[0], curve[1])) # preserve angle b/w P0 & original 1st control point
    split_pnt.c2 = polar(split_pnt, length, backward_tangent_angle)
    # b/w split_pnt and curve[3]
    curve3 = dPnt(curve[3])
    length = distance(split_pnt, curve3)/3.0
    curve3.c1 = polar(split_pnt, length, forward_tangent_angle)
    curve3.c2 = polar(curve3, length, angleOfLine(curve3, curve[2])) # preserve angle b/w original 2nd control point & P1
    new_curve = []
    new_curve.append(curve[0])
    new_curve.append(split_pnt.c1)
    new_curve.append(split_pnt.c2)
    new_curve.append(split_pnt)
    new_curve.append(curve3.c1)
    new_curve.append(curve3.c2)
    new_curve.append(curve3)
    return new_curve

def splitCurveAtPoint(curve, split_pnt):
    #FIXME: Replace this function. This is not mathematically accurate. It's good enough for now...
    split_pnt = dPnt(split_pnt)
    length = curveLengthAtPoint(curve, split_pnt)
    interpolated_points = interpolateCurve(curve[0], curve[1], curve[2], curve[3])
    # find tangent at split point
    pnt1 = dPnt(interpolatedCurvePointAtLength(interpolated_points, length - 5)) # arbitrary 5px - good enough for this application?
    pnt2 = dPnt(interpolatedCurvePointAtLength(interpolated_points, length + 5))
    forward_tangent_angle = angleOfLine(pnt1, pnt2)
    backward_tangent_angle = angleOfLine(pnt2, pnt1)

    # b/w curve[0] and split_pnt
    length = distance(curve[0], split_pnt) / 3.33
    p0 = dPnt(curve[0])
    c1 = polar(curve[0], length, angleOfLine(curve[0], curve[1])) # preserve angle b/w P0 & original 1st control point
    c2 = polar(split_pnt, length, backward_tangent_angle)
    p1 = dPnt(split_pnt)

    # b/w split_pnt and curve[3]
    length = distance(split_pnt, curve[3])/3.33
    c3 = polar(split_pnt, length, forward_tangent_angle)
    c4 = polar(curve[3], length, angleOfLine(curve[3], curve[2])) # preserve angle b/w original 2nd control point & P1
    p2 = dPnt(curve[3])
    new_curve = []
    new_curve.append(p0)
    new_curve.append(c1)
    new_curve.append(c2)
    new_curve.append(p1)
    new_curve.append(c3)
    new_curve.append(c4)
    new_curve.append(p2)
    return new_curve


# --- intersections-circles---

# TODO test this after changes - No current pattern uses this
def intersectCircles(C1, r1, C2, r2):
    """
    Accepts C1, r1, C2, r2 where C1 & C2 are point objects for the center of each circle,  and r1 & r2 are the radius of each circle
    Returns an array P which holds objects of class Point for each intersection
    """
    C1 = dPnt(C1)
    C2 = dPnt(C2)
    x0, y0 = C1.x, C1.y
    x1, y1 = C2.x, C2.y
    d = distanceXY(x0, y0, x1, y1) # distance b/w circle centers
    dx, dy = (x1 - x0), (y1 - y0) # negate y b/c canvas increases top to bottom
    P = []
    if (d == 0):
        #intersections=0
        print 'center of both circles are the same...intersections.intersectCircles()'
        print 'C1 =',  C1.x,  C1.y,  'radius1 =',  r1
        print 'C2 =',  C2.x,  C2.y,  'radius1 =', r2
    elif (d < abs(r1 - r2)):
        #intersections=0
        print 'one circle is within the other ...intersections.intersectCircles()'
        print 'd =',  d
        print 'r1 - r2 =', (r1-r2)
        print 'd <  abs(r1 - r2) ?',  (d < abs(r1-r2))
        print 'C1 =',  C1.x,  C1.y,  'radius1 =',  r1
        print 'C2 =',  C2.x,  C2.y,  'radius1 =', r2
    elif (d > (r1 + r2)):
        #intersections=0
        print 'circles do not intersect ...intersections.intersectCircles()'
        print 'd =',  d
        print 'r1 + r2 =', (r1+r2)
        print 'd >  abs(r1 + r2) ?',  (d > abs(r1+r2))
        print 'C1 =',  C1.x,  C1.y,  'radius1 =',  r1
        print 'C2 =',  C2.x,  C2.y,  'radius1 =', r2
        # TODO:possible kluge -check if this is acceptable using a small margin of error between r1 & r2 (2*CM)?:
        #r2=d-r1
    else:
        #intersections=2 or intersections=1
        a = ((r1 * r1) - (r2 * r2) + (d * d)) / (2.0 * d)
        x2 = x0 + (dx * a / d)
        y2 = y0 + (dy * a / d)
        h = math.sqrt((r1 * r1) - (a * a))
        rx = -dy * (h / d)
        ry = dx * (h / d)
        X1 = x2 + rx
        Y1 = y2 + ry
        X2 = x2 - rx
        Y2 = y2 - ry
        P.append(dPnt((X1, Y1)))
        P.append(dPnt((X2, Y2)))
    return P

def onCircleAtX(C, r, x):
    """
    Finds points on circle where p.x=x
    Accepts C as an object of class Point or xy coords for the center of the circle,
    r as the radius,  and x to find the points on the circle
    Returns an array P which holds objects of class dPnt for each intersection
    """
    C = dPnt(C)
    P = []
    if abs(x - C.x) > r:
        print 'x is outside radius of circle in intersections.onCircleAtX()'
    else:
        translated_x = x - C.x # center of translated circle is (0, 0) as translated_x is the difference b/w C.x & x
        translated_y1 = abs(math.sqrt(r**2 - translated_x**2))
        translated_y2 = -(translated_y1)
        y1 = translated_y1 + C.y # translate back to C.y
        y2 = translated_y2 + C.y # translate back to C.y
        P.append(dPnt((x, y1)))
        P.append(dPnt((x, y2)))
    return P

def onCircleAtY(C, r, y):
    """
    Finds points one or two points on circle where P.y=y
    Accepts C of class Point or coords as circle center,  r of type float as radius,  and y of type float)
    Returns an array P containg intersections of class dPnt
    Based on paulbourke.net/geometry/sphereline/sphere_line_intersection.py, written in Python 3.2 by Campbell Barton
    """
    C = dPnt(C)
    if abs(y - C.y) > r:
        print 'y is outside radius in onCircleAtY() -- no intersection'
        return
    else:
        translated_y = y - C.y
        translated_x1 = abs(math.sqrt(r**2 - translated_y**2))
        translated_x2 = -translated_x1
        x1 = translated_x1 + C.x
        x2 = translated_x2 + C.x
        P = []
        P.append(dPnt((x1, y)))
        P.append(dPnt((x2, y)))
    return P

def intersectLineCircle(C, r, P1, P2):
    """
    Finds intersection of a line segment and a circle.
    Accepts circle center point object C, radius r, and two line point objects P1 & P2
    Returns an object P with number of intersection points, and up to two coordinate pairs as P.intersections, P.p1, P.p2
    Based on paulbourke.net/geometry/sphereline/sphere_line_intersection.py, written in Python 3.2 by Campbell Barton
    """
    C = dPnt(C)
    P1 = dPnt(P1)
    P2 = dPnt(P2)

    P, p1, p2 = dPnt(("","")), dPnt(("","")), dPnt(("",""))

    if P1.x == P2.x: #vertical line
        if abs(P1.x - C.x) > r:
            print 'no intersections for vertical line P1', P1.name, P1.x, P1.y, ',  P2', P2.name, P2.x, P2.y, ', and Circle', C.name, C.x, C.y, ',  radius', r
            return None
        else:
            p1.x = P1.x
            p2.x = P1.x
            p1.y = C.y + sqrt(r**2 - (P1.x - C.x)**2)
            p2.y = C.y - sqrt(r**2 - (P1.x - C.x)**2)
    elif P1.y==P2.y: #horizontal line
        if abs(P1.y-C.y) > r:
            print 'no intersections for horizontal line P1', P1.name, P1.x, P1.y, ',  P2', P2.name, P2.x, P2.y, ', and Circle', C.name, C.x, C.y, ',  radius', r
            return None
        else:
            p1.y = P1.y
            p2.y = P1.y
            p1.x = C.x + sqrt(r**2 - (P1.y - C.y)**2)
            p2.x = C.x - sqrt(r**2 - (P1.y - C.y)**2)
    else:
        a = (P2.x - P1.x)**2 + (P2.y - P1.y)**2
        b = 2.0 * ((P2.x - P1.x) * (P1.x - C.x)) + ((P2.y - P1.y) * (P1.y - C.y))
        c = C.x**2 + C.y**2 + P1.x**2 + P1.y**2 - (2.0 * (C.x * P1.x + C.y * P1.y)) - r**2
        i = b**2 - 4.0 * a * c
        if i < 0.0:
            print 'no intersections b/w line', P1.name, P1.x, P1.y, '--', P2.name, P2.x, P2.y, 'and Circle', C.name, C.x, C.y, 'with radius', r
            return None
        elif i == 0.0:
            # one intersection
            mu = -b/(2.0 * a)
            p1.x, p1.y = P1.x + mu * (P2.x - P1.x), P1.y + mu * (P2.y - P1.y)
        elif i > 0.0:
            # two intersections
            # first intersection
            mu1 = (-b + math.sqrt(i)) / (2.0*a)
            p1.x, p1.y = P1.x + mu1 * (P2.x - P1.x), P1.y + mu1 * (P2.y - P1.y)
            # second intersection
            mu2 = (-b - math.sqrt(i)) / (2.0*a)
            p2.x, p2.y = P1.x + mu2 * (P2.x - P1.x), P1.y + mu2 * (P2.y - P1.y)
    P.p1 = p1
    P.p2 = p2
    return P

def intersectChordCircle(C, r, P, chord_length):
    ''' Accepts center of circle, radius of circle, a point on the circle, and chord length.  Returns a list of two points on the circle at chord_length distance away from original point'''
    C = dPnt(C)
    P = dPnt(P)
    d = chord_length
    # point on circle given chordlength & starting point=2*asin(d/2r)
    d_div_2r = d / (2.0 * r)
    angle = 2 * asin(d_div_2r)
    P = []
    P.append(polar(C, r, angle))
    P.append(polar(C, r, - angle))
    return P

def onCircleTangentFromOutsidePoint(C, r, P):
  '''
  Accepts C center of circle, r radius, and P point outside of circle.
  Returns two points where lines to point P are tangent to circle
  '''
  d = distance(C, P)
  l = sqrt(d*d - r*r)
  return intersectCircles(C, r, P, l)

#---vectors and rays---

def onRayAtX(P, angle, x):
    '''
    Accepts point P and angle of line.
    Returns point along ray at x
    '''
    #convert degrees to slope
    m = slopeOfAngle(angle)
    #solve for y
    #(P.y - y)/(P.x - x) = m
    y = P.y - m * (P.x - x)
    return (x, y)

def onRayAtY(P, angle, y):
    '''
    Accepts point P and angle of line.
    Returns point along ray at y
    '''
    #convert degrees to slope
    m = slopeOfAngle(angle)
    #solve for x
    #(P.y - y)/(P.x - x) = m
    x = P.x - (P.y - y)/m
    return (x, y)

def intersectLineRay(P1, P2, R1, angle):
    '''
    Accepts two points defining a line, and a point and angle defining a ray.
    Returns point where they intersect.
    '''
    #define a line R1-R2 by finding point R2 along ray 1 inch (arbitary) from R1
    R2 = polar(R1, 1*IN,  angle)
    return intersectLines(P1, P2, R1, R2)

#---adjust Curves---#
def adjustCurves(curve, P0, C1, C2, P1):
    '''
    Accepts 2 curves, adjusts control handle length until curve2 matches curve1
    Returns new curve
    '''
    #check sleeve cap length
    orig_length = curveLength(curve, n=200)
    new_curve = points2List(P0, C1, C2, P1)
    new_curve_length = curveLength(new_curve, n=200)
    diff = new_curve_length - orig_length
    length1 = distance(P0, C1)
    length2 = distance(P1, C2)
    angle1 = angleOfLine(P0, C1)
    angle2 = angleOfLine(P1, C2)
    if diff > 1:
        length1 = length1/2.0 #reduce handle length by 50%
        length2 = length2/2.0 #reduce handle length by 50%
        updatePoint(C1, polar(P0, length1, angle1))
        updatePoint(C2, polar(P1, length2, angle2))
        adjustCurves(curve, P0, C1, C2, P1)
    elif diff < -1:
        length1 = 1.5 * length1 #increase handle length by 50%
        length2 = 1.5 * length2 #increase handle length by 50%
        updatePoint(C1, polar(P0, length1, angle1))
        updatePoint(C2, polar(P1, length2, angle2))
        adjustCurves(curve, P0, C1, C2, P1)

# TODO Darts need reworking
#---darts---
def waistDart(parent, dart_width, dart_length, length, waist_curve, dart_angle=ANGLE90):
    '''Accepts dart_width, dart_length, length, and curve  list from center to side with points P0 C1 C2 P1, and angle of dart in radians.
    Default angle is pi/4 radians (90 degrees).
    If waist does not have a curve, create waist_curve list with control points at 1/3 & 2/3 distance on line from center to side.
    Returns dart_apex, curve1 list from center to dart with points P0 C11 C12 P1, and curve2 list from dart to side with points P2 C31 C32 P3.
    Side point is rotated/moved out to accommodate dart.'''
    # see http://math.stackexchange.com/questions/164541/finding-a-point-having-the-radius-chord-length-and-another-point
    # find the angle between two points given center, radius, chordlength & starting point=2*asin(d/2r)
    d = dart_width # chord length
    r = dart_length # radius
    d_div_2r = d / (2.0 * r)
    rotation_angle = 2 * asin(d_div_2r)
    # split neck curve at length-returns curve with P0 C11 C12 P1 C21 C22 P2
    split_curve = splitCurveAtLength(length, waist_curve)
    #dart_apex=dPnt(parent, parent.name+'dart_apex', polar(split_curve[3], dart_length, angleOfLine(split_curve[3], split_curve[2])+ANGLE90))
    # TODO:test for direction of dart-plus or minus 90 degrees from the angle of the tangent at the dart...
    # ...the angle of line from 2nd control point (split_curve[2]) to the split point (split_curve[3])
    dart_apex = polar(split_curve[3], dart_length, angleOfLine(split_curve[3], split_curve[2]) + dart_angle)
    # separate split_curve into inside_curve1 & outside_curve
    inside_curve = []
    i = 0
    while i <= 3:
        inside_curve.append(dPnt(split_curve[i]))
        i = i+1
    outside_curve = []
    i = 3
    while i <= 6:
        outside_curve.append(dPnt(split_curve[i ]))
        i = i+1
    # rotate outside leg & side point (outside_curve) relative to the dart_apex, creating the dart
    slashAndSpread(dart_apex, rotation_angle, outside_curve[0], outside_curve[1], outside_curve[2], outside_curve[3])
    return dart_apex, inside_curve, outside_curve

def neckDart(parent, dart_width, dart_length, length, neck_curve):
    '''Accepts dart_width, dart_length, length, and curve list of neck from center to shoulder with points P0 C1 C2 P1.
    Moves/rotates nape point to accomodate dart.
    Returns dart_apex, curve1 list from center to dart with points P0 C11 C12 P1, curve2 list from dart to shoulder with points P2 C31 C32 P3.
    Dart is formed from P1 to dart_apex to P2'''
    # split neck curve at length
    split_curve = splitCurveAtLength(length, neck_curve)
    # see http://math.stackexchange.com/questions/164541/finding-a-point-having-the-radius-chord-length-and-another-point
    # find the angle between two points given center, radius, chordlength & starting point=2*asin(d/2r)
    #d=dart_width # chord length
    #r=dart_length # radius
    #d_div_2r=d/(2.0*r)
    #rotation_angle=2*asin(d_div_2r)

    rotation_angle = angleFromChord(dart_width, dart_length)
    #print('rotation_angle =',  rotation_angle)
    dart_apex = dPnt(parent, 'dart_apex', polar(split_curve[3], dart_length, angleOfLine(split_curve[3], split_curve[2]) + ANGLE90))
    #print('dart_apex =',  dart_apex)

    # separate split_curve into curve1 & curve2
    curve1 = []
    i = 0
    while i <= 3:
        p#rint('i = ',  i)
        #print('split_curve[',  i,  '] =',  split_curve[i].x,  split_curve[i].y)
        curve1.append(dPnt(split_curve[i]))
        #print('curve1[',  i,  '] =',  curve1[i].x,  curve1[i].y)
        i += 1

    curve2 = []
    i = 3
    while i <= 6:
        p#rint('i = ',  i)
        #print('split_curve[',  i,  '] =',  split_curve[i].x,  split_curve[i].y)
        curve2.append(dPnt(split_curve[i]))
        #print('curve2[', i, '] =',  curve2[i].x,  curve2[i].y)
        i += 1
    # rotate curve1 relative to the dart_apex, creating the dart
    slashAndSpread(dart_apex, rotation_angle, curve1[0], curve1[1], curve1[2], curve1[3])
    return dart_apex, curve1, curve2

def foldDart(parent, dart, inside_pnt):
    DART_LENGTH = distance(dart, dart.o)
    DART_HALF_ANGLE = abs(angleOfVector(dart.o, dart, dart.i)) / 2.0
    O_ANGLE = angleOfLine(dart, dart.o)
    I_ANGLE = angleOfLine(dart, dart.i)
    # determine which direction the dart will be folded
    if I_ANGLE <= O_ANGLE:
        FOLD_ANGLE = I_ANGLE - DART_HALF_ANGLE
    else:
        FOLD_ANGLE = I_ANGLE + DART_HALF_ANGLE
    # find intersection of fold & armscye b/w bd2.i & inside_pnt
    # TODO:use intersectLineCurve()
    temp_pnt = dPnt(polar(dart, DART_LENGTH, FOLD_ANGLE))
    fold_pnt = dPnt(intersectLines(dart.i, inside_pnt, dart, temp_pnt))
    # dart midpoint at seamline
    temp_pnt = dPnt(midPoint(dart.i, dart.o))
    mid_pnt = dPnt(onLineAtLength(dart, temp_pnt, distance(dart, fold_pnt)))
    if hasattr(dart, 'm'):
        updatePoint(dart.m, mid_pnt)
    else:
        dart.m = dPnt(parent, dart.name+'.m', mid_pnt)
    # dart outside leg at cuttingline
    #temp_pnt=onLineAtLength(dart.o, dart, -SEAM_ALLOWANCE)
    temp_pnt = dPnt(polar(dart, distance(dart, dart.o) + SEAM_ALLOWANCE, angleOfLine(dart, dart.o)))
    if hasattr(dart, 'oc'):
        updatePoint(dart.oc, temp_pnt)
    else:
        dart.oc = dPnt(parent, dart.name + '.oc', temp_pnt)
    # dart inside leg at cuttingline
    temp_pnt = dPnt(onLineAtLength(dart.i, dart, -SEAM_ALLOWANCE))
    if hasattr(dart, 'ic'):
        updatePoint(dart.ic, temp_pnt)
    else:
        dart.ic = dPnt(parent, dart.name + '.ic', temp_pnt)
    #create or update dart.angles
    dart.angle = angleOfVector(dart.i, dart, dart.o)

    return

def foldDart2(dart, inside_pnt):
    '''
	Accepts dart, and the nearest point in the direction dart will be folded
    Returns dart.m, dart.oc, dart.ic, dart.angle
	dart.m = middle dart leg at seamline (to be included in seamline path)
	dart.oc = inside dart leg at cuttingline (to be included in dartline path)
	dart.oc = outside dart leg at cuttingline (to be included in dartline path)
    '''
    DART_LENGTH = distance(dart, dart.o)
    DART_HALF_ANGLE = abs(angleOfVector(dart.o, dart, dart.i)) / 2.0
    O_ANGLE = angleOfLine(dart, dart.o)
    I_ANGLE = angleOfLine(dart, dart.i)
    #determine which direction the dart will be folded
    if I_ANGLE <= O_ANGLE:
        FOLD_ANGLE = I_ANGLE - DART_HALF_ANGLE
    else:
        FOLD_ANGLE = I_ANGLE + DART_HALF_ANGLE
    #TODO:find intersection of fold & armscye b/w bd2.i & inside_pnt
    #TODO:use intersectLineCurve()
    temp_pnt = dPnt(polar(dart, DART_LENGTH, FOLD_ANGLE))
    fold_pnt = dPnt(intersectLines(dart.i, inside_pnt, dart, temp_pnt))
    temp_pnt = dPnt(midPoint(dart.i, dart.o))
    dart.m = dPnt(onLineAtLength(dart, temp_pnt, distance(dart, fold_pnt))) #dart midpoint at seamline
    dart.oc = dPnt(polar(dart, distance(dart, dart.o) + SEAM_ALLOWANCE, angleOfLine(dart, dart.o))) #dart outside leg at cuttingline
    dart.ic = dPnt(onLineAtLength(dart.i, dart, -SEAM_ALLOWANCE)) #dart inside leg at cuttingline
    #create or update dart.angles
    dart.angle = angleOfVector(dart.i, dart, dart.o)

    return

def adjustDartLength(p1, dart, p2, extension=1/3.0):
    """
    Finds optimum leg length to smooth the curve from p1 to p2
    Accepts p1 of class Point or coords,  dart of class Dart,  and p2 of class Point or coords
    dart.i & dart.o are updated to new longer point on dart legs
    Default extension is 1/3 distance from orig dart length to the line
    drawn between p1 & p2 after the dart is created
    """
    #TODO: define class Dart
    #rotate point 'p1' to p1_new where it would lie if dart were closed
    rotation_angle = angleOfVector(dart.i, dart, dart.o)
    p1_new = dPnt(polar(dart, distance(dart, p1), angleOfLine(dart, p1) + rotation_angle))
    ######slashAndSpread(dart, rotation_angle, p1_new)
    #find intersection of dart leg and line p1_new to p2
    p3 = intersectLines(dart, dart.i, p1_new, p2)
    #new dart length at 1/3 distance from dart.i to p3
    new_dart_length = distance(dart, dart.i) + distance(dart.i, p3) * extension
    #update dart.i & dart.o
    p4 = dPnt(onLineAtLength(dart, dart.i, new_dart_length))
    p5 = dPnt(onLineAtLength(dart, dart.o, new_dart_length))
    (dart.i.x, dart.i.y) = (p4.x, p4.y)
    (dart.o.x, dart.o.y) = (p5.x, p5.y)
    return

# ---control points---
def points2List(*args):
    points = []
    for arg in args:
        points.append(arg)
    return points

def controlPoints(name, knots):
    #TODO:remove name from args
    k_num = len(knots)-1 # last iterator for n knots 0..n-1
    c_num = k_num-1 # last iterator for n-1 curve segments 0..n-2
    c1 = [] # first control points c1[0..c_num]
    c2 = [] # second control points c2[0..c_num]
    i = 1
    while (i <= c_num):
        # each loop produces c2[previous] and c1[current]
        # special cases:get c1[0] in 1st loop & c2[c_num] in last loop
        # previous segment is segment b/w previous knot & current knot
        # current segment is segment b/w current knot & next knot
        # start with i=1 because can't start processing with knot[0] b/c it doesn't have a previous knot
        previous = (i - 1)
        current = i
        next = (i + 1)
        last_knot = k_num
        last_segment = c_num
        # process previous segment's c2
        angle = angleOfLine(knots[next], knots[previous])
        length = distance(knots[current], knots[previous]) / 3.0
        pnt = polar(knots[current], length, angle)
        c2.append(pnt) # c2[previous]
        if (current == 1):
            # process 1st segment's c1
            angle = angleOfLine(knots[0], c2[0])
            pnt = polar(knots[0], length, angle)
            c1.append(pnt)
        # process current segment's c1
        angle = angleOfLine(knots[previous], knots[next])
        length = distance(knots[current], knots[next]) / 3.0
        pnt=polar(knots[current], length, angle)
        c1.append(pnt) # c1[current]
        if (current == c_num):
            # process last segment's c2
            angle = angleOfLine(knots[last_knot], c1[last_segment])
            pnt = polar(knots[last_knot], length, angle)
            c2.append(pnt) # c2[last_segment]
        i = i + 1
    return c1, c2

# ----------------...Connect 2 objects together using 2 points each...------------------------------

def connectObjects(connector_pnts, old_pnts):
        # connector_pnts[0] and old_pnts[0] will connect together
        # connector_pnts[1] and old_pnts[1] will connect together
        # connector_pnts[1] is counterclockwise from connector_pnts[0] on object which doesn't move
        # old_pnts[] contains all of the points of the object to be moved in order clockwise, starting with old_pnts[0]
        t_pnts = [] # translated points. 1st step.
        r_pnts = [] # translated points that are rotated. 2nd step.
        # translate so that old_pnts[0] will connect with connector_pnts[0]
        (dx, dy) = (connector_pnts[0].x - old_pnts[0].x), (connector_pnts[0].y - old_pnts[0].y)
        i = 0
        for o in old_pnts:
            # translate all points in old_pnts[]
            t_pnts.append(dPnt(("","")))
            t_pnts[i].x, t_pnts[i].y = o.x + dx, o.y + dy
            i = i + 1
        angle1 = angleOfLine(connector_pnts[0], connector_pnts[1])
        angle2 = angleOfLine(connector_pnts[0], t_pnts[1])
        rotation_angle = angle2 - angle1 # subtract this angle from each angle of 2nd object's points towards connector0
        i = 1 # don't rotate the 1st translated point, it should now be equal to connector0
        r_pnts.append(t_pnts[0])
        for t_pnt in t_pnts:
            if  (i != len(t_pnts)):
                length = distance(connector_pnts[0], t_pnts[i])
                translated_angle = angleOfLine(connector_pnts[0], t_pnts[i])
                r_angle = translated_angle - rotation_angle
                r_pnts.append(dPnt(("","")))
                r_pnts[i] = polar(connector_pnts[0], length, r_angle)
                i = i + 1
        return r_pnts

def slashAndSpread(pivot, angle, *args):
        """
        Accepts pivot point, angle of rotation, and the points to be rotated.
        Accepts positive & negative angles.
        """
        if (angle == 0.0):
            print "Angle = 0 -- Slash and Spread not possible"
        else:
            list = []
            for arg in args:
                list.append(arg)
            i = 0
            while (i < len(list)):
                pnt = list[i]
                length = distance(pivot, pnt)
                rotated_pnt = dPnt(polar(pivot, length, angleOfLine(pivot, pnt) + angle)) # if angle > 0 spread clockwise. if angle < 0 spread counterclockwise
                pnt.x = rotated_pnt.x
                pnt.y = rotated_pnt.y
                #pnt.xy = "(" + str(rotated_pnt.x) + ', ' + str(rotated_pnt.y) + ')'
                i = i + 1
        return

#---append points,  lines and curves to paths---

def moveP(pathSVG, point, transform=''):
    """
    appendMoveToPath method
    """
    if (transform == '') :
        x, y = point.x, point.y
    else:
        x, y = transformPointXY(point.x, point.y, transform)
    return pathSVG.appendMoveToPath(x, y, relative=False)

def lineP(pathSVG, point, transform=''):
    """
    appendLineToPath method
    """
    if (transform == '') :
        x, y = point.x, point.y
    else:
        x, y = transformPointXY(point.x, point.y, transform)
    return pathSVG.appendLineToPath(x, y, relative=False)

def cubicCurveP(pathSVG, control1, control2, point, transform=''):
    """
    Accepts pathSVG, control1, control2, point and optional transform to call appendCubicCurveToPath method
    """
    if (transform == '') :
        c1x, c1y, c2x, c2y, px, py = control1.x, control1.y, control2.x, control2.y, point.x, point.y
    else:
        c1x, c1y = transformPointXY(control1.x, control1.y, transform)
        c2x, c2y = transformPointXY(control2.x, control2.y, transform)
        px, py = transformPointXY(point.x, point.y, transform)
    return pathSVG.appendCubicCurveToPath(c1x, c1y, c2x, c2y, px, py, relative=False)

def quadraticCurveP(pathSVG, control1, point, transform=''):
    """
    Accepts pathSVG, control1, point, & optional transform. Calls cubicCurveP with pathSVG, control1, control1, point, transform
    """
    return cubicCurveP(pathSVG, control1, control1, point, transform)
