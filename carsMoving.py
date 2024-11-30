from PIL import Image
from cmu_graphics import  *
from objects import Button, Road, Intersection, TrafficLight,Car
from practicalFunctions import *
import math




def onAppStart(app):
    app.carURLs = [f'./cars/{i}.png' for i in range(0,3)]
    app.carImages = [CMUImage(loadPilImage(url)) for url in app.carURLs]
    print(app.carURLs)
    app.roads = [Road('Straight',[(900,800),(200,0)],0)]
    app.cars = [Car(1, app.roads[0],(800,800))]
    app.width = 1000
    app.height = 600

def redrawAll(app):
    drawCar(app)

def drawCar(app):
    for car in app.cars:
        x1,y1 = car.pos
        x2,y2 = car.currDestination
        angle = findAngleTwoPints(x1,y1,x2,y2)
        car.angle = angle
        print(angle)
        drawImage(app.carImages[car.type], x1,y1, align='center',rotateAngle = car.angle)

def onStep(app):
    for car in app.cars:
        currD = car.currDestination
        xCD,yCD = currD
        xC,yC = car.pos
        if getDistance(xC,yC, xCD, yCD) < 2:
            car.currRoadPoint += 1
            car.currDestination = car.currRoad.points[car.currRoadPoint+1]
        x2,y2 = findPointAtDistance(xC,yC, xCD, yCD, 2)
        car.updateLocation((x2,y2))



def main():
    runApp()


main()
