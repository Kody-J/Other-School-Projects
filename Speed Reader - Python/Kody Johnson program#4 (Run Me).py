########################################################################################
## CS 101                                                                             ##
## PROGRAM 4                                                                          ##
##                                                                                    ##
##                                                                                    ##
## CREATION DATE: 08-12 MAR 2017                                                      ##
##                                                                                    ##
##                                                                                    ##
##                                                                                    ##                                            
##   PROBLEM:                                                                         ##
##      OPEN UP A .TXT FILE BASED ON USER INPUT. THEN BREAK THE FILE CONTAINING       ##
##      STRINGS INTO LINES AND LINES INTO WORDS THEN DISPLAY EACH WORD AT A           ##
##        GIVEN RATE ALONG WITH A WORD COOUNT. CREATING A SPEED READER.THE SPEED      ##
##        DEPENDS ON THE USER INPUT AND A WORD ENDING WITH PUNCTUATION DISPLAYS FOR   ##
##        TWICE AS LONG. ALLOW THE USER TO PAUSE, EXIT THE WINDOW, AND CHOOSE         ##
##       ANOTHER BOOK.                                                                ##
##                                                                                    ##
##                                                                                    ##
##    ALGORITHIM:                                                                     ##
##        I1: Greet the user, introduce them to the program                           ##
##        SP: Start the MAIN program loop with a True statement                       ##
##        SP1: While MAIN program loop == True                                        ##
##        UI1: Begin the loops to ask the user for desired inputs                     ##
##        UI2: Create a while loop Function to prompt user to input for which         ##
##             file/book they want to read                                            ##
##        UI2.1: Try user input                                                       ##
##        UI2.1.1: If user input is valid:                                            ##
##        UI2.1.1a: Accept user input                                                 ##
##        UI2.1.1b: return file/book                                                  ##
##        UI2.2: Check for and except any possible errors (FileNotFound)              ##
##        UI2.1: warn user                                                            ##
##        UI2.2 Prompt user to make valid input                                       ##
##        UI3: Create another while loop Funtion. Prompt user to input how many       ##
##             words per minute they want to read. Integer (1, 1000 wpm)              ##
##		UI3.1: change user input into and integer and Try user input          ##
##			UI3.1.1: If user input >= 1 or user input <= 1,000:           ##
##				UI3.1.1a: Accept user input                           ##
##        UI3.1.1b: return user input                                                 ##
##			UI3.1.2: elif user not >= 1 or user input not <= 1,000        ##
##                            UI3.1.2a: Warn user                                     ##
##			    UI3.1.2b: Prompt user to make valid input                 ##
##        UI3.2: Check for and except any possible errors (ValueErrors etc.)          ##
##        UI3.2.1: Warn user                                                          ##
##        UI3.2.2: Prompt user to make a valid input                                  ##
##        UI4: Create another while loop Fuunction. Prompt User to input what font    ##
##             size they want to use. Integer (5-36)                                  ##
##            UI4.1: Try user input                                                   ##
##		UI4.1.1: If user input >= 5 or user input <= 36:                      ##
##        UI.4.1.1: accept user input                                                 ##
##        UI4.1.2: break loop                                                         ##
##		UI4.1.2: Else:                                                        ##
##        UI4.1.2.1 warn user                                                         ##
##        UI4.1.2.2. Prompt user for valid input                                      ##
##        UI4.2: Check for and except any possible errors (ValueErrors etc)           ##
##		UI4.2.1: Warn user                                                    ##
##		UI4.2.2: Prompt user for valid input                                  ##
##        UI5: Create another while loop Function, ask user to input what word number ##
##        to start at. (Must be in range of the first word of the file to the last    ##
##        word of file)                                                               ##
##	UI5.1: Try user input:                                                        ##
##		UI5.1.1: If user input >= (beginning of file) or user                 ##
##                      input <=(end of file):                                        ##
##			UI5.1.1a: Accept user input                                   ## 
##        UI5.1.1b: Break loop                                                        ##
##       UI5.1.2: Elif: use input <= (beginning of file) or user input >=             ##
##        (end of file):                                                              ##
##			UI5.1.2a: Warn the user                                       ## 
##        UI5.1.2b: Prompt user for valid input                                       ##
##            UI5.2: Check for and except any possible errors (ValueErros etc.)       ##
##		UI5.2.1: Warn user                                                    ##
##        UI5.2.2: Prompt user for valid input                                        ##
##            G: Create a Graphics loop Function                                      ##
##            G1: While word_cnt is != file end count (total of words in user         ##
##            selected file):                                                         ##
##            G2: Create a graphics window.                                           ##
##        G3: Split file user choose into a collection of individual words.           ## 
##        G4: Display, starting with on the word number the user selected, each word  ##
##            one by one in sequential order.                                         ##
##        G4.1: Display each word based on the WPM (words per minute) the user        ##
##              selected; for the correct amount of time and go to the next.          ##
##        G4.2 If word displayed contains a punctuation mark ( , . ?!):               ##
##        G4.2.1: keep the word displayed for 2* as long as chosen WPM count          ##
##                (example if WMP is 60 or 1 word a sec, and a punctuation mark is    ##
##                 displayed, then the word is displays for 2sec instead of just 1sec)##
##		G5: If user clicks on screen:                                         ##
##			G5.1: Pause window                                            ##
##		G6: If user clicks again:                                             ##
##			G6.1: Continue                                                ##
##	G7: If user exits the graphics window or word_cnt == file end count:          ##
##	E1: Ask user to input if they would like to open another file (Y/YES/N/NO)    ##
##	E2: While user input.upper not = (Y/YES/N/NO):                                ##
##		E2.1: Warn user                                                       ##
##		E2.2: Prompt user to make valid input                                 ##
##	E3: If user input.upper == N or user input.upper == NO:                       ##
##		E4: set MAIN loop = False                                             ##
##		E5: Say goodbye to user                                               ##
##	E3: If user input.upper == YES or user input.upper == Y:                      ##
##		E3.1: Repeat                                                          ##
##                                                                                    ##
##                                                                                    ##                                                 
########################################################################################

import graphics as gfx
import time
import PyPDF2

print("\tGreetings and welcome to the Pyhton Speed Reader")
def user_input():
    """ Gets which book the user wants to read """
    while True:
        try:
            wht_file = input("\nEnter the name of a file to speed read(end with .txt): ")
            ### adds .txt if necessary
            if wht_file.lower()[-4:] != ".txt":
                wht_file = "{}.txt".format(wht_file)
            opn_file = open(wht_file, "r")
            return opn_file
        except FileNotFoundError:
            print("Sorry file not found, check spelling and try again(end with .txt). ")
        except ValueError:
            print("\nPlease only enter a file name. ")

def usr_wpm():
    """ Gets the WPM the reader will go from user """
    while True:
        try:
            usr_wpm_inpt = float(input("\nHow many Words Per Minute do you want to read? "))
            while usr_wpm_inpt < 1.0 or usr_wpm_inpt > 1000.0:
                print("Please choose a count from 1 to 1000")
                usr_wpm_inpt = float(input("\nHow many Words Per Minute do you want to read? "))
            return usr_wpm_inpt
        except ValueError:
            print("Please use number keys")

def usr_font():
    """ Gets font size from user [5-36] """
    while True:
        try:
            usr_font_inpt = input("\nWhat size font would you like to read in? ")
            while float(usr_font_inpt) < 5.0 or float(usr_font_inpt) > 36.0:
                print("Please choose an integer size from 5 to 36" )
                usr_font_inpt = input("\nWhat size font would you like to read in?")
            return int(usr_font_inpt)
        except ValueError:
            print("Please use number keys")

def start_point(words):
    """ Prompts user for start point """
    while True:
        try:
            usr_strt_inpt = input("\nEnter what word number to start at? ")
            if usr_strt_inpt == '':
                return 1
            while int(usr_strt_inpt) < 1 or int(usr_strt_inpt) > len(words):
                print("Please enter an interger from 1 to {}".format(len(words)))
                usr_strt_inpt = input("\nEnter what word number to start at? ")
            if usr_strt_inpt == '':
                return 1
            return int(usr_strt_inpt)
        except ValueError:
            print("Please use number keys")

def speed_reader_output(speed):
    """ Convesion for WPM """
    word_speed = 60/speed
    return word_speed

def words_control(file):
    """ Counts words in book/ and stores them in a list """
    word_bank = []
    for lines in file:
        words = lines.split()
        word_bank.extend(words)
    return word_bank

def pdf_words_control(file):
    word_bank = []
    num_pages = file.numPages
    count = 2
    text = ""
    #Loop reads each page
    while count < num_pages:
        pageObj = file.getPage(count)
        count += 1
        text = pageObj.extractText()
        word_bank.extend(text)

    return word_bank

def continue_on():
    """ Asks user to continue or not """
    again = input("\nWould you like to run this again? (Y/YES/N/NO): ")
    while again.upper() != "YES" and again.upper() != "Y" and again.upper() != "NO" and again.upper() != "N":
        print("You must enter Y, YES, N, or NO")
        print()
        again = input("\nWould you like to run this again? (Y/YES/N/NO): ")
    if again.upper() == "Y" or again.upper() == "YES":
        return True
    else:
        return False

def file_reader(start, words, size ,sleep_time):
    """ Open user chosen book/ itterates through book and display is to user """
    win = gfx.GraphWin("Speed Reader", 350, 350)
    while win.isClosed() == False:
        try:
            word_count = start
            ###GFX window for the words/ count to display
            for i in words[start:]:
                print_word = gfx.Text(gfx.Point(175,175), i)
                print_word.setSize(size)
                print_word.draw(win)
                word_count += 1
                count_txt = "{} of {}".format(word_count, len(words))
                count = gfx.Text(gfx.Point(175, 295), count_txt)
                count.setSize(10)
                count.draw(win)
                win.checkMouse()## Checking for click 
                ### Checking for punctuation and pausing if necessary
                if i[-1] == "," or i[-1] == "." or i[-1] == "?" or i[-1] == "!" or i[-1] == ";" or i[-1] == ":":
                    sleep = time.sleep(sleep_time*2)
                else:
                    sleep = time.sleep(sleep_time)
                pause = win.checkMouse()### Checking for click
                while pause != None:### if cicked Pauses and waits for click from user
                    win.getMouse()
                    break
                print_word.undraw()
                count.undraw()
            win.close()
            run_again = continue_on()  
            return run_again
        except Exception:
            run_again = continue_on()
            return run_again
        
### Start of the running program ###
run = True
while run == True:
    file = user_input()
    words = words_control(file)
    speed = usr_wpm()
    size = usr_font()
    start = start_point(words)
    sleep_time = speed_reader_output(speed)
    main_program = file_reader(start,words,size,sleep_time)
    run = main_program
print()
print("Good Bye!")
