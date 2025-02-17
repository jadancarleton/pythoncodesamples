#Jadan Carleton
#Sunday, February 16th, 2025

#This program draws a randomly-colored multicolor spiral


import turtle
import random

#set up the turtle
wn = turtle.Screen()
spiral = turtle.Turtle()

#set turtle speed and initial length
spiral.speed(0)
distance = 0

for i in range(125):

    #extend length and change color to random
    distance = distance + 5
    spiral.pencolor(random.random(), random.random(), random.random())

    #move and rotate turtle
    spiral.forward(distance)
    spiral.left(90)

spiral.hideturtle()

