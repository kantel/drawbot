from random import choice

riley1 = [(4/255, 21/255, 31/255), (1/255, 155/255, 183/255),
          (226/255, 107/255, 67/255), (60/255, 76/255, 97/255),
          (144/255, 166/255, 215/255), (240/255, 192/255, 68/255)]
          
margin = 5
gridsize = 30
size(900, 900)

fill(240/255, 245/255, 248/255)
rect(0, 0, width(), height())

for x in range(gridsize):
  for y in range(gridsize):
    riley = choice(riley1)  
    r = riley[0]
    g = riley[1]
    b = riley[2]
    fill(r, g, b)
    if random() > 0.5:
      rect(gridsize*x + margin, gridsize*y + margin, 20, 20)
    else:
      oval(gridsize*x + margin, gridsize*y + margin, 20, 20)
      
saveImage("images/riley1.pdf")
print("I did it, Babe!")