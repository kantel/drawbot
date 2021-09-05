from random import choice

riley1 = [(4/255, 21/255, 31/255), (1/255, 155/255, 183/255),
          (226/255, 107/255, 67/255), (60/255, 76/255, 97/255),
          (144/255, 166/255, 215/255), (240/255, 192/255, 68/255)]
          
marginh = 18
marginw = 10
gridsize_x = 25
gridsize_y = 21
WIDTH = 640
HEIGHT = 480
seconds = 5 # 60 bei MP4, 5 bei GIF
fps = 5
duration = 1/fps
total_frames = seconds*fps

def animate():
    newPage(WIDTH, HEIGHT)
    frameDuration(duration)
    fill(240/255, 245/255, 248/255)
    rect(0, 0, width(), height())
    for x in range(gridsize_x):
      for y in range(gridsize_y):
        riley = choice(riley1)  
        r = riley[0]
        g = riley[1]
        b = riley[2]
        fill(r, g, b)
        if random() > 0.5:
          rect(gridsize_x*x + marginw, gridsize_y*y + marginh, 20, 20)
        else:
          oval(gridsize_x*x + marginw, gridsize_y*y + marginh, 20, 20)

for _ in range(total_frames):
    animate()
      
# saveImage("images/riley2.mp4")
saveImage("images/riley2.gif", imageGIFLoop = True)
print("I did it, Babe!")