#Jadan Carleton
#Sunday, February 16th, 2025

#This program prints the numbers 1-50
#and replaces those that are divisible by 3 or 5


for i in range(50):
    
    num = i + 1
    
    if(num%3 == 0 and num%5 == 0):
        print("Divisible by both")
        
    elif(num%3 == 0):
        print("Divisible by three")
        
    elif(num%5 == 0):
        print("Divisible by five")
        
    else:
        print(num)

