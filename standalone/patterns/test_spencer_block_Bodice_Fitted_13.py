#!/usr/bin/env python
#Spencer_block_Bodice_Fitted_12.py

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
    #the front underarm control handle for a4 was adjusted to be parallel to the front bust dart.
    #back waist side is calculated by:
    #1. extending the back waist by 1/12 additional length.
    #2. creating the back waist dart bD1 with this extra width.
    #3. creating back waist side b12 intersecting the side length from the underarm with the remaining waist width from the outside of the dart

    #start new_var dictionary
    checkpoint=['checkpoint']+locals().keys()[:]
    #front
    a1=Pnt(0.0,0.0) #front neck center
    a2=downPoint(a1,CD.front_waist_length) #front waist center
    a3=downPoint(a1,CD.front_underarm_height) #front underarm center
    a4=rightPoint(a3,CD.front_underarm_width/2.0) #front underarm side
    #a5=downPoint(a1,distance(a1,a3)/2.0) #front across chest center
    a5=downPoint(a1,0.75*distance(a1,a3)) #front across chest center - 3/4ths of a1 to a3
    a6=rightPoint(a5,CD.across_chest/2.0) #front across chest side
    pnts=intersectCircles(a1,CD.across_chest_balance,a2,CD.front_shoulder_balance)
    if isRight(a1,pnts[0]): # use the rightmost intersection
        a8=pnts[0] #front shoulder tip
    else:
        a8=pnts[1] #front shoulder tip
    pnts=intersectCircles(a8,CD.shoulder,a2,CD.front_shoulder_balance)
    if isAbove(pnts[1],pnts[0]): #use the highest intersection
        a7=pnts[0] #front neck side
    else:
        a7=pPoint(A,'a8',pnts[1]) #front neck side
    a9=Pnt(a6.x,a3.y) #front armscye corner
    a10=downPoint(a1,CD.front_bust_height) #front bust center
    a_apex=rightPoint(a10,CD.bust_point_distance/2.0)
    #a11-----
    #a11=rightPoint(a10,CD.front_bust_width/2.0) #front bust side
    #angle=-angleOfVector(a4,a_apex,a11)/2.0 #angle sweeps counterclockwise
    #pnt1=polarPoint(a_apex,distance(a_apex,a11),angle)
    #updatePoint(a11,pnt1) #front bust side adjusted up by 1/2 angle of front dart apex to underarm
    pnts=intersectCircles(a4,CD.bust_underarm_height,a_apex,CD.front_bust_width/2.0-CD.bust_point_distance/2.0)
    if isBelow(pnts[1],pnts[0]): #if pnts[0] below pnts[1]
        a11=pnts[0]
    else:
        a11=pnts[1]

    if debug:
        i = 0
        for pnt1 in a_apex,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11:
            if i==0:
                print('a_apex =',pnt1.x,pnt1.y)
            else:
                print('a',i,'=',pnt1.x,pnt1.y)
            i=i+1

    pnts=intersectCircles(a1,CD.front_waist_balance,a11,CD.side-distance(a4,a11))
    if isBelow(pnts[1],pnts[0]):  #if pnts[0] below pnts[1]
        a12=pnts[0] #front waist side
    else:
        a12=pnts[1] #front waist side
    a13=intersectLines(a1,a12,a_apex,a11)
    a14=PntP(a13) #copy of a13 in case 2nd dart is needed

    #front waist dart
    aD1=downPoint(a_apex,abs(a_apex.y-a2.y)/7.0) #front dart apex is lower than a_apex
    pnt1=Pnt(aD1.x,a2.y)
    aD1.i=leftPoint(pnt1,distance(a2,pnt1)/5.0)
    dart_length=distance(aD1,aD1.i)
    pnts=intersectCircles(aD1,dart_length,a12,CD.front_waist_width/2.0-distance(a2,aD1.i))
    if isBelow(pnts[1],pnts[0]): #if pnts[0] below pnts[1]
        aD1.o=pnts[0] #adjust back waist side
    else:
        aD1.o=pnts[1] #adjust back waist side

    #front bust dart
    ###if distance(aD1.i,aD1.o)>CD.front_waist_width/6.0: #if waistdart width greater than 1/3 of half the front waist width
    #create 2nd dart
    aD2=PntP(a_apex) #2nd dart point is to the right of a_apex, same distance away from a_apex as aD1
    print 'aD2 =',aD2.x,aD2.y
    aD2.i=intersectLines(a4,a12,a_apex,a11)
    aD2.o=rightPoint(a_apex,distance(a_apex,aD2.i))
    updatePoint(aD2,rightPoint(a_apex,distance(a_apex,aD1)))
    pivot=a_apex
    rotation_angle=angleOfVector(aD2.i,a_apex,aD2.o)
    slashAndSpread(pivot,rotation_angle,a12,a14,aD1.o)
    pnt1=intersectLines(a1,a13,aD2,aD2.i)
    updatePoint(a13,pnt1)
    pnt2=rightPoint(aD2,distance(aD2,a13))
    updatePoint(a14,pnt2)
    pnts=intersectCircles(aD2.o,distance(aD2.o,a12),a14,CD.front_waist_balance-distance(a1,a13))
    if isBelow(pnts[1],pnts[0]): #if pnts[0] is below pnts[1]
        updatePoint(a12,pnts[0])
    else:
        updatePoint(a12,pnts[1])
    pnts=intersectCircles(aD1,distance(aD1,aD1.i),a12,CD.front_waist_width/2.0-distance(a2,aD1.i))
    if isBelow(pnts[1],pnts[0]):
        updatePoint(aD1.o,pnts[0])
    else:
        updatePoint(aD1.o,pnts[1])


    #create curve at dart base, then shape dart fold to match curve
    #TODO: rename adjustDartLength() as smoothDartOnCurve()
    #TODO: rename foldDart2() as createDartFold()
    adjustDartLength(a12,aD1,a2,extension=0.5)
    pnts=intersectCircles(aD1,distance(aD1,aD1.o),a12,CD.front_waist_width/2.0-distance(a2,aD1.i))
    pnt1=lowest(pnts[0],pnts[1])
    updatePoint(aD1.o,pnt1)
    foldDart2(aD1,a2) #creates aD1.m,aD1.oc,aD1.ic; dart folds in toward pattern center a2
    #do not call adjustDartLength(a12,aD2,a4) -- dart aD2 is not on a curve
    foldDart2(aD2,a4) #creates aD2.m,aD2.oc,aD2.ic; dart folds up toward underarm a4

    #front control points
    #front armscye control points
    length1=distance(a8,a6)/3.0
    length2=distance(a6,a4)/3.0
    a6.c1=polarPoint(a8,length1,angleOfLine(a7,a8)+ANGLE90)
    angle=angleOfLine(a4,a8)
    angle2=angleOfLine(a6,a6.c1)
    angle3=(angle+angle2)/2.0
    #a4.c2=polarPoint(a4,length2,angleOfLine(a4,a12)+ANGLE90)
    a4.c2=polarPoint(a4,length2,angleOfLine(aD2.i,a_apex))
    a6.c2=polarPoint(a6,length1,angle3)
    a4.c1=polarPoint(a6,length2,angle3-ANGLE180)
    #front waist control points
    length=distance(a12,aD1.o)/6.0 #from a12 to aD1.o
    aD1.o.c1=polarPoint(a12,length,angleOfLine(a12,aD1.o))
    #aD1.o.c2=polarPoint(aD1.o,length,angleOfLine(aD1.o,a12))
    aD1.o.c2=polarPoint(aD1.o,length,angleOfLine(aD1.m,aD1.o))
    a2.c2=rightPoint(a2,distance(a2,aD1.i)/2.0)
    a2.c1=polarPoint(aD1.i,distance(a2,aD1.i)/6.0,angleOfLine(aD1.i,a2.c2))
    #front dart control points
    length=distance(aD1.o,aD1.m)/3.0 #b/w aD1.o & aD1.m
    aD1.m.c1=polarPoint(aD1.o,length,angleOfLine(aD1.o,aD1.m))
    aD1.m.c2=polarPoint(aD1.m,length,angleOfLine(aD1.m,aD1.o))
    length=distance(aD1.m,aD1.i)/3.0 #b/w aD1.m & aD1.i
    aD1.i.c1=polarPoint(aD1.m,length,angleOfLine(aD1.m,aD1.i))
    aD1.i.c2=polarPoint(aD1.i,length,angleOfLine(aD1.i,aD1.m))
    #front neck control points
    a7.c1=rightPoint(a1,abs(a1.x-a7.x)*4/5.0)
    a7.c2=polarPoint(a7,distance(a7,a7.c1)/2.0,angleOfLine(a7,a7.c1))
    FRONT_NECK_ANGLE=angleOfVector(a8,a7,a7.c2)

    #back
    b1=Pnt(0.0,0.0) #back neck center
    b2=downPoint(b1,CD.back_waist_length) #back waist center
    b3=downPoint(b1,CD.back_underarm_height) #back underarm center
    b4=leftPoint(b3,CD.back_underarm_width/2.0) #back underarm side
    #b5=downPoint(b1,distance(b1,b3)*2/3.0) #back across chest center
    b5=downPoint(b1,0.75*distance(b1,b3)) #back across chest center - 3/4ths distance b1 to b3
    b6=leftPoint(b5,CD.across_chest/2.0) #back across chest side
    pnts=intersectCircles(b1,CD.across_back_balance,b2,CD.back_shoulder_balance)
    if isLeft(b1,pnts[0]): # use the intersection to the left of b1
        b8=pnts[0] #back shoulder tip
    else:
        b8=pnts[1] #back shoulder tip
    pnts=intersectCircles(b2,CD.back_neck_balance,b8,CD.shoulder)
    if isAbove(pnts[1],pnts[0]): #use the highest intersection
        b7=pnts[0] #back neck side
    else:
        b7=pnts[1] #back neck side
    b9=Pnt(b6.x,b3.y) #back armscye corner
    b10=downPoint(b3,distance(a4,a11)) #back bust center
    b11=leftPoint(b10,CD.back_bust_width/2.0) #back bust side


    #back waist dart
    back_width=CD.back_waist_width/2.0
    dart_width=back_width/6.0 #based on 24" waist with 1" back waist darts
    pnts=intersectCircles(b1,CD.back_waist_balance,b2,back_width)
    if isLeft(pnts[1],pnts[0]):  #use the leftmost intersection
        tmp_waist_side=pnts[0] #temporary back waist side
    else:
        tmp_waist_side=pnts[1] #temporary back waist side


    tws=pPoint(B,'tws',tmp_waist_side)
    bD1=intersectLines(b1,tmp_waist_side,b2,b8) #back dart apex
    b_apex=Pnt(bD1.x,b3.y) #bodice back apex is on bust line

    pnt1=intersectLines(bD1,b_apex,b2,tmp_waist_side) #back dart midline intersected with line b2-tmp_waist_side
    mid_pnt=pPoint(B,'mid',Pnt(bD1.x,(b2.y+pnt1.y)/2.0)) #halfway b/w pnt1.y & b2.y
    #mid_pnt=intersectLines(bD1,b_apex,b2,tmp_waist_side) #back dart midline intersected with line b2-tmp_waist_side

    bD1.i=rightPoint(mid_pnt,dart_width/2.0)
    bD1.o=leftPoint(mid_pnt,dart_width/2.0)
    inside_length=distance(b2,bD1.i)
    outside_length=back_width-inside_length
    #update b4 if needed
    if isAbove(b3,bD1): #if bD1 is above b3
        b13=intersectLines(bD1,bD1.i,b3,b4)
        b14=intersectLines(bD1,bD1.o,b3,b4)
        pnt1=intersectLineAtLength(b3,b4,distance(b3,b4)+distance(b13,b14))
        updatePoint(b4,pnt1)
    #update b11 if needed
    if isAbove(b10,bD1): #if bD1 is above b10
        b15=intersectLines(bD1,bD1.i,b10,b11)
        b16=intersectLines(bD1,bD1.o,b10,b11)
        pnt1=intersectLineAtLength(b10,b11,distance(b10,b11)+distance(b15,b16))
        updatePoint(b11,pnt1)
    #b12 - back waist side
    pnts=intersectCircles(b4,CD.side,bD1.o,outside_length)
    if isBelow(pnts[1],pnts[0]):  #use the leftmost intersection
        b12=pnts[0] #back waist side
    else:
        b12=pnts[1] #back waist side
    #adjust dart for waist curve
    adjustDartLength(b12,bD1,b2,extension=0.3)
    #create dart fold to match waist curve
    foldDart2(bD1,b2) #creates bD1.m,bD1.oc,bD1.ic; dart folds toward pattern center

    #back dart control points
    length1=distance(b12,bD1.o)/3.0 #from b12 to bD1.o
    length2=distance(bD1.i,b2)/3.0 #from bD1.i to b2
    angle1=angleOfLine(b12,bD1.o) #B angle from b12 to bD1.o
    angle2=angleOfVector(bD1.o,bD1,bD1.i) #C angle of dart
    angle3=angleOfLine(bD1.i,b2) #A angle from bD1.i to b2 - too flat
    angle4=angle1-angle2 #D rotated angle from b12 to bD1.o - too steep
    angle5=(angle4+angle3)/2.0 #E angle at dart - 1/2 between angle3 & angle4
    #angle6=angle5-ANGLE180-angle2 # F opposite of angle5 before rotation
    b2.c1=polarPoint(bD1.i,length2,angle5)
    b2.c2=leftPoint(b2,length2)
    bD1.o.c1=polarPoint(b12,length1,angle1)
    angle6=angleOfLine(b2.c1,bD1.i)+angle2
    bD1.o.c2=polarPoint(bD1.o,length1,angle6)


    angle=abs(angleOfVector(b2.c1,bD1.i,b2)) #from bD1.m to bD1.i
    length1=distance(bD1.m,bD1.i)/3.0
    bD1.i.c1=intersectLineAtLength(bD1.m,bD1.i,length1)
    bD1.i.c2=polarPoint(bD1.i,length1,angleOfLine(b2.c1,bD1.i))
    length2=distance(bD1.o,bD1.m)/3.0
    bD1.m.c1=polarPoint(bD1.o,length2,angleOfLine(bD1.o.c2,bD1.o))
    bD1.m.c2=intersectLineAtLength(bD1.m,bD1.o,length2)

    #back control points
    #back armscye control points
    length1=distance(b8,b6)/3.0
    length2=distance(b6,b4)/3.0
    b6.c1=polarPoint(b8,length1,angleOfLine(b7,b8)-ANGLE90)
    angle=angleOfLine(b4,b8)
    angle=angleOfLine(b4,b8)
    angle2=angleOfLine(b6,b6.c1)
    angle3=(angle+angle2)/2.0
    b4.c2=polarPoint(b4,length2,angleOfLine(b4,b12)-ANGLE90)
    b6.c2=polarPoint(b6,length1,angle3)
    b4.c1=polarPoint(b6,length2,angle3+ANGLE180)

    #back neck control points
    length1=abs(b7.x-a1.x)*2/3.0
    b7.c1=leftPoint(b1,length1)
    angle1=(angleOfLine(b7,b7.c1)+ANGLE90)/2.0 #angle1 is halfway b/w vertical line & angle to 1st control point
    b7.c2=polarPoint(b7,distance(b7,b7.c1)/2.0,angle1)

    #create dictionary
    var_keys_since_checkpoint=set(locals().keys())-set(checkpoint)
    new_vars=dict()
    for item in var_keys_since_checkpoint:
        if item[0] in ('a','b') and item[:5]!='angle' and item[:4]!='back':
            new_vars[item]=locals()[item]

    #return variable dictionary to the calling program
    return new_vars

#vi:set ts=4 sw=4 expandta2:

