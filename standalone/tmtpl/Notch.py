   def addNotch(self, number, pnt, angle, transform=''):
        notch = Notch(number, pnt.x, pnt.y, angle, transform)
        self.add(notch)
        return notch
        #           group,     name,      label,                  xstart, ystart, xend, yend, styledef='default', transform='') :
        #gline=Line("pattern", 'grainline', self.name + ' Grainline',  p1.x, p1.y, p2.x, p2.y, "grainline_style", transform)
        #gline.setMarker('Arrow1M', start=True, end=True)
        #self.add(gline)
        #return gline


#class Line(pBase):
class Notch(pBase):
    """
    Creates instance of Python class Notch
    Draw notch in pattern group on pattern piece.
    All notches exist in pairs
    """
    def __init__(self, number, xstart, ystart, angle, transform='') :

        self.groupname = 'pattern'
        self.name = 'Notch' + number
        self.label = self.name
        self.sdef = 'notch_style'
        self.xstart = xstart
        self.ystart = ystart
        self.length = SEAM_ALLOWANCE
        self.angle = angle
        self.attrs = {}
        self.attrs['transform'] = transform
        
        # make some checks
        if self.sdef not in self.styledefs:
            raise ValueError("Style %s was specified but isn't defined" % self.sdef)
        pBase.__init__(self)

    def add(self, obj):
        # Lines don't have children. If this changes, change the svg method also.
        raise RuntimeError('The Line class can not have children')

    def getsvg(self):
        """
        generate the svg for this notch and return it as a pysvg object
        """
        if self.debug:
            print 'getsvg() called for Line ID ', self.id

        # an empty dict to hold our svg elements
        md = self.mkgroupdict()

        pstyle = PYB.StyleBuilder(self.styledefs[self.sdef])
        
        pnt = polar(dPnt((self.xstart, self.ystart)), SEAM_ALLOWANCE, self.angle)
        self.xend, self.yend = pnt.x, pnt.y
        
        p = PYB.line(self.xstart, self.ystart, self.xend, self.yend)
        p.set_style(pstyle.getStyle())
        p.set_id(self.id)
        
        for attrname, attrvalue in self.attrs.items():
            p.setAttribute(attrname, attrvalue)
            
        md[self.groupname].append(p)

        return md

    def boundingBox(self, grouplist=None):
        """
        Return two points which define a bounding box around the object
        """
        if grouplist is None:
            grouplist = self.groups.keys()
        #if self.groupname in grouplist:
            #print '         end pattern.Line.boundingBox(', self.name, ')-returning (xmin:', min(self.xstart, self.xend), ' ymin:', min(self.ystart, self.yend) , ') ( xmax:', max(self.xstart, self.xend), ' ymax:', max(self.ystart, self.yend), ')'
            #return (min(self.xstart, self.xend), min(self.ystart, self.yend), max(self.xstart, self.xend), max(self.ystart, self.yend))
        #else:
            #print '         end pattern.Line.boundingBox(', self.name, ')-returning (None, None, None, None)'
            #return None, None, None, None
        if self.groupname in grouplist:
            dd = 'M ' + str(self.xstart) + ' ' + str(self.ystart) + ' L ' +str(self.xend) + ' ' + str(self.yend)
            xmin, ymin, xmax, ymax=getBoundingBox(dd)
            return xmin, ymin, xmax, ymax
        else:
            return None, None, None, None
