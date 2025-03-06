#Jadan Carleton
#Tuesday, March 4th, 2025

#Problem 1: Equality
#This program contains a function which takes two inputs
#and prints whether or not they are equal.

#function that determines equality
def isEqual(input1, input2):
    if input1 == input2:
        print("These two inputs are equal!")
    else:
        print("These two inputs are not equal!")


#prompt the user to input 2 values
userInput1 = input("Please input your first value: ")
userInput2 = input("Please input your second value: ")

#use equality function with user values
isEqual(userInput1, userInput2)
