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
        self.setInfo('patternNumber', 'MR_B1')
        self.setInfo('patternTitle', 'Spencer Bodice Short')
        self.setInfo('companyName', 'Next Patterns')
        self.setInfo('designerName', 'S.L.Spencer')
        self.setInfo('patternmakerName', 'S.L.Spencer')
        self.setInfo('description', """Women's bodice block pattern with minimum ease, includes long sleeve with elbow dart.""")
        self.setInfo('category', 'Shirt/TShirt/Blouse')
        self.setInfo('type', 'Block')
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

        #create a pattern named 'bodice'
        bodice = self.addPattern('bodice')

# measurement constants
#in_to_pt         = ( 72 / 1    )             #convert inches to printer's points
#cm_to_pt       = ( 72 / 2.54  )          #convert centimeters to printer's points
#cm_to_in        = ( 1 / 2.54 )             #convert centimeters to inches
#in_to_cm        = ( 2.54 / 1 )             #convert inches to centimeters

# sewing constants
#quarter_seam_allowance = ( in_to_pt * 1 / 4 )   # 1/4" seam allowance
#seam_allowance              = ( in_to_pt * 5 / 8 )   # 5/8" seam allowance
#hem_allowance               = ( in_to_pt * 2     )    # 2" seam allowance
#pattern_offset                 = ( in_to_pt * 3     )    # 3" between patterns


        #get client data
        CD = self.CD #client data is prefaced with CD

        #create a pattern named 'bodice'
        bodice = self.addPattern('bodice')

        #create pattern pieces,  assign an id lettercd 
        A = bodice.addPiece('Jacket Back', 'A', fabric = 2, interfacing = 0, lining = 0)
        B = bodice.addPiece('Jacket Front', 'B', fabric = 2, interfacing = 0, lining = 0)
        C = bodice.addPiece('Jacket Sleeve', 'C', fabric = 2, interfacing = 0, lining = 0)

        # Jacket Back

        # reference back center seam points for nape, shoulder, chest, waist, hip, hem
        a1 = A.addPoint('a1',   0,   0, 'corner',   reference_layer,  no_transform)   # start calculations from nape at 0,0
           A.seam.center.shoulder = Point('jacket.back.seam.center.shoulder',  A.nape.x,    A.nape.y + back_shoulder_length, 'smooth', reference_layer,  no_transform)
           A.seam.center.chest = Point( 'jacket.back.seam.center.chest',  A.nape.x + (1*cm_to_pt),  A.nape.y + back_chest_length,  'smooth', reference_layer, A.transform  )
           A.seam.center.waist = Point( 'jacket.back.seam.center.waist', A.nape.x + (2.5*cm_to_pt),  A.nape.y + back_waist_length,    'symmetric', reference_layer, A.transform)
           A.seam.center.hip =  Point( 'jacket.back.seam.center.hip', A.nape.x + (2*cm_to_pt),    A.seam.center.waist.y + back_hip_length, 'smooth', reference_layer,  A.transform )
           A.seam.center.hem = Point( 'jacket.back.seam.center.hem', A.nape.x + (1.5*cm_to_pt),  back_jacket_length,   'smooth', reference_layer, A.transform )
           A.seam.center.hem_allowance = Point( 'jacket.back.seam.center.hem_allowance', A.seam.center.hem.x +0, A.seam.center.hem.y + hem_allowance, 'corner', reference_layer ,  A.transform)

           # reference back side seam points for chest, waist, hip, hem
           A.seam.side.chest = Point( 'jacket.back.seam.side.chest', A.nape.x + back_shoulder_width - (1*cm_to_pt),  A.nape.y + back_chest_length, 'smooth', reference_layer, A.transform )
           A.seam.side.waist = Point( 'jacket.back.seam.side.waist', A.nape.x + back_shoulder_width - (3*cm_to_pt),  A.nape.y + back_waist_length, 'symmetric',  reference_layer, A.transform )
           A.seam.side.hip = Point( 'jacket.back.seam.side.hip', A.nape.x + back_shoulder_width - (2*cm_to_pt),  A.seam.side.waist.y + back_hip_length, 'smooth', reference_layer, A.transform )
           A.seam.side.hem = Point( 'jacket.back.seam.side.hem', A.nape.x + back_shoulder_width - (1.5*cm_to_pt),   back_jacket_length, 'smooth', reference_layer, A.transform )
           A.seam.side.hem_allowance = Point( 'jacket.back.seam.side.hem_allowance', A.seam.side.hem.x, A.seam.side.hem.y + hem_allowance, 'corner',  reference_layer, A.transform )

           # armscye points
           A.balance = Point( 'jacket.back.balance', A.nape.x + back_shoulder_width,  A.nape.y + back_balance_length, 'smooth', reference_layer,  A.transform )
           A.underarm = Point( 'jacket.back.underarm', A.nape.x + back_shoulder_width, A.nape.y + back_balance_length + abs(back_balance_length - back_chest_length)*(.48), 'smooth', reference_layer,  A.transform )

           # diagonal shoulder line
           A.seam.shoulder.high = Point( 'jacket.back.seam.shoulder.high', A.nape.x + back_neck_width, A.nape.y - back_neck_length, 'corner', reference_layer,  A.transform )
           A.seam.shoulder.low   = Point( 'jacket.back.seam.shoulder.low', A.seam.center.shoulder.x + back_shoulder_width + (1*cm_to_pt), A.seam.center.shoulder.y, 'corner', reference_layer,  A.transform )

           # Back Vertical Reference Grid
           d = 'M '+ A.nape.coords   + ' v ' + str( A.height )
           self.DrawPath( reference_layer, d , 'reference' , 'Jacket Back - Center', A.transform )
           d = 'M '+ str(A.nape.x + back_shoulder_width) + ', ' + str(A.nape.y) + ' v ' + str( A.height)
           self.DrawPath( reference_layer, d , 'reference' , 'Jacket Back - Shoulder Width',   A.transform )
           d = 'M '+ str(A.nape.x + A.width) + ', ' + str(A.nape.y)       + ' v ' + str( A.height )
           self.DrawPath( reference_layer, d , 'reference' , 'Jacket Back - Side',   A.transform )
           d = 'M '+ A.seam.shoulder.high.coords  +' v '+ str(back_neck_length)
           self.DrawPath( reference_layer, d, 'reference', 'Jacket Back - Neck',     A.transform )

           # Back Horizontal Reference Grid
           d = 'M '+ A.nape.coords  + ' h ' + str( A.width )   # top grid line
           self.DrawPath( reference_layer, d, 'reference', 'Jacket Back - Top',  A.transform )
           d = 'M ' + str(A.nape.x) + ', ' + str( A.seam.center.shoulder.y)   + ' h ' + str( A.width ) # shoulder grid line
           self.DrawPath( reference_layer, d, 'reference', 'Jacket Back - Shoulder', A.transform )
           d = 'M ' + str(A.nape.x) + ', ' + str( A.seam.center.chest.y)        + ' h ' + str( A.width ) # chest grid line
           self.DrawPath( reference_layer, d, 'reference', 'Jacket Back - Chest',    A.transform )
           d = 'M ' + str(A.nape.x) + ', ' + str( A.seam.center.waist.y)         + ' h ' + str( A.width) # waist
           self.DrawPath( reference_layer, d, 'reference', 'Jacket Back - Waist',    A.transform )
           d = 'M ' + str(A.nape.x) + ', ' + str( A.seam.center.hip.y )           + ' h ' + str( A.width ) #hip
           self.DrawPath( reference_layer, d, 'reference', 'Jacket Back - Hip',      A.transform )
           d = 'M ' + str(A.nape.x) + ', ' + str( A.seam.center.hem.y )         + ' h ' + str( A.width ) # hem
           self.DrawPath( reference_layer, d, 'reference', 'Jacket Back - Hem',      A.transform )
           d = 'M ' + str(A.nape.x) + ', ' + str( A.seam.center.hem_allowance.y )  + ' h ' + str( A.width )# hem allowance
           self.DrawPath( reference_layer, d, 'reference', 'Jacket Back - Hem',      A.transform )
           d = 'M ' + str(A.nape.x) + ', ' + str(A.nape.y + A.height)                + ' h ' + str( A.width )
           self.DrawPath( reference_layer, d, 'reference', 'Jacket Back - End',      A.transform )

           # Back Center Seam line clockwise from bottom left:
           x1, y1 = self.PointwithSlope( A.seam.center.hip.x, A.seam.center.hip.y, A.seam.center.hem.x, A.seam.center.hem.y, abs( A.seam.center.hip.y - A.seam.center.waist.y )*(.3), 'normal' )
           c1 = Point( 'c1', x1, y1, 'control', reference_layer, A.transform)
           c2 = Point( 'c2', A.seam.center.waist.x,  A.seam.center.waist.y + abs( A.seam.center.waist.y -  A.seam.center.hip.y   ) * (.3), 'control', reference_layer, A.transform )
           c3 = Point( 'c3', A.seam.center.waist.x,  A.seam.center.waist.y - abs( A.seam.center.waist.y - A.seam.center.chest.y ) * (.3), 'control', reference_layer,  A.transform )

           x1, y1 = self.PointwithSlope( A.seam.center.chest.x, A.seam.center.chest.y, A.seam.center.shoulder.x, A.seam.center.shoulder.y, abs( A.seam.center.chest.y - A.seam.center.waist.y )*(.3), 'normal' )
           c4 = Point( 'c4', x1, y1, 'control', reference_layer,  A.transform )
           c5 = Point( 'c5', A.seam.center.chest.x - abs(A.seam.center.chest.x - A.seam.center.shoulder.x)*(.3), A.seam.center.chest.y - abs( A.seam.center.chest.y - A.seam.center.shoulder.y )*(.3), 'control', reference_layer,  A.transform )
           c6 = Point( 'c6', A.seam.center.shoulder.x, A.seam.center.shoulder.y + abs( A.seam.center.shoulder.y - A.seam.center.chest.y )*(.3), 'control', reference_layer,  A.transform )

           # Back Center Seam path
           A.seam.center.path  = 'L '+ A.seam.center.hem_allowance.coords +' L '+  A.seam.center.hem.coords + ' L ' +  A.seam.center.hip.coords +' C '+ c1.coords +' '+ c2.coords +' '+ A.seam.center.waist.coords +' C '+ c3.coords +' '+ c4.coords +' '+ A.seam.center.chest.coords +' C '+ c5.coords +' '+ c6.coords + ' '+ A.seam.center.shoulder.coords +' L '+ A.nape.coords

           # Back Neck seam line clockwise from A.nape to high point of shoulder:
           x1, y1       = self.PointwithSlope( A.seam.shoulder.high.x, A.seam.shoulder.high.y, A.seam.shoulder.low.x, A.seam.shoulder.low.y, (abs( A.seam.shoulder.high.y - A.nape.y )*(.75)), 'perpendicular')
           c1 = Point( 'c1_!', x1, y1, 'control', reference_layer,  A.transform) #c1 is perpendicular to shoulder line at A.seam.shoulder.high.

           x1, y1       = self.PointwithSlope( A.nape.x, A.nape.y, A.seam.shoulder.high.x, A.nape.y, ( -(abs( A.seam.shoulder.high.x - A.nape.x ) ) * (.50) ), 'normal')
           c2 = Point( 'c2_!', x1, y1, 'control', reference_layer, A.transform)

           # Back Neck Seam path - starts with 'a1' from Back_Center_Seam
           path 'M ' + a1 + ' C '+ c2.coords +' '+ c1.coords +' '+ A.seam.shoulder.high.coords

           # Back Shoulder & Armhole seam lines clockwise from high point to low point of shoulder to top of side seam
           c1   = Point( 'c1_@', A.seam.shoulder.high.x + (abs( A.seam.shoulder.low.x - A.seam.shoulder.high.x )*(.33)), A.seam.shoulder.high.y + (abs( A.seam.shoulder.low.y - A.seam.shoulder.high.y )*(.4)),  'control', reference_layer,  A.transform )
           c2   = Point( 'c2_@', A.seam.shoulder.high.x + (abs( A.seam.shoulder.low.x - A.seam.shoulder.high.x )*(.6) ), A.seam.shoulder.high.y + (abs( A.seam.shoulder.low.y - A.seam.shoulder.high.y )*(.66)), 'control', reference_layer,   A.transform )

           # Back Shoulder Seam path - starts with 'jacket.back.seam.shoulder.high.coords' from Back_Neck_Seam
           A.seam.shoulder.path = ' C '+ c1.coords +' '+ c2.coords +' '+ A.seam.shoulder.low.coords
           A.seam.armhole.path  = ' Q ' + A.balance.coords + ' ' + A.underarm.coords

           # Back Side seam line clockwise from A.underarm. to hem
           x1, y1 = self.PointwithSlope( A.seam.side.chest.x, A.seam.side.chest.y, A.underarm.x, A.underarm.y, abs(A.seam.center.chest.y - A.seam.side.waist.y) * (.3) , 'normal')
           c1 = Point( 'c1_*' , x1, y1, 'control' , reference_layer,  A.transform)

           c2 = Point( 'c2_*', A.seam.side.waist.x, A.seam.side.waist.y - (abs( A.seam.side.waist.y - A.seam.side.chest.y )*(.3)), 'control', reference_layer,  A.transform )
           c3 = Point( 'c3_*', A.seam.side.waist.x, A.seam.side.waist.y + (abs( A.seam.side.waist.y - A.seam.side.hip.y )*(.3)),   'control', reference_layer,  A.transform )

           x1, y1  = self.PointwithSlope( A.seam.side.hip.x, A.seam.side.hip.y, A.seam.side.hem.x, A.seam.side.hem.y, (abs(A.seam.side.waist.y - A.seam.side.hip.y)*(.3)), 'normal')
           c4 = Point( 'c4_*', x1, y1, 'control', reference_layer,  A.transform )

           # Back Side Seam path -- starts with 'jacket.back.underarm.' from Back_Shoulder_Armhole_Seam
           A.seam.side.path  = ' L '+ A.seam.side.chest.coords +' C '+ c1.coords + ' '+ c2.coords +' '+ A.seam.side.waist.coords +' C '+ c3.coords +' '+ c4.coords +' '+ A.seam.side.hip.coords +' L '+ A.seam.side.hem.coords + ' ' + A.seam.side.hem_allowance.coords

           # Back Hemline path
           A.seam.hem.path = 'M ' +  A.seam.center.hem.coords + ' L ' + A.seam.side.hem.coords

           # Grainline
           g1 = Point( 'g1', (A.seam.shoulder.low.x)/2, A.underarm.y, 'grainline', reference_layer,  A.transform )
           g2 = Point( 'g2', g1.x, g1.y + (60*cm_to_pt), 'grainline', reference_layer,  A.transform )
           A.grainline = Generic()   #not in use at this time
           A.grainline.path = 'M '+ g1.coords + ' L ' + g2.coords # not in use at this time

           # Jacket Back Pattern path
           A.path = A.seam.neck.path +' '+ A.seam.shoulder.path + ' '+ A.seam.armhole.path +' '+ A.seam.side.path + ' ' + A.seam.center.path +' z'

           #Draw Jacket Back pattern piece on pattern layer
           self.DrawPath( A.layer, A.seam.hem.path, 'hemline',  'jacket.back.seam.hem.path',  A.transform )
           self.DrawPath( A.layer, A.path, 'seamline',  'jacket.back.path_Seamline',  A.transform )
           self.DrawPath( A.layer, A.path, 'cuttingline', 'jacket.back.path_Cuttingline',  A.transform )
           self.Grainline( A.layer, g1.x, g1.y, g2.x, g2.y, 'jacket.back.grainline.path',  A.transform )
           #self.DrawGrainline( A.layer, A.grainline.path, 'jacket.back.grainline.path', A.transform ) # use this after creating markers for Arrows at each end of grainline

           # Write description on pattern piece
           x, y = A.nape.x + (5 * cm_to_pt) , A.nape.y + back_shoulder_length
           font_size  = 50
           spacing = (font_size * .20)
           y = ( y+ font_size + spacing )
           self.WriteText( A.layer,  x,  y,  font_size, 'company_name',   company_name,  A.transform )
           y = ( y+ font_size + spacing )
           self.WriteText( A.layer,  x,  y, font_size, 'pattern_number', pattern_number,  A.transform )
           y = ( y+ font_size + spacing )
           self.WriteText( A.layer, x,  y, font_size, 'jacket.back.letter', 'Pattern Piece '+ A.letter,  A.transform )
           if A.fabric > 0:
             y = ( y+ font_size + spacing )
             self.WriteText( A.layer, x, y, font_size, 'jacket.back.fabric', 'Cut '+str(A.fabric)+ ' Fabric',  A.transform )
           if A.interfacing > 0:
             y = ( y+ font_size + spacing )
             self.WriteText( A.interfacing, x,  y, font_size, 'jacket.back.interfacing', 'Cut '+str(A.interfacing)+ ' Interfacing',     A.transform )
           if A.lining > 0:
             y = ( y+ font_size + spacing )
             self.WriteText( A.lining, x, y, font_size, 'jacket.back.lining', 'Cut '+str(A.fabric)+ ' Lining',     A.transform )

           # document calculations
           A.low.x,  A.low.y,  A.high.x,  A.high.y = self.NewBoundingBox( A.path, A.start.x, A.start.y )
           layout.document_low.x  = min( layout.document_low.x ,  A.low.x  )
           layout.document_low.y  = min( layout.document_low.y ,  A.low.y  )
           layout.document_high.x = max( layout.document_high.x, A.high.x)
           layout.document_high.y = max( layout.document_high.y, A.high.y )

           # document calculations
           layout.height = layout.document_high.y + border
           layout.width  = layout.document_high.x + border
           # reset document size
           self.svg_svg( str( layout.width ), str( layout.height ), str( border ) )

# my_effect is an instance of DrawJacket() - my_effect is an arbitrary name
# my_effect.affect() is a built-in function which causes my_effect to evaluate itself - e.g. initialize, execute and thus draw the pattern

my_effect = DrawJacket()
my_effect.affect()
