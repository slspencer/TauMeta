# !/usr/bin/python
#
# adult_bib.py
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
        self.setInfo('patternNumber', '')
        self.setInfo('patternTitle', 'A Square')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', '')
        self.setInfo('patternmakerName', '')
        self.setInfo('description', """Test for creating seam allowances""")
        self.setInfo('category', 'Test')
        self.setInfo('type', 'Test')
        #
        # The next group are all optional
        #
        self.setInfo('gender', '') # 'M',  'F',  or ''
        self.setInfo('yearstart', '')
        self.setInfo('yearend', '')
        self.setInfo('culture', '')
        self.setInfo('wearer', '')
        self.setInfo('source', '')
        self.setInfo('characterName', '')
        self.setInfo('recommendedFabric', '')
        self.setInfo('recommendedNotions', '')

        #get client data
        CD = self.CD #client data is prefaced with CD

        #create a pattern named 'square'
        square = self.addPattern('square')

        #create pattern pieces,  assign an id lettercd 
        A = square.addPiece('Square', 'A', fabric = 0, interfacing = 0, lining = 0)

        #pattern points
        # x, y coordinates are always passed as a two-item list like this: (23.6, 67.0)
        # points are always in the 'reference' group, and always have style='point_style'
   
        SA = SEAM_ALLOWANCE     
        a = A.addPoint('a', (0,0))
        b = A.addPoint('b', down(a, 5*IN))
        c = A.addPoint('c', right(b, 5*IN))
        d = A.addPoint('d', up(c, 5*IN))
                
        for pnt in a, b, c, d:
            pnt.outset = SEAM_ALLOWANCE / 2.0   
        

        #Square A
        pnt1 = dPnt(((a.x + d.x)/2.0, (a.y + b.y) / 2.0))
        A.setLabelPosition(pnt1)
        pnt2 = dPnt((pnt1.x, pnt1.y - 0.5*IN))
        A.setLetter((pnt2.x, pnt2.y), scaleby = 10.0)
        AG1 = dPnt(((a.x + pnt.x)/2.0, pnt2.y))
        AG2 = down(AG1, distance(a, b) / 4.0)
        A.addGrainLine(AG1, AG2)
        pth = (['M', a, 'L', b, 'L', c, 'L', d, 'L', a])
        A.addSeamLine(pth)     
        A.addCuttingLine(pth)
        outset_pth = createOutset(pth)
        A.addOutsetLine(outset_pth)

                             
        #call draw() to generate svg file
        self.draw()

        return

