from random import randint

WIDTH, HEIGHT = 640, 400
malewitsch = [(42/255.0, 40/255.0, 45/255.0),
              (160/255.0, 51/255.0, 46/255.0),
              (54/255.0, 50/255.0, 80/255.0),
              (50/255.0, 80/255.0, 105/255.0),
              (180/255.0, 144/255.0, 55/255.0),
              (215/255.0, 158/255.0, 40/255.0),
              (140/255.0, 82/255.0, 48/255.0)]
                        
a = 0.6       # Alpha (Transparenz)
numCircles = 200

def makeFillColor(color, a):
    r = color[0]
    g = color[1]
    b = color[2]
    fill(r, g, b, a)


size(WIDTH, HEIGHT)
# Hintergrundfarbe (Packpapier)
bgColor = (230/255.0, 226/255.0, 204/255.0)
makeFillColor(bgColor, 1)
rect(0, 0, width(), height())

strokeWidth(1)
for _ in range(numCircles):
    x = randint(50, WIDTH - 50)
    y = randint(50, HEIGHT - 50)
    stroke(0)            # Schwarzer Rand
    makeFillColor(malewitsch[(randint(0, len(malewitsch) -1))], 1.0)
    d = 6.               # Durchmesser
    r = d//2.            # Radius
    oval(x - r, y - r, d, d)
    stroke(0, 0.0)       # no stroke
    makeFillColor(malewitsch[(randint(0, len(malewitsch) -1))], a)
    d = randint(20, 60)  # Durchmesser
    r = d//2.            # Radius
    oval(x - r, y - r, d, d)

print("I did it, Babe!")