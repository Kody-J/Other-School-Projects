#########################################################################################
## CS 101
## PROGRM 6
## KODY JOHNSON
## KSJQM5@MAIL.UMKC.EDU
## CREATION DATE: APR 7-9
## DUE DATE: 9 APR 2017
##
## PROBLEM:
##    USING A CSV FILE, COVERT THE CONTENTS INTO JSON DATA FILE TO BE OPENED IN
##    A HTML PAGE. FILE AND DATA SHOULD BE SPECIFIC TO USER INPUT
##
## ALGORITHM:
##    Attendance CSV
##    G: Greet the user and inform user of the purpose for the program
##    (displaying data files for attendance purposes)
##    F1: Create a function which asks for user input and checks if
##    input is valid:
##     	F1.1: Option 1: Read an attendance csv file and create a
## 	single class output:
##    F1.2: Quit
##    F1.3: If user input not == 1 or Q:
##	F1.3.1: Warn the user
##	F1.3.2: Prompt user for valid input
##    F1.4: Else if user input is 1, 2 or Q then return or accept
##          user input:
##    F2:  Create a function which prompts user to input a CSV file,
##         and checks if the file is valid:
##	F2.1: Prompt user to input CSV file name:
##	F2.2: If the file is not in the directory
##		F2.2a: Warn the user
##		F2.2b: Prompt user for valid input
##	F2.3: If user input triggers and error
##		F2.3a: warn user
##		F2.3b: Prompt user for valid input
##	F2.4: If file is in directory:
##		F2.4a: Accept user input
##    F3: Create a function to handle to handle option 1
##	F3.1: Open user file CSV file and covert its contents into a list.
##	F3.2: Prompt the user to specify which class they would like data for
##	F3.3: If user inputs a class that is not contained in the file:
##		F3.3a: Warn the user
##		F3.3b: Prompt user for valid input
##	F3.4: If user input valid:
##		F3.4a: Accept user input
##	F3.5: Sort the information in the file for the specified class
##		F3.5a: Format dates appropriately
##		F3.5b: If dates cannot be formatted the same and an Error is generated:
##			F3.5b1: Warn user of possibly corrupt data
##			F3.5b2: Prompt user to input new file (F2)
##		F3.5c: Calculate the attendance appropriately (percentage present)
##       F3.5: Output data to a Jason file
##       F3.5: Open an html page and automatically display the data to the user
##         F4: Create a function which asks user if they wish to view another file
##            or class after the have closed the html. (F1-F2 etc.)
##	F4.1: If user input == Q
##	F4.1a: Exit the program
#########################################################################################
import csv
import os
import time
import datetime
import json
import webbrowser
from operator import itemgetter
import time

def user_choice():
    """ Displays options to the user. Determins iif user input is valid"""
    while True:
        try:
            print("\n{:>50}\n\n{}".format("Attendance Data File Generator","You can create a single data file of attandance for a single class or for multiple"))
### Display users option ###
            print("""
1. Read an attendance csv file and create a single class output. (data.js)
Q. Quit """)
            user_choice = input("\n\nPlease make a selection (1 or Q)\n\n==> ")
            if user_choice == "1"  or user_choice.upper() == "Q":
                return user_choice
            else:
                print("You must choose a valid option from (1 or Q) ")
        except ValueError:
            print("You must choose a valid option from (1 or Q) ")

def file_choice():
    """ Asks user for a csv file until a file within the directory is chosen
        Does not check if the file is proper, just its existance """
    while True:
        csv_in_dir = os.listdir()
        user_choice = input("\nEnter the csv file name: ")
        if user_choice in csv_in_dir:
            return user_choice
        elif user_choice + ".csv" in csv_in_dir:
            return user_choice + ".csv"
        print("\nCould not open the file {}, please try again".format(user_choice))

def csv_file_lst():
    """ Converts the csv file into a list of lists """
    file = open(user_file)
    csv_file = csv.reader(file)
    csv_lst = []
    for line in csv_file:
        csv_lst.append(line)
    file.close()
    return csv_lst
        
def date_conversion():
    """ Itterates through the csv list and changes format of the dates colums
        to be sortable """
    try:
        for line in csv_lst:
            date = line[1]
            date_convert = datetime.datetime.strptime(date,"%m/%d/%Y")
            line[1] = date_convert
        return csv_lst
    except ValueError:
        print("\nThe file given has an invalid date colum. Please enter another")
        return False

def option1_class():
    """ Ask user to pick a valid class, keep asking till good input """
    while True:
        try:
            which_class = input("\nEnter the class you want exported to data.js: ")
            ### seperates file into each class
            class_lst = []
            for lines in right_dates:
                if lines[0] not in class_lst:
                        class_lst.append(lines[0])
            choice = class_lst.index(which_class.upper())
            ### Creates list with with as many lists as there are classes in it		
            big_class = []
            for classes in class_lst:
                    classes = []
                    big_class.append(classes)
            ### Seperates all data for each class into a seperate list
            for line in right_dates:
                    if line[0] == class_lst[0]:
                            big_class[0].append(line)
                    elif line[0] == class_lst[1]:
                            big_class[1].append(line)
                    elif line[0] == class_lst[2]:
                            big_class[2].append(line)
                    elif line[0] == class_lst[3]:
                            big_class[3].append(line)
                    else:
                            big_class[4].append(line)
            ### Sorts the file in order of dates
            class_by_dates = sorted(big_class[choice], key=itemgetter(1))
            title = which_class.upper()
            return class_by_dates, title
        except TypeError:
            print("\n\nclass{} is not in the attendance file. You must chose form {}".format(which_class, class_lst))
        except ValueError:
            print("\n\nclass{} is not in the attendance file. You must chose form {}".format(which_class, class_lst))

def class_attendance_dic():
    """ Creates a dictionary of Key, Values for each individual date with its, attendace ratio [30,15]"""
    class_att_dic = {}
    for classes in option1:
        if classes[1] not in class_att_dic:
            class_att_dic[classes[1]] = [1, 0]
            if classes[5] == "Present":
                class_att_dic[classes[1]][1] += 1
        elif classes[1] in class_att_dic:
            class_att_dic[classes[1]][0] += 1
            if classes[5] == "Present":
                class_att_dic[classes[1]][1] += 1
    return class_att_dic

def format_data():
    """ changes the key, values in the class_attendance dic to key,value tuples and put into a list """
    value_key_lst = []
    for key, value in date_attendance.items():
        value_key_lst.append((key, value))
    return value_key_lst

def format_data_2(formatted_data):
    """creates a list of dictions for each date exp; [{key(attendance): \\
    value(the attendance rate),key(date), value(date)}]"""
    var_lst = []
    for items in formatted_data:
            var_dic = {"attendance": items[1][1]/items[1][0] * 100, "date": items[0]}
            var_lst.append(var_dic)
    return var_lst

def change_date():
    """ re-formats the dates in the dictionaries """
    for value in re_format_data:
            date = value["date"]
            date_convert = date.strftime("%m/%d/%Y")
            value["date"] = (date_convert)
    return re_format_data

def output_file():
    """ Places the json ready data into a file in json format to be displayed via html"""
    output_file = open("data.js", "w") 
    print("var title =",vartitle+";","\nvar json_data=\n",varjson_data+";",file=output_file)
    output_file.close()


run = True
while run == True:
    user_input = user_choice()
    if user_input.upper() == "Q":
        print("\nGood Bye!" )
        run == False
        break
    user_file = file_choice()
    csv_lst = csv_file_lst()
    right_dates = date_conversion()
    while right_dates == False:
        ### warning user if dates arent acceptable ###
        user_input = user_choice()
        user_file = file_choice()
        csv_lst = csv_file_lst()
        right_dates = date_conversion()
    option1, var_title = option1_class()
    date_attendance = class_attendance_dic()
    formatted_data = format_data()
    re_format_data = format_data_2(formatted_data)
    var_lst = change_date()
    varjson_data = json.dumps(var_lst)
    vartitle = json.dumps(var_title)
    js_file = output_file()

    webbrowser.open("ClassAttendance.html")

