"""Rock paper scissors, by ChronosWithA-K, coded for fun"""
import random # allows for randomized choices / values
import os # allows for clear()

responses = ['rock', 'paper', 'scissors']
valid_responses = ['rock', 'paper', 'scissors']

play_again = 'yes'

def clear():
    """Clear terminal text."""
    os.system('clear')

def opponent_choice():
    """Lets the robot respond."""
    global opponent_response
    response_type = random.randint(1, 2)
    if response_type == 1:
        opponent_response = random.choice(responses)
    opponent_response = random.choice(['rock', 'paper', 'scissors'])

def player_lose():
    """Lets the player play again if they lose."""
    global play_again
    play_again = input(f"\nYou lost (you chose {choice}, and your opponent chose\
 {opponent_response}). Do you want to play again (yes / no)? ")
    while play_again != 'yes' and play_again != 'no':
        play_again = input("That is not a valid input. Do you want to play again (yes / no)? ")
        clear()

def player_win():
    """Lets the player play again if they win."""
    global play_again
    play_again = input(f"""\nYou won (you chose {choice} and your opponent chose \
 {opponent_response})! Do you want to play again (yes / no)? """)
    while play_again not in ('yes', 'no'):
        play_again = input("\nThat is not a valid input. Do you want to play again (yes / no)? ")
        clear()

clear()
name = input("\nHello user. What's your name? ")
clear()
print(f"\nNow then {name.title()}, are you ready to play some Rock Paper Scissors?")
input("(enter to continue)")
clear()
get_it = input("""\nThe rules to the game are as follows: when it's time to choose between rock,\
 paper, and scissors, type in either 'rock', 'paper', or 'scissors'. Then your opponent will make a move!\
 They will choose between rock, paper, and scissors, and then you will see who won. Ready to\
 play (y / n)? """)
clear()
while get_it != 'y':
    get_it = input("""\nThe rules to the game are as follows: when it's time to choose between rock\
, paper, and scissors, type in either 'rock', 'paper', or 'scissors'. Then your opponent will make a move!\
 They will choose between rock, paper, and scissors, and then you will see who won? Ready to play\
 (y / n)? """)
    clear()

while play_again == 'yes':
    choice = input("\nDo you want to choose rock, paper, or scissors? ")
    clear()
    while choice not in valid_responses:
        choice = input("That was not a valid response. Choose either rock, paper, or scissors: ")
        clear()
    opponent_choice()

    if choice == opponent_response:
        print(f"You both chose {choice}.")

    if choice == 'rock':
        responses.append('paper')
    if choice == 'paper':
        responses.append('scissors')
    if choice == 'scissors':
        responses.append('rock')

    if choice == 'rock' and opponent_response == 'paper':
        player_lose()
    if choice == 'paper' and opponent_response == 'scissors':
        player_lose()
    if choice == 'scissors' and opponent_response == 'rock':
        player_lose()

    if choice == 'rock' and opponent_response == 'scissors':
        player_win()
    if choice == 'paper' and opponent_response == 'rock':
        player_win()
    if choice == 'scissors' and opponent_response == 'paper':
        player_win()
