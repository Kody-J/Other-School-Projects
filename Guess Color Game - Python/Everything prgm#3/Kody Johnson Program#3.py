
###################################################################################
## CS 101                                                                        ##
## PROGRAM 3                                                                     ##
##                                                                               ##
##                                                                               ##
## CREATION DATE: 20-25 FEB 2017                                                 ##
##                                                                               ##
##                                                                               ##
## PROBLEM:                                                                      ## 
##    CREATE A BRAIN GAME THAT DIPLAYS A WORD TO THE USER. THE WORD              ##
##    WILL SPELL A COLOR AND IT WILL ALSO BE OULINED IN A RANDOM COLOR           ##
##    TIME THE USER AS THEY TRY TO GUESS THE OUTLINE COLOR NOT WHAT              ##
##    COLOR IS SPELLED. THEN DIPLAY TIME, NUMBER CORRECT AND A USER              ##
##    RATING.                                                                    ##
##                                                                               ##
## ALGORITHM:                                                                    ##
## I1: Greet the user and Display the game set                                   ##
##	* Chose a number of problems.                                                ##
##	* A window will pop up with a countdown after the countdown the              ##
##          game begins                                                          ##
##	* A word in a given color will be displayed, Red, Green or Blue              ##
##          The text of the word  will also be red, green or blue                ##
##          Enter the color of the word shown ( R - Red, G - Green, B -          ##
##           Blue )                                                              ##
##          not the word, but the color of the word                              ##
##	* After the game is over, you'll be shown how many you got right,            ##
##          the percentage and how long it took you.                             ##
##                                                                               ##
##        UI1: Ask user how many problems to try.                                ##
##                UI2: User input should be an int betweet [3,20] inclusive      ##
##                UI3: If outside limits, warn user and don’t continue until     ##
##                    valid entry entered                                        ##
##        GM1: Initialize the ‘Game Mode’                                        ##
##        GM2: Create a UI graphics screen for the game to take place.           ##
##		GM2: Graphics should prompt the user to ‘click when ready’               ##
##		GM4: Once user is ready, display a count down from 5 and                 ##
##		     start the game                                                      ##
##        PM1: While the user is playing:                                        ##
##		PM2: A Numbered problem is displayed, one at a time                      ##
##        PM3: Each problem will be a print of a random ‘color string’ and the   ##
##             string will BE a random color                                     ##
##        PM4: Allow user to input R for (Red), G (Green), and B (Blue)          ##
##	      (User is guessing the actual color of the string not what              ##
##             color the string spells)                                          ##
##        PM5: If user guess == color of the color_str                           ##
##                PM5.1: add 1 to correct answer variable                        ##
##        PM6: If user guess != color of the color_str                           ##
##                PM6.1: add 1 to incorrect variable                             ##
##        PM7: Only generate number of problems desired by user, once questions  ##
##               are finished.                                                   ##
##               PM7.1: If 0 correct assign a value and do not divide            ##
##               PM7.2: Display to the user total correct out of total possible  ##
##                      in an int and %                                          ##
##               PM7.3: Display to the user Total time spent on test             ##
##               PM7.4: Give user a rating based on performance                  ##
##                       Time/ correct answers)                                  ##
##       EG1: Ask user if they would like to play again. (Y/Yes or N/No)         ##
##       EG2: If user inputs are outside of limits. Warn user and don’t          ##
##             continue until valid entry entered                                ##
##                    EG3: If user input is N/No end the game.                   ##
##       EG4:Else, Restart the game.                                             ##
##                                                                               ##
###################################################################################

def get_number():
    """Ask user how many problems they want, doesnt advance till proper input"""
    print()
    prompt = int(input("How many problems do you want: "))
    min_value = 3
    max_value = 21
    while prompt not in range(min_value, max_value):
        print("Please choose a number that's in range [3,20]: ")
        prompt = int(input("How many problems do you want: "))
    return (prompt, min_value, max_value)

def get_color():
    """creates random words and colors them"""
    colors = ("Blue", "Red", "Green")
    color_str = random.choice(colors)
    color_outline = random.choice(colors)
    return(color_str, color_outline)

def play_again():
    """Determins if user wants to play again"""
    next_round = input("Do you want to play again: ")
    while next_round.upper()!= "Y" and next_round.upper()!= "YES" and next_round.upper()!= "N" and next_round.upper()!="NO":
        print("Please select Y/Yes/N/No to continue: ")
        next_round = input("Do you wnat to play again:  ")

    if next_round.upper() == "Y" or next_round.upper() == "YES":
        run_game = True
        return run_game
    else:
        run_game = False
        return run_game, win.close(),print("Good Bye!")

def is_answer_correct(response):
    """Determinse if user answer is True or False"""
    while response.lower() != "b" and response.lower()!= "g" and response.lower()!= "r":
        print("Please select a key (R), (G) or (B) to continue: ")
        user_input = str(win.getKey())
        response = user_input  

    if response.upper() == color_outline[0]:
        correct = True
        return correct
    else:
        correct = False
        return correct

    
run_game = True
while run_game == True:

    import graphics as gfx
    import time
    import random
    qs_cnt = 0
    nbr_cnt = 1
    nbr_correct = 0
###Game intro with game rules###
    print("\t\tThis game will keep your mind flexible")
    print()
    print("""*Choose the nummber of problems
* A window will pop up with a countdown after the countdown the game will begin
* A word in a given color will be displayed, Red, Green, or Blue.
 The text of the word will also be Red, Green, or Blue.
 Enter the color OF the word as is shown (R - Red, G - Green, B - blue) not the word, but the color of the word.""")
    print("* After the game is over, you'll be shown how many you got right, the percentage and how long it took you. ")



    ### Loop for number of questions user wants to have ###
    nbr = get_number()

    ### Start of Graphics display ###
    win = gfx.GraphWin("My UI", 300, 300)
    text = gfx.Text(gfx.Point(150,150), "Click to begin")
    text.draw(win)
    press = win.getMouse()
    text.undraw()

    ### count down to begin ###
    for i in range(5 ,0, -1):
        cnt_dwn = gfx.Text(gfx.Point(150,150), i)
        cnt_dwn.draw(win)
        time.sleep(.5)
        cnt_dwn.undraw()

    start = time.time()
    ###This is where the game starts ###    
    while qs_cnt in range (nbr[0]):
        color_str, color_outline = get_color()
    
        ###diplaying the random questions and asking for user input###
        question = gfx.Text(gfx.Point(150,150), str(nbr_cnt)+"."+color_str)
        question_outline = question.setOutline(color_outline)
        question.draw(win)
   
        user_input = str(win.getKey())
        response = user_input

        ###Tracking correct answers### 
        correct = is_answer_correct(response)
        if correct == True:
            nbr_correct += 1

        question.undraw()
        qs_cnt += 1
        nbr_cnt += 1
        
    ###Correct percent based on number correct / question count###
    if nbr_correct > 0:
        correct_percent = float((nbr_correct/qs_cnt))
        end = time.time()
        end_time = end - start
        rating = float(end_time)/float(nbr_correct)
    ###Generate a Rating based on total time/ number correct##    
        if rating < 0.8:
            rate = "Great!"
        elif rating < 1.0:
            rate = "Good!"
        else:
            rate = "Poor"
        
    ###Counting for 0 division rule###
    else:
        correct_percent = 0
        end = time.time()
        end_time = end - start
        rate = "Poor!"
    win.close()
    ###Displaying results back to the User###
    print("You got {} out of {} problems correct, or {:.2%}".format(nbr_correct, qs_cnt, correct_percent))#Game data
    print("It took you {:.2f} seconds".format(end_time))
    print("Your rating is {}:".format(rate))

    ###Play again loop###
    run_game = play_again()
