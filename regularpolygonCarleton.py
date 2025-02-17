#Jadan Carleton
#Sunday, February 16th, 2025

#This program draws a regular polygon with user selected number of sides,
#side length, color, and fill color.


import turtle

sides = int(input("Hello! Please enter the number of sides in your polygon: "))
side_length = int(input("Now, enter the side length of your polygon: "))
color = input("Now, please enter your polygon's side color as a six-digit hexcode: ")
fill_color = input("Finally, please enter your polygon's fill color as a six-digit hexcode: ")


turn_angle = 360 / sides


wn = turtle.Screen()
poly = turtle.Turtle()

poly.speed(2)
poly.up()
poly.goto(0 - side_length/2, 0 - side_length/2)
poly.down()

poly.color("#" + color)
poly.fillcolor("#" + fill_color)

poly.begin_fill()

for i in range(sides):
    poly.forward(side_length)
    poly.left(turn_angle)

poly.end_fill()

poly.hideturtle()

