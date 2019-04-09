#!/usr/bin/env python3

"""
     Rock, Paper, Scissors Game.
     Rules of the Game:
        The objective of Rock, Paper, Scissors is to defeat your opponent by selecting a weapon that defeats their choice under the following rules:
        * Rock smashes (or blunts) Scissors, so Rock wins
        * Scissors cut Paper, so Scissors win
        * Paper covers Rock, so Paper wins
        * If players choose the same weapon, neither win and the game is played again
"""

import random


def eval_winner(p1, p2):
    """
    This function will check if player one or player two is going to win the turn.
    :param p1: Player One
    :param p2: Player Two
    :return: a 0 if there is a tie, 1 if player 1 wins, and a 2 if player 2 wins.
    """
    if (p1 == 'r' and p2 == 's'):
        print('Player 1 chose ' + playerInput + ' - Player 2 chose ' + CPU)
        print('Player 1 Win\n')
        return 1
    elif (p1 == 's' and p2 == 'r'):
        print('Player 1 chose ' + playerInput + ' - Player 2 chose ' + CPU)
        print('Player 2 Win\n')
        return 2
    elif (p1 == 's' and p2 == 'p'):
        print('Player 1 chose ' + playerInput + ' - Player 2 chose ' + CPU)
        print('Player 1 Win\n')
        return 1
    elif (p1 == 'p' and p2 == 's'):
        print('Player 1 chose ' + playerInput + ' - Player 2 chose ' + CPU)
        print('Player 2 Win\n')
        return 2
    elif (p1 == 'p' and p2 == 'r'):
        print('Player 1 chose ' + playerInput + ' - Player 2 chose ' + CPU)
        print('Player 1 Win\n')
        return 1
    elif (p1 == 'r' and p2 == 'p'):
        print('Player 1 chose ' + playerInput + ' - Player 2 chose ' + CPU)
        print('Player 2 Win\n')
        return 2
    elif (p1 == p2 or p2 == p1):
        print('Player 1 chose ' + playerInput + ' - Player 2 chose ' + CPU)
        print('Match Tie')
        return 0


# Create a weapon list
weapon = ['r', 'p', 's']

print('Round Started\n'
      'Valid Choices are:\n '
      'P or p (Paper)\n '
      'R or r (Rock)\n '
      'S or s (Scissor)\n '
      'Q or q (Quit)\n'
      'Please Enter your Weapon Choice: ')
# Assign any value to y variable to get into the while loop but not q letter
playerInput = 0
# While y not equal q value, get inside the while loop.
while playerInput != 'q':
    # Assign player two as CPU variable to random letter from weapon list.
    CPU = random.choice(weapon)

    while True:
        playerInput = input()
        # Convert input to lower case letter.
        playerInput = playerInput.lower()
        # Check if the input not in the weapon list.
        if playerInput not in ('r', 'p', 's', 'q'):
            # if not print this message.
            print("Entered wrong value please enter again.\n")
        else:
            # if the input is in the weapon list, get out of the if condition (do nothing)
            break
    # invoke eval_winner function and add CPU and playerInput as an argument.
    eval_winner(CPU, playerInput)


def main():
    """Run the script"""
    p1 = []
    p2 = []

    eval_winner(p1, p2)


if __name__ == "__main__":
    main()
    exit(0)
