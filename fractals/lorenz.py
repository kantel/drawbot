# Lorenz-Attraktor

WIDTH, HEIGHT = 640, 400

b = 8.0/3
r = 40.0
sigma = 10.0
dt = 0.001
t = 0.0
maxi = 75.0   # Max Iteration
x = y = 0.01
z = 0.0

size(WIDTH, HEIGHT)
# Hintergrundfarbe
stroke(0, 0, 0)
rect(0, 0, width(), height())

strokeWidth(1)
while (t < maxi):
    colorStep = 1.0/maxi
    stroke(t, t*colorStep, 0)
    dx = -sigma*(x - y)*dt
    dy = (x*(r - z) - y)*dt
    dz = (x*y - b*z)*dt
    x += dx
    y += dy
    z += dz
    # auf Fenstergröße skalieren
    xx = (x*8) + WIDTH//2
    # Y braucht eine Sonderbehandlung: XY
    yy = HEIGHT//2 - (y*4)
    # Y braucht eine Sonderbehandlung: YZ
    # yy = HEIGHT - 50 - (y*8) 
    zz =  40 + (z*4)
    if t == 0.0:
        # XY
        line((xx, yy), (xx, yy))
        # XZ
        # line((xx, zz), (xx, zz))
        # YZ
        # line((yy, zz), (yy, zz))
    else:
        # XY
        line((oldX, oldY), (xx, yy)) 
        # XZ
        # line((oldX, oldZ), (xx, zz))
        # YZ
        # line((oldY, oldZ), (yy, zz))      
    oldX = xx
    oldY = yy
    oldZ = zz
    t += dt
    
# Als PNG sichern
saveImage("lorenz.png")
print("I did it, Babe!")
    
    
