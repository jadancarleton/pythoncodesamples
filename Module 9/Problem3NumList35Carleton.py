#Jadan Carleton
#Saturday, March 15th, 2025

#This program uses a while loop to repeatedly ask the user to input
#a number, and appends a list to add that number. The program only
#stops when the sum of the list is greater than 100.


L = []
LSum = 0

while LSum < 101:
    usernumber = int(input("Please enter a number here: "))
    L.append(usernumber)
    LSum = sum(L)


print("Finished! The sum of your list is: " + str(LSum))
