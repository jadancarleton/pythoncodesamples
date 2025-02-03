#Jadan Carleton
#Saturday, February 1st, 2025

#This program asks the user for their name
#and greets them only if their name is Jadan Carleton or Nathan Braun



firstname = input("Please enter your first name here:")

lastname = input("Please enter your last name here:")


if firstname == "Jadan" and lastname == "Carleton":

    print("Hello, " + firstname + " " + lastname + "! It is great to see you!")
    
elif firstname == "Nathan" and lastname == "Braun":

    print("Hello, Professor " + lastname + "! It is great to see you!")

else:
    
    print("You are not an authorized user.")

