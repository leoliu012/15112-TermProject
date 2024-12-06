#####################################################
## Author: Xinrui (Leo) Liu
## CMU 2024 15-112 Term Project
## Section: K
#####################################################

from practicalFunctions import *
class Road:
    def __init__(self,type,points,elevation,beginning = False):
        self.type = type
        self.points = points
        self.elevation = elevation
        self.intersections = set()
        self.leftEdgeLines = []
        self.rightEdgeLines = []
        self.endStatus = 0 #1:start at 3-way inter, 2:end at 3-way inter
        self.trafficLights = []
        self.laneMarkings = []
        self.beginning = beginning
        self.highlighted = False

    def __repr__(self):
        return f'Road("{self.type}", {self.points}, "{self.elevation}")'


    def addIntersection(self,intersection):
        self.intersections.add(intersection)

    def changeEndStatus(self,status):
        self.endStatus = status


class TrafficLight:
    def __init__(self,intersection,status,duration = 30,road=None):
        self.intersection = intersection
        self.status = status
        self.yellowDuration = 15 #2
        self.greenDuration = duration #0 and 1
        self.redDuration = self.greenDuration*2+15 #3
        self.counter = 0
        self.road = None
        self.pos = ((0, 0), (0, 0))
        self.firstTimeEntered = True
        self.road = road
        self.pos3=None

    def changeStatus(self,status):
        self.status = status

    def update(self):
        self.counter += 1
        if self.status == 2:
            duration = self.yellowDuration
        elif self.status == 1:
            duration = self.greenDuration
        elif self.status == 0:
            duration = self.greenDuration
        elif self.status == 3:
            duration = self.redDuration
        else:
            print('ER')
        if self.counter % duration == 0:

            self.status = (self.status + 1) % 4
            self.counter = 0

    def __repr__(self):
        return str(self.pos)
class Intersection:
    def __init__(self,points,elevation,type,roads,duration=30):
        self.points = points
        self.elevation = elevation
        self.type = type
        self.roads = roads
        self.trafficLights = []
        if not self.type.isdigit():
            tl1  = TrafficLight(self,0,duration=duration)
            tl2  = TrafficLight(self, 3,duration=duration)
            self.trafficLights.append(tl1)
            self.trafficLights.append(tl2)

        self.TLInitialized = False

    def __repr__(self):
        return str(self.points) +' '+ str(self.elevation)+' '+ str(self.type)+' '+ str(self.roads)



class Button:
    def __init__(self, type, label, x, y, width=200, height=50):
        self.type = type
        self.label = label
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class Car:
    def __init__(self,type, originRoad,destination,path, shiftVal):
        self.pathUsing = 0
        self.path = path
        self.type = type
        self.currPointInd = 0
        self.shiftVal = shiftVal
        self.shiftedPath = self.findShiftedPath()
        self.currRoadPoints = originRoad.points
        self.origin = self.shiftedPath[0]
        self.currDestination = self.shiftedPath[1]
        self.finalDestination = destination
        self.pos = self.origin
        self.currRoad = originRoad
        self.passedInterWith = set()
        self.nextMove = None

        x2, y2 = self.currDestination
        x1,y1 = self.origin
        angle = findAngleTwoPints(x1, y1, x2, y2)
        self.angle = angle
        self.speed = 4
        self.startTime = None
        self.endTime = None
        self.finished = False

    def updateLocation(self,pos):
        self.pos = pos

    def findShiftedPath(self):
        shiftedPath = []
        for i in range(len(self.path)-1):
            currRoad,currPoint = self.path[i]
            nextRoad,nextPoint = self.path[i+1]
            x1,y1 = currPoint
            x2,y2 = nextPoint

            length = getDistance(x1,y1,x2,y2)
            if length == 0:
                continue
            dx = x2 - x1
            dy = y2 - y1

            perpX = -dy
            perpY = dx

            # unit vector
            perpX /= length
            perpY /= length

            sx1 = x1 - perpX*self.shiftVal
            sy1 = y1 - perpY*self.shiftVal
            sx2 = x2 - perpX*self.shiftVal
            sy2 = y2 - perpY*self.shiftVal

            shiftedPath.append((sx1, sy1))
            if i == len(self.path) - 2:
                shiftedPath.append((sx2, sy2))

        return shiftedPath

class Player:
    def __init__(self,name,diffLevel):
        self.name = name
        self.diffLevel = diffLevel