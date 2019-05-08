import graphics as gfx
import time
import random


color_str = ["Blue", "Red", "Green"]
color = random.choice(color_str)


win = gfx.GraphWin("My UI", 300, 300)
text = gfx.Text(gfx.Point(150,150), "CLick to begin")
text.draw(win)
win.getMouse()
text.undraw()

cnt_dwn = time.time()
for i in range(5 ,0, -1):
    #time.sleep(1)
    nums = gfx.Text(gfx.Point(150,150), i)
    nums.draw(win)
    time.sleep(1)
    nums.undraw()


win.close()

