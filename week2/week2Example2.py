# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 17:41:34 2020

@author: Eric
"""

import random

randNum = random.randint(1,10) # Picks a random number between 1 and 10
print('Pick a number between 1 and 10, type now')
guess = int(input()) # User input

def randomNumberFunc(): 
    if guess == randNum:
        print ('My number was also ' + str(randNum))
    if guess > randNum:
        print('You guessed too high!')
    if guess < randNum:
        print('You guessed too low!')
        
randomNumberFunc()

# Allow the user to have a second chance at guessing
if guess != randNum:
    print('Try again!')
    guess = int(input())
    randomNumberFunc()
else:
    print('You win!') 