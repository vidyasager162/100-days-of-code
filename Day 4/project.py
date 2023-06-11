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

#Write your code below this line 👇
import random
print("Welcome to the Ultimate Showdown with Rock, Paper and Scissors!!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
pc_choice = random.randint(0,2)
if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
else:
  print(scissors)

print("Computer chose:")
if pc_choice == 0:
  print(rock)
elif pc_choice == 1:
  print(paper)
else:
  print(scissors)

if user_choice == pc_choice:
  print("Draw")
elif user_choice == 0:
  if pc_choice == 1:
    print("You lose")
  else:
    print("You win")
elif user_choice == 1:
  if pc_choice == 0:
    print("You win")
  else:
    print("You lose")
else:
  if pc_choice == 0:
    print("You lose")
  else:
    print("You win")