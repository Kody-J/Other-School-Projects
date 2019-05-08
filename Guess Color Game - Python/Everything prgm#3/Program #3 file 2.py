
#### Begenning Loop

def nbr_problems():
    """Ask user how many problems they want, doesnt advance till proper input"""

    usr_input = int(input("How many problems do you want: "))
    while usr_input <= 0:
        print()
        print("Please choose a number greater then 0 to contiue: ")
        usr_input = int(input("How many problems do you want: "))
    return usr_input

run_game = True
while run_game == True:

    print(" This Game Will Keep Your Mind Flexile")
    print("""*Choose the nummber of problems
* A window will pop up with a countdown after the countdown the game will begin
*A word in a given color will be displayed, Red, Green, or Blue.
The text of the word will also be Red, Green, or Blue.
Enter the color OF the word as is shown (R - Red, G - Green, B - blue) not the word, but the color
of the word.""")
    print("* After the game is over, you'll be shown how many you got right, the percentage and how long\
it took you. ")
    break
nbr = nbr_problems()



