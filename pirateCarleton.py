#Jadan Carleton
#Friday, February 7th, 2025

#This program asks a potential pirate for a password
#rejects them if they are a pirate
#and welcomes them if they are not a pirate

greeting = input("Hello, possible pirate! What's the password?")

if greeting in ["Arrr!"]:
	print("Go away, pirate.")
else:
    print("Greetings, hater of pirates!")
