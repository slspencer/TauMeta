#!/usr/bin/env python
#Spencer_block_Bodice_Fitted_2.py

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

from tmtpl.document import *
from tmtpl.pattern import *
from tmtpl.constants import *
from tmtpl.utils import debug


def pattern(doc,A,B,CD):
    '''
    All measurements are converted to pixels
    x increases towards right, y increases towards bottom of drawing - Quadrants are 'upside down'
    All angles are in radians
    Angles start with 0 and '3:00' and move clockwise b/c quadrants are 'upside down'
    '''

    #start new_var dictionary
    checkpoint=['checkpoint']+locals().keys()[:]

    #front
    a1=pPointXY(A,'a1',0.0,0.0) #front neck center
    a2=pPoint(A,'a2',downPoint(a1,CD.front_waist_length)) #front waist center
    a3=pPoint(A,'a3',downPoint(a1,CD.front_underarm_height)) #front undera13 center
    a4=pPoint(A,'a4',rightPoint(a3,CD.front_underarm_width/2.0)) #front underarm side
    a5=pPoint(A,'a5',downPoint(a1,distance(a1,a3)/2.0)) #front across chest center
    a6=pPoint(A,'a6',rightPoint(a5,CD.across_chest/2.0)) #front across chest side
    pnts=intersectCircleAtX(a2,CD.front_neck_balance,CD.neck_width/2.0)
    if isAbove(a2,pnts[0]):
        a7=pPoint(A,'a7',pnts[0]) #front neck side
    else:
        a7=pPoint(A,'a7',pnts[1]) #front neck side
    pnts=intersectCircles(a2,CD.front_shoulder_balance,a7,CD.shoulder)
    if isRight(pnts[1],pnts[0]): #use the rightmost intersection
        a8=pPoint(A,'a8',pnts[0]) #front shoulder tip
    else:
        a8=pPoint(A,'a8',pnts[1]) #front shoulder tip
    a9=pPointXY(A,'a9',a6.x,a3.y) #front armscye corner
    a10=pPoint(A,'a10',downPoint(a1,CD.front_bust_height)) #front bust center
    a11=pPoint(A,'a11',rightPoint(a10,CD.front_bust_width/2.0)) #front bust side
    a_apex=pPoint(A,'a_apex',rightPoint(a10,CD.bust_point_distance/2.0))
    front_dart_length=distance(a10,a2)
    aD1=pPoint(A,'aD1',a_apex) #front dart apex is lower than a_apex
    aD1.i=pPoint(A,'aD1.i',downPoint(aD1,front_dart_length)) #front dart inside leg
    angle=-angleOfVector(a4,aD1,a11)/2.0 #angle sweeps counterclockwise
    p1=polarPoint(aD1,distance(aD1,a11),angle)
    updatePoint(a11,p1) #front bust side adjusted up by 1/2 angle of front dart apex to underarm
    a12=pPoint(A,'a12',intersectLineAtLength(a4,a11,CD.side)) #front waist side

    pnts=intersectCircles(aD1,front_dart_length,a12,CD.front_waist_width/2.0-distance(a2,aD1.i))
    if isBelow(a12,pnts[0]):
        aD1.o=pPoint(A,'aD1.o',pnts[0]) #front dart outside leg
    else:
        aD1.o=pPoint(A,'aD1.o',pnts[1]) #front dart outside leg
    adjustDartLength(a12,aD1,a2)
    updatePoint(aD1,downPoint(a_apex,front_dart_length/7.0))
    foldDart(A,aD1,a2) #creates aD1.m,aD1.oc,aD1.ic; dart folds toward pattern center

    #front control points
    #front armscye control points
    length1=distance(a8,a6)/3.0
    length2=distance(a6,a4)/3.0
    a6.c1=cPoint(A,'a6.c1',polarPoint(a8,length1,angleOfLine(a7,a8)+ANGLE90))
    angle=angleOfLine(a4,a8)
    angle2=angleOfLine(a6,a6.c1)
    angle3=(angle+angle2)/2.0
    a4.c2=cPoint(A,'a4.c2',polarPoint(a4,length2,angleOfLine(a4,a12)+ANGLE90))
    a6.c2=cPoint(A,'a6.c2',polarPoint(a6,length1,angle3))
    a4.c1=cPoint(A,'a4.c1',polarPoint(a6,length2,angle3-ANGLE180))
    #front waist control points
    length=distance(a12,aD1.o)/3.0 #from a12 to aD1.o
    aD1.o.c1=cPoint(A,'aD1.o.c1',polarPoint(a12,length,angleOfLine(a12,aD1.o)))
    aD1.o.c2=cPoint(A,'aD1.o.c2',polarPoint(aD1.o,length,angleOfLine(aD1.o,a12)))
    length=distance(a2,aD1.i)/3.0 #from aD1.i to a2
    a2.c1=cPoint(A,'a2.c1',polarPoint(aD1.i,length,angleOfLine(aD1.i,a2)))
    a2.c2=cPoint(A,'a2.c2',polarPoint(a2,length,angleOfLine(a2,aD1.i)))
    #front dart control points
    length=distance(aD1.o,aD1.m)/3.0 #b/w aD1.o & aD1.m
    aD1.m.c1=cPoint(A,'aD1.m.c1',polarPoint(aD1.o,length,angleOfLine(aD1.o,aD1.m)))
    aD1.m.c2=cPoint(A,'aD1.m.c2',polarPoint(aD1.m,length,angleOfLine(aD1.m,aD1.o)))
    length=distance(aD1.m,aD1.i)/3.0 #b/w aD1.m & aD1.i
    aD1.i.c1=cPoint(A,'aD1.i.c1',polarPoint(aD1.m,length,angleOfLine(aD1.m,aD1.i)))
    aD1.i.c2=cPoint(A,'aD1.i.c2',polarPoint(aD1.i,length,angleOfLine(aD1.i,aD1.m)))
    #front neck control points
    a7.c1=cPoint(A,'a7.c1',rightPoint(a1,distance(a1,a7)/2.0))
    a7.c2=cPoint(A,'a7.c2',downPoint(a7,distance(a1,a7)/6.0))
    FRONT_NECK_ANGLE=angleOfVector(a8,a7,a7.c2)

    #back
    b1=pPointXY(B,'b1',0.0,0.0) #back neck center
    b2=pPoint(B,'b2',downPoint(b1,CD.back_waist_length)) #back waist center
    b3=pPoint(B,'b3',downPoint(b1,CD.back_underarm_height)) #back undera13 center
    b4=pPoint(B,'b4',leftPoint(b3,CD.back_underarm_width/2.0)) #back undera13 side
    b5=pPoint(B,'b5',downPoint(b1,distance(b1,b3)*2/3.0)) #back across chest center
    b6=pPoint(B,'b6',leftPoint(b5,CD.across_chest/2.0)) #back across chest side
    pnts=intersectCircleAtX(b2,CD.back_neck_balance,-CD.neck_width/2.0)
    if isAbove(b2,pnts[0]):
        b7=pPoint(B,'b7',pnts[0]) #back neck side
    else:
        b7=pPoint(B,'b7',pnts[1]) #back neck side
    pnts=intersectCircles(b2,CD.back_shoulder_balance,b7,CD.shoulder)
    if isLeft(pnts[1],pnts[0]): #use the leftmost intersection
        b8=pPoint(B,'b8',pnts[0]) #back neck side
    else:
        b8=pPoint(B,'b8',pnts[1]) #back neck side
    b9=pPointXY(B,'b9',b6.x,b3.y) #back armscye corner
    b10=pPoint(B,'b10',downPoint(b3,distance(a4,a11))) #back bust center
    b11=pPoint(B,'b11',leftPoint(b10,CD.back_bust_width/2.0)) #back bust side
    b12=pPoint(B,'b12',intersectLineAtLength(b4,b11,CD.side)) #back waist side
    #back waist dart
    b_apex=pPoint(B,'b_apex',leftPoint(b3,distance(b5,b6)/2.0))
    back_dart_length=distance(b3,b2)
    bD1=pPoint(B,'bD1',b_apex) #back dart apex lower than b_apex
    bD1.i=pPoint(B,'bD1.i',downPoint(b_apex,back_dart_length)) #back dart inside leg
    pnts=intersectCircles(bD1,back_dart_length,b12,CD.back_waist_width/2.0-distance(b2,bD1.i))
    if isBelow(pnts[1],pnts[0]):  #if pnts[0] b5low pnts[1]
        bD1.o=pPoint(B,'bD1.o',pnts[0]) #back dart outside leg
    else:
        bD1.o=pPoint(B,'bD1.o',pnts[1])
    adjustDartLength(b12,bD1,b2)
    updatePoint(bD1,downPoint(b_apex,back_dart_length/7.0))
    foldDart(B,bD1,b2) #creates bD1.m,bD1.oc,bD1.ic; dart folds toward pattern center

    #back control points
    #back armscye control points
    length1=distance(b8,b6)/3.0
    length2=distance(b6,b4)/3.0
    b6.c1=cPoint(B,'b6.c1',polarPoint(b8,length1,angleOfLine(b7,b8)-ANGLE90))
    angle=angleOfLine(b4,b8)
    angle2=angleOfLine(b6,b6.c1)
    angle3=(angle+angle2)/2.0
    b4.c2=cPoint(B,'b4.c2',polarPoint(b4,length2,angleOfLine(b4,b12)-ANGLE90))
    b6.c2=cPoint(B,'b6.c2',polarPoint(b6,length1,angle3))
    b4.c1=cPoint(B,'b4.c1',polarPoint(b6,length2,angle3+ANGLE180))
    #back waist control points
    length=distance(b12,bD1.o)/3.0 #from b12 to bD1.o
    bD1.o.c1=cPoint(B,'bD1.o.c1',polarPoint(b12,length,angleOfLine(b12,bD1.o)))
    bD1.o.c2=cPoint(B,'bD1.o.c2',polarPoint(bD1.o,length,angleOfLine(bD1.o,b12)))
    length=distance(b2,bD1.i)/3.0 #from bD1.i to b2
    b2.c1=cPoint(B,'b2.c1',polarPoint(bD1.i,length,angleOfLine(bD1.i,b2)))
    b2.c2=cPoint(B,'b2.c2',polarPoint(b2,length,angleOfLine(b2,bD1.i)))
    #back dart control points
    angle=abs(angleOfVector(b2.c1,bD1.i,b2)) #from bD1.m to bD1.i
    length1=distance(bD1.m,bD1.i)/3.0
    bD1.i.c1=cPoint(B,'bD1.i.c1',intersectLineAtLength(bD1.m,bD1.i,length1))
    bD1.i.c2=cPoint(B,'bD1.i.c2',polarPoint(bD1.i,length1,angleOfLine(b2.c1,bD1.i)))
    length2=distance(bD1.o,bD1.m)/3.0
    bD1.m.c1=cPoint(B,'bD1.m.c1',polarPoint(bD1.o,length2,angleOfLine(bD1.o.c2,bD1.o)))
    bD1.m.c2=cPoint(B,'bD1.m.c2',intersectLineAtLength(bD1.m,bD1.o,length2))
    #back neck control points
    b7.c1=cPoint(B,'b7.c1',leftPoint(b1,distance(b1,b7)/2.0))
    b7.c2=cPoint(B,'b7.c2',polarPoint(b7,distance(b1,b7)/6.0,angleOfLine(b8,b7)+FRONT_NECK_ANGLE))

    #create dictionary
    var_keys_since_checkpoint=set(locals().keys())-set(checkpoint)
    new_vars=dict()
    for item in var_keys_since_checkpoint:
        if item[0] in ('a','b') and item[:5]!='angle' and item[:4]!='back':
            new_vars[item]=locals()[item]

    #return variable dictionary to the calling program
    return new_vars

#vi:set ts=4 sw=4 expandta2:

