#####################################################
## Author: Xinrui (Leo) Liu
## CMU 2024 15-112 Term Project
## Section: K
#####################################################

from cmu_graphics import  *
from objects import *
def getRoadLineParts(road):
    lines = []
    if road.type == 'Straight':
        # only one straight line for straight road
        x1, y1 = road.points[0]
        x2, y2 = road.points[1]
        lines.append(((x1, y1), (x2, y2)))
    elif road.type == 'Curved':
        start, mid, end = road.points
        numSteps = 10
        points = []
        for i in range(numSteps + 1):
            i /= numSteps
            x = (1 - i)**2*start[0] + 2*(1 - i)*i*mid[0] + i**2*end[0]
            y = (1 - i)**2*start[1] + 2*(1 - i)*i*mid[1] + i**2*end[1]
            points.append((x, y))

        for i in range(len(points)-1):
            lines.append((points[i], points[i + 1]))
    return lines


def findIntersections(app):
    intersections = set()
    for i in range(len(app.roads)):
        road1 = app.roads[i]
        line1 = getRoadLineParts(road1)
        for j in range(i + 1, len(app.roads)):
            road2 = app.roads[j]
            line2 = getRoadLineParts(road2)
            startR1,endR1 = road1.points[0],road1.points[-1]
            startR2,endR2 = road2.points[0],road2.points[-1]
            x1r1,y1r1 = startR1
            x2r1,y2r1 = endR1
            x1r2,y1r2 = startR2
            x2r2,y2r2 = endR2
            for l1 in line1:
                for l2 in line2:
                    point = linesIntersect(l1, l2)
                    if point:
                        cx,cy = point
                        if (getDistance(cx,cy,x1r1,y1r1) > 20 and getDistance(cx,cy,x2r1,y2r1) > 20 and
                            getDistance(cx,cy,x1r2,y1r2) > 20 and getDistance(cx,cy,x2r2,y2r2) > 20):
                            if point and road1.elevation == road2.elevation:
                                inter = Intersection(point, road1.elevation, '4-way', (road1, road2),duration=app.tlDuration)
                                road2.addIntersection(inter)
                                road1.addIntersection(inter)
                                app.intersections.add(inter)
    pointToRoads = {}

    for road in app.roads:
        if road.type == 'Straight':
            endpoints = [road.points[0], road.points[1]]
        elif road.type == 'Curved':
            endpoints = [road.points[0], road.points[2]]

        for point in endpoints:
            roundedPoint = (rounded(point[0]), rounded(point[1]))
            if roundedPoint not in pointToRoads:
                pointToRoads[roundedPoint] = []
            pointToRoads[roundedPoint].append(road)


    for point, roadsAtPoint in pointToRoads.items():
        if len(roadsAtPoint) > 1:
            x, y = point
            interType = len(roadsAtPoint)
            inter = Intersection((x, y), roadsAtPoint[0].elevation, str(interType), roadsAtPoint,duration=app.tlDuration)
            for road in roadsAtPoint:
                road.addIntersection(inter)
            app.intersections.add(inter)

        intersections = list(app.intersections)
        for inter1 in intersections:
            for inter2 in intersections:
                if inter1.type.isdigit() and inter2.type.isdigit():
                    if inter1 == inter2:
                        continue
                    if inter1.elevation == inter2.elevation and inter1.points == inter2.points:
                        if int(inter1.type)>int(inter2.type):
                            if inter2 in intersections:
                                ind = intersections.index(inter2)
                                intersections.pop(ind)
                        else:
                            if inter1 in intersections:
                                ind = intersections.index(inter1)
                                intersections.pop(ind)
        app.intersections = set(intersections)
    return intersections

def checkIntersectsCurve(app):
    for i in range(len(app.roads)):
        road1 = app.roads[i]
        line1 = getRoadLineParts(road1)
        road2 = app.currentRoad
        line2 = getRoadLineParts(road2)
        startR1,endR1 = road1.points[0],road1.points[-1]
        startR2,endR2 = road2.points[0],road2.points[-1]
        x1r1,y1r1 = startR1
        x2r1,y2r1 = endR1
        x1r2,y1r2 = startR2
        x2r2,y2r2 = endR2
        for l1 in line1:
            for l2 in line2:
                point = linesIntersect(l1, l2)
                if point:
                    cx,cy = point
                    if (getDistance(cx,cy,x1r1,y1r1) > 20 and getDistance(cx,cy,x2r1,y2r1) > 20 and
                        getDistance(cx,cy,x1r2,y1r2) > 20 and getDistance(cx,cy,x2r2,y2r2) > 20):
                        if point and road1.elevation == road2.elevation:
                            if app.roads[i].type == 'Curved' or app.currentRoad.type == 'Curved':
                                return i
    return None

def getRoadEdgeLines(app, road):
    leftLines = []
    rightLines = []
    dist = app.roadWidth / 2

    if road.type == 'Straight':
        #check if finished drawing
        if len(road.points) < 2:
            return [], []
        x1, y1 = road.points[0]
        x2, y2 = road.points[1]

        length = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

        if length == 0:
            return [], []
        #unit vector
        dx = (x2 - x1) / length
        dy = (y2 - y1) / length
        #find perpendicular
        perpX = -dy
        perpY = dx

        leftStart = (x1 + dist*perpX, y1 + dist*perpY)
        leftEnd = (x2 + dist*perpX, y2 + dist*perpY)

        rightStart = (x1 - dist*perpX, y1 - dist*perpY)
        rightEnd = (x2 - dist*perpX, y2 - dist*perpY)

        leftLines.append((leftStart, leftEnd))
        rightLines.append((rightStart, rightEnd))

    elif road.type == 'Curved':
        #check if finished drawing
        if len(road.points) < 3:
            return [], []

        points = []
        numSteps = 10
        start, mid, end = road.points
        for i in range(numSteps + 1):
            i /= numSteps
            x = (1 - i) ** 2 * start[0] + 2 * (1 - i) * i * mid[0] + i ** 2 * end[0]
            y = (1 - i) ** 2 * start[1] + 2 * (1 - i) * i * mid[1] + i ** 2 * end[1]
            points.append((x, y))

        leftPoints = []
        rightPoints = []
        for i in range(len(points)):
            if i == len(points) - 1:
                continue
            x1, y1 = points[i]
            x2, y2 = points[i+1]

            length = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
            if length == 0:
                continue
            # unit vector
            dx = (x2 - x1) / length
            dy = (y2 - y1) / length
            # find perpendicular
            perpX = -dy
            perpY = dx

            leftX = x1 + dist*perpX
            leftY = y1 + dist*perpY
            leftPoints.append((leftX, leftY))

            rightX = x1 - dist*perpX
            rightY = y1 - dist*perpY
            rightPoints.append((rightX, rightY))

        #set of points between points[i] and points[i+1]
        for i in range(len(leftPoints)-1):
            leftLines.append((leftPoints[i], leftPoints[i+1]))
        for i in range(len(rightPoints)-1):
            rightLines.append((rightPoints[i], rightPoints[i+1]))

    return leftLines, rightLines


def findEdgeIntersections(app):
    intersections = []

    for road in app.roads:
        road.leftEdgeLines, road.rightEdgeLines = getRoadEdgeLines(app,road)

        road.leftEdgeLines[-1] = extendLine(road.leftEdgeLines[-1][0], road.leftEdgeLines[-1][1], 0)

        road.rightEdgeLines[-1] = extendLine(road.rightEdgeLines[-1][0], road.rightEdgeLines[-1][1], 0)

        road.leftEdgeLines[0] = extendLine(road.leftEdgeLines[-1][1], road.leftEdgeLines[-1][0], 0)

        road.rightEdgeLines[0] = extendLine(road.rightEdgeLines[-1][1], road.rightEdgeLines[-1][0], 0)

    for i in range(len(app.roads)):
        road1 = app.roads[i]

        for j in range(i + 1, len(app.roads)):
            road2 = app.roads[j]

            edgeIntersects = []
            allEdgesR1 = road1.leftEdgeLines + road1.rightEdgeLines
            allEdgesR2 = road2.leftEdgeLines + road2.rightEdgeLines
            for e1 in allEdgesR1:
                for e2 in allEdgesR2:
                    point = linesIntersect(e1, e2)
                    if point:
                        edgeIntersects.append(point)
            if len(edgeIntersects) >= 4:
                edgeIntersects = edgeIntersects[:4]
                intersectionSet = road1.intersections & road2.intersections
                if intersectionSet:
                    inter = intersectionSet.pop()
                    intersections.append((edgeIntersects, (road1, road2), inter))

    return intersections


def sortRoadsElevation(app):
    retGround = []
    retBridge = []
    print(app.roads)
    for road in app.roads:
        if road.elevation == 'Bridge':
            retBridge.append(road)
        elif road.elevation == 'Ground':
            retGround.append(road)
    return retGround + retBridge

def sortRoads(inter):
    anglePoints = []
    cX,cY = inter.points
    for road in inter.roads:
        if road.points[0] == inter.points:
            x, y = road.points[1]
        else:
            x, y = road.points[0]
        angle = math.atan2(y - cY, x - cX)
        anglePoints.append((angle, road))

    for i in range(len(anglePoints)):
        for j in range(i + 1, len(anglePoints)):
            if anglePoints[i][0] > anglePoints[j][0]:
                anglePoints[i], anglePoints[j] = anglePoints[j], anglePoints[i]
    sorted = []
    for angle, road in anglePoints:
        sorted.append(road)
    return sorted

def checkCrossingOutlets(app,currentRoad):
    if currentRoad.type == 'Straight' or currentRoad.type == 'Curved':
        if len(currentRoad.points)>1:
            currentParts = getRoadLineParts(currentRoad)
            for i in range(len(app.roads)):
                road = app.roads[i]
                if road.type == 'Straight':
                    roadParts = getRoadLineParts(road)
                    for currentPart in currentParts:
                        for roadPart in roadParts:
                            intersection = linesIntersect(currentPart, roadPart)

                            if intersection:
                                interX, interY = intersection
                                startDistToIntersect = getDistance(interX, interY, road.points[0][0], road.points[0][1])
                                endDistToIntersect = getDistance(interX, interY, road.points[1][0], road.points[1][1])

                                if endDistToIntersect < 45:
                                    return 'end', (interX,interY),i
                                elif startDistToIntersect < 45:
                                    return 'start', (interX,interY),i

                if road.type == 'Curved':
                    roadParts = getRoadLineParts(road)
                    for currentPart in currentParts:
                        for roadPart in roadParts:
                            intersection = linesIntersect(currentPart, roadPart)

                            if intersection:
                                interX, interY = intersection
                                startDistToIntersect = getDistance(interX, interY, road.points[0][0], road.points[0][1])
                                endDistToIntersect = getDistance(interX, interY, road.points[2][0], road.points[2][1])

                                if endDistToIntersect < 45:
                                    return 'end', (interX,interY),i
                                elif startDistToIntersect < 45:
                                    return 'start', (interX,interY),i