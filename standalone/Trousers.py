#!/usr/bin/env python
# Trousers.py
# Shaped hem trousers - circa 1850-1890
# Seamly-1870-M-T-1
#
# This is a sample pattern design distributed as part of the tmtp
# open fashion design project. It contains a design for one piece
# of the back of a trousers, and will be expanded in the future.
#
# In order to allow designers to control the licensing of their fashion
# designs, this design file is released under the creative commons license
# http://creativecommons.org/


from tmtpl.constants import *
from tmtpl.pattern import *
from tmtpl.document import *
from tmtpl.client import Client
from tmtpl.curves import GetCurveControlPoints

#Project specific
#from math import sin, cos, radians

from pysvg.filter import *
from pysvg.gradient import *
from pysvg.linking import *
from pysvg.script import *
from pysvg.shape import *
from pysvg.structure import *
from pysvg.style import *
from pysvg.text import *
from pysvg.builders import *


class PatternDesign():

	def __init__(self):
		self.styledefs={}
		self.markerdefs={}
		return

	def pattern(self):
		"""
		Method defining a pattern design. This is where the designer places
		all elements of the design definition
		"""
		CM=CM_TO_PX
		IN=IN_TO_PX
		#The following attributes are set before calling this method:
		#self.cd - Client Data, which has been loaded from the client data file
		#self.styledefs - the style difinition dictionary, loaded from the styles file
		#self.markerdefs - the marker definition dictionary
		#self.cfg - configuration settings from the main app framework
		#TODO - find a way to get this administrative cruft out of this pattern method
		cd=self.cd	#client data is prefaced with cd.
		self.cfg['clientdata']=cd
		#TODO - also extract these from this file to somewhere else
		printer='36" wide carriage plotter'
		if (printer=='36" wide carriage plotter'):
		    self.cfg['paper_width']=(36 * IN)
		self.cfg['border']=(5*CM)#document borders
		BORDER=self.cfg['border']
		self.cfg['verbose']=('1')#document borders
		BORDER=self.cfg['border']
		#TODO - abstract these into configuration file(s)
		metainfo={'companyName':'Seamly Patterns',  #mandatory
					'designerName':'Susan Spencer',#mandatory
					'patternName':'Steampunk Trousers',#mandatory
					'patternNumber':'1870-M-T-1'   #mandatory
					}
		self.cfg['metainfo']=metainfo
		#attributes for the entire svg document
		docattrs={'currentscale' : "0.5 : 1",
					'fitBoxtoViewport' : "True",
					'preserveAspectRatio' : "xMidYMid meet",
					}
		doc=Document(self.cfg, name='document', attributes=docattrs)
		#Set up the Title Block and Test Grid for the top of the document
		TB=TitleBlock('notes', 'titleblock', 0, 0, stylename='titleblock_text_style')
		doc.add(TB)
		TG=TestGrid('notes', 'testgrid', self.cfg['paper_width']/3.0, 0, stylename='cuttingline_style')
		doc.add(TG)

		#Begin the pattern ...

		#pattern values
		pattern_pieces=7
		patternOutsideLeg=112*CM
		patternInsideLeg=80*CM
		patternWaist=86*CM
		patternSeat=102*CM
		patternKnee=50*CM
		patternHemWidth=43*CM
		patternRise=abs(patternOutsideLeg - patternInsideLeg)

		#client values
		#rise=abs(cd.outside_leg - cd.inside_leg) - (0.5*CM)
		scale=cd.seat/2.0 #scale is 1/2 body circumference of reference measurement
		scale_1_4=scale/4.0
		scale_1_8=scale/8.0

		#client ratios
		outsideLegRatio=(cd.outside_leg/patternOutsideLeg)
		outsideLeg=(cd.outside_leg)
		insideLegRatio=(cd.inside_leg/patternInsideLeg)
		insideLeg=cd.inside_leg
		waistRatio=(cd.waist/patternWaist)
		waist=cd.waist
		seatRatio=(cd.seat/patternSeat)
		seat=cd.seat
		kneeRatio=seatRatio
		knee=(patternKnee*kneeRatio)
		hemWidthRatio=seatRatio
		hemWidth=(patternHemWidth*hemWidthRatio)
		riseRatio=(cd.rise/patternRise)
		rise=cd.rise

		#Begin Trousers
		trousers=Pattern('trousers')
		doc.add(trousers)
		#TODO - move next two lines into Pattern class?
		trousers.styledefs.update(self.styledefs)
		trousers.markerdefs.update(self.markerdefs)

		# Begin Trousers Front pattern
		trousers.add(PatternPiece('pattern', 'front', 'A', fabric=2, interfacing=0, lining=0))  # trousers.front
		tf=trousers.front
		#Points
		A=rPoint(tf, 'A', scale_1_8 + (0.5*CM)*seatRatio, 8.0*CM) # waistband
		B=rPoint(tf, 'B', A.x, A.y + (3.8*CM)*riseRatio) # waistline
		C=rPoint(tf, 'C', B.x, B.y + (18.5*CM)*riseRatio) # seatline
		D=rPoint(tf, 'D', B.x, B.y + rise) # riseline
		E=rPoint(tf, 'E', D.x, D.y + (insideLeg/2.0) - (5.5*CM)*insideLegRatio) # kneeline
		F=rPoint(tf,'F', B.x, D.y + insideLeg - (1.0*CM)*insideLegRatio) # hemline
		I=rPoint(tf, 'I', B.x, B.y + abs(C.y - B.y)/2.0) # midpoint b/w waistline and seatline
		p2=rPoint(tf, 'p2', D.x - scale_1_8 - (0.5*CM)*seatRatio, D.y)
		length=(D.x - p2.x)/2.0
		x, y=pointAlongLine(D.x, D.y, (D.x - 100), (D.y - 100), length) # 100pt is arbitrary distance to create 45degree angle
		p3=rPoint(tf, 'p3', x, y)
		p7=rPoint(tf, 'p7', B.x + (waist/4.0), B.y)
		p8=rPoint(tf, 'p8', A.x + (waist/4.0)+(0.75*CM)*waistRatio, A.y)
		p9=rPoint(tf, 'p9', I.x + (seat/4.0) - (1.0*CM)*seatRatio, I.y)
		p10=rPoint(tf, 'p10', C.x + (seat/4.0), C.y)
		p11=rPoint(tf, 'p11', D.x + (seat/4.0) - (0.5*CM)*seatRatio, D.y)
		p16=rPoint(tf, 'p16', p2.x + (abs(p11.x - p2.x)/2.0), p2.y)
		p4=rPoint(tf, 'p4', p16.x - (knee/4.0), E.y)
		p5=rPoint(tf, 'p5', p16.x - (hemWidth/4.0), F.y)
		m=(p5.y - p4.y)/(p5.x-p4.x)
		b=p4.y - (m*p4.x)
		x=(D.y - b)/m
		p6=rPoint(tf, 'p6', x, D.y)
		p12=rPoint(tf, 'p12', p4.x + (knee/2.0), p4.y)
		p13=rPoint(tf, 'p13', p5.x + (hemWidth/2.0), p5.y)
		p14=rPoint(tf, 'p14', p16.x, F.y)
		p15=rPoint(tf, 'p15', p14.x, p14.y - (2.0*CM)*insideLegRatio)
		m=(p13.y - p12.y)/(p13.x-p12.x)
		b=p13.y - (m*p13.x)
		x=(D.y - b)/m
		p30=rPoint(tf, 'p30', x, D.y)
		length=abs(D.y -A.y)
		x, y=pointAlongLine(p16.x, p16.y, p15.x, p15.y, -length)
		G=rPoint(tf, 'G', x, y)
		distance=HEM_ALLOWANCE
		x, y=pointAlongLine(p5.x, p5.y, p4.x, p4.y, distance)
		K=rPoint(tf, 'K', x, y)
		x, y=pointAlongLine(p13.x, p13.y, p12.x, p12.y, distance)
		L=rPoint(tf, 'L', x, y)
		M=rPoint(tf, 'M', p15.x, p15.y - HEM_ALLOWANCE)
		Knee=rPoint(tf, 'Knee', p16.x, E.y)
		#control points for side seam
		distance = ((math.sqrt(((p12.x - p11.x)**2) + ((p12.y - p11.y)**2))) / 3.0)
		x, y=pointAlongLine(p12.x, p12.y, p13.x, p13.y, -distance)
		c4b=cPoint(tf, 'c4b', x, y) #b/w p11 & p12
		pointlist=[]
		pointlist.append(p7)
		pointlist.append(p9)
		pointlist.append(p10)
		pointlist.append(p11)
		pointlist.append(c4b)
		fcp, scp=GetCurveControlPoints('Seamline', pointlist)
		c1a=cPoint(tf, 'c1a', fcp[0].x, fcp[0].y) #b/w p7 & p9
		c1b=cPoint(tf, 'c1b', scp[0].x, scp[0].y) #b/w  p7 & p9
		c2a=cPoint(tf, 'c2a', fcp[1].x, fcp[1].y) #b/w p9 & p10
		c2b=cPoint(tf, 'c2b', scp[1].x, scp[1].y) #b/w p9 & p10
		c3a=cPoint(tf, 'c3a', fcp[2].x, fcp[2].y) #b/w p10 & p11
		c3b=cPoint(tf, 'c3b', scp[2].x, scp[2].y) #b/w p10 & p11
		c4a=cPoint(tf, 'c4a', fcp[3].x, fcp[3].y) #b/w p11 & c4b
		#control points for hemallowance
		pointlist=[]
		pointlist.append(L)
		pointlist.append(M)
		pointlist.append(K)
		fcp, scp=GetCurveControlPoints('HemAllowance', pointlist)
		c5=cPoint(tf, 'c5', fcp[0].x, fcp[0].y) #b/w L & M
		c6=cPoint(tf, 'c6', scp[0].x, scp[0].y) #b/w  L & M
		c7=cPoint(tf, 'c7', fcp[1].x, fcp[1].y) #b/w M & K
		c8=cPoint(tf, 'c8', scp[1].x, scp[1].y) #b/w M & K
		#control points for inseam curve
		distance= ((math.sqrt(((p4.x - p2.x)**2) + ((p4.y - p2.y)**2))) / 3.3)
		x, y=pointAlongLine(p4.x, p4.y, p5.x, p5.y, -distance)
		c9=cPoint(tf, 'c9', x, y) # b/w p4 & p2
		pointlist=[]
		pointlist.append(p4)
		pointlist.append(c9)
		pointlist.append(p2)
		fcp, scp=GetCurveControlPoints('Inseam', pointlist)
		c10=cPoint(tf, 'c10', scp[1].x,  scp[1].y) # b/w p4 & p2
		#control points at front fly curve
		dx = abs(p2.x - p3.x)
		dy = abs(p2.y - p3.y)
		p2a = cPoint(tf, 'p2a', p2.x - dx, p2.y - dy)
		dx = abs(C.x - p3.x)
		dy = abs(C.y - p3.y)
		Ca = cPoint(tf, 'Ca', C.x - dx, C.y - dy)
		pointlist=[]
		pointlist.append(p2)
		pointlist.append(p3)
		pointlist.append(C)
		pointlist.append(Ca)
		fcp, scp=GetCurveControlPoints('Inseam', pointlist)
		c11a=cPoint(tf, 'c11a', fcp[0].x,  fcp[0].y) # b/w p2 & p3
		c11b=cPoint(tf, 'c11b', scp[0].x,  scp[0].y) # b/w p2 & p3
		c11c=cPoint(tf, 'c11c', fcp[1].x,  fcp[1].y) # b/w p3 & C
		c11d=cPoint(tf, 'c11d', scp[1].x, scp[1].y) #b/w p3 & C
		#TODO - improve intersectionOfLines function to accept vertical lines
		#control points for hemline
		pointlist=[]
		pointlist.append(p13)
		pointlist.append(p15)
		pointlist.append(p5)
		fcp, scp=GetCurveControlPoints('HemLine', pointlist)
		c13=cPoint(tf, 'c13', fcp[0].x, fcp[0].y) #b/w 13 & 15
		c14=cPoint(tf, 'c14', scp[0].x, scp[0].y) #b/w  13 & 15
		c15=cPoint(tf, 'c15', fcp[1].x, fcp[1].y) #b/w 15 & 5
		c16=cPoint(tf, 'c16', scp[1].x, scp[1].y) #b/w 15 & 5
		#fly stitch line
		f1=rPoint(tf, 'f1', C.x + (5*CM)*seatRatio, C.y)
		f2=rPoint(tf, 'f2', f1.x, A.y)
		c17=cPoint(tf, 'c17', p3.x+ (abs(f1.x-p3.x) / 2.0), p3.y) #b/w p3 & f1
		c18=cPoint(tf, 'c18', f1.x, f1.y + (abs(f1.y-p3.y) / 2.0))#b/w p3 & f1

		# Trousers Front Grid lines
		g=path()
		#vertical grid
		moveP(g, A)
		lineP(g, F)
		moveP(g, p6)
		lineP(g, p5)
		moveP(g, p30)
		lineP(g, p13)
		moveP(g, G)
		lineP(g, p14)
		#horizontal grid
		moveP(g, I)
		lineP(g, p9)
		moveP(g, C)
		lineP(g, p10)
		moveP(g, p2)
		lineP(g, p11)
		moveP(g, p4)
		lineP(g, p12)
		moveP(g, p5)
		lineP(g, p13)
		#diagonal grid
		moveP(g, D)
		lineP(g, p3)
		# Trousers Front Gridline path
		tf.add(Path('reference','grid', 'Trousers Front Gridline', g, 'gridline_style'))

		#trousers front waist line
		wl=path()
		moveP(wl, B)
		lineP(wl, p7)
		#trousers front waist line path
		tf.add(Path('pattern', 'waistLine', 'Trousers Front Waist line', wl, 'dart_style'))

		#trousers front fly line
		fl=path()
		moveP(fl, p3)
		cubicCurveP(fl, c17,  c18, f1)
		lineP(fl, f2)
		#trousers front fly line path
		tf.add(Path('pattern', 'flyLine', 'Trousers Front Fly line', fl, 'dart_style'))

		#Trousers Front Grainline & Label Location
		g1=rPoint(tf, 'g1', p16.x, C.y)
		g2=rPoint(tf, 'g2', p16.x, (p4.y + (abs(p14.y - p4.y) / 2.0)))

		# Trousers Front Cuttingline & Seamline
		c=path()
		s=path()
		paths=[]
		paths.append(c)
		paths.append(s)
		for p in paths:
			#print p.get_d
			# Trousers Front Waistband
			moveP(p, A)
			lineP(p, p8)
			lineP(p, p7)
			#Trousers Front Sideseam
			cubicCurveP(p, c1a, c1b, p9)
			cubicCurveP(p, c2a, c2b, p10)
			cubicCurveP(p, c3a, c3b, p11)
			cubicCurveP(p, c4a, c4b, p12)
			lineP(p, p13)
			#Trousers Front Hemline
			cubicCurveP(p, c13, c14, p15)
			cubicCurveP(p, c15, c16, p5)
			#Trousers Front Inseam
			lineP(p, p4)
			cubicCurveP(p, c9, c10, p2)
			#Trousers Front Centerseam
			cubicCurveP(p, c11a, c11b, p3)
			cubicCurveP(p, c11c, c11d, C)
			lineP(p, A)
			print p.get_d()
			#p = s
		# Trousers Front Seamline & Cuttingline paths
		(tf.label_x, tf.label_y)=( p16.x + (2.0*CM), p16.y)
		tf.add(grainLinePath("grainLine", "Trousers Front Grainline", g1, g2))
		tf.add(Path('pattern', 'seamLine', 'Trousers Front Seamline', s,  'seamline_path_style'))
		tf.add(Path('pattern', 'cuttingLine', 'Trousers Front Cuttingline', c, 'cuttingline_style'))

		#Trousers Front Waistband Pattern
		trousers.add(PatternPiece('pattern', 'FrontWaistBand', 'B', fabric=1, interfacing=1, lining=0))  # trousers.frontwaistband
		tfwb=trousers.FrontWaistBand
		#Trousers Front Waistband Grainline & Label
		g1=rPoint(tfwb, 'g1', A.x + (9*CM)*waistRatio, A.y + (0.5*CM)*riseRatio)
		g2=rPoint(tfwb, 'g2', A.x + (9*CM)*waistRatio, B.y - (0.5*CM)*riseRatio)
		# Front Waistband Seamline & Cuttingline
		c=path()
		s=path()
		paths=[]
		paths.append(c)
		paths.append(s)
		for p in paths:
			print p
			moveP(p, A)
			lineP(p, p8)
			lineP(p, p7)
			lineP(p, B)
			lineP(p, A)
			print p.get_d
		# create paths & label location
		(tfwb.label_x,  tfwb.label_y)=(A.x + (1.0*CM)*waistRatio, A.y + (1.0*CM)*riseRatio)
		tfwb.add(grainLinePath('grainLine',  "Trousers Front Waistband Grainline", g1, g2))
		tfwb.add(Path('pattern', 'seamLine', 'Trousers Front Waistband Seamline', s, 'seamline_path_style'))
		tfwb.add(Path('pattern', 'cuttingLine', 'Trousers Front Waistband Cuttingline', c, 'cuttingline_style'))


		#Trousers Front Fly Pattern
		trousers.add(PatternPiece('pattern', 'frontFly', letter='C', fabric=3, interfacing=2, lining=0))
		tff=trousers.frontFly
		#Trousers Front Fly Grainline & Label Location
		g1=rPoint(tff, 'g1', A.x + (3.0*CM)*waistRatio, A.y + (5.0*CM)*riseRatio)
		g2=rPoint(tff, 'g2', A.x + (3.0*CM)*waistRatio, f1.y - (2.0*CM)*riseRatio)
		# Trousers Front Fly Seamline & Cuttingline
		s = path()
		c = path()
		paths=[]
		paths.append(s)
		paths.append(c)
		for p in paths:
			moveP(p, A)
			lineP(p, C)
			cubicCurveP(p, c11d, c11c, p3)
			cubicCurveP(p, c17, c18, f1)
			lineP(p, f2)
			lineP(p, A)
		# create paths & label location
		(tff.label_x,  tff.label_y)=(A.x + (0.5*CM)*waistRatio, A.y + (2.0*CM)*riseRatio)
		tff.add(grainLinePath("grainLine", "Trousers Front Fly Grainline", g1, g2))
		tff.add(Path('pattern', 'seamLine', 'Trousers Front Fly Seamline', s, 'seamline_path_style'))
		tff.add(Path('pattern', 'cuttingLine', 'Trousers Front Fly Cuttingline', c, 'cuttingline_style'))

		#Trousers Front Hemlining Pattern
		trousers.add(PatternPiece('pattern', 'frontHemLining', letter='D', fabric=2, interfacing=0, lining=0))
		tfh = trousers.frontHemLining
		#Trousers Front Hemlining Grainline & Label Location
		g1=rPoint(tfh, 'g1', p15.x, M.y + (1.0*CM))
		g2=rPoint(tfh, 'g2', p15.x, p15.y  - (1.0*CM))
		#Trousers Front Hemlining Seamline & Grainline
		s=path()
		c=path()
		paths=[]
		paths.append(s)
		paths.append(c)
		for p in paths:
			moveP(p, p5)
			lineP(p, K)
			cubicCurveP(p, c8, c7, M)
			cubicCurveP(p, c6, c5, L)
			lineP(p, p13)
			cubicCurveP(p, c13, c14, p15)
			cubicCurveP(p, c15, c16, p5)
		# create paths & label location
		(tfh.label_x,  tfh.label_y)=(K.x + (2.0*CM), K.y + (1.0*CM))
		tfh.add(grainLinePath("grainLine", "Trousers Front Hemlining Grainline", g1, g2))
		tfh.add(Path('pattern', 'seamLine', 'Trousers Front Hemlining Seamline', s, 'seamline_path_style'))
		tfh.add(Path('pattern', 'cuttingLine', 'Trousers Front Hemlining Cuttingline', c, 'cuttingline_style'))


		#Trousers Back Pattern
		trousers.add(PatternPiece('pattern', 'back', letter='E', fabric=2, interfacing=0, lining=0))
		tb=trousers.back
		#Points
		#back center points
		p17=rPoint(tb, 'p17', p2.x - (3*CM)*seatRatio, p2.y)# extends back crotch measurement by 3cm
		p19=rPoint(tb, 'p19', A.x +(5*CM)*waistRatio, A.y)
		#back waist points
		distance=-(2.0*CM)*waistRatio
		x, y=pointAlongLine(p19.x, p19.y, C.x, C.y, distance)
		p20=rPoint(tb, 'p20', x,y)# waistline at back center seam
		r=(waist/4.0) + (2.0*CM)*waistRatio
		a, b, y=p20.x, p20.y, B.y
		x=abs(math.sqrt(r**2 - (y - b)**2) + a)
		p21=rPoint(tb, 'p21', x, y)# waistline at side seamside seam --> waist/4 + 2cm) away from p20
		distance=-(3.8*CM)*riseRatio
		x, y=pointAlongLine(p20.x, p20.y, p19.x, p19.y, distance) #
		W=rPoint(tb, 'W', x, y)#W --> (4cm) up from waistline, same as waistband height at side seam.
		distance=(waist/4.0) + (2.0*CM)*waistRatio+ (0.75*CM)*waistRatio
		x1=tb.W.x + (p21.x - p20.x)#find x of a point through W at same slope as waistline p20p21
		y1=tb.W.y + (p21.y - p20.y) #find y of point through W at same slope as waistline p20p21
		x, y=pointAlongLine(tb.W.x, tb.W.y, x1, y1, distance)#adds line from W parallel to p20p21 to find p22
		p22=rPoint(tb, 'p22', x, y)# top of waistband at side seam (4cm from waistline)
		distance=-(5.0*CM*riseRatio)
		x, y=pointAlongLine(p20.x, p20.y, p19.x, p19.y, distance)
		p23=rPoint(tb, 'p23', x, y)# top of waistband at center back seam (5cm from waistline)
		distance=(4.5*CM*waistRatio)
		x, y=pointAlongLine(p23.x, p23.y, p22.x, p22.y, distance)
		p24=rPoint(tb, 'p24', x, y)# back button
		distance=(2.5*CM)*riseRatio
		x, y=pointAlongLine(p24.x, p24.y, p23.x, p23.y, distance, 90)
		p25=rPoint(tb, 'p25', x, y) #back waistband highpoint
		#back waist dart
		distance=(9.5*CM*waistRatio)
		x, y=pointAlongLine(p22.x, p22.y, p23.x, p23.y, distance)
		H=rPoint(tb, 'H', x, y)# back dart center near top of waistband
		distance=(11.5*CM*riseRatio)
		x, y=pointAlongLine(tb.H.x, tb.H.y, p22.x, p22.y, distance, 90)
		P=rPoint(tb, 'P', x, y)# back dart point
		distance=(1.3*CM)*waistRatio*(0.5)
		x, y=pointAlongLine(tb.H.x, tb.H.y, p22.x, p22.y, distance)
		Q=rPoint(tb, 'Q', x, y)# inside dart point near top of waistband
		x, y=pointAlongLine(tb.H.x, tb.H.y, p22.x, p22.y, -distance)
		R=rPoint(tb, 'R', x, y)#outside dart point near top of waistband
		x, y=intersectionOfLines(tb.H.x, tb.H.y, tb.P.x, tb.P.y, p20.x, p20.y, p21.x, p21.y)
		S=rPoint(tb, 'S', x, y)# back dart center at waistline
		distance=(2*CM)*waistRatio*(0.5)
		x, y=pointAlongLine(tb.S.x, tb.S.y, p21.x, p21.y, distance)
		T=rPoint(tb, 'T', x, y)# inside dart point at waistline
		x, y=pointAlongLine(tb.S.x, tb.S.y, p21.x, p21.y, -distance)
		U=rPoint(tb, 'U', x, y)# outside dart point at waistline
		#side seam points
		p26=rPoint(tb, 'p26', p9.x + (4.5*CM*seatRatio), p9.y)# upper hip at side seam
		p27=rPoint(tb, 'p27', p10.x + (3*CM*seatRatio), p10.y)# seat at side seam
		p28=rPoint(tb, 'p28', p11.x + (1.75*CM*seatRatio), p11.y)# rise at side seam
		x, y=intersectionOfLines(p12.x, p12.y, p13.x, p13.y, p28.x, p28.y, Knee.x, Knee.y)#f intersection of lines p12p13 and p28Knee
		#back hem allowance
		p29=rPoint(tb, 'p29', p14.x, p14.y + (1.3*CM)*insideLegRatio)# lowered back trouser hem
		O=rPoint(tb, 'O', p29.x, p29.y - HEM_ALLOWANCE)# lowered back trouser hemallowance
		#control points for back center curve
		c19=cPoint(tb, 'c19', p17.x + (abs(D.x-p17.x)/2.), p17.y)#b/w  p17 & C
		x, y=intersectionOfLines(C.x, C.y, p23.x, p23.y, p17.x + (abs(D.x-p17.x)/2.), p17.y, p21.x, p21.y)
		c20=cPoint(tb, 'c20', x, y)#b/w p17 & C
		#control points waistband
		c21=cPoint(tb, 'c21', p25.x, p25.y)# b/w p25 & p8
		c22=cPoint(tb, 'c22', tb.H.x, tb.H.y)# b/w p25 & p8
		#control points for back side seam
		distance = (math.sqrt(((p12.x -p28.x)**2) + ((p12.y - p28.y)**2)) / 3.0)
		x, y=pointAlongLine(p12.x, p12.y, p13.x, p13.y, -distance)
		c26b=cPoint(tb, 'c26b', x, y) #b/w p28 & p12
		pointlist=[]
		pointlist.append(p21)
		pointlist.append(p26)
		pointlist.append(p27)
		pointlist.append(p28)
		pointlist.append(c26b)
		fcp, scp=GetCurveControlPoints('BackSideSeam', pointlist)
		c23a=cPoint(tb, 'c23a', fcp[0].x, fcp[0].y) #b/w p21 & p26
		c23b=cPoint(tb, 'c23b', scp[0].x, scp[0].y) #b/w  p21 & p26
		c24a=cPoint(tb, 'c24a', fcp[1].x, fcp[1].y) #b/w p26 & p27
		c24b=cPoint(tb,  'c24b', scp[1].x, scp[1].y) #b/w p26 & p27
		c25a=cPoint(tb, 'c25a', fcp[2].x, fcp[2].y) #b/w p27 & p28
		c25b=cPoint(tb, 'c25b', scp[2].x, scp[2].y) #b/w  p27 & p28
		c26a=cPoint(tb, 'c26a', fcp[3].x, fcp[3].y) #b/w p28 & p12
		#control points hem line
		pointlist=[]
		pointlist.append(p13)
		pointlist.append(p29)
		pointlist.append(p5)
		fcp, scp=GetCurveControlPoints('HemLine', pointlist)
		c27=cPoint(tb, 'c27', fcp[0].x, fcp[0].y)#b/w p13 & p29
		c28=cPoint(tb, 'c28', scp[0].x, scp[0].y)#b/w p13 & p29
		c29=cPoint(tb, 'c29', fcp[1].x, fcp[1].y)#b/w p29 & p5
		c30=cPoint(tb, 'c30', scp[1].x, scp[1].y)#b/w p29 & p5
		#control points hem allowance
		pointlist=[]
		pointlist.append(L)
		pointlist.append(O)
		pointlist.append(K)
		fcp, scp=GetCurveControlPoints('HemAllowance', pointlist)
		c31=cPoint(tb, 'c31', fcp[0].x, fcp[0].y)#b/w L & O
		c32=cPoint(tb, 'c32', scp[0].x, scp[0].y)#b/w L & O
		c33=cPoint(tb, 'c33', fcp[1].x, fcp[1].y)#b/w O & K
		c34=cPoint(tb, 'c34', scp[1].x, scp[1].y)#b/w O & K
		#control points inseam
		distance=(math.sqrt(((p4.x - p17.x)**2) + ((p4.y - p17.y)**2)) / 3.0)
		x, y=pointAlongLine(p4.x, p4.y, p5.x, p5.y, -distance)
		c35a=cPoint(tb, 'c35a', x, y) #b/w p4 & p17
		pointlist=[]
		pointlist.append(p4)
		pointlist.append(c35a)
		pointlist.append(p17)
		fcp, scp=GetCurveControlPoints('BackInseam', pointlist)
		c35b=cPoint(tb, 'c35b', scp[1].x, scp[1].y)#b/w p4 & p17

		#Trousers Back Grid
		gr=path()
		#vertical grid
		moveP(gr, C)
		lineP(gr, A)
		moveP(gr, p5)
		lineP(gr, p6)
		moveP(gr, p30)
		lineP(gr, p13)
		moveP(gr, p14)
		lineP(gr, G)
		#horizontal grid
		moveP(gr, A)
		lineP(gr, p22)
		moveP(gr, B)
		lineP(gr, p21)
		moveP(gr, I)
		lineP(gr, p26)
		moveP(gr, C)
		lineP(gr, p27)
		moveP(gr, p17)
		lineP(gr, p28)
		moveP(gr, p4)
		lineP(gr, p12)
		moveP(gr, p5)
		lineP(gr, p13)
		#diagonal grid
		moveP(gr, W)
		lineP(gr, p22)
		moveP(gr, p17)
		lineP(gr, Knee)
		lineP(gr, p28)
		moveP(gr, p23)
		lineP(gr, p22)
		moveP(gr, p25)
		lineP(gr, p24)
		tb.add(Path('reference','grid', 'Trousers Back Gridline', gr, 'gridline_style'))

		#Trousers Back Waistline marking line
		wl=path()
		moveP(wl, p20)
		lineP(wl, p21)
		tb.add(Path('pattern', 'waistLine', 'Trousers Back Waistline', wl, 'dart_style'))

		#Trousers Back Dart marking lines
		d=path()
		moveP(d, H)
		lineP(d, P)
		moveP(d, Q)
		lineP(d, T)
		lineP(d, P)
		moveP(d, R)
		lineP(d, U)
		lineP(d, P)
		tb.add(Path('pattern', 'dart', 'Trousers Back Dart', d, 'dart_style'))
		#Trousers Back Grainline & Label Location
		g1=rPoint(tb, 'g1',  p16.x, C.y)
		g2=rPoint(tb, 'g2', p16.x, p4.y + (abs(p14.y - p4.y)*(0.5)))

		#Trousers Back Seamline & Cuttingline
		s=path()
		c=path()
		paths=[]
		paths.append(s)
		paths.append(c)
		for p in paths:
			moveP(p, p17)
			cubicCurveP(p, c19, c20, C)
			lineP(p, p23)
			lineP(p, p25)
			cubicCurveP(p, c21, c22, p22)
			lineP(p, p21)
			cubicCurveP(p, c23a, c23b, p26)
			cubicCurveP(p, c24a, c24b, p27)
			cubicCurveP(p, c25a, c25b, p28)
			cubicCurveP(p, c26a, c26b, p12)
			lineP(p, p13)
			cubicCurveP(p, c27, c28, p29)
			cubicCurveP(p, c29, c30, p5)
			lineP(p, p4)
			cubicCurveP(p, c35a, c35b, p17)
		# create paths & label location
		tb.label_x, tb.label_y=p16.x + (3*CM*seatRatio), p16.y
		tb.add(grainLinePath("grainLine", "Trousers Back Grainline", g1, g2))
		tb.add(Path('pattern', 'seamLine', 'Trousers Back Seamline', s, 'seamline_path_style'))
		tb.add(Path('pattern', 'cuttingLine', 'Trousers Back Cuttingline', c, 'cuttingline_style'))

		#Trousers Back  Waistlining Pattern
		trousers.add(PatternPiece('pattern', 'backWaistLining', letter='F', fabric=1, interfacing=1, lining=0))
		tbwl = trousers.backWaistLining
		#Trousers Back Waistlining Dart
		d=path()
		moveP(d, H)
		lineP(d, S)
		moveP(d, Q)
		lineP(d, T)
		moveP(d, R)
		lineP(d, U)
		tbwl.add(Path('pattern', 'dart', 'Trousers Back Waistlining Dart', d, 'dart_style'))

		#Trousers Back Waistlining Grainline & Label location
		m=(p23.y - p20.y) / (p23.x - p20.x)
		g1=rPoint(tbwl, 'g1', p20.x + (3.0*CM), p20.y - (0.5*CM))
		b=g1.y - m*g1.x
		y=p24.y
		g2=rPoint(tbwl, 'g2', ((y - b)/m), y)

		#Trousers Back Waistlining Seamline & Cuttingline
		s=path()
		c=path()
		paths=[]
		paths.append(s)
		paths.append(c)
		for p in paths:
			moveP(p, p23)
			lineP(p, p25)
			cubicCurveP(p, c21, c22, p22)
			lineP(p, p21)
			lineP(p, p20)
			lineP(p, p23)
		# create paths & label location
		(tbwl.label_x,  tbwl.label_y)=(p25.x, p25.y + (3.0*CM))
		tbwl.add(grainLinePath("grainLine", "Trousers Back Waistband Grainline", g1, g2))
		tbwl.add(Path('pattern', 'seamLine', 'Trousers Back Waistlining Seamline', s, 'seamline_path_style'))
		tbwl.add(Path('pattern', 'cuttinLine', 'Trousers Back Waistlining Cuttingline', c, 'cuttingline_style'))

		#Trouser Back Hemlining Pattern
		trousers.add(PatternPiece('pattern', 'backHemLining', letter='G', fabric=2, interfacing=0, lining=0))
		tbhl = trousers.backHemLining
		# Trouser Back Hem Lining Grainline & Label Location
		g1=rPoint(tbhl, 'g1', O.x, O.y + (1.5*CM))
		g2=rPoint(tbhl, 'g2', O.x, p29.y  - (1.5*CM))

		# Trouser Back Hem Lining Seamline & CuttingLine
		s=path()
		c=path()
		paths=[]
		paths.append(s)
		paths.append(c)
		for p in paths:
			moveP(p, K)
			cubicCurveP(p, c34, c33, O)
			cubicCurveP(p, c32, c31, L)
			lineP(p, p13)
			cubicCurveP(p, c27, c28, p29)
			cubicCurveP(p, c29, c30, p5)
			lineP(p, K)
		# create paths & label location
		(tbhl.label_x,  tbhl.label_y)=(K.x + (2.0*CM), K.y + (2.0*CM))
		tbhl.add(grainLinePath("grainLine", "Trousers Back Hemlining Grainline", g1, g2))
		tbhl.add(Path('pattern', 'seamLine', 'seamLine', s, 'seamline_path_style'))
		tbhl.add(Path('pattern', 'cuttingLine', 'cuttingline', c, 'cuttingline_style'))

		#call draw once for the entire pattern
		doc.draw()
		return

# vi:set ts=4 sw=4 expandtab:

