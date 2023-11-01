"""Rock paper scissors, by ChronosWithA-K, coded for fun."""

import random
import os

playing = True
player_has_bullet = False
opponent_has_bullet = False

valid_responses = ['reload', 'block', 'reflect', 'shoot']

def clear():
    """Clear terminal text."""
    os.system('clear')

def opponent_choice():
    """Lets the robot play."""
    global response
    global opponent_has_bullet

    if opponent_has_bullet:
        response = random.choice(['reflect', 'shoot', 'block'])
    else:
        response = random.choice(['reload', 'block', 'reflect'])
        if response == 'reload':
            opponent_has_bullet = True

def win():
    """Win logic for the player."""
    global playing
    global response
    global play_again
    global choice

    play_again = input(f"""\nYou won (you chose {choice} and your opponent chose {response}).\
 Do you want to play again (yes / no)? """)
    while play_again != 'yes' and play_again != 'no':
        play_again = input("That was not a valid response. Type in either yes or no. ")
        clear()

def lose():
    """Lose logic for the player."""
    global playing
    global response
    global play_again
    global choice

    play_again = input(f"""\nYou lost (you chose {choice} and your opponent chose {response}).\
 Do  you want to play again? """)
    while play_again != 'yes' and play_again != 'no':
        play_again = input("That was not a valid response. Type in either yes or no. ")

clear()

name = input("Hello user. What's your name? ")
print(f"Well then, {name.title()}, are you ready to play some Double Up Seven? ")
input("(enter to continue)")
clear()

understand = input("""The rules of the game are as follows: when it's time to choose\
 between reload, shoot, reflect, and block. Reloading gives you a bullet (you can only\
 have one bullet at a time). Shooting shoots your gun (you can only do this if you have a\
 bullet). Blocking lets you block a bullet that your opponent shot. Reflecting lets you\
 send a bullet that your opponent shot back at them (you cannot do this twice in a row). Do you\
 understand (yes / no)? """)
while understand != 'yes' and understand != 'no':
    understand = input("""The rules of the game are as follows: when it's time to choose\
 between reload, shoot, reflect, and block. Reloading gives you a bullet (you can only\
 have one bullet at a time). Shooting shoots your gun (you can only do this if you have a\
 bullet). Blocking lets you block a bullet that your opponent shot. Reflecting lets you\
 send a bullet that your opponent shot back at them (you cannot do this twice in a row). Do you\
 understand (yes / no)? """)
    clear()

while playing:
    # Logic for what the player can choose.
    if player_has_bullet:
        choice = input("Do you want to block, reflect, or shoot?")

        while choice not in valid_responses:
            choice = input("That was not a valid input. Do you want to block, reflect, or shoot? ")
            clear()
    else:
        choice = input("Do you want to reload, block, or reflect? ")
        clear()

        while choice not in valid_responses:
            choice = input("That was not a valid input. Do you want to reload, block, or reflect? ")
            clear()

    opponent_choice()

    if choice != 'reflect' and response == 'shoot':
        win()
    else:
        lose()
