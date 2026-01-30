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
choice = [rock, paper, scissors]
computerChoice = random.choice(choice)

playerNumber = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if playerNumber > 2:
    print("Please make a valid selection")
match playerNumber:
    case 0:
        playerChoice = rock
    case 1:
        playerChoice = paper
    case 2:
        playerChoice = scissors

print(playerChoice)
print("Computer chose:")
print(computerChoice)

computerNumber = choice.index(computerChoice)

if playerNumber == computerNumber:
    print("Draw!")
elif (
    (playerNumber == 0 and computerNumber == 1) or
    (playerNumber == 1 and computerNumber == 2) or
    (playerNumber == 2 and computerNumber == 0)
):
    print("Computer wins!")
else:
    print("You win!!")
