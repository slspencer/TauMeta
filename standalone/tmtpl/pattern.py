#!/usr/bin/python
#
# This file is part of the tmtp (Tau Meta Tau Physica) project.
# For more information,see http://www.sew-brilliant.org/
#
# Copyright (C) 2010,2011,2012 Susan Spencer and Steve Conklin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation,either version 3 of the License,or
# (at your option) any later version. Attribution must be given in
# all derived works.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not,see <http://www.gnu.org/licenses/>.

#python libs
import math
import string
import re
import random
import inspect
from math import sin,cos,pi,sqrt,asin

#pysvg libs
import pysvg.builders as PYB

# tmtp libs
from constants import *
from utils import debug
from document import *


# ---- Pattern methods ----------------------------------------
#
# A lot of these depend on the classes in this file,so we put them here

# ----------------...Create Points..------------------------------

def pPoint(x,y):
    '''Undrawn point to use in pattern calculations.
    Accepts x,y and returns an object of class Pnt. Does not create an SVG point'''
    pnt=Pnt(x,y)
    return pnt

def pPointP(pnt1):
    '''Accepts an object of class Point or Pnt (can be from another calculation).
    Returns an object of class Pnt - Does not create an SVG point.'''
    pnt=Pnt(pnt1.x,pnt1.y)
    return pnt

def rPoint(parent,id,x,y,transform=''):
    '''Accepts parent object,id,x,y,& optional transform. Returns object of class Point.
    Creates SVG red dot in reference group for pattern calculation point.'''
    pnt=Point('reference',id,x,y,'point_style',transform)
    parent.add(pnt)
    return pnt

def rPointP(parent,id,pnt,transform=''):
    '''Accepts parent object,id,point object (can be from another calculation),and optional transform.
    Returns object of class Point. Creates SVG red dot in reference group for pattern calculation point.'''
    return rPoint(parent,id,pnt.x,pnt.y,transform='')

def cPoint(parent,id,x,y,transform=''):
    '''Accepts parent object,id,x,y,and optional transform. Returns object of class Point.
    Creates SVG blue open dot in reference group to display control point in bezier curves.'''
    pnt=Point('reference',id, x, y, 'controlpoint_style',transform)
    parent.add(pnt)
    return pnt

def cPointP(parent,id,pnt,transform=''):
    '''Accepts parent object,id,point object (can be from another calculation),and optional transform.
    Returns object of class Point. Creates SVG blue open dot in reference group for control point in bezier curves.'''
    return cPoint(parent,id,pnt.x,pnt.y,transform='')

def updatePoint(pnt,new_pnt):
    '''Accepts two point objects.  The 1st point's .x & .y is updated with 2nd point's x & y values.'''
    pnt.x,pnt.y,pnt.coords=new_pnt.x,new_pnt.y,str(new_pnt.x)+','+str(new_pnt.y)
    return

# ----------------...Add Points to Paths..------------------------------

def moveP(pathSVG,point,transform=''):
    """
    appendMoveToPath method
    """
    if (transform == '') :
        x,y=point.x, point.y
    else:
        x,y=transformPoint(point.x,point.y,transform)
    return pathSVG.appendMoveToPath( x,y,relative=False)

def lineP(pathSVG,point, transform=''):
    """
    appendLineToPath method
    """
    if (transform == '') :
        x,y=point.x, point.y
    else:
        x,y=transformPoint(point.x,point.y,transform)
    return pathSVG.appendLineToPath( x,y, relative=False)

def cubicCurveP(pathSVG,control1,control2,point,transform=''):
    """
    Accepts pathSVG,control1,control2,point and optional transform to call appendCubicCurveToPath method
    """
    if (transform == '') :
        c1x,c1y,c2x,c2y,px,py=control1.x,control1.y,control2.x, control2.y,point.x,point.y
    else:
        c1x,c1y=transformPoint(control1.x,control1.y,transform)
        c2x,c2y=transformPoint(control2.x,control2.y,transform)
        px, py=transformPoint(point.x,point.y,transform)
    return pathSVG.appendCubicCurveToPath(c1x,c1y,c2x,c2y,px,py,relative=False)

def quadraticCurveP(pathSVG,control1,point,transform=''):
    """
    Accepts pathSVG,control1,point,& optional transform. Calls cubicCurveP with pathSVG,control1,control1,point,transform
    """
    return cubicCurveP(pathSVG,control1,control1,point,transform)

# ----------------...Create Paths..------------------------------

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
    Creates pattern line path in pattern group,other than cuttingline,seamline,or hemline - used for darts,etc.
    """
    return Path('pattern',name,label,pathSVG,'dartline_style',transform)

def stitchLinePath( name,label, pathSVG,transform='' ):
    """
    Creates stitch line in pattern group,other than cuttingline,seamline,or hemline
    """
    return Path('pattern',name,label,pathSVG,'dartline_style',transform)

def foldLinePath(name,label,pathSVG,transform='' ):
    """
    Creates fold line in pattern group,other than dartline,cuttingline,seamline,or hemline
    """
    return Path('pattern',name,label,pathSVG,'foldline_style',transform)

def grainLinePath(name,label,pnt1,pnt2, transform=''):
    """
    Creates grain line in pattern group
    """
    if (transform == '') :
        x1,y1=pnt1.x, pnt1.y
        x2,y2=pnt2.x, pnt2.y
    else:
        x1,y1=transformPoint(pnt1.x,pnt1.y,transform)
        x2,y2=transformPoint(pnt2.x,pnt2.y,transform)
    gline=Line("pattern",name,label,x1,y1,x2,y2,"grainline_style")
    gline.setMarker('Arrow1M',start=True,end=True)
    return gline

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
    while (i < len(tokens)):
        cmd=tokens[i]
        if (cmd == 'M'):
            pnt=tokens[i+1]
            moveP(p,pnt)
            i=i+2
        elif (cmd=='L'):
            pnt=tokens[i+1]
            lineP(p,pnt)
            i=i+2
        elif (cmd == 'C'):
            c1=tokens[i+1]
            c2=tokens[i+2]
            pnt=tokens[i+3]
            cubicCurveP(p,c1,c2,pnt)
            i=i+4
        else:
            print 'Unknown command token'
    return

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

# ----------------...Calculate Angle and Slope..------------------------------

def slopeOfLine(x1,y1,x2,y2):
    """ Accepts two sets of coordinates x1,y1,x2,y2 and returns the slope   """
    if (x2 <> x1):
        m=(y2 - y1)/(x2 - x1)
    else:
        print 'Vertical Line'
        m=None
    return m

def slopeOfLineP(P1,p2):
    """ Accepts two point objects and returns the slope """
    if ((p2.x - p1.x) <> 0):
        m=(p2.y - p1.y)/(p2.x - p1.x)
    else:
        print 'Vertical Line'
        m=None
    return m

def degreeOfAngle(angle):
    return angle*180.0/math.pi

def angleOfDegree(degree):
    return degree*math.pi/180.0

def angleOfSlope(x1,y1,x2,y2):
    """Accepts two sets of coordinates x1,y1,x2,y2 inputs and returns angle in radians. Uses atan2.   """
    rise=y2 - y1
    run=x2 - x1
    return math.atan2(rise,run )

def angleOfSlopeP(pnt1,pnt2):
    return angleOfSlope(pnt1.x,pnt1.y,pnt2.x,pnt2.y)

def angleOfLine(x1,y1,x2,y2):
    """ Accepts two sets of coordinates x1,y1,x2,y2 and returns the angle of the vector between them. Uses atan2.   """
    return math.atan2(y2 - y1,x2 - x1)

def angleOfLineP(p1,p2):
    """ Accepts two point objects and returns the angle of the vector between them. Calls angleOfLine(x1,y1,x2,y2)"""
    return angleOfLine(p1.x,p1.y,p2.x,p2.y)

def angleOfVectorP(p1,v,p2):
    #L1=distanceP(p1,p2)
    #L2=distanceP(p1,p3)
    #L3=distanceP(p2,p3)
    #return math.acos((L1**2+L2**2 - L3**2)/(2*L1*L2))
    return abs(angleOfLineP(v,p1) - angleOfLineP(v,p2))

def rightPointP(p1,n):
    pnt=Pnt(p1.x+n,p1.y)
    return pnt

def leftPointP(p1,n):
    pnt=Pnt(p1.x - n,p1.y)
    return pnt

def upPointP(p1,n):
    pnt=Pnt(p1.x,p1.y - n)
    return pnt

def downPointP(p1,n):
    pnt=Pnt(p1.x,p1.y+n)
    return pnt

def symmetricPointP(p1,p2,type):
    ''' Accepts p1 point to copy,p2 as reference point,type {'vertical','horizontal'}
    Copy p1 symmetrical to vertical line x=p2.x or horizontal line y=p2.y.
    Returns pnt which is mirror image of p1'''
    pnt=Pnt()
    dx=p2.x - p1.x
    dy=p2.y - p1.y
    if (type == 'vertical'):
        pnt.x=p2.x+dx
        pnt.y=p1.y
    elif (type == 'horizontal'):
        pnt.x=p1.x
        pnt.y=p2.y+dy
    return pnt


# ----------------...Calculate points with Angle and Slope..------------------------------

def xyPolarPoint(x1,y1,distance,angle):
    # http://www.teacherschoice.com.au/maths_library/coordinates/polar_-_rectangular_conversion.htm
    r=distance
    x=x1+(r*cos(angle))
    y=y1+(r*sin(angle))
    return (x ,y )

def xyPolarPointP(pnt,distance,angle):
    x,y=xyPolarPoint(pnt.x,pnt.y,distance,angle)
    return (x,y)

def polarPoint(x1,y1,distance,angle):
    pnt1=Pnt()
    pnt1.x,pnt1.y=xyPolarPoint(x1,y1,distance,angle)
    return pnt1

def polarPointP(pnt,distance,angle):
    pnt1=Pnt()
    pnt1.x,pnt1.y=xyPolarPoint(pnt.x,pnt.y,distance,angle)
    return pnt1

def xyOnLine(x1,y1,x2,y2,distance,rotation=0):
    """
    Accepts two pairs of coordinates x1,y1,x2,y2 and an optional rotation angle
    Returns x,y measured from x1,y1 towards x2,y2
    Negative distance returns x,y measured in opposite direction
    The point is optionally rotated about the first point by the rotation angle in degrees
    """
    lineangle=angleOfLine(x1,y1,x2,y2)
    angle=lineangle+(rotation*(math.pi/180))
    x=(distance*math.cos(angle))+x1
    y=(distance*math.sin(angle))+y1
    return (x,y)

def xyOnLineP(p1,p2,distance,rotation=0):
    """
    Accepts two points p1,p2 and an optional rotation angle
    Returns x,y values on the line measured from p1
    the point is optionally rotated about the first point by the rotation angle in degrees
    """
    x,y=xyOnLine(p1.x,p1.y,p2.x,p2.y,distance,rotation)
    return (x,y)

def pntOnLine(x1,y1,x2,y2,distance,rotation=0):
    """
    Accepts x1,y1,x2,y2 and an optional rotation angle
    Returns a point object pnt on the line measured from x1,y1 towards x2,y2
    the point is optionally rotated about the first point by the rotation angle in degrees
    """
    pnt=Pnt()
    pnt.x,pnt.y=xyOnLine(x1,y1,x2,y2,distance,rotation)
    return pnt

def pntOnLineP(p1,p2,distance,rotation=0):
    """
    Accepts two points p1,p2 and an optional rotation angle. Returns a point object on the line,measured from p1,towards p2
    the point is optionally rotated about the first point by the rotation angle in degrees
    """
    pnt=Pnt()
    pnt.x,pnt.y=xyOnLine(p1.x,p1.y,p2.x,p2.y,distance,rotation)
    return pnt

def xyOffLine(x1,y1,x2,y2,distance,rotation=0):
    """
    Accepts two point objects and an optional rotation angle,returns x,y
    Returns x,y values away from the line,measured from p1,opposite direction from p2
    the point is optionally rotated about the first point by the rotation angle in degrees
    """
    (x,y)=xyOnLine(x1,y1,x2,y2,-distance,rotation)
    return (x,y)

def xyOffLineP(p1,p2,distance,rotation=0):
    """
    Accepts two point objects and an optional rotation angle,returns x,y
    Returns x,y values away from the line,measured from p1,away from p2
    the point is optionally rotated about the first point by the rotation angle in degrees
    """
    (x,y)=xyOffLine(p1.x,p1.y,p2.x,p2.y,distance,rotation)
    return (x,y)

def pntOffLine(x1,y1,x2,y2,distance,rotation=0):
    """
    Accepts x1,y1,x2,y2 and an optional rotation angle
    Returns a point object pnt,measured from p1,opposite direction from p2
    the point is optionally rotated about the first point by the rotation angle in degrees
    """
    pnt=Pnt()
    pnt.x,pnt.y=xyOffLine(x1,y1,x2,y2,distance,rotation)
    return pnt

def pntOffLineP(p1,p2,distance,rotation=0):
    """
    Accepts two points and an optional rotation angle
    Returns a point object pnt,measured from p1,away from p2
    the point is optionally rotated about the first point by the rotation angle in degrees
    """
    pnt=Pnt()
    pnt.x,pnt.y=xyOffLine(p1.x,p1.y,p2.x,p2.y,distance,rotation)
    return pnt

# ----------------...Calculate Midpoints on line..------------------------------

def xyMidPoint(x1,y1,x2,y2,n=0.5):
    '''Accepts x1,y1,x2,y2 and 0<n<1,returns x,y'''
    return (x1+x2)*n, (y1+y2)*n

def xyMidPointP(p1,p2,n=0.5):
    '''Accepts p1 & p2 and 0<n<1,returns x,y'''
    return xyMidPoint(p1.x, p1.y, p2.x, p2.y,n)

def pntMidPoint(x1,y1,x2,y2,n=0.5):
    '''Accepts x1,y1,x2,y2 and 0<n<1,returns pnt'''
    #TODO - fix nomenclature of functions - pMidPointP should be pntMidpointP,etc...or pMidpointP - for all functions
    pnt=Pnt()
    pnt.x,pnt.y=xyMidPoint(x1,y1,x2,y2,n)
    return pnt

def pntMidPointP( p1,p2,n=0.5):
    '''Accepts p1 & p2 and 0<n<1,returns p3'''
    pnt=Pnt()
    pnt.x, pnt.y=xyMidPointP(p1,p2,n)
    return pnt

# ----------------...Calculate intercepts given x or y..------------------------------

def pntOnLineAtXP(p1,p2,x):
    #on line p1-p2, given x find y
    pnt=Pnt()
    pnt.x=x
    if (p1.x == p2.x): # vertical line
        print  'infinite values of y on vertical line'
        return None
    else:
        m=(p1.y - p2.y)/(p1.x-p2.x)
        b=p2.y - (m*p2.x)
        pnt.y=(x*m)-b
        return pnt

def pntOnLineAtYP(p1,p2,y):
    #on line p1-p2,find x given y
    pnt=Pnt()
    pnt.y=y
    if (p1.y == p2.y) and (p1.y != y): # if horizontal line,and value y is different than horizontal line's y
        print 'y=',y,' not on line'
        return None
    elif (p1.x != p2.x): # if not vertical line
        m=(p1.y - p2.y)/(p1.x-p2.x)
        b=p2.y - (m*p2.x)
        pnt.x=(y - b)/m
    else: # if vertical line
        pnt.x=p1.x
    return pnt

def pntOnCircleAtY(C,r,y):
    """
    Finds points one or two points on circle where P.y=y
    Accepts circle center point object C,radius r,and value y
    Returns an object P with number of intersection points,and up to two coordinate pairs.
    Based on paulbourke.net/geometry/sphereline/sphere_line_intersection.py,written in Python 3.2 by Campbell Barton
    """

    if abs(y - C.y) > r:

        print 'y is beyond radius in pntOnCircleAtY()'
        return

    else:

        translated_y=y - C.y
        translated_x1=abs(math.sqrt(r**2 - translated_y**2))
        translated_x2=-translated_x1

        x1=translated_x1+C.x
        x2=translated_x2+C.x

        P=Pnt()
        P.p1=Pnt(x1,y)
        P.p2=Pnt(x2,y)

    return P

def pntOnCircleAtX(C,r,x):
    """
    Finds points one or two points on circle where p.x=x
    Accepts circle center point object C,radius r,and value x
    Returns an object P with number of intersection points,and up to two coordinate pairs.
    """

    if abs(x - C.x) > r:

        print 'x is beyond radius in pntOnCircleAtX()'
        return

    else:

        translated_x=x - C.x
        translated_y1=abs(math.sqrt(r**2 - translated_x**2))
        translated_y2=-translated_y1

        y1=translated_y1+C.y
        y2=translated_y2+C.y

        P=Pnt()
        P.p1=Pnt(x,y1)
        P.p2=Pnt(x,y2)

    return P


def pntsOnCurveAtX(curve, x):
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
    while j <= len(curve)  - 4:  # for each bezier curve in curveArray

        interpolatedPoints=interpolateCurve(curve[j],curve[j+1],curve[j+2],curve[j+3],100)  #interpolate this bezier curve,n=100

        # get min & max for x & y for this bezier curve from its interpolated points
        i=0
        while (i < len(interpolatedPoints)):
            xlist.append(interpolatedPoints[i].x)
            ylist.append(interpolatedPoints[i].y)
            i=i+1
        xmin,ymin,xmax,ymax=min(xlist), min(ylist), max(xlist), max(ylist)
        print 'xmin,xmax =',xmin,xmax,'...pattern.pntsOnCurveAtX()'
        print 'ymin,ymax =',ymin,ymax,'...pattern.pntsOnCurveAtX()'
        print 'x =',x,'...pattern.pntsOnCurveAtX()'

        i=0
        if ((x >= xmin) and (x <= xmax)):
            while (i < (len(interpolatedPoints) - 1)):
                if (x >= interpolatedPoints[i].x) and (x <= interpolatedPoints[i+1].x):
                    pnt=pntOnLineAtXP(interpolatedPoints[i],interpolatedPoints[i+1],x)
                    intersect_points.append(pnt)
                i=i+1

        j=j+3 # skip j up to P3 of the current curve to be used as P0 start of next curve

    return intersect_points # return list of intersection points


# ----------------...Calculate length..------------------------------

def distance(xstart,ystart,xend,yend):
    """Accepts four values x1,y1,x2,y2 and returns distance"""
    #a^2+b^2=c^2
    return math.sqrt(((xend-xstart)**2)+((yend-ystart)**2))

def distanceP(p1,p2):
    """Accepts two point objects and returns distance between the points"""
    return distance(p1.x,p1.y,p2.x,p2.y)

def curveTangentAtLine(P1,P2,curve):
    '''
    Accepts two points objects and an array of point objects.  The two points describe a line that intersects the curve P0 C1 C2 P1 contained in the array.
    This function returns the first found intersection point of the line and curve,and also returns the angle of the tangent ray at that point,directionally down the path '''

    # determine whether P1 or P2 is the  furthest away from 1st point in curve[].
    # The point further away is considered the 'fixed point' & use this point to derive the angle of the line towards the curve
    if distanceP(P1,curve[0]) >= distanceP(P2,curve[0] ):
        fixed_pnt=P1
        angle=angleOfLineP(P1,P2)
    else:
        fixed_pnt=P2
        angle=angleOfLineP(P2,P1)

    intersections=[]
    pnt=Pnt()

    found='false'
    j=0
    while j <= len(curve)  - 4 and found != 'true':  # for each bezier curve in curveArray until a point is found
        intersection_estimate=pntIntersectLinesP(P1,P2,curve[j],curve[j+3]) # is there an intersection?
        if intersection_estimate != None or intersection_estimate != '':
            interpolated_points=interpolateCurve(curve[j],curve[j+1],curve[j+2],curve[j+3],100)  #interpolate this bezier curve,n=100

            k=0
            while (k < len(interpolated_points) - 1) and (found != 'true'):
                pnt_on_line=polarPointP(fixed_pnt,distanceP(fixed_pnt,interpolated_points[k]),angle)
                range=distanceP(interpolated_points[k],interpolated_points[k+1]) # TODO: improve margin of error
                if (distanceP(pnt_on_line,interpolated_points[k]) < range):
                    # its close enough!
                    num=k
                    found='true'
                    if k > 1:
                        if (interpolated_points[k - 1] not in intersections) and (interpolated_points[k-2] not in intersections):
                            intersections.append(interpolated_points[k])
                    elif k == 1:
                        if (interpolated_points[k - 1] not in intersections):
                            intersections.append(interpolated_points[k])
                    else:
                        intersections.append(interpolated_points[k])
                k=k+1

        j=j+3 # skip j up to P3 of the current curve to be used as P0 start of next curve

    if (found == 'true'):
        tangent_angle=angleOfLineP(interpolated_points[num - 1],interpolated_points[num+1])
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
    while j <= len(curve)  - 4:  # for each curve,get segmentLength & add to curveLength
        interpolatedPoints=interpolateCurve(curve[j],curve[j+1],curve[j+2],curve[j+3],n)  #interpolate this curve
        # add up lengths between the interpolated points
        segmentLength=0.0
        i=1
        while (i <= n):
                segmentLength=segmentLength+distanceP(interpolatedPoints[i-1],interpolatedPoints[i]) #length from previous point to current point
                i=i+1
        curveLength=curveLength+segmentLength
        j=j+3 # skip j up to P3 of the current curve to be used as P0 start of next curve
    return curveLength

def curveLengthAtPoint(pnt,curve,n=100):
    print 'find curve at point',pnt.x,',',pnt.y
    found=0
    curveLength=0.0
    j=0
    while j <= len(curve)  - 4 and found == 0:  # for each curve,get segmentLength & add to curveLength

        interpolatedPoints=interpolateCurve(curve[j],curve[j+1],curve[j+2],curve[j+3],n)  #interpolate this curve

        # add up lengths between the interpolated points
        segmentLength=0.0
        i=1
        while (i <= n) and (found == 0):
                segmentLength=segmentLength+distanceP(interpolatedPoints[i-1],interpolatedPoints[i]) #length from previous point to current point
                try:
                    if pnt == interpolatedPoints[i] or distanceP(pnt,interpolatedPoints[i]) <= 0.01:
                        found=1
                except:
                    print 'out of bounds i=',i
                i=i+1

        curveLength=curveLength+segmentLength
        j=j+3 # skip j up to P3 of the current curve to be used as P0 start of next curve

    return curveLength

def interpolatedCurveLengthAtPoint(pnt,interpolatedPoints):
    # add up lengths between the interpolated points
    segmentLength=0.0
    found=0
    i=1
    while (i < len(interpolatedPoints)) and (found == 0):
            segmentLength=segmentLength+distanceP(interpolatedPoints[i-1],interpolatedPoints[i]) #length from previous point to current point
            try:
                if pnt == interpolatedPoints[i] or distanceP(pnt,interpolatedPoints[i]) <= 1.0: # 1 pixel
                    found=1
            except:
                print 'out of bounds i=',i
            i=i+1

    return segmentLength

def interpolatedCurvePointAtLength(length,interpolatedPoints):
    # add up lengths between the interpolated points
    pnt=Pnt()
    curveLength=0.0
    segmentLength=0.0
    found=0
    i=1
    while (i < len(interpolatedPoints)) and (found == 0):
            segmentLength=segmentLength+distanceP(interpolatedPoints[i-1],interpolatedPoints[i]) #length from previous point to current point
            if segmentLength >= length: # 1 pixel - err on the side of too much rather than too little length
                    found=1
                    pnt=interpolatedPoints[i]
            i=i+1

    return pnt

def interpolateCurveList(curve,t=100):
    '''curve can be multiple cubic curves in an array ' P0 C1a C2a P1 C1b C2b P2...'''
    interpolatedPoints=[]
    j=0
    while j <= len(curve) - 4: # interpolate each curve segment
        temp_list=interpolateCurve(curve[j],curve[j+1],curve[j+2],curve[j+3],t)
        for pnt in temp_list:
            interpolatedPoints.append(pnt)
        j=j+3
    return interpolatedPoints

def interpolateCurve(P0,P1,P2,P3,t=100):
    '''
    Accepts curve points P0,P1,P2,P3 & number of interpolations t from curveLength()
    P0 - knot point 1,P1 - control point 1,P2 - control point 2,P3 - knot point 2
    Adapted from http://www.planetclegg.com/projects/WarpingTextToSplines.htm
    Using P0 P1 P2 P3 not P0 C1 C2 P1 to make the formulas easier
    '''

    # calculate coefficients for two knot points P0 & P3 ;     P1 & P2 are the controlpoints.
    # x coefficients
    A=P3.x - (3*P2.x)+(3*P1.x) - P0.x
    B=(3*P2.x) - (6*P1.x)+(3*P0.x)
    C=(3*P1.x) - (3*P0.x)
    D=P0.x
    # y coefficients
    E=P3.y - (3*P2.y)+(3*P1.y) - P0.y
    F=(3*P2.y) - (6*P1.y)+(3*P0.y)
    G=(3*P1.y) - (3*P0.y)
    H=P0.y

    # calculate interpolated points
    interpolatedPoints=[]
    maxPoint=float(t)
    i=0
    while ( i <= t):
            j=i/maxPoint # j can't be an integer,i/t is an integer..always 0.
            x=A*(j**3)+B*(j**2)+C*j+D
            y=E*(j**3)+F*(j**2)+G*j+H
            interpolatedPoints.append(Pnt(x,y))
            i=i+1
    return interpolatedPoints


# ----------------...Calculate intersections...------------------------------

def xyIntersectLines2(L1x1,L1y1,L1x2,L1y2,L2x1,L2y1,L2x2,L2y2):
    """ Accepts coords for endpoints of 2 lines: L1x1,L1y1,L1x2,L1y2,L2x1,L2y1,L2x2,L2y2. Returns x,y of intersection"""
    L1startx=float(L1x1)
    L1starty=float(L1y1)
    L1endx=float(L1x2)
    L1endy=float(L1y2)
    L2startx=float(L2x1)
    L2starty=float(L2y1)
    L2endx=float(L2x2)
    L2endy=float(L2y2)
    if (L1startx == L1endx):
        x=L1startx
        L2m=slopeOfLine(L2startx,L2starty,L2endx,L2endy)
        L2b=L2starty - L2m*L2startx
        y=L2m*x+L2b
    elif (L2startx == L2endx):
        x=L2startx
        L1m=slopeOfLine(L1startx,L1starty,L1endx,L1endy)
        L1b=L1starty - L1m*L1startx
        y=L1m*x+L1b
    else:
        L1m=(L1endy - L1starty)/(L1endx - L1startx)
        L2m=(L2endy - L2starty)/(L2endx - L2startx)
        L1b=L1starty - L1m*L1startx
        L2b=L2starty - L2m*L2startx
        if (abs(L1b - L2b) < 0.01):
            debug('***** Parallel lines in intersectLines2 *****')
            return None,None
        else:
            if (L1m == L2m):
                x=L1startx
            else:
                x=(L2b - L1b) / (L1m - L2m)
            y=(L1m*x)+L1b # arbitrary choice,could have used L2m & L2b
    return x,y

def xyIntersectLines_notinuse(xstart1,ystart1,xend1,yend1,xstart2,ystart2,xend2,yend2):
    """
    Find intersection between two lines. Accepts 8 values (begin & end for 2 lines),returns x & y values.
    Intersection does not have to be within the supplied line segments
    Returns x,y
    """
    # Find point x,y where m1*x+b1=m2*x+b2
    # m=(ystart1-y2)/(xstart1-xend1) --> find slope for each line
    # y=mx+b --> b=y - mx  --> find b for each line
    FIRST_VERTICAL=''
    SECOND_VERTICAL=''
    if (xend1==xstart1):
        # vertical 1st line
        FIRST_VERTICAL='True'
        x=xstart1
    else:
        m1= slopeOfLine(xstart1,ystart1,xend1,yend1)
        b1=(ystart1 - (m1*xstart1)) # b=y-mx

    if (xend2==xstart2):
        # vertical 2nd line
        SECOND_VERTICAL='True'
        x=xstart2
    else:
        m2=slopeOfLine(xstart2,ystart2,xend2,yend2)
        b2=(ystart2 - (m2*xstart2))

    # test for parallel
    if (FIRST_VERTICAL and SECOND_VERTICAL):
        debug('***** Parallel lines in intersectLines *****')
        return None,None
    elif (not (FIRST_VERTICAL or SECOND_VERTICAL)):
            if  (abs(b2 - b1) < 0.01):
                debug('***** Parallel lines in intersectLines *****')
                return None,None

    # find x where m1*x+b1=m2*x+b2
    # m1*x - m2*x   = b2 - b1
    # x( m1 - m2 ) =b2 - b1
    # x=(b2-b1)/(m1-m2)
    if (FIRST_VERTICAL):
        y=m2*x+b2
    elif (SECOND_VERTICAL):
        y=m1*x+b1
    else:
        x=(b2 - b1) / (m1 - m2)
        y=(m1*x)+b1 # arbitrary choice,could have used y=m2*x+b2
    return x,y

def xyIntersectLinesP(p1,p2,p3,p4):
    """
    Find intersection between two lines. Accepts 4 point objects,Returns x,y values
    Intersection does not have to be within the supplied line segments
    """
    x,y=xyIntersectLines2(p1.x,p1.y,p2.x,p2.y,p3.x,p3.y,p4.x,p4.y)
    return x,y

def pntIntersectLines(x1,y1,x2,y2,x3,y3,x4,y4):
    """
    Find intersection between two lines. Accepts 8 values (begin & end for 2 lines),Returns pnt object
    Intersection does not have to be within the supplied line segments
    """
    pnt=Pnt()
    pnt.x,pnt.y=xyIntersectLines2(x1,y1,x2,y2,x3,y3,x4,y4)
    return pnt

def pntIntersectLinesP(p1,p2,p3,p4):
    """
    Find intersection between two lines. Accepts 4 point objects,Returns pnt object
    Intersection does not have to be within the supplied line segments
    """
    x,y=xyIntersectLines2(p1.x,p1.y,p2.x,p2.y,p3.x,p3.y,p4.x,p4.y)
    pnt=Pnt()
    pnt.x=x
    pnt.y=y
    return pnt

def pntIntersectLineCircleP(C,r,P1,P2):
    """
    Finds intersection of a line segment and a circle.
    Accepts circle center point object C,radius r,and two line point objects P1 & P2
    Returns an object P with number of intersection points,and up to two coordinate pairs as P.intersections,P.p1,P.p2
    Based on paulbourke.net/geometry/sphereline/sphere_line_intersection.py,written in Python 3.2 by Campbell Barton
    """
    #TODO - add test parameter to determine which intersection should be used
    #TODO - doesn't work on P1-P2 vertical line - CRASHES!!!!!!

    def square(f):
        return f*f

    # P1.x,P1.y  --> P1 coordinates (point of line)
    # P2.x,P2.y,-->  P2 coordinates (point of line)
    # C.x,C.y,r  --> P3 coordinates and radius (Chere)
    # x,y   intersection coordinates
    #
    # This function returns a pointer array which first index indicates
    # the number of intersection points,followed by coordinate pairs.

    P,p1,p2=Pnt(), Pnt(), Pnt()
    intersections=0
    a=square(P2.x - P1.x)+square(P2.y - P1.y)
    b=(2.0*((P2.x - P1.x)*(P1.x - C.x))+((P2.y - P1.y)*(P1.y - C.y)))
    c=(square(C.x)+square(C.y)+square(P1.x)+square(P1.y) - (2.0*(C.x*P1.x+C.y*P1.y )) -
            square(r))

    i=b*b - 4.0*a*c

    if i < 0.0:
        print 'no intersections b/w line',P1.name, P1.x,P1.y,'--',P2.name,P2.x,P2.y,'and Circle',C.name,C.x,C.y,'with radius', r
        return None

    elif i == 0.0:
        # one intersection
        intersections=1
        mu=-b / (2.0*a)
        p1.x, p1.y=P1.x+mu*(P2.x - P1.x), P1.y+mu*(P2.y - P1.y)

    elif i > 0.0:
        # two intersections
        intersections=2

        # first intersection
        mu1=(-b+math.sqrt(i)) / (2.0*a)
        p1.x, p1.y=P1.x+mu1*(P2.x - P1.x),P1.y+mu1*(P2.y - P1.y)

        # second intersection
        mu2=(-b - math.sqrt(i)) / (2.0*a)
        p2.x,p2.y=P1.x+mu2*(P2.x - P1.x),P1.y+mu2*(P2.y - P1.y)

    P.intersections=intersections
    P.p1=p1
    P.p2=p2
    return P

def intersectCircles(x0,y0,r0,x1,y1,r1):
    """
    Accepts data for two circles x1,y1,r1,x2,y2,r2
    Returns xi,yi,xi_prime,yi_prime pairs where circles intersect,and intersections=number of intersections
    example: returns ax,ay,bx,by,number of intersections {0|1|2} --> ax,ay and bx,by are empty when intersections=0,and  bx,by is empty when intersections=1
    """
    #print 'radius of 1st circle ro:',r0
    #print 'radius of 2nd circle r1:',r1
    d=distance(x0,y0,x1,y1) # distance b/w circle centers
    #print 'distance between circle centers:',d
    dx,dy=(x1 - x0),(y1 - y0) # negate y b/c canvas increases top to bottom

    if (d == 0):
            print 'center of both circles are the same...patternintersectCircles()'
            intersections=0
    elif (d < abs(r0 - r1)):
            print 'one circle is within the other ...pattern.intersectCircles()'
            print 'r0 - r1 =', (r0 - r1),abs(r0 - r1)
            print 'd < abs(r0 - r1)?', (d<abs(r0 - r1))
            intersections=0
    elif (d > (r0+r1)):
            print 'circles do not intersect ...pattern.intersectCircles()'
            #intersections=0
            # TODO: possible kluge  - check if this is acceptable using a small margin of error between r0 & r1 (2*CM)?:
            r1=d - r0
    else:
            #'I' is the point where the line through the circle centers crosses the line between the intersection points,creating 2 right triangles
            a=((r0*r0) - (r1*r1)+(d*d)) / (2.0*d)
            intersections=2

            x2=x0+(dx*a/d)
            y2=y0+(dy*a/d)
            h=math.sqrt((r0*r0) - (a*a))
            rx=-dy*(h/d)
            ry=dx*(h/d)
            xi=x2+rx
            xi_prime=x2 - rx
            yi=y2+ry
            yi_prime=y2 - ry
            return xi,yi,xi_prime,yi_prime,intersections

def xyIntersectCirclesP(C1,r1,C2,r2):
    """
    Accepts C1,r1,C2,r2 where C1 & C2 are point objects
    Returns x1,y1,x2,y2 where the two circles intersect
    """
    return intersectCircles(C1.x,C1.y,r1,C2.x,C2.y,r2)

def pntIntersectCirclesP(C1,r1,C2,r2):
    """
    Accepts C1,r1,C2,r2 where C1 & C2 are point objects
    Returns an object P,where P.intersections=number of intersections,and P.p1 & P.p2 are point objects where the two circles intersect
    """
    P,p1,p2=Pnt(), Pnt(), Pnt()
    intersections=0
    #print 'C1.x,C1.y,r1 =',C1.x, C1.y,r1
    #print 'C2.x,C2.y,r2 =', C2.x,C2.y,r2
    x1,y1,x2,y2,intersections=intersectCircles(C1.x,C1.y,r1,C2.x,C2.y,r2)
    p1=Pnt(x1,y1)
    p2=Pnt(x2,y2)
    P.intersections=intersections
    P.p1=p1
    P.p2=p2
    return P

def pntsOnCircleFromChordLength(C,P,r,chord_length):
    ''' Accepts center of circle,a point on the circle,radius of circle,and chord length.  Returns a list of two points on the circle at chord_length distance away from original point'''
    d=chord_length
    # point on circle given chordlength & starting point=2*asin(d/2r)
    d_div_2r=d/(2.0*r)
    angle=2*asin(d_div_2r)
    pnts=[]
    pnts.append(polarPointP(C,r,angle))
    pnts.append(polarPointP(C,r,- angle))
    return pnts

def pntsOnChord(C,r,P,chord_length):
    ''' Accepts center of circle,radius of circle,a point on the circle,and chord length.  Returns a list of two points on the circle at chord_length distance away from original point'''
    d=chord_length
    # point on circle given chordlength & starting point=2*asin(d/2r)
    d_div_2r=d/(2.0*r)
    angle=2*asin(d_div_2r)
    pnts=[]
    pnts.append(polarPointP(C,r,angle))
    pnts.append(polarPointP(C,r,- angle))
    return pnts

def splitCurveAtLength(length,curve):
    '''Accepts a point on a curve,and a curve list with points P0 C1 C2 P1. Returns curve list with P0,split.c1,split.c2,split_pnt,new.c11,new.c12,P1'''

    #TODO: use lib2geom to split a curve - this function is temporary

    # find split point
    interpolated_points=interpolateCurve(curve[0],curve[1],curve[2],curve[3])
    split_pnt=interpolatedCurvePointAtLength(length,interpolated_points) # split neck curve at this point

    # find tangent at split point
    pnt1=interpolatedCurvePointAtLength(length - .1*IN,interpolated_points) # arbitrary 1/10th of an inch - good enough for this application?
    pnt2=interpolatedCurvePointAtLength(length+.1*IN,interpolated_points) # arbitrary 1/10th of an inch - good enough for this application?
    forward_tangent_angle=angleOfLineP(pnt1,pnt2)
    backward_tangent_angle=angleOfLineP(pnt2,pnt1)

    # neck control points
    #b/w curve[0] and split_pnt
    length=distanceP(curve[0],split_pnt)/3.0
    split_pnt.c1=polarPointP(curve[0],length,angleOfLineP(curve[0],curve[1])) # preserve angle b/w P0 & original 1st control point
    split_pnt.c2=polarPointP(split_pnt,length,backward_tangent_angle)
    # b/w split_pnt and curve[3]
    curve3=PntP(curve[3])
    length=distanceP(split_pnt,curve3)/3.0
    curve3.c1=polarPointP(split_pnt,length,forward_tangent_angle)
    curve3.c2=polarPointP(curve3,length,angleOfLineP(curve3,curve[2])) # preserve angle b/w original 2nd control point & P1

    new_curve=[]
    new_curve.append(curve[0])
    new_curve.append(split_pnt.c1)
    new_curve.append(split_pnt.c2)
    new_curve.append(split_pnt)
    new_curve.append(curve3.c1)
    new_curve.append(curve3.c2)
    new_curve.append(curve3)

    return new_curve

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

    # split neck curve at length - returns curve with P0 C11 C12 P1 C21 C22 P2
    split_curve=splitCurveAtLength(length,waist_curve)

    #dart_apex=rPointP(parent,parent.name+'dart_apex',polarPointP(split_curve[3],dart_length,angleOfLineP(split_curve[3],split_curve[2])+ANGLE90))
    # TODO: test for direction of dart - plus or minus 90 degrees from the angle of the tangent at the dart...
    # ...the angle of line from 2nd control point (split_curve[2]) to the split point (split_curve[3])
    dart_apex=polarPointP(split_curve[3],dart_length,angleOfLineP(split_curve[3],split_curve[2])+dart_angle)

    # separate split_curve into inside_curve1 & outside_curve
    inside_curve=[]
    i=0
    while i <= 3:
        inside_curve.append(PntP(split_curve[i]))
        i=i+1

    outside_curve=[]

    i=3
    while i <= 6:
        outside_curve.append(PntP(split_curve[i ]))
        i=i+1

    # rotate outside leg & side point (outside_curve) relative to the dart_apex,creating the dart
    slashAndSpread(dart_apex,rotation_angle,outside_curve[0],outside_curve[1],outside_curve[2],outside_curve[3])

    return dart_apex, inside_curve, outside_curve

def angleFromChord(chord_width, radius):
    # see http://math.stackexchange.com/questions/164541/finding-a-point-having-the-radius-chord-length-and-another-point
    # find the angle between two points given center,radius,chordlength & starting point=2*asin(d/2r)
    d=chord_width # chord width - usage: could be the dart width
    r=radius # radius - usage: could be the dart length
    d_div_2r=d/(2.0*r)
    angle=2*asin(d_div_2r) # angle - usage: could be the rotation angle used in slashAndSpread to create a dart

    return angle

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
    rotation_angle=angleFromChord(dart_width,dart_length)

    dart_apex=rPointP(parent,'dart_apex',polarPointP(split_curve[3],dart_length,angleOfLineP(split_curve[3],split_curve[2])+ANGLE90))

    # separate split_curve into curve1 & curve2
    curve1=[]
    i=0
    while i <= 3:
        curve1.append(PntP(split_curve[i]))
        i=i+1

    curve2=[]

    i=3
    while i <= 6:
        curve2.append(PntP(split_curve[i ]))
        i=i+1

    # rotate curve1 relative to the dart_apex,creating the dart
    slashAndSpread(dart_apex,rotation_angle,curve1[0],curve1[1],curve1[2],curve1[3])

    return dart_apex, curve1, curve2


def intersectLineCurve(P1,P2,curve,n=100):
    '''
    Accepts two points of a line P1 & P2,and an array of connected bezier curves [P11,C11,C12,P12,C21,C22,P22,C31,C32,P32,...]
    Returns an array points_found[] of point objects where line intersected with the curve, and tangents_found[] of tangent angle at that point
    '''

    # get polar equation for line for P1-P2
    # point furthest away from 1st point in curve[] is the fixed point & sets the direction of the angle towards the curve
    #if distanceP(P1,curve[0]) >= distanceP(P2,curve[0] ):
    #   fixed_pnt=P1
    #   angle=angleOfLineP(P1,P2)
    #else:
    #   fixed_pnt=P2
    #  angle=angleOfLineP(P2,P1)
    fixed_pnt=P1
    angle=angleOfLineP(P1,P2)

    #print 'P1 =',P1.x,P1.y
    #print 'P2 =',P2.x,P2.y
    #for pnt in curve:
        #print 'curve =',pnt.x,pnt.y

    intersections=0
    points_found=[]
    tangents_found=[]
    pnt=Pnt()

    j=0
    while j <= len(curve)  - 4:  # for each bezier curve in curveArray
        intersection_estimate=pntIntersectLinesP(P1,P2,curve[j],curve[j+3]) # is there an intersection?
        if intersection_estimate != None or intersection_estimate != '':
            interpolatedPoints=interpolateCurve(curve[j],curve[j+1],curve[j+2],curve[j+3],n)  #interpolate this bezier curve,n=100

            k=0
            while k < len(interpolatedPoints) - 1:
                pnt_on_line=polarPointP(fixed_pnt,distanceP(fixed_pnt,interpolatedPoints[k]),angle)
                range=distanceP(interpolatedPoints[k],interpolatedPoints[k+1]) # TODO: improve margin of error
                distance=distanceP(pnt_on_line,interpolatedPoints[k])
                #print k,'pntOnCurve',interpolatedPoints[k].x,interpolatedPoints[k].y,'pntOnLine',pnt_on_line.x,pnt_on_line.y,distance,range
                if ( distance <= range):
                    # its close enough!
                    #print 'its close enough!'
                    if k>1:
                        if (interpolatedPoints[k - 1] not in points_found) and (interpolatedPoints[k-2] not in points_found):
                            points_found.append(interpolatedPoints[k])
                            tangents_found.append(angleOfLineP(interpolatedPoints[k-1],interpolatedPoints[k+1]))
                            intersections=intersections+1
                    elif k==1:
                        if (curve[0] not in intersections):
                            points_found.append(interpolatedPoints[1])
                            tangents_found.append(angleOfLineP(curve[0],interpolatedPoints[2]))
                            intersections=intersections+1
                    else:
                        intersections.append(curve[0])
                        tangents_found.append(angleOfLineP(curve[0],curve[1]))
                k=k+1

        j=j+3 # skip j up to P3 of the current curve to be used as P0 start of next curve
        
        if intersections==0:
            print 'no intersections found in intersectLineCurve(',P1.name,P2.name,' and curve'

    return points_found,tangents_found

# __________...Create darts...________________________________

def addDartFold(parent,dart,inside_pnt):

        DART_LENGTH=distanceP(dart,dart.o)
        DART_HALF_ANGLE=abs(angleOfVectorP(dart.o,dart,dart.i))/2.0
        O_ANGLE=angleOfLineP(dart,dart.o)
        I_ANGLE=angleOfLineP(dart,dart.i)

        # determine which direction the dart will be folded
        if I_ANGLE <= O_ANGLE:
            FOLD_ANGLE=I_ANGLE - DART_HALF_ANGLE
        else:
            FOLD_ANGLE=I_ANGLE+DART_HALF_ANGLE

        # find intersection of fold & armscye b/w bd2.i & inside_pnt
        # TODO: use intersectLineCurve()
        temp_pnt=polarPointP(dart,DART_LENGTH,FOLD_ANGLE)
        fold_pnt=pntIntersectLinesP(dart.i,inside_pnt,dart,temp_pnt)

        # dart midpoint at seamline
        temp_pnt=pntMidPointP(dart.i,dart.o)
        mid_pnt=pntOnLineP(dart,temp_pnt,distanceP(dart,fold_pnt))
        if hasattr(dart,'m'):
            updatePoint(dart.m,mid_pnt)
        else:
            dart.m=rPointP(parent,dart.name+'.m',mid_pnt) # adds '.' automatically - why?

        # dart outside leg at cuttingline
        temp_pnt=pntOnLineP(dart.o,dart,-SEAM_ALLOWANCE)
        if hasattr(dart,'oc'):
            updatePoint(dart.oc, temp_pnt)
        else:
            dart.oc=rPointP(parent,dart.name+'.oc',temp_pnt) # adds '.' automatically - why?

        # dart inside leg at cuttingline
        temp_pnt=pntOnLineP(dart.i,dart,-SEAM_ALLOWANCE)
        if hasattr(dart,'ic'):
            updatePoint(dart.ic,temp_pnt)
        else:
            dart.ic=rPointP(parent,dart.name+'.ic',temp_pnt) # adds '.' automatically - why?

        return


def addDartMidPoint(parent,dart_leg1,dart_apex,dart_leg2,next_pnt):
        '''old version of addDartFold() -- uses .o,oc,.i,.ic instead of newer .o,.oc,.i,.ic'''
        DART_LENGTH=distanceP(dart_apex,dart_leg1)
        DART_HALF_ANGLE=abs(angleOfVectorP(dart_leg1,dart_apex,dart_leg2))/2.0
        DART_LEG1_ANGLE=angleOfLineP(dart_apex,dart_leg1)
        DART_LEG2_ANGLE=angleOfLineP(dart_apex,dart_leg2)
        # determine which direction the dart will be folded
        if DART_LEG2_ANGLE <= DART_LEG1_ANGLE:
            DART_FOLD_ANGLE=DART_LEG2_ANGLE - DART_HALF_ANGLE
        else:
            DART_FOLD_ANGLE=DART_LEG2_ANGLE+DART_HALF_ANGLE
        midpnt=pntMidPointP(dart_leg1,dart_leg2)
        foldpnt=polarPointP(dart_apex,DART_LENGTH,DART_FOLD_ANGLE)
        intpnt=pntIntersectLinesP(dart_leg2,next_pnt,dart_apex,foldpnt)
        # dart midpoint at waist
        pnt=pntOnLineP(dart_apex,midpnt,distanceP(dart_apex,intpnt))
        if hasattr(dart_apex,'m'):
            dart_apex.m.x, dart_apex.m.y=pnt.x,pnt.y
            dart_apex.m.coords  =str(pnt.x)+","+str(pnt.y)
        else:
            dart_apex.m=rPointP(parent,dart_apex.name+'.m',pnt)
        # dart outside leg at cuttingline
        pnt=pntOnLineP(dart_leg1,dart_apex,-SEAM_ALLOWANCE)
        if hasattr(dart_apex,'oc'):
            dart_apex.oc.x,dart_apex.oc.y=pnt.x,pnt.y
            dart_apex.oc.coords  =str(pnt.x)+","+str(pnt.y)
        else:
            dart_apex.oc=rPointP(parent,dart_apex.name+'.oc',pnt)
        # dart inside leg at cuttingline
        pnt=pntOnLineP(dart_leg2,dart_apex,-SEAM_ALLOWANCE)
        if hasattr(dart_apex,'ic'):
            dart_apex.ic.x,dart_apex.ic.y=pnt.x,pnt.y
            dart_apex.ic.coords  =str(pnt.x)+","+str(pnt.y)
        else:
            dart_apex.ic=rPointP(parent,dart_apex.name+'.ic',pnt)

        return

# ----------------...Calculate control points..------------------------------

def pointList(*args):
    points=[]
    for arg in args:
        points.append(arg)
    return points

def controlPoints(name,knots):
    #TODO: remove name from args
    k_num=len(knots) - 1 # last iterator for n knots 0..n-1
    c_num=k_num - 1 # last iterator for n-1 curve segments 0..n-2
    c1=[] # first control points c1[0..c_num]
    c2=[] # second control points c2[0..c_num]

    i=1
    while (i <= c_num):
        # each loop produces c2[previous] and c1[current]
        # special cases: get c1[0] in 1st loop & c2[c_num] in last loop
        # previous segment is segment b/w previous knot & current knot
        # current segment is segment b/w current knot & next knot
        # start with i=1 because can't start processing with knot[0] b/c it doesn't have a previous knot
        previous=(i - 1)
        current=i
        next=(i+1)
        last_knot=k_num
        last_segment=c_num

        # process previous segment's c2
        angle=angleOfLineP(knots[next],knots[previous])
        length=distanceP(knots[current],knots[previous])/3.0
        pnt=polarPointP(knots[current],length,angle)
        c2.append(pnt) # c2[previous]

        if (current == 1):
            # process 1st segment's c1
            angle=angleOfLineP(knots[0],c2[0])
            pnt=polarPointP(knots[0],length,angle)
            c1.append(pnt)

        # process current segment's c1
        angle=angleOfLineP(knots[previous],knots[next])
        length=distanceP(knots[current],knots[next])/3.0
        pnt=polarPointP(knots[current],length,angle)
        c1.append(pnt) # c1[current]

        if (current == c_num):
            # process last segment's c2
            angle=angleOfLineP(knots[last_knot],c1[last_segment])
            pnt=polarPointP(knots[last_knot],length,angle)
            c2.append(pnt) # c2[last_segment]

        i=(i+1)

    return c1, c2

# ----------------...Calculate transforms..------------------------------

def transformPoint(x,y,transform=''):
    """
    Apply an SVG transformation string to a 2D point and return the resulting x,y pair
    """
    #
    # -spc- TODO - use numpy to do a proper handling of all transformations in order
    # Postponing this until after the LGM workshop in order not to introduce
    # a new dependency - for now we will only handle a few transformation types
    #
    if transform == '':
        return x,y

    # Every transform in the list ends with a close paren
    transforms=re.split(r'\)',transform)
    for tr in transforms:
        # I don't know why we get an empty string at the end
        if tr == '':
            continue
        tr=tr.strip()

        trparts=re.split(r',|\(',tr)
        trtype=trparts[0].strip()

        if trtype == 'translate':
            #tx=float(trparts[1].strip()) #-- commented out by susan 26/08/11 -- was returning 'invalid literal for float(): 0 0' error message -- 0,0 because the transform for 1st pattern is 0,0
            splitx=re.split("( )",trparts[1].strip())  # added by susan 26/08/11 -- to split apart the two values in tx
            sx=splitx[0].strip() # strip one more time - susan 26/08/11
            tx=float(sx) # substituted sx for trparts[1].strip() - susan 26/08/11
            x=x+tx
            try:
                ty=float(trparts[2].strip())
                y=y+ty
            except IndexError:
                pass

        elif trtype == 'scale':
            sx=float(trparts[1].strip())
            try:
                sy=float(trparts[2].strip())
            except IndexError:
                sy=sx
            x=x*sx
            y=y*sy

        elif trtype == 'skewX':
            sx=float(trparts[1].strip())
            # now do the thing
            #TODO: skewX transform not handled yet
            raise NotImplementedError

        elif trtype == 'skewY':
            sy=float(trparts[1].strip())
            # now do the thing
            #TODO: skewY not handled yet
            raise NotImplementedError

        elif trtype == 'rotate':
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
            #TODO: rotate not handled yet
            raise NotImplementedError

        elif trtype == 'matrix':
            ma=float(trparts[1].strip())
            mb=float(trparts[2].strip())
            mc=float(trparts[3].strip())
            md=float(trparts[3].strip())
            me=float(trparts[3].strip())
            mf=float(trparts[3].strip())
            # now do the thing
            #TODO: matrix not handled yet
            raise NotImplementedError
        else:
            #TODO: Unexpected transformation %s' % trtype
            raise ValueError

    return x,y

# ----------------...create a scaling transform..------------------------------

def scaleAboutPointTransform(x,y,scale):
    """
    Return an SVG transform that scales about a specific x,y coordinate
    """
    sx=scale
    sy=scale
    return "matrix(%f,0,0,%f,%f,%f)" % (sx,sy,x-(sx*x),y-(sy*y))

# ----------------...Calculate bounding box..------------------------------

def boundingBox(path):
    # TODO: only use information from paths - cuttinLine,seamLine,foldLine,dartLine
    xlist=[]
    ylist=[]
    #print '===== Entered boundingBox ====='
    #print 'path=',path
    path_tokens=path.split() # split path into pieces,separating at each 'space'

    tok=iter(path_tokens)

    try:
        cmd=tok.next()
        if cmd != 'M':
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

            if ((cmd == 'M') or (cmd == 'L') or (cmd == 'T')):
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
            elif cmd == 'H':
                x=float(tok.next())
                if relative:
                    currentx=currentx+x
                else:
                    currentx=x
                xlist.append(currentx)
            elif cmd == 'V':
                y=float(tok.next())
                if relative:
                    currenty=currenty+y
                else:
                    currenty=y
                ylist.append(currenty)
            elif ((cmd == 'C') or (cmd == 'S') or (cmd == 'Q')):
                # Curve
                # TODO This could be innacurate,we are only basing on control points not the actual line

                # 'C' uses two control points,'S' and 'Q' use one
                if cmd == 'C':
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
            elif cmd == 'A':
                # TODO implement arcs - punt for now
                # See http://www.w3.org/TR/SVG/paths.html#PathElement
                raise ValueError('Arc commands in a path are not currently handled')
            elif cmd == 'Z':
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
    if transform == '':
        return xmin,ymin,xmax,ymax

    new_xmin,new_ymin=transformPoint(xmin,ymin,transform)
    new_xmax,new_ymax=transformPoint(xmax,ymax,transform)
    return new_xmin,new_ymin,new_xmax,new_ymax

def extractMarkerId(markertext):
    # Regex -
    # <marker id=\"grainline_mk\"\nviewBox=
    # one or more WS,followed by 'id' followed by zero or more WS followed by '=' followed by zero or more WS,followed by '"',
    m=re.search('(\s+id\s*=\s*\"\w+\")',markertext,re.I)
    mid=m.group(0).split('"')[1]
    return mid

# ----------------...Connect 2 objects together using 2 points each...------------------------------


def connectObjects(connector_pnts,old_pnts):
        # connector_pnts[0] and old_pnts[0] will connect together
        # connector_pnts[1] and old_pnts[1] will connect together
        # connector_pnts[1] is counterclockwise from connector_pnts[0] on object which doesn't move
        # old_pnts[] contains all of the points of the object to be moved in order clockwise,starting with old_pnts[0]

        t_pnts=[] # translated points. 1st step.
        r_pnts=[] # translated points that are rotated. 2nd step.

        # translate so that old_pnts[0] will connect with connector_pnts[0]
        (dx,dy)=(connector_pnts[0].x - old_pnts[0].x),(connector_pnts[0].y - old_pnts[0].y)
        i=0
        for o in old_pnts:
            # translate all points in old_pnts[]
            t_pnts.append(Pnt())
            t_pnts[i].x,t_pnts[i].y=o.x+dx,o.y+dy
            i=i+1

        angle1=angleOfLineP(connector_pnts[0],connector_pnts[1])
        angle2=angleOfLineP(connector_pnts[0],t_pnts[1])
        rotation_angle=angle2 - angle1 # subtract this angle from each angle of 2nd object's points towards connector0
        i=1 # don't rotate the 1st translated point,it should now be equal to connector0
        r_pnts.append(t_pnts[0])
        for t_pnt in t_pnts:
            if  (i != len(t_pnts)):
                distance=distanceP(connector_pnts[0],t_pnts[i])
                translated_angle=angleOfLineP(connector_pnts[0],t_pnts[i])
                r_angle=translated_angle - rotation_angle
                r_pnts.append(Pnt())
                r_pnts[i]=polarPointP(connector_pnts[0],distance,r_angle)
                i=i+1

        return r_pnts

# ----Slash and spread with slash line,pivot point,and angle
def slashAndSpread(pivot,angle,*args):

        list=[]
        for arg in args:
            list.append(arg)
        i=0
        while (i < len(list)):
            pnt=list[i]
            distance=distanceP(pivot,pnt)
            rotated_pnt=polarPointP(pivot,distance,angleOfLineP(pivot,pnt)+angle) # angle>0=spread clockwise. angle<0=spread counterclockwise.
            updatePoint(pnt,rotated_pnt)
            i=i+1
        return

# ---- Set up pattern document with design info ----------------------------------------
def setupPattern(pattern_design,clientData,printer,companyName,designerName,patternName,patternNumber):
        pattern_design.cfg['clientdata']=clientData
        if (printer == '36" wide carriage plotter'):
            pattern_design.cfg['paper_width']=(36.0*IN)
        pattern_design.cfg['border']=(2.54*CM)
        BORDER=pattern_design.cfg['border']
        metainfo={'companyName': companyName, #mandatory
                    'designerName': designerName,#mandatory
                    'patternName': patternName,#mandatory
                    'patternNumber': patternNumber #mandatory
                    }
        pattern_design.cfg['metainfo']=metainfo
        docattrs={'currentscale' : "0.5 : 1",
                    'fitBoxtoViewport' : "True",
                    'preserveAspectRatio' : "xMidYMid meet",
                    }
        doc=Document(pattern_design.cfg,name='document',attributes=docattrs)
        doc.add(TitleBlock('notes','titleblock',0.0,0.0,stylename='titleblock_text_style'))
        doc.add(TestGrid('notes','testgrid',pattern_design.cfg['paper_width']/3.0,0.0,stylename='cuttingline_style'))
        return doc

# ---- Pattern Classes ----------------------------------------

class Pnt():
    '''Accepts x,y & name. Returns an object with .x,.y,and .name children.  Does not create point in SVG document'''
    def __init__(self,x=0.0,y=0.0,name=''):
        self.x=x
        self.y=y
        self.name=name

class PntP():
    '''Accepts a point object. Returns a point object with .x,.y,and .name children.  Does not create point in SVG document'''
    def __init__(self,pnt=Pnt(),name=''):
        self.x=pnt.x
        self.y=pnt.y
        self.name=name

class Pattern(pBase):
    """
    Create an instance of Pattern class,eg - jacket,pants,corset,which will contain the set of pattern piece objects - eg  jacket.back,pants.frontPocket,corset.stayCover
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
        pg_width=self.cfg['paper_width'] - (2*self.cfg['border'])
        if 'verbose' in self.cfg:
            print 'Autolayout:'
            print ' total paperwidth=',self.cfg['paper_width']
            print ' border width=',self.cfg['border']
            print ' available paperwidth=',pg_width
            print ' pattern offset=',PATTERN_OFFSET

        next_x=0
        # -spc- FIX Leave room for the title block!
        next_y=8.0*IN_TO_PT # this should be zero
        #next_y=0 # this should be zero
        max_height_this_row=0
        # a very simple algorithm

        # we want to process these in alphabetical order of part letters
        index_by_letter={}
        letters=[]
        for pp,info in parts.items():
            letter=pp.lettertext
            if letter in index_by_letter:
                raise ValueError('The same Pattern Piece letter <%s> is used on more than one pattern piece' % letter)
            index_by_letter[letter]=pp
            letters.append(letter)

        # sort the list
        letters.sort()

        for thisletter in letters:
            pp=index_by_letter[thisletter]
            info=parts[pp]
            pp_width=info['xhi'] - info['xlo']
            pp_height=info['yhi'] - info['ylo']

            if 'verbose' in self.cfg:
                print '   Part letter: ',thisletter
                print '     part width=pp_width:',pp_width,' <-- info[xhi]:',info['xhi'], ' - info[xlo]:',info['xlo']
                print '     part height=pp_height:',pp_height,' <-- info[yhi]:',info['yhi'], ' - info[ylo]:',info['ylo']
                print '     current x=next_x:',next_x
                print '     current y=next_y:',next_y

            if pp_width > pg_width:
                print 'Error: Pattern piece <%s> is too wide to print on page width' % pp.name
                # TODO: -figure out something smarter
                ## raise

            if next_x+pp_width > pg_width:
                # start a new row
                real_next_y=next_y+max_height_this_row+PATTERN_OFFSET
                if 'verbose' in self.cfg:
                    print '     Starting new row,right side of piece would have been=',next_x+pp_width
                    print '     New x=0'
                    print '     Previous y=next_y:',next_y
                    print '     New y=real_next_y:',real_next_y,' <-- (next_y:',next_y,'+max_height_this_row:',max_height_this_row,'+PATTERN_OFFSET:',PATTERN_OFFSET,')'
                    print '     New max_height_this_row=pp_height:',pp_height

                next_y=real_next_y
                max_height_this_row=pp_height
                next_x=0
            else:
                if pp_height > max_height_this_row:
                    max_height_this_row=pp_height
                    if 'verbose' in self.cfg:
                        print'       Previous y=next_y:',next_y
                        print'       New y=Previous y'
                        print'       New max_height_this_row=pp_height:',pp_height

            # now set up a transform to move this part to next_x,next_y
            xtrans=(next_x - info['xlo'])
            ytrans=(next_y - info['ylo'])
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

class PatternPiece(pBase):
    """
    Create an instance of the PatternPiece class,eg jacket.back,pants.frontPocket,corset.stayCover
    which will contain the set of seams and all other pattern piece info,
    eg - jacket.back.seam.shoulder,jacket.back.grainline, jacket.back.interfacing
    """
    def __init__(self,group,name,letter='?',fabric=0,interfacing=0,lining=0):
        self.name=name
        self.groupname=group
        self.width=0
        self.height=0
        self.labelx=0
        self.labely=0
        self.lettertext=letter
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

        for child_group_name,members in child_group_dict.items(): # for each group used in this pattern piece
            if self.debug:
                print 'self.id =',self.id, 'child_group_name =', child_group_name
                print '++ Group ==',child_group_name,' in pattern.PatternPiece.getsvg()'

            # create a temporary pySVG group object
            temp_group=PYB.g()

            # assign temp group a unique id
            try:
                grpid=self.id+'.'+child_group_name
            except:
                print 'self.id =',self.id, 'child_group_name =', child_group_name, 'in pattern.PatternPiece.getsvg()'
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

        text.append('Designer: %s' % mi['designerName'])
        text.append('Client: %s' % self.cfg['clientdata'].customername)
        text.append(mi['patternNumber'])
        text.append('Pattern Piece %s' % self.lettertext)
        if self.fabric > 0:
            text.append('Cut %d Fabric' % self.fabric)
        if self.interfacing > 0:
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
        xmin,ymin,xmax,ymax= pBase.boundingBox(self,grouplist)
        xmin,ymin,xmax,ymax= transformBoundingBox(xmin,ymin,xmax,ymax,self.attrs['transform'])

        return xmin,ymin,xmax,ymax

class Node(pBase):
    """
    Create an instance which is only intended to be a holder for other objects
    """
    def __init__(self,name):
        self.name=name
        pBase.__init__(self)

class Point(pBase):
    """
    Creates instance of Python class Point
    """
    def __init__(self,group,name,x=0, y=0,styledef='default',transform='') :

        self.groupname=group
        self.name=name
        self.sdef=styledef
        self.x      =x
        self.y      =y
        self.attrs={}
        self.attrs['transform']=transform
        self.size    =5
        self.coords  =str(x)+","+str(y)
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

        pstyle= PYB.StyleBuilder(self.styledefs[self.sdef])
        p=PYB.circle(self.x,self.y,self.size)
        p.set_style(pstyle.getStyle())
        p.set_id(self.id)
        if 'tooltips' in self.cfg:
            p.set_onmouseover('ShowTooltip(evt)')
            p.set_onmouseout('HideTooltip(evt)')

        for attrname,attrvalue in self.attrs.items():
            p.setAttribute(attrname,attrvalue)
        md[self.groupname].append(p)

        txtlabel=self.id+'.text'
        txttxt=self.name
        if '_c' in txttxt:
            txtstyle='control_point_text_style'
        else:
            txtstyle='point_text_style'
        txt=self.generateText(self.x,self.y - 25,txtlabel,txttxt,txtstyle)
        md[self.groupname].append(txt)

        return md

    def boundingBox(self,grouplist=None):
        """
        Return two points which define a bounding box around the object
        """
        if grouplist is None:
            grouplist=self.groups.keys()
        if self.groupname in grouplist:
            (x1,y1)=(self.x - (self.size/2.0),self.y - (self.size/2.0))
            (x2,y2)=(self.x+(self.size/2.0),self.y+(self.size/2.0))
            return x1,y1,x2,y2
        else:
            return None,None,None,None

class Line(pBase):
    """
    Creates instance of Python class Line
    """
    def __init__(self,group,name,label,xstart, ystart,xend,yend,styledef='default',transform='') :

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

        pstyle= PYB.StyleBuilder(self.styledefs[self.sdef])
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
            #print '         end pattern.Line.boundingBox(',self.name,') - returning (xmin:',min(self.xstart,self.xend),' ymin:',min(self.ystart,self.yend) ,') ( xmax:',max(self.xstart,self.xend),' ymax:',max(self.ystart,self.yend),')'
            #return (min(self.xstart,self.xend),min(self.ystart,self.yend),max(self.xstart,self.xend),max(self.ystart,self.yend))
        #else:
            #print '         end pattern.Line.boundingBox(',self.name,') - returning (None,None,None,None)'
            #return None,None,None,None
        if self.groupname in grouplist:
            dd='M '+str(self.xstart)+' '+str(self.ystart)+' L '+str(self.xend)+' '+str(self.yend)
            xmin,ymin,xmax,ymax= boundingBox(dd)
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
            print 'Markerdefs: ',self.markerdefs
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

            pstyle= PYB.StyleBuilder(self.styledefs[self.sdef])

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
            xmin,ymin,xmax,ymax= boundingBox(dd)
            return xmin,ymin,xmax,ymax
        else:
            return None,None,None,None

class TextBlock(pBase):
    """
    Creates instance of Python class TextBlock
    """
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
            spacing = ( int(self.styledefs[self.textsdef]['font-size'])*1.2 )
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
