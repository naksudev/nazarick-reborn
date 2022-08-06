from classes.character import Character
from functions.battle import *

def main():
    player = Character("Naksu", 100, 25, 10, 10, [])
    ennemy = Character("Slime", 50, 15, 5, 10, [])

    battle(player, ennemy)

if __name__ == '__main__':
        main()