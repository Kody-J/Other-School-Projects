#### Begenning Loop

def nbr_problems(user_input):
    """Ask user how many problems they want, doesnt advance till proper input"""

    usr_input = int(input("How many problems do you want: "))
    while usr_input <= 0:
        print()
        print("Please choose a number greater then 0 to contiue: ")
        usr_input = int(input("How many problems do you want: "))
    return
