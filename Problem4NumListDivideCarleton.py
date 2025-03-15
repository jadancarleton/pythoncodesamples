#Jadan Carleton
#Saturday, March 15th, 2025

#This program runs a while loop with a counter from 0 to 50.
#When the counter is divisible by 10, it is added to a list called tens.
#Finally, the list is printed.

tens = []
counter = 0

while counter < 51:
    if counter % 10 == 0:
        tens.append(counter)
    counter = counter + 1

print(tens)
