#Jadan Carleton
#Saturday, February 1st, 2025

#This program calculates what number day a holiday will end



startday = int(input("Hello! What day will you be leaving for your holiday? (Please enter a number between 0 and 6, assuming 0 means Sunday and 6 means Saturday)"))

length = int(input("And how many nights will your holiday last?"))

endday = (startday + length) % 7

print("Your holiday will end on day number " + str(endday) + " of the week! Have a good trip!")
