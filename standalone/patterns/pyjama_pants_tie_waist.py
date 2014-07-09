#!/usr/bin/env python
# patternName: pyjama_pants_tie_waist
# patternNumber: pyjama_pants_tie_waist

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
        self.setInfo('patternNumber', 'pyjama_pants_tie_waist')
        self.setInfo('patternTitle', 'Pyjama Pants with Tie Waist')
        self.setInfo('companyName', 'Seamly Patterns')
        self.setInfo('designerName', 'S. L. Spencer')
        self.setInfo('patternmakerName', 'S. L. Spencer')
        self.setInfo('description', """Pyjama pants with tie waist""")
        self.setInfo('category', 'Loungewear')
        self.setInfo('type', 'Pyjamas')
        self.setInfo('gender', '') # 'M',  'F',  or ''
        #
        # The next group are all optional
        #
        self.setInfo('recommendedFabric', 'Cotton, Flannel')
        self.setInfo('recommendedNotions', 'Grosgrain tape for tie waist, 2.5cm width, length = waist size + 24cm')
        #
        self.setInfo('yearstart', '1910' )
        #self.setInfo('yearend', '')
        self.setInfo('culture', 'Modern')
        #self.setInfo('wearer', '')
        #self.setInfo('source', '')
        #self.setInfo('characterName', '')
        #
        #get client data
        CD = self.CD #client data is prefaced with CD
        #
        #create pattern called 'pants'
        pants = self.addPattern('pants')
        #
        #create pattern pieces
        A = pants.addPiece('Front Pants', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = pants.addPiece('Back Pants', 'B', fabric = 2, interfacing = 0, lining = 0)
        C = pants.addPiece('Front Waist Facing', 'C', fabric = 2, interfacing = 0, lining = 0)
        D = pants.addPiece('Back Waist Facing', 'D', fabric = 2, interfacing = 0, lining = 0)
        E = pants.addPiece('Fly Facing', 'E', fabric = 2, interfacing = 0, lining = 0)
        
        elastic_width = 2.54 * CM
        casing_width = 1.5 * elastic_width
        hem_width = 2.54 * CM
        
        #---Front points---#
        p0 = A.addPoint('p0', (0,0)) #waist side
        p1 = A.addPoint('p1', down(p0, CD.rise)) #crotch side guidepoint
        p2 = A.addPoint('p2', down(p1, CD.inseam)) #hem side guidepoint
        p3 = A.addPoint('p3', up(p2, (6 * CM) + (CD.inseam / 2.0))) #knee side        
        p4 = A.addPoint('p4', left(p1, (3 * CM) + (CD.hip / 4.0))) #front crotch center
        p5 = A.addPoint('p5', (p4.x, p0.y)) #front waist center
        p6 = A.addPoint('p6', (p4.x, p3.y)) #front knee center
        p7 = A.addPoint('p7', (p4.x, p2.y)) #pattern point to calculate front hem center
        p9 = A.addPoint('p9', left(p4, (CD.hip / 12.0) - (0.5 * CM))) #front crotch point
        p11 = A.addPoint('p11', left(p2, 2.5 * CM)) #hem side
        p17 = A.addPoint('p17', down(p11, hem_width)) #hem extension side          
        p10 = A.addPoint('p10', right(p7, 4 * CM)) #front hem center
        p16 = A.addPoint('p16', down(p10, hem_width)) #front hem extension center        
      
        w0 = A.addPoint('w0', down(p0, 0.2 * CD.rise)) #waist side
        w1 = A.addPoint('w1', down(w0, casing_width)) #waist casing side 1 
        w2 = A.addPoint('w2', (p5.x, w0.y)) #waist casing center  1
        w3 = A.addPoint('w3', (w2.x, w1.y)) #front waist casing center 2    
  
        f1 = A.addPoint('f1', (w2.x - (6 * CM), w0.y)) #fly upper left, fly is 6cm wide     
        f3 = A.addPoint('f3', up(p4, 0.25 * distance(p4, p5))) #fly lower left
        f2 = A.addPoint('f2', (f1.x, f3.y)) #fly lower right

        #---front control points---#
        #b/w p10 front hem center & p6 front knee center
        p10.addOutpoint(up(p10, distance(p10, p6) / 3.0))
        p6.addInpoint(polar(p6, distance(p10, p6) / 3.0, angleOfLine(p9, p10)))
        #b/w p6 & p9 front crotch point
        p6.addOutpoint(polar(p6, distance(p6, p9) / 3.0, angleOfLine(p10, p9)))
        p9.addInpoint(polar(p9, distance(p6, p9) / 3.0, angleOfLine(p9, p6.outpoint)))
        #b/w p9 & f3 front lower left fly
        p9.addOutpoint(midPoint(p9, p4)) #midpoint b/w p9 &  p4
        f3.addInpoint(midPoint(p4, f3)) #midpoint b/w p4 & f3
        
        #---Back points---#
        p18 = B.addPoint('p18', right(p5, 2.5 * CM)) #pattern point to calculate back waist center
        p19 = B.addPoint('p19', up(p18, 4 * CM)) #back waist center
        p20 = B.addPoint('p20', left(p6, 4 * CM)) #back knee center
        p21 = B.addPoint('p21', right(p7, 1 * CM)) #back hem center        
        p22 = B.addPoint('p22', up(p4, 0.5 * distance(p4, p5))) #pattern point on back center seam
        p23 = B.addPoint('p23', left(p9, (CD.hip / 12.0) - (0.5 * CM))) #pattern point to calculate back crotch point
        p24 = B.addPoint('p24', onLineAtLength(p20, p23, distance(p6, p9))) #back crotch point      
        p25 = B.addPoint('p25', down(p21, hem_width)) #back hem extension center
        
        w5 = B.addPoint('w5', down(p19, distance(p0, w0))) #back waist center guide 0
        w6 = B.addPoint('w6', down(w5, casing_width)) #back waist center guide 1
        w8 = B.addPoint('w8', intersectLines(p19, p22, w0, w5)) #back waist center 0
        w9 = B.addPoint('w9', intersectLines(p19, p22, w1, w6)) #back waist center 1
        
        #---back control points---#
        #b/w w8 back waist center & w0 waist side
        w8.addOutpoint(polar(w8, distance(w8, w0) / 3.0, angleOfLine(p22, w8) + ANGLE90))
        w0.addInpoint(left(w0, distance(w8, w0) / 3.0))
        #b/w p21 back hem center & p20 back knee center
        p21.addOutpoint(up(p21, distance(p21, p20) / 3.0))
        p20.addInpoint(polar(p20, distance(p21, p20) / 3.0, angleOfLine(p24, p21)))
        #b/w p20 & p24 back crotch point
        p20.addOutpoint(polar(p20, distance(p20, p24) / 3.0, angleOfLine(p21, p24)))
        p24.addInpoint(polar(p24, distance(p20, p24) / 3.0, angleOfLine(p24, p20.outpoint)))
        #b/w p24 & p22 on back center seam
        p24.addOutpoint(right(p24, distance(p24, p4) / 2.0))
        p22.addInpoint(polar(p22, distance(p24, p22) / 3.0, angleOfLine(p19, p22)))
        #b/w w1 waist side & w9 waist center
        w1.addOutpoint(left(w1, distance(w1, w9) / 3.0))
        w9.addInpoint(polar(w9, distance(w1, w9) / 3.0, angleOfLine(w8, w8.outpoint)))
        

        #draw Front A
        pnt1 = dPnt(midPoint(p1, p4))
        pnt2 = dPnt((pnt1.x, f2.y))
        A.setLabelPosition((pnt1.x, pnt1.y))
        A.setLetter((pnt2.x, pnt2.y), scaleby=10.0)
        AG1 = dPnt(down(pnt1, 0.1 * distance(p1, p2)))
        AG2 = dPnt(polar(AG1, 0.75 * distance(p1, p2), angleOfLine(p0, p11))) #grainline is set parallel to side seam
        A.addGrainLine(AG1, AG2)   
        pth = (['M', p10, 'L', p11, 'M', f3, 'L', w2])
        A.addFoldLine(pth)   
        A.addGridLine(['M', p5, 'L', p0, 'L', p2, 'L', p7, 'L', p5, 'M', p9, 'L', p1, 'M', p6, 'L', p3, 'M', w1, 'L', w3])  
        pth = (['M', f1, 'L', w0, 'L', w1, 'L', p11, 'L', p17, 'L', p16, 'L', p10, 'C', p6, 'C', p9, 'C', f3, 'L', f2, 'L', f1])
        A.addSeamLine(pth)
        A.addCuttingLine(pth)
        
        #draw Back B
        pnt1 = dPnt(midPoint(p1, p4))
        pnt2 = dPnt((pnt1.x, f2.y))
        B.setLabelPosition((pnt1.x, pnt1.y))
        B.setLetter((pnt2.x, pnt2.y), scaleby=10.0)
        BG1 = dPnt(down(pnt1, 0.1 * distance(p1, p2)))
        BG2 = dPnt(polar(BG1, 0.75 * distance(p1, p2), angleOfLine(p0, p11))) #grainline is set parallel to side seam
        B.addGrainLine(BG1, BG2)
        pth = (['M', p21, 'L', p11])
        B.addFoldLine(pth)
        B.addGridLine(['M', p5, 'L', p0, 'L', p2, 'L', p7, 'L', p5, 'M', p23, 'L', p1, 'M', p20, 'L', p3, 'M', w1, 'C', w9, 'M', p22, 'L', p19, 'L', p0])
        pth = (['M', w8, 'C', w0, 'L', w1, 'L', p17, 'L', p25, 'L', p21, 'C', p20, 'C', p24, 'C', p22, 'L', w8])
        B.addSeamLine(pth)
        B.addCuttingLine(pth)  
        
        #draw Front Waist Facing C
        pnt1 = dPnt((w2.x + 0.1 * distance(w0, w2), w2.y + 0.75 * distance(w2, w3)))
        pnt2 = dPnt((w2.x + 0.2 * distance(w0, w2), w2.y + 0.2 * distance(w2, w3)))
        pnt3 = dPnt((w2.x + 0.4 * distance(w0, w2), w2.y + 0.4 * distance(w2, w3)))
        C.setLetter((pnt1.x, pnt1.y), scaleby=5.0)        
        C.setLabelPosition((pnt2.x, pnt2.y))
        CG1 = dPnt((pnt3.x, pnt3.y))
        CG2 = dPnt(right(CG1, 0.5 * distance(w0, w2))) 
        C.addGrainLine(CG1, CG2)
        pth = (['M', w0, 'L', w1, 'L', w3, 'L', w2, 'L', w0])
        C.addSeamLine(pth)
        C.addCuttingLine(pth) 
        
        #draw Back Waist Facing D
        pnt1 = dPnt((w8.x + 0.1 * distance(w8, w0), w8.y + 0.85 * distance(w8, w9)))
        pnt2 = dPnt((w8.x + 0.2 * distance(w8, w0), w8.y + 0.5 * distance(w8, w9)))
        pnt3 = dPnt((w8.x + 0.6 * distance(w8, w0), w0.y + 0.5 * distance(w0, w1)))
        D.setLetter((pnt1.x, pnt1.y), scaleby=5.0)        
        D.setLabelPosition((pnt2.x, pnt2.y))
        DG1 = dPnt((pnt3.x, pnt3.y))
        DG2 = dPnt(right(DG1, 0.3 * distance(w0, w8))) 
        D.addGrainLine(DG1, DG2)
        pth = (['M', w8, 'C', w0, 'L', w1, 'C', w9, 'L', w8])
        D.addSeamLine(pth)
        D.addCuttingLine(pth)
        
        #draw Fly Facing E
        pnt1 = dPnt((f1.x + 0.15 * distance(f1, w2), f1.y + 0.2 * distance(f1, f2)))
        pnt2 = dPnt((pnt1.x, f1.y + 0.25 * distance(f1, f2)))
        pnt3 = dPnt((pnt1.x + + 0.5 * distance(f1, w2), f1.y + 0.5 * distance(f1, f2)))
        E.setLetter((pnt1.x, pnt1.y), scaleby=3.0)        
        E.setLabelPosition((pnt2.x, pnt2.y))
        EG1 = dPnt((pnt3.x, pnt3.y))
        EG2 = dPnt(down(EG1, 0.35 * distance(f1, f2))) 
        E.addGrainLine(EG1, EG2)
        pth = (['M', f1, 'L', w2, 'L', f3, 'L', f2, 'L', f1])
        E.addSeamLine(pth)
        E.addCuttingLine(pth)                                

        # call draw once for the entire pattern
        self.draw()
        return
#vi:set ts=4 sw=4 expandta2:

