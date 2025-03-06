#Jadan Carleton
#Tuesday, March 4th, 2025

#Problem 4: Leap Year
#This program contains a function that checks whether a given year
#is a leap year.

#function that checks if a year is a leap year
def leapYear(year):
    intYear = int(year)
    
    if intYear % 4 == 0:
        if intYear % 100 == 0:
            if intYear % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


        
#prompt the user to input a year
userYear = input("Please input a year to check if it is a leap year: ")

#use leapYear function with user year
print(leapYear(userYear))
