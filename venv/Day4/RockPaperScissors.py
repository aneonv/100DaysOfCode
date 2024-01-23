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
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
player = int(player_choice)
computer = random.randint(0, 2)
if player == 0:
  print(f"Player chose Rock {rock}")
  if computer == 0:
      print(f"Computer chose Rock {rock}")
  elif computer == 1:
      print(f"Computer chose Paper {paper}")
  else:
      print(f"Computer chose Scissors {scissors}")
elif player == 1:
  print(f"Player chose Paper {paper}")
  if computer == 0:
      print(f"Computer chose Rock {rock}")
  elif computer == 1:
      print(f"Computer chose Paper {paper}")
  else:
      print(f"Computer chose Scissors {scissors}")
elif player == 2:
  print(f"Player chose Scissors {scissors}")
  if computer == 0:
      print(f"Computer chose Rock {rock}")
  elif computer == 1:
      print(f"Computer chose Paper {paper}")
  else:
      print(f"Computer chose Scissors {scissors}")
else:
  print("Player chose wrong number. Try again.")

if player == computer:
    print("Its a tie. Play again.")
elif (player == 0 and computer == 2):
    print("Player won the game.")
elif (player == 0 and computer == 1):
    print("Computer won the game.")
elif (player == 1 and computer == 2):
    print("Computer won the game.")
elif (player == 1 and computer == 0):
    print("Player won the game.")
elif (player == 2 and computer == 1):
    print("Player won the game.")
elif (player == 2 and computer == 0):
    print("Computer won the game.")

