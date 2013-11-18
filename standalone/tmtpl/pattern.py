#!/usr/bin/python
#
# This file is part of the tmtp (Tau Meta Tau Physica) project.
# For more information,see http://www.taumeta.org/
#
# Copyright (C) 2010,2011,2012 Susan Spencer and Steve Conklin
#
# This program is free software:you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation,either version 2 of the License,or
# (at your option) any later version. Attribution must be given in
# all derived works.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not,see<http://www.gnu.org/licenses/>.

#python
import math
import re
from math import sin,cos,sqrt,asin
#pysvg
import pysvg.builders as PYB
#tmtp
from document import *
from constants import *
from utils import debug


#c = {"one": 1, "two": 2}
#for k,v in c.iteritems():
#    exec("%s=%s" % (k,v))



    #TODO: write function to draw shortest line from point to line
    #TODO: write function to draw perpendicular line from point to line (with optional parameter to use a given angle)
#---



#---calculate and draw points---

def pPoint(parent,id,p1,transform=''):
    '''
    Creates an SVG red pattern point in group/layer 'reference', id=p2.id, stroke=none, fill=red
    Accepts:
        parent of class patternPiece,
        id of type string,
        p1 of class Point or function which returns a Point,
        optional SVG transform phrase.
    Returns:
        p2 of class Point as child of parent,
        p2.x=p1.x+transform,
        p2.y=p1.y+transform,
        p2.name=id,
        p2.id=parent.letter+'.'+id,
    Naming convention:
        minimum of two lowercase letters:
            lowercase(parent.letter) + next unused lower case letter, e.g. for pattern piece A: aa,ab,ac,ad,etc.
    Always assign to python variable of same name in pattern design file
        Examples:
            ac=pPoint(A,'ac',downP(aa,2*IN)) #ac is point on pattern piece A, 2inches below point aa
            bd=pPoint(B,'bd',temp_point) #bd is point on pattern piece B, same x & y values as variable temp_point
            cc=pPoint(C,'cc',ba)#cc is point on pattern piece B, same x & y values as ba
    The python variable assignment is required because they are used to write the SVG circles and paths to the XML Document at the doc.draw() command at the end of the pattern design file
    Paths are built as    'M',aa,'L',ab,'C',ac.c1,ac.c2,ac,'L',aa   (no 'm','l','h','v','z' relative path or 'Q' quadratic curve commands)
    '''
    p2=Point('reference',id,p1.x,p1.y,'point_style',transform)
    parent.add(p2)
    return p2


def cPoint(parent,id,p1,transform=''):
    '''
    Creates SVG unfilled gray circle for bezier curve control points
    Accepts:
        parent as class patternPiece,
        id as type string,
        p1 as type Point or function that returns a Point,
        optional SVG transform phrase
    Returns:
        p2 as class Point and grandchild of parent and child of pattern point,
        p2.x=p1.x+transform,
        p2.y=p1.y+transform,
        p2.name=id,
        p2.id=parent.name+'.'+id,
        SVG circle id=p2.id
    Naming convention is pattern point variable name +'.'+{'c1'|'c2'} --- the control points on bezier curve to ac are ac.c1 and ac.c2
    Always assign to python variable of same name in pattern design file:
        Example of control points on curve from ac to ad:
            length=distance(ac,ad)/3.0
            ad.c1=cPoint(A,'ad.c1',polar(ac,length,angleOfLine(ab,ac)+ANGLE90)
            ad.c2=cPoint(A,'ad.c2',polar(ad,length,angleOfLine(ad,ad.c1))
    The python variable assignment is required because they are used to write the SVG circles and paths to the XML Document at the doc.draw() command at the end of the pattern design file
    Paths are built as    'M',aa,'L',ab,'C',ac.c1,ac.c2,ac,'L',aa   (no 'm','l','h','v','z' relative path or 'Q' quadratic curve commands)
    '''
    p2=Point('reference',id,p1.x,p1.y,'controlpoint_style',transform)
    parent.add(p2)
    return p2

def cPointXY(parent,id,x,y,transform=''):
    '''Similar to cPoint() above, except accepts x and y of type float instead of p1 as type Point
    Creates SVG unfilled gray circle for control points in bezier curves'''
    p1=Point('reference',id,x,y,'controlpoint_style',transform)
    parent.add(p1)
    return p1

def circle(parent,id,p1):
    """creates an unfilled circle """
    p2=Point('reference',id+'_circle',p1.x,p1.y,'circle_style',transform='',size=p1.size)
    parent.add(p2)
    p3=Point('reference',id,p1.x,p1.y,'point_style',transform='',size=5)
    parent.add(p3)
    return



#---functions to calculate points. These functions do not create SVG objects---

def updatePoint(p1,p2):
    '''Accepts p1 and p2 of class Point. Updates p1 with x & y values from p2'''
    #p2 might not have p2.coords, so create p1.coords with p2.x & p2.y
    p1.x,p1.y,p1.coords=p2.x,p2.y,str(p2.x)+','+str(p2.y)
    return

def right(p1,n):
    '''Accepts p1 of class Point,n of type float. Returns p2 of class Point to the right of p1 at (p1.x+n, p1.y)'''
    p2=Pnt(p1.x+n,p1.y)
    return p2

def left(p1,n):
    '''Accepts p1 of class Point,n of type float. Returns p2 of class Point to the left of p1 at (p1.x-n, p1.y)'''
    p2=Pnt(p1.x-n,p1.y)
    return p2

def up(p1,n):
    '''Accepts p1 of class Point,n of type float. Returns p2 of class Point above p1 at (p1.x, p1.y-n)'''
    p2=Pnt(p1.x,p1.y-n)
    return p2

def down(p1,n):
    '''Accepts p1 of class Point,n of type float. Returns p2 of class Point below p1 at (p1.x, p1.y+n)'''
    p2=Pnt(p1.x,p1.y+n)
    return p2

def symmetricPoint(p1,p2,type='vertical'):
    """
    Accepts p1 and p2 of class Point, and optional type is either 'vertical' or 'horizontal with default 'vertical'.
    Returns p3 of class Point as "mirror image" of p1 relative to p2
    If type=='vertical': pnt is on opposite side of vertical line x=p2.x from p1
    If type=='horizontal': pnt is on opposite side of horizontal line y=p2.y from p1
    """
    p3=Pnt()
    dx=p2.x-p1.x
    dy=p2.y-p1.y
    if (type=='vertical'):
        p3.x=p2.x+dx
        p3.y=p1.y
    elif (type=='horizontal'):
        p3.x=p1.x
        p3.y=p2.y+dy
    return p3

def polar(p1,distance,angle):
    '''
    Adapted from http://www.teacherschoice.com.au/maths_library/coordinates/polar_-_rectangular_conversion.htm
    Accepts p1 as type Point,distance as float,angle as float. angle is in radians
    Returns p2 as type Point, calculated at distance and angle from p1,
    Angles start at position 3:00 and move clockwise due to y increasing downwards on Cairo Canvas
    '''
    r=distance
    x=p1.x+(r*cos(angle))
    y=p1.y+(r*sin(angle))
    p2=Pnt(x,y)
    return p2

def midPoint(p1,p2,n=0.5):
    '''Accepts p1 & p2 of class Point or Pnt, and n where 0<n<1. Returns p3 of class Pnt as midpoint b/w p1 & p2'''
    p3=Pnt((p1.x+p2.x)*n,(p1.y+p2.y)*n)
    return p3

# ---length---

def distance(p1,p2):
    """Accepts p1 & p2 if class Pnt or Point and returns distance between the points (type float)"""
    return math.sqrt(((p2.x-p1.x)**2)+((p2.y-p1.y)**2))

def distanceXY(x1,y1,x2,y2):
    """Accepts four values x1,y1,x2,y2 and returns distance"""
    return math.sqrt(((x2-x1)**2)+((y2-y1)**2))

#---angles---

def degreeOfAngle(angle):
    return angle*180.0/math.pi

def angleOfDegree(degree):
    return degree*math.pi/180.0

def angleOfSlope(p1,p2):
    """
    Accepts p1 & p2 of class Pnt
    Returns the angle in radians from p1 to p2
    Identical to function angleOfLine(); keep this function for educational purposes
    """
    rise=p2.y-p1.y
    run=p2.x-p1.x
    return math.atan2(rise,run)

def angleOfLine(p1,p2):
    """
    Accepts p1 & p2 of class Pnt
    Returns the angle in radians of the vector between them\
    """
    return math.atan2(p2.y-p1.y,p2.x-p1.x)

def angleOfVector(p1,v,p2):
    """
    Accepts p1, v, and p2 of class Pnt
    Returns the angle in radians between the vector v-to-p1 and vector v-to-p2
    """
    #L1=distance(p1,p2)
    #L2=distance(p1,p3)
    #L3=distance(p2,p3)
    #return math.acos((L1**2+L2**2-L3**2)/(2*L1*L2))
    return abs(angleOfLine(v,p1)-angleOfLine(v,p2))

def angleOfChord(chord_width,radius):
    """
    Find the angle between two points given center,radius,chordlength & starting point=2*asin(d/2r)
    Adapted from http://math.stackexchange.com/questions/164541/finding-a-point-having-the-radius-chord-length-and-another-point
    """
    d=chord_width # chord width-usage:could be the dart width
    r=radius # radius-usage:could be the dart length
    d_div_2r=d/(2.0*r)
    angle=2*asin(d_div_2r) # angle-usage:could be the rotation angle used in slashAndSpread to create a dart
    return angle

#---slope---
def slopeOfLine(p1,p2):
    """ Accepts two point objects and returns the slope """
    if ((p2.x-p1.x) <> 0):
        m=(p2.y-p1.y)/(p2.x-p1.x)
    else:
        print 'Vertical Line'
        m=None
    return m

#---tests for position---
def isRight(pnt1, pnt2):
    '''returns 1 if pnt2 is to the right of pnt1'''
    right=0
    if pnt2.x>pnt1.x:
        right=1
    return right

def isLeft(pnt1, pnt2):
    '''returns 1 if pnt2 is to the left of pnt1'''
    left=0
    if pnt2.x<pnt1.x:
        left=1
    return left

def isAbove(pnt1, pnt2):
    '''returns 1 if pnt2 is above pnt1'''
    up=0
    if pnt2.y<pnt1.y:
        up=1
    return up

def isBelow(pnt1, pnt2):
    '''returns 1 if pnt2 is below pnt1'''
    down=0
    if pnt2.y>pnt1.y:
        down=1
    return down

def lowest(pnt1,pnt2):
    if pnt2.y>pnt1.y:
        return pnt2
    else:
        return pnt1

def highest(pnt1,pnt2):
    if pnt2.y<pnt1.y:
        return pnt2
    else:
        return pnt1

def leftmost(pnt1,pnt2):
    if pnt2.x<pnt1.x:
        return pnt2
    else:
        return pnt1

def rightmost(pnt1,pnt2):
    if pnt2.x>pnt1.x:
        return pnt2
    else:
        return pnt1

# ---lines---

def onLineAtLength(p1,p2,length,rotation=0):
    """
    Accepts p1 and p2 of class Pnt, distance, and an optional rotation angle
    Returns p3 of class Pnt on the line at length measured from p1 towards p2
    If length is negative, will return p3 at length measured from p1 in opposite direction from p2
    The point is optionally rotated about the first point by the rotation angle in degrees
    """
    p3=Pnt()
    lineangle=angleOfLine(p1,p2)
    angle=lineangle+(rotation*(math.pi/180))
    x=(length*math.cos(angle))+p1.x
    y=(length*math.sin(angle))+p1.y
    p3=Pnt(x,y)
    return p3

def onLineAtX(p1,p2,x):
    #on line p1-p2,given x find y
    pnt=Pnt()
    pnt.x=x
    if (p1.x==p2.x):# vertical line
        print  'infinite values of y on vertical line'
        return None
    else:
        m=(p1.y-p2.y)/(p1.x-p2.x)
        b=p2.y-(m*p2.x)
        pnt.y=(x*m)-b
        return pnt

def onLineAtY(p1,p2,y):
    #on line p1-p2,find x given y
    p3=Pnt()
    if (p1.y==p2.y): #if horizontal line
        if (p1.y!=y): #if y is not on horizontal line
            print 'y =',y,' -- not on horizontal line p1.y =', p1.y, 'in onLineAtY -- no intersection'
        else:
            p3.y=y
    elif (p1.x==p2.x):# if vertical line
        p3.x=p1.x
        p3.y=y
    else:
        m=(p1.y-p2.y)/(p1.x-p2.x)
        b=p2.y-(m*p2.x)
        p3.x=(y-b)/m
        p3.y=y
    return p3

def intersectLines(p1,p2,p3,p4):
    """
    Find intersection between two lines. Accepts p1,p2,p3,p4 as class Point. Returns p5 as class Point
    Intersection does not have to be within the supplied line segments
    """
    x,y=0.0,0.0
    if (p1.x==p2.x): #if 1st line vertical,use slope of 2nd line
        x=p1.x
        m2=slopeOfLine(p3,p4)
        b2=p3.y-m2*p3.x
        y=m2*x+b2
    elif (p3.x==p4.x): #if 2nd line vertical, use slope of 1st line
        x=p3.x
        m1=slopeOfLine(p1,p2)
        b1=p1.y-m1*p1.x
        y=m1*x+b1
    else: #otherwise use ratio of difference between slopes
        m1=(p2.y-p1.y)/(p2.x-p1.x)
        m2=(p4.y-p3.y)/(p4.x-p3.x)
        b1=p1.y-m1*p1.x
        b2=p3.y-m2*p3.x
        #if (abs(b1-b2)<0.01) and (m1==m2):
        if (m1==m2):
            debug('***** Parallel lines in intersectLines2 *****')
        #else:
            #if (m1==m2):
                #x=p1.x
            #else:
                #x=(b2-b1)/(m1-m2)
        else:
            x=(b2-b1)/(m1-m2)
            y=(m1*x)+b1 # arbitrary choice,could have used m2 & b2
    p5=Pnt(x,y)
    return p5

#---curves---
def intersectLineCurve(P1,P2,curve,n=100):
    '''
    Accepts two points of a line P1 & P2,and an array of connected bezier curves [P11,C11,C12,P12,C21,C22,P22,C31,C32,P32,...]
    Returns an array points_found[] of point objects where line intersected with the curve,and tangents_found[] of tangent angle at that point
    '''
    # get polar equation for line for P1-P2
    # point furthest away from 1st point in curve[] is the fixed point & sets the direction of the angle towards the curve
    #if distance(P1,curve[0]) >=distance(P2,curve[0] ):
    #   fixed_pnt=P1
    #   angle=angleOfLine(P1,P2)
    #else:
    #   fixed_pnt=P2
    #  angle=angleOfLine(P2,P1)
    fixed_pnt=P1
    angle=angleOfLine(P1,P2)
    #print 'P1 =',P1.x,P1.y
    #print 'P2 =',P2.x,P2.y
    #for pnt in curve:
        #print 'curve =',pnt.x,pnt.y
    intersections=0
    points_found=[]
    #tangents_found=[]
    j=0
    while j<=len(curve) -4: # for each bezier curve in curveArray
        intersection_estimate=intersectLines(P1,P2,curve[j],curve[j+3]) # is there an intersection?
        if intersection_estimate !=None or intersection_estimate !='':
            interpolatedPoints=interpolateCurve(curve[j],curve[j+1],curve[j+2],curve[j+3],n)  #interpolate this bezier curve,n=100
            k=0
            while k<len(interpolatedPoints)-1:
                pnt_on_line=polar(fixed_pnt,distance(fixed_pnt,interpolatedPoints[k]),angle)
                range=distance(interpolatedPoints[k],interpolatedPoints[k+1]) # TODO:improve margin of error
                length=distance(pnt_on_line,interpolatedPoints[k])
                #print k,'pntOnCurve',interpolatedPoints[k].x,interpolatedPoints[k].y,'onLineAtLength',pnt_on_line.x,pnt_on_line.y,distance,range
                if ( length<=range):
                    # its close enough!
                    #print 'its close enough!'
                    if k>1:
                        if (interpolatedPoints[k-1] not in points_found) and (interpolatedPoints[k-2] not in points_found):
                            points_found.append(interpolatedPoints[k])
                            #tangents_found.append(angleOfLine(interpolatedPoints[k-1],interpolatedPoints[k+1]))
                            intersections=intersections+1
                    elif k==1:
                        if (curve[0] not in intersections):
                            points_found.append(interpolatedPoints[1])
                            #tangents_found.append(angleOfLine(curve[0],interpolatedPoints[2]))
                            intersections=intersections+1
                    else:
                        intersections.append(curve[0])
                        #tangents_found.append(angleOfLine(curve[0],curve[1]))
                k=k+1
        j=j+3 # skip j up to P3 of the current curve to be used as P0 start of next curve
        if intersections==0:
            print 'no intersections found in intersectLineCurve(',P1.name,P2.name,' and curve'
    #return points_found,tangents_found
    return points_found

def onCurveAtX(curve,x):
    '''
    Accepts an array 'curve' of bezier curves,returns list of points. Each bezier curve consists of  P0,P1,P2,P3 [eg knot1,controlpoint1,controlpoint2,knot2].
    P3 of one curve is P0 of the next curve. Minimum of one bezier curve in curveArray.
    Accepts value of x to find on curve.
    Returns array 'intersections' which contains y values of each intersection found in order from 1st to last bezier curve in curveArray.
    '''
    intersect_points=[]
    xlist,ylist=[],[]
    pnt=Pnt()
    j=0
    while j<=len(curve) -4: # for each bezier curve in curveArray
        interpolatedPoints=interpolateCurve(curve[j],curve[j+1],curve[j+2],curve[j+3],100)  #interpolate this bezier curve,n=100
        # get min & max for x & y for this bezier curve from its interpolated points
        i=0
        while (i<len(interpolatedPoints)):
            xlist.append(interpolatedPoints[i].x)
            ylist.append(interpolatedPoints[i].y)
            i=i+1
        xmin,ymin,xmax,ymax=min(xlist),min(ylist),max(xlist),max(ylist)
        #print 'xmin,xmax =',xmin,xmax,'...pattern.onCurveAtX()'
        #print 'ymin,ymax =',ymin,ymax,'...pattern.onCurveAtX()'
        #print 'x =',x,'...pattern.onCurveAtX()'
        i=0
        if ((x >=xmin) and (x<=xmax)):
            while (i<(len(interpolatedPoints)-1)):
                if (x >=interpolatedPoints[i].x) and (x<=interpolatedPoints[i+1].x):
                    pnt=onLineAtX(interpolatedPoints[i],interpolatedPoints[i+1],x)
                    intersect_points.append(pnt)
                i=i+1
        j=j+3 # skip j up to P3 of the current curve to be used as P0 start of next curve
    return intersect_points # return array of intersection points

def tangentOfCurveAtLine(P1,P2,curve):
    '''
    Accepts P1 & P2 of class Pnt or Point, and curve as 4-element array containing bezier curve points P0 C1 C2 P1 of type Pnt or Point.
    P1 & P2 define a line that intersects the curve.
    Returns the first found intersection point and the angle of the tangent ray at that point directional down the path
    '''
    # determine whether P1 or P2 is the  furthest away from 1st point in curve[].
    # The point further away is considered the 'fixed point' & use this point to derive the angle of the line towards the curve
    if distance(P1,curve[0]) >=distance(P2,curve[0] ):
        fixed_pnt=P1
        angle=angleOfLine(P1,P2)
    else:
        fixed_pnt=P2
        angle=angleOfLine(P2,P1)
    intersections=[]
    pnt=Pnt()
    found='false'
    j=0
    while j<=len(curve) -4 and found !='true': # for each bezier curve in curveArray until a point is found
        intersection_estimate=intersectLines(P1,P2,curve[j],curve[j+3]) # is there an intersection?
        if intersection_estimate !=None or intersection_estimate !='':
            interpolated_points=interpolateCurve(curve[j],curve[j+1],curve[j+2],curve[j+3],100)  #interpolate this bezier curve,n=100
            k=0
            while (k<len(interpolated_points)-1) and (found !='true'):
                pnt_on_line=polar(fixed_pnt,distance(fixed_pnt,interpolated_points[k]),angle)
                range=distance(interpolated_points[k],interpolated_points[k+1]) # TODO:improve margin of error
                if (distance(pnt_on_line,interpolated_points[k])<range):
                    # its close enough!
                    num=k
                    found='true'
                    if k>1:
                        if (interpolated_points[k-1] not in intersections) and (interpolated_points[k-2] not in intersections):
                            intersections.append(interpolated_points[k])
                    elif k==1:
                        if (interpolated_points[k-1] not in intersections):
                            intersections.append(interpolated_points[k])
                    else:
                        intersections.append(interpolated_points[k])
                k=k+1
        j=j+3 # skip j up to P3 of the current curve to be used as P0 start of next curve
    if (found=='true'):
        tangent_angle=angleOfLine(interpolated_points[num-1],interpolated_points[num+1])
    else:
        tangent_angle=None
    return interpolated_points[num],tangent_angle

def curveLength(curve,n=100):
    '''
    Accepts curve array with a minimum of four Pnt objects P0,P1,P2,P3 (knot1,controlpoint1,controlpoint2,knot2).
    Each curve after the first will use P3 from the previous curve as it's P0,and use it's own P1,P2,P3
    n is the number to subdivide each curve for calculating the interpolated points and curve length.
    Adapted from http://www.planetclegg.com/projects/WarpingTextToSplines.html
    '''
    curveLength=0.0
    j=0
    while j<=len(curve) -4: # for each curve,get segmentLength & add to curveLength
        interpolatedPoints=interpolateCurve(curve[j],curve[j+1],curve[j+2],curve[j+3],n)  #interpolate this curve
        # add up lengths between the interpolated points
        segmentLength=0.0
        i=1
        while (i<=n):
                segmentLength=segmentLength+distance(interpolatedPoints[i-1],interpolatedPoints[i]) #length from previous point to current point
                i=i+1
        curveLength=curveLength+segmentLength
        j=j+3 # skip j up to P3 of the current curve to be used as P0 start of next curve
    return curveLength

def curveLengthAtPoint(pnt,curve,n=100):
    found=0
    curve_length=0.0
    j=0
    while j<=len(curve) -4 and found==0: # for each curve,get segmentLength & add to curveLength
        interpolated_points=interpolateCurve(curve[j],curve[j+1],curve[j+2],curve[j+3],n)  #interpolate this curve
        # add up lengths between the interpolated points
        current_curve_length,found=interpolatedCurveLengthAtPoint(pnt,interpolated_points,found)
        curve_length=curve_length+current_curve_length
        j=j+3 # skip j up to P3 of the current curve to be used as P0 start of next curve
    if curve_length==0.0:
        print 'Point not found in curveLengthAtPoint'
    return curve_length

def interpolatedCurveLengthAtPoint(pnt,interpolatedPoints,found=0):
    # add up lengths between the interpolated points
    segment_length=0.0
    i=1
    while (i<len(interpolatedPoints)) and (found==0):
        current_length=distance(interpolatedPoints[i-1],interpolatedPoints[i]) #length from previous point to current point
        segment_length=segment_length+current_length
        if pnt==interpolatedPoints[i] or distance(pnt,interpolatedPoints[i])<=current_length:
            found=1
        i=i+1
    return segmentLength,found

def curvePointAtLength(length,curve):
    p1=Pnt()
    found=0
    j=0
    while (j <= len(curve)-4) and (p1.x == ""): # for each curve, find pnt
        interpolated_points = interpolateCurve(curve[j],curve[j+1],curve[j+2],curve[j+3],n)
        p1 = interpolatedCurvePointAtlength(length, interpolated_points)
        j = j+3 # skip j up to P3 of the current curve to be used as P0 start of next curve
    return p1

def interpolatedCurvePointAtLength(length, interpolatedPoints):
    p1 = Pnt()
    i = 1
    segmentLength = 0
    while (i < len(interpolatedPoints)) and (p1.x == ''):
        segmentLength += distance(interpolatedPoints[i-1], interpolatedPoints[i]) #length from previous point to current point
        if segmentLength >= length:
            p1.x, p1.y = interpolatedPoints[i].x, interpolatedPoints[i].y
            i = i+1
    return p1

def interpolateCurveList(curve,t=100):
    '''curve can have multiple cubic curves P0 C1 C2 P1 C1 C2 P3...'''
    interpolatedPoints=[]
    j=0
    while j<=len(curve)-4:#interpolate each cubic curve
        temp_list=interpolateCurve(curve[j],curve[j+1],curve[j+2],curve[j+3],t)
        for pnt in temp_list:
            interpolatedPoints.append(pnt)
        j=j+3
    return interpolatedPoints

def interpolateCurve(P0,C1,C2,P1,t=100):
    '''
    Accepts curve points P0,C1,C2,P1 & number of interpolations t
    Returns array of interpolated points of class Pnt
    Adapted from http://www.planetclegg.com/projects/WarpingTextToSplines.htm
    '''
    # calculate coefficients for two knot points P0 & P1 ;     C1 & C2 are the controlpoints.
    # x coefficients
    A=P1.x-(3*C2.x)+(3*C1.x)-P0.x
    B=(3*C2.x)-(6*C1.x)+(3*P0.x)
    C=(3*C1.x)-(3*P0.x)
    D=P0.x
    # y coefficients
    E=P1.y-(3*C2.y)+(3*C1.y)-P0.y
    F=(3*C2.y)-(6*C1.y)+(3*P0.y)
    G=(3*C1.y)-(3*P0.y)
    H=P0.y
    # calculate interpolated points
    interpolatedPoints=[]
    maxPoint=float(t)
    i=0
    while ( i<=t):
            j=i/maxPoint # j can't be an integer,i/t is an integer..always 0.
            x=A*(j**3)+B*(j**2)+C*j+D
            y=E*(j**3)+F*(j**2)+G*j+H
            interpolatedPoints.append(Pnt(x,y))
            i=i+1
    return interpolatedPoints

def splitCurveAtLength(length, curve):
    '''Accepts a point on a curve,and a curve list with points P0 C1 C2 P1.
    Returns curve list with P0,split.c1,split.c2,split_pnt,new.c11,new.c12,P1'''
    # find split point
    interpolated_points = interpolateCurve(curve[0], curve[1], curve[2], curve[3])
    split_pnt = interpolatedCurvePointAtLength(length, interpolated_points) # split neck curve at this point
    # find tangent at split point
    pnt1 = interpolatedCurvePointAtLength(length - .25*CM, interpolated_points) # arbitrary 1/4th of a cm-good enough for this application?
    pnt2 = interpolatedCurvePointAtLength(length + .25*CM, interpolated_points) # arbitrary 1/4th of a cm-good enough for this application?
    forward_tangent_angle = angleOfLine(pnt1, pnt2)
    backward_tangent_angle = angleOfLine(pnt2, pnt1)
    # neck control points
    # b/w curve[0] and split_pnt
    length=distance(curve[0],split_pnt)/3.0
    split_pnt.c1=polar(curve[0],length,angleOfLine(curve[0],curve[1])) # preserve angle b/w P0 & original 1st control point
    split_pnt.c2=polar(split_pnt,length,backward_tangent_angle)
    # b/w split_pnt and curve[3]
    curve3=PntP(curve[3])
    length=distance(split_pnt,curve3)/3.0
    curve3.c1=polar(split_pnt,length,forward_tangent_angle)
    curve3.c2=polar(curve3,length,angleOfLine(curve3,curve[2])) # preserve angle b/w original 2nd control point & P1
    new_curve=[]
    new_curve.append(curve[0])
    new_curve.append(split_pnt.c1)
    new_curve.append(split_pnt.c2)
    new_curve.append(split_pnt)
    new_curve.append(curve3.c1)
    new_curve.append(curve3.c2)
    new_curve.append(curve3)
    return new_curve

# --- intersections-circles---

def intersectCircles(C1,r1,C2,r2):
    """
    Accepts C1,r1,C2,r2 where C1 & C2 are point objects for the center of each circle, and r1 & r2 are the radius of each circle
    Returns an array P which holds objects of class Pnt for each intersection
    """
    x0,y0=C1.x,C1.y
    x1,y1=C2.x,C2.y
    d=distanceXY(x0,y0,x1,y1) # distance b/w circle centers
    dx,dy=(x1-x0),(y1-y0) # negate y b/c canvas increases top to bottom
    P=[]
    if (d==0):
        #intersections=0
        print 'center of both circles are the same...intersections.intersectCircles()'
        print 'C1 =', C1.x, C1.y, 'radius1 =', r1
        print 'C2 =', C2.x, C2.y, 'radius1 =',r2
    elif (d<abs(r1-r2)):
        #intersections=0
        print 'one circle is within the other ...intersections.intersectCircles()'
        print 'd =', d
        print 'r1 - r2 =',(r1-r2)
        print 'd< abs(r1 - r2) ?', (d<abs(r1-r2))
        print 'C1 =', C1.x, C1.y, 'radius1 =', r1
        print 'C2 =', C2.x, C2.y, 'radius1 =',r2
    elif (d>(r1+r2)):
        #intersections=0
        print 'circles do not intersect ...intersections.intersectCircles()'
        print 'd =', d
        print 'r1 + r2 =',(r1+r2)
        print 'd > abs(r1 + r2) ?', (d>abs(r1+r2))
        print 'C1 =', C1.x, C1.y, 'radius1 =', r1
        print 'C2 =', C2.x, C2.y, 'radius1 =',r2
        # TODO:possible kluge -check if this is acceptable using a small margin of error between r1 & r2 (2*CM)?:
        #r2=d-r1
    else:
        #intersections=2 or intersections=1
        a=((r1*r1)-(r2*r2)+(d*d))/(2.0*d)
        x2=x0+(dx*a/d)
        y2=y0+(dy*a/d)
        h=math.sqrt((r1*r1)-(a*a))
        rx=-dy*(h/d)
        ry=dx*(h/d)
        X1=x2+rx
        Y1=y2+ry
        X2=x2-rx
        Y2=y2-ry
        P.append(Pnt(X1,Y1))
        P.append(Pnt(X2,Y2))
    return P

def onCircleAtX(C,r,x):
    """
    Finds points on circle where p.x=x
    Accepts C as an object of class Pnt for the center of the circle,
    r as the radius, and x to find the points on the circle
    Returns an array P which holds objects of class Pnt for each intersection
    """
    P=[]
    if abs(x-C.x)>r:
        print 'x is outside radius of circle in intersections.onCircleAtX()'
    else:
        translated_x=x-C.x # center of translated circle is (0,0) as translated_x is the difference b/w C.x & x
        translated_y1=abs(math.sqrt(r**2-translated_x**2))
        translated_y2=-(translated_y1)
        y1=translated_y1+C.y # translate back to C.y
        y2=translated_y2+C.y # translate back to C.y
        P.append(Pnt(x,y1))
        P.append(Pnt(x,y2))
    return P

def onCircleAtY(C,r,y):
    """
    Finds points one or two points on circle where P.y=y
    Accepts C of class Pnt or Point as circle center, r of type float as radius, and y of type float)
    Returns an array P containg intersections of class Pnt
    Based on paulbourke.net/geometry/sphereline/sphere_line_intersection.py,written in Python 3.2 by Campbell Barton
    """
    if abs(y-C.y)>r:
        print 'y is outside radius in onCircleAtY() -- no intersection'
        return
    else:
        translated_y=y-C.y
        translated_x1=abs(math.sqrt(r**2-translated_y**2))
        translated_x2=-translated_x1
        x1=translated_x1+C.x
        x2=translated_x2+C.x
        P=[]
        P.append(Pnt(x1,y))
        P.append(Pnt(x2,y))
    return P

def intersectLineCircle(C,r,P1,P2):
    """
    Finds intersection of a line segment and a circle.
    Accepts circle center point object C,radius r,and two line point objects P1 & P2
    Returns an object P with number of intersection points,and up to two coordinate pairs as P.intersections,P.p1,P.p2
    Based on paulbourke.net/geometry/sphereline/sphere_line_intersection.py,written in Python 3.2 by Campbell Barton
    """
    P,p1,p2=Pnt(),Pnt(),Pnt()
    intersections=0

    if P1.x==P2.x: #vertical line
        if abs(P1.x-C.x)>r:
            print 'no intersections for vertical line P1',P1.name,P1.x,P1.y,', P2',P2.name,P2.x,P2.y,',and Circle',C.name,C.x,C.y,', radius',r
            return None
        else:
            p1.x=P1.x
            p2.x=P1.x
            p1.y=C.y+sqrt((r**2)-((P1.x-C.x)**2))
            p2.y=C.y-sqrt(r**2-(P1.x-C.x)**2)
    elif P1.y==P2.y: #horizontal line
        if abs(P1.y-C.y)>r:
            print 'no intersections for horizontal line P1',P1.name,P1.x,P1.y,', P2',P2.name,P2.x,P2.y,',and Circle',C.name,C.x,C.y,', radius',r
            return None
        else:
            p1.y=P1.y
            p2.y=P1.y
            p1.x=C.x+sqrt(r**2-(P1.y-C.y)**2)
            p2.x=C.x-sqrt(r**2-(P1.y-C.y)**2)
    else:
        a=(P2.x-P1.x)**2+(P2.y-P1.y)**2
        b=(2.0*((P2.x-P1.x)*(P1.x-C.x))+((P2.y-P1.y)*(P1.y-C.y)))
        c=((C.x)**2+(C.y)*82+(P1.x**2)+(P1.y)**2-(2.0*(C.x*P1.x+C.y*P1.y ))-(r)**2)
        i=b**2-4.0*a*c
        if i<0.0:
            print 'no intersections b/w line',P1.name,P1.x,P1.y,'--',P2.name,P2.x,P2.y,'and Circle',C.name,C.x,C.y,'with radius',r
            return None
        elif i==0.0:
            # one intersection
            intersections=1
            mu=-b/(2.0*a)
            p1.x,p1.y=P1.x+mu*(P2.x-P1.x),P1.y+mu*(P2.y-P1.y)
        elif i>0.0:
            # two intersections
            intersections=2
            # first intersection
            mu1=(-b+math.sqrt(i))/(2.0*a)
            p1.x,p1.y=P1.x+mu1*(P2.x-P1.x),P1.y+mu1*(P2.y-P1.y)
            # second intersection
            mu2=(-b-math.sqrt(i))/(2.0*a)
            p2.x,p2.y=P1.x+mu2*(P2.x-P1.x),P1.y+mu2*(P2.y-P1.y)
    P.p1=p1
    P.p2=p2
    return P

def intersectChordCircle(C,r,P,chord_length):
    ''' Accepts center of circle,radius of circle,a point on the circle,and chord length.  Returns a list of two points on the circle at chord_length distance away from original point'''
    d=chord_length
    # point on circle given chordlength & starting point=2*asin(d/2r)
    d_div_2r=d/(2.0*r)
    angle=2*asin(d_div_2r)
    P=[]
    P.append(polar(C,r,angle))
    P.append(polar(C,r,- angle))
    return P


#---darts---
def waistDart(parent,dart_width,dart_length,length,waist_curve,dart_angle=ANGLE90):
    '''Accepts dart_width,dart_length,length,and curve  list from center to side with points P0 C1 C2 P1,and angle of dart in radians.
    Default angle is pi/4 radians (90 degrees).
    If waist does not have a curve,create waist_curve list with control points at 1/3 & 2/3 distance on line from center to side.
    Returns dart_apex,curve1 list from center to dart with points P0 C11 C12 P1,and curve2 list from dart to side with points P2 C31 C32 P3.
    Side point is rotated/moved out to accommodate dart.'''
    # see http://math.stackexchange.com/questions/164541/finding-a-point-having-the-radius-chord-length-and-another-point
    # find the angle between two points given center,radius,chordlength & starting point=2*asin(d/2r)
    d=dart_width # chord length
    r=dart_length # radius
    d_div_2r=d/(2.0*r)
    rotation_angle=2*asin(d_div_2r)
    # split neck curve at length-returns curve with P0 C11 C12 P1 C21 C22 P2
    split_curve=splitCurveAtLength(length,waist_curve)
    #dart_apex=pPoint(parent,parent.name+'dart_apex',polar(split_curve[3],dart_length,angleOfLine(split_curve[3],split_curve[2])+ANGLE90))
    # TODO:test for direction of dart-plus or minus 90 degrees from the angle of the tangent at the dart...
    # ...the angle of line from 2nd control point (split_curve[2]) to the split point (split_curve[3])
    dart_apex=polar(split_curve[3],dart_length,angleOfLine(split_curve[3],split_curve[2])+dart_angle)
    # separate split_curve into inside_curve1 & outside_curve
    inside_curve=[]
    i=0
    while i<=3:
        inside_curve.append(PntP(split_curve[i]))
        i=i+1
    outside_curve=[]
    i=3
    while i<=6:
        outside_curve.append(PntP(split_curve[i ]))
        i=i+1
    # rotate outside leg & side point (outside_curve) relative to the dart_apex,creating the dart
    slashAndSpread(dart_apex,rotation_angle,outside_curve[0],outside_curve[1],outside_curve[2],outside_curve[3])
    return dart_apex,inside_curve,outside_curve

def neckDart(parent,dart_width,dart_length,length,neck_curve):
    '''Accepts dart_width,dart_length,length,and curve list of neck from center to shoulder with points P0 C1 C2 P1.
    Moves/rotates nape point to accomodate dart.
    Returns dart_apex,curve1 list from center to dart with points P0 C11 C12 P1,curve2 list from dart to shoulder with points P2 C31 C32 P3.
    Dart is formed from P1 to dart_apex to P2'''
    # split neck curve at length
    split_curve=splitCurveAtLength(length,neck_curve)
    # see http://math.stackexchange.com/questions/164541/finding-a-point-having-the-radius-chord-length-and-another-point
    # find the angle between two points given center,radius,chordlength & starting point=2*asin(d/2r)
    #d=dart_width # chord length
    #r=dart_length # radius
    #d_div_2r=d/(2.0*r)
    #rotation_angle=2*asin(d_div_2r)

    rotation_angle = angleFromChord(dart_width,dart_length)
    #print('rotation_angle =', rotation_angle)
    dart_apex = pPoint(parent,'dart_apex',polar(split_curve[3],dart_length,angleOfLine(split_curve[3],split_curve[2])+ANGLE90))
    #print('dart_apex =', dart_apex)

    # separate split_curve into curve1 & curve2
    curve1 = []
    i = 0
    while i <= 3:
        p#rint('i = ', i)
        #print('split_curve[', i, '] =', split_curve[i].x, split_curve[i].y)
        curve1.append(PntP(split_curve[i]))
        #print('curve1[', i, '] =', curve1[i].x, curve1[i].y)
        i += 1

    curve2 = []
    i = 3
    while i <= 6:
        p#rint('i = ', i)
        #print('split_curve[', i, '] =', split_curve[i].x, split_curve[i].y)
        curve2.append(PntP(split_curve[i]))
        #print('curve2[',i,'] =', curve2[i].x, curve2[i].y)
        i += 1
    # rotate curve1 relative to the dart_apex,creating the dart
    slashAndSpread(dart_apex,rotation_angle,curve1[0],curve1[1],curve1[2],curve1[3])
    return dart_apex,curve1,curve2

def foldDart(parent,dart,inside_pnt):
    DART_LENGTH=distance(dart,dart.o)
    DART_HALF_ANGLE=abs(angleOfVector(dart.o,dart,dart.i))/2.0
    O_ANGLE=angleOfLine(dart,dart.o)
    I_ANGLE=angleOfLine(dart,dart.i)
    # determine which direction the dart will be folded
    if I_ANGLE<=O_ANGLE:
        FOLD_ANGLE=I_ANGLE-DART_HALF_ANGLE
    else:
        FOLD_ANGLE=I_ANGLE+DART_HALF_ANGLE
    # find intersection of fold & armscye b/w bd2.i & inside_pnt
    # TODO:use intersectLineCurve()
    temp_pnt=polar(dart,DART_LENGTH,FOLD_ANGLE)
    fold_pnt=intersectLines(dart.i,inside_pnt,dart,temp_pnt)
    # dart midpoint at seamline
    temp_pnt=midPoint(dart.i,dart.o)
    mid_pnt=onLineAtLength(dart,temp_pnt,distance(dart,fold_pnt))
    if hasattr(dart,'m'):
        updatePoint(dart.m,mid_pnt)
    else:
        dart.m=pPoint(parent,dart.name+'.m',mid_pnt)
    # dart outside leg at cuttingline
    #temp_pnt=onLineAtLength(dart.o,dart,-SEAM_ALLOWANCE)
    temp_pnt=polar(dart,distance(dart,dart.o)+SEAM_ALLOWANCE,angleOfLine(dart,dart.o))
    if hasattr(dart,'oc'):
        updatePoint(dart.oc,temp_pnt)
    else:
        dart.oc=pPoint(parent,dart.name+'.oc',temp_pnt)
    # dart inside leg at cuttingline
    temp_pnt=onLineAtLength(dart.i,dart,-SEAM_ALLOWANCE)
    if hasattr(dart,'ic'):
        updatePoint(dart.ic,temp_pnt)
    else:
        dart.ic=pPoint(parent,dart.name+'.ic',temp_pnt)
    #create or update dart.angles
    dart.angle=angleOfVector(dart.i,dart,dart.o)

    return

def foldDart2(dart,inside_pnt):
    DART_LENGTH=distance(dart,dart.o)
    DART_HALF_ANGLE=abs(angleOfVector(dart.o,dart,dart.i))/2.0
    O_ANGLE=angleOfLine(dart,dart.o)
    I_ANGLE=angleOfLine(dart,dart.i)
    #determine which direction the dart will be folded
    if I_ANGLE<=O_ANGLE:
        FOLD_ANGLE=I_ANGLE-DART_HALF_ANGLE
    else:
        FOLD_ANGLE=I_ANGLE+DART_HALF_ANGLE
    #TODO:find intersection of fold & armscye b/w bd2.i & inside_pnt
    #TODO:use intersectLineCurve()
    temp_pnt=polar(dart,DART_LENGTH,FOLD_ANGLE)
    fold_pnt=intersectLines(dart.i,inside_pnt,dart,temp_pnt)
    temp_pnt=midPoint(dart.i,dart.o)
    dart.m=onLineAtLength(dart,temp_pnt,distance(dart,fold_pnt)) #dart midpoint at seamline
    dart.oc=polar(dart,distance(dart,dart.o)+SEAM_ALLOWANCE,angleOfLine(dart,dart.o)) #dart outside leg at cuttingline
    dart.ic=onLineAtLength(dart.i,dart,-SEAM_ALLOWANCE) #dart inside leg at cuttingline
    #create or update dart.angles
    dart.angle=angleOfVector(dart.i,dart,dart.o)

    return

def adjustDartLength(p1,dart,p2,extension=1/3.0):
    """
    Finds optimum leg length to smooth the curve from p1 to p2
    Accepts p1 of class Pnt or Point, dart of class Dart, and p2 of class Pnt or Point
    dart.i & dart.o are updated to new longer point on dart legs
    Default extension is 1/3 distance from orig dart length to the line
    drawn between p1 & p2 after the dart is created
    """
    #TODO: define class Dart
    #rotate point 'p1' to p1_new where it would lie if dart were closed
    p1_new=PntP(p1)
    rotation_angle=angleOfVector(dart.i,dart,dart.o)
    slashAndSpread(dart,rotation_angle,p1_new)
    #find intersection of dart leg and line p1_new to p2
    p3=intersectLines(dart,dart.i,p1_new,p2)
    #new dart length at 1/3 distance from dart.i to p3
    new_dart_length=distance(dart,dart.i)+distance(dart.i,p3)*extension
    #update dart.i & dart.o
    p4=onLineAtLength(dart,dart.i,new_dart_length)
    p5=onLineAtLength(dart,dart.o,new_dart_length)
    updatePoint(dart.i,p4)
    updatePoint(dart.o,p5)
    return

# ---control points---
def pointList(*args):
    points=[]
    for arg in args:
        points.append(arg)
    return points

def controlPoints(name,knots):
    #TODO:remove name from args
    k_num=len(knots)-1 # last iterator for n knots 0..n-1
    c_num=k_num-1 # last iterator for n-1 curve segments 0..n-2
    c1=[] # first control points c1[0..c_num]
    c2=[] # second control points c2[0..c_num]
    i=1
    while (i<=c_num):
        # each loop produces c2[previous] and c1[current]
        # special cases:get c1[0] in 1st loop & c2[c_num] in last loop
        # previous segment is segment b/w previous knot & current knot
        # current segment is segment b/w current knot & next knot
        # start with i=1 because can't start processing with knot[0] b/c it doesn't have a previous knot
        previous=(i-1)
        current=i
        next=(i+1)
        last_knot=k_num
        last_segment=c_num
        # process previous segment's c2
        angle=angleOfLine(knots[next],knots[previous])
        length=distance(knots[current],knots[previous])/3.0
        pnt=polar(knots[current],length,angle)
        c2.append(pnt) # c2[previous]
        if (current==1):
            # process 1st segment's c1
            angle=angleOfLine(knots[0],c2[0])
            pnt=polar(knots[0],length,angle)
            c1.append(pnt)
        # process current segment's c1
        angle=angleOfLine(knots[previous],knots[next])
        length=distance(knots[current],knots[next])/3.0
        pnt=polar(knots[current],length,angle)
        c1.append(pnt) # c1[current]
        if (current==c_num):
            # process last segment's c2
            angle=angleOfLine(knots[last_knot],c1[last_segment])
            pnt=polar(knots[last_knot],length,angle)
            c2.append(pnt) # c2[last_segment]
        i=(i+1)
    return c1,c2

# ---transforms---
def transformPointXY(x,y,transform=''):
    """
    Apply an SVG transformation string to a 2D point and return the resulting x,y pair
    """
    #
    # -spc- TODO-use numpy to do a proper handling of all transformations in order
    # Postponing this until after the LGM workshop in order not to introduce
    # a new dependency-for now we will only handle a few transformation types
    #
    if transform=='':
        return x,y
    # Every transform in the list ends with a close paren
    transforms=re.split(r'\)',transform)
    for tr in transforms:
        # I don't know why we get an empty string at the end
        if tr=='':
            continue
        tr=tr.strip()
        trparts=re.split(r',|\(',tr)
        trtype=trparts[0].strip()
        if trtype=='translate':
            #tx=float(trparts[1].strip()) #-- commented out by susan 26/08/11 -- was returning 'invalid literal for float():0 0' error message -- 0,0 because the transform for 1st pattern is 0,0
            splitx=re.split("( )",trparts[1].strip())  # added by susan 26/08/11 -- to split apart the two values in tx
            sx=splitx[0].strip() # strip one more time-susan 26/08/11
            tx=float(sx) # substituted sx for trparts[1].strip()-susan 26/08/11
            x=x+tx
            try:
                ty=float(trparts[2].strip())
                y=y+ty
            except IndexError:
                pass
        elif trtype=='scale':
            sx=float(trparts[1].strip())
            try:
                sy=float(trparts[2].strip())
            except IndexError:
                sy=sx
            x=x*sx
            y=y*sy
        elif trtype=='skewX':
            sx=float(trparts[1].strip())
            # now do the thing
            #TODO:skewX transform not handled yet
            raise NotImplementedError
        elif trtype=='skewY':
            sy=float(trparts[1].strip())
            # now do the thing
            #TODO:skewY not handled yet
            raise NotImplementedError
        elif trtype=='rotate':
            an=float(trparts[1].strip())
            try:
                rx=float(trparts[2].strip())
            except IndexError:
                rx=0
                ry=0
            try:
                ry=float(trparts[3].strip())
            except IndexError:
                ry=0
            # now do the thing
            #TODO:rotate not handled yet
            raise NotImplementedError
        elif trtype=='matrix':
            ma=float(trparts[1].strip())
            mb=float(trparts[2].strip())
            mc=float(trparts[3].strip())
            md=float(trparts[3].strip())
            me=float(trparts[3].strip())
            mf=float(trparts[3].strip())
            # now do the thing
            #TODO:matrix not handled yet
            raise NotImplementedError
        else:
            #TODO:Unexpected transformation %s' % trtype
            raise ValueError
    return x,y

def scaleAboutPointTransform(x,y,scale):
    """
    Return an SVG transform that scales about a specific x,y coordinate
    """
    sx=scale
    sy=scale
    return "matrix(%f,0,0,%f,%f,%f)" % (sx,sy,x-(sx*x),y-(sy*y))

# ---bounding box---

def getBoundingBox(path):
    # TODO:only use information from paths-cuttinLine,seamLine,foldLine,dartLine
    xlist=[]
    ylist=[]
    #print '=====Entered boundingBox ====='
    #print 'path=',path
    path_tokens=path.split() # split path into pieces,separating at each 'space'
    tok=iter(path_tokens)
    try:
        cmd=tok.next()
        if cmd !='M':
            raise ValueError("Unable to handle patches that don't start with an absolute move")
        currentx=float(tok.next())
        currenty=float(tok.next())
        beginx=currentx
        beginy=currenty
        xlist.append(currentx)
        ylist.append(currenty)
    except:
        raise ValueError("Can't handle a path string shorter than 3 tokens")
    while True:
        try:
            cmd=tok.next()
            #print 'processing ',cmd
            if cmd.islower():
                relative=True
            else:
                relative=False
            cmd=cmd.upper()
            if ((cmd=='M') or (cmd=='L') or (cmd=='T')):
                # Note T is really for a Bezier curve,this is a simplification
                x=float(tok.next())
                y=float(tok.next())
                if relative:
                    currentx=currentx+x
                    currenty=currenty+y
                else:
                    currentx=x
                    currenty=y
                xlist.append(currentx)
                ylist.append(currenty)
            elif cmd=='H':
                x=float(tok.next())
                if relative:
                    currentx=currentx+x
                else:
                    currentx=x
                xlist.append(currentx)
            elif cmd=='V':
                y=float(tok.next())
                if relative:
                    currenty=currenty+y
                else:
                    currenty=y
                ylist.append(currenty)
            elif ((cmd=='C') or (cmd=='S') or (cmd=='Q')):
                # Curve
                # TODO This could be innacurate,we are only basing on control points not the actual line
                # 'C' uses two control points,'S' and 'Q' use one
                if cmd=='C':
                    cpts=2
                else:
                    cpts=1
                # control points
                for i in range(0,cpts):
                    #print '  Control Point ',
                    x=float(tok.next())
                    y=float(tok.next())
                    #print 'xy=',x,y
                    if relative:
                        tmpx=currentx+x
                        tmpy=currenty+y
                    else:
                        tmpx=x
                        tmpy=y
                    xlist.append(tmpx)
                    ylist.append(tmpy)
                # final point is the real curve endpoint
                x=float(tok.next())
                y=float(tok.next())
                if relative:
                    currentx=currentx+x
                    currenty=currenty+y
                else:
                    currentx=x
                    currenty=y
                xlist.append(currentx)
                ylist.append(currenty)
            elif cmd=='A':
                # TODO implement arcs-punt for now
                # See http://www.w3.org/TR/SVG/paths.html#PathElement
                raise ValueError('Arc commands in a path are not currently handled')
            elif cmd=='Z':
                # No argumants to Z,and no new points
                # but we reset position to the beginning
                currentx=beginx
                currenty=beginy
                continue
            else:
                raise ValueError('Expected a command letter in path')
        except StopIteration:
            #print 'Done'
            # we're done
            break
    xmin=min(xlist)
    ymin=min(ylist)
    xmax=max(xlist)
    ymax=max(ylist)
    return xmin,ymin,xmax,ymax

def transformBoundingBox(xmin,ymin,xmax,ymax,transform):
    """
    Take a set of points representing a bounding box,and
    put them through a supplied transform,returning the result
    """
    if transform=='':
        return xmin,ymin,xmax,ymax
    new_xmin,new_ymin=transformPointXY(xmin,ymin,transform)
    new_xmax,new_ymax=transformPointXY(xmax,ymax,transform)
    return new_xmin,new_ymin,new_xmax,new_ymax

def extractMarkerId(markertext):
    # Regex -
    #<marker id=\"grainline_mk\"\nviewBox=
    # one or more WS,followed by 'id' followed by zero or more WS followed by '=' followed by zero or more WS,followed by '"',
    m=re.search('(\s+id\s*=\s*\"\w+\")',markertext,re.I)
    mid=m.group(0).split('"')[1]
    return mid

def drawPoints(parent,vdict):
    '''Create svg objects for the python objects listed in the dictionary. This function not necessary in Inkscape extensions.'''
    #print('Called drawPoints()')

    def getControlPoints(parent,key,val):
        #if object in val has c1 & c2 attributes
        if hasattr(val,'c1') and hasattr(val,'c2'):
            cPoint(parent,key+'.c1',getattr(val,'c1')) #create control point SVG object
            cPoint(parent,key+'.c2',getattr(val,'c2')) #creat control point SVG object
        return

    def getDartPoints(parent,name,pnt):
        #all darts have .o,.oc,.i,.ic,.m dynamic object attributes of class Pnt()
        for attrib in 'i','ic','o','oc','m':
            name1=name+'.'+attrib #'aD1.i','aD1.ic',etc.
            pnt1=getattr(pnt,attrib)
            pPoint(parent,name1,pnt1)
            getControlPoints(parent,name1,pnt1) # find & create control points SVG objects, if any
        return

    for key,val in vdict.iteritems():
        #print(key)
        if hasattr(val,'isCircle'):
            circle(parent,key,val)
        elif ('Letter' in parent.name) or ('letter' in parent.name):
            pPoint(parent,key,val)
            getControlPoints(parent,key,val)
        else:
            letter=parent.lettertext.lower()
            if key[0]==letter:
                #create svg pattern & control points
                if key[1].isdigit(): #a1,b3,...
                    pPoint(parent,key,val)
                    getControlPoints(parent,key,val)
                #create svg dart points
                elif key[1]=='D' and key[2].isdigit():
                    pPoint(parent,key,val) #aD1,bD1,...
                    getDartPoints(parent,key,val)
                elif 'apex' in key:
                    pPoint(parent,key,val) #a_apex,b_apex,...
    return


# ----------------...Connect 2 objects together using 2 points each...------------------------------

def connectObjects(connector_pnts,old_pnts):
        # connector_pnts[0] and old_pnts[0] will connect together
        # connector_pnts[1] and old_pnts[1] will connect together
        # connector_pnts[1] is counterclockwise from connector_pnts[0] on object which doesn't move
        # old_pnts[] contains all of the points of the object to be moved in order clockwise,starting with old_pnts[0]
        t_pnts=[] # translated points. 1st step.
        r_pnts=[] # translated points that are rotated. 2nd step.
        # translate so that old_pnts[0] will connect with connector_pnts[0]
        (dx,dy)=(connector_pnts[0].x-old_pnts[0].x),(connector_pnts[0].y-old_pnts[0].y)
        i=0
        for o in old_pnts:
            # translate all points in old_pnts[]
            t_pnts.append(Pnt())
            t_pnts[i].x,t_pnts[i].y=o.x+dx,o.y+dy
            i=i+1
        angle1=angleOfLine(connector_pnts[0],connector_pnts[1])
        angle2=angleOfLine(connector_pnts[0],t_pnts[1])
        rotation_angle=angle2-angle1 # subtract this angle from each angle of 2nd object's points towards connector0
        i=1 # don't rotate the 1st translated point,it should now be equal to connector0
        r_pnts.append(t_pnts[0])
        for t_pnt in t_pnts:
            if  (i !=len(t_pnts)):
                length=distance(connector_pnts[0],t_pnts[i])
                translated_angle=angleOfLine(connector_pnts[0],t_pnts[i])
                r_angle=translated_angle-rotation_angle
                r_pnts.append(Pnt())
                r_pnts[i]=polar(connector_pnts[0],length,r_angle)
                i=i+1
        return r_pnts

# ----Slash and spread with slash line,pivot point,and angle
def slashAndSpread(pivot,angle,*args):
        list=[]
        for arg in args:
            list.append(arg)
        i=0
        while (i<len(list)):
            pnt=list[i]
            length=distance(pivot,pnt)
            rotated_pnt=polar(pivot,length,angleOfLine(pivot,pnt)+angle) # angle>0=spread clockwise. angle<0=spread counterclockwise.
            updatePoint(pnt,rotated_pnt)
            i=i+1
        return

#---append points, lines and curves to paths---

def moveP(pathSVG,point,transform=''):
    """
    appendMoveToPath method
    """
    if (transform=='') :
        x,y=point.x,point.y
    else:
        x,y=transformPointXY(point.x,point.y,transform)
    return pathSVG.appendMoveToPath( x,y,relative=False)

def lineP(pathSVG,point,transform=''):
    """
    appendLineToPath method
    """
    if (transform=='') :
        x,y=point.x,point.y
    else:
        x,y=transformPointXY(point.x,point.y,transform)
    return pathSVG.appendLineToPath( x,y,relative=False)

def cubicCurveP(pathSVG,control1,control2,point,transform=''):
    """
    Accepts pathSVG,control1,control2,point and optional transform to call appendCubicCurveToPath method
    """
    if (transform=='') :
        c1x,c1y,c2x,c2y,px,py=control1.x,control1.y,control2.x,control2.y,point.x,point.y
    else:
        c1x,c1y=transformPointXY(control1.x,control1.y,transform)
        c2x,c2y=transformPointXY(control2.x,control2.y,transform)
        px,py=transformPointXY(point.x,point.y,transform)
    return pathSVG.appendCubicCurveToPath(c1x,c1y,c2x,c2y,px,py,relative=False)

def quadraticCurveP(pathSVG,control1,point,transform=''):
    """
    Accepts pathSVG,control1,point,& optional transform. Calls cubicCurveP with pathSVG,control1,control1,point,transform
    """
    return cubicCurveP(pathSVG,control1,control1,point,transform)

#---create paths---

def gridPath(name,label,pathSVG,transform=''):
    """
    Creates grid paths in reference group
    """
    return Path('reference',name,label,pathSVG,'gridline_style',transform)

def cuttingLinePath(name,label,pathSVG,transform=''):
    """
    Creates Cuttingline path in pattern group
    """
    return Path('pattern',name,label,pathSVG,'cuttingline_style',transform)

def seamLinePath(name,label,pathSVG,transform=''):
    """
    Creates Seamline path in pattern group
    """
    return Path('pattern',name,label,pathSVG,'seamline_style',transform)

def patternLinePath(name,label,pathSVG,transform=''):
    """
    Accepts name,label,svg path,transform. Returns path object using 'dartline_style'.
    Creates pattern line path in pattern group,other than cuttingline,seamline,or hemline-used for darts,etc.
    """
    return Path('pattern',name,label,pathSVG,'dartline_style',transform)

def stitchLinePath( name,label,pathSVG,transform='' ):
    """
    Creates stitch line in pattern group,other than cuttingline,seamline,or hemline
    """
    return Path('pattern',name,label,pathSVG,'dartline_style',transform)

def foldLinePath(name,label,pathSVG,transform='' ):
    """
    Creates fold line in pattern group,other than dartline,cuttingline,seamline,or hemline
    """
    return Path('pattern',name,label,pathSVG,'foldline_style',transform)

def grainLinePath(name,label,pnt1,pnt2,transform=''):
    """
    Creates grain line in pattern group
    """
    if (transform=='') :
        x1,y1=pnt1.x,pnt1.y
        x2,y2=pnt2.x,pnt2.y
    else:
        x1,y1=transformPointXY(pnt1.x,pnt1.y,transform)
        x2,y2=transformPointXY(pnt2.x,pnt2.y,transform)
    gline=Line("pattern",name,label,x1,y1,x2,y2,"grainline_style")
    gline.setMarker('Arrow1M',start=True,end=True)
    return gline

def addGridLine(parent,path):
    parent.add(Path('reference','gridline',parent.name+' Gridline',path,'gridline_style'))
    return

def addSeamLine(parent,path):
    parent.add(Path('pattern','seamline',parent.name+' Seamline',path,'seamline_style'))
    return

def addCuttingLine(parent,path):
    parent.add(Path('pattern','cuttingline',parent.name+' Cuttingline',path,'cuttingline_style'))
    return

def addGrainLine(parent,pnt1,pnt2):
    parent.add(grainLinePath('grainline',parent.name+' Grainline',pnt1,pnt2))
    return

def addFoldLine(parent,path):
    parent.add(foldLinePath('foldline',parent.name+' Foldline',path))
    return

def addDartLine(parent,path):
    parent.add(Path('pattern','dartline',parent.name+' Dartline',path,'dartline_style'))
    return

def addCenterLine(parent,path):
    parent.add(Path('pattern','centerline',parent.name+' Centerline',path,'dartline_style'))
    return

def addMarkingLine(parent,path):
    parent.add(Path('pattern','markingline',parent.name+' Markingline',path,'markingline_style'))
    return

def addFacingLine(parent,path):
    parent.add(Path('pattern','facingline',parent.name+' Facingline',path,'dartline_style'))
    return

def addToPath(p,*args):
    """
    Accepts a path object and a string variable containing a pseudo svg path using M,L,C and point objects.
    Calls functions to add commands and points to the path object
    """
    pnt=Pnt()
    tokens=[]
    for arg in args:
        tokens.append(arg)
    i=0
    while (i<len(tokens)):
        cmd=tokens[i]
        if (cmd=='M'):
            pnt=tokens[i+1]
            moveP(p,pnt)
            i=i+2
        elif (cmd=='L'):
            pnt=tokens[i+1]
            lineP(p,pnt)
            i=i+2
        elif (cmd=='C'):
            c1=tokens[i+1]
            c2=tokens[i+2]
            pnt=tokens[i+3]
            cubicCurveP(p,c1,c2,pnt)
            i=i+4
        else:
            print 'Unknown command token ' + cmd
    return

# ---- Set up pattern document with design info ----------------------------------------
def setupPattern(pattern_design,clientData,printer,patternData):
        pattern_design.cfg['clientdata']=clientData
        if (printer=='36" wide carriage plotter'):
            pattern_design.cfg['paper_width']=(36.0*IN)
        #set default border for document to allow printing
        pattern_design.cfg['border']=(2.5*CM)
        BORDER=pattern_design.cfg['border']
        #set data to print at top of pattern
        metainfo={'companyName':patternData['companyName'],#mandatory
                    'designerName':patternData['designerName'],#mandatory
                    'patternTitle':patternData['patternTitle'],#mandatory
                    'patternNumber':patternData['patternNumber'] #mandatory
                    }
        pattern_design.cfg['metainfo']=metainfo
        docattrs={'currentscale':"0.5:1",
                    'fitBoxtoViewport':"True",
                    'preserveAspectRatio':"xMidYMid meet",
                    }
        doc=Document(pattern_design.cfg,name='document',attributes=docattrs)
        doc.add(TitleBlock('notes','titleblock',0.0,0.0,stylename='titleblock_text_style'))
        doc.add(TestGrid('notes','testgrid',pattern_design.cfg['paper_width']/3.0,0.0,stylename='cuttingline_style'))
        return doc

# ---- Pattern Classes ----------------------------------------

class Node(pBase):
    """
    Create an instance which is only intended to be a holder for other objects
    """
    def __init__(self,name):
        self.name=name
        pBase.__init__(self)


class Pnt():
    '''Returns a Pnt object with .x,.y,and .name children'''
    def __init__(self,x=0.0,y=0.0,name='',size=''):
        self.x=x
        self.y=y
        self.name=name
        self.size=size


class PntP():
    '''Accepts no parameters, or optional Point or Pnt object. Returns a Pnt object with .x,.y,and .name children.  Does not create point in SVG document. Same as class Pnt()'''
    def __init__(self,pnt=Pnt(),name='',size=''):
        self.x=pnt.x
        self.y=pnt.y
        self.name=name
        self.size=size

class Circ():
    '''Returns a Circ object with .x,.y,and .name children'''
    def __init__(self,p1=Pnt(0,0),name='',size=''):
        self.x=p1.x
        self.y=p1.y
        self.name=name
        self.size=size
        self.isCircle=1

class Point(pBase):
    """
    Creates instance of Python class Point
    """
    def __init__(self,group,name,x=0,y=0,styledef='default',transform='',size=5) :

        self.groupname=group
        self.name=name
        self.sdef=styledef
        self.x=x
        self.y=y
        self.attrs={}
        self.attrs['transform']=transform
        self.size=size
        self.coords=str(x)+","+str(y)
        pBase.__init__(self)

    def add(self,obj):
        # Points don't have children. If this changes,change the svg and boundingbox methods also.
        raise RuntimeError('The Point class can not have children')

    def getsvg(self):
        """
        generate the svg for this item and return it as a pysvg object
        """
        if self.debug:
            print 'getsvg() called for Point ID ',self.id

        # an empty dict to hold our svg elements
        md=self.mkgroupdict()

        pstyle=PYB.StyleBuilder(self.styledefs[self.sdef])
        p=PYB.circle(self.x,self.y,self.size)
        p.set_style(pstyle.getStyle())
        p.set_id(self.id)
        if 'tooltips' in self.cfg:
            p.set_onmouseover('ShowTooltip(evt)')
            p.set_onmouseout('HideTooltip(evt)')

        for attrname,attrvalue in self.attrs.items():
            p.setAttribute(attrname,attrvalue)
        md[self.groupname].append(p)

        if 'circle' not in self.id: #circles get a separate point in the middle with text id, this would be redundant
            txtlabel=self.id+'.text'
            txttxt=self.name
            if '_c' in txttxt:
                txtstyle='control_point_text_style'
            else:
                txtstyle='point_text_style'
            txt=self.generateText(self.x+7,self.y-7,txtlabel,txttxt,txtstyle)
            md[self.groupname].append(txt)

        return md

    def boundingBox(self,grouplist=None):
        """
        Return two points which define a bounding box around the object
        """
        if grouplist is None:
            grouplist=self.groups.keys()
        if self.groupname in grouplist:
            (x1,y1)=(self.x-(self.size/2.0),self.y-(self.size/2.0))
            (x2,y2)=(self.x+(self.size/2.0),self.y+(self.size/2.0))
            return x1,y1,x2,y2
        else:
            return None,None,None,None

class Line(pBase):
    """
    Creates instance of Python class Line
    """
    def __init__(self,group,name,label,xstart,ystart,xend,yend,styledef='default',transform='') :

        self.groupname=group
        self.name=name
        self.sdef=styledef
        self.label=label
        self.xstart=xstart
        self.ystart=ystart
        self.xend=xend
        self.yend=yend
        self.attrs={}
        self.attrs['transform']=transform
        # make some checks
        if self.sdef not in self.styledefs:
            raise ValueError("Style %s was specified but isn't defined" % self.sdef)
        pBase.__init__(self)

    def setMarker(self,markername=None,start=True,end=True):

        if markername not in self.markerdefs:
            raise ValueError("Marker %s was specified but isn't defined" % markername)
        else:
            # List it as used so we put it in the output file
            if markername not in self.markers:
                self.markers.append(markername)
            if type(self.markerdefs[markername]) is str:
                # This is a plain marker,not start,end or mid markers in a dict
                if start:
                    startMarkID=extractMarkerId(self.markerdefs[markername])
                    self.attrs['marker-start']="url(#%s)" % startMarkID
                if end:
                    endMarkID=extractMarkerId(self.markerdefs[markername])
                    self.attrs['marker-end']="url(#%s)" % endMarkID
            elif type(self.markerdefs[markername]) is dict:
                # Extract start and end as needed
                if start:
                    startMarkID=extractMarkerId(self.markerdefs[markername]['start'])
                    self.attrs['marker-start']="url(#%s)" % startMarkID
                if end:
                    endMarkID=extractMarkerId(self.markerdefs[markername]['end'])
                    self.attrs['marker-end']="url(#%s)" % endMarkID
            else:
                raise ValueError('marker %s is an unexpected type of marker' % markername)

    def add(self,obj):
        # Lines don't have children. If this changes,change the svg method also.
        raise RuntimeError('The Line class can not have children')

    def getsvg(self):
        """
        generate the svg for this item and return it as a pysvg object
        """
        if self.debug:
            print 'getsvg() called for Line ID ',self.id

        # an empty dict to hold our svg elements
        md=self.mkgroupdict()

        pstyle=PYB.StyleBuilder(self.styledefs[self.sdef])
        p=PYB.line(self.xstart,self.ystart,self.xend,self.yend)
        p.set_style(pstyle.getStyle())
        p.set_id(self.id)
        for attrname,attrvalue in self.attrs.items():
            p.setAttribute(attrname,attrvalue)
        md[self.groupname].append(p)

        return md

    def boundingBox(self,grouplist=None):
        """
        Return two points which define a bounding box around the object
        """
        if grouplist is None:
            grouplist=self.groups.keys()
        #if self.groupname in grouplist:
            #print '         end pattern.Line.boundingBox(',self.name,')-returning (xmin:',min(self.xstart,self.xend),' ymin:',min(self.ystart,self.yend) ,') ( xmax:',max(self.xstart,self.xend),' ymax:',max(self.ystart,self.yend),')'
            #return (min(self.xstart,self.xend),min(self.ystart,self.yend),max(self.xstart,self.xend),max(self.ystart,self.yend))
        #else:
            #print '         end pattern.Line.boundingBox(',self.name,')-returning (None,None,None,None)'
            #return None,None,None,None
        if self.groupname in grouplist:
            dd='M '+str(self.xstart)+' '+str(self.ystart)+' L '+str(self.xend)+' '+str(self.yend)
            xmin,ymin,xmax,ymax=getBoundingBox(dd)
            return xmin,ymin,xmax,ymax
        else:
            return None,None,None,None

class Path(pBase):
    """
    Creates instance of Python class Path
    Holds a path object and applies grouping,styles,etc when drawn
    """
    def __init__(self,group,name,label,pathSVG,styledef='default',transform='') :

        self.groupname=group
        self.name=name
        self.label=label
        self.sdef=styledef
        self.pathSVG=pathSVG
        self.attrs={}
        self.attrs['transform']=transform

        pBase.__init__(self)

    def setMarker(self,markername=None,start=True,end=True,mid=True):

        if markername not in self.markerdefs:
            print 'Markerdefs:',self.markerdefs
            raise ValueError("Marker %s was specified but isn't defined" % markername)
        else:
            # List it as used so we put it in the output file
            if markername not in self.markers:
                self.markers.append(markername)

            if type(self.markerdefs[markername]) is str:
                # This is a plain marker,not start,end or mid markers in a dict
                if start:
                    markID=extractMarkerId(self.markerdefs[markername])
                    self.attrs['marker-start']="url(#%s)" % markID
                if end:
                    markID=extractMarkerId(self.markerdefs[markername])
                    self.attrs['marker-end']="url(#%s)" % markID
                if mid:
                    markID=extractMarkerId(self.markerdefs[markername])
                    self.attrs['marker-mid']="url(#%s)" % markID
            elif type(self.markerdefs[markername]) is dict:
                # Extract start and end as needed
                if start:
                    markID=extractMarkerId(self.markerdefs[markername]['start'])
                    self.attrs['marker-start']="url(#%s)" % markID
                if end:
                    markID=extractMarkerId(self.markerdefs[markername]['end'])
                    self.attrs['marker-end']="url(#%s)" % markID
                if mid:
                    if 'mid' not in self.markerdefs[markername]:
                        # TODO Not sure whether this should be an exception,
                        # or just print a warning and not set mid markers
                        raise ValueError()
                    markID=extractMarkerId(self.markerdefs[markername]['mid'])
                    self.attrs['marker-mid']="url(#%s)" % markID
            else:
                raise ValueError('marker %s is an unexpected type of marker' % markername)

    def add(self,obj):
        # Paths don't have children. If this changes,change the svg method also.
        raise RuntimeError('The Path class can not have children')

    def getsvg(self):
        """
        generate the svg for this item and return it as a pysvg object
        """
        if self.debug:
            print 'getsvg() called for Line ID ',self.id

        try:
            # an empty dict to hold our svg elements
            md=self.mkgroupdict()

            pstyle=PYB.StyleBuilder(self.styledefs[self.sdef])

            self.pathSVG.set_id(self.id)
            self.pathSVG.set_style(pstyle.getStyle())
            for attrname,attrvalue in self.attrs.items():
                self.pathSVG.setAttribute(attrname,attrvalue)
            md[self.groupname].append(self.pathSVG)
        except:
            print '************************'
            print 'Exception in element',self.id
            print '************************'
            raise

        return md

    def boundingBox(self,grouplist=None):
        """
        Return two points which define a bounding box around the object
        """
        # This is not elegant,should perhaps be redone
        if grouplist is None:
            grouplist=self.groups.keys()
        if self.groupname in grouplist:
            dd=self.pathSVG.get_d()
            xmin,ymin,xmax,ymax=getBoundingBox(dd)
            return xmin,ymin,xmax,ymax
        else:
            return None,None,None,None

class TextBlock(pBase):
    """Creates instance of Python class TextBlock"""
    def __init__(self,group,name,headline,x,y,text,textstyledef='default_textblock_text_style',boxstyledef=None,transform=''):
        self.groupname=group
        self.name=name
        self.text=text
        self.textsdef=textstyledef
        self.boxsdef=boxstyledef
        self.headline=headline
        self.x=x
        self.y=y
        self.attrs={}
        self.attrs['transform']=transform

        pBase.__init__(self)

    def add(self,obj):
        # Text Blocks don't have children. If this changes,change the svg method also.
        raise RuntimeError('The TextBlock class can not have children')

    def getsvg(self):
        """
        generate the svg for this item and return it as a pysvg object
        """
        if self.debug:
            print 'getsvg() called for TextBlock ID ',self.id

        # an empty dict to hold our svg elements
        md=self.mkgroupdict()

        # create the text first
        tg=PYB.g()
        tg.set_id(self.id)
        x=self.x
        y=self.y

        if self.text is None:
            if self.debug:
                print '  TextBlock special case for pattern letter,getting text from parent'
            label=self.id+'.letterline'
            # TODO possibly check type of parent object to make sure it's a PatternPiece
            txt=self.generateText(x,y,label,self.parent.lettertext,self.textsdef)
            tg.addElement(txt)
        else:
            # this is a bit cheesy
            spacing=( int(self.styledefs[self.textsdef]['font-size'])*1.2 )
            line=1
            for line in self.text:
                label=self.id+'.line'+str(line)
                txt=self.generateText(x,y,label,line,self.textsdef)
                y=y+spacing
                tg.addElement(txt)

        # if headline is None,then don't print it or space for it
        # if boxstyledef is none,then no box

        # TODO getting element sizes is note yet supported in pySVG,
        # so we'll do the outline box and headline later
        for attrname,attrvalue in self.attrs.items():
            tg.setAttribute(attrname,attrvalue)
        md[self.groupname].append(tg)

        return md

class PatternPiece(pBase):
    """
    Create an instance of the PatternPiece class,eg jacket.back,pants.frontPocket,corset.stayCover
    which will contain the set of seams and all other pattern piece info,
    eg-jacket.back.seam.shoulder,jacket.back.grainline,jacket.back.interfacing
    """
    def __init__(self,group,name,lettertext='?',fabric=0,interfacing=0,lining=0):
        self.name=name
        self.groupname=group
        self.width=0
        self.height=0
        self.labelx=0
        self.labely=0
        self.lettertext=lettertext
        self.fabric=fabric
        self.interfacing=interfacing
        self.lining=lining
        self.attrs={}
        self.attrs['transform']=''
        pBase.__init__(self)

    def getsvg(self):
        """
        generate the svg for this patternpiece and return it in a dictionary of groups which contain the svg objects
        """
        if self.debug:
            print 'getsvg() called for PatternPiece ID ',self.id

        # generate the label from information which is part of the pattern piece
        self.makeLabel()

        child_group_dict=pBase.getsvg(self) # call the baseclass svg method on this pattern piece. Returns a dictionary of all groups to be drawn.

        for child_group_name,members in child_group_dict.items():# for each group used in this pattern piece
            if self.debug:
                print 'self.id =',self.id,'child_group_name =',child_group_name
                print '++ Group ==',child_group_name,' in pattern.PatternPiece.getsvg()'

            # create a temporary pySVG group object
            temp_group=PYB.g()

            # assign temp group a unique id
            try:
                grpid=self.id+'.'+child_group_name
            except:
                print 'self.id =',self.id,'child_group_name =',child_group_name,'in pattern.PatternPiece.getsvg()'
            temp_group.set_id(grpid)

            # temp group gets all patternpiece's attributes
            for attrname,attrvalue in self.attrs.items():
                temp_group.setAttribute(attrname,attrvalue)
            # and all patternpiece's child elements
            for cgitem in child_group_dict[child_group_name]:
                temp_group.addElement(cgitem)

            # Add temp group to a temp list (list will have only one item)
            temp_group_list=[]
            temp_group_list.append(temp_group)
            # Replace dictionary entry for this group with the temp list
            child_group_dict[child_group_name]=temp_group_list

        return child_group_dict

    def setLetter(self,x=None,y=None,style='default_letter_text_style',text=None,scaleby=None):
        # text=None is a flag to get the letter from the pattern piece at draw time
        if scaleby is not None:
            tform=scaleAboutPointTransform(x,y,scaleby)
        else:
            tform=''
        tb=TextBlock('pattern','letter',None,x,y,text,textstyledef=style,transform=tform)
        self.add(tb)

    def makeLabel(self):
        """
        Create a label block for display on the pattern piece,which contains
        information like pattern number,designer name,logo,etc
        """
        text=[]
        mi=self.cfg['metainfo']

        text.append(mi['companyName'])

        text.append('Designer:%s' % mi['designerName'])
        text.append('Client:%s' % self.cfg['clientdata'].customername)
        text.append(mi['patternNumber'])
        text.append('Pattern Piece %s' % self.lettertext)
        if self.fabric>0:
            text.append('Cut %d Fabric' % self.fabric)
        if self.interfacing>0:
            text.append('Cut %d Interfacing' % self.interfacing)

        #def __init__(group,name,headline,x,y,text,textstyledef='default_textblock_text_style',boxstyledef=None,transform=''):
        tb=TextBlock('pattern','info','Headline',self.label_x,self.label_y,text,'default_textblock_text_style','textblock_box_style')
        self.add(tb)

        return

    def boundingBox(self,grouplist=None):
        """
        Return two points which define a bounding box around the object
        """
        # get all the children
        xmin,ymin,xmax,ymax=pBase.boundingBox(self,grouplist)
        xmin,ymin,xmax,ymax=transformBoundingBox(xmin,ymin,xmax,ymax,self.attrs['transform'])

        return xmin,ymin,xmax,ymax

class Pattern(pBase):
    """
    Create an instance of Pattern class,eg-jacket,pants,corset,which will contain the set of pattern piece objects-eg  jacket.back,pants.frontPocket,corset.stayCover
    A pattern does not generate any svg itself,output is only generated by children objects
    """
    def __init__(self,name):
        self.name=name
        pBase.__init__(self)

    def autolayout(self):
        """
        find out the bounding box for each pattern piece in this pattern,then make them fit within the
        width of the paper we're using
        """

        # get a collection of all the parts,we'll sort them before layout
        parts={}
        for chld in self.children:
            if isinstance(chld,PatternPiece):
                #print 'Pattern.py calling ',chld.name,'.boundingBox()'
                xlo,ylo,xhi,yhi=chld.boundingBox()
                #print 'Pattern.py -',chld.name,'.boundingBox() returned info[xlo]:',xlo,'info[ylo]:',ylo,'info[xhi]:',xhi,'info[yhi]:',yhi
                parts[chld]={}
                parts[chld]['xlo']=xlo
                parts[chld]['ylo']=ylo
                parts[chld]['xhi']=xhi
                parts[chld]['yhi']=yhi

        # our available paper width is reduced by twice the border
        #print self.cfg['paper_width']
        pg_width=self.cfg['paper_width']-(2*self.cfg['border'])
        if 'verbose' in self.cfg:
            print 'Autolayout:'
            print ' total paperwidth=',self.cfg['paper_width']
            print ' border width=',self.cfg['border']
            print ' available paperwidth=',pg_width
            print ' pattern offset=',PATTERN_OFFSET

        next_x=SEAM_ALLOWANCE
        # -spc- FIX Leave room for the title block!
        next_y=6.0*IN_TO_PT # this should be zero
        #next_y=0 # this should be zero
        max_height_this_row=0
        # a very simple algorithm

        # we want to process these in alphabetical order of part letters
        index_by_letter={}
        letters=[]
        for pp,info in parts.items():
            letter=pp.lettertext
            if letter in index_by_letter:
                raise ValueError('The same Pattern Piece letter<%s> is used on more than one pattern piece' % letter)
            index_by_letter[letter]=pp
            letters.append(letter)

        # sort the list
        letters.sort()

        for thisletter in letters:
            #print 'thisletter =',thisletter
            pp=index_by_letter[thisletter]
            #print 'pp=',pp
            info=parts[pp]
            pp_width=info['xhi']-info['xlo']
            pp_height=info['yhi']-info['ylo']

            if 'verbose' in self.cfg:
                print '   Part letter:',thisletter
                print '     part width=pp_width:',pp_width,'<-- info[xhi]:',info['xhi'],'-info[xlo]:',info['xlo']
                print '     part height=pp_height:',pp_height,'<-- info[yhi]:',info['yhi'],'-info[ylo]:',info['ylo']
                print '     current x=next_x:',next_x
                print '     current y=next_y:',next_y

            if pp_width>pg_width:
                print 'Error:Pattern piece<%s> is too wide to print on page width' % pp.name
                # TODO:-figure out something smarter
                ## raise

            if next_x+pp_width>pg_width:
                # start a new row
                real_next_y=next_y+max_height_this_row+PATTERN_OFFSET
                if 'verbose' in self.cfg:
                    print '     Starting new row,right side of piece would have been=',next_x+pp_width
                    print '     New x=0'
                    print '     Previous y=next_y:',next_y
                    print '     New y=real_next_y:',real_next_y,'<-- (next_y:',next_y,'+max_height_this_row:',max_height_this_row,'+PATTERN_OFFSET:',PATTERN_OFFSET,')'
                    print '     New max_height_this_row=pp_height:',pp_height
                next_y=real_next_y
                max_height_this_row=pp_height
                next_x=0
            else:
                if pp_height>max_height_this_row:
                    max_height_this_row=pp_height
                    if 'verbose' in self.cfg:
                        print'       Previous y=next_y:',next_y
                        print'       New y=Previous y'
                        print'       New max_height_this_row=pp_height:',pp_height
            # now set up a transform to move this part to next_x,next_y
            xtrans=(next_x-info['xlo'])
            ytrans=(next_y-info['ylo'])
            pp.attrs['transform']=pp.attrs['transform']+(' translate(%f,%f)' % (xtrans,ytrans))
            if 'verbose' in self.cfg:
                print '     Transform=translate(xtrans:',xtrans,',ytrans:',ytrans,')<-- (next_x:',next_x,'- info[xlo]:',info['xlo'],'),next_y:',next_y,'- info[ylo]:',info['ylo'],')'
                print '     New x is next_x:',next_x+pp_width+PATTERN_OFFSET,'<--(next_x:',next_x,'+ppwidth:',pp_width,'+PATTERN_OFFSET:',PATTERN_OFFSET,')'
            next_x=next_x+pp_width+PATTERN_OFFSET
        if 'verbose' in self.cfg:
            print 'Autolayout END'
        return

    def getsvg(self):
        # Automatically change pattern piece locations as needed
        self.autolayout()
        # Now call the base class method to assemble the SVG for all my children
        return pBase.getsvg(self)
