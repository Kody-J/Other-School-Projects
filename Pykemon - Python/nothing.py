import os
import csv
import random



class Creature(object):
    """ creates creatures and battles them """
    def __int__(self, name: str, hp: int, dmg: int, attack_type: str, weakness: str):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.attack_type = attack_type
        self.weakness = weakness

def user_display(user):
    """ Display to the user their Pokedex"""
    while True:
        try:
            print("Please choose 1 of {} Pokemon from your hand".format(len(user)))
            nbr = 0
            for pokemon in user:
                usr_pokedex = "{}. {:<11} ({}) - {}".format(nbr, pokemon[0], pokemon[1], pokemon[4][1].upper())
                print(usr_pokedex)
                nbr += 1
            war_lord = input("===> ")
            while int(war_lord)!= 0 and int(war_lord)!= 1 and int(war_lord)!= 2:
                print("You must enter a valid choice of 0,1 or 2")
                war_lord = input("===> ")
            return user.pop(int(war_lord))
        except ValueError:
            print("Use number keys only\n")
