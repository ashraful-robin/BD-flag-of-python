"""
	
	This is only for windows. If you are not really like to run in windows, then try to ignore the line 'import winsound' and then it will be work properly.
	I know I am a raw coder. But some times I feel safe with python. 

	This is a simple python file only. I just write the codes for learnig nothing else. 

"""

import winsound
import turtle
f = turtle.Pen()

#   stand part....
f.color('black')
f.begin_fill()
f.right(90)
f.forward(200)
f.left(90)
f.forward(4)
f.left(90)
f.forward(400)
f.left(90)
f.forward(4)
f.left(90)
f.forward(200)
f.end_fill()
#   Box/Rectangular part ....
f.up()
f.back(200)
f.left(90)
f.down()
f.color('black', 'green')
f.begin_fill()
f.forward(174)
f.right(90)
f.forward(80)
f.right(90)
f.forward(170)
f.right(90)
f.forward(80)
f.end_fill()

#   Circle Portion .... 
f.up()
f.right(90)
f.forward(57)
f.right(90)
f.forward(37)
f.down()
f.color('red')
f.begin_fill()
f.circle(30)
f.end_fill()

#   Music Part ...
winsound.PlaySound("nSong.wav",winsound.SND_FILENAME)

