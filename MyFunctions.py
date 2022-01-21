import math


def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def get_rise(p1, p2):
    return p2[1]-p1[1]

def get_run(p1, p2):
    if p2[0]-p1[0] == 0:
        return 0.0001
    return p2[0]-p1[0]

#Returns float of slope when given 2 points
def get_slope(p1, p2):
    return get_rise(p1, p2)/get_run(p1, p2)

#Returns y-intercept when given slope and point on line
def get_b(slope, p2):
    return p2[1] - p2[0]*(slope)

# returns a list where index 0 is slope(m) and index 1 is y-int(b)
#y = list[o]x + list[1]
def get_line(p1, p2):
    return [get_slope(p1, p2), get_b(get_slope(p1, p2), p1)]

#return angle in radians between two points
def get_angle(p1, p2):
    return math.atan(get_rise(p1, p2)/get_run(p1, p2))


#return angle in degrees between two points
def get_angle_deg(p1, p2):
    return math.degrees(get_angle(p1, p2))

#p1 needs to be the middle of the circle with radius r
def get_circle_points(r, p1, p2):
    angle = get_angle_deg(p1, p2)
    return [p1[0] + r * math.degrees(math.cos(angle)), p1[1] + r * math.degrees(math.sin(angle))]

#p1 needs to be the middle of the circle with radius r
def get_point_circle(r, p1, p2):
    return [p1[0] + get_run(p1, p2)/distance(p1, p2)*r, p1[1] + get_rise(p1, p2)/distance(p1, p2)*r]
