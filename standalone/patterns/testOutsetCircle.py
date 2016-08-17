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
        
        a1 = A.addPoint('a1', (0.0, 0.0)) #center point
        a2 = A.addPoint('a2', up(a1, radius)) #top
        a3 = A.addPoint('a3', right(a1, radius)) #right
        a4 = A.addPoint('a4', down(a1, radius)) #bottom
        a5 = A.addPoint('a5', left(a1, radius)) #right
        
        length = circumference/12
        a2.addOutpoint(right(a2, length))
        a3.addInpoint(up(a3, length))
        a3.addOutpoint(down(a3, length))
        a4.addInpoint(right(a4, length))
        a4.addOutpoint(left(a4, length))
        a5.addInpoint(down(a5, length))
        a5.addOutpoint(up(a5, length))
        a2.addInpoint(left(a2, length))
        
        curve1 = points2List(a2, a2.outpoint, a3.inpoint, a3)
        curve2 = points2List(a3, a3.outpoint, a4.inpoint, a4)
        curve3 = points2List(a4, a4.outpoint, a5.inpoint, a5)
        curve4 = points2List(a5, a5.outpoint, a2.inpoint, a2)
        
        #create outset curves
        outC1 = outsetCurve(curve1, 1*IN, -ANGLE90) #returns outset_curve[p1, c1, c2, p2, c3, c4, p3]
        outC2 = outsetCurve(curve2, 1*IN, -ANGLE90) #returns outset_curve[p3, c5, c6, p4, c7, c8, p5]
        outC3 = outsetCurve(curve3, 1*IN, -ANGLE90) #returns outset_curve[p5, c9, c10, p6, c11, c12, p7]
        outC4 = outsetCurve(curve4, 1*IN, -ANGLE90) #returns outset_curve[p7, c13, c14, p8, c15, c16, p9]
        
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
        o1.addInpoint(outC4[5]) #c16
        o1.addOutpoint(outC1[1]) #c1
        
        o2 = A.addPoint('o2', outC1[3]) #p2
        o2.addInpoint(outC1[2]) #c2
        o2.addOutpoint(outC1[4]) #c3
       
        o3 = A.addPoint('o3', outC1[6]) #p3
        o3.addInpoint(outC1[5]) #c4
        o3.addOutpoint(outC2[1]) #c5

        o4 = A.addPoint('o4', outC2[3]) #p4
        o4.addInpoint(outC2[2]) #c6
        o4.addOutpoint(outC2[4]) #c7
           
        o5 = A.addPoint('o5', outC2[6]) #p5
        o5.addInpoint(outC2[5]) #c8
        o5.addOutpoint(outC3[1]) #c9
        
        o6 = A.addPoint('o6', outC3[3]) #p6
        o6.addInpoint(outC3[2]) #c10
        o6.addOutpoint(outC3[4]) #c11
           
        o7 = A.addPoint('o7', outC3[6]) #p7
        o7.addInpoint(outC3[5]) #c12
        o7.addOutpoint(outC4[1]) #c13 
        
        o8 = A.addPoint('o8', outC4[3]) #p8
        o8.addInpoint(outC4[2]) #c14
        o8.addOutpoint(outC4[4]) #c15
        
        o9 = A.addPoint('o9', outC4[6]) #p9
        o9.addInpoint(outC4[5]) #c14
        
        #---------------------------------------------#
        #---all points defined, draw pattern pieces---#
        #---------------------------------------------#

        #draw Front A
        x1 = a3.x/2
        y1 = a4.y/2
        x2 = a3.x/3
        y2 = a4.y/3
        x3 = a3.x/5
        y3 = a4.y/5
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
        pth1 = (['M', a2, 'C', a3, 'C', a4, 'C', a5, 'C', a2])
        pth2 = (['M', o1, 'C', o2, 'C', o3, 'C', o4, 'C', o5, 'C', o6, 'C', o7, 'C', o8, 'C', o9])
        A.addSeamLine(pth1)
        A.addCuttingLine(pth2)

        # call draw once for the entire pattern
        self.draw()
        return

#vi:set ts=4 sw=4 expandta2:
