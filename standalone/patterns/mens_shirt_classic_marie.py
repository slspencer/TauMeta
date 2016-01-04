#!/usr/bin/env python
# patternName: mens_shirt_classic
# patternNumber: M-S-S-1

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
        self.setInfo('patternNumber', 'M-S-S-1')
        self.setInfo('patternTitle', 'Mens Shirt Classic')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'Winifred Aldrich')
        self.setInfo('patternmakerName', 'S.L.Spencer')
        self.setInfo('description', """This is a test pattern for Seamly Patterns""")
        self.setInfo('category', 'Shirt/TShirt/Blouse')
        self.setInfo('type', 'streetwear')
        self.setInfo('gender', 'M') # 'M',  'F',  or ''
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
        #create pattern called 'shirt'
        shirt = self.addPattern('shirt')
        #
        #create pattern pieces
        A = shirt.addPiece('yoke', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = shirt.addPiece('back', 'B', fabric = 2, interfacing = 0, lining = 0)
        C = shirt.addPiece('front', 'C', fabric = 2, interfacing = 0, lining = 0)
        D = shirt.addPiece('sleeve', 'D', fabric = 2, interfacing = 0, lining = 0)
        E = shirt.addPiece('cuff', 'E', fabric = 2, interfacing = 1, lining = 0)
        F = shirt.addPiece('collarstand', 'F', fabric = 2, interfacing = 1, lining = 0)
        G = shirt.addPiece('collar', 'G', fabric = 2, interfacing = 1, lining = 0)

        #pattern global values
        #SHIRT_LENGTH = 80*CM
        #CUFF_WIDTH = 25.5*CM    
        #CUFF_HEIGHT = 7.5*CM
        CUFF_WIDTH = 1.5 * CD.wrist
        CUFF_HEIGHT = CD.oversleeve_length/6.0        
        
        #pattern points
        # x, y coordinates are always passed as a two-item list like this: (23.6, 67.0)
        
        #______________
        #Shirt Yoke - A
        a1 = A.addPoint('a1', (0.0, 0.0)) # nape
        a2 = A.addPoint('a2', down(a1, CD.front_waist_length/10.0)) # yoke bottom center            
        a3 = A.addPoint('a3', right(a2, 1.05 * CD.across_back/2.0)) #yoke side = 5% ease across back
        a4 = A.addPoint('a4', (a3.x, a1.y)) # yoke -- ref pt
        a5 = A.addPoint('a5', (a1.x + (1.07 * CD.across_back/2.0), (a2.y - a1.y)/2.0)) #yoke shoulder point       
        a6 = A.addPoint('a6', right(a1, .95 * CD.neck/5.0)) #back neck -- ref pt    
        a7 = A.addPoint('a7', up(a6, distance(a2, a4))) #back neck side      
        a8 = A.addPoint('a8', polar(a6, distance(a2, a4), angleOfDegree(225)))
        
        #a3_old = A.addPoint('a3_old', (a1.x + CD.across_back/2.0 + 4*CM, a2.y)) #yoke side
        #a5_old = A.addPoint('a5_old', (a3.x + 0.75*CM, a4.y - 2*CM)) #yoke shoulder point
        #a6_old = A.addPoint('a6_old', (a1.x + CD.neck/5.0 - 0.5*CM, a1.y)) #back neck -- ref pt
        #a7_old = A.addPoint('a7_old', (a6.x, a6.y - 4.5*CM)) #back neck side
        #a8_old = A.addPoint('a8_old', polar(a6, 2*CM, angleOfDegree(225)))                                 

        #control points for Shirt Yoke A
        #control points b/w a8 & a7
        a8.addOutpoint(polar(a8, distance(a8, a7)/3.0, angleOfDegree(315)))
        a7.addInpoint(polar(a7, distance(a8, a7)/3.0, angleOfLine(a7, a5) + ANGLE90))
        #control points b/w a1 & a8
        a1.addOutpoint(right(a1, distance(a1, a8)/3.0))
        a8.addInpoint(onLineAtY(a8.outpoint, a8, a1.y))
        #control points b/w a5 & a3
        length = distance(a3, a5)/3.0
        a3.addInpoint(up(a3, length ))
        a5.addOutpoint(polar(a5, length, angleOfLine(a7, a5) + ANGLE90))
        
        
        
        # ------------------------------------------------ #
        # ----- all points defined, now define paths ----- #
        # ------------------------------------------------ #

        # shirt Yoke A
        Ag1 = dPnt((a6.x, a6.y))
        Ag2 = dPnt((Ag1.x, a2.y))
        A.addGrainLine(Ag1, Ag2)
        A.setLabelPosition((Ag1.x, Ag1.y))
        A.setLetter((Ag1.x + 7*CM, Ag2.y), scaleby=1.0)
        gpth = (['M', a1, 'L', a2, 'L', a3, 'L', a4, 'L', a1, 'M', a7, 'L', a6, 'L', a8])
        A.addGridLine(gpth)
        pth = (['M', a1, 'C', a8,'C', a7, 'L', a5, 'C', a3, 'L', a2, 'L', a1])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)
        
        
        #______________        
        # call draw once for the entire pattern
        self.draw()
        return
# vi:test ts=4 sw=4 expandtab:
        
        
        

