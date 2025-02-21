#Jadan Carleton
#Thursday, February 20th, 2025

#Problem 6: Factorial
#This program calculates the factorial of an integer,
#uses the math module to make the same calculation,
#and prints both results.

import math

number = int(input("Please enter a positive integer: "))

total = 1

for i in range(number):
    total = total*(i+1)

print("I calculate that the factorial of " + str(number) + " is equal to " + str(total))

print("The math module calculates that the factorial of " + str(number) + " is equal to " + str(math.factorial(number)))
