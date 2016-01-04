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
        #D = shirt.addPiece('sleeve', 'D', fabric = 2, interfacing = 0, lining = 0)
        #E = shirt.addPiece('cuff', 'E', fabric = 2, interfacing = 1, lining = 0)
        #F = shirt.addPiece('collarstand', 'F', fabric = 2, interfacing = 1, lining = 0)
        #G = shirt.addPiece('collar', 'G', fabric = 2, interfacing = 1, lining = 0)

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
        A1 = A.addPoint('A1', (0.0, 0.0)) #start
        A2 = A.addPoint('A2', right(A1, .9 * CD.neck/5.0)) # neck side
        A3 = A.addPoint('A3', right(A1, CD.across_back/2.0)) # across_back side -- ref pt
        A4 = A.addPoint('A4', right(A1, 1.06 * CD.across_back/2.0)) # across_back side + ease -- ref pt        
        A5 = A.addPoint('A5', right(A1, CD.back_shoulder_width/2.0)) #shouldertip -- ref pt
        A6 = A.addPoint('A6', right(A1, 1.06 * CD.back_shoulder_width/2.0)) #shouldertip + ease -- ref pt
        
        a1 = A.addPoint('a1', down(A1, CD.back_shoulder_height - CD.back_waist_length)) # neck center, "nape"
        a2 = A.addPoint('a2', down(a1, CD.back_waist_length/6.0)) #across_back center  
        a3 = A.addPoint('a3', right(a2, distance(A1, A4))) #across_back side -- ref pt
        a4 = A.addPoint('a4', right(a3, distance(A4, A6)/2.0)) #across_back side
            
        a5 = A.addPoint('a5', lowestP(onCircleAtX(A2, CD.shoulder, A5.x))) #shouldertip -- ref pt
        a6 = A.addPoint('a6', (A6.x, a5.y)) #shouldertip -- ref pt
        a7a = A.addPoint('a7a', up(a6, distance(a5, a6))) #shouldertip
        a7 = A.addPoint('a7', onLineAtLength(A2,  a7a,  distance(A2,  a6)))
        a8 = A.addPoint('a8', (A2.x, a1.y)) #neck side -- ref pt                                

        #control points for Shirt Yoke A
        #b/w a1 & A2
        angle = angleOfLine(A2, a7) + ANGLE90
        a1.addOutpoint(right(a1, distance(a1, A2)/5.0))
        A2.addInpoint(polar(A2, distance(A2, a8)/2.0, angle))
        #b/w a7 & a4
        #a6.addOutpoint(polar(a6, length2, angle))
        length = distance(a4, a7)/4.0 
        a7.addOutpoint(polar(a7, length, angle))       
        a4.addInpoint(up(a4, length))
        
        #______________        
        #Shirt Back - B                
        b1 = B.addPoint('b1', a2) #back top center, matches with yoke bottom center (a2)      
        b2 = B.addPoint('b2', down(b1, 1.05 * CD.back_waist_length - distance(a1, a2))) #back waist center
        b3 = B.addPoint('b3', up(b2, 0.8 * CD.side)) #back underarm center 
        b4 = B.addPoint('b4', down(b2, 1.10 * CD.back_hip_height)) #back hem center 
        
        b10 = B.addPoint('b10', right(b1, distance(a2, a4))) #back top side -- ref pt                                 
        b5 = B.addPoint('b5', right(b2, 1.06 * max(CD.waist, CD.bust)/4.0)) #back waist side
        b6 = B.addPoint('b6', right(b3, 1.08 * CD.bust/4.0)) #back underarm side
        b7 = B.addPoint('b7', right(b4, 1.08 * max(CD.hip, CD.waist, CD.bust)/4.0)) #back hem side -- ref pt #1
        b8 = B.addPoint('b8', up(b7, distance(b2, b4)/3.0)) #back hem side -- ref pt #2        
        b9 = B.addPoint('b9', midPoint(b4, b7)) #back hem side         

        b11 = B.addPoint('b11', left(b1, 0.12 * distance(b1, b10))) #tuck top center        
        b13 = B.addPoint('b13', midPoint(b11, b10)) # midpoint b/w tuck top center & back top side -- ref pt 
        b15 = B.addPoint('b15', lowestP(intersectChordCircle(b13, b10, distance(a6,a7))))       
        b12 = B.addPoint('b12', left(b4, distance(b1, b11))) #tuck hem center
                              
        #control points B
        #b/w b13 & b15
        length = distance(b13, b15)/3.0
        b13.addOutpoint(right(b13, length)) 
        angle = angleOfLine(b15, b13.outpoint)     
        b15.addInpoint(polar(b15, length, angle))
        #b/w b15 & b6 armscye
        b15.addOutpoint(polar(b15, distance(b15, b6)/3.0, angle - ANGLE90))
        b6.addInpoint(left(b6, 0.75 * abs(b6.x - b15.x)))
        #b/w b6, b5, b8 side
        length = distance(b5, b6)/3.0
        b5.addInpoint(up(b5, length))
        b6.addOutpoint(polar(b6, length, angleOfLine(b6, b5.inpoint)))
        length = distance(b5, b8)/3.0
        b5.addOutpoint(down(b5, length))
        b8.addInpoint(polar(b8, length, angleOfLine(b8, b5.outpoint)))
        #b/w b8 & b9 hem
        length = distance(b8, b9)/3.0
        b8.addOutpoint(polar(b8, length/2.0, angleOfLine(b8.inpoint, b8) + ANGLE90))
        b9.addInpoint(right(b9, length))
        

        #______________
        #Shirt Front - C     
        C1 = C.addPoint('C1', a1) #start
        C2 = C.addPoint('C2', left(C1, .9 * CD.neck/5.0)) # neck side
        C3 = C.addPoint('C3', left(C1, CD.across_chest/2.0)) # across_chest side -- ref pt
        C4 = C.addPoint('C4', left(C1, 1.06 * CD.across_chest/2.0)) # across_chest side + ease -- ref pt        
        C5 = C.addPoint('C5', left(C1, CD.front_shoulder_width/2.0)) #shouldertip -- ref pt
        C6 = C.addPoint('C6', left(C1, 1.06 * CD.front_shoulder_width/2.0)) #shouldertip + ease -- ref pt 
        #front center line
        c1 = C.addPoint('c1', down(C1, CD.front_shoulder_height - CD.front_waist_length)) #front neck center 
        c2 = C.addPoint('c2', down(c1, 1.05 * CD.front_waist_length)) #front waist center
        c3 = C.addPoint('c3', up(c2, distance(b2, b3))) #front underarm center
        c4 = C.addPoint('c4', down(c2, distance(b2, b4))) #front hem center
        #shoulder
        c5 = C.addPoint('c5', lowestP(onCircleAtX(C2, CD.shoulder, C5.x))) #shouldertip -- ref pt
        c6 = C.addPoint('c6', (C6.x, c5.y)) #shouldertip -- ref pt
        c7a = C.addPoint('c7a', up(c6, distance(c5, c6))) #shouldertip  
        c7 = C.addPoint('c7', onLineAtLength(C2, c7a, 0.97 * distance(A2,  a7)))
        #side
        c8 = C.addPoint('c8', left(c2, distance(b2, b5))) #front waist side
        c9 = C.addPoint('c9', left(c3, distance(b3, b6))) #front underarm side
        c10 = C.addPoint('c10', left(c4, distance(b4, b7))) #front hem side -- ref pt #1
        c11 = C.addPoint('c11', up(c10, distance(b7, b8))) #front hem side -- ref pt #2        
        c12 = C.addPoint('c12', midPoint(c4, c10)) #front hem side 
        #armscye
        c13 = C.addPoint('c13', down(c1, distance(c1, c3)/2.0)) #across_chest center , 1/2 b/w neck front & underarm side
        c14 = C.addPoint('c14', left(c13, distance(C1, C3))) #across_chest side -- armscye curve -- ref pt
        c15 = C.addPoint('c15', left(c14, distance(C3, C4)/2.0)) #across_chest side -- armscye curve                       
        #placket
        c16 = C.addPoint('c16', right(c1, 0.04 * CD.bust/4.0)) #neck placket centerline
        c17 = C.addPoint('c17', (c16.x, c4.y)) #hem placket centerline          
        c18 = C.addPoint('c18', right(c16, 2 * distance(c1, c16))) #neck placket foldline
        c19 = C.addPoint('c19', (c18.x, c4.y)) #hem placket foldline 
        c20 = C.addPoint('c20', right(c18,  distance(c1,  c18))) #front neck placket foldback
        c21 = C.addPoint('c21', (c20.x, c4.y)) #hem placket foldback
        
        #control points Shirt Back C
        #b/w b12 & b11 - hem
        length = distance(c11,  c12)/3.0
        c12.addOutpoint(left(c12,  length))
        c11.addInpoint(polar(c11, length/2.0,  angleOfLine(c11,  c8) + ANGLE90))
        #b/w c11 & c8 - side
        length = distance(c11,  c8)/3.0
        c8.addInpoint(down(c8, length))
        c11.addOutpoint(polar(c11,  length,  angleOfLine(c11,  c8.inpoint)))
        #b/w c8 & c9 - side
        length = distance(c8,  c9)/3.0
        c8.addOutpoint(up(c8,  length))
        c9.addInpoint(polar(c9,  length,  angleOfLine(c9, c8.outpoint)))
        #b/w c9 & c15 - armscye
        c9.addOutpoint(right(c9, 0.75 * abs(c15.x - c9.x)))
        c15.addInpoint(down(c15,  abs(c9.y - c15.y)/2.0))
        #b/w c15 & c7 - armscye
        length = distance(c15, c7)/3.0
        angle = angleOfLine(c7, C2) + ANGLE90
        c15.addOutpoint(up(c15, length))
        c7.addInpoint(polar(c7,  length/2.0,  angle))
        #b/w C2 & c1
        C2.addOutpoint(polar(C2, abs(C2.y - c1.y)/2.0, angle))
        c1.addInpoint(onLineAtY(C2, C2.outpoint, c1.y))

        # ------------------------------------------------ #
        # ----- all points defined, now define paths ----- #
        # ------------------------------------------------ #

        # Shirt Yoke A
        Ag1 = dPnt((right(A6, 3*CM)))
        Ag2 = dPnt((down(Ag1, 3*CM)))
        A.addGrainLine(Ag1, Ag2)
        pnt = right(Ag1, 2*CM)
        A.setLetter((pnt), scaleby=1.0)        
        A.setLabelPosition((down(pnt, 0.75*CM)))

        gpth = (['M', A1, 'L', A6, 'L', a7, 'L', a4, 'L', a2, 'L', A1, 'M', a1, 'L', a8, 'L', A2, 'M', a3, 'L', a5,  'L',  a6, 'M',  A2,  'L', a5])
        A.addGridLine(gpth)
        pth = (['M', a1, 'C', A2, 'L', a7, 'C', a4, 'L', a2, 'L', a1])         
        A.addSeamLine(pth)
        A.addCuttingLine(pth)
  
        # Shirt Back B
        Bg1 = dPnt((right(b6, 3*CM)))
        Bg2 = dPnt((down(Bg1, 3*CM)))
        B.addGrainLine(Bg1, Bg2)
        pnt = right(Bg1, 2*CM)
        B.setLetter((pnt), scaleby=1.0)        
        B.setLabelPosition((down(pnt, 0.75*CM)))
        B.addGridLine(['M', b1, 'L', b10, 'M', b3, 'L', b6, 'M', b2, 'L', b5, 'M', b8, 'L', b7, 'L', b4, 'M', b1])
        B.addFoldLine(['M', b1, 'L', b4])
        pth = (['M', b11, 'L', b1, 'L', b13, 'C', b15, 'C', b6, 'C', b5, 'C', b8, 'C', b9, 'L', b12, 'L',  b11])
        B.addSeamLine(pth)
        B.addCuttingLine(pth) 
        
        # shirt Front C
        Cg1 = dPnt((right(c20, 3*CM)))
        Cg2 = dPnt((down(Cg1, 3*CM)))
        C.addGrainLine(Cg1, Cg2)
        pnt = right(Cg1, 2*CM)
        C.setLetter((pnt), scaleby=1.0)        
        C.setLabelPosition((down(pnt, 0.75*CM)))
        C.addGridLine(['M', c7,  'L', C6, 'L', C1, 'L', c4, 'M', c2, 'L', c8, \
        'M', c3, 'L',  c9, 'M',  C2, 'L',  c5, 'L',  c6,  'M',  c13,  'L', c15])
        C.addFoldLine(['M', c18, 'L', c19])
        C.addMarkingLine(['M', c16, 'L', c17])
        pth = (['M', c1, 'L', c20, 'L', c21, 'L', c19, 'L', c21])
        pth += (['L', c12, 'C', c11, 'C', c8, 'C', c9])
        pth += (['C', c15,  'C', c7, 'L',  C2,  'C', c1])
        C.addSeamLine(pth)
        C.addCuttingLine(pth)           
        
        #______________        
        # call draw once for the entire pattern
        self.draw()
        return
# vi:test ts=4 sw=4 expandtab:
        
        
        

