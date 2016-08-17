#!/usr/bin/env python
# patternName: Test Outset Circle
# patternNumber: Test_Outset_1

from tmtpl.designbase import *
from tmtpl.document import *
from tmtpl.pattern import *
from tmtpl.patternmath import *
from tmtpl.constants import *
from tmtpl.utils import *
from math import pi

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
        self.setInfo('patternTitle', 'Test Outset Circle')
        self.setInfo('companyName', '')
        self.setInfo('designerName', '')
        self.setInfo('patternmakerName', '')
        self.setInfo('description', """Test Outset Circle""")
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
        #create pattern called 'circle'
        circle = self.addPattern('circle')
        #
        ## measurements required by this pattern

        #
        #create pattern pieces
        A = circle.addPiece('Circle', 'A', fabric = 1, interfacing = 0, lining = 0)

        #---circle A---#
        radius = 2*IN
        circumference = 2*pi*radius
        
        c1 = A.addPoint('c1', (0.0, 0.0)) #center top
        a2 = A.addPoint('a2', up(c1, radius)) #top 
        a3 = A.addPoint('a3', right(c1, radius)) #right top        
        c2 = A.addPoint('c2', down(c1, radius)) #center bottom
        a4 = A.addPoint('a4', right(c2, radius)) #right bottom
        a5 = A.addPoint('a5', down(c2, radius)) #bottom
        a6 = A.addPoint('a6', left(c2, radius)) #left bottom
        a7 = A.addPoint('a7', left(c1, radius)) #left top

        l1 = A.addPoint('l1', right(a3, 0.25*IN))
        l2 = A.addPoint('l2', right(a4, 0.25*IN))
        l3 = A.addPoint('l3', left(a6, 0.25*IN))
        l4 = A.addPoint('l4', left(a7, 0.25*IN))
        
        length = circumference/12
        a2.addOutpoint(right(a2, length))
        a3.addInpoint(up(a3, length))
        a4.addOutpoint(down(a4, length))
        a5.addInpoint(right(a5, length))
        a5.addOutpoint(left(a5, length))
        a6.addInpoint(down(a6, length))
        a7.addOutpoint(up(a7, length))
        a2.addInpoint(left(a2, length))
        
        curve1 = points2List(a2, a2.outpoint, a3.inpoint, a3)
        curve2 = points2List(a4, a4.outpoint, a5.inpoint, a5)
        curve3 = points2List(a5, a5.outpoint, a6.inpoint, a6)
        curve4 = points2List(a7, a7.outpoint, a2.inpoint, a2)
        
        #create outset curves
        outC1 = outsetCurves(curve1, 1*IN, -ANGLE90) #returns outset_curve[p1, c1, c2, p2, c3, c4, p3]
        outC2 = outsetCurves(curve2, 1*IN, -ANGLE90) #returns outset_curve[p4, c5, c6, p5, c7, c8, p6]
        outC3 = outsetCurves(curve3, 1*IN, -ANGLE90) #returns outset_curve[p6, c9, c10, p7, c11, c12, p8]
        outC4 = outsetCurves(curve4, 1*IN, -ANGLE90) #returns outset_curve[p9, c13, c14, p10, c15, c16, p11]
        
        for item in outC1:
           print 'outC1', item.x, item.y
        
        #o1 = dPnt(intersectLines(outC1[2], outC1[3], outC2[0],outC2[1]))
        #print 'o1', o1.x, o1.y
        #o2 = dPnt(intersectLines(outL2[2], outL2[3], outL3[0],outL3[1]))
        #print 'o2', o2.x, o2.y
        #o3 = dPnt(intersectLines(outL3[2], outL3[3], outL4[0],outL4[1]))
        #print 'o3', o3.x, o3.y
        #o4 = dPnt(intersectLines(outL4[2], outL4[3], outL1[0],outL1[1]))
        #print 'o4', o4.x, o4.y 
        
        o1 = A.addPoint('o1', outC1[0]) #p1
        o1.addOutpoint(outC1[1]) #c1      
        o2 = A.addPoint('o2', outC1[3]) #p2
        o2.addInpoint(outC1[2]) #c2
        o2.addOutpoint(outC1[4]) #c3     
        o3 = A.addPoint('o3', outC1[6]) #p3
        o3.addInpoint(outC1[5]) #c4       

        o4 = A.addPoint('o4', outC2[0]) #p4
        o4.addOutpoint(outC2[1]) #c5         
        o5 = A.addPoint('o5', outC2[3]) #p5
        o5.addInpoint(outC2[2]) #c6
        o5.addOutpoint(outC2[4]) #c7     
        o6 = A.addPoint('o6', outC2[6]) #p6
        o6.addInpoint(outC2[5]) #c8
        
        o6.addOutpoint(outC3[1]) #c9                  
        o7 = A.addPoint('o7', outC3[3]) #p7
        o7.addInpoint(outC3[2]) #c10
        o7.addOutpoint(outC3[4]) #c11   
        o8 = A.addPoint('o8', outC3[6]) #p8
        o8.addInpoint(outC3[5]) #c12
        
        o9 = A.addPoint('o9', outC4[0]) #p9
        o9.addOutpoint(outC4[1]) #c13
        o10 = A.addPoint('o10', outC4[3])
        o10.addInpoint(outC4[2]) #c14
        o10.addOutpoint(outC4[4]) #c15
        o11 = A.addPoint('o11', outC4[6])
        o11.addInpoint(outC4[5])
        
        #create outset lines
        oline1 = outsetLine(a3, a4, 1*IN, -ANGLE90)
        oline2 = outsetLine(a6, a7, 1*IN, -ANGLE90)

        
        #---------------------------------------------#
        #---all points defined, draw pattern pieces---#
        #---------------------------------------------#

        #draw Front A
        x1 = a3.x/2
        y1 = a5.y/2
        x2 = a3.x/3
        y2 = a5.y/3
        x3 = a3.x/5
        y3 = a5.y/5
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
        pth1 = (['M', a2, 'C', a3, 'L', l1, 'L', l2, 'L', a4, 'C', a5, 'C', a6, 'L', l3, 'L', l4, 'L', a7, 'C', a2])
        pth2 = (['M', o1, 'C', o2, 'C', o3, 'L', o4, 'C', o5, 'C', o6, 'C', o7, 'C', o8, 'L', o9, 'C', o10, 'C', o11])
        A.addSeamLine(pth1)
        A.addCuttingLine(pth2)

        # call draw once for the entire pattern
        self.draw()
        return

#vi:set ts=4 sw=4 expandta2:
