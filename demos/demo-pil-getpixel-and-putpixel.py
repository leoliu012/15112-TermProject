from cmu_graphics import *
from urllib.request import urlopen
from PIL import Image

# This demos PIL getpixel and putpixel.

def loadPilImage(url):
    # Loads a PIL image (not a CMU image!) from a url:
    return Image.open(url)

def onAppStart(app):
    # 1. Load a PIL image from a url:
    url = '/Users/xinruil3/PycharmProjects/15112-TermProject/cars/1.png'
    pilImage1 = loadPilImage(url)

    # 2. Create a new PIL image that only uses the red parts of the
    #    RGB colors in the first image:
    pilImage2 = getRedParts(pilImage1)

    # 3. Convert from PIL images to CMU images before drawing:
    app.cmuImage1 = CMUImage(pilImage1)
    app.cmuImage2 = CMUImage(pilImage2)

def getRedParts(pilImage1):
    rbgImage1 = pilImage1.convert('RGB')
    pilImage2 = Image.new(mode='RGB', size=rbgImage1.size)
    for x in range(rbgImage1.width):
        for y in range(rbgImage1.height):
            r,g,b = rbgImage1.getpixel((x,y))
            pilImage2.putpixel((x,y),(r,0,0))
    return pilImage2

def redrawAll(app):
    drawImage(app.cmuImage1, 200, app.height/2, align='center')
    drawImage(app.cmuImage2, 500, app.height/2, align='center')

def main():
    runApp(width=700, height=600)

main()