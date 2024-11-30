import math
from PIL import Image

def getDistance(x1,y1,x2,y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def extendLine(point1, point2, extendDist):
    x1, y1 = point1
    x2, y2 = point2

    length = getDistance(x1,y1,x2,y2)

    if length == 0:
        return (x1, y1), (x1, y1)

    uX = (x2 - x1) / length
    uY = (y2 - y1) / length

    #extend twoards point2
    newX2 = x2 + uX * extendDist
    newY2 = y2 + uY * extendDist

    return (x1,y1), (newX2, newY2)

def findMidPoint(point1, point2):

    x1, y1 = point1
    x2, y2 = point2
    return ((x1 + x2)/2, (y1 + y2)/2)

def findPerpendicularPoint(point1, point2, distance):
    x1, y1 = point1
    x2, y2 = point2

    midX, midY = findMidPoint(point1, point2)

    dx = x2 - x1
    dy = y2 - y1

    length = getDistance(x1, y1, x2, y2)

    perpX = -dy
    perpY = dx


    #unit vector
    perpX /= length
    perpY /= length

    px = midX + perpX * distance
    py = midY + perpY * distance

    return (px, py)


def findPointAtDistance(x1, y1, x2, y2, distance):

    totalDistance = getDistance(x1, y1, x2, y2)
    if totalDistance == 0:
        return (x1, y1)

    r = distance / totalDistance
    x = x1 + r*(x2 - x1)
    y = y1 + r*(y2 - y1)

    return (x, y)

def findAngleTwoPints(x1,y1,x2,y2):
    angle = math.atan2(y2 - y1, x2 - x1)
    degrees = math.degrees(angle)
    if x1<=x2:
        degrees += 90
    else:
        if y2>y1:
            degrees += 90
        else:

            degrees += 90

    return degrees

def findPointAtAngleDistance(x1, y1, angle, distance):

    x2 = x1 + distance * math.cos(math.radians(angle))
    y2 = y1 + distance * math.sin(math.radians(angle))
    return (x2, y2)

##The function loadPilImage(url) is from TP-Related Demos
## -> https://www.cs.cmu.edu/~112/notes/tp-related-demos/tp-related-demos.html

# This demos PIL getpixel and putpixel.
def loadPilImage(url):
    # Loads a PIL image (not a CMU image!) from a url:
    return Image.open(url)


def linesIntersect(line1, line2):
    (x1, y1), (x2, y2) = line1
    (x3, y3), (x4, y4) = line2

    #find slopes
    #if line 1 is vertical
    if x2 - x1 == 0:
        r1 = None
    else:
        r1 = (y2 - y1) / (x2 - x1)

    if x4 - x3 == 0:
        r2 = None
    else:
        r2 = (y4 - y3) / (x4 - x3)
    #find the intersection point
    if r1 == None and r2 == None:
        return None

    elif r1 == None:
        x = x1
        # y-y2 = r(x-x1)+y2
        y = r2 * (x - x3) + y3
    elif r2 == None:
        x = x3
        y = r1 * (x - x1) + y1
    elif r1 == r2:
        return None
    else:
        # y = r2 * (x - x3) + y3
        # y=r1 * (x - x1) + y1
        # r1 * (x - x1) + y1 = r2 * (x - x3) + y3
        x = (r2 * x3 - r1 * x1 + y1 - y3) / (r2 - r1)
        y = r1 * (x - x1) + y1

    #check if the intersection is in both lines
    if (min(x1, x2) <= x <= max(x1, x2) and
            min(y1, y2) <= y <= max(y1, y2) and
            min(x3, x4) <= x <= max(x3, x4) and
            min(y3, y4) <= y <= max(y3, y4)):
        return (x, y)
    else:
        return None

def findClosestPoint(point1, points):
    closestPointInd = None
    closestDistance = 100000
    x1, y1 = point1
    for i in range(len(points)):
        point = points[i]
        x2, y2 = point
        distance = getDistance(x1,y1,x2,y2)
        if distance < closestDistance:
            closestPointInd = i
            closestDistance = distance
    return closestPointInd


