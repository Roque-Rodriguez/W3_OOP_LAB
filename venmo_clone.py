"""
Remove all of the code in main.py. Inside main.py, create a new class called Person.

This class should have the following instance variables:
A string that represents the name of the person.
The initial value of this instance variable should be set with a parameter.
An integer that represents the amount of money the person has in their account.
The initial value of this instance variable should be set with a parameter.

Write two methods for this class:
Method #1: Remove money from the account balance by subtracting the total amount by an amount passed in via a parameter.
The subtracted amount should be returned from the method
If there are not enough funds to support the removal of money, print a console message stating, “Insufficient funds available!”.
Method #2: Add money to the account balance of the current object.
Take the amount to add into the method as a parameter.
Take the name of the person the money is being received from as a parameter.
Print the new balance and the name of the person who transferred the money to you to the console.

Create two objects: person_one  and person_two. Have person_one send $100 to person_two.
Remember to:
Create your two objects by creating new variables and setting them equal to the class with parenthesis. Include the initial values for their names and account balances.
Call methods using dot notation, sending any values needed for those methods as arguments.

"""

class Person:

    def __init__(self, name_passed_in, cash_passed_in):
        self.name = name_passed_in
        self.cash = cash_passed_in

    def removing_money(self, cash):
       if player_one.cash <= cash:
        print(f'{player_one.name} does not have enough funds for this transaction.')
       else:
        player_one.cash -= cash
        player_two.cash += cash

    
    
        


# player_one = Person("Rocky", 700)
# player_two = Person("Adrian", 1000)

# player_one.removing_money(800)
# print(player_one.cash)
# print(player_two.cash)  #This code works as normally check if player one has enough funds and if not it will deny the transaction going thru and prints their current money else it will remove the amount out and add it to the other and print
                        #the new amount the players have.  Dont know if you were trying for us to have more funtions.  Let me know if I need to rewrite the code please.



    
