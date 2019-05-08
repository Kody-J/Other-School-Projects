import graphics as gfx
import time
import random


color_str = ["Blue", "Red", "Green"]
color = random.choice(color_str)
question_cnt = 0


win = gfx.GraphWin("My UI", 300, 300)
text = gfx.Text(gfx.Point(150,150), "Click to begin")
text.draw(win)
win.getMouse()
text.undraw()


### count down to begin ###
for i in range(5 ,0, -1):
    cnt_dwn = gfx.Text(gfx.Point(150,150), i)
    cnt_dwn.draw(win)
    time.sleep(1)
    cnt_dwn.undraw()

while question_cnt != nbr:
    start_time = time.time()
    
    

win.close()

