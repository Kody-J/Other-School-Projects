######################################################################################
## CS 101
## PROGRAM 7
## KODY JOHNSON
## KSJQM5@MAIL.UMKC.EDU
## CREATIONDATE: 03-07 MAY 2017
## DUE DATE: 07 APR 2017
##
##  PROBLEM:
##          GIVEN A SKELITON PROGRAM AND USING UNIT TESTING, CREATE A PROGRAM
##          WHICH OPENS A FILE CONTAINING CUSTOMERS AND SIMULATES A GROCERY
##          STORE. CUSOMERS WILL CHOOSE A 1 OF FOUR LANES TO GO THROUGHT BASED
##          ON THEIR LINES, WHILE CASHIERS CHECK CUSTOMES ITEMS, UNTILL NO MORE
##          CUSTOMERS ARE LEFT.
##
##  ALGORITHM:
##              C1: Create a class which will simulate a Customer
##	C1.1: Each customer will have these attributes:
##		C1.a: Customer Number
##		C1.b: Arrival time
##		C1.c: Number of Items in basket
##		C1.d: Number of Items purchased (payed)
##		C1.e: Exit Line Time
##		C1.f: When the Cahier Arrived 
##		C1.g: When the Cashier Exited
##
##      C1.2: Create a Method which will print out each Customer details
##	    C1.2a: Each customer Instance should be in the Format C (1) 
##
##      C1.3: Create a Method which sets an arrival time to each Customer instance when they get
##            into a Line (time will be tracked in “tick”s; whole number increments starting from 0)
##
##	C1.4: Create a Method which can be called when the Customer gets to the cashier:
##		C1.4.1: Sets the line_exit attribute
##		C1.4.2: Sets the cashier_arrival_attribute
##		
##	C1.5: Create a Method for when the Customer exits the Cashier:
##		C1.5.1: Takes in the time “tick” when the customer got to the Cashier
##		C1.5.2: Sets the cashier_exit attribute
##
##	C1.6: Create a method which Updates the Clock:
##		C1.6.1: If the customer has arrived at the Cashier:
##          C1.6.1a: Number of payed Items increases, and number of Items decreases per clock tick
##          C1.6.1b: If the number of Items left is < 1:
##	    C1.6.1b.a: The Customers is finished checking out
##	
##      C1.7: Create a Method which tracks the “Wait Time”
##	 	C1.7.1: Subtract the arrival tick(n) time form the exit tick(n) time:
##			C1.7.1a: Assign that value back to that customer Instance
##
##      C2: Create a class for the Cashier:
##	    C2.1: Each Cashier will have these attributes:
##		C2.1a: Lane (will reflect the unique lane up to 4 for each customer line)
##		C2.1b: Line (reflects the number of Customers in the Lane queue
##              C2.1c: Exit_Pool (reflects the number of Customers finished purchasing Items in a single Lane)
##
##	C2.2: Create a Method which will print out a string representation of the Cashier 
##		C2.2a: It should be in the form Checker $ (1) 
##		C2.2.b: If the Cashier has a customer:
##			C2.2ba: Format should look like Checker $ (1) – C (1)
##	C2.3: Create a Method which updates the Cashier Instance:
##		C2.3a: If the Cashier has a Customer:
##			C2.3a1: Each time tick Increases the Customers “Purchased “items by 1
##			And decreases the “Items” by 1:
##		C2.3b: If the Cashier has a Customer and the Customers “Items” < 1:
##			C2.3b1: Customer leaves Line and enter the Exit_Pool
##			C2.2b2: If there is another Customer in the Cashier Line queue:
##				C2.2b2a: Customer moves to the Cashier
##		C2.3c: If the is no Customer:
##			C2.3c1: We get one from the Line queue if there is one
##	
##      C2.4: Create a Method for is_empty:
##	C2.4a: If there are no Customers with a Cashier or in the Cahiers Line:
##		C2.4a1: Returns a True bool
##
##      F1: Create a function which reads in the “arrivals” .txt file
##	F1.2: Open file and append contents into a list for further user
##	F1.3: Close the File
##
##      F2: Create a Function which will act as a clock:
##	F2.1: The Clock will only use Integers starting form tick (1)
#################################################################################################

import copy
import time

class Customer(object):
    """ Simulates a customer in a queue """

    def __init__(self, cust_number: int, arrived: int, items: int):
        """ This method initializes the variables for the instance of the Customer instance
        :param cust_number  : int - The number of the customer
        :param arrived      : int - The time the customer arrived
        :param items        : int - How many items they've purchased.
        :return             : None

        The __init__ also initializes other attributes that aren't passed in.
        items_paid          : int - How many items have been paid for.
            Starts out at zero and as the checker checks them out it gets incremented.
        line_arrival        : int - Initializes to None, but is the time they arrive at the line.
        line_exit           : int - The clock time they exited the line.  Initially should be None
        cashier_arrival     : int - The time they arrived at the cashier.  Initially should be None
        cashier_exit        : int - The time they left the cashier.  Initially should be None
        """
        self.cust_number = cust_number
        self.arrived = arrived
        self.items = items
        self.items_paid = 0
        self.line_arrival = None
        self.line_exit = None
        self.cashier_arrival = None
        self.cashier_exit = None

    def __str__(self):
        """ String Representation
        :return             : str - Returns the string representation of the customer instance.

        It should be in the form C(1)  Where 1 is the number of the customer.
        """
        customer = "C({})".format(self.cust_number)
        return customer

    def __repr__(self):
        """ String Representation of the instance
        :return             : str -  Returns the string representation of the customer instance.
        """
        return "C({})".format(self.cust_number)

    def get_in_line(self, clock):
        """ Method sets the arrival time to the clock.
        :param clock        : int - The time as an int when the person gets into line.
        :return             : None
        """
        self.line_arrival = clock
       
        

    def at_cashier(self, clock):
        """  Method is called when the customer gets to the cashier.
        :param clock        : int - The time the customer got to the cashier.
        :return             : None
         It should set the line_exit attribute and cashier_arrival attribute
        """
        self.cashier_arrival = clock

        self.line_exit = clock

    def exit_cashier(self, clock):
        """ Method is called when the customer exists the cashier.
        :param clock        : int - The time the customer got to the cashier.
        :return             : None
         Sets the cashier_exit attribute
        """
        self.cashier_exit = clock
        

    def update(self, clock):
        """ Method is called for each update at the clock.  If the customer has arrived at the cashier and has items
            Then their items get decremented and items_paid is incremented. ( an item got scanned ).
        :param clock        : int - The time the customer got to the cashier.
        :return             : None
        """
        if self.cashier_arrival != None and self.items > 0 and clock > self.arrived:
            self.items -= 1
            self.items_paid += 1

            
    def wait_time(self):
        """ Method returns how long the customer has waited.
        The difference from when they left the line and when they entered it
        If they haven't arrived in a line or exited the line then it should return None
        :return             : int - The time they waited in line.
        """
        if self.cashier_arrival != None and self.line_arrival != None:
            return self.cashier_arrival - self.line_arrival
            
       

class Cashier(object):
    """ Simulates a cashier """
    def __init__(self, lane : int, line : iter, exit_pool : iter):
        """ Initializes the Cashier
        :param lane         : int - The lane of the cashier.  1, 2, 3, etc
        :param line         : list - Iterable that is the line of customers waiting.
        :param exit_pool    : list - All customers leave the cashier into an exit pool.  We can then examine our
                                customers in the exit pool to see how long they waited.
        :return             : None
        """
        self.lane = lane
        self.line = line
        self.exit_pool = exit_pool
        self.customer = None

    def __str__(self):
        """ String Representation of Cashier
        :return             : str - Returns the string representation of the Register instance.

        It should be in the form $(1)  Where 1 is the number of the Lane
                If the Cashier has a customer in it then it should be $(1) - C(1)  ( followed by the customer )
        """
        self_str = "$({})".format(self.lane)
        if self.customer != None:
            cashier_w_cust = "{} - {}".format(self_str, self.customer)
            return cashier_w_cust
        elif self.customer != None and len(self.line) == 2:
            cashier_w_line = "{} - {}<- {}".format(self.str, self.customer, self.line[0])
            return cashier_w_line
        elif self.customer != None and len(self.line) == 3:
            cashier_w_2line = "{} - {}<- {},{}".format(self.str, self.customer, self.line[0], self.line[1])
            return cashier_w_2line

        return self_str

            
    def update(self, clock):
        """ updates the world for every clock tick.
        :param clock        : int - The clock time of when the update occurs.
        :return             : None
        If the cashier has a customer then it updates the customer until all the items are paid for
            If the customer has all the items paid for then
                they leave and hit the exit pool
                We get another customer from the line assuming there is one.
        If there is no customer then we get one from our line assuming that their is one.
        """

        if self.customer == None and len(self.line) > 0:
            self.customer = self.line.pop(0)
            self.customer.at_cashier(clock)

        elif self.customer != None and self.customer.items > 0:
            self.customer.update(clock)
            if self.customer.items < 1:
                self.exit_pool.append(self.customer)
                self.customer = None
      

    def is_empty(self):
        """ Returns if there is none at the register either in line or being checked out.
        :return             : bool True if their is no customer checking out and the line is empty.
        """
        if self.line == None and self.customer == None:
            return True

def generate_cust_lst(person_lst):
    """ Converts the list of shoppers to instances of customers """
    cust_lst = []
    for index in range(0, len(person_lst)):
        cust = Customer(person_lst[index][0],person_lst[index][1],person_lst[index][2])
        cust_lst.append(cust)

    return cust_lst

def create_cashier():
    """ Creates 4 instances of cashier """
    cashier_lst = []
    for cnt in range(1,5):
        cashier = Cashier(cnt,[],[])
        cashier_lst.append(cashier)

    return  cashier_lst

def choose_line(teller_lst):
    tester = teller_lst[0]
    for teller in teller_lst:
        if len(teller.line) < len(tester.line):
            tester = teller
    return tester        
        
# If the name of module running is the main module and isn't being imported run it.
if __name__ == "__main__":
    import os
    file = open("arrivals.txt")
    person_lst = []
    for line in file:
        strip_line = line.strip()
        temp_lst = strip_line.split(" ")
        person_lst.append(temp_lst)
    cashier_lst = create_cashier()
    cust_lst = generate_cust_lst(person_lst)
    file.close()


    clock = 1
    print("Clock is at {}".format(clock))
    idx = 0
    while idx in range(0,len(person_lst)) and len(person_lst) > 0:
        if cust_lst[idx].arrived == clock:
            temp_short = cashier_lst[0]
            for cashier in cashier_lst:
                if len(cashier.line) == 0:
                    cashier.line.append(cust_lst[idx])
                    cust_lst.remove(idx)
                    for itmes in cashier_lst:
                        print(str(items))
                elif len(cashier.line) < len(temp_short.line):
                    temp_short = cashier
                    cashier.line.append(cust_lst[idx])
                    cust_lst.remove(idx)
                    for itmes in cashier_lst:
                        print(str(items))
                else:
                    cashier.line.append(cust_lst[idx])
                    cust_lst.remove(idx)
                    for itmes in cashier_lst:
                        print(str(items))
                    
        
        idx += 1
        clock += 1              
                       
                       
                       
            
            
                
                
        break
                
                
                
                
        
    
    

        
    

        

    
