#Jadan Carleton
#Thursday, February 20th, 2025

#Problem 5: Degrees
#This program converts an angle measure from radians to degrees,
#uses the math module to make the same conversion,
#and prints both results.

import math

radians = float(input("Please enter your angle measure in radians: "))
degrees = (radians/math.pi)*180

print("By my calculations, " + str(radians) + " radians is about " + str(degrees) + " degrees!")

print("The math module calculates " + str(radians) + " radians is about " + str(math.degrees(radians)) + " degrees.")



