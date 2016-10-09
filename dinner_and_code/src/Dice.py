'''
Created on Oct 8, 2016

@author: Ed
'''

from builtins import input
import random

def roll (sides=6):
    num_rolled = random.randint(1, sides)
    return num_rolled

def main():
    sides =6
    rolling = True
    while rolling:
        roll_again = input("Ready to roll? ENTER=Roll. Q=Quit. ")
        if roll_again.lower() !="q":
            num_rolled = roll(sides)
            
            print("You rolled a {}".format(num_rolled))
        else:
            rolling = False
            
    print("Thanks for playing! :D")
    
main()
