# import random

size(300, 300)
for x in range(10):
  for y in range(10):
    print(x, y)
    fill(x/10, y/10, 0.5)
    if random() > 0.5:
      rect(30*x, 30*y, 20, 20)
    else:
      oval(30*x, 30*y, 20, 20)