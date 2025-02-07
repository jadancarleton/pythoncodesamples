#Jadan Carleton
#Saturday, February 1st, 2025

#This program converts a temperature from Fahrenheit to Celsius.



tempf = float(input("Please enter a temperature in degrees Fahrenheit: "))

tempc = round(((tempf - 32) / 1.8), 1)

print(str(tempf) + " degrees Fahrenheit is equal to about " + str(tempc) + " degrees Celsius!")
