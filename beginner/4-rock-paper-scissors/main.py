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

#Write your code below this line 👇
ascii_images = [rock, paper, scissors]
computer_choice = random.choice([0, 1, 2])
user_choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
if user_choice not in [0, 1, 2]:
  print("Invalid choice.")
else:
  print(ascii_images[user_choice])
  print("Computer Choose: ")
  print(ascii_images[computer_choice])
  
  if user_choice == computer_choice:
    print("Its a Draw")
  elif user_choice == 0:
    if computer_choice == 1:
      print("You Loose")
    else:
      print("You Win")
  elif user_choice == 1:
    if computer_choice == 2:
      print("You Loose")
    else:
      print("You Win")
  elif user_choice == 2:
    if computer_choice == 0:
      print("You Loose")
    else:
      print("You Win")
  else:
    print("Choose either 1 or 2 or 3 accordingly.")
  