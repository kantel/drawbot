from random import random, randint

WIDTH = 1000
HEIGHT = 800
lmargin =  20  # unterer Rand und Rand links
umargin = 100  # oberer Rand und Rand rechts
nRects  = 100   # Anzahl der Rechtecke
size(WIDTH, HEIGHT)
fill(235/255.0, 215/255.0, 182/255.0) # Hintergrundfarbe Packpapier
rect(0, 0, width(), height())

for _ in range(nRects):
    r, g, b, a = randint(100, 220)/255.0, randint(20, 150)/255.0, randint(20, 200)/255.0, 0.7
    x, y, w, h = randint(lmargin, width() - umargin), randint(lmargin, height() - umargin), randint(lmargin, umargin), randint(lmargin, umargin)
    stroke(0)
    fill(r, g, b, a)
    rect(x, y, w, h)

print("I did it, Babe!")