from practicalFunctions import *
from cmu_graphics import  *
from objects import *
import time
def drawPaths(app):
    for car in app.cars:
        points = []
        points.append(car.pos)
        for point in car.shiftedPath[car.currPointInd:]:
            points.append(point)
        if car.type == 1:
            carColor = 'gold'
        elif car.type == 2:
            carColor = 'blue'
        else:
            carColor = 'darkRed'
        for i in range(len(points)-1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            drawLine(x1, y1, x2, y2, fill=carColor,lineWidth=2)
def generateCars(app):
    for i in range(app.diffLevel):
        startRoad = app.roads[i]
        startRoadInd = i
        carInd = int(generateRadnBetween(0,3))
        endRoadInd = int(generateRadnBetween(0,app.diffLevel-1)+1)
        while endRoadInd == startRoadInd:
            endRoadInd = int(generateRadnBetween(0,app.diffLevel-1)+1)
        endRoad = app.roads[endRoadInd]


        paths = findUnpackedPaths(app,findPaths(app, startRoad, endRoad))
        path = sortPath(app,paths)[0]
        shiftVal = app.roadWidth / 3
        car = Car(carInd, app.roads[1], app.roads[0].points[1],path,-shiftVal)
        car.startTime = time.time()
        app.cars.append(car)


def drawCar(app):
    for car in app.cars:
        if not car.finished:
            collisionBox = getCollisionBox(app, car)
            x1,y1 = car.pos
            x2,y2 = car.currDestination
            angle = findAngleTwoPints(x1,y1,x2,y2)
            car.angle = angle
            if app.carRepr:
                drawImage(app.carImages[car.type], x1,y1,width = app.carImageWidth, height =app.carImageHeight,
                      align='center',rotateAngle = car.angle)
            else:
                if car.type == 1:
                    carColor = 'gold'
                elif car.type == 2:
                    carColor = 'blue'
                else:
                    carColor = 'darkRed'
                drawRect(x1,y1,app.carImageWidth, app.carImageHeight,
                      align='center',rotateAngle = car.angle,fill=carColor)

def getCollisionBox(app,car):
    carX,carY = car.pos
    upperMidX,upperY = carX,carY - app.collisionBoxHeight
    cornerX1,cornerY1 = upperMidX-app.collisionBoxWidth/2,carY
    cornerX2,cornerY2 = upperMidX+app.collisionBoxWidth/2,carY
    cornerX3,cornerY3 = upperMidX-app.collisionBoxWidth/2,upperY
    cornerX4,cornerY4 = upperMidX+app.collisionBoxWidth/2,upperY

    cX, cY = findPointAtDistance(cornerX1, cornerY1, cornerX2,cornerY2, app.collisionBoxWidth/2)

    rotatedCornerX1,rotatedCornerY1 = rotatePoint(cX, cY, cornerX1,cornerY1, car.angle)
    rotatedCornerX2, rotatedCornerY2 = rotatePoint(cX, cY, cornerX2,cornerY2, car.angle)
    rotatedCornerX3, rotatedCornerY3 = rotatePoint(cX, cY, cornerX3,cornerY3, car.angle)
    rotatedCornerX4, rotatedCornerY4 = rotatePoint(cX, cY, cornerX4,cornerY4, car.angle)

    return (rotatedCornerX1,rotatedCornerY1), (rotatedCornerX2, rotatedCornerY2),(rotatedCornerX3, rotatedCornerY3),(rotatedCornerX4, rotatedCornerY4)

def checkCollisionTL(app, car,tl):
    collisionBox = getCollisionBox(app, car)
    if collisionBox:
        p1, p2, p3, p4 = collisionBox
        x1,y1 = p1
        x2,y2 = p2
        x3,y3 = p3
        x4,y4 = p4
        (tlX1,tlY1),(tlX2,tlY2) = tl.pos
        (tlX,tlY) = findMidPoint((tlX1,tlY1),(tlX2,tlY2))
        if (min(x1, x2, x3, x4) <= tlX <= max(x1, x2, x3, x4) and
                min(y1, y2, y3, y4) <= tlY <= max(y1, y2, y3, y4)):

            return True
    return False

def getCollisionBoxCar(app,car):
    carX,carY = car.pos
    upperMidX,upperY = carX,carY - app.collisionBoxHeightCar
    cornerX1,cornerY1 = upperMidX-app.collisionBoxWidth/2,carY
    cornerX2,cornerY2 = upperMidX+app.collisionBoxWidth/2,carY
    cornerX3,cornerY3 = upperMidX-app.collisionBoxWidth/2,upperY
    cornerX4,cornerY4 = upperMidX+app.collisionBoxWidth/2,upperY

    cX, cY = findPointAtDistance(cornerX1, cornerY1, cornerX2,cornerY2, app.collisionBoxWidth/2)

    rotatedCornerX1,rotatedCornerY1 = rotatePoint(cX, cY, cornerX1,cornerY1, car.angle)
    rotatedCornerX2, rotatedCornerY2 = rotatePoint(cX, cY, cornerX2,cornerY2, car.angle)
    rotatedCornerX3, rotatedCornerY3 = rotatePoint(cX, cY, cornerX3,cornerY3, car.angle)
    rotatedCornerX4, rotatedCornerY4 = rotatePoint(cX, cY, cornerX4,cornerY4, car.angle)

    return (rotatedCornerX1,rotatedCornerY1), (rotatedCornerX2, rotatedCornerY2),(rotatedCornerX3, rotatedCornerY3),(rotatedCornerX4, rotatedCornerY4)
def checkCollisionCar(app, car):
    collisionBox = getCollisionBoxCar(app, car)
    if collisionBox:
        p1, p2, p3, p4 = collisionBox
        x1,y1 = p1
        x2,y2 = p2
        x3,y3 = p3
        x4,y4 = p4
        for otherCar in app.cars:
            if otherCar != car:
                carX,carY = car.pos
                otherCarX,otherCarY = otherCar.pos
                if (min(x1, x2, x3, x4) <= otherCarX <= max(x1, x2, x3, x4) and
                        min(y1, y2, y3, y4) <= otherCarY <= max(y1, y2, y3, y4)
                        and abs(car.angle-otherCar.angle)<60 and getDistance(otherCarX,otherCarY,carX,carY)>6):

                    return True
    return False

def updateCarMove(app):

    for car in app.cars:
        if car.currPointInd >= len(car.path)-1:
            car.endTime = time.time()
            car.finished = True
            ind = app.cars.index(car)
            app.cars.pop(ind)
            app.carNum += 1
            timeSpent = (pythonRound(car.startTime-car.endTime))
            app.timeSpent.append(timeSpent)
            if len(app.timeSpent) == 0:
                lengthAllTime = 1
            else:
                lengthAllTime = len(app.timeSpent)
            app.aveTime = abs(pythonRound(sum(app.timeSpent) / lengthAllTime,1))
        if not car.finished:
            car.currRoad = car.path[car.currPointInd][0]
            currTL = checkTrafficLightStatus(app,car)
            if ((currTL == 0 and car.nextMove == 'Left') or (currTL == 1 and car.nextMove == None) or
                    (currTL == 2 and car.nextMove == None) or (currTL == None) or (car.nextMove == 'Right')or
                    (currTL == None and car.nextMove == None)):
                currD = car.currDestination
                xCD,yCD = currD
                xC,yC = car.pos
                if getDistance(xC,yC, xCD, yCD) < car.speed:
                    car.currPointInd += 1
                    if car.currPointInd + 1 < len(car.shiftedPath):
                        car.currDestination = car.shiftedPath[car.currPointInd + 1]
                    else:
                        continue
                anyInterBetween = False
                # If there's no intersections between the current location and currDestination
                for inter in car.currRoad.intersections:

                    interX, interY = inter.points
                    dX, dY = car.currDestination
                    if ((min(xC, dX) < interX < max(xC, dX)) and (min(yC, dY) < interY < max(yC, dY))):
                        anyInterBetween = True
                        break
                    else:
                        anyInterBetween = False

                if (car.currPointInd + 2) < len(car.path):
                #If the car is going to change its road
                    if not anyInterBetween:
                        if car.path[car.currPointInd + 1][0] != car.path[car.currPointInd][0]:
                            curDX,curDY = car.path[car.currPointInd + 1][1]
                            nextDX,nextDY = car.path[car.currPointInd + 2][1]
                            curX,curY = car.pos

                            line1 = ((curDX,curDY),(curX,curY))
                            line2 = ((curDX,curDY),(nextDX,nextDY))

                            angle = angleBetweenTwoLine(line1, line2)

                            if abs(angle) < 100:
                                if angle < 0:
                                    car.nextMove = 'Right'
                                elif angle > 0:
                                    car.nextMove = 'Left'
                            else:
                                car.nextMove = None
                    else:
                        car.nextMove = None
                else:
                    car.nextMove = None

                if checkCollisionCar(app, car):
                    if car.speed!=0:
                        car.speed -= 1
                elif car.speed != 4:
                    car.speed += 1
                x2,y2 = findPointAtDistance(xC,yC, xCD, yCD, car.speed)

                car.updateLocation((x2,y2))
        app.carRoadCurvedUnpacked = True

def checkTrafficLightStatus(app,car):
    for inter in app.intersections:
        carX,carY = car.pos
        currDX,currDY = car.currDestination

        signtOnLight = findPointAtDistance(carX,carY, currDX,currDY, 15)
        sightX, sightY = car.pos
        interX,interY = inter.points

        for tl in inter.trafficLights:
            if tl.road == car.currRoad:
                tlX,tlY = tl.pos[0]
                if checkCollisionTL(app, car,tl) and getDistance(carX,carY,tlX,tlY) > 15:
                    return tl.status

############## CITATION #########################
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
    for inter in currRoad.intersections:
        for road in inter.roads:
            if road != currRoad:
                neighbors.append((road, inter.points))
    if currRoad.type == 'Straight':
        if pointsEqual(currPoint, currRoad.points[0]):
            neighbors.append((currRoad, currRoad.points[1]))
        else:
            neighbors.append((currRoad, currRoad.points[0]))

    elif currRoad.type == 'Curved':
        if pointsEqual(currPoint, currRoad.points[0]):
            neighbors.append((currRoad, currRoad.points[2]))
        elif pointsEqual(currPoint, currRoad.points[1]):
            neighbors.append((currRoad, currRoad.points[2]))
            neighbors.append((currRoad, currRoad.points[0]))
        else:
            neighbors.append((currRoad, currRoad.points[0]))
    return neighbors

def pointsEqual(p1, p2, tol=1):
    return abs(p1[0] - p2[0]) < tol and abs(p1[1] - p2[1]) < tol

############## END CITATION #####################
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
                i /= numSteps
                x = (1 - i)**2 * start[0] + 2 * (1 - i) * i * mid[0] + i ** 2 * end[0]
                y = (1 - i)**2 * start[1] + 2 * (1 - i) * i * mid[1] + i ** 2 * end[1]
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

def sortPath(app,paths):
    pathDistanceDict = dict()
    for i in range(len(paths)):
        path = paths[i]
        totalDistance = 0
        for j in range(len(path)-1):
            road1, point1 = path[j]
            road2, point2 = path[j+1]
            x1, y1 = point1
            x2, y2 = point2
            dist = getDistance(x1,y1,x2,y2)
            totalDistance += dist
        pathDistanceDict[i] = totalDistance
    pathDistanceDict = sortAmountCarsUsingPath(app, paths,pathDistanceDict)
    ret = []
    shortedPath = 0
    shortedPathLen = pathDistanceDict[shortedPath]
    for ind in pathDistanceDict:
        if pathDistanceDict[ind] > shortedPath:
            dist = pathDistanceDict[ind]
            if dist < shortedPathLen:
                ret.insert(0,paths[ind])
            else:
                ret.append(paths[ind])
    return ret

def sortAmountCarsUsingPath(app,paths,pathDistanceDict):
    for ind in pathDistanceDict:
        for car in app.cars:
            if car.path == paths[ind]:
                pathDistanceDict[ind] += 50
    return pathDistanceDict
