from cmu_graphics import *
from PIL import Image, ImageDraw

# This demos creating a new blank image and using PIL ImageDraw.

def makePilImage(imageWidth, imageHeight, bgColor):
    # Creates a new PIL image with the given bgColor:
    return Image.new('RGB', (imageWidth, imageHeight), bgColor)

def drawSomeLines(pilImage):
    # For more info on ImageDraw, see:
    # https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
    draw = ImageDraw.Draw(pilImage)
    imageWidth, imageHeight = pilImage.size
    draw.line((0, 0, imageWidth, imageHeight), width=10, fill=(255, 0, 0)) # red
    draw.line((0, imageHeight, imageWidth, 0), width=10, fill=(0, 0, 255)) # blue

def onAppStart(app):
    # 1. Create a new PIL image (not from a url):
    bgColor = (0, 255, 255) # rgb for cyan
    pilImage1 = makePilImage(app.width//3, app.height//2, bgColor)

    # 2. Draw some lines in the image:
    drawSomeLines(pilImage1)

    # 3. Create a new PIL image that is 2/3 sized:
    imageWidth, imageHeight = pilImage1.size
    pilImage2 = pilImage1.resize((imageWidth*2//3, imageHeight*2//3))

    # 4. Convert from PIL images to CMU images before drawing:
    app.cmuImage1 = CMUImage(pilImage1)
    app.cmuImage2 = CMUImage(pilImage2)

def redrawAll(app):
    drawImage(app.cmuImage1, 200, app.height/2, align='center')
    drawImage(app.cmuImage2, 500, app.height/2, align='center')

def main():
    runApp(width=700, height=600)

main()