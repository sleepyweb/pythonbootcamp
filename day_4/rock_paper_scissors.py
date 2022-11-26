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

rps = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user >= 3 or user < 0:
    print("You typed an invalid number, you lose")
else:
    print(rps[user])

    print("Computer chose:")
    computer = random.randint(0, 2)
    print(rps[computer])


    if computer == 0 and user == 2:
        print("You lose")
    elif user == 2 and computer == 0:
        print("You win")
    elif computer > user:
        print("You lose")
    elif user > computer:
        print("You win")
    elif user == computer:
        print("It's a draw")
