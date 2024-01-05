import random
import math
computer_input = ["rock", "scissors", "paper"]
scatter = math.floor(random.random() * 10)
much = computer_input * scatter
y = random.choice(much)
player_input = input("Your Input: ")
x = player_input.lower()
if x == y:
    print(f"Your Input = {x}\n Computer Input = {y}\n That is a draw")
elif x == "rock" and y == "scissors":
    print(f"Your Input = {x}\n Computer Input = {y}\n rocks Breaks scissors\n You win!!!")
elif x == "paper" and y == "rock":
    print(f"Your Input = {x}\n Computer Input = {y}\n paper Captures rock\n You win!!!")
elif x == "scissors" and y == "paper":
    print(f"Your Input = {x}\n Computer Input = {y}\n scissors Tears paper\n You win!!!")
elif x == "scissors" and y == "rock":
    print(f"Your Input = {x}\n Computer Input = {y}\n rocks Breaks scissors\n You lose!!!")
elif x == "paper" and y == "scissors":
    print(f"Your Input = {x}\n Computer Input = {y}\n scissors Tears paper\n You lose!!!")
elif x == "rock" and y == "paper":
    print(f"Your Input = {x}\n Computer Input = {y}\n paper Captures rock\n You lose!!!")
else:
    print("Input allowed is only Rock, Paper, Scissors")
