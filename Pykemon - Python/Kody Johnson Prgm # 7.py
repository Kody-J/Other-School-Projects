1##################################################################################################################
## CS 101
## PROGRAM 7
##
## 
## CREATIONDATE: 20-22 APR 2017
## 
##
##
##  PROBLEM:
##          CREATE A GAME WHICH MAKES CREATURES OUT OF A CSV FILE WITH CREATURE INFORMATION.
##          ASK THE USER IF THEY WISH TO PLAY THE GAME AND GIVE THEM THE OPTION TO QUIT
##          EACH PYMON CREATURE HAS ATTRIBUTS LIKE HEALTH, DAMAGE, AND WEAKNESS. THE USER WILL GET
##          3 PYMON CREATURES TO BATTLE AGAINST THE AI WITH 3 SEPERATE PYMON. THE BATTLE WILL
##          GO BACK AND FORTH TILL A VICTOR IS DETERMINED
##
##  ALGORITHM:
##          F: Create a function which greets the user and asks for input.
##                F1: Ask user to input if they would like to “Play” against the AI or “Quit” the game.
##                    F1.1 Check if user input is valid: input is either 1 (to play a game) or “Q”
##                    (quit the program)
##                    F1.1a: If user input is 1 or Q:
##                        F1.1aa Accept user input
##                    F1.1b: If user input is NOT = to 1 or Q:
##                        F1.1ba: Warn User
##                        F1.1bb: Repeat to F1 until valid input is received
##            O: If the user input = 1:
##                O1: open Pymon CSV File
##                O2: Iterate CSV file and save contents for in a list or dic, etc… 
##                O3: Close CSV file
##
##            C: Create a class/ object for the Pymon creatures:
##            C1: Based on CSV file, randomly assign three Pokémon from the CSV file to user and computer
##                C1.1: Assign specific attributes to each Pymon 
##                     C1.1a: Attribute 1 = name
##                     C1.1b: Attribute 2 = hit points (hp)
##                     C1.1c: Attribute 3 = damage (dmg)
##                     C1.1d: Attribute 4 = attack type (The damage type that will be done (blade, fire, Ice)
##                     C1.1e: Attribute 5 = weakness (If attacking Pymon type matches weakness, attackers
##                                            dmg does double)
##            C2: Create a string method:
##                C2.1: Return a string representation of creature instance:
##                    C2.1a: Pymon 1 = (name, hp, dmg, attack type, weakness)
##
##            C3: Create an attack method:
##                C3.1: For each instance of battle:
##                    C3.1a:  Attacking Pokmen randomly generates an attack which does random damamge within
##                            range of attackers dmg pts.
##                    C3.1b: Deduct damage from defenders hp:
##                    C3.1c: Display and update creature information after each attack:
##                        C3.1ca: If defender Pymon hp < 1:
##                            C3.1.1caa: End instance of attack
##
##        F2: Create a Function which allows the user to choose which Pymon to battle:
##            F2.1: If the first battle instance hasn’t occurred:
##                F2.1a: Allow the user to select (0,1, or 3) for which Pymon to battle
##                    F2.1aa: If user input = 0, 1, or 3 remove creature from user creature list and accept
##                            user input:
##                F2.1b: If user input not 0, 1, or 3:
##                    F2.1ba: Warn user 
##                    F2.1bb: repeat F2.1a
##            F2.2: If user Pymon has been knocked out:
##                F2.2a: Allow user to select one of remaining Pymon to battle:
##                    F2.2aa: If user input = to one of the remaining Pymon, accept user input
##                F2.2b: If user input not = to one of the remaining Pymon:
##                    F2.2ba: Warn user
##                    F2.2bb: Repeat F2.2a:
##    F3: Create a function which displays end results and repeats to F:
##      Q: If user input = Q:
##        Q1: End Program
#######################################################################################################################

import os
import csv
import random
class Creature(object):
    """ creates creatures and battles them """
    def __init__(self, name: str, hp: int, dmg: int, attack_type: str, weakness: str):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.attack_type = attack_type
        self.weakness = weakness

    def user_display(self):
        """ Display to the user their Pykedex in a specific order """
        while True:
            try:
                print("\nPlease choose 1 of {} Pokemon from your hand".format(len(user_pykedex)))
                nbr = 0
                for pykemon in user_pykedex:
                    user_pykedex_display = "{}. {:<10} ({}) - {}".format(nbr, pykemon[0], pykemon[1], pykemon[4][1].upper())
                    print(user_pykedex_display)
                    nbr += 1
                war_lord = input("===> ")
                while int(war_lord)!= 0 and int(war_lord)!= 1 and int(war_lord)!= 2:
                    print("You must enter a valid choice of 0,1 or 2")
                    war_lord = input("===> ")
                return user_pykedex.pop(int(war_lord))
            except ValueError:
                print("Use number keys only\n")
            except IndexError:
                print("\nYou must choose 0 or 1")

    def battle_royale(self, victim):
        """ This is the battle portion of the game. An attacker will be chosen at random\
            then a battle will ensue in an alternating fashion. Each instance of attack\
            will give a random dmg no greater than the cratures highest dmg rating. If the\
            victim has a weakness that matches the attackers type, all dmg will reduce the\
            victims hp by x2. Other wise the hp will be deducted by the dmg amount till one\
            of the pokemon hp is 0. All the information will be displayed in real time as it\
            occurs. """
        battle = True
        while battle == True:
            random_attack = random.randint(1, self.dmg)
            if self.attack_type == victim.weakness:
                random_attack = random_attack * 2
            victim.hp = victim.hp - random_attack
            if self == user_pykemon: 
                battle_report = "(Player) {} ({})- {} does {} pt(s) of {} damage to {} ({})- {}".format(self.name, self.hp, self.attack_type[0].upper(), random_attack, self.attack_type, victim.name, victim.hp, victim.attack_type[0].upper())
                print(battle_report)
            elif self == ai_pykemon:
                battle_report = "(AI) {} ({})- {} does {} pt(s) of {} damage to {} ({})- {}".format(self.name, self.hp, self.attack_type[0].upper(), random_attack, self.attack_type, victim.name, victim.hp, victim.attack_type[0].upper())
                print(battle_report)
            if victim.hp < 1 and victim == user_pykemon:
                print("\nYour {} ({}) - was beaten by the ai {} ({}) - {}".format(victim.name, victim.hp, self.name, self.hp, self.attack_type[0].upper()))
                battle = False
                return self
            elif victim.hp < 1 and victim == ai_pykemon:
                print("\nYour {} ({}) - was Victorious over the ai {} ({}) - {}".format(self.name, self.hp, victim.name, victim.hp, victim.name[0].upper()))
                return self

            ### every thing above, just in reverse order, creating an alternating attack order ###
            random_attack = random.randint(1, victim.dmg)
            if victim.attack_type == self.weakness:
                random_attack = random_attack * 2
            self.hp = self.hp - random_attack
            if victim == user_pykemon: 
                battle_report = "(Player) {} ({})- {} does {} pt(s) of {} damage to {} ({})- {}".format(victim.name, victim.hp, victim.attack_type[0].upper(), random_attack, victim.attack_type, self.name, self.hp, self.attack_type[0].upper())
                print(battle_report)
            elif victim == ai_pykemon:
                battle_report = "(AI) {} ({})- {} does {} pt(s) of {} damage to {} ({})- {}".format(victim.name, victim.hp, victim.attack_type[0].upper(), random_attack, victim.attack_type, self.name, self.hp, self.attack_type[0].upper())
                print(battle_report)
            if self.hp < 1 and self == user_pykemon:
                print("\nYour {} ({}) - was beaten by the ai {} ({}) - {}".format(self.name, self.hp, victim.name, victim.hp, victim.attack_type[0].upper()))
                return victim
            elif self.hp < 1 and self == ai_pykemon:
                print("\nYour {} ({}) - was Victorious over the ai {} ({}) - {}".format(victim.name, victim.hp, self.name, victim.hp, victim.name[0].upper()))
                battle = False
                return victim
                                
def pykemon_selector(wild_pykemon):
    """ generates random pokemon with """
    bag = []
    x = 0
    for x in range(0, 3):
        creature = random.choice(wild_pykemon)
        bag.append(creature)     
    return bag

def file_handler():
    """ Opens up our handy dandy file for the Pokemon, and coverts the hp and dmg into ints """
    creature_lst = []
    file = open("pykemonindex.csv")
    csv_file = csv.reader(file)
    for lines in csv_file:
        lines[1], lines[2] = int(lines[1]), int(lines[2])
        creature_lst.append(lines)
    file = file.close()
    return creature_lst

def choose_attacker(ai_pykemon, user_pykemon):
    """ This just randomly decides who attacks first for each instance of battle, then displays\
        who won the coin toss  """
    user = random.randint(1, 2)
    random_number = random.randint(1,2)
    if random_number == user:
        attacker = user_pykemon
        print("\nPlayer creature gets first hit ")
        victim = ai_pykemon
        return attacker, victim
    attacker = ai_pykemon
    print("\nAI creature gets first hit ")
    victim = user_pykemon
    return attacker, victim

def start_game():
    """ Introduces user to the game and asks if user whishes to play, and checks for a valid input"""
    while True:
        try:
            intro = "Pykemon Creature Game"
            print("\n{:>25}".format(intro))
            play_or_quit = input("1. Play against AI \nQ. Quit game \n===> ")
            while play_or_quit != "1" and play_or_quit != "Q" and play_or_quit != "q":
                print("\nYou must enter a valid choice of 1 or Q")
                play_or_quit = input("1. Play against AI \nQ. Quit game \n===> ")    
            if play_or_quit == "1":
                return True
            else:
                print("Good bye!")
                return False
        except ValueError:
            print("Please make a valid selction. 1 or Q")
def check_to_cheat():
    """Checkes the weakness of the user pykemon to see if AI can cheat and match its pykmon with its strength"""
    count = 0
    for pykemon in ai_pykedex:
        if pykemon[3] == user_pykemon.weakness:
            cheat_pykemon = ai_pykedex.pop(count)
            return cheat_pykemon
    return False

### Main Program
start = start_game()
loss_count = 1
while start == True:
    ### opens the csv file and creates a lst of each line
    wild_pykemon = file_handler()
    ### Gives the user three random Pykemon
    user_pykedex = pykemon_selector(wild_pykemon)
    ### Gives the AI three random Pykemon
    ai_pykedex = pykemon_selector(wild_pykemon)
    ### Alows the user to choose their fir Pykemon
    user_choice = Creature.user_display(user_pykedex)
    ### converts the user choice to a Creature Instance 
    user_pykemon = Creature(user_choice[0],user_choice[1],user_choice[2],user_choice[3],user_choice[4])
    ### Cheats and choose AI pokemon based on user_pymon weakness a random Pymon for the AI to use
    ai_cheat_pymon = check_to_cheat()
    if ai_cheat_pymon == False:
        ai_cheat_pymon = ai_pykedex.pop(random.randint(0, len(ai_pykedex)-1)) 
    ### converts the AI Pykemon into a creature instance
    ai_pykemon = Creature(ai_cheat_pymon[0],ai_cheat_pymon[1],ai_cheat_pymon[2],ai_cheat_pymon[3],ai_cheat_pymon[4])

    ### This loop starts the instances of battle ###
    dojo = True
    while dojo == True:
        ### Chooses who will attack first at random 
        attacker, victim = choose_attacker(ai_pykemon, user_pykemon)
        ### Starts the for instance o battle in the creature class
        battle_instance = Creature.battle_royale(attacker, victim)
        ### These loops check who won the battle. Based on who won, the looser chooses a new Pymon and the\
        ### battle continues till avictor is determoned
        if battle_instance != user_pykemon and len(user_pykedex) > 1:
            user_choice = Creature.user_display(user_pykedex)
            user_pykemon = Creature(user_choice[0],user_choice[1],user_choice[2],user_choice[3],user_choice[4])
        elif battle_instance != user_pykemon and len(user_pykedex) == 1:
            print("\nThis is your LAST chance!!! Brace Yourself!!!")
            user_choice = user_pykedex.pop(0)
            user_pykemon = Creature(user_choice[0],user_choice[1],user_choice[2],user_choice[3],user_choice[4])
        elif battle_instance != ai_pykemon and len(ai_pykedex) > 0:
            ai_cheat_pymon = check_to_cheat()
            if ai_cheat_pymon == False:
                ai_cheat_pymon = ai_pykedex.pop(random.randint(0, len(ai_pykedex)-1)) 
            ai_pykemon = Creature(ai_cheat_pymon[0],ai_cheat_pymon[1],ai_cheat_pymon[2],ai_cheat_pymon[3],ai_cheat_pymon[4])
        elif battle_instance == user_pykemon and ai_pykedex == []:
            print("\nAI could not handle your Dojo!! You are Victorious!!")
            dojo = False
            start = start_game()
            break
        elif battle_instance == ai_pykemon and user_pykedex == []:
            print("\nThe AI won! Try again and do better. (you've been defeated {} times!!)".format(loss_count))
            if loss_count == 10:
                print("you've been defeated {} times. YOU CANT HANDLE THIS DOJO, LEAVE AT ONCE!!!!".format(loss_count))
                break
            dojo = False
            start = start_game()
            loss_count += 1
    
        







