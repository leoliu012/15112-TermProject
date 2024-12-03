from cmu_graphics import  *
from cmu_cpcs_utils import prettyPrint
from PIL import *

import time
from objects import *
from practicalFunctions import *
import math
import random

##
#Car images: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fillustrations%2Fcar-top-view&psig=AOvVaw2X3GXjKWFy73DUyrCA1lRk&ust=1732922954816000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCKDF0JqXgIoDFQAAAAAdAAAAABAE
#Bulldoze sign: https://www.google.com/url?sa=i&url=https%3A%2F%2Fdepositphotos.com%2Fvector%2Fbulldozer-danger-sign-or-symbol-text-do-not-enter-work-area-137213888.html&psig=AOvVaw12XVTRP41F261VeAQafj0D&ust=1733115705195000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCLiCwqTlhYoDFQAAAAAdAAAAABAJ
#"TimeWise Transport" Title generated at: "https://www.textstudio.com/"
#"ARE YOUR READY" Title generated at: "https://www.textstudio.com/"
#"Difficulty Level" Title generated at: "https://www.textstudio.com/"
#"Username" Title generated at: "https://www.textstudio.com/"
#"Settings" Button: https://www.google.com/url?sa=i&url=https%3A%2F%2Fdepositphotos.com%2Fphoto%2Fsettings-button-41886883.html&psig=AOvVaw0cnc_XdL26flFumwKCCoC-&ust=1733259661859000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIja09H9iYoDFQAAAAAdAAAAABAE
#Button background: https://www.google.com/url?sa=i&url=https%3A%2F%2Fpngtree.com%2Fso%2F2d-game-button&psig=AOvVaw11TPQ7pAeBcv6ewxS0LY9I&ust=1733191210619000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOjUyMX-h4oDFQAAAAAdAAAAABAJ
##

def onAppStart(app):
    app.width = 1000
    app.height = 600
    app.username = ''
    app.diffLevel = 4
    # app.soundBack = Sound('backMusi.mp3')
    # app.soundBack.play()


def intro_onAppStart(app):
    introURL = './backgrounds/intro.jpg'
    app.introImage = CMUImage(loadPilImage(introURL))

    buttonURL = './button/button1.png'
    app.buttonImage = CMUImage(loadPilImage(buttonURL))

    titleURL = './title/title.png'
    app.titleImage = CMUImage(loadPilImage(titleURL))


    app.introButtons = []
    buttonLabels = ["Instructions", 'Settings','History',"Quit"]
    app.buttonWidth = 150
    app.buttonHeight = 50
    app.titleY = 150

    for i in range(len(buttonLabels)):
        label = buttonLabels[i]
        x = 160 + i*(app.buttonWidth + 20)
        y = 325
        button = Button('intro', label, x, y, app.buttonWidth, app.buttonHeight)
        app.introButtons.append(button)
    app.currOnButton = None
    app.startButton = Button('intro', 'Start!', 400, 435, 200, 75)

    app.initiated = False
    app.introCounter = 0

def intro_redrawAll(app):
    drawImage(app.introImage,0, 0, width = app.width, height = app.height)
    titleWidth, titleHeight = getImageSize(app.titleImage)
    drawImage(app.titleImage, app.width / 2, app.titleY,align='center',width=titleWidth/1.2,height=titleHeight/1.2)

    for button in app.introButtons:
        if app.currOnButton == button:
            buttonY = button.y - 5
        else:
            buttonY = button.y

        drawImage(app.buttonImage,button.x, buttonY, width = button.width, height = button.height)

        drawLabel(button.label, button.x + button.width / 2, buttonY + button.height / 2, size=16,bold=True)

    if app.currOnButton == app.startButton:
        stbuttonY = app.startButton.y - 5
    else:
        stbuttonY = app.startButton.y

    drawImage(app.buttonImage,  app.startButton.x, stbuttonY, width= app.startButton.width, height= app.startButton.height)
    drawLabel(app.startButton.label,  app.startButton.x +  app.startButton.width/2, stbuttonY +  app.startButton.height/2, size=20, bold=True)

def intro_onMouseMove(app, mouseX, mouseY):
    currOnButton = None
    for button in app.introButtons:
        if (button.x <= mouseX <= button.x + button.width and
            button.y <= mouseY <= button.y + button.height):
            currOnButton = button
            break
    if (app.startButton.x <= mouseX <= app.startButton.x + app.startButton.width and
            app.startButton.y <= mouseY <= app.startButton.y + app.startButton.height):
        currOnButton = app.startButton
    app.currOnButton = currOnButton
            
def intro_onMousePress(app, mouseX, mouseY):
    for button in app.introButtons:
        if (button.x <= mouseX <= button.x + button.width and
            button.y <= mouseY <= button.y + button.height):
            if button.label == "Instructions":
                setActiveScreen(app, "instructions")
            elif button.label == "Quit":
                app.quit()
            break
    if (app.startButton.x <= mouseX <= app.startButton.x + app.startButton.width and
            app.startButton.y <= mouseY <= app.startButton.y + app.startButton.height):
        app.initiated = True

def intro_onStep(app):
    if app.initiated:
        app.introCounter += 1
        for button in app.introButtons:
            button.y -= 20
        app.titleY -= 20
        if app.introCounter > 40:
            setActiveScreen("difficulty")


def resetIntro(app):
    app.introButtons = []
    buttonLabels = ["Instructions", 'Settings', 'History', "Quit"]
    app.buttonWidth = 150
    app.buttonHeight = 50
    app.titleY = 150

    for i in range(len(buttonLabels)):
        label = buttonLabels[i]
        x = 160 + i * (app.buttonWidth + 20)
        y = 325
        button = Button('intro', label, x, y, app.buttonWidth, app.buttonHeight)
        app.introButtons.append(button)
    app.currOnButton = None
    app.startButton = Button('intro', 'Start!', 400, 435, 200, 75)

    app.initiated = False
    app.introCounter = 0



def difficulty_onAppStart(app):
    app.diffBoxX = 210
    app.diffBoxY = 280
    app.plusButtonX = app.diffBoxX + 160
    app.plusButtonY = app.diffBoxY+40
    app.minusButtonX = app.diffBoxX - 45
    app.minusButtonY = app.diffBoxY+40
    showBoxURL = './button/diffSel.png'
    app.showBoxImage = CMUImage(loadPilImage(showBoxURL))

    plusURL = './button/plus.png'
    app.plusImage = CMUImage(loadPilImage(plusURL))

    minusURL = './button/minus.png'
    app.minusImage = CMUImage(loadPilImage(minusURL))

    titleDFURL = './title/diffTitle.png'
    app.titleDFImage = CMUImage(loadPilImage(titleDFURL))

    titleDFLevelURL = './title/diffLevel.png'
    app.DFLevelImage = CMUImage(loadPilImage(titleDFLevelURL))

    titleUSRURL = './title/username.png'
    app.usernameImage = CMUImage(loadPilImage(titleUSRURL))

    backButtonWidth = 100
    backButtonHeight = 40
    backButtonX = 20
    backButtonY = app.height - backButtonHeight - 20
    app.backButton = Button('back', "Back", backButtonX, backButtonY, backButtonWidth, backButtonHeight)
    app.startButton = Button('intro', 'Start!', 400, 435, 200, 75)
    app.currOnButton = None
    app.initiated = False

    app.usrBoxX = 620
    app.usrBoxY = 280

    app.userEntering = False

    app.nextInitiated = False
    app.nextPageOpacity = 0
    app.diffCounter = 0




def difficulty_redrawAll(app):
    drawImage(app.introImage, 0, 0, width=app.width, height=app.height)
    dflTitleWidth, dflTtitleHeight = getImageSize(app.DFLevelImage)

    drawImage(app.DFLevelImage, app.diffBoxX-80, app.diffBoxY-70,width = dflTitleWidth/3.5, height = dflTtitleHeight/3.5)

    drawImage(app.showBoxImage, app.diffBoxX, app.diffBoxY, width=120, height=80)
    drawLabel(app.diffLevel, app.diffBoxX+60,app.diffBoxY+40,bold = True, size = 25)
    drawImage(app.plusImage, app.plusButtonX, app.plusButtonY, width=50., height=50,align = 'center')
    drawImage(app.minusImage, app.minusButtonX, app.minusButtonY, width=50., height=50,align = 'center')

    if app.userEntering:
        drawImage(app.showBoxImage, app.usrBoxX, app.usrBoxY, width=230, height=84.2)

    else:
        drawImage(app.showBoxImage, app.usrBoxX, app.usrBoxY, width=220, height=80)
    drawImage(app.usernameImage, app.usrBoxX-10, app.usrBoxY - 60, width=dflTitleWidth / 4,
            height=dflTtitleHeight / 4)

    drawLabel(app.username, app.usrBoxX + 110, app.usrBoxY + 40, bold=True, size=25,)
 


    if app.currOnButton == app.startButton:
        stbuttonY = app.startButton.y - 5
    else:
        stbuttonY = app.startButton.y

    drawImage(app.buttonImage,  app.startButton.x, stbuttonY, width= app.startButton.width, height= app.startButton.height)
    drawLabel(app.startButton.label,  app.startButton.x +  app.startButton.width/2, stbuttonY +  app.startButton.height/2, size=20, bold=True)

    if app.currOnButton == app.backButton:
        backButtonY = app.backButton.y - 2
    else:
        backButtonY = app.backButton.y

    drawImage(app.buttonImage,  app.backButton.x, backButtonY, width= app.backButton.width, height= app.backButton.height)
    drawLabel(app.backButton.label,  app.backButton.x +  app.backButton.width/2, backButtonY +  app.backButton.height/2, size=20, bold=True)

    titleWidth, titleHeight = getImageSize(app.titleDFImage)
    drawImage(app.titleDFImage, app.width / 2, 80, align='center', width=titleWidth / 1.8,
              height=titleHeight / 1.8)

    if app.nextInitiated:
        drawRect(0,0,app.width,app.height,fill = 'white',opacity = app.nextPageOpacity)

def difficulty_onStep(app):
    if app.nextInitiated:
        app.nextPageOpacity += 2
        if app.nextPageOpacity >= 99:
            setActiveScreen("play")
    
def difficulty_onMousePress(app, mouseX, mouseY):
    if getDistance(mouseX, mouseY,app.plusButtonX,app.plusButtonY) < 25 and app.diffLevel <= 7:
        app.diffLevel += 1
    if getDistance(mouseX, mouseY,app.minusButtonX,app.minusButtonY) < 25 and app.diffLevel >= 4:
        app.diffLevel -= 1

    if (app.usrBoxX <= mouseX <= app.usrBoxX + 220 and
            app.usrBoxY <= mouseY <= app.usrBoxY + 80):
        app.userEntering = True
    else:
        app.userEntering = False

    if (app.startButton.x <= mouseX <= app.startButton.x + app.startButton.width and
            app.startButton.y <= mouseY <= app.startButton.y + app.startButton.height):
        app.nextInitiated = True
        
    
    if (app.backButton.x <= mouseX <= app.backButton.x + app.backButton.width and
            app.backButton.y <= mouseY <= app.backButton.y + app.backButton.height):
        resetIntro(app)
        setActiveScreen("intro")


def difficulty_onMouseMove(app, mouseX, mouseY):
    app.currOnButton = None
    if (app.startButton.x <= mouseX <= app.startButton.x + app.startButton.width and
            app.startButton.y <= mouseY <= app.startButton.y + app.startButton.height):
        app.currOnButton = app.startButton

    if (app.backButton.x <= mouseX <= app.backButton.x + app.backButton.width and
            app.backButton.y <= mouseY <= app.backButton.y + app.backButton.height):

        app.currOnButton = app.backButton

def difficulty_onKeyPress(app,key):
    if app.userEntering:
        if key != 'backspace':
            app.username += key
        else:
            app.username = app.username[:-1]






def play_onAppStart(app):
    app.mouseX = 0
    app.mouseY = 0
    app.roadPreview = False
    app.roadOpacity = 100
    app.gridSize = 20
    app.roadWidth = 30
    app.laneMarkingInterval = 10
    app.showGrid = True
    app.roadsCoordinates = []
    for i in range(0,app.height,4):
        row = []
        for j in range(0,app.width,4):
            row.append(0)
        app.roadsCoordinates.append(row)
    top = []
    right = []
    down = []
    left = []
    app.roads = []
    for i in range(0,app.diffLevel):
        side = random.random()*4
        # Left side of the screen
        if 0<=side<1:
            y = generateRadnBetween(140,500)//10*10
            for point in left:
                while abs(y-point)<40:
                    y = generateRadnBetween(140, 500)//10*10
            left.append(y)
            p1 = (0, y)
            p2 = (75, y)
            left.append(y)
            app.roads.append(Road('Straight', [p1,p2], 'Ground',True))
        # Top side
        elif 1<=side<2:
            x = generateRadnBetween(280, 760)//10*10
            for point in top:
                while abs(x-point)<40:
                    x = generateRadnBetween(280, 760)//10*10
            top.append(x)
            p1 = (x, 0)
            p2 = (x,75)
            app.roads.append(Road('Straight', [p1, p2], 'Ground',True))
        #Right side
        elif 2<=side<3:
            y = generateRadnBetween(140, 480)//10*10
            for point in right:
                while abs(y - point) < 40:
                    y = generateRadnBetween(140, 480)//10*10
            right.append(y)
            p1 = (app.width, y)
            p2 = (app.width-75, y)
            app.roads.append(Road('Straight', [p1, p2], 'Ground',True))
        else:
            x = generateRadnBetween(280, 760)//10*10
            for point in down:
                while abs(x - point) < 40:
                    x = generateRadnBetween(280, 760)//10*10
            down.append(x)
            p1 = (x, app.height)
            p2 = (x, app.height-75)
            app.roads.append(Road('Straight', [p1, p2], 'Ground',True))

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
    app.collisionBoxWidth = 8
    app.collisionBoxHeight = 30
    app.collisionBoxHeightCar = 42

    bulldozeURL = './sign/bz.png'
    app.bdImage = CMUImage(loadPilImage(bulldozeURL))
    bdWidth, bdHeight = getImageSize(app.bdImage)
    app.BDmode = False
    app.BDWidth = bdWidth/5
    app.BDHeight = bdHeight/5

    settingURL = './sign/settings.png'
    app.settingsImage = CMUImage(loadPilImage(settingURL))
    settingsWidth, settingsHeight = getImageSize(app.settingsImage)
    app.showSettings = False
    app.settingsWidth = settingsWidth / 16.2
    app.settingsHeight = settingsHeight / 16.2

    shovelURL = './sign/shovel.png'
    app.shovelImage = CMUImage(loadPilImage(shovelURL))

    app.BDselect = None
    app.justCome = True
    app.palyPageOpacity = 100

    app.timeSpent=[]
    app.aveTime = 'N/A'

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
    bdButton = Button('BD',' ',910,40)
    settingsButton = Button('settings', ' ', 970, 40)
    app.buttons.append(button)
    app.buttons.append(startButton)
    app.buttons.append(bdButton)

    app.buttons.append(settingsButton)


def play_onMousePress(app,mouseX,mouseY):
    app.roads = sortRoadsElevation(app)
    if app.isDrawing or app.currentMode:
        app.roadsChanged = True
        app.edgeIntersections = findEdgeIntersections(app)


    #if clcked again, then draw the road
    if app.isDrawing and app.currentMode != None and not app.BDmode:

        mappedX, mappedY = int(app.cursorX),int(app.cursorY)
        if app.currentMode == 'Straight':

            #if we already have an end points

            if len(app.currentRoad.points) == 2:
                app.roads.append(app.currentRoad)
            if app.megTemp != None:
                ind = app.megTemp[0]
                # if app.megTemp[2] == 'end':
                #     if app.roads[ind].type == 'Straight':
                #         inter = Intersection(app.roads[ind].points[1],app.roads[ind].elevation,'3-way',
                #                              (app.currentRoad,app.roads[ind]))
                #         app.roads[ind].changeEndStatus(2)
                #
                #         app.intersections.add(inter)
                #         app.roads[ind].addIntersection(inter)
                #         app.currentRoad.addIntersection(inter)
                #
                #     if app.roads[ind].type == 'Curved':
                #         inter = Intersection(app.roads[ind].points[2],app.roads[ind].elevation,'3-way',
                #                              (app.currentRoad,app.roads[ind]))
                #         app.intersections.add(inter)
                #         app.roads[ind].addIntersection(inter)
                #         app.currentRoad.addIntersection(inter)
                #         app.roads[ind].changeEndStatus(2)
                # else:
                #     if app.roads[ind].type == 'Straight':
                #         inter = Intersection(app.roads[ind].points[0],app.roads[ind].elevation,'3-way',
                #                              (app.currentRoad,app.roads[ind]))
                #         app.roads[ind].changeEndStatus(1)
                #
                #         app.intersections.add(inter)
                #         app.roads[ind].addIntersection(inter)
                #         app.currentRoad.addIntersection(inter)
                #
                #     if app.roads[ind].type == 'Curved':
                #         inter = Intersection(app.roads[ind].points[0],app.roads[ind].elevation,'3-way',
                #                              (app.currentRoad,app.roads[ind]))
                #         app.intersections.add(inter)
                #         app.roads[ind].addIntersection(inter)
                #         app.currentRoad.addIntersection(inter)
                #         app.roads[ind].changeEndStatus(1)


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
        if each.type == 'BD':

            if (each.x-app.BDWidth <= mouseX <= each.x+app.BDWidth and
            each.y-app.BDHeight <= mouseY <= each.y+app.BDHeight):
                app.BDmode = not app.BDmode
                return

        if each.type == 'settings':
            if (each.x-app.BDWidth <= mouseX <= each.x+app.BDWidth and
            each.y-app.BDHeight <= mouseY <= each.y+app.BDHeight):
                app.showSettings = not app.showSettings
                return


        if (each.x <= mouseX <= each.x+app.buttonWidth and
            each.y <= mouseY <= each.y+app.buttonHeight):
            if each.type == 'mode':
                app.currentMode = each.label
            elif each.type == 'grid':
                app.showGrid = not app.showGrid
            elif each.type == 'start':
                app.paused = not app.paused
                if not app.initiated:
                    app.path = findUnpackedPaths(app,findPaths(app, app.roads[0], app.roads[1]))


                app.initiated = True
            return


    #map to the closet 20*20 coordinate
    mappedX, mappedY = int(app.cursorX),int(app.cursorY)

    if app.currentMode == 'Straight' and not app.BDmode:

        app.currentRoad = Road("Straight",[(mappedX, mappedY)], app.currentElevation)
        app.isDrawing = True

    elif app.currentMode == 'Curved' and not app.BDmode:
        #check is this is the first click
        if not app.isDrawing:
            app.currentRoad = Road('Curved',[(mappedX, mappedY)], app.currentElevation)
            app.isDrawing = True
            #the next point will be the middle point between start and end point
            app.drawingState = 'p2'

    if app.BDmode and app.BDselect:
        for road in app.roads:
            if app.BDselect == road:
                ind = app.roads.index(road)
                app.roads.pop(ind)


def play_onMouseMove(app, mouseX,mouseY):
    app.mouseX,app.mouseY = mouseX,mouseY
    magneticCursor(app,mouseX,mouseY)
    if app.cursorUserControlled:
        app.cursorX, app.cursorY = mouseX, mouseY

    if app.isDrawing and app.currentMode != None and not app.BDmode:
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
    elif app.BDmode:
        for road in app.roads:
            for i in range(len(road.points)-1):
                lx1,ly1 = road.points[i]
                lx2,ly2 = road.points[i+1]
                if ((distancePointToLine(mouseX,mouseY,lx1,ly1,lx2,ly2) < 15) and
                min(lx1,lx2) < mouseX<max(lx1,lx2) and min(ly1,ly2)-15 < mouseY < max(ly1,ly2)+15):
                    app.BDselect = road
                    return
        app.BDselect = None



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

def sortAmountCarsUsingPath(app,paths,pathDistanceDict):
    for ind in pathDistanceDict:
        for car in app.cars:
            if car.path == paths[ind]:
                pathDistanceDict[ind] += 50
    return pathDistanceDict
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
def play_redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill='lightGreen')

    if app.showGrid:
        drawGrid(app)

    for each in app.roads:
        drawRoad(app, each)

    if app.isDrawing and app.currentRoad != None:
        drawRoad(app, app.currentRoad)

    drawIntersectMarking(app)
    drawCar(app)
    drawIntersectMarkingWithTL(app)
    drawTrafficLightsForMagCursor(app)
    drawButtons(app)

    points = []
    for path in app.path:
        for i in range(len(path) - 1):
            points.append((path[i][1], path[i + 1][1]))
        for each in points:
            x1, y1 = each[0]
            x2, y2 = each[1]
            drawLine(x1, y1, x2, y2)


    if not app.BDmode:
        drawCircle(app.cursorX, app.cursorY, 10, fill='darkSlateGray')
        drawCircle(app.cursorX, app.cursorY, 10, fill='darkSlateGray')
    else:
        shovelWidth,shovelHeight = getImageSize(app.shovelImage)
        drawImage(app.shovelImage,app.mouseX,app.mouseY,width=shovelWidth//10,height=shovelHeight//10,align = 'center')

    drawRect(830,420,400,110,opacity = 65,fill='white')
    drawLabel("Current elevation:", 920, 490, bold=True, size=15)
    drawLabel(app.currentElevation,920,510,size=20,bold=True)
    if app.justCome:
        drawRect(0,0,app.width,app.height,fill = 'white',opacity = app.palyPageOpacity)

    drawLabel("Average Time Spent:",920,440,bold=True,size = 15)
    drawLabel(app.aveTime, 920, 465, bold=True, size=20)

def play_onKeyPress(app,key):
    if key == 'up' and app.currentElevation == 'Ground':
        app.currentElevation = 'Bridge'
        if app.isDrawing and app.currentRoad != None:
            app.currentRoad.elevation = app.currentElevation

    elif key == 'down' and app.currentElevation == 'Bridge':
        app.currentElevation = 'Ground'
        if app.isDrawing and app.currentRoad != None:
            app.currentRoad.elevation = app.currentElevation
def play_onStep(app):
    if app.justCome:
        app.palyPageOpacity -= 2
        if app.palyPageOpacity <= 4:
            app.justCome = False

    if not app.paused:
        if app.counter % 40 == 0:
            generateCars(app)
        app.counter += 1
        trafficLightsToggle(app)
        updateCarMove(app)
    if app.roadsChanged:

        findIntersections(app)
        app.edgeIntersections = findEdgeIntersections(app)
        app.roadsChanged = False

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
            for x, y in collisionBox:
                drawCircle(x, y, 2)
            x1,y1 = car.pos
            x2,y2 = car.currDestination
            angle = findAngleTwoPints(x1,y1,x2,y2)
            car.angle = angle
            imageWidth,imageHeight = getImageSize(app.carImages[car.type])
            drawImage(app.carImages[car.type], x1,y1,width = imageWidth//18, height = imageHeight//18, align='center',rotateAngle = car.angle)

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
                otherCarX,otherCarY = otherCar.pos
                if (min(x1, x2, x3, x4) <= otherCarX <= max(x1, x2, x3, x4) and
                        min(y1, y2, y3, y4) <= otherCarY <= max(y1, y2, y3, y4)
                        and abs(car.angle-otherCar.angle)<60):

                    return True
    return False


def updateCarMove(app):

    for car in app.cars:
        if car.currPointInd >= len(car.path)-1:
            car.endTime = time.time()
            car.finished = True
            ind = app.cars.index(car)
            app.cars.pop(ind)
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
                    # if (car.currPointInd + 1) < len(car.path):
                    #     nextRoad = car.path[car.currPointInd + 1][0]
                    #     print(car.currRoad.points[-1])
                    #     print(car.currRoad.points[0])
                    #     print(inter.points)
                    #     if inter.type == '4' and (car.currRoad.points[-1] == inter.points or car.currRoad.points[0] == inter.points):
                    #         anyInterBetween = False
                    #         currRoadInd = inter.roads.index(car.currRoad)
                    #         nextRoadInd = inter.roads.index(nextRoad)
                    #         if currRoadInd+1 == nextRoadInd:
                    #             car.nextMove = 'Right'
                    #         elif currRoadInd+1 < nextRoadInd:
                    #             car.nextMove = None
                    #         elif currRoadInd-1 == nextRoadInd:
                    #             car.nextMove = 'Left'
                    #         break

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

                            if abs(angle) < 130:
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


        if each.type == 'BD':
            drawImage(app.bdImage, each.x, each.y, width=app.BDWidth, height=app.BDHeight,
                      align='center')
            drawLabel(each.label, each.x + app.BDWidth / 2, each.y + app.BDHeight / 2, size=12)
        elif each.type == 'settings':
            drawImage(app.settingsImage, each.x, each.y, width=app.settingsWidth, height=app.settingsHeight, align ='center')
            drawLabel(each.label, each.x + app.settingsWidth / 2, each.y + app.settingsHeight / 2, size=12)
        else:
            drawRect(each.x, each.y, app.buttonWidth, app.buttonHeight, fill=color, border='black')
            drawLabel(each.label, each.x + app.buttonWidth / 2, each.y + app.buttonHeight / 2, size=12)


def mapToCoordinates(app,x,y):
    return rounded(x / app.gridSize) * app.gridSize, rounded(y / app.gridSize) * app.gridSize

def drawRoad(app,road):
    roadType = road.type
    points = road.points
    elevation = road.elevation
    if roadType == 'Straight':
        #chekc if drawing is finished
        if len(points) >= 2:
            drawStraightRoad(app,points[0], points[1], elevation,road)
            if app.isDrawing:
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

    if app.BDselect == road:
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

    if app.BDselect == road:
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

    if app.isDrawing:
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
                                inter = Intersection(point, road1.elevation, '4-way', (road1, road2))
                                road2.addIntersection(inter)
                                road1.addIntersection(inter)
                                app.intersections.add(inter)

    for i in range(len(app.roads)):
        road = app.roads[i]

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
                inter = Intersection((x, y), roadsAtPoint[0].elevation, str(interType), roadsAtPoint)
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

def sortRoadsElevation(app):
    retGround = []
    retBridge = []
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


def drawTrafficLightsForMagCursor(app):
    visited = set()
    for inter in app.intersections:
        if (inter.type == '4' or inter.type == '3') and inter.points not in visited:
            inter.roads = sortRoads(inter)
            visited.add(inter.points)
            for i in range(len(inter.roads)):
                road = inter.roads[i]

                if len(inter.trafficLights)<int(inter.type) and not inter.TLInitialized:

                    if i == 0 or i == 2:
                        tl = TrafficLight(inter, 0)
                        tl.road = road
                        inter.trafficLights.append(tl)
                    else:
                        tl = TrafficLight(inter, 3)

                        tl.road = road
                        inter.trafficLights.append(tl)
                elif len(inter.trafficLights) == int(inter.type):
                    if i == 0 or i == 2:
                        tl = TrafficLight(inter, 0)
                        tl.road = road
                        inter.trafficLights.append(tl)
                    else:
                        tl = TrafficLight(inter, 3)

                        tl.road = road
                        inter.trafficLights.append(tl)
                    inter.TLInitialized = True
                else:
                    tl = inter.trafficLights[i]

                if road.points[0] == inter.points:
                    rx1,ry1 = road.points[0]
                    rx2,ry2 = road.points[1]

                else:
                    rx1, ry1= road.points[1]
                    rx2, ry2 = road.points[0]



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


def main():
    runAppWithScreens(initialScreen='intro')

main()