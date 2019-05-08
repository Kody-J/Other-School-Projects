###########################################################################
## CS 101                                                                ##
## PROGRAM 2                                                             ##
## KODY JOHNSON                                                          ##
## KSJQM5@MAIL.UMKC.EDU                                                  ##
## CREATION DATE: 06-12 FEB 2017                                         ##
## DUE DATE: 12 Feb 2017                                                 ##
##                                                                       ##
## PROBLEM:                                                              ## 
##    MUST CONSTRUCT A PROGRAM WHICH ASSISTS A USER IN                   ##   
##    GENERATING A RANDOM LIST OF JOB OFFERS, AND COMPARE                ##
##    THEIR SALARIES. THEN CHOOSE THE HIGHEST PAYED JOB                  ##
##    BASED ON A DETERMINED CONTROL GROUP.                               ##
##    FINISHED BY DISPLAYING FINAL INFORMATOION. MAKE IT REPEATABL       ##
##                                                                       ##
##                                                                       ##
## ALGORITHM:                                                            ##
##  I1: Ask user How many Jobs they interested in looking at             ##
##  I2: The users input must be > 0                                      ##
##  I3: If input is < 0 warn the user to enter a valid number\           ##
##     ( > 0) repeat I1 until a valid input is received                  ##
##       reject (create a base)                                          ##
##    I5: Input must be > 0.                                             ##
##	I6: If Input is < 0, warn the user and repeat I4 until           ##
##	a vailed input is received                                       ##
##    I7: Ask the user if they would like to see details about           ##
##        the job offer                                                  ##
##    I8: Valid inputs must be (1 for yes or 2 for no)                   ##
##	I9: If Input is outside limits, warn the user and                ##
##	repeat I8 until a valid input is received                        ##
##    P1: Based on user inputs, generate Job offers with Gaussian        ##
##        distribution                                                   ##
##    P2: Reject, (Display if necessary), initial job offers. Keep       ##
##        a record of all the offers rejected.                           ##
##    P3: After Initial rejections, take the highest payed               ##
##       (rejected) offer and compare it to ALL future offers            ##
##	P4: If Job offer Salary is < the Highest of the previou          ##
##	    s offers, Reject                                             ##
##	P5: If Job offer Salary is > previous Highest offer,             ##
##	    Accept                                                       ##
##    P6: If no other job offer is > any previous offer then             ##
##        automatically Accept the final offer                           ##
##    E1: Once Job offer is accepted, reject all remaining offers.       ##
##    E2: Display to the user the Highest Payed REJECTED offer           ##
##    E3: Display to the user the Highest Payed POSSIBLE offer           ##
##    E4: Display the difference between the Highest POSSIBLE Job        ##
##        Salary and compare to their Accepted Job Salary, showing       ##
##        any losses.                                                    ##
##    F1: Ask the user if they would like to Look for another Job        ##
##       (Y/YES or N/NO)                                                 ##
##    F2: If Input is outside limits, warn the user and repeat F1 until  ##
##        a valid input is received                                      ##
##	F3: If Y/YES, Repeat to I1                                       ##
##    F4: Else end the program                                           ##
##                                                                       ##
###########################################################################

##Start of program, creating true statement for BIG loop and name variables used

Run_program = True


##Begin prompting the user for desired information
while Run_program == True:

    rejected_high = 0
    low_salary = 0
    high_salary = 0
    selected_job = 0
    import random
    random_job = 0

    
    print()
    job_offer_cnt = int(input("How many Job Offers Would You Like to Consider: "))
    print()

    ## Dont let User proceded without proper input
    while job_offer_cnt <= 0:
        print('You must consider at least 1 Job Offer to continue')
        print()   
        job_offer_cnt = int(input("How many Job Offers Would You Like to Consider: "))
        print()

    ## Ask User For number of rejected jobs
    job_salary_base = int(input("How many offers should we disguard for a base: "))
    print()

    ## Dont let User proceded without proper input      
    while job_salary_base <= 0 or job_salary_base >= job_offer_cnt:
        print()
        print('Please do not choose a number less than zero or less than the total Jobs you are concidering! ')
        print()
        job_salary_base  = int(input("How many offers should we diguard for a base: ")) 
        print()

    ## Ask useer if they want the detail for each job
    job_detail_str = int(input("Would you like to see Job Offer Details (Please select 1(for No) or 2(for Yes): "))
    print()

    ## Dont let the user procede without proper input
    while job_detail_str != 1 and job_detail_str != 2:
        print()
        print('Please enter make a valid selection')
        print()
        job_detail_str = int(input("Would you like to see Job Offer Details (Please select 1(for No) 2(for Yes): "))
        print()
        
    ##Program Running if user doesnt want to see Job Details 
    if job_detail_str == 1:
        dns_details = True

        ## Create loop for the dns (Do Not Show) details option
        ## Keep Track of low , high, and the users 'selected' job
        while dns_details == True:

            ## Reject the 'base' amount the user chose
            ## Keep track of highs and lows but dont accept any offers yet
            generated_job = random.gauss (65,5)
            while random_job < job_salary_base:

                if generated_job < low_salary:
                    low_salary = generated_job
                    random_job += 1
                    generated_job = random.gauss (65,5)

                if generated_job > high_salary:
                    rejected_high = generated_job
                    high_salary = generated_job
                    random_job += 1
                    generated_job = random.gauss (65,5)
                  
                else:
                  random_job += 1
                  generated_job = random.gauss (65,5)
                  

            ## Generate Acceptable jobs, comparing the highest to previous high salary
            ## Keep track of lows and his and Accept the first higest salary
            while random_job != job_offer_cnt and generated_job < high_salary:
                generated_job = random.gauss (65,5)

                if generated_job < low_salary:
                    low_salary = generated_job
                    random_job += 1

                elif generated_job <= high_salary:
                    random_job += 1

                if generated_job > high_salary:
                    high_salary = generated_job
                    selected_job = generated_job
                    random_job += 1
    
            while random_job != job_offer_cnt:
                generated_job = random.gauss (65,5)


                if generated_job < low_salary :
                   low_salary = generated_job
                   random_job += 1
                if generated_job > high_salary:
                    high_salary = generated_job
                    random_job += 1

                else:
                    random_job += 1

                if random_job == job_offer_cnt and selected_job != 0:
                    generated_job = random.gauss (65,5)
                    selected_job = generated_job

            dns_details = False

    ## Repeat Just the same as before except diplay (PRINT) the individual Job information        
    if job_detail_str == 2:
        show_details = True

        while show_details == True:
            generated_job = random.gauss (65,5)
            while random_job < job_salary_base:
                if generated_job < low_salary:
                    low_salary = generated_job
                    print(generated_job,'Job Rejected')
                    print()
                    random_job += 1
                    generated_job = random.gauss (65,5)
                if generated_job > high_salary:
                    rejected_high = generated_job
                    high_salary = generated_job
                    print(generated_job,' Job Rejected')
                    print()
                    random_job += 1
                    generated_job = random.gauss (65,5)

                else:
                    random_job += 1
                    print(generated_job,' Job Rejected')
                    print()
                    generated_job = random.gauss (65,5)
                  

            
            while random_job != job_offer_cnt and generated_job < high_salary:
                generated_job = random.gauss (65,5)

                if generated_job < low_salary:
                    low_salary = generated_job
                    print(generated_job,'Job Rejected')
                    print()
                    random_job += 1

                elif generated_job <= high_salary:
                    print(generated_job,'Job Rejected')
                    print()
                    random_job += 1


                if generated_job > high_salary:
                    high_salary = generated_job
                    selected_job = generated_job
                    print(selected_job,'Job Accepted!')
                    print()
                    random_job += 1

            while random_job != job_offer_cnt:
                generated_job = random.gauss (65,5)


                if generated_job < low_salary:
                    low_salary = generated_job
                    print(generated_job,'Job Rejected')
                    print()
                    random_job += 1
    
                elif generated_job > high_salary:
                    high_salary = generated_job
                    print(generated_job,'Job Rejected' )
                    print()
                    random_job += 1

                else:
                    print(generated_job,'Job Rejected')
                    print()
                    random_job += 1

                if random_job == job_offer_cnt and selected_job <= 0:
                    generated_job = random.gauss (65,5)
                    selected_job = generated_job
                    print(selected_job,'Job Accepted!!')
                    print()

            show_details = False

    ## Display all the resulting information for the user
    print('The Highest Payed Job Was:', high_salary,)
    print()
    print('The Highest Payed Rejected Job Was:', rejected_high,)
    print()
    print('The Job You Excepted Was:', selected_job,)
    print()
    print('You Missed Out On:', high_salary - selected_job,)


    ## Ask user if they want to go again
    play_again = str(input('Would you like to continue searching? Y/Yes or N/No: '))

    while play_again != 'Y' and play_again != 'Yes' and play_again != 'N' and play_again != 'No':
        print()
        print('Please make a valid selection!')
        print()
        play_again = str(input('Would you like to continue searching? Y/Yes or N/No: '))

    ## End the program if user doesnt wish to continue
    if play_again == 'N' or play_again == 'NO' or play_again == 'N/NO':
        print()
        print('Thank you, good bye')
        play_again = 'Done'
        Run_program = False

    else:
        Run_program = True
                


            
                
                        

                

                

                    
                    
                

            

            
                
        

            
                
            

            
    
