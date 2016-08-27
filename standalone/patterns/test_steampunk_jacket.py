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
        self.setInfo('patternNumber', 'Stp_J_1')
        self.setInfo('patternTitle', 'Spencer Steampunk Jacket')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'S.L.Spencer')
        self.setInfo('patternmakerName', 'S.L.Spencer')
        self.setInfo('description', """Steampunk Jacket """)
        self.setInfo('category', 'Shirt/TShirt/Blouse')
        self.setInfo('type', 'Block')
        #
        # The next group are all optional
        #
        self.setInfo('gender', '') # 'M',  'F',  or ''
        self.setInfo('yearstart', '1850')
        self.setInfo('yearend', '')
        self.setInfo('culture', 'European')
        self.setInfo('wearer', '')
        self.setInfo('source', '')
        self.setInfo('characterName', '')
        self.setInfo('recommendedFabric', '')
        self.setInfo('recommendedNotions', '')

        #get client data
        CD = self.CD #client data is prefaced with CD

        #create a pattern named 'bodice'
        bodice = self.addPattern('bodice')

        # measurement constants
        #in_to_pt         = ( 72 / 1    )         #convert inches to printer's points
        #cm_to_pt       = ( 72 / 2.54  )          #convert centimeters to printer's points - 72pt per 2.54 cm
        #cm_to_in        = ( 1 / 2.54 )           #convert centimeters to inches - 1in per 2.54cm
        #in_to_cm        = ( 2.54 / 1 )           #convert inches to centimeters
        
        # sewing constants
        #quarter_seam_allowance = ( in_to_pt * 1 / 4 )   # 1/4" seam allowance
        #seam_allowance              = ( in_to_pt * 5 / 8 )   # 5/8" seam allowance
        #hem_allowance               = ( in_to_pt * 2     )    # 2" seam allowance
        #pattern_offset                 = ( in_to_pt * 3     )    # 3" between patterns

        #get client data
        CD = self.CD #client data is prefaced with CD
        CM = CD.back_waist_length/44.5
        JACKET_HEM_ALLOWANCE = 5*CM
        SCALE = CD.bust/2.0
        HALF_SCALE = SCALE/2.0
        FOURTH_SCALE = SCALE/4.0
        EIGHTH_SCALE = SCALE/8.0

        #create a pattern named 'bodice'
        jacket = self.addPattern('jacket')

        #create pattern pieces,  assign an id lettercd 
        A = jacket.addPiece('Jacket Back', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = jacket.addPiece('Jacket Front', 'B', fabric = 2, interfacing = 0, lining = 0)
        #C = jacket.addPiece('Jacket Sleeve', 'C', fabric = 2, interfacing = 0, lining = 0)

        # Jacket Back
        # back center ref for top, shoulder, chest, waist, hip, hem, hem allowance
        a0 = A.addPoint('a0', (0, 0)) # start back neck center - nape
        a1 = A.addPoint('a1', down(a0, 0.168*CD.back_waist_length)) #back shoulder center ref
        a2 = A.addPoint('a2', down(a0, 0.54*CD.back_waist_length)) #back chest center ref
        a3 = A.addPoint('a3', down(a0, CD.back_waist_length)) #back waist center ref
        a4 = A.addPoint('a4', down(a3, CD.back_hip_height)) #back hip center ref
        a5 = A.addPoint('a5', down(a3, 1.5*CD.back_hip_height)) #back hem center ref
        a6 = A.addPoint('a6', down(a5, HEM_ALLOWANCE)) #back hem allowance center ref

        # back side ref points for top, shoulder, chest, waist, hip, hem, hem allowance
        a7 = A.addPoint('a7', right(a0, CD.across_back/2)) #back top side ref
        a8 = A.addPoint('a8', right(a1, CD.across_back/2)) #back shoulder side ref
        a9 = A.addPoint('a9', right(a2, CD.across_back/2)) #back chest side ref
        a10 = A.addPoint('a10', right(a3, CD.across_back/2)) #back waist side ref
        a11 = A.addPoint('a11', right(a4, CD.across_back/2)) #back hip side ref
        a12 = A.addPoint('a12', right(a5, CD.across_back/2)) #back hem side ref
        a13 = A.addPoint('a13', right(a6, CD.across_back/2)) #back hem allowance side ref
        
        # back center seam
        a14 = A.addPoint('a14', right(a2, 1.0*CM)) #back chest center
        a15 = A.addPoint('a15', right(a3, 2.5*CM)) #back waist center
        a16 = A.addPoint('a16', right(a4, 1.75*CM)) #back hip center
        a17 = A.addPoint('a17', right(a5, 1.5*CM)) #back hem center
        a18 = A.addPoint('a18', right(a6, 1.5*CM)) #back hem allowance center
        
        #back neck
        a19 = A.addPoint('a19', right(a0, EIGHTH_SCALE + 2*CM)) #back neck ref point
        a20 = A.addPoint('a20', up(a19, 2*CM)) #back neck side point
        
        #back shoulder
        a21 = A.addPoint('a21', right(a8,1*CM)) #back shoulder point
        a22 = A.addPoint('a22', down(a8, 3*distance(a21,a9)/11.0)) #back armhole/sleeve balance point        
        a23 = A.addPoint('a23', up(a9, 4*distance(a21,a9)/11.0)) #back armhole midpoint
        
        #back side seam
        a24 = A.addPoint('a24', left(a9, 1*CM)) #back chest side
        a25 = A.addPoint('a25', left(a10, 3*CM)) #back waist side
        a26 = A.addPoint('a26', left(a11, 2*CM)) #back hip side
        a27 = A.addPoint('a27', left(a12, 2*CM)) #back hem side
        a28 = A.addPoint('a28', left(a13, 2*CM)) #back hem allowance side
        
        # curve control points
        #b/w a0 & a20
        a0.addOutpoint(right(a0,distance(a0,a19)/2))
        a20.addInpoint(polar(a20,distance(a20,a19)/2,angleOfLine(a20,a21)+angleOfDegree(100)))
        #b/2 a20,a21
        a20.addOutpoint(polar(a20,distance(a20,a21)/3.0,angleOfLine(a20,a21)+angleOfDegree(5)))
        a21.addInpoint(polar(a21,distance(a20,a21)/3.0, angleOfLine(a21,a20)-angleOfDegree(5)))
        # armhole
        a23.addInpoint(polar(a23,distance(a22,a23)/3.0, angleOfDegree(265)))
        a22.addOutpoint(polar(a22,distance(a22,a23)/3.0, angleOfLine(a21,a23.inpoint)))        
        a22.addInpoint(polar(a22,distance(a22,a21)/3.0, angleOfLine(a23.inpoint,a21)))
        a21.addOutpoint(polar(a21,distance(a22,a21)/3.0, angleOfLine(a21,a22.inpoint)))
        #b/w a24, a25
        a24.addOutpoint(polar(a24,distance(a24,a25)/3.0, angleOfLine(a23,a24)))
        a25.addInpoint(up(a25,distance(a24,a25)/6.0))
        #b/w a25,a25
        a25.addOutpoint(down(a25,distance(a25,a26)/6.0))
        a26.addInpoint(polar(a26,distance(a25,a26)/2.0, angleOfLine(a27,a26)))
        #b/w a16,a15
        a16.addOutpoint(polar(a16,distance(a16,a15)/2.0, angleOfLine(a17,a16)))
        a15.addInpoint(down(a15,distance(a16,a15)/6.0))
        #b/w a15,a14
        a15.addOutpoint(up(a15,distance(a15,a14)/6.0))
        a14.addInpoint(polar(a14,distance(a15,a14)/3.0, angleOfLine(a1,a15)))
        #b/w a14, a0
        a14.addOutpoint(polar(a14,distance(a14,a1)/3.0, angleOfLine(a15,a1)))
        a0.addInpoint(down(a0,distance(a0,a14)/3.0))
        
        #Jacket Front
        #grid ref points
        b0 = B.addPoint('b0',a0)
        b1 = B.addPoint('b1',a1)
        b2 = B.addPoint('b2',a2)
        b3 = B.addPoint('b3',a3)
        b4 = B.addPoint('b4',a4)
        b5 = B.addPoint('b5',a5)
        b6 = B.addPoint('b6',a6)
        
        b7 = B.addPoint('b7', right(b0, 0.875*SCALE)) #front shoulder center
        b8 = B.addPoint('b8', (b7.x, a2.y)) #front chest center
        b9 = B.addPoint('b9', (b7.x, a3.y)) #front waist center
        b10 = B.addPoint('b10', (b7.x, a4.y)) #front hip center
        b11 = B.addPoint('b11', (b7.x, a5.y)) #front hem center
        b12 = B.addPoint('b12', (b7.x, a6.y)) #front hem allowance center

        #Create Pattern Piece A Jacket Back
        pnt1 = dPnt(midPoint(a1, a8))
        A.setLetter((pnt1.x, pnt1.y), scaleby=10.0)
        A.setLabelPosition(down(pnt1, 2*CM))
        Ag1 = dPnt(midPoint(a14, a24))
        Ag2 = dPnt(midPoint(a16, a26))
        A.addGrainLine(Ag1, Ag2)
        A.addGridLine(['M', a0,'L',a7,'L',a13,'L',a6,'L',a0, 'M',a1,'L',a8,'M',a2,'L',a9,'M',a3,'L',a10,'M',a4,'L',a11,'M',a5,'L',a12,'M',a6,'L',a13])
        pth = (['M',a0,'C',a20,'C',a21,'C',a22,'C',a23,'L',a24,'C',a25,'C',a26,'L',a27,'L',a28])
        pth += (['L',a18,'L',a17,'L',a16,'C',a15,'C',a14,'C',a0])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)
        
        #Create Pattern Piece B Jacket Front
        pnt1 = dPnt(midPoint(b2, b8))
        B.setLetter((pnt1.x, pnt1.y), scaleby=10.0)
        B.setLabelPosition(down(pnt1, 2*CM))
        Bg1 = dPnt(midPoint(b3, b9))
        Bg2 = dPnt(midPoint(b4, b10))
        B.addGrainLine(Bg1, Bg2)
        B.addGridLine(['M', b0,'L',b7,'L',b11,'L',b5,'L',a0, 'M',b2,'L',b8,'M',b3,'L',b9,'M',b4,'L',b10,'M',b5,'L',b11])
        pth = (['M',b0,'L',b7])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)

        # call draw once for the entire pattern
        self.draw()
        return
