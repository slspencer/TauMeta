# !/usr/bin/python
#
# single_breasted_dinner_tuxedo_tuxedo_1880.py
# Copyright (C) 2010, 2011, 2012 Susan Spencer, Steve Conklin <www.taumeta.org>

'''
Licensing paragraph :

1. CODE LICENSE :  GPL 2.0 +
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT FNY WARRFNTY; without even the implied warranty of
MERCHFNTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111 - 1307  USA

2. PATTERN LICENSE :  CC BY - NC 3.0
The output of this code is a pattern and is considered a
visual artwork. The pattern is licensed under
Attribution - NonCommercial 3.0 (CC BY - NC 3.0)
<http : //creativecommons.org/licenses/by - nc/3.0/>
Items made from the pattern may be sold;
the pattern may not be sold.

End of Licensing paragraph.
'''

from tmtpl.designbase import *
from tmtpl.document import *
from tmtpl.pattern import *
from tmtpl.patternmath import *
from tmtpl.constants import *
from tmtpl.utils import *

class Design(designBase):

    def pattern(self) :
        """
        Method defining a pattern design. This is where the designer places
        all elements of the design definition
        """

        # The designer must supply certain information to allow
        #   tracking and searching of patterns
        #
        # This group is all mandatory
        #
        self.setInfo('patternNumber', 'HM_1')
        self.setInfo('patternTitle', 'Single Breasted Tuxedo Jacket, circa 1880 to 1900')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'S.L.Spencer')
        self.setInfo('patternmakerName', 'S.L.Spencer')
        self.setInfo('description', """Men's Victorian tuxedo dinner jacket. Single breasted with shawl collar and two buttons.""")
        self.setInfo('category', 'Historical')
        self.setInfo('type', 'Design')
        #
        # The next group are all optional
        #
        self.setInfo('gender', 'M') # 'M',  'F',  or ''
        self.setInfo('yearstart', '1880')
        self.setInfo('yearend', '1900')
        self.setInfo('culture', 'European')
        self.setInfo('wearer', '')
        self.setInfo('source', '')
        self.setInfo('characterName', '')
        self.setInfo('recommendedFabric', '')
        self.setInfo('recommendedNotions', '')

        #get client data
        CD = self.CD #client data is prefaced with CD

        #create a pattern named 'tuxedo'
        tuxedo = self.addPattern('tuxedo')

        #create pattern pieces,  assign an id lettercd 
        A = tuxedo.addPiece('Tuxedo Back', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = tuxedo.addPiece('Tuxedo Front', 'B', fabric = 2, interfacing = 0, lining = 0)
        #C = bodice.addPiece('Tuxedo Sleeve', 'C', fabric = 2, interfacing = 0, lining = 0)

        # Tuxedo Back points
        scale = CD.bust / 2.0
        back_scale = CD.back_bust / 2.0
        f_underarm_height = 9.*CM
        f_bust_height = 18.*CM
        b_underarm_height = 18.*CM
        back_shoulder_ease = 1.*CM
        pA = A.addPoint('pA',  (0, 0)) #A back neck center
        pB = A.addPoint('pB', down(pA, 7.5*CM)) #B back shoulder center
        pC = A.addPoint('pC', down(pA, b_underarm_height)) #C back underarm center
        pD = A.addPoint('pD', down(pA, CD.back_waist_length)) #D back waist center
        pE = A.addPoint('pE', down(pD, CD.back_hip_height)) #E back hip center
        pF = A.addPoint('pF', down(pD, 1.5 * CD.back_hip_height)) #F back hem center
        BSH = A.addPoint('BSH', up(pD, CD.back_shoulder_height)) #back shoulder height
        BSW = A.addPoint('BSW', right(BSH, CD.back_shoulder_width / 2.0)) #back shoulder width
        p1 = A.addPoint('p1', right(pA, CD.back_shoulder_width / 2.0)) #back neck side ref point
        #p2 = A.addPoint('p2', right(pB, CD.back_shoulder_width / 2.0)) #back shoulder side ref point
        p3 = A.addPoint('p3', right(pC, CD.back_shoulder_width / 2.0)) #back underarm side ref point
        p4 = A.addPoint('p4', right(pD, CD.back_shoulder_width / 2.0)) #back waist side ref point
        p5 = A.addPoint('p5', right(pE, CD.back_shoulder_width / 2.0)) #back hip side ref point
        p6 = A.addPoint('p6', right(pF, CD.back_shoulder_width / 2.0)) #back hem side ref point
        p7 = A.addPoint('p7', right(pC, 1.*CM)) 
        p8 = A.addPoint('p8', right(pD, 2.5*CM))
        p9 = A.addPoint('p9', right(pE, 1.75*CM))
        p10 = A.addPoint('p10', right(pF, 1.5*CM))
        p11 = A.addPoint('p11', right(pA, (scale / 8.) + 2.*CM)) #back neck width ref point
        #p12 = A.addPoint('p12', (p11.x, BSH.y)) #back
        #p13 = A.addPoint('p13', right(p2, 1.*CM)) #back shoulder point        
        p2b = A.addPoint('p2b', highestP(onCircleAtX(p8, CD.back_shoulder_balance, BSW.x))) #back shoulder point ref
        p13b = A.addPoint('p13b', right(p2b, 1.*CM)) #back shoulder point
        p12b = A.addPoint('p12b', leftmostP(onCircleAtY(p2b, CD.shoulder + back_shoulder_ease, BSH.y))) #back neck point
        p14 = A.addPoint('p14', up(p3, scale / 8.)) #back mid-scye
        p15 = A.addPoint('p15', up(p3, scale / 4.)) #back sleeve balance point
        p16 = A.addPoint('p16', left(p3, 1.*CM))
        p17 = A.addPoint('p17', left (p4, 3.*CM))
        p18 = A.addPoint('p18', left(p5, 1.75*CM))
        p19 = A.addPoint('p19', left(p6, 1.5*CM))
        
        #control points
        pA.addOutpoint(right(pA, distance(pA, p12b) / 3.0))
        p12b.addInpoint(polar(p12b, distance(pA, p12b) / 3.0, angleOfLine(p12b, p13b) + ANGLE90))
        p13b.addOutpoint(polar(p13b, distance(p13b, p15) / 3.0, angleOfLine(p12b, p13b) + ANGLE90))
        p15.addInpoint(polar(p15, distance(p13b, p15) / 3.0, (ANGLE270 + angleOfLine(p13b.outpoint, p13b)) / 2.0))
        p15.addOutpoint(polar(p15, distance(p15, p14) / 3.0,  angleOfLine(p15.inpoint, p15)))
        p14.addInpoint(polar(p14, distance(p15, p14) / 3.0, ANGLE270 - angleOfVector(p2b, p15, p15.inpoint)))
        p16.addOutpoint(polar(p16, distance(p16, p17) / 3.0, angleOfLine(p14, p16)))
        p17.addInpoint(up(p17, distance(p16, p17) / 3.0))
        p17.addOutpoint(down(p17, distance(p17, p18) / 3.0))
        p18.addInpoint(polar(p18, distance(p17, p18) / 3.0, angleOfLine(p19, p18)))
        p9.addOutpoint(polar(p9, distance(p9, p8) / 3.0, angleOfLine(p10, p9)))
        p8.addInpoint(down(p8, distance(p9, p8) / 3.0))
        p8.addOutpoint(up(p8, distance(p8, p7) / 3.0))
        p7.addInpoint(polar(p7, distance(p8, p7) / 3.0, angleOfLine(p7, p8.outpoint)))
        p7.addOutpoint(polar(p7, distance(p7, pB) / 3.0, angleOfLine(p7.inpoint, p7)))
        pB.addInpoint(down(pB, distance(p7, pB) / 3.0))
        
        #Tuxedo Front B
        FSH = B.addPoint('FSH', up(p4, CD.front_shoulder_height))         
        p20 = B.addPoint('p20', right(p3, 7.5*CM))
        p21 = B.addPoint('p21', right(p14, 8.5*CM))
        p22 = B.addPoint('p22', right(p4, 7.5*CM))      
        p23 = B.addPoint('p23', right(p5, 3.5*CM))
        p24 = B.addPoint('p24', right(p6, 2.5*CM))
        p25 = B.addPoint('p25', right(p20, (scale / 4.0) + 2.*CM))
        p26 = B.addPoint('p26', (p25.x, FSH.y))
        p27 = B.addPoint('p27', right(p26, (scale / 8.0) + 1.5*CM))
        p28 = B.addPoint('p28', down(p26, 1.3*CM))
        p29 = B.addPoint('p29', onLineAtLength(p27, p28, distance(p12b, p13b) - back_shoulder_ease))
        p30 = B.addPoint('p30', up(p25, 2.5*CM))
        pG = B.addPoint('pG', midPoint(p29, p30)) #midpoint of line across front armscye
        pH = B.addPoint('pH', polar(pG, 2.*CM, angleOfLine(p29, p30) - ANGLE90)) #midpoint of front armscye
        pI = B.addPoint('pI', polar(p25, 2.*CM, ANGLE225))
        pJ = B.addPoint('pJ', polar(p20, 4.*CM, ANGLE315))
        p31 = B.addPoint('p31', right(p25, (scale / 2.0) - 3.5*CM)) #marks centerfrontline at chest/underarmline
        p32 = B.addPoint('p32', (p31.x, p22.y)) #centerfrontline at waist
        p33 = B.addPoint('p33', (p31.x, p23.y)) #centerfrontline at hip
        p34 = B.addPoint('p34', (p31.x, p24.y)) #centerfrontline at hem
        p35 = B.addPoint('p35', down(p34, 2.5*CM))
        pK = B.addPoint('pK', up(p32, 2.5*CM))
        pL = B.addPoint('pL', down(pK, 10.*CM))
        p36 = B.addPoint('p36', right(pK, 2.*CM))
        #p37 = B.addPoint('p37', up(p31, 14.*CM))
        p37b = B.addPoint('p37b', up(p32, CD.front_waist_length))
        p38 = B.addPoint('p38', down(p27, 6.5*CM))
        p39 = B.addPoint('p39', polar(p38, 2.5*CM, ANGLE315))
        p40 = B.addPoint('p40', extendLine(p29, p27, 2.5*CM))
        p41 = B.addPoint('p41', intersectLines(p40,p36, p38, p37b))
        p42 = B.addPoint('p42', extendLine(p38, p37b, 1.*CM))
        p43 = B.addPoint('p43', right(p31, 3.*CM))
        p44 = B.addPoint('p44', midPoint(p41, p42))
        p45 = B.addPoint('p45', right(pL, 1.5*CM))
        p46 = B.addPoint('p46', left(p33, 1.*CM))
        p47 = B.addPoint('p47', left(p34, 5.*CM))
        p48 = B.addPoint('p48', onLineAtLength(p35, p24, distance(p35, p24) / 4.0))
        #lapel dart
        BD1 = B.addPoint('BD1', polar(p44, 9.*CM, angleOfLine(p41, p42) + ANGLE90))        
        BD1.i = B.addPoint('BD1.i', onLineAtLength(p44, p41, 0.75*CM))
        BD1.o = B.addPoint('BD1.o', onLineAtLength(p44, p42, 0.75*CM))
        extendDart(p41, BD1, p42)
        foldDart(BD1, p41)
        #hip pocket
        pM = B.addPoint('pM', down(p25, distance(p31, p32) + distance(p32, p33)/3.0))
        pN = B.addPoint('pN', polar(pM, 7.5*CM, angleOfLine(p35, p24)))
        pO = B.addPoint('pO', polar(pM, 7.5*CM, angleOfLine(pN, pM)))
        pNb = B.addPoint('pNb', polar(pN, 4.5*CM, angleOfLine(pN, pO) + ANGLE90))
        pOb = B.addPoint('pOb', polar(pO, 2.25*CM, angleOfLine(pN, pO) + ANGLE90))
        pMb = B.addPoint('pMb', polar(pNb, 4.25*CM, angleOfLine(pN, pO)))

   
        #Tuxedo Back A
        pnt1 = dPnt((p12b.x, pD.y))
        A.setLabelPosition(pnt1)
        pnt2 = up(pnt1, 0.5*IN)
        A.setLetter(pnt2, scaleby = 10.0)
        AG1 = dPnt(((p8.x + p12b.x)/2.0, pB.y))
        AG2 = down(AG1, distance(pB, pE))
        A.addGrainLine(AG1, AG2)
        A.addGridLine(['M', BSH, 'L', BSW, 'L', p6,
                       'L', pF, 'L', BSH])
        path = (['M', pA, 'C', p12b, 'L', p13b,
                       'C', p15, 'C', p14, 
                       'L', p16, 'C', p17, 'C', p18, 'L', p19, 
                       'L', p10, 'L', p9, 'C', p8, 'C', p7, 'C', pB, 'L', pA])
        A.addSeamLine(path)
        A.addCuttingLine(path)
        
        #Tuxedo Front B
        pnt1 = dPnt(((p27.x + p28.x)/2.0, p25.y))
        B.setLabelPosition(pnt1)
        pnt2 = up(pnt1, 0.5*IN)
        B.setLetter(pnt2, scaleby = 10.0)
        BG1 = dPnt((BD1.x, p31.y))
        BG2 = down(BG1, distance(p31, p33))
        B.addGrainLine(BG1, BG2)
        path = (['M', FSH, 'L', p6, 'L', p34, 'L', p37b, 'L', p38, 'L', p27, 'L', FSH])
        B.addGridLine(path)
        path = (['M', BD1.ic, 'L', BD1, 'L', BD1.oc])
        B.addDartLine(path)    
        path = (['M', p27, 'L', p39, 'L', p41, 'L', BD1.i, 'L', BD1.m, 'L', BD1.o, 'L', p42,
                       'L', p43, 'L', p36, 'L', p45, 'L', p46, 'L', p47, 'L', p48, 'L', p24,
                       'L', p23, 'L', p22, 'L', p20, 'L', p21, 
                       'L', pJ, 'L', pI, 'L', p30, 'L', pH, 'L', p29, 'L', p27])
        B.addSeamLine(path)
        B.addCuttingLine(path)        
        
        #call draw() to generate svg file
        self.draw()

        return                

