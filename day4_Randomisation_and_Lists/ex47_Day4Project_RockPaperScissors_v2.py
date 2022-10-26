# This is a very simple "Rock, Paper, Scissors" game constructed using nested lists i.e., matrices (a matrix is simply
# a nested list).


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


# There are 9 possible scenarios: (0, 0) (0, 1) (0, 2) (1, 0) (1, 1) (1, 2) (2, 0) (2, 1) (2, 2), where (0, 0) is
# (rock, rock), for example. We will construct a 3x3 nested list i.e., a 3x3 matrix, and call it "possibility matrix".

p1_rock = ["You draw.", "Tie.", "You win!"]
p1_paper = ["You win!", "Tie.", "You lose."]
p1_scissors = ["You lose.", "You win!", "Tie."]

possibility_matrix = [p1_rock, p1_paper, p1_scissors]

p1_choice = int(input("Rock (1), paper (2), or scissors (3)? Make your choice!\n"))

if p1_choice == 1:
    print(rock)
elif p1_choice == 2:
    print(paper)
elif p1_choice == 3:
    print(scissors)
else:
    print("Invalid input.")

comp_choice = int(random.randint(0, 2))

if comp_choice == 0:
    print(rock)
elif comp_choice == 1:
    print(paper)
elif comp_choice == 2:
    print(scissors)
else:
    print("Invalid input.")

print(f"{possibility_matrix[p1_choice - 1][comp_choice]}")




