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
        self.setInfo('patternTitle', 'Adult Bibb')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', '')
        self.setInfo('patternmakerName', '')
        self.setInfo('description', """Women's bibb block pattern with minimum ease, includes long sleeve with elbow dart.""")
        self.setInfo('category', 'Accessories')
        self.setInfo('type', 'Design')
        #
        # The next group are all optional
        #
        self.setInfo('gender', 'F') # 'M',  'F',  or ''
        self.setInfo('yearstart', '1900')
        self.setInfo('yearend', '')
        self.setInfo('culture', 'European')
        self.setInfo('wearer', '')
        self.setInfo('source', '')
        self.setInfo('characterName', '')
        self.setInfo('recommendedFabric', '')
        self.setInfo('recommendedNotions', '')

        #get client data
        CD = self.CD #client data is prefaced with CD

        #create a pattern named 'bibb'
        bibb = self.addPattern('bibb')

        #create pattern pieces,  assign an id lettercd 
        A = bibb.addPiece('Bibb Front & Back', 'A', fabric = 2, interfacing = 0, lining = 1)

        #pattern points
        # x, y coordinates are always passed as a two-item list like this: (23.6, 67.0)
        # points are always in the 'reference' group, and always have style='point_style'
   
        SA = SEAM_ALLOWANCE     
        a = A.addPoint('a', (0,0))
        b = A.addPoint('b', up(a, 8.5*IN))
        c = A.addPoint('c', down(b, 39*IN))
        d = A.addPoint('d', right(b, 9*IN))
        e = A.addPoint('e', right(c, 9*IN))
        f = A.addPoint('f', up(a, distance(a,b) / 4.0))
        g = A.addPoint('g', right(f, 3.5*IN))
        h = A.addPoint('h', (d.x, a.y))
        i = A.addPoint('i', down(b, 0.5*IN))
        j = A.addPoint('j', right(i, 0.5*IN))
        k = A.addPoint('k', up(e, distance(e, h) / 3.0))       
  
        l = A.addPoint('l', mirror(a, k))
        m = A.addPoint('m', mirror(a, h))
        n = A.addPoint('n', mirror(a, j))
        o = A.addPoint('o', mirror(a, g)) 
        
        for pnt in a, g, j, h, k, c, l, m, n, o:
            pnt.outset = SEAM_ALLOWANCE / 2.0      
        
        #controlpoints
        a.addOutpoint(right(a, 0.75 * distance(a, g)))
        g.addInpoint(down(g, abs(g.y - a.y) / 3.0))
        g.addOutpoint(up(g, 0.8 * abs(g.y - j.y) ))
        j.addInpoint(polar(j, distance(g, j) / 3.0, angleOfDegree(110)))
        j.addOutpoint(polar(j, distance(g, j) / 3.0, angleOfLine(j.inpoint, j)))
        h.addInpoint(up(h, 0.75 * distance(j, h)))
        k.addOutpoint(down(k, 0.75 * distance(k, e)))
        
        c.addInpoint(e)
        c.addOutpoint(mirror(a, c.inpoint))
        
        l.addInpoint(mirror(a, k.outpoint))
       
        m.addOutpoint(mirror(a, h.inpoint))
        
        n.addInpoint(mirror(a, j.outpoint))
        n.addOutpoint(mirror(a, j.inpoint))
        
        o.addInpoint(mirror(a, g.outpoint))
        o.addOutpoint(mirror(a, g.inpoint))
        
        a.addInpoint(mirror(a, a.outpoint))
  

        #Bibb Front & Back A
        pnt1 = dPnt((g.x, (a.y + c.y) / 2.0))
        A.setLabelPosition(pnt1)
        pnt2 = up(pnt1, 0.5*IN)
        A.setLetter(pnt2, scaleby = 10.0)
        AG1 = dPnt(midPoint(a, c))
        AG2 = down(AG1, distance(AG1, c) / 2.0)
        A.addGrainLine(AG1, AG2)
        A.addGridLine(['M', a, 'L', g, 'L', j, 'L', h, 'L', e, 'L', c, 'L', l, 'L', m, 'L', n, 'L', o, 'L', a ])        
        pth = (['M', a, 'C', g, 'C', j, 'C', h, 'L', k, 'C', c, 'C', l, 'L', m, 'C', n, 'C', o, 'C', a])
        A.addSeamLine(pth)     
        A.addCuttingLine(pth)
                             
        #call draw() to generate svg file
        self.draw()

        return

