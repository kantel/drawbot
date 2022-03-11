from random import random

size = 600

def tiling(x, y, s, l):
    if l == 0:
        if random() < 0.5:
            line((x, y-s), (x, y+s))
        else:
            line((x-s, y), (x+s, y))
    else:
        s /= 2
        l -= 1
        tiling(x-s, y+s, s, l)
        tiling(x+s, y+s, s, l)
        tiling(x-s, y-s, s, l)
        tiling(x+s, y-s, s, l)

newPage(width = 700, height = 700)
# size(300, 200)
stroke(0)
strokeWidth(2)
with savedState():
    # translate(x = 80, y = 80)
    tiling(0, 0, size, 6)

# print(x, y)
print("I did it Babe!")