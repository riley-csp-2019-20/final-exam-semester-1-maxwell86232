#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#Maxwell Martinez
#Date
#12/18/2019


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl
import random as rand

#create turtle
sketch = trtl.Turtle()
sketch.pensize(5)
sketch.turtlesize(2)

#make a color list
color_list = ["red","blue","green","yellow","purple","orange"]

#define movement
def sketchup():
    sketch.setheading(90)
    sketch.forward(10)
def sketchright():
    sketch.setheading(0)
    sketch.forward(10)
def sketchdown():
    sketch.setheading(270)
    sketch.forward(10)
def sketchleft():
    sketch.setheading(180)
    sketch.forward(10)
def boardclear():
    sketch.clear()

#define penup/pendown
def sketchpenup():
    sketch.penup()
def sketchpendown():
    sketch.pendown()

#define pensize
def sketchpenincrease():
    sketch.pensize(5)
def sketchpendecrease():
    sketch.pensize(3)

#define color
def randomcolor():
    sketch.pencolor(color_list)

#create screen
wn = trtl.Screen()

#bind to keypresses
wn.onkeypress(sketchup,"Up")
wn.onkeypress(sketchright,"Right")
wn.onkeypress(sketchdown,"Down")
wn.onkeypress(sketchleft,"Left")
wn.onkeypress(boardclear,"space")
wn.onkeypress(sketchpenup,"u")
wn.onkeypress(sketchpendown,"i")
wn.onkeypress(sketchpenincrease,"p")
wn.onkeypress(sketchpendecrease,"o")
wn.onkeypress(randomcolor,"y")

#listen
wn.listen()

#mainloop
wn.mainloop()