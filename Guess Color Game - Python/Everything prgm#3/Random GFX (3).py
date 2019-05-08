import graphics as gfx
import time
import random


win = gfx.GraphWin("My UI", 300, 300)
text = gfx.Text(gfx.Point(150,150), "Click to begin")
text.draw(win)
win.getMouse()
text.undraw()

colors = ["Blue", "Red", "Green"]
color_str = random.choice(colors)
color_str.setOutline('Blue')
question = gfx.Text(gfx.Point(150,150), color_str)
question.draw(win)
answer = win.getKey()
