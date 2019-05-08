def play_again(run_game):
    """Determins if user wants to play again"""
    next_round = input("Do you wnat to play again? Y/Yes or N/No:  ")
    while next_round.upper()!= "Y" or next_round.upper()!= "YES" or next_round.upper()!= "N" or next_round.upper()!="NO":
        print("Please select Y for Yes or N for No to continue: ")
        next_round = input("Do you wnat to play again? Y/Yes or N/No:  ")

    if next_round.upper() == "Y" or next_round.upper() == "YES":
        return run_game == True
    else:
        return run_game == False, win.close()
        
def play_againn():
    print("You got {} out of {} problems correct, or {:.2%}".format(nbr_correct, qs_cnt, correct_percent))
    print("It took you {:.2f} seconds".format(end_time))

    next_round = input("Do you wnat to play again? Y/Yes or N/No: ")
    while next_round.upper()!= "Y" and next_round.upper()!= "YES" and next_round.upper()!= "N" and next_round.upper()!="NO":
        print("Please select Y for Yes or N for No to continue: ")
        next_round = input("Do you wnat to play again? Y/Yes or N/No:  ")

    if next_round.upper() == "Y" or next_round.upper() == "YES":
        return run_game = True)
    else:
        return (run_game = False)
        win.close()
