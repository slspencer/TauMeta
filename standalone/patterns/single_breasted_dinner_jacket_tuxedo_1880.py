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
        #B = bodice.addPiece('Tuxedo Front', 'B', fabric = 2, interfacing = 0, lining = 0)
        #C = bodice.addPiece('Tuxedo Sleeve', 'C', fabric = 2, interfacing = 0, lining = 0)

        # Tuxedo Back points
        scale = CD.bust / 2.0
        back_scale = CD.back_bust / 2.0
        f_underarm_height = 9.0 * CM
        f_bust_height = 18 * CM
        b_underarm_height = 18.0 * CM
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
        p9 = A.addPoint('p9', right(pE, 1.5*CM))
        p10 = A.addPoint('p10', right(pF, 1.5*CM))
        p11 = A.addPoint('p11', right(pA, (scale / 8.) + 2.*CM)) #back neck width ref point
        #p12 = A.addPoint('p12', (p11.x, BSH.y)) #back
        #p13 = A.addPoint('p13', right(p2, 1.*CM)) #back shoulder point        
        p2b = A.addPoint('p2b', highestP(onCircleAtX(p8, CD.back_shoulder_balance, BSW.x))) #back shoulder point ref
        p13b = A.addPoint('p13b', right(p2b, 1.*CM)) #back shoulder point
        p12b = A.addPoint('p12b', leftmostP(onCircleAtY(p2b, CD.shoulder, BSH.y))) #back neck point
        p14 = A.addPoint('p14', up(p3, scale / 8.)) #back mid-scye
        p15 = A.addPoint('p15', up(p3, scale / 4.)) #back sleeve balance point
        p16 = A.addPoint('p16', left(p3, 1.*CM))
        p17 = A.addPoint('p17', left (p4, 3*CM))
        p18 = A.addPoint('p18', left(p5, 2.*CM))
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
        pth = (['M', pA, 'C', p12b, 'L', p13b,
                       'C', p15, 'C', p14, 
                       'L', p16, 'C', p17, 'C', p18, 'L', p19, 
                       'L', p10, 'L', p9, 'C', p8, 'C', p7, 'C', pB, 'L', pA])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)
        
        #call draw() to generate svg file
        self.draw()

        return                

