from cmu_graphics import  *
from drawHelpers import *
from cars import*
from roadDrawHelpers import *
from roadCalculations import *

from objects import *
from practicalFunctions import *
import math
import random


import resource

def increase_file_limit():
    soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    print(f"Current limits: soft={soft}, hard={hard}")
    try:
        # Define new soft and hard limits
        new_soft = 4096
        new_hard = hard if hard >= 4096 else 4096

        resource.setrlimit(resource.RLIMIT_NOFILE, (new_soft, new_hard))
        print(f"New limits: soft={new_soft}, hard={new_hard}")
    except ValueError as e:
        print(f"Failed to set file limits: {e}")
    except resource.error as e:
        print(f"Resource error: {e}")


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
    increase_file_limit()
    soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    print(f"After increase: soft={soft}, hard={hard}")
    app.instruFromMenu = False
    app.width = 1000
    app.height = 600
    app.username = ''
    app.diffLevel = 4

    crossURL = '../assets/sign/cross.png'
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

    app.soundBack = Sound('../assets/music/bgm.mp3')
    if app.backgroundMusic:
        app.soundBack.play(loop=True)
    else:
        app.soundBack.pause()

    app.buttonSound = Sound('../assets/music/button.mp3')
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

    app.imageUrlsStraightRoad = [f'../assets/instructions/straightRoad/ezgif-frame-00{i}.jpg' for i in range(1, 10)]
    app.imageUrlsStraightRoad += [f'../assets/instructions/straightRoad/ezgif-frame-0{i}.jpg' for i in range(10, 100)]
    app.imageUrlsStraightRoad += [f'../assets/instructions/straightRoad/ezgif-frame-{i}.jpg' for i in range(100, 111)]
    app.imagesStraightRoad = [Image.open(url) for url in app.imageUrlsStraightRoad]
    app.imagesStraightRoad = [CMUImage(image) for image in app.imagesStraightRoad]
    app.straightRoadImageInd = 0


    app.imageUrlsBridge = [f'../assets/instructions/bridge/ezgif-frame-00{i}.jpg' for i in range(1, 10)]
    app.imageUrlsBridge += [f'../assets/instructions/bridge/ezgif-frame-0{i}.jpg' for i in range(10, 100)]
    app.imageUrlsBridge += [f'../assets/instructions/bridge/ezgif-frame-{i}.jpg' for i in range(100, 201)]
    app.imagesBridge = [Image.open(url) for url in app.imageUrlsBridge]
    app.imagesBridge = [CMUImage(image) for image in app.imagesBridge]
    app.bridgeInd = 0


    app.imageUrlsCurvedRoad = [f'../assets/instructions/curvedRoad/ezgif-frame-00{i}.jpg' for i in range(1, 10)]
    app.imageUrlsCurvedRoad += [f'../assets/instructions/curvedRoad/ezgif-frame-0{i}.jpg' for i in range(10, 46)]
    app.imageUrlsCurvedRoad += [f'../assets/instructions/curvedRoad/ezgif-frame-{i}.jpg' for i in range(100, 142)]
    app.imagesCurvedRoad = [Image.open(url) for url in app.imageUrlsCurvedRoad]
    app.imagesCurvedRoad = [CMUImage(image) for image in app.imagesCurvedRoad]
    app.curvedRoadImageInd = 0


    app.imageUrlsRemove = [f'../assets/instructions/remove/ezgif-frame-00{i}.jpg' for i in range(1, 10)]
    app.imageUrlsRemove += [f'../assets/instructions/remove/ezgif-frame-0{i}.jpg' for i in range(10, 46)]
    app.imagesRemove = [Image.open(url) for url in app.imageUrlsRemove]
    app.imagesRemove = [CMUImage(image) for image in app.imagesRemove]
    app.removeInd = 0


    app.imageUrlsPlay = [f'../assets/instructions/play/ezgif-frame-00{i}.jpg' for i in range(1, 10)]
    app.imageUrlsPlay += [f'../assets/instructions/play/ezgif-frame-0{i}.jpg' for i in range(10, 100)]
    app.imageUrlsPlay += [f'../assets/instructions/play/ezgif-frame-{i}.jpg' for i in range(100, 201)]
    app.imagesPlay = [Image.open(url) for url in app.imageUrlsPlay]
    app.imagesPlay = [CMUImage(image) for image in app.imagesPlay]
    app.playInd = 0
    app.ranking = []
    print(app.imageUrlsPlay)

def intro_onAppStart(app):
    introURL = '../assets/backgrounds/intro.jpg'
    app.introImage = CMUImage(loadPilImage(introURL))

    buttonURL = '../assets/button/button1.png'
    app.buttonImage = CMUImage(loadPilImage(buttonURL))

    titleURL = '../assets/title/title.png'
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




def history_onAppStart(app):
    backButtonWidth = 100
    backButtonHeight = 40
    backButtonX = 20
    backButtonY = app.height - backButtonHeight - 20
    app.backButton = Button('back', "Back", backButtonX, backButtonY, backButtonWidth, backButtonHeight)
    app.currOnButton = None

    introURL = '../assets/backgrounds/intro.jpg'
    app.introImage = CMUImage(loadPilImage(introURL))

    titleHistoryURL = '../assets/title/history.png'
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
    file = open("../savedInfo.txt", "r")
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
    showBoxURL = '../assets/button/diffSel.png'
    app.showBoxImage = CMUImage(loadPilImage(showBoxURL))

    plusURL = '../assets/button/plus.png'
    app.plusImage = CMUImage(loadPilImage(plusURL))

    minusURL = '../assets/button/minus.png'
    app.minusImage = CMUImage(loadPilImage(minusURL))

    titleDFURL = '../assets/title/diffTitle.png'
    app.titleDFImage = CMUImage(loadPilImage(titleDFURL))

    titleDFLevelURL = '../assets/title/diffLevel.png'
    app.DFLevelImage = CMUImage(loadPilImage(titleDFLevelURL))

    titleUSRURL = '../assets/title/username.png'
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

    app.carURLs = [f'../assets/cars/{i}.png' for i in range(0, 3)]
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

    bulldozeURL = '../assets/sign/bz.png'
    app.bdImage = CMUImage(loadPilImage(bulldozeURL))
    bdWidth, bdHeight = getImageSize(app.bdImage)
    app.BDmode = False
    app.BDWidth = bdWidth/4.8
    app.BDHeight = bdHeight/4.8



    shovelURL = '../assets/sign/shovel.png'
    app.shovelImage = CMUImage(loadPilImage(shovelURL))


    app.palyPageOpacity = 100

    app.timeSpent=[]
    app.aveTime = 'N/A'

    settingURL = '../assets/sign/settings.png'
    app.settingsImage = CMUImage(loadPilImage(settingURL))
    settingsWidth, settingsHeight = getImageSize(app.settingsImage)
    app.settingsWidth = settingsWidth / 16.3
    app.settingsHeight = settingsHeight / 16.3

    instructionsURL = '../assets/sign/instructions.png'
    app.instructionsImage = CMUImage(loadPilImage(instructionsURL))
    instructionsWidth, instructionsHeight = getImageSize(app.instructionsImage)
    app.instructionsWidth = instructionsWidth / 7.5
    app.instructionsHeight = instructionsHeight / 7.5

    app.soundTraffic = Sound('../assets/music/traffic.mp3')

    controlBarURL = '../assets/control/bar.png'
    app.barImage = CMUImage(loadPilImage(controlBarURL))
    barWidth, barHeight = getImageSize(app.barImage)
    app.barWidth = barWidth / 6
    app.barHeight = barHeight / 10

    controlBallURL = '../assets/control/bar1.png'
    app.ballImage = CMUImage(loadPilImage(controlBallURL))
    ballWidth, ballHeight = getImageSize(app.ballImage)
    app.ballWidth = ballWidth / 8
    app.ballHeight = ballHeight / 8

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
    app.controlBallX = 350

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
            not app.showInstructions):
        app.roads = sortRoadsElevation(app)
        if app.isDrawing or app.currentMode and not app.showTlPanel:
            app.roadsChanged = True
            app.edgeIntersections = findEdgeIntersections(app)


        #if clcked again, then draw the road
        if (app.isDrawing and app.currentMode != None and not app.BDmode
                and not app.showTlPanel and app.paused):

            mappedX, mappedY = int(app.cursorX),int(app.cursorY)
            if app.currentMode == 'Straight':

                #if we already have an end points
                if len(app.currentRoad.points) == 2:
                    for road in app.roads:
                        if road.highlighted:
                            return
                    app.roads.append(app.currentRoad)
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

        if not app.showTlPanel and app.paused:
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
            saveInfo(app.username, app.diffLevel, app.score)
            resetPlay(app)

def resetPlay(app):
    app.score = 0
    app.tlDuration = 30
    app.showTlPanel = False
    app.controlBallX = 350
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

    app.carURLs = [f'../assets/cars/{i}.png' for i in range(0, 3)]
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
    if app.showTlPanel:
        drawTlPanel(app)



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


def play_onMouseDrag(app,mouseX,mouseY):
    if 280 < mouseX < 430:
        app.controlBallX = mouseX

        app.tlDuration = int((mouseX-350)/3.5 + 30)

        print(app.tlDuration)

#############
#Learned this from:
#https://www.geeksforgeeks.org/reading-writing-text-files-python/
#############
def saveInfo(userName,diffLevel,score):
    saved = open('../savedInfo.txt','a')
    saved.write(f"{userName} {diffLevel} {score}\n")

def main():
    runAppWithScreens(initialScreen='intro')

main()