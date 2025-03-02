#Jadan Carleton
#Saturday, March 1st, 2025

#Problem 4: Unique
#This program takes a list of numbers and returns a new list containing
#all numbers from the original list, with any duplicate numbers removed.

def unique(oldList):
    newList = []

    for num in oldList:
        if num not in newList:
            newList.append(num)

    return newList


sampleList = [1, 3, 3, 3, 6, 2, 3, 5]

print("Here is the list " + str(sampleList) + " with all duplicates removed: " + str(unique(sampleList)))
