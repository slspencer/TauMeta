def trueDart(p1, p2, dart_leg1, dart_leg2, dart_point):
    """
    trues dart from p1 to p2
    Accepts dart and two points p1 & p2 nearest points on both sides of dart, 0 < extension <= 1
    dart_inside_leg and dart_outside_leg are updated to new longer point on dart legs
    Line drawn between p1 & p2 after the dart is created
    p1 is next to dart_leg1, dart_leg2 is next to p2
    """

    #rotate point 'p1' to p1_temp where it would lie if dart were closed
    rotation_angle = angleOfVector(dart_inside_leg, dart_point, dart_outside_leg)
    p1_temp = rotate(dart_point, p1, rotation_angle) #dart_point is pivot, p1 is rotated about pivot in clockwise direction.  Use negative angle to move counterclockwise direction
    
    #find intersection of dart_leg1 and line p1_temp to p2
    dart_leg1_new = intersectLines(dart_point, dart_leg1, p1_temp, p2)

    #get new dart_leg2
    dart_leg2_new = rotate(dart_point, dart_leg1_new, -rotation_angle) 
   

    #update dart_inside_leg & dart_outside_leg
    return dart_leg1_new, dart_leg2_new


def polar(p1, length, angle):
    '''
    Adapted from http://www.teacherschoice.com.au/maths_library/coordinates/polar_-_rectangular_conversion.htm
    Accepts p1 as type Point, distance as float, angle as float. angle is in radians
    Returns p2 as type Point,  calculated at distance and angle from p1,
    Angles start at position 3:00 and move clockwise due to y increasing downwards on Cairo Canvas
    '''
    p1 = dPnt(p1)
    # if length is negative, create point in opposite direction from angle
    if (length < 0):
        angle = angle + ANGLE180
    r = length
    x = p1.x + (r * cos(angle))
    y = p1.y + (r * sin(angle))
    return (x, y)
    
def angleOfLine(p1, p2):
    """
    Accepts p1 & p2 of class point or coordinate pairs
    Returns the angle in radians of the vector between them
    """
    angle = math.atan2(p2.y - p1.y, p2.x - p1.x)
    #get the actual angle, don't return negative angles
    if angle < 0:
        angle = 2*pi + angle
    return angle

def angleOfVector(p1, v, p2):
    """
    Accepts p1,  v,  and p2 of class Point or coordinate pairs
    Returns the angle in radians between the vector v-to-p1 and vector v-to-p2
    """
    angle1 = angleOfLine(v, p1)
    angle2 = angleOfLine(v, p2)
    #get the absolute angle
    angle = abs(angle1 - angle2)
    #get the smallest angle of the vector, should not be greater than a straight line
    if angle > pi:
        angle = 2*pi - angle
    return angle

def rotate(pivot, pnt, rotation_angle):
    '''
    Accepts pivot point, single point to rotate, and rotation angle.
    Returns new point after rotatation.
    '''
    return polar(pivot, distance(pivot, pnt), angleOfLine(pivot, pnt) + rotation_angle)
    
def intersectLines(p1, p2, p3, p4):
    """
    Find intersection between two lines. Accepts p1, p2, p3, p4 as class Point. Returns coordinate
    pair at the intersection.
    Intersection does not have to be within the supplied line segments
    """
    p1 = dPnt(p1)
    p2 = dPnt(p2)
    p3 = dPnt(p3)
    p4 = dPnt(p4)
    x, y = 0.0, 0.0
    if (p1.x == p2.x): #if 1st line vertical, use slope of 2nd line
        x = p1.x
        m2 = slopeOfLine(p3, p4)
        b2 = p3.y - (m2 * p3.x)
        y = (m2 * x) + b2
    elif (p3.x == p4.x): #if 2nd line vertical,  use slope of 1st line
        x = p3.x
        m1 = slopeOfLine(p1, p2)
        b1 = p1.y - (m1 * p1.x)
        y = (m1 * x) + b1
    else: #otherwise use ratio of difference between slopes
        m1 = (p2.y - p1.y)/(p2.x - p1.x)
        m2 = (p4.y - p3.y)/(p4.x - p3.x)
        b1 = p1.y - (m1 * p1.x)
        b2 = p3.y - (m2 * p3.x)
        #if (abs(b1-b2) < 0.01) and (m1==m2):
        if (m1 == m2):
            raise ValueError('Parallel lines in intersectLines, no intersection!')
        else:
            x = (b2 - b1)/(m1 - m2)
            y = (m1 * x) + b1 # arbitrary choice, could have used m2 & b2
    return (x, y)
    


    
    
    
    
    
