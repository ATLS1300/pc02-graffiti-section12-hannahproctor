#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.penup()

turtle.goto(-35,108)

turtle.fillcolor("DeepPink")

turtle.begin_fill()

turtle.circle(20)

turtle.end_fill()

turtle.clear()

turtle.right(60)

turtle.circle(20)

turtle.begin_fill()

turtle.circle(20)

turtle.end_fill()

turtle.penup()

turtle.right(20)

turtle.left(60)

turtle.left(20)

turtle.left(10)

turtle.forward(20)

turtle.forward(20)

turtle.left(60)

turtle.left(30)

turtle.forward(20)

turtle.backward(10)

turtle.right(60)

turtle.right(15)

turtle.right(5)

turtle.right(6)

turtle.backward(5)

turtle.backward(3)

turtle.forward(6)

turtle.color("black")

turtle.pendown()

turtle.forward(20)

turtle.forward(20)

turtle.backward(7)

turtle.undo()

turtle.undo()

turtle.forward(15)

turtle.penup()

turtle.right(60)

turtle.right(20)

turtle.pendown()

turtle.fillcolor("DarkCyan")

turtle.begin_fill()

turtle.circle(20)

turtle.end_fill()

turtle.undo()

turtle.undo()

turtle.right(30)

turtle.penup()

turtle.forward(10)

turtle.pendown()

turtle.begin_fill()

turtle.circle(20)

turtle.end_fill()

turtle.clear()

turtle.penup()

turtle.goto(-35,108)

turtle.pendown()

turtle.begin_fill()

turtle.circle(20)

turtle.end_fill()

turtle.penup()

turtle.right(80)

turtle.left(160)

turtle.left(30)

turtle.forward(30)

turtle.forward(15)

turtle.backward(10)

turtle.forward(2)

turtle.color("black")

turtle.pendown()

turtle.forward(20)

turtle.forward(3)

turtle.forward(2)

turtle.forward(2)

turtle.forward(2)

turtle.penup()

turtle.right(60)

turtle.right(20)

turtle.forward(4)

turtle.pendown()

turtle.fillcolor("DeepPink")

turtle.begin_fill()

turtle.circle(20)

turtle.end_fill()

turtle.penup()

turtle.goto(-35,108)

turtle.left(60)

turtle.left(160)

turtle.left(7)

turtle.pendown()

turtle.forward(15)

turtle.undo()

turtle.left(10)

turtle.forward(30)

turtle.forward(20)

turtle.penup()

turtle.goto(-25,108)

turtle.forward(20)

turtle.forward(15)

turtle.right(60)

turtle.forward(30)

turtle.forward(20)

turtle.right(70)

turtle.forward(10)

turtle.right(90)

turtle.right(20)

turtle.right(10)

turtle.right(10)

turtle.pendown()

turtle.forward(20)

turtle.forward(30)

turtle.undo()

turtle.forward(20)

turtle.penup()

turtle.left(160)

turtle.forward(30)

turtle.forward(6)

turtle.left(70)

turtle.left(20)

turtle.left(20)

turtle.left(60)

turtle.left(20)

turtle.forward(10)

turtle.right(20)

turtle.right(30)

turtle.right(30)

turtle.right(10)

turtle.pendown()

turtle.forward(30)

turtle.penup()

turtle.goto(0,0)

turtle.goto(111,-90)

turtle.pensize(8)

turtle.right(160)

turtle.forward(5)

turtle.pendown()

turtle.color("DarkMagenta")

turtle.forward(30)

turtle.undo()

turtle.color("azure4")

turtle.forward(30)

turtle.penup()

turtle.backward(30)

turtle.color("AliceBlue")

turtle.forward(7)

turtle.pendown()

turtle.forward(7)

turtle.undo()

turtle.penup()

turtle.backward(5)

turtle.backward(7)

turtle.pendown()

turtle.forward(10)

turtle.penup()

turtle.goto(33,190)

turtle.forward(200)

turtle.forward(30)

turtle.right(160)

turtle.forward(20)

turtle.forward(20)

turtle.pendown()

turtle.color("DarkGoldenrod1")

turtle.circle(10)

turtle.undo()

turtle.circle(30)

turtle.penup()

turtle.forward(40)

turtle.right(10)

turtle.right(10)

turtle.right(10)

turtle.pendown()

turtle.forward(15)

turtle.penup()

turtle.right(160)

turtle.right(60)

turtle.forward(30)

turtle.forward(30)

turtle.right(60)

turtle.right(30)

turtle.right(30)

turtle.forward(15)

turtle.left(10)

turtle.left(10)

turtle.pendown()

turtle.forward(15)

turtle.penup()

turtle.right(90)

turtle.right(150)

turtle.forward(50)

turtle.left(30)

turtle.left(90)

turtle.right(30)

turtle.forward(30)

turtle.right(60)

turtle.right(60)

turtle.forward(15)

turtle.pendown()

turtle.forward(15)

turtle.penup()







#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
