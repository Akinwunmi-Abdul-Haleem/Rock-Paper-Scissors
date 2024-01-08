import random


# Player Info
def get_player_choice():
    player_choice = input("Input either Rock, Paper or Scissors:").lower()
    while player_choice not in ("rock", "paper", "scissors"):
        print("Invalid input, \n Input allowed is Rock, Paper, Scissors")
        player_choice = input("Input either Rock, Paper or Scissors:").lower()
    return player_choice


# Computer Info
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


# Determine Winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "The game is a tie!!"
    elif player_choice == "rock" and computer_choice == "scissors" or \
            player_choice == "scissors" and computer_choice == "paper" or \
            player_choice == "paper" and computer_choice == "rock":
        return "You win!!"
    else:
        return "Computer Win"


# Gameplay
def gameplay():
    print("Lets play a game of Rock, Paper and Scissors")
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    print("Player Input is " + player_choice)
    print("Computer Input is " + computer_choice)
    result = determine_winner(player_choice, computer_choice)

    print(result)


gameplay()
