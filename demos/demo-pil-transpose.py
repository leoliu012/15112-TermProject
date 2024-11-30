from cmu_graphics import *
from urllib.request import urlopen
from PIL import Image

# This demos PIL transpose, which (non-mutatingly) flips an image in
# various ways.  Here, we flip horizontally.  See the PIL docs for more.

def loadPilImage(url):
    # Loads a PIL image (not a CMU image!) from a url:
    return Image.open(urlopen(url))

def onAppStart(app):
    # 1. Load a PIL image from a url:
    url = 'https://tinyurl.com/great-pitch-gif'
    pilImage1 = loadPilImage(url)

    # 2. Create a new PIL image that is the transpose of the original:
    pilImage2 = pilImage1.transpose(Image.FLIP_LEFT_RIGHT)

    # 3. Convert from PIL images to CMU images before drawing:
    app.cmuImage1 = CMUImage(pilImage1)
    app.cmuImage2 = CMUImage(pilImage2)

def redrawAll(app):
    drawImage(app.cmuImage1, 200, app.height/2, align='center')
    drawImage(app.cmuImage2, 500, app.height/2, align='center')

def main():
    runApp(width=700, height=600)

main()