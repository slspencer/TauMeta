#!/usr/bin/env python
# patternName: Test Outset Square
# patternNumber: Test_Outset_1

from tmtpl.designbase import *
from tmtpl.document import *
from tmtpl.pattern import *
from tmtpl.patternmath import *
from tmtpl.constants import *
from tmtpl.utils import *

class Design(designBase):

    def pattern(self):
        """
        Method defining a pattern design. This is where the designer places
        all elements of the design definition
        """

        # The designer must supply certain information to allow
        #   tracking and searching of patterns
        #
        # This group is all mandatory
        #
        self.setInfo('patternNumber', 'Test_Outset_1')
        self.setInfo('patternTitle', 'Test Outset Square')
        self.setInfo('companyName', '')
        self.setInfo('designerName', '')
        self.setInfo('patternmakerName', '')
        self.setInfo('description', """Test Outset Square""")
        self.setInfo('category', 'test')
        self.setInfo('type', 'pattern')
        self.setInfo('gender', '') # 'M',  'F',  or ''
        #
        # The next group are all optional
        #
        self.setInfo('recommendedFabric', '')
        self.setInfo('recommendedNotions', '')
        #
        #self.setInfo('yearstart',1940 )
        #self.setInfo('yearend', 2013)
        #self.setInfo('culture', 'European')
        #self.setInfo('wearer', '')
        #self.setInfo('source', '')
        #self.setInfo('characterName', '')
        #
        #get client data
        CD = self.CD #client data is prefaced with CD
        #
        #create pattern called 'square'
        square = self.addPattern('square')
        #
        ## measurements required by this pattern

        #
        #create pattern pieces
        A = square.addPiece('Square', 'A', fabric = 1, interfacing = 0, lining = 0)

        #---Square A---#
        sq1 = A.addPoint('sq1', (0.0, 0.0)) #upper left
        sq2 = A.addPoint('sq2', right(sq1, 5*IN)) #upper right
        sq3 = A.addPoint('sq3', down(sq2, 5*IN)) #lower right
        sq4 = A.addPoint('sq4', left(sq3, 5*IN)) #lower left
      
        #create outset
        outL1 = outsetLine(sq1, sq2, 1*IN, -ANGLE90) #returns outset_line[p1, p2]
        outL2 = outsetLine(sq2, sq3, 1*IN, -ANGLE90) #returns outset_line[p2, p3]        
        outL3 = outsetLine(sq3, sq4, 1*IN, -ANGLE90) #returns outset_line[p3, p4]
        outL4 = outsetLine(sq4, sq1, 1*IN, -ANGLE90) #returns outset_line[p4, p1]
        o1 = dPnt(intersectLines(outL1[0], outL1[1], outL2[0],outL2[1]))
        print 'o1', o1.x, o1.y
        o2 = dPnt(intersectLines(outL2[0], outL2[1], outL3[0],outL3[1]))
        print 'o2', o2.x, o2.y
        o3 = dPnt(intersectLines(outL3[0], outL3[1], outL4[0],outL4[1]))
        print 'o3', o3.x, o3.y
        o4 = dPnt(intersectLines(outL4[0], outL4[1], outL1[0],outL1[1]))
        print 'o4', o4.x, o4.y           
       

        #---------------------------------------------#
        #---all points defined, draw pattern pieces---#
        #---------------------------------------------#

        #draw Front A
        x1 = sq2.x/2
        y1 = sq4.y/2
        x2 = sq2.x/3
        y2 = sq4.y/3
        x3 = sq2.x/5
        y3 = sq4.y/5
        x4 = x3
        y4 = 4 * y3 
        p1 = dPnt((x1, y1))
        p2 = dPnt((x2, y2))
        p3 = dPnt((x3, y3))
        p4 = dPnt((x4, y4))     
        A.setLabelPosition(p1)
        A.setLetter(p2, scaleby=10.0)
        aG1 = p3
        aG2 = p4
        A.addGrainLine(aG1, aG2)
        pth1 = (['M', sq1, 'L', sq2, 'L', sq3, 'L', sq4, 'L', sq1])
        pth2 = (['M', o1, 'L', o2, 'L', o3, 'L', o4, 'L', o1])
        A.addSeamLine(pth1)
        A.addCuttingLine(pth2)

        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

