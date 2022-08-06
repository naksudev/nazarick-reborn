from random import * 
import keyboard
from tabulate import tabulate

def battle(player, ennemy):
    showsBattleDetails(player, ennemy)

    while (player.health > 0.99 and ennemy.health > 0.99):
        # RNG Speed taken from character's origin speed
        playerspeed = randint(0, player.speed)
        ennemyspeed = randint(0, ennemy.speed)

        # Choose an action before clase (RNG for ennemy's choice)
        playerChoice = chooseActionPlayer()
        ennemyChoice = chooseActionEnnemy() 

        # Clash
        if (playerspeed > ennemyspeed):
            if (playerChoice == 1):
                player.dealDamage(ennemy)
            elif (playerChoice == 2):
                player.defend()

            if (ennemyChoice == 1):
                ennemy.dealDamage(player)
            elif (ennemyChoice == 2):
                ennemy.defend()

            showsBattleDetails(player, ennemy)
        elif (playerspeed < ennemyspeed):
            if (ennemyChoice == 1):
                ennemy.dealDamage(player)
            elif (ennemyChoice == 2):
                ennemy.defend()

            if (playerChoice == 1):
                player.dealDamage(ennemy)
            elif (playerChoice == 2):
                player.defend()

            showsBattleDetails(player, ennemy)
        else:
            print("==============================")
            print("You two attacked at the same time !")
            print("==============================")
    
    # Victory/Fail message
    if (player.health < 0):
        print("💥 You lose..")
    else:
        print("🎊 You won !")

def chooseActionPlayer():
        print("Choose an action")
        choice = int(input("1/ Attack\n2/ Defend\n>> "))

        return choice

def chooseActionEnnemy():
        choice = randint(1, 2)

        return choice

def showsBattleDetails(player, ennemy):
    print("==============================")
    print(tabulate([["Health : {:.0f} ❤".format(player.health), "Health : {:.0f} ❤".format(ennemy.health)], 
                    ["Attack : {:} ⚔".format(player.attack), "Attack : {:} ⚔".format(ennemy.attack)], 
                    ["Defense : {:} 🛡".format(player.defense), "Defense : {:} 🛡".format(ennemy.defense)], 
                    ["Speed : {:} ⚡".format(player.speed), "Speed : {:} ⚡".format(ennemy.speed)]], 
                    [player.name, ennemy.name], tablefmt="plain"))
    print("==============================")