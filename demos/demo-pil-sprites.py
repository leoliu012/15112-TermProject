# Here is the sprites demo from the CMU Graphics docs:
# https://academy.cs.cmu.edu/cpcs-docs/images_and_sounds

# This version is different -- it downloads a single spritesheet and
# uses PIL's crop method to extract each individual frame.

# This version also runs more smoothly in the desktop version of CMU Graphics.

# Note: this uses a spritestrip from this tutorial:
# https://www.codeandweb.com/texturepacker/tutorials/how-to-create-a-sprite-sheet

from cmu_graphics import *
from urllib.request import urlopen
from PIL import Image

def onAppStart(app):
    url = 'https://www.cs.cmu.edu/~112-f24/notes/tp-related-demos/sample-spritestrip.png'
    spritePilImages = loadSpritePilImages(url)
    app.spriteCmuImages = [CMUImage(pilImage) for pilImage in spritePilImages]
    app.spriteIndex = 0
    app.stepsPerSecond = 7

def loadPilImage(url):
    # Loads a PIL image (not a CMU image!) from a url:
    return Image.open(urlopen(url))

def loadSpritePilImages(url):
    spritestrip = loadPilImage(url)
    spritePilImages = [ ]
    for i in range(6):
        spriteImage = spritestrip.crop((30+260*i, 30, 230+260*i, 250))
        spritePilImages.append(spriteImage)
    return spritePilImages

def onStep(app):
    app.spriteIndex = (app.spriteIndex + 1) % len(app.spriteCmuImages)

def onKeyPress(app, key):
    if key in ['up', 'right']:
        app.stepsPerSecond += 1
    elif key in ['down', 'left'] and app.stepsPerSecond > 1:
        app.stepsPerSecond -= 1

def redrawAll(app):
    drawLabel('Sprite Demo', 200, 20, size=16)
    drawLabel('Press up/down to go faster/slower', 200, 40, size=16)
    drawLabel(f'app.stepsPerSecond = {app.stepsPerSecond}', 200, 60, size=16)
    drawImage(app.spriteCmuImages[app.spriteIndex], 200, 200, align='center')

def main():
    runApp()

main()