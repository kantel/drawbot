# Hommage an Kasimir Malewitsch

from random import randint

WIDTH, HEIGHT = 480, 640
lmargin = 40   # unterer Rand und Rand links
umargin = 100  # oberer Rand und Rand rechts
nIter   = 30   # Anzahl der Shapes
a = 0.85       # Alpha (Transparenz)

# Farbpalette
malPal = [(42/255.0, 40/255.0, 45/255.0),
          (160/255.0, 51/255.0, 46/255.0),
          (54/255.0, 50/255.0, 80/255.0),
          (50/255.0, 80/255.0, 105/255.0),
          (180/255.0, 144/255.0, 55/255.0),
          (215/255.0, 158/255.0, 40/255.0),
          (140/255.0, 82/255.0, 48/255.0)]
          
def makeFillColor(color, a):
    r = color[0]
    g = color[1]
    b = color[2]
    fill(r, g, b, a)

def drawRect():
    x = randint(lmargin, width() - umargin)
    y = randint(lmargin, height() - umargin)
    w = randint(lmargin, umargin)
    h = randint(lmargin, umargin)
    rect(x, y, w, h)

def drawCircle():
    x = randint(lmargin, width() - umargin)
    y = randint(lmargin, height() - umargin)
    r = randint(15, 50)
    oval(x, y, r, r)
    
size(WIDTH, HEIGHT)
# Hintergrundfarbe (Packpapier)
bgColor = (230/255.0, 226/255.0, 204/255.0)
makeFillColor(bgColor, 1)
rect(0, 0, width(), height())

for _ in range(nIter):
    rand = randint(0, 100)
    if rand < 30:
        stroke(0)
        strokeWidth(1)
        makeFillColor(malPal[randint(0, 1)], a)
        if randint(0, 100) > 50:
            drawRect()
        else:
            drawCircle()
    elif rand < 85:
        makeFillColor(malPal[randint(2, 5)], a)
        drawRect()
    else:
        strokeR = malPal[6][0]
        strokeG = malPal[6][1]
        strokeB = malPal[6][2]
        strokeWidth(randint(4, 8))
        stroke(strokeR, strokeG, strokeB)
        makeFillColor(bgColor, a)
        drawCircle()
        stroke(0)
        strokeWidth(1)
            
print("I did it, Babe!")