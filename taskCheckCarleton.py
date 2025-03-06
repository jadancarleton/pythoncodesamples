#Jadan Carleton
#Wednesday, March 5th, 2025

#Problems 5, 6, 7: Task Checks
#This program checks whether a game character is able to complete
#three different tasks, based on possessed items and debuffs, and prints
#the results for each task.


class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self. weaknesses

    def profile(self):
        return self.nickname, self.weapons, self. weaknesses


player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']

player2 = character('','','')
player2.nickname = 'Gary'
player2.weapons = ['pan', 'groceries', 'coat', 'rope', 'first aid kit', 'pen', 'paper', 'idea']
player2.weaknesses = ['small']


def canClimbMountain(player):
    hasRope = False
    hasCoat = False
    hasFirstAidKit = False
    isSlow = False

    for weapon in player.weapons:
        if weapon == "rope":
            hasRope = True
        if weapon == "coat":
            hasCoat = True
        if weapon == "first aid kit":
            hasFirstAidKit = True
            
    for weakness in player.weaknesses:
        if weakness == "slow":
            isSlow = True

    if hasRope == True and hasCoat == True and hasFirstAidKit == True:
        if isSlow == False:
            print(player.nickname + " is able to climb the mountain!")
        else:
            print(player.nickname + " is NOT able to climb the mountain.")
    else:
        print(player.nickname + " is NOT able to climb the mountain.")


def canCookMeal(player):
    hasPan = False
    hasGroceries = False
    isSmall = False

    for weapon in player.weapons:
        if weapon == "pan":
            hasPan = True
        if weapon == "groceries":
            hasGroceries = True
            
    for weakness in player.weaknesses:
        if weakness == "small":
            isSmall = True

    if hasPan == True and hasGroceries == True:
        if isSmall == False:
            print(player.nickname + " is able to cook a meal!")
        else:
            print(player.nickname + " is NOT able to cook a meal.")
    else:
        print(player.nickname + " is NOT able to cook a meal.")


def canWriteBook(player):
    hasPen = False
    hasPaper = False
    hasIdea = False
    hasConfusion = False

    for weapon in player.weapons:
        if weapon == "pen":
            hasPen = True
        if weapon == "paper":
            hasPaper = True
        if weapon == "idea":
            hasIdea = True
            
    for weakness in player.weaknesses:
        if weakness == "confusion":
            hasConfusion = True

    if hasPen == True and hasPaper == True and hasIdea == True:
        if hasConfusion == False:
            print(player.nickname + " is able to write a book!")
        else:
            print(player.nickname + " is NOT able to write a book.")
    else:
        print(player.nickname + " is NOT able to write a book.")


canClimbMountain(player1)
canClimbMountain(player2)


canCookMeal(player1)
canCookMeal(player2)

canWriteBook(player1)
canWriteBook(player2)
