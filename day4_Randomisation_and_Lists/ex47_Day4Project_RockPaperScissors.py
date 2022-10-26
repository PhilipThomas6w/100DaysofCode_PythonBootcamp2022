# This is a very simple "Rock, Paper, Scissors" game constructed using if/elif statements and the random.choice()
# function.


import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


player1 = input("Rock, paper, or scissors?\n")

if player1.lower() == "rock":
    print(rock)
elif player1.lower() == "paper":
    print(paper)
elif player1.lower() == scissors:
    print(scissors)

x = [rock, paper, scissors]

computer = random.choice(x)
print(f"Computer chooses {computer}.")

if player1.lower() == "rock" and computer == rock:
    print("It's a draw...")
elif player1.lower() == "rock" and computer == paper:
    print("You lose!")
elif player1.lower() == "rock" and computer == scissors:
    print("You win!")
elif player1.lower() == "paper" and computer == rock:
    print("You win!")
elif player1.lower() == "paper" and computer == paper:
    print("It's a draw...")
elif player1.lower() == "paper" and computer == scissors:
    print("You lose!")
elif player1.lower() == "scissors" and computer == rock:
    print("You lose!")
elif player1.lower() == "scissors" and computer == paper:
    print("You win!")
elif player1.lower() == "scissors" and computer == scissors:
    print("It's a draw...")