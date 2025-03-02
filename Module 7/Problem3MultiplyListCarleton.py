#Jadan Carleton
#Saturday, March 1st, 2025

#Problem 3: Multiply List
#This program contains a function that takes a list of numbers
#and calculates the product of the entire list

def multiplyList(numbers):

    total = 1
    
    for num in numbers:
        total = total * num

    return total



sampleList = [5, 2, 7, -1]

print("The product of this list: " + str(sampleList) + " is equal to: " + str(multiplyList(sampleList)))
