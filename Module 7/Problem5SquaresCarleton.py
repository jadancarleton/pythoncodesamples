#Jadan Carleton
#Saturday, March 1st, 2025

#Problem 5: Squares

#This program uses a pre-built drawSquare function to draw 5 concentric
#squares as its output.

import turtle

def drawSquare(t, sz):
    #Get turtle t to draw a square of sz side
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

#set initial side length
sideLength = 30

#loop for each square
for i in range(5):
    #draw square and increment side length
    drawSquare(alex, sideLength)
    sideLength = sideLength + 20

    #relocate turtle for the beginning of the next square
    alex.penup()
    alex.setheading(270)
    alex.forward(10)
    alex.setheading(180)
    alex.forward(10)
    alex.setheading(0)
    alex.pendown()





wn.exitonclick()
