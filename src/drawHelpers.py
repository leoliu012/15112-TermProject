#####################################################
## Author: Xinrui (Leo) Liu
## CMU 2024 15-112 Term Project
## Section: K
#####################################################

from cmu_graphics import  *
import math


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


def drawResults(app):
    drawRect(160, 100, app.width - 320, app.height - 200, fill='powderBlue', border='cornflowerBlue', borderWidth=4)
    drawLabel(f"{app.username}, you did it!",200,app.height - 450,size=40,bold=True,align='left')
    drawLabel("Over the course of 60s, you let", 200, app.height - 390, size=20,bold=True,align='left')
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

def drawTlPanel(app):
    drawRect(250, 50, 200, 100, fill='powderBlue', border='cornflowerBlue', borderWidth=4)
    drawLabel("Traffic Lights Duration:", 345, 75, size=15, bold=True)
    drawImage(app.barImage, 350, 100, width=app.barWidth, height=app.barHeight, align='center')
    drawImage(app.ballImage, app.controlBallX, 100, width=app.ballWidth, height=app.ballHeight, align='center')
    drawLabel("Short", 280, 120, size=12, bold=True)
    drawLabel("Medium", 350, 120, size=12, bold=True)
    drawLabel("Long", 420, 120, size=12, bold=True)


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
