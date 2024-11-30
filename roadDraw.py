from cmu_graphics import  *
from cmu_cpcs_utils import prettyPrint
from PIL import *


from objects import *
from practicalFunctions import *
import math

##
#Car images: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fillustrations%2Fcar-top-view&psig=AOvVaw2X3GXjKWFy73DUyrCA1lRk&ust=1732922954816000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCKDF0JqXgIoDFQAAAAAdAAAAABAE
##

def onAppStart(app):
    app.roadPreview = False
    app.roadOpacity = 100
    app.width = 1000
    app.height = 600
    app.gridSize = 20
    app.roadWidth = 30
    app.laneMarkingInterval = 10
    app.gridSize = 20
    app.showGrid = True
    app.roadsCoordinates = []
    for i in range(0,app.height,4):
        row = []
        for j in range(0,app.width,4):
            row.append(0)
        app.roadsCoordinates.append(row)
    app.roads = []
    app.roads.append(Road('Straight',[(0,400),(150,400)],0))
    app.roads.append(Road('Straight', [(1000, 400), (700, 400)], 0))
    app.currentRoad = None


    app.modes = ['Straight','Curved']
    #default mode
    app.currentMode = 'Straight'
    app.isDrawing = False

    app.elevation = 0
    app.elevations = ['Ground', 'Bridge', 'Tunnel']
    app.currentElevation = 'Ground'

    # UI Elements positions
    app.buttonWidth = 100
    app.buttonHeight = 30
    app.buttonMargin = 10
    app.buttons = []
    createButtons(app)
    app.drawingState = None
    app.megTemp = None
    app.intersections = set()
    app.edgeIntersections = []
    app.stepsPerSecond = 20
    app.counter = 0
    app.roadsChanged = True
    app.paused = True
    app.initiated = False

    app.carURLs = [f'./cars/{i}.png' for i in range(0, 3)]
    app.carImages = [CMUImage(loadPilImage(url)) for url in app.carURLs]
    app.cars = []
    # app.carImages = []
    # for each in carImages:
    #     resized = each.resize((each.width // 14, each.height // 14))
    #     resized = CMUImage(resized)
    #     app.carImages.append(resized)
    app.carRoadCurvedUnpacked = False

    app.cursorX = 0
    app.cursorY = 0

    app.cursorUserControlled = True
    app.path = []

def createButtons(app):
    for i in range(len(app.modes)):
        x = app.buttonMargin + i*(app.buttonWidth + app.buttonMargin)
        y = app.buttonMargin
        button = Button('mode',app.modes[i], x, y)
        app.buttons.append(button)

    x = app.buttonMargin
    y = app.buttonMargin*2 + app.buttonHeight
    button = Button('grid',"Toggle Grid", x, y)
    startButton = Button('start', "Finished!",880,540)
    app.buttons.append(button)
    app.buttons.append(startButton)


def onMousePress(app,mouseX,mouseY):

    app.roadsChanged = True
    app.edgeIntersections = findEdgeIntersections(app)

    #if clcked again, then draw the road
    if app.isDrawing and app.currentMode != None:

        mappedX, mappedY = int(app.cursorX),int(app.cursorY)
        if app.currentMode == 'Straight':

            #if we already have an end points

            if len(app.currentRoad.points) == 2:
                app.roads.append(app.currentRoad)
            if app.megTemp != None:
                ind = app.megTemp[0]
                if app.megTemp[2] == 'end':
                    if app.roads[ind].type == 'Straight':
                        inter = Intersection(app.roads[ind].points[1],app.roads[ind].elevation,'3-way',
                                             (app.currentRoad,app.roads[ind]))
                        app.roads[ind].changeEndStatus(2)

                        app.intersections.add(inter)
                        app.roads[ind].addIntersection(inter)
                        app.currentRoad.addIntersection(inter)

                    if app.roads[ind].type == 'Curved':
                        inter = Intersection(app.roads[ind].points[2],app.roads[ind].elevation,'3-way',
                                             (app.currentRoad,app.roads[ind]))
                        app.intersections.add(inter)
                        app.roads[ind].addIntersection(inter)
                        app.currentRoad.addIntersection(inter)
                        app.roads[ind].changeEndStatus(2)
                else:
                    if app.roads[ind].type == 'Straight':
                        inter = Intersection(app.roads[ind].points[0],app.roads[ind].elevation,'3-way',
                                             (app.currentRoad,app.roads[ind]))
                        app.roads[ind].changeEndStatus(1)

                        app.intersections.add(inter)
                        app.roads[ind].addIntersection(inter)
                        app.currentRoad.addIntersection(inter)

                    if app.roads[ind].type == 'Curved':
                        inter = Intersection(app.roads[ind].points[0],app.roads[ind].elevation,'3-way',
                                             (app.currentRoad,app.roads[ind]))
                        app.intersections.add(inter)
                        app.roads[ind].addIntersection(inter)
                        app.currentRoad.addIntersection(inter)
                        app.roads[ind].changeEndStatus(1)


            app.megTemp = None
                #reset
            app.currentRoad = None
            app.isDrawing = False
            return

        elif app.currentMode == 'Curved':

            #if this is the third click
            if app.drawingState == 'end':
                app.roads.append(app.currentRoad)
                app.currentRoad = None
                app.isDrawing = False
                app.drawingState = None
                return
            if app.drawingState == 'p2':
                app.currentRoad.points.append((mappedX, mappedY))
                #the next click will be the end poiny
                app.drawingState = 'end'

                if app.megTemp != None:
                    ind = app.megTemp[0]
                    if app.megTemp[2] == 'end':
                        if app.roads[ind].type == 'Straight':
                            inter = Intersection(app.roads[ind].points[1], app.roads[ind].elevation, '3-way',
                                                 (app.currentRoad, app.roads[ind]))
                            app.intersections.add(inter)
                            app.roads[ind].addIntersection(inter)
                            app.currentRoad.addIntersection(inter)
                            app.roads[ind].changeEndStatus(2)
                        if app.roads[ind].type == 'Curved':
                            inter = Intersection(app.roads[ind].points[2], app.roads[ind].elevation, '3-way',
                                                 (app.currentRoad, app.roads[ind]))
                            app.intersections.add(inter)
                            app.roads[ind].addIntersection(inter)
                            app.currentRoad.addIntersection(inter)
                            app.roads[ind].changeEndStatus(2)
                    else:
                        if app.roads[ind].type == 'Straight':
                            inter = Intersection(app.roads[ind].points[0], app.roads[ind].elevation, '3-way',
                                                 (app.currentRoad, app.roads[ind]))
                            app.intersections.add(inter)
                            app.roads[ind].addIntersection(inter)
                            app.currentRoad.addIntersection(inter)
                            app.roads[ind].changeEndStatus(1)
                        if app.roads[ind].type == 'Curved':
                            inter = Intersection(app.roads[ind].points[0], app.roads[ind].elevation, '3-way',
                                                 (app.currentRoad, app.roads[ind]))
                            app.intersections.add(inter)
                            app.roads[ind].addIntersection(inter)
                            app.currentRoad.addIntersection(inter)
                            app.roads[ind].changeEndStatus(1)
                app.megTemp = None

    # check which button is pressed
    for each in app.buttons:
        if (each.x <= mouseX <= each.x+app.buttonWidth and
            each.y <= mouseY <= each.y+app.buttonHeight):
            if each.type == 'mode':
                app.currentMode = each.label
            elif each.type == 'grid':
                app.showGrid = not app.showGrid
            elif each.type == 'start':
                app.paused = not app.paused
                if not app.initiated:
                    generateCars(app)
                    app.path = findUnpackedPaths(app,findPaths(app, app.roads[0], app.roads[1]))
                app.initiated = True
            return

    #map to the closet 20*20 coordinate
    mappedX, mappedY = int(app.cursorX),int(app.cursorY)

    if app.currentMode == 'Straight':

        app.currentRoad = Road("Straight",[(mappedX, mappedY)], 0)
        app.isDrawing = True

    elif app.currentMode == 'Curved':
        #check is this is the first click
        if not app.isDrawing:
            app.currentRoad = Road('Curved',[(mappedX, mappedY)], 0)
            app.isDrawing = True
            #the next point will be the middle point between start and end point
            app.drawingState = 'p2'





def onMouseMove(app, mouseX,mouseY):
    magneticCursor(app,mouseX,mouseY)
    if app.cursorUserControlled:
        app.cursorX, app.cursorY = mouseX, mouseY

    if app.isDrawing and app.currentMode != None:
        app.roadsChanged = True
        mappedX, mappedY = app.cursorX,app.cursorY
        if app.currentMode == 'Straight':
            #Check if we have an end point
            if len(app.currentRoad.points) == 1:
                app.currentRoad.points.append((mappedX, mappedY))
            else:
                app.currentRoad.points[1] = (mappedX, mappedY)
                result = checkCrossingOutlets(app, app.currentRoad)
                if result:

                    side, (interX, interY), ind = result
                    if app.roads[ind].type == 'Straight':
                        if app.megTemp == None:
                            if side == 'end':
                                app.megTemp = [ind, app.roads[ind].points[1], 'end']
                            else:
                                app.megTemp = [ind, app.roads[ind].points[0], 'start']


                        if side == 'end':
                            app.roads[ind].points[1] = (interX, interY)
                        else:
                            app.roads[ind].points[0] = (interX, interY)
                    elif app.roads[ind].type == 'Curved':
                        if app.megTemp == None:
                            if side == 'end':
                                app.megTemp = [ind, app.roads[ind].points[2], 'end']
                            else:
                                app.megTemp = [ind, app.roads[ind].points[0], 'start']

                        if side == 'end':
                            app.roads[ind].points[2] = (interX, interY)
                        else:
                            app.roads[ind].points[0] = (interX, interY)

                else:
                    if app.megTemp:
                        ind = app.megTemp[0]
                        if app.roads[ind].type == 'Straight':
                            if app.megTemp[2] == 'end':
                                app.roads[ind].points[1] = app.megTemp[1]
                            else:
                                app.roads[ind].points[0] = app.megTemp[1]
                            app.megTemp = None
                        elif app.roads[ind].type == 'Curved':
                            if app.megTemp[2] == 'end':
                                app.roads[ind].points[2] = app.megTemp[1]
                            else:
                                app.roads[ind].points[0] = app.megTemp[1]
                            app.megTemp = None


        # if this is the third points
        elif app.currentMode == 'Curved' and app.drawingState == 'p2':
            #immediately add a second point
            if len(app.currentRoad.points) == 1:
                app.currentRoad.points.append((mappedX, mappedY))
            else:
                app.currentRoad.points[1] = (mappedX, mappedY)
        #if this is the third points
        elif app.currentMode == 'Curved' and app.drawingState == 'end':
            if len(app.currentRoad.points) == 2:
                app.currentRoad.points.append((mappedX, mappedY))
            else:
                app.currentRoad.points[2] = (mappedX, mappedY)
                result = checkCrossingOutlets(app, app.currentRoad)
                if result:

                    side, (interX, interY), ind = result
                    if app.roads[ind].type == 'Straight':
                        if app.megTemp == None:
                            if side == 'end':
                                app.megTemp = [ind, app.roads[ind].points[1], 'end']
                            else:
                                app.megTemp = [ind, app.roads[ind].points[0], 'start']

                        if side == 'end':
                            app.roads[ind].points[1] = (interX, interY)
                        else:
                            app.roads[ind].points[0] = (interX, interY)
                    elif app.roads[ind].type == 'Curved':
                        if app.megTemp == None:
                            if side == 'end':
                                app.megTemp = [ind, app.roads[ind].points[2], 'end']
                            else:
                                app.megTemp = [ind, app.roads[ind].points[0], 'start']

                        if side == 'end':
                            app.roads[ind].points[2] = (interX, interY)
                        else:
                            app.roads[ind].points[0] = (interX, interY)

                else:
                    if app.megTemp:
                        ind = app.megTemp[0]
                        if app.roads[ind].type == 'Straight':
                            if app.megTemp[2] == 'end':
                                app.roads[ind].points[1] = app.megTemp[1]
                            else:
                                app.roads[ind].points[0] = app.megTemp[1]
                            app.megTemp = None
                        elif app.roads[ind].type == 'Curved':
                            if app.megTemp[2] == 'end':
                                app.roads[ind].points[2] = app.megTemp[1]
                            else:
                                app.roads[ind].points[0] = app.megTemp[1]
                            app.megTemp = None


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
    app.cursorUserControlled = True

def redrawAll(app):

    drawRect(0, 0, app.width, app.height, fill='lightGreen')


    if app.showGrid:
        drawGrid(app)

    drawButtons(app)

    for each in app.roads:
        drawRoad(app, each)

    if app.isDrawing and app.currentRoad != None:
        drawRoad(app, app.currentRoad)

    drawIntersectMarking(app)
    drawCar(app)

    drawCircle(app.cursorX, app.cursorY, 10, fill='darkSlateGray')

    points = []
    for path in app.path:
        for i in range(len(path) - 1):
            points.append((path[i][1], path[i + 1][1]))
        for each in points:
            x1, y1 = each[0]
            x2, y2 = each[1]
            drawLine(x1, y1, x2, y2)
def onStep(app):
    if not app.paused:
        app.counter += 1
        trafficLightsToggle(app)
        updateCarMove(app,4)
    if app.roadsChanged:
        findIntersections(app)
        app.edgeIntersections = findEdgeIntersections(app)
        app.roadsChanged = False

def generateCars(app):
    path = findUnpackedPaths(app,findPaths(app, app.roads[0], app.roads[1]))[0]
    shiftVal = app.roadWidth / 4
    app.cars.append(Car(1, app.roads[1], app.roads[0].points[1],path,-shiftVal))


def drawCar(app):
    for car in app.cars:
        x1,y1 = car.pos
        x2,y2 = car.currDestination
        angle = findAngleTwoPints(x1,y1,x2,y2)
        car.angle = angle
        imageWidth,imageHeight = getImageSize(app.carImages[car.type])
        drawImage(app.carImages[car.type], x1,y1,width = imageWidth//14, height = imageHeight//14, align='center',rotateAngle = car.angle)


def updateCarMove(app, speed):

    for car in app.cars:
        car.currRoad = car.path[car.currPointInd][0]

        # for road,point in car.path:

        # if not app.carRoadCurvedUnpacked:
        #     if car.currRoad.type == 'Curved':
        #         start, mid, end = car.currRoadPoints
        #         numSteps = 10
        #         points = []
        #         for i in range(numSteps + 1):
        #             i = i / numSteps
        #             x = (1 - i) ** 2 * start[0] + 2 * (1 - i) * i * mid[0] + i ** 2 * end[0]
        #             y = (1 - i) ** 2 * start[1] + 2 * (1 - i) * i * mid[1] + i ** 2 * end[1]
        #             points.append((x, y))
        #         car.currRoadPoints = points
        #         car.currDestination = car.currRoadPoints[1]
        currTL = checkTrafficLightStatus(app,car)
        if currTL == 0 or currTL == 1 or currTL == 2 or currTL == None:
            currD = car.currDestination
            xCD,yCD = currD
            xC,yC = car.pos
            if getDistance(xC,yC, xCD, yCD) < speed:
                car.currPointInd += 1
                if car.currPointInd + 1 < len(car.shiftedPath):
                    car.currDestination = car.shiftedPath[car.currPointInd + 1]
                else:
                    continue
            x2,y2 = findPointAtDistance(xC,yC, xCD, yCD, speed)
            car.updateLocation((x2,y2))
    app.carRoadCurvedUnpacked = True

def checkTrafficLightStatus(app,car):
    for inter in car.currRoad.intersections:
        carX,carY = car.pos
        currDX,currDY = car.currDestination

        signtOnLight = findPointAtDistance(carX,carY, currDX,currDY, 25)
        sightX, sightY = car.pos
        interX,interY = inter.points


        if getDistance(sightX,sightY,interX,interY) < 15:
            for tl in inter.trafficLights:
                if tl.road == car.currRoad:
                    return tl.status

def trafficLightsToggle(app):
    for inter in app.intersections:
        for tl in inter.trafficLights:
            tl.update()


def drawGrid(app):
    for i in range(0, app.width, app.gridSize):
        drawLine(i, 0, i, app.height, fill='lightGray')
    for i in range(0, app.width, app.gridSize):
        drawLine(0, i, app.width, i, fill='lightGray')

def drawButtons(app):
    for each in app.buttons:
        if (each.type == 'mode' and app.currentMode == each.label or
            each.type == 'grid' and not app.showGrid or
            each.type == 'start' and not app.paused) :
            color = 'lightBlue'
        else:
            color = 'white'
        drawRect(each.x,each.y,app.buttonWidth,app.buttonHeight,fill=color,border = 'black')
        drawLabel(each.label,each.x + app.buttonWidth/2,each.y+app.buttonHeight/2,size = 12)

def mapToCoordinates(app,x,y):
    return rounded(x / app.gridSize) * app.gridSize, rounded(y / app.gridSize) * app.gridSize

def drawRoad(app,road):
    roadType = road.type
    points = road.points
    elevation = road.elevation
    if roadType == 'Straight':
        #chekc if drawing is finished
        if len(points) >= 2:
            drawStraightRoad(app,points[0], points[1], elevation)

    if roadType == 'Curved':
        if len(points) == 3:
            drawCurvedRoad(app,points[0], points[1], points[2], elevation)

            return
        elif len(points) == 2:
            drawCurvedRoad(app,points[0], points[1], points[1], elevation)


def drawStraightRoad(app,start,end,elevation):
    x1,y1 = start
    x2,y2 = end
    color = getElevationColor(elevation)

    drawLine(x1,y1,x2,y2,fill = color,lineWidth = app.roadWidth, opacity = app.roadOpacity)
    drawLaneMarking(app,[start,end])

    drawCircle(x1,y1, app.roadWidth/2, fill=color,  opacity = app.roadOpacity)
    drawCircle(x2,y2, app.roadWidth/2, fill=color,  opacity = app.roadOpacity)

def drawCurvedRoad(app, start, mid, end, elevation):
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

    color = getElevationColor(elevation)
    for i in range(len(points)-1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        drawLine(x1, y1, x2, y2, fill=color, lineWidth=app.roadWidth, opacity=app.roadOpacity)

    #draw circles to make the curve smooth
    for x,y in points:
        drawCircle(x, y, app.roadWidth / 2, fill=color, opacity=app.roadOpacity)

    drawLaneMarking(app, points)


    drawCircle(start[0], start[1], app.roadWidth / 2, fill=color, opacity=app.roadOpacity)
    drawCircle(end[0],end[1], app.roadWidth / 2, fill=color, opacity=app.roadOpacity)

# Draw dashed lane markings and intersections on the road
def drawLaneMarking(app,points):
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

        for i in range(0,len(dashPos)-1,2):
            drawLine(dashPos[i][0],dashPos[i][1],
                     dashPos[i+1][0],dashPos[i+1][1], fill='white', lineWidth=2)


def getElevationColor(elevation):
    if elevation == '0':
        return 'gray'
    elif elevation >= 1:
        return 'dimGray'
    elif elevation < 0:
        return 'darkSlateGray'
    else:
        return 'gray'

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
            i = i / numSteps
            x = (1 - i)**2*start[0] + 2*(1 - i)*i*mid[0] + i**2*end[0]
            y = (1 - i)**2*start[1] + 2*(1 - i)*i*mid[1] + i**2*end[1]
            points.append((x, y))

        for i in range(len(points)-1):
            lines.append((points[i], points[i + 1]))
    return lines



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

def findIntersections(app):
    intersections = set()
    for i in range(len(app.roads)):
        road1 = app.roads[i]
        line1 = getRoadLineParts(road1)
        for j in range(i + 1, len(app.roads)):
            road2 = app.roads[j]
            line2 = getRoadLineParts(road2)
            for l1 in line1:
                for l2 in line2:
                    point = linesIntersect(l1, l2)
                    if point and road1.elevation == road2.elevation:
                        inter = Intersection(point, road1.elevation, '4-way', (road1, road2))
                        road2.addIntersection(inter)
                        road1.addIntersection(inter)
                        app.intersections.add(inter)

    for i in range(len(app.roads)):
        road1 = app.roads[i]
        if road1.type == 'Straight':
            r1Start = road1.points[0]
            r1End = road1.points[1]
        elif road1.type == 'Curved':
            r1Start = road1.points[0]
            r1End = road1.points[2]

        for j in range(i + 1, len(app.roads)):
            road2 = app.roads[j]
            if road1 == road2:
                continue
            if road2.type == 'Straight':
                r2Start = road2.points[0]
                r2End = road2.points[1]
            elif road2.type == 'Curved':
                r2Start = road2.points[0]
                r2End = road2.points[2]

            if road1.elevation == road2.elevation:
                if r1Start == r2Start:
                    inter = Intersection(r1Start, road1.elevation, '2-way', (road1, road2))
                    road2.addIntersection(inter)
                    road1.addIntersection(inter)
                    app.intersections.add(inter)
                elif r1End == r2Start:
                    inter = Intersection(r2Start, road1.elevation, '2-way', (road1, road2))
                    road2.addIntersection(inter)
                    road1.addIntersection(inter)
                    app.intersections.add(inter)
                elif r1Start == r2End:
                    inter = Intersection(r1Start, road1.elevation, '2-way', (road1, road2))
                    road2.addIntersection(inter)
                    road1.addIntersection(inter)
                    app.intersections.add(inter)
                elif r1End == r2End:
                    inter = Intersection(r1End, road1.elevation, '2-way', (road1, road2))
                    road2.addIntersection(inter)
                    road1.addIntersection(inter)
                    app.intersections.add(inter)
    return intersections





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

        road.leftEdgeLines[-1] = extendLine(road.leftEdgeLines[-1][0], road.leftEdgeLines[-1][1], 1)

        road.rightEdgeLines[-1] = extendLine(road.rightEdgeLines[-1][0], road.rightEdgeLines[-1][1], 1)


        road.leftEdgeLines[0] = extendLine(road.leftEdgeLines[-1][1], road.leftEdgeLines[-1][0], 1)

        road.rightEdgeLines[0] = extendLine(road.rightEdgeLines[-1][1], road.rightEdgeLines[-1][0], 1)

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


def drawIntersectMarking(app):
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

            for i in range(len(sorted)-1):
                x1, y1 = sorted[i]
                x2, y2 = sorted[i+1]


                midx, midy = findMidPoint((x1, y1), (x2, y2))

                drawTrafficLights(app, (midx, midy), (x1, y1), i,inter,(x2,y2))
            x1, y1 = sorted[-1]
            x2, y2 = sorted[0]
            midx, midy = findMidPoint((x1, y1), (x2, y2))

            # if inter.type == "3-way":
            #     print('3-way')
            #     for road in inter.roads:
            #
            #         if road.type == 'Straight':
            #             if road.endStatus == 1:
            #
            #
            #                 old,(rx,ry) = extendLine(road.points[1],road.points[0], 15)
            #                 print(rx, ry )
            #                 print(midx,midy)
            #                 print(getDistance(midx, midy, rx, ry))
            #                 if getDistance(midx, midy, rx, ry) > 4:
            #
            #                     drawTrafficLights(app, (midx, midy), (x1, y1), 3,inter)
            #             elif road.endStatus == 2:
            #                 old, (rx, ry) = extendLine(road.points[0], road.points[1], 15)
            #                 print(rx, ry)
            #                 print(midx, midy)
            #                 print(getDistance(midx, midy, rx, ry))
            #                 if getDistance(midx, midy, rx, ry) > 4:
            #                     drawTrafficLights(app, (midx, midy), (x1, y1), 3, inter)
            drawTrafficLights(app, (midx, midy), (x1, y1), 3, inter,(x2,y2))




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

##############CITATION###########################
#################################################
#The code below is adapted from ChatGPT,
# some changes/adjustment has been made
#The feature of "excluding nodes" is NOT
#from ChatGPT
#THIS IS THE BEGINNING OF CITED CODE
#################################################
#################################################


def findPath(app, startRoad, endRoad, excluded=None):
    pointIDMap = {}
    pointCounter = [0]

    def getPointID(point):
        roundedPoint = (rounded(point[0]), rounded(point[1]))
        if roundedPoint not in pointIDMap:
            pointIDMap[roundedPoint] = pointCounter[0]
            pointCounter[0] += 1
        return pointIDMap[roundedPoint]

    if excluded == None:
        excluded = set()

    startPoint = startRoad.points[0]
    endPoint = endRoad.points[0]
    startNode = (startRoad, startPoint)
    endNode = (endRoad, endPoint)

    queue = [(startNode, [startNode])]
    visitedNodes = set()
    visitedNodes.add((startRoad, getPointID(startPoint)))

    while queue:
        (currRoad, currPoint), path = queue.pop(0)
        if currRoad == endRoad and pointsEqual(currPoint, endPoint):
            return path

        for nRoad, nPoint in getNeighbors(currRoad, currPoint):
            nPointID = getPointID(nPoint)
            node = (nRoad, nPoint)
            if (nRoad, nPointID) not in visitedNodes and node not in excluded:
                visitedNodes.add((nRoad, nPointID))
                queue.append((node, path + [node]))

    return None

def getNeighbors(currRoad, currPoint):
    neighbors = []
    # Add adjacent roads via intersections
    for inter in currRoad.intersections:
        for road in inter.roads:
            if road != currRoad:
                neighbors.append((road, inter.points))
    # Add the other end of the current road
    if currRoad.type == 'Straight':
        if pointsEqual(currPoint, currRoad.points[0]):
            neighbors.append((currRoad, currRoad.points[1]))
        else:
            neighbors.append((currRoad, currRoad.points[0]))
    elif currRoad.type == 'Curved':
        if pointsEqual(currPoint, currRoad.points[0]):
            neighbors.append((currRoad, currRoad.points[2]))
        else:
            neighbors.append((currRoad, currRoad.points[0]))
    return neighbors

def pointsEqual(p1, p2, tol=1):
    return abs(p1[0] - p2[0]) < tol and abs(p1[1] - p2[1]) < tol

##############END CITATION#######################
#################################################
#THIS IS THE END OF CITED CODE
#################################################
#################################################

def findPaths(app, startRoad, endRoad, maxNum=3):
    paths = []

    shortestPath = findPath(app, startRoad, endRoad)
    if shortestPath == None:
        return paths

    paths.append(shortestPath)

    for i in range(1, len(shortestPath) - 1):
        tempExcluded = set()
        tempExcluded.add(shortestPath[i])
        path = findPath(app, startRoad, endRoad, tempExcluded)
        if path != None and path not in paths:
            paths.append(path)
            if len(paths) >= maxNum:
                return paths

    return paths

def unPackPath(app, path):
    unpacked = []
    ind = 0
    while ind<(len(path) - 1):
        road1, point1 = path[ind]
        road2, point2 = path[ind+1]
        if road1.type == 'Curved':
            start, mid, end = road1.points
            numSteps = 10
            points = []
            for i in range(numSteps + 1):
                i = i / numSteps
                x = (1 - i) ** 2 * start[0] + 2 * (1 - i) * i * mid[0] + i ** 2 * end[0]
                y = (1 - i) ** 2 * start[1] + 2 * (1 - i) * i * mid[1] + i ** 2 * end[1]
                points.append((x, y))

            PointIndEnter= findClosestPoint(point1, points)
            PointIndExit= findClosestPoint(point2, points)
            if PointIndEnter <= PointIndExit:
                curvedPath=points[PointIndEnter:PointIndExit + 1]
            else:

                curvedPath=reversed(points[PointIndExit:PointIndEnter + 1])

            for cP in curvedPath:
                unpacked.append((road1, cP))
            ind += 1
        else:
            unpacked.append(path[ind])
            ind += 1

    if ind < len(path):
        unpacked.append(path[ind])
    return unpacked


def findUnpackedPaths(app,paths):
    ret = []
    for path in paths:
        path = unPackPath(app,path)
        ret.append(path)
    return ret


def main():
    runApp()

main()