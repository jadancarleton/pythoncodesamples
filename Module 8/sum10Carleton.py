#Jadan Carleton
#Tuesday, March 4th, 2025

#Problem 2: Sum 10
#This program takes two values from a user and determines
#if their sum is greater than, equal to, or less than 10

#function that compares the sum of 2 inputs to 10
def isSum10(input1, input2):
    inputSum = float(input1) + float(input2)

    if inputSum < 10:
        print("These two numbers have a sum less than 10!")
    elif inputSum == 10:
        print("These two numbers have a sum equal to 10!")
    else:
        print("These two numbers have a sum greater than 10!")


#prompt the user to input 2 values
userInput1 = input("Please input a number: ")
userInput2 = input("Please input another number: ")

#use sum10 function with user values
isSum10(userInput1, userInput2)
