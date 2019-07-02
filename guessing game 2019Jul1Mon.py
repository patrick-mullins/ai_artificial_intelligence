"""guessing game 2019Jul1Mon p1. In this project the guess game is recast using a function."""

import random

computers_number = random.randint(1,1000)
PROMPT = 'What is your guess? '

def do_guess_round():
    """Choose a random number, ask the user for a guess check whterh the guess is true and repeat until the user is correct."""
    computers_number = random.randint(1,100) #Added while true:
        players_guess = raw_input(PROMPT)
        if computers_number == int(players_guess)
            print('Correct! ')
            break
        elif computers_number > int(players_guess):
            print('Too LOW ')
        else:
            print('Too HIGH! ')


while True:
    players_guess = raw_input(prompt)
    print('Correct! ')
    break
elif computers_number > int(players_guess):
    print('Too LOW ')
else:
    print('Too HIGH! ')

do_guess_round


