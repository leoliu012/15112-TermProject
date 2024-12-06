#####################################################
## Author: Xinrui (Leo) Liu
## CMU 2024 15-112 Term Project
## Section: K
#####################################################

from cmu_graphics import  *
from practicalFunctions import *
from objects import *
from roadCalculations import *
def drawRoad(app,road):
    roadType = road.type
    points = road.points
    elevation = road.elevation
    if roadType == 'Straight':
        #chekc if drawing is finished
        if len(points) >= 2:
            drawStraightRoad(app,points[0], points[1], elevation,road)
            if app.isDrawing or app.shortCutMode:
                road.laneMarkings = findLaneMarking(app, road.points)
                drawLaneMarking(app, road.laneMarkings)
            else:
                drawLaneMarking(app, road.laneMarkings)

    if roadType == 'Curved':
        if len(points) == 3:
            drawCurvedRoad(app,points[0], points[1], points[2], elevation,road)
            return
        elif len(points) == 2:
            drawCurvedRoad(app,points[0], points[1], points[1], elevation,road)

def drawStraightRoad(app,start,end,elevation,road):
    x1,y1 = start
    x2,y2 = end
    if app.BDselect == road or road.highlighted:
        color = 'darkRed'
    else:
        color = getElevationColor(elevation)

    drawLine(x1,y1,x2,y2,fill = color,lineWidth = app.roadWidth, opacity = app.roadOpacity)
    drawCircle(x1,y1, app.roadWidth/2, fill=color,  opacity = app.roadOpacity)
    drawCircle(x2,y2, app.roadWidth/2, fill=color,  opacity = app.roadOpacity)

    if road.elevation == 'Bridge':
        for each in road.leftEdgeLines:
            for i in range(len(each)-1):
                x1,y1 = each[i]
                x2,y2 = each[i+1]
                drawLine(x1,y1,x2,y2,fill='black',lineWidth = 2)
        for each in road.rightEdgeLines:
            for i in range(len(each) - 1):
                x1, y1 = each[i]
                x2, y2 = each[i + 1]
            drawLine(x1,y1,x2,y2,fill='black',lineWidth = 2)

def drawCurvedRoad(app, start, mid, end, elevation,road):
    #use Bézier curve here
    #learned this from:
    #https://javascript.info/bezier-curve

    points = []
    numSteps = 10

    for i in range(numSteps+1):
        i /= numSteps
        x=(1 - i)**2*start[0] + 2*(1 - i)*i*mid[0] + i** 2*end[0]
        y=(1 - i)**2*start[1] + 2*(1 - i)*i*mid[1] + i** 2*end[1]
        points.append((x, y))

    if app.BDselect == road or road.highlighted:
        color = 'darkRed'
    else:
        color = getElevationColor(elevation)
    for i in range(len(points)-1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        drawLine(x1, y1, x2, y2, fill=color, lineWidth=app.roadWidth, opacity=app.roadOpacity)

    if road.elevation == 'Bridge':
        for each in road.leftEdgeLines:
            for i in range(len(each)-1):
                x1,y1 = each[i]
                x2,y2 = each[i+1]
                drawLine(x1,y1,x2,y2,fill='black',lineWidth = 2)
        for each in road.rightEdgeLines:
            for i in range(len(each) - 1):
                x1, y1 = each[i]
                x2, y2 = each[i + 1]
            drawLine(x1,y1,x2,y2,fill='black',lineWidth = 2)

    #draw circles to make the curve smooth
    for x,y in points:
        drawCircle(x, y, app.roadWidth / 2, fill=color, opacity=app.roadOpacity)

    drawCircle(start[0], start[1], app.roadWidth / 2, fill=color, opacity=app.roadOpacity)
    drawCircle(end[0],end[1], app.roadWidth / 2, fill=color, opacity=app.roadOpacity)

    if app.isDrawing or app.shortCutMode:
        road.laneMarkings = findLaneMarking(app, points)
        drawLaneMarking(app, road.laneMarkings)
    else:
        drawLaneMarking(app, road.laneMarkings)

# Draw dashed lane markings and intersections on the road
def findLaneMarking(app,points):
    if len(points) >= 2:
        totalLength = 0
        segmentLengths = []

        for i in range(len(points)-1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            length = ((x1-x2)**2 + (y1-y2)**2)**0.5
            segmentLengths.append(length)
            totalLength += length

        dashPos = []
        distance = 0
        for i in range(len(points)-1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            dx = x2-x1
            dy = y2-y1
            segmentLength = segmentLengths[i]
            while distance < segmentLength:
                r = distance / segmentLength
                dashX = x1 + dx*r
                dashY = y1 + dy*r
                dashPos.append((dashX,dashY))
                distance += app.laneMarkingInterval*2

            distance -= segmentLength
        return dashPos

def drawLaneMarking(app,dashPos):
    for i in range(0,len(dashPos)-1,2):
        drawLine(dashPos[i][0],dashPos[i][1],
                 dashPos[i+1][0],dashPos[i+1][1], fill='white', lineWidth=2)

def getElevationColor(elevation):
    if elevation == 'Ground':
        return 'gray'
    elif elevation == 'Bridge':
        return 'dimGray'
    else:
        return 'gray'


def drawIntersectMarking(app):
    visitedBG = set()
    for inter in app.intersections:
        if inter.elevation == 'Bridge' and inter.points not in visitedBG and inter.type.isdigit():
            visitedBG.add(inter.points)
            cx,xy = inter.points
            drawCircle(cx, xy, app.roadWidth/2, fill='dimGray')
            for road in inter.roads:
                if road.type == 'Straight':
                    if road.points[0] == inter.points:
                        x1,y1 = road.points[0]
                        x2,y2 = road.points[1]
                    else:
                        x1, y1 = road.points[1]
                        x2, y2 = road.points[0]
                else:
                    if road.points[0] == inter.points:
                        x1, y1 = road.points[0]
                        x2, y2 = road.points[1]
                    else:
                        x1, y1 = road.points[2]
                        x2, y2 = road.points[1]
                lx,ly = findPointAtDistance(x1, y1, x2, y2, 20)
                drawLine(x1, y1,lx,ly,fill='dimGray',lineWidth = app.roadWidth+3)

    visited = set()
    for each in app.edgeIntersections:
        intersectPoints, roads, inter = each

        if intersectPoints[0] not in visited:
            visited.add(intersectPoints[0])
            #find centroids
            totalNum = len(intersectPoints)

            xs = []
            ys = []
            for x, y in intersectPoints:
                xs.append(x)
                ys.append(y)
            cX = sum(xs) /totalNum
            cY = sum(ys) /totalNum

            #angle relative to the centroid
            anglePoints = []
            for point in intersectPoints:
                x, y = point
                angle = math.atan2(y - cY, x - cX)
                anglePoints.append((angle, point))

            for i in range(len(anglePoints)):
                for j in range(i + 1, len(anglePoints)):
                    if anglePoints[i][0] > anglePoints[j][0]:
                        anglePoints[i], anglePoints[j] = anglePoints[j], anglePoints[i]

            sorted = []
            for angle, point in anglePoints:
                sorted.append(point)

            polygonXY = []
            for x, y in sorted:
                polygonXY.extend([x, y])

            drawPolygon(*polygonXY, fill='gray')

def drawIntersectMarkingWithTL(app):
    visited = set()
    for each in app.edgeIntersections:
        intersectPoints, roads, inter = each

        if intersectPoints[0] not in visited:
            visited.add(intersectPoints[0])
            #find centroids
            totalNum = len(intersectPoints)

            xs = []
            ys = []
            for x, y in intersectPoints:
                xs.append(x)
                ys.append(y)
            cX = sum(xs) /totalNum
            cY = sum(ys) /totalNum

            #angle relative to the centroid
            anglePoints = []
            for point in intersectPoints:
                x, y = point
                angle = math.atan2(y - cY, x - cX)
                anglePoints.append((angle, point))

            for i in range(len(anglePoints)):
                for j in range(i + 1, len(anglePoints)):
                    if anglePoints[i][0] > anglePoints[j][0]:
                        anglePoints[i], anglePoints[j] = anglePoints[j], anglePoints[i]

            sorted = []
            for angle, point in anglePoints:
                sorted.append(point)

            polygonXY = []
            for x, y in sorted:
                polygonXY.extend([x, y])

            for i in range(len(sorted)-1):
                x1, y1 = sorted[i]
                x2, y2 = sorted[i+1]


                midx, midy = findMidPoint((x1, y1), (x2, y2))

                drawTrafficLights(app, (midx, midy), (x1, y1), i,inter,(x2,y2))
            x1, y1 = sorted[-1]
            x2, y2 = sorted[0]
            midx, midy = findMidPoint((x1, y1), (x2, y2))

            drawTrafficLights(app, (midx, midy), (x1, y1), 3, inter,(x2,y2))

def drawTrafficLightsForMagCursor(app):
    visited = set()
    for inter in app.intersections:
        if (inter.type == '4' or inter.type == '3') and inter.points not in visited:
            inter.roads = sortRoads(inter)
            visited.add(inter.points)
            for i in range(len(inter.roads)):
                road = inter.roads[i]


                if i == 0 or i == 2:
                    tl = TrafficLight(inter, 0, duration=app.tlDuration)
                    tl.road = road
                    inter.trafficLights.append(tl)
                else:
                    tl = TrafficLight(inter, 3,duration=app.tlDuration)

                    tl.road = road
                    inter.trafficLights.append(tl)

                if road.type == "Curved":
                    start, mid, end = road.points
                    numSteps = 10
                    points = []
                    for j in range(numSteps + 1):
                        j /= numSteps
                        x = (1 - j) ** 2 * start[0] + 2 * (1 - j) * j * mid[0] + j ** 2 * end[0]
                        y = (1 - j) ** 2 * start[1] + 2 * (1 - j) * j * mid[1] + j ** 2 * end[1]
                        points.append((x, y))
                else:
                    points = road.points

                if road.points[0] == inter.points:
                    rx1,ry1 = points[0]
                    rx2,ry2 = points[1]

                else:
                    rx1, ry1= points[-1]
                    rx2, ry2 = points[-2]


                tlMidX1, tlMidY1 = findPointAtDistance(rx1, ry1, rx2, ry2, 18)
                tlMidX2, tlMidY2 = findPointAtDistance(rx1, ry1, rx2, ry2, 36)
                tlx1,tly1 = findPerpendicularPoint((tlMidX1, tlMidY1),( tlMidX2, tlMidY2),15)
                tlx2,tly2 = findPerpendicularPoint( ( tlMidX2, tlMidY2),(tlMidX1, tlMidY1), 15)

                x1,y1 = findMidPoint((tlx1,tly1), (tlx2,tly2))
                x2,y2 = tlx2,tly2

                pos1 = x1, y1  # mid point
                pos2 = x2, y2 # one edge
                pos3 = tlx1,tly1
                tlLine = (pos2, pos3)

                tl.pos = (pos1,pos2)

                drawTrafficLights(app, pos1, pos2, i,inter,pos3)

def drawTrafficLights(app,pos1,pos2,i,inter,pos3):
    x1, y1 = pos1  # mid point
    x2, y2 = pos2  # one edge

    edgeX1, edgeY1 = pos3  # another edge
    tlLine = (pos2, pos3)

    tlRoad = None
    for road in inter.roads:
        for j in range(len(road.points) - 1):
            rLine = (road.points[j], road.points[j + 1])
            if linesIntersect(tlLine, rLine):
                tlRoad = road


    drawCircle(x1,y1,4)
    drawCircle(x2,y2,4)
    drawLine(x1,y1,x2,y2,lineWidth = 8)
    redX, redY = findPointAtDistance(x1, y1, x2, y2, 15.5)
    drawCircle( redX, redY, 2.2, fill='darkRed')
    yellowX,yellowY = findPointAtDistance(x1,y1,x2,y2,10.5)
    drawCircle(yellowX,yellowY, 2.2, fill='darkKhaki')
    greenX, greenY = findPointAtDistance(x1, y1, x2, y2, 5)
    drawCircle(greenX, greenY, 2.2, fill='darkOliveGreen')

    #Left turn
    arrowX1, arrowY1 = findPointAtDistance(x1, y1, x2, y2, 2)
    (trash,trash), (arrowX2, arrowY2) = extendLine((x2,y2),(x1,y1) , 3)


    angle = math.atan2(arrowY1-arrowY2, arrowX1-arrowX2)
    lAngle = angle + math.radians(30)
    rAngle = angle - math.radians(30)

    leftX = arrowX2 + 5*math.cos(lAngle)
    leftY = arrowY2 + 5*math.sin(lAngle)
    rightX = arrowX2 + 5*math.cos(rAngle)
    rightY = arrowY2 + 5*math.sin(rAngle)

    drawLine(arrowX1, arrowY1, arrowX2, arrowY2, lineWidth=1.5, fill='darkOliveGreen')
    # Draw arrowhead
    drawLine(arrowX2, arrowY2, leftX, leftY, lineWidth=1.5, fill='darkOliveGreen')
    drawLine(arrowX2, arrowY2, rightX, rightY, lineWidth=1.5, fill='darkOliveGreen')


    if i == 0:
        tl = inter.trafficLights[0]
        tl.road = tlRoad
    elif i == 1:
        tl = inter.trafficLights[1]
        tl.road = tlRoad
    elif i == 2:
        tl = inter.trafficLights[0]
        tl.road = tlRoad
    else:
        tl = inter.trafficLights[1]
        tl.road = tlRoad
    status = tl.status
    tl.pos = (pos1,pos2)

    if status == 0:
        drawLine(arrowX1, arrowY1, arrowX2, arrowY2, lineWidth=1.5, fill='limeGreen')
        # Draw arrowhead
        drawLine(arrowX2, arrowY2, leftX, leftY, lineWidth=1.5, fill='limeGreen')
        drawLine(arrowX2, arrowY2, rightX, rightY, lineWidth=1.5, fill='limeGreen')
        drawCircle(redX, redY, 2.2, fill='red')

    elif status == 1:
        drawCircle(greenX, greenY, 2.2, fill='limeGreen')

    elif status == 2:
        drawCircle(yellowX, yellowY, 2.2, fill='yellow')

    elif status == 3:
        drawCircle(redX, redY, 2.2, fill='red')

def magneticCursor(app,mouseX,mouseY):
    for road in app.roads:
        if road.type == "Straight":
            startPoint, endPoint = road.points[0],road.points[1]
        else:
            startPoint, endPoint = road.points[0], road.points[2]
        startX, startY = startPoint
        endX, endY = endPoint
        if getDistance(mouseX,mouseY,startX,startY) < 50:
            app.cursorX, app.cursorY = startX,startY
            app.cursorUserControlled = False
            return
        elif getDistance(mouseX,mouseY,endX,endY) < 50:
            app.cursorX, app.cursorY = endX,endY
            app.cursorUserControlled = False
            return

        roadLines = getRoadLineParts(road)
        for line in roadLines:
            lx1, ly1 = line[0]
            lx2, ly2 = line[1]

            if distancePointToLine(mouseX, mouseY, lx1, ly1, lx2, ly2) <= 20:
                perps = find_perpendicular_point(line,(mouseX, mouseY) )
                if perps:
                    perpX,perpY = perps
                    trash,(app.cursorX, app.cursorY) = extendLine((mouseX, mouseY),(perpX,perpY),30)
                    app.cursorUserControlled = False
                    return
    app.cursorUserControlled = True

def trafficLightsToggle(app):
    for inter in app.intersections:
        for tl in inter.trafficLights:
            tl.update()