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
    app.instruFromMenu = False
    app.width = 1000
    app.height = 600
    app.username = ''
    app.diffLevel = 4

    crossURL = './sign/cross.png'
    app.crossImage = CMUImage(loadPilImage(crossURL))

    app.crossImage = CMUImage(loadPilImage(crossURL))
    crossWidth, crossHeight = getImageSize(app.crossImage)
    app.crossWidth = crossWidth / 16.3
    app.crossHeight = crossHeight / 16.3

    app.showSettings = False
    app.backgroundMusic = True
    app.backgroundMusicButtonX = 520
    app.backgroundMusicButtonY = 200
    app.musicEffects = True
    app.musicEffectsButtonX = 520
    app.musicEffectsButtonY = 260
    app.carRepr = True
    app.carReprButtonX = 520
    app.carReprButtonY = 320
    app.showPath = False
    app.showPathButtonX = 520
    app.showPathButtonY = 380
    app.settingsButtonWidth = 100
    app.settingsButtonHeight = 40

    app.BDselect = None
    app.justCome = True
    app.settingsButtons = []

    app.soundBack = Sound('./music/bgm.mp3')
    if app.backgroundMusic:
        app.soundBack.play(loop=True)
    else:
        app.soundBack.pause()

    app.buttonSound = Sound('./music/button.mp3')
    app.roads = []

    app.showInstructions = False

    app.overAllInstructions = True
    app.roadDrawStraightInstructions = False
    app.roadDrawCurvedInstructions = False
    app.roadDrawBridgeInstructions = False
    app.removeRoadInstructions = False
    app.playInstructions = False
    app.settingsInstructions = False
    app.scoreInstructions = False

    app.imageUrlsStraightRoad = [f'./instructions/straightRoad/ezgif-frame-00{i}.jpg' for i in range(1, 10)]
    app.imageUrlsStraightRoad += [f'./instructions/straightRoad/ezgif-frame-0{i}.jpg' for i in range(10, 100)]
    app.imageUrlsStraightRoad += [f'./instructions/straightRoad/ezgif-frame-{i}.jpg' for i in range(100, 111)]
    app.imagesStraightRoad = [Image.open(url) for url in app.imageUrlsStraightRoad]
    app.imagesStraightRoad = [CMUImage(image) for image in app.imagesStraightRoad]
    app.straightRoadImageInd = 0

    app.imageUrlsBridge = [f'./instructions/bridge/ezgif-frame-00{i}.jpg' for i in range(1, 10)]
    app.imageUrlsBridge += [f'./instructions/bridge/ezgif-frame-0{i}.jpg' for i in range(10, 100)]
    app.imageUrlsBridge += [f'./instructions/bridge/ezgif-frame-{i}.jpg' for i in range(100, 201)]
    app.imagesBridge = [Image.open(url) for url in app.imageUrlsBridge]
    app.imagesBridge = [CMUImage(image) for image in app.imagesBridge]
    app.bridgeInd = 0

    app.imageUrlsCurvedRoad = [f'./instructions/curvedRoad/ezgif-frame-00{i}.jpg' for i in range(1, 10)]
    app.imageUrlsCurvedRoad += [f'./instructions/curvedRoad/ezgif-frame-0{i}.jpg' for i in range(10, 46)]
    app.imageUrlsCurvedRoad += [f'./instructions/curvedRoad/ezgif-frame-{i}.jpg' for i in range(100, 142)]
    app.imagesCurvedRoad = [Image.open(url) for url in app.imageUrlsCurvedRoad]
    app.imagesCurvedRoad = [CMUImage(image) for image in app.imagesCurvedRoad]
    app.curvedRoadImageInd = 0

    app.imageUrlsRemove = [f'./instructions/remove/ezgif-frame-00{i}.jpg' for i in range(1, 10)]
    app.imageUrlsRemove += [f'./instructions/remove/ezgif-frame-0{i}.jpg' for i in range(10, 46)]
    app.imagesRemove = [Image.open(url) for url in app.imageUrlsRemove]
    app.imagesRemove = [CMUImage(image) for image in app.imagesRemove]
    app.removeInd = 0

    app.imageUrlsPlay = [f'./instructions/play/ezgif-frame-00{i}.jpg' for i in range(1, 10)]
    app.imageUrlsPlay += [f'./instructions/play/ezgif-frame-0{i}.jpg' for i in range(10, 100)]
    app.imageUrlsPlay += [f'./instructions/play/ezgif-frame-{i}.jpg' for i in range(100, 201)]
    app.imagesPlay = [Image.open(url) for url in app.imageUrlsPlay]
    app.imagesPlay = [CMUImage(image) for image in app.imagesPlay]
    app.playInd = 0
    app.ranking = []

def intro_onAppStart(app):
    introURL = './backgrounds/intro.jpg'
    app.introImage = CMUImage(loadPilImage(introURL))

    buttonURL = './button/button1.png'
    app.buttonImage = CMUImage(loadPilImage(buttonURL))

    titleURL = './title/title.png'
    app.titleImage = CMUImage(loadPilImage(titleURL))


    app.introButtons = []
    buttonLabels = ["Instructions", 'Settings','History',"Quit"]
    app.introButtonWidth = 150
    app.introButtonHeight = 50
    app.titleY = 150

    for i in range(len(buttonLabels)):
        label = buttonLabels[i]
        x = 160 + i*(150 + 20)
        y = 325
        button = Button('intro', label, x, y, 150, 50)
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

        drawImage(app.buttonImage,button.x, buttonY, width = 150, height = 50)

        drawLabel(button.label, button.x + 150 / 2, buttonY + 50 / 2, size=16,bold=True)

    if app.currOnButton == app.startButton:
        stbuttonY = app.startButton.y - 5
    else:
        stbuttonY = app.startButton.y

    drawImage(app.buttonImage,  app.startButton.x, stbuttonY, width= 200, height= 75)
    drawLabel(app.startButton.label,  app.startButton.x +  200/2, stbuttonY +  75/2, size=20, bold=True)

    if app.showSettings:
        drawSettings(app)


def intro_onMouseMove(app, mouseX, mouseY):
    currOnButton = None
    for button in app.introButtons:
        if (button.x <= mouseX <= button.x + button.width and
            button.y <= mouseY <= button.y + button.height):
            currOnButton = button
            if app.musicEffects:
                app.buttonSound.play()
            break
    if (app.startButton.x <= mouseX <= app.startButton.x + app.startButton.width and
            app.startButton.y <= mouseY <= app.startButton.y + app.startButton.height):
        currOnButton = app.startButton
        if app.musicEffects:
            app.buttonSound.play()
    app.currOnButton = currOnButton
            
def intro_onMousePress(app, mouseX, mouseY):
    if not app.showSettings:
        for button in app.introButtons:
            if (button.x <= mouseX <= button.x + button.width and
                button.y <= mouseY <= button.y + button.height):
                if button.label == "Instructions":
                    if app.musicEffects:
                        app.buttonSound.play()
                    app.instruFromMenu = True
                    app.showInstructions = True
                    setActiveScreen("play")
                if button.label == "Settings":
                    if app.musicEffects:
                        app.buttonSound.play()
                    app.showSettings = True
                if button.label == "History":
                    if app.musicEffects:
                        app.history = readSavedInfo()
                        for line in app.history.splitlines():
                            temp = []
                            for each in line.split(' '):
                                temp.append(each)
                            app.ranking.append(temp)
                        ###################################################
                        #Learned this from:
                        #https://stackoverflow.com/questions/18563680/how-to-sort-a-2d-list
                        ###################################################
                        app.ranking = sorted(app.ranking, key=lambda x: float(x[2]), reverse=True)
                        app.buttonSound.play()
                    setActiveScreen("history")
                elif button.label == "Quit":
                    if app.musicEffects:
                        app.buttonSound.play()
                    app.quit()
                break
        if (app.startButton.x <= mouseX <= app.startButton.x + app.startButton.width and
                app.startButton.y <= mouseY <= app.startButton.y + app.startButton.height):
            if app.musicEffects:
                app.buttonSound.play()
            app.initiated = True
    else:
        if (app.backgroundMusicButtonX-app.settingsButtonWidth/2 <= mouseX <=
                app.backgroundMusicButtonX+app.settingsButtonWidth*1.5 and
                app.backgroundMusicButtonY-app.settingsButtonHeight/2 <= mouseY <=
                app.backgroundMusicButtonY+app.settingsButtonHeight/2):
            if app.musicEffects:
                app.buttonSound.play()
            app.backgroundMusic = not app.backgroundMusic
            if app.backgroundMusic:
                app.soundBack.play(loop=True)
            else:
                app.soundBack.pause()

        elif (app.musicEffectsButtonX-app.settingsButtonWidth/2 <= mouseX <=
                app.musicEffectsButtonX+app.settingsButtonWidth*1.5 and
                app.musicEffectsButtonY-app.settingsButtonHeight/2 <= mouseY <=
                app.musicEffectsButtonY+app.settingsButtonHeight/2):
            if app.musicEffects:
                app.buttonSound.play()
            app.musicEffects = not app.musicEffects

        elif (app.carReprButtonX-app.settingsButtonWidth/2 <= mouseX <=
                app.carReprButtonX+app.settingsButtonWidth*1.5 and
                app.carReprButtonY-app.settingsButtonHeight/2 <= mouseY <=
                app.carReprButtonY+app.settingsButtonHeight/2):
            if app.musicEffects:
                app.buttonSound.play()
            app.carRepr = not app.carRepr

        elif (app.showPathButtonX-app.settingsButtonWidth/2 <= mouseX <=
                app.showPathButtonX+app.settingsButtonWidth*1.5 and
                app.showPathButtonY-app.settingsButtonHeight/2 <= mouseY <=
                app.showPathButtonY+app.settingsButtonHeight/2):
            if app.musicEffects:
                app.buttonSound.play()
            app.showPath = not app.showPath

        elif (870 <= mouseX <= 870+app.crossWidth and
                85 <= mouseY <= 85+app.crossHeight):
            if app.musicEffects:
                app.buttonSound.play()
            app.showSettings = False

def intro_onStep(app):
    if app.initiated:
        app.introCounter += 1
        for button in app.introButtons:
            button.y -= 20
        app.titleY -= 20
        if app.introCounter > 40:
            setActiveScreen("difficulty")


def resetIntro(app):
    app.introButtonWidth = 150
    app.introButtonHeight = 50
    app.introButtons = []
    buttonLabels = ["Instructions", 'Settings', 'History', "Quit"]
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

def history_onAppStart(app):
    backButtonWidth = 100
    backButtonHeight = 40
    backButtonX = 20
    backButtonY = app.height - backButtonHeight - 20
    app.backButton = Button('back', "Back", backButtonX, backButtonY, backButtonWidth, backButtonHeight)
    app.currOnButton = None

    introURL = './backgrounds/intro.jpg'
    app.introImage = CMUImage(loadPilImage(introURL))

    titleHistoryURL = './title/history.png'
    app.titleHistoryImage = CMUImage(loadPilImage(titleHistoryURL))

    app.history = readSavedInfo()

def history_redrawAll(app):
    drawImage(app.introImage,0, 0, width = app.width, height = app.height)
    titleWidth, titleHeight = getImageSize(app.titleImage)
    drawImage(app.titleHistoryImage, app.width / 2, 80,align='center',width=titleWidth/3,height=titleHeight/3)

    drawLabel("Rank", 200, 140, size=30, bold=True)
    drawLabel("Username",400,140,size=30,bold=True)
    drawLabel("Difficulty", 600, 140, size=30,bold=True)
    drawLabel("Score", 800, 140, size=30,bold=True)

    if len(app.ranking)<=10:
        for i in range(len(app.ranking)):
            user = app.ranking[i]
            userName = user[0]
            diffLevel = user[1]
            score = user[2]
            drawLabel(i+1,200,30*i+200,size=20, bold=True)
            drawLabel(userName,400,30*i+200,size=20, bold=True)
            drawLabel(diffLevel,600,30*i+200,size=20, bold=True)
            drawLabel(score, 800, 30*i+200,size=20, bold=True)
    else:
        for i in range(10):
            user = app.ranking[i]
            userName = user[0]
            diffLevel = user[1]
            score = user[2]
            drawLabel(userName, 200, 200)
            drawLabel(diffLevel, 250, 200)
            drawLabel(score, 300, 200)

    if app.currOnButton == app.backButton:
        backButtonY = app.backButton.y - 2
    else:
        backButtonY = app.backButton.y
    drawImage(app.buttonImage, app.backButton.x, backButtonY, width=app.backButton.width, height=app.backButton.height)
    drawLabel(app.backButton.label, app.backButton.x + app.backButton.width / 2,
              backButtonY + app.backButton.height / 2, size=20, bold=True)

def difficulty_onMouseMove(app, mouseX, mouseY):
    app.currOnButton = None

    if (app.backButton.x <= mouseX <= app.backButton.x + app.backButton.width and
            app.backButton.y <= mouseY <= app.backButton.y + app.backButton.height):
        if app.musicEffects:
            app.buttonSound.play()
        app.currOnButton = app.backButton

def history_onMousePress(app, mouseX, mouseY):
    if (app.backButton.x <= mouseX <= app.backButton.x + app.backButton.width and
            app.backButton.y <= mouseY <= app.backButton.y + app.backButton.height):
        if app.musicEffects:
            app.buttonSound.play()
        intro_onAppStart(app)
        setActiveScreen("intro")


##################################
#Learned this from:
#https://hackernoon.com/how-to-read-text-file-in-python
##################################
def readSavedInfo():
    file = open("savedInfo.txt", "r")
    history = file.read()
    file.close()
    return history

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
        if app.musicEffects:
            app.buttonSound.play()
    if getDistance(mouseX, mouseY,app.minusButtonX,app.minusButtonY) < 25 and app.diffLevel >= 4:
        app.diffLevel -= 1
        if app.musicEffects:
            app.buttonSound.play()

    if (app.usrBoxX <= mouseX <= app.usrBoxX + 220 and
            app.usrBoxY <= mouseY <= app.usrBoxY + 80):
        if app.musicEffects:
            app.buttonSound.play()
        app.userEntering = True
    else:
        app.userEntering = False

    if (app.startButton.x <= mouseX <= app.startButton.x + app.startButton.width and
            app.startButton.y <= mouseY <= app.startButton.y + app.startButton.height):
        if app.musicEffects:
            app.buttonSound.play()
        app.nextInitiated = True
        if not app.username:
            app.username = 'Anonym'
        app.roads = []
        top = []
        right = []
        down = []
        left = []

        for i in range(0, app.diffLevel):
            side = random.random() * 4
            # Left side of the screen
            if 0 <= side < 1:
                y = generateRadnBetween(140, 500) // 10 * 10
                for point in left:
                    while abs(y - point) < 40:
                        y = generateRadnBetween(140, 500) // 10 * 10
                left.append(y)
                p1 = (0, y)
                p2 = (150, y)
                left.append(y)
                app.roads.append(Road('Straight', [p1, p2], 'Ground', True))
            # Top side
            elif 1 <= side < 2:
                x = generateRadnBetween(280, 760) // 10 * 10
                for point in top:
                    while abs(x - point) < 40:
                        x = generateRadnBetween(280, 760) // 10 * 10
                top.append(x)
                p1 = (x, 0)
                p2 = (x, 150)
                app.roads.append(Road('Straight', [p1, p2], 'Ground', True))
            # Right side
            elif 2 <= side < 3:
                y = generateRadnBetween(180, 480) // 10 * 10
                for point in right:
                    while abs(y - point) < 40:
                        y = generateRadnBetween(180, 480) // 10 * 10
                right.append(y)
                p1 = (app.width, y)
                p2 = (app.width - 150, y)
                app.roads.append(Road('Straight', [p1, p2], 'Ground', True))
            else:
                x = generateRadnBetween(180, 780) // 10 * 10
                for point in down:
                    while abs(x - point) < 40:
                        x = generateRadnBetween(180, 780) // 10 * 10
                down.append(x)
                p1 = (x, app.height)
                p2 = (x, app.height - 150)
                app.roads.append(Road('Straight', [p1, p2], 'Ground', True))
        
    
    if (app.backButton.x <= mouseX <= app.backButton.x + app.backButton.width and
            app.backButton.y <= mouseY <= app.backButton.y + app.backButton.height):
        if app.musicEffects:
            app.buttonSound.play()
        intro_onAppStart(app)
        setActiveScreen("intro")


def difficulty_onMouseMove(app, mouseX, mouseY):
    app.currOnButton = None
    if (app.startButton.x <= mouseX <= app.startButton.x + app.startButton.width and
            app.startButton.y <= mouseY <= app.startButton.y + app.startButton.height):
        if app.musicEffects:
            app.buttonSound.play()
        app.currOnButton = app.startButton

    if (app.backButton.x <= mouseX <= app.backButton.x + app.backButton.width and
            app.backButton.y <= mouseY <= app.backButton.y + app.backButton.height):
        if app.musicEffects:
            app.buttonSound.play()
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
    app.carImageWidth, app.carImageHeight = getImageSize(app.carImages[0])
    app.carImageWidth /= 18
    app.carImageHeight /= 18
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
    app.BDWidth = bdWidth/4.8
    app.BDHeight = bdHeight/4.8



    shovelURL = './sign/shovel.png'
    app.shovelImage = CMUImage(loadPilImage(shovelURL))


    app.palyPageOpacity = 100

    app.timeSpent=[]
    app.aveTime = 'N/A'

    settingURL = './sign/settings.png'
    app.settingsImage = CMUImage(loadPilImage(settingURL))
    settingsWidth, settingsHeight = getImageSize(app.settingsImage)
    app.settingsWidth = settingsWidth / 16.3
    app.settingsHeight = settingsHeight / 16.3

    instructionsURL = './sign/instructions.png'
    app.instructionsImage = CMUImage(loadPilImage(instructionsURL))
    instructionsWidth, instructionsHeight = getImageSize(app.instructionsImage)
    app.instructionsWidth = instructionsWidth / 7.5
    app.instructionsHeight = instructionsHeight / 7.5

    app.soundTraffic = Sound('./music/traffic.mp3')

    app.sessionFinished = False
    app.carNum = 0

    app.returnMenuButtonX = 220
    app.returnMenuButtonY = 440

    app.restartButtonX = 420
    app.restartButtonY = 440
    app.resultsButtonWidth = 180
    app.resultsButtonHeight = 50

    app.inrtruButtonWidth = 80
    app.inrtruButtonHeight = 30

    app.overAllInstructionsPrevButtonX = None
    app.overAllInstructionsPrevButtonY = None


    app.overAllInstructionsNextButtonX = 630
    app.overAllInstructionsYButtonY = 390

    app.roadDrawStraightPrevButtonX = 160
    app.roadDrawStraightPrevButtonY = 490

    app.roadDrawStraightNextButtonX = 510
    app.roadDrawStraightNextButtonY = 490


    app.roadDrawCurvedPrevButtonX = 150
    app.roadDrawCurvedPrevButtonY = 450

    app.roadDrawCurvedNextButtonX = 510
    app.roadDrawCurvedNextButtonY = 450


    app.roadBridgePrevButtonX = 340
    app.roadBridgePrevButtonY = 470

    app.roadBridgeNextButtonX = 690
    app.roadBridgeNextButtonY = 470


    app.removePrevButtonX = 160
    app.removePrevButtonY = 520

    app.removeNextButtonX = 510
    app.removeNextButtonY = 520


    app.playPrevButtonX = 530
    app.playPrevButtonY = 480

    app.playNextButtonX = 880
    app.playNextButtonY = 480

    app.curveIntersects = False

    app.score = 0
    app.tlDuration = 30
    app.showTlPanel = False

def createButtons(app):
    for i in range(len(app.modes)):
        x = app.buttonMargin + i*(app.buttonWidth + app.buttonMargin)
        y = app.buttonMargin
        button = Button('mode',app.modes[i], x, y)
        app.buttons.append(button)

    x = app.buttonMargin
    y = app.buttonMargin*2 + app.buttonHeight
    button = Button('grid',"Toggle Grid", x, y)
    tlButton = Button("tl","Traffic Lights", x+(app.buttonWidth + app.buttonMargin), y)
    startButton = Button('start', "Finished!",880,540)
    bdButton = Button('BD',' ',100,550)
    settingsButton = Button('settings', ' ', 40, 550)
    instructionsButton = Button('instructions', ' ', 136, 525)
    app.buttons.append(button)
    app.buttons.append(startButton)
    app.buttons.append(bdButton)
    app.buttons.append(instructionsButton)
    app.buttons.append(tlButton)

    app.buttons.append(settingsButton)


def play_onMousePress(app,mouseX,mouseY):
    if (not app.showSettings and not app.sessionFinished and
            not app.showInstructions and app.paused):
        app.roads = sortRoadsElevation(app)
        if app.isDrawing or app.currentMode and not app.showTlPanel:
            app.roadsChanged = True
            app.edgeIntersections = findEdgeIntersections(app)


        #if clcked again, then draw the road
        if app.isDrawing and app.currentMode != None and not app.BDmode and not app.showTlPanel:

            mappedX, mappedY = int(app.cursorX),int(app.cursorY)
            if app.currentMode == 'Straight':

                #if we already have an end points
                if len(app.currentRoad.points) == 2:
                    for road in app.roads:
                        if road.highlighted:
                            return
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
                    for road in app.roads:
                        if road.highlighted:
                            return
                    app.roads.append(app.currentRoad)
                    app.currentRoad = None
                    app.isDrawing = False
                    app.drawingState = None
                    return
                if app.drawingState == 'p2':
                    app.currentRoad.points.append((mappedX, mappedY))
                    #the next click will be the end poiny
                    app.drawingState = 'end'

        # check which button is pressed
        for each in app.buttons:
            if each.type == 'BD':

                if (each.x-app.BDWidth/2 <= mouseX <= each.x+app.BDWidth/2 and
                each.y-app.BDHeight/2 <= mouseY <= each.y+app.BDHeight/2):
                    app.BDmode = not app.BDmode
                    if app.musicEffects:
                        app.buttonSound.play()
                    return

            if each.type == 'settings':
                if ((each.x-app.settingsWidth/2 <= mouseX <= each.x+app.settingsWidth/2) and
                        (each.y-app.settingsHeight/2 <= mouseY <= each.y+app.settingsHeight/2)):

                    app.showSettings = not app.showSettings
                    if app.musicEffects:
                        app.buttonSound.play()
                    return
            if each.type == 'instructions':
                if ((each.x<= mouseX <= each.x + app.instructionsWidth) and
                        (each.y<= mouseY <= each.y + app.instructionsHeight)):
                    app.showInstructions = not app.showInstructions
                    if app.musicEffects:
                        app.buttonSound.play()


            if (each.x <= mouseX <= each.x+app.buttonWidth and
                each.y <= mouseY <= each.y+app.buttonHeight):
                if each.type == 'mode':
                    app.currentMode = each.label
                    if app.musicEffects:
                        app.buttonSound.play()
                elif each.type == 'grid':
                    app.showGrid = not app.showGrid
                    if app.musicEffects:
                        app.buttonSound.play()
                elif each.type == 'tl':
                    app.showTlPanel = not app.showTlPanel
                    if app.musicEffects:
                        app.buttonSound.play()
                    return
                elif each.type == 'start':
                    app.paused = False
                    app.carNum = 0
                    if app.backgroundMusic:
                        if not app.paused:
                            app.soundBack.pause()
                            app.soundTraffic.play()
                        else:
                            app.soundTraffic.pause()
                            app.soundBack.play()
                    if app.musicEffects:
                        app.buttonSound.play()
                    if not app.initiated:
                        app.path = findUnpackedPaths(app,findPaths(app, app.roads[0], app.roads[1]))
                    app.initiated = True
                return

        if not app.showTlPanel:
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
                        for inter in app.roads[ind].intersections:
                            if inter.type.isdigit():
                                for interRoad in inter.roads:
                                    if (rounded(interRoad.points[1][0]) == rounded(road.points[1][0]) and
                                            rounded(interRoad.points[1][1]) == rounded(road.points[1][1])):
                                        inter.roads.remove(interRoad)

                        app.roads.pop(ind)
    elif app.showSettings:
        if (app.backgroundMusicButtonX-app.settingsButtonWidth/2 <= mouseX <=
                app.backgroundMusicButtonX+app.settingsButtonWidth*1.5 and
                app.backgroundMusicButtonY-app.settingsButtonHeight/2 <= mouseY <=
                app.backgroundMusicButtonY+app.settingsButtonHeight/2):
            if app.musicEffects:
                app.buttonSound.play()
            app.backgroundMusic = not app.backgroundMusic

            if app.backgroundMusic:
                if app.paused:
                    app.soundBack.play(loop=True)
                else:
                    app.soundTraffic.play(loop=True)
            else:
                app.soundBack.pause()

        elif (app.musicEffectsButtonX-app.settingsButtonWidth/2 <= mouseX <=
                app.musicEffectsButtonX+app.settingsButtonWidth*1.5 and
                app.musicEffectsButtonY-app.settingsButtonHeight/2 <= mouseY <=
                app.musicEffectsButtonY+app.settingsButtonHeight/2):
            if app.musicEffects:
                app.buttonSound.play()
            app.musicEffects = not app.musicEffects

        elif (app.carReprButtonX-app.settingsButtonWidth/2 <= mouseX <=
                app.carReprButtonX+app.settingsButtonWidth*1.5 and
                app.carReprButtonY-app.settingsButtonHeight/2 <= mouseY <=
                app.carReprButtonY+app.settingsButtonHeight/2):
            if app.musicEffects:
                app.buttonSound.play()
            app.carRepr = not app.carRepr

        elif (app.showPathButtonX-app.settingsButtonWidth/2 <= mouseX <=
                app.showPathButtonX+app.settingsButtonWidth*1.5 and
                app.showPathButtonY-app.settingsButtonHeight/2 <= mouseY <=
                app.showPathButtonY+app.settingsButtonHeight/2):
            if app.musicEffects:
                app.buttonSound.play()
            app.showPath = not app.showPath

        elif (870 <= mouseX <= 870+app.crossWidth and
                85 <= mouseY <= 85+app.crossHeight):
            if app.musicEffects:
                app.buttonSound.play()
            app.showSettings = False


    elif app.showInstructions:
        if app.overAllInstructions:
            if (app.overAllInstructionsNextButtonX-app.inrtruButtonWidth/2 <= mouseX <=
                app.overAllInstructionsNextButtonX+app.inrtruButtonWidth*1.5 and
                app.overAllInstructionsYButtonY-app.inrtruButtonHeight/2 <= mouseY <=
                app.overAllInstructionsYButtonY+app.inrtruButtonHeight/2):
                if app.musicEffects:
                    app.buttonSound.play()
                app.overAllInstructions = False
                app.roadDrawStraightInstructions = True
        if app.roadDrawStraightInstructions:
             if (app.roadDrawStraightPrevButtonX-app.inrtruButtonWidth/2 <= mouseX <=
                app.roadDrawStraightPrevButtonX+app.inrtruButtonWidth*1.5 and
                app.roadDrawStraightPrevButtonY-app.inrtruButtonHeight/2 <= mouseY <=
                app.roadDrawStraightPrevButtonY+app.inrtruButtonHeight/2):
                if app.musicEffects:
                     app.buttonSound.play()
                app.roadDrawStraightInstructions = False
                app.overAllInstructions = True
             elif (app.roadDrawStraightNextButtonX - app.inrtruButtonWidth / 2 <= mouseX <=
                    app.roadDrawStraightNextButtonX + app.inrtruButtonWidth * 1.5 and
                    app.roadDrawStraightNextButtonY - app.inrtruButtonHeight / 2 <= mouseY <=
                    app.roadDrawStraightNextButtonY + app.inrtruButtonHeight / 2):
                app.roadDrawStraightInstructions = False
                app.roadDrawCurvedInstructions = True
        if app.roadDrawCurvedInstructions:
            if (app.roadDrawCurvedPrevButtonX - app.inrtruButtonWidth / 2 <= mouseX <=
                    app.roadDrawCurvedPrevButtonX + app.inrtruButtonWidth * 1.5 and
                    app.roadDrawCurvedPrevButtonY - app.inrtruButtonHeight / 2 <= mouseY <=
                    app.roadDrawCurvedPrevButtonY + app.inrtruButtonHeight / 2):
                if app.musicEffects:
                    app.buttonSound.play()
                app.roadDrawCurvedInstructions = False
                app.roadDrawStraightInstructions = True
            elif (app.roadDrawCurvedNextButtonX - app.inrtruButtonWidth / 2 <= mouseX <=
                    app.roadDrawCurvedNextButtonX + app.inrtruButtonWidth * 1.5 and
                    app.roadDrawCurvedPrevButtonY - app.inrtruButtonHeight / 2 <= mouseY <=
                    app.roadDrawCurvedNextButtonY + app.inrtruButtonHeight / 2):
                if app.musicEffects:
                    app.buttonSound.play()
                app.roadDrawCurvedInstructions = False
                app.roadDrawBridgeInstructions = True
        if app.roadDrawBridgeInstructions:
            if (app.roadBridgePrevButtonX - app.inrtruButtonWidth / 2 <= mouseX <=
                    app.roadBridgePrevButtonX + app.inrtruButtonWidth * 1.5 and
                    app.roadBridgePrevButtonY - app.inrtruButtonHeight / 2 <= mouseY <=
                    app.roadBridgePrevButtonY + app.inrtruButtonHeight / 2):
                if app.musicEffects:
                    app.buttonSound.play()
                app.roadDrawBridgeInstructions = False
                app.roadDrawStraightInstructions = True
            elif (app.roadBridgeNextButtonX - app.inrtruButtonWidth / 2 <= mouseX <=
                    app.roadBridgeNextButtonX + app.inrtruButtonWidth * 1.5 and
                    app.roadBridgeNextButtonY - app.inrtruButtonHeight / 2 <= mouseY <=
                    app.roadBridgeNextButtonY + app.inrtruButtonHeight / 2):
                if app.musicEffects:
                    app.buttonSound.play()
                app.removeRoadInstructions = True
                app.roadDrawBridgeInstructions = False
        if app.removeRoadInstructions:
            if (app.removePrevButtonX - app.inrtruButtonWidth / 2 <= mouseX <=
                    app.removePrevButtonX + app.inrtruButtonWidth * 1.5 and
                    app.removePrevButtonY - app.inrtruButtonHeight / 2 <= mouseY <=
                    app.removePrevButtonY + app.inrtruButtonHeight / 2):
                if app.musicEffects:
                    app.buttonSound.play()
                app.removeRoadInstructions = False
                app.roadDrawBridgeInstructions = True
            elif (app.removeNextButtonX - app.inrtruButtonWidth / 2 <= mouseX <=
                    app.removeNextButtonX + app.inrtruButtonWidth * 1.5 and
                    app.removeNextButtonY - app.inrtruButtonHeight / 2 <= mouseY <=
                    app.removeNextButtonY + app.inrtruButtonHeight / 2):
                if app.musicEffects:
                    app.buttonSound.play()
                app.playInstructions = True
                app.removeRoadInstructions = False
        if app.playInstructions:
            if (app.playPrevButtonX - app.inrtruButtonWidth / 2 <= mouseX <=
                    app.playPrevButtonX + app.inrtruButtonWidth * 1.5 and
                    app.playPrevButtonY - app.inrtruButtonHeight / 2 <= mouseY <=
                    app.playPrevButtonY + app.inrtruButtonHeight / 2):
                if app.musicEffects:
                    app.buttonSound.play()
                app.removeRoadInstructions = True
                app.playInstructions = False
            elif (app.playNextButtonX - app.inrtruButtonWidth / 2 <= mouseX <=
                  app.playNextButtonX + app.inrtruButtonWidth * 1.5 and
                  app.playNextButtonY - app.inrtruButtonHeight / 2 <= mouseY <=
                  app.playNextButtonY + app.inrtruButtonHeight / 2):
                if app.musicEffects:
                    app.buttonSound.play()
                app.playInstructions = False
                app.showInstructions = False
                app.overAllInstructions = True
                if app.instruFromMenu:
                    app.instruFromMenu = False
                    setActiveScreen('intro')
                    resetPlay(app)



    if app.sessionFinished:
        if (app.returnMenuButtonX - app.resultsButtonWidth / 2 <= mouseX <=
                app.returnMenuButtonX + app.resultsButtonWidth * 1.5 and
                app.returnMenuButtonY - app.resultsButtonHeight / 2 <= mouseY <=
                app.returnMenuButtonY + app.resultsButtonHeight / 2):
            if app.musicEffects:
                app.buttonSound.play()
            saveInfo(app.username, app.diffLevel, app.score)
            resetPlay(app)
            intro_onAppStart(app)
            setActiveScreen('intro')

        elif (app.restartButtonX - app.resultsButtonWidth / 2 <= mouseX <=
                app.restartButtonX + app.resultsButtonWidth * 1.5 and
                app.restartButtonY - app.resultsButtonHeight / 2 <= mouseY <=
                app.restartButtonY + app.resultsButtonHeight / 2):
            if app.musicEffects:
                app.buttonSound.play()
            saveInfo(app.username, app.diffLevel, score)
            resetPlay(app)

def resetPlay(app):
    app.score = 0
    app.tlDuration = 30
    app.mouseX = 0
    app.mouseY = 0
    app.roadPreview = False
    app.roadOpacity = 100
    app.gridSize = 20
    app.roadWidth = 30
    app.laneMarkingInterval = 10
    app.showGrid = True
    app.roadsCoordinates = []
    for i in range(0, app.height, 4):
        row = []
        for j in range(0, app.width, 4):
            row.append(0)
        app.roadsCoordinates.append(row)
    top = []
    right = []
    down = []
    left = []
    app.roads = []

    for i in range(0, app.diffLevel):
        side = random.random() * 4
        # Left side of the screen
        if 0 <= side < 1:
            y = generateRadnBetween(140, 500) // 10 * 10
            for point in left:
                while abs(y - point) < 40:
                    y = generateRadnBetween(140, 500) // 10 * 10
            left.append(y)
            p1 = (0, y)
            p2 = (150, y)
            left.append(y)
            app.roads.append(Road('Straight', [p1, p2], 'Ground', True))
        # Top side
        elif 1 <= side < 2:
            x = generateRadnBetween(280, 760) // 10 * 10
            for point in top:
                while abs(x - point) < 40:
                    x = generateRadnBetween(280, 760) // 10 * 10
            top.append(x)
            p1 = (x, 0)
            p2 = (x, 150)
            app.roads.append(Road('Straight', [p1, p2], 'Ground', True))
        # Right side
        elif 2 <= side < 3:
            y = generateRadnBetween(180, 480) // 10 * 10
            for point in right:
                while abs(y - point) < 40:
                    y = generateRadnBetween(180, 480) // 10 * 10
            right.append(y)
            p1 = (app.width, y)
            p2 = (app.width - 150, y)
            app.roads.append(Road('Straight', [p1, p2], 'Ground', True))
        else:
            x = generateRadnBetween(180, 780) // 10 * 10
            for point in down:
                while abs(x - point) < 40:
                    x = generateRadnBetween(180, 780) // 10 * 10
            down.append(x)
            p1 = (x, app.height)
            p2 = (x, app.height - 150)
            app.roads.append(Road('Straight', [p1, p2], 'Ground', True))

    app.currentRoad = None

    app.modes = ['Straight', 'Curved']
    # default mode
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
    app.carImageWidth, app.carImageHeight = getImageSize(app.carImages[0])
    app.carImageWidth /= 18
    app.carImageHeight /= 18
    app.cars = []
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
    app.BDWidth = bdWidth / 4.8
    app.BDHeight = bdHeight / 4.8

    shovelURL = './sign/shovel.png'
    app.shovelImage = CMUImage(loadPilImage(shovelURL))

    app.palyPageOpacity = 100

    app.timeSpent = []
    app.aveTime = 'N/A'

    app.sessionFinished = False
    app.carNum = 0


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

                roadInd = checkIntersectsCurve(app)
                if roadInd!=None:
                    app.curveIntersects = True
                    app.roads[roadInd].highlighted = True

                else:
                    for road in app.roads:
                        road.highlighted = False
                    app.curveIntersects = False

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

                roadInd = checkIntersectsCurve(app)
                if roadInd != None:
                    app.curveIntersects = True
                    app.roads[roadInd].highlighted = True

                else:
                    for road in app.roads:
                        road.highlighted = False
                    app.curveIntersects = False

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

def instructionPanel(app,x,y,message,width=250,showPrev=True,showNext=True,type=None):
    lines = math.ceil(len(message)/(width//8))
    messageStartY = y+30
    textWidth = (width//8)
    height = (lines) * 30+50

    if type:
        height += 240
        drawRect(x, y, width, height, fill='powderBlue', border='cornflowerBlue', borderWidth=4)
        if type == 'straightRoad':
            imageWidth, imageHeight = getImageSize(app.imagesStraightRoad[0])
            drawImage(app.imagesStraightRoad[app.straightRoadImageInd],x+width/2,height-imageHeight//6-40,
                      width=imageWidth//5,height=imageHeight//5,align='top')
        elif type == 'curvedRoad':
            imageWidth, imageHeight = getImageSize(app.imagesCurvedRoad[0])
            drawImage(app.imagesCurvedRoad[app.curvedRoadImageInd], x + width / 2, height - imageHeight // 6 - 40,
                      width=imageWidth // 5, height=imageHeight // 5, align='top')
        elif type == 'bridge':
            imageWidth, imageHeight = getImageSize(app.imagesBridge[0])
            drawImage(app.imagesBridge[app.bridgeInd], x + width / 2, height - imageHeight // 6 - 70,
                      width=imageWidth // 5, height=imageHeight // 5, align='top')
        elif type == 'remove':
            imageWidth, imageHeight = getImageSize(app.imagesRemove[0])
            drawImage(app.imagesRemove[app.removeInd], x + width / 2, height - imageHeight // 6+65,
                      width=imageWidth // 5, height=imageHeight // 5, align='top')
        elif type == 'play':
            imageWidth, imageHeight = getImageSize(app.imagesPlay[0])
            drawImage(app.imagesPlay[app.playInd], x + width / 2, height - imageHeight // 6+45,
                      width=imageWidth // 5.5, height=imageHeight // 5.5, align='top')


    else:
        drawRect(x, y, width, height, fill='powderBlue', border='cornflowerBlue', borderWidth=4)


    for i in range(1,lines+1):
        drawLabel(message[(i-1)*textWidth:i*textWidth],x+20,messageStartY+(i-1)*30,size=15,align='left')

    if showPrev:
        prevButtonX = x + 30
        prevButtonY =messageStartY + height-80

        drawRect(prevButtonX,prevButtonY,app.inrtruButtonWidth,app.inrtruButtonHeight,fill='honeydew', border='cornflowerBlue', borderWidth=2)
        drawLabel('Prev', prevButtonX+app.inrtruButtonWidth/2,prevButtonY+app.inrtruButtonHeight/2,size=15,bold=True)

    if showNext:
        nextButtonX = x+width-120
        nextButtonY = messageStartY + height-80

        drawRect(nextButtonX, nextButtonY, app.inrtruButtonWidth, app.inrtruButtonHeight, fill='honeydew',
                 border='cornflowerBlue', borderWidth=2)
        drawLabel('Next', nextButtonX+app.inrtruButtonWidth/2,nextButtonY+app.inrtruButtonHeight/2, size=15, bold=True)




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
    if app.showPath:
        drawPaths(app)
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

    drawRect(800,20,180,130,opacity = 65,fill='white')
    drawLabel("Current elevation:", 890, 40, bold=True, size=15)
    drawLabel(app.currentElevation,890,65,size=20,bold=True)

    drawLabel("Average Time Spent:",890,100,bold=True,size = 15)
    drawLabel(app.aveTime, 890, 125, bold=True, size=20)

    if app.showSettings:
        drawSettings(app)
    if app.sessionFinished:
        drawResults(app)

    if app.curveIntersects:
        drawRect(15, 100, 300, 80, fill='powderBlue', border='cornflowerBlue', borderWidth=4)
        drawLabel("Curved roads can not",30,125,align='left',bold=True,size=20)
        drawLabel("intersects with other roads!",30,150,align='left',bold=True,size=20)

    if app.showInstructions:
        if app.overAllInstructions:
            instructionPanel(app, 250, 150,
                             "Welcome to TimeWise Transport!. In this game, your goal is to design an efficient road "+
                            'network that allows each car to reach its destination as quickly as possible. ' +
                             "Cars are generated   from different outlets on the screen, and each outlet also    serves as a destination. " +
                             "Your task is to connect these trafficoutlets by designing straight roads, curved roads, and bridges" +
                             "Let's get started! Click 'Next' to learn how to draw straight roads.",500,False,True)
        if app.roadDrawStraightInstructions:
            instructionPanel(app, 130, 60,
                             "To draw straight roads, please elect the 'Straight' road mode from the toolbar. " +
                             "Click on the canvas where you want the road to start. " +
                             "Click again at the desired end point to complete the straight road. " +
                             "The road will automatically align to the grid for precision. " +
                             "Please ensure that roads are spaced adequately to prevent traffic congestion.", 500, True,
                             True,'straightRoad')
        if app.roadDrawCurvedInstructions:
            instructionPanel(app, 130, 60,
                             "To draw curved roads, please elect the 'Curved' road mode fromthe toolbar. " +
                             "Click on the canvas to set the starting point of the curve. " +
                             "Then click at the midpoint where you want the curve to bend. " +
                             "Click once more at the end point to complete the    curved road."
                             , 500, True,
                             True,'curvedRoad')
        if app.roadDrawBridgeInstructions:
            instructionPanel(app, 310, 20,
                             "To create a bridge, select the Straight or Curved road mode   and click once on the "+
                             "canvas to connect your road to a ground-level road. Press the 'Up' key to elevate the road "+
                             "to bridge  level, then continue drawing the bridge as usual. "+
                             "To connect  the bridge back to the ground, switch to Bridge mode, click   the desired starting point, "+
                             "and press the 'Down' key to lower the road back to ground level and click the desired end point."
                             , 500, True,
                             True,'bridge')
        if app.removeRoadInstructions:
            instructionPanel(app, 130, 160,
                             "To remove a road, select the 'Bulldoze' mode from the toolbar." +
                             "Hover over the road segment you wish to remove. The selected  road will be highlighted. "+
                             "Click on the highlighted road to    remove it from your network."
                             , 500, True,
                             True,'remove')
        if app.playInstructions:
            instructionPanel(app, 500, 120,
                             "Once you have designed your road network, click the 'Start'   button to begin the simulation. " +
                             "Cars will start generating from the outlets and will navigate through your network to reach their destinations"
                             , 500, True,
                             True,'play')
        if app.justCome:
            drawRect(0, 0, app.width, app.height, fill='white', opacity=app.palyPageOpacity)



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
    #check if the session should be ended
    if app.counter//20 == 20:
        if isinstance(app.aveTime, str):
            app.score = 0
        else:
            app.score = app.diffLevel * 100 + app.carNum * app.diffLevel * 50 - app.aveTime * 10
        app.sessionFinished = True
        app.paused = True
        if app.backgroundMusic:
            app.soundTraffic.pause()
            app.soundBack.play()

    if app.roadsChanged:
        findIntersections(app)
        app.edgeIntersections = findEdgeIntersections(app)
        app.roadsChanged = False

    if app.roadDrawStraightInstructions:
        app.straightRoadImageInd = (app.straightRoadImageInd + 1) % len(app.imagesStraightRoad)
    if app.roadDrawCurvedInstructions:
        app.curvedRoadImageInd = (app.curvedRoadImageInd + 1) % len(app.imagesCurvedRoad)
    if app.roadDrawBridgeInstructions:
        app.bridgeInd = (app.bridgeInd + 1) % len(app.imagesBridge)
    if app.removeRoadInstructions:
        app.removeInd = (app.removeInd + 1) % len(app.imagesRemove)
    if app.playInstructions:
        app.playInd = (app.playInd + 1) % len(app.imagesPlay)

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
            for x, y in collisionBox:
                drawCircle(x, y, 2)
def drawResults(app):
    drawRect(160, 100, app.width - 320, app.height - 200, fill='powderBlue', border='cornflowerBlue', borderWidth=4)
    drawLabel(f"{app.username}, you did it!",200,app.height - 450,size=40,bold=True,align='left')
    drawLabel("Over the course of 90s, you let", 200, app.height - 390, size=20,bold=True,align='left')
    drawLabel(f'{app.carNum} cars', 220, app.height - 350, size=40, bold=True,align='left')
    drawLabel('safely reached their destinations, with the average time spent:', 200, app.height - 290, size=20, bold=True,align='left')
    drawLabel(f'{app.aveTime} s!', 220, app.height - 250, size=40, bold=True,align='left')


    drawLabel('Your score is: ',670, 140, size=20, bold=True)
    drawLabel(f'{app.score}', 675, 200, size=40, bold=True)



    drawRect(app.returnMenuButtonX + app.resultsButtonWidth - 2, app.returnMenuButtonY,
             app.resultsButtonWidth,
             app.resultsButtonHeight, align='center', fill='honeydew', border='cornflowerBlue', borderWidth=4)
    drawLabel('Return to menu', app.returnMenuButtonX + app.resultsButtonWidth - 2, app.returnMenuButtonY, bold=True,
              size=20)

    drawRect(app.restartButtonX + app.resultsButtonWidth - 2, app.restartButtonY,
             app.resultsButtonWidth,
             app.resultsButtonHeight, align='center', fill='honeydew', border='cornflowerBlue', borderWidth=4)
    drawLabel('Restart', app.restartButtonX + app.resultsButtonWidth - 2, app.restartButtonY, bold=True,
              size=20)

#############
#Learned this from:
#https://www.geeksforgeeks.org/reading-writing-text-files-python/
#############
def saveInfo(userName,diffLevel,score):
    saved = open('savedInfo.txt','a')
    saved.write(f"{userName} {diffLevel} {score}\n")



def drawSettings(app):
    drawRect(60,60,app.width-120,app.height-120,fill='powderBlue',border='cornflowerBlue',borderWidth=4)
    drawImage(app.crossImage,870,85,width = app.crossWidth,height=app.crossHeight)

    drawLabel("Settings",180,120,bold = True,size=40,fill='midnightBlue')
    drawLabel("Background music:", 190, 200, bold=True, size=25,fill='midnightBlue',align='left')
    drawLabel("Music effects:", 190, 260, bold=True, size=25, fill='midnightBlue',align='left')
    drawLabel("Car representation:", 190, 320, bold=True, size=25, fill='midnightBlue', align='left')
    drawLabel("Show car path:", 190, 380, bold=True, size=25, fill='midnightBlue', align='left')

    if app.backgroundMusic:
        bgMOnButtonColor = 'lightSteelBlue'
        bgMOffButtonColor = 'honeydew'
    else:
        bgMOnButtonColor = 'honeydew'
        bgMOffButtonColor = 'lightSteelBlue'

    drawRect(app.backgroundMusicButtonX,app.backgroundMusicButtonY,app.settingsButtonWidth,app.settingsButtonHeight,
             align='center',fill = bgMOnButtonColor,border='cornflowerBlue',borderWidth=4)
    drawLabel('ON',app.backgroundMusicButtonX,app.backgroundMusicButtonY,bold=True,size=20)

    drawRect(app.backgroundMusicButtonX+app.settingsButtonWidth-2, app.backgroundMusicButtonY, app.settingsButtonWidth,
             app.settingsButtonHeight, align='center', fill=bgMOffButtonColor,border='cornflowerBlue', borderWidth=4)
    drawLabel('OFF', app.backgroundMusicButtonX+app.settingsButtonWidth-2, app.backgroundMusicButtonY, bold=True, size=20)


    if app.musicEffects:
        musicEffectsOnButtonColor = 'lightSteelBlue'
        musicEffectsOffButtonColor = 'honeydew'
    else:
        musicEffectsOnButtonColor = 'honeydew'
        musicEffectsOffButtonColor = 'lightSteelBlue'

    drawRect(app.musicEffectsButtonX,app.musicEffectsButtonY,app.settingsButtonWidth,app.settingsButtonHeight,
             align='center',fill = musicEffectsOnButtonColor,border='cornflowerBlue',borderWidth=4)
    drawLabel('ON',app.musicEffectsButtonX,app.musicEffectsButtonY,bold=True,size=20)

    drawRect(app.musicEffectsButtonX+app.settingsButtonWidth-2, app.musicEffectsButtonY, app.settingsButtonWidth,
             app.settingsButtonHeight, align='center', fill=musicEffectsOffButtonColor,border='cornflowerBlue', borderWidth=4)
    drawLabel('OFF', app.musicEffectsButtonX+app.settingsButtonWidth-2, app.musicEffectsButtonY, bold=True, size=20)

    if app.carRepr:
        carReprOnButtonColor = 'lightSteelBlue'
        carReprOffButtonColor = 'honeydew'
    else:
        carReprOnButtonColor = 'honeydew'
        carReprOffButtonColor = 'lightSteelBlue'

    drawRect(app.carReprButtonX,app.carReprButtonY,app.settingsButtonWidth,app.settingsButtonHeight,
             align='center',fill = carReprOnButtonColor,border='cornflowerBlue',borderWidth=4)
    drawLabel('ON',app.carReprButtonX,app.carReprButtonY,bold=True,size=20)

    drawRect(app.carReprButtonX+app.settingsButtonWidth-2, app.carReprButtonY, app.settingsButtonWidth,
             app.settingsButtonHeight, align='center', fill=carReprOffButtonColor,border='cornflowerBlue', borderWidth=4)
    drawLabel('OFF', app.carReprButtonX+app.settingsButtonWidth-2, app.carReprButtonY, bold=True, size=20)


    if app.showPath:
        showPathOnButtonColor = 'lightSteelBlue'
        showPathOffButtonColor = 'honeydew'
    else:
        showPathOnButtonColor = 'honeydew'
        showPathOffButtonColor = 'lightSteelBlue'

    drawRect(app.showPathButtonX,app.showPathButtonY,app.settingsButtonWidth,app.settingsButtonHeight,
             align='center',fill = showPathOnButtonColor,border='cornflowerBlue',borderWidth=4)
    drawLabel('ON',app.showPathButtonX,app.showPathButtonY,bold=True,size=20)

    drawRect(app.showPathButtonX+app.settingsButtonWidth-2, app.showPathButtonY, app.settingsButtonWidth,
             app.settingsButtonHeight, align='center', fill=showPathOffButtonColor,border='cornflowerBlue', borderWidth=4)
    drawLabel('OFF', app.showPathButtonX+app.settingsButtonWidth-2, app.showPathButtonY, bold=True, size=20)

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
            each.type == 'start' and not app.paused or
            each.type == 'tl' and app.showTlPanel) :
            color = 'lightBlue'
        else:
            color = 'white'


        if each.type == 'BD':
            drawImage(app.bdImage, each.x, each.y, width=app.BDWidth, height=app.BDHeight,
                      align='center')
            drawLabel(each.label, each.x + app.BDWidth / 2, each.y + app.BDHeight / 2, size=12)
        elif each.type == 'settings':
            drawImage(app.settingsImage, each.x, each.y, width=app.settingsWidth, height=app.settingsHeight,
                      align ='center')
            drawLabel(each.label, each.x + app.settingsWidth / 2, each.y + app.settingsHeight / 2, size=12)
        elif each.type == 'instructions':
            drawImage(app.instructionsImage, each.x, each.y, width=app.instructionsWidth,height = app.instructionsHeight)
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
                print(i)
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

    print(i)

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
            numSteps = 20
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