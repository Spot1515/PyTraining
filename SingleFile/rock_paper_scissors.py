import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Please enter a valid input.")
        continue

    computer_action = random.randint(0,2) 
    # 0 is rock, 1 is paper, 2 is scissors

    if user_input == options[0]:
        user_action = 0
    elif user_input == options[1]:
        user_action = 1
    else: # scissors
        user_action = 2 

    if user_action == computer_action:
        print(f"\nBoth players selected {options[user_action]}. It's a tie!\n")
    elif ((user_action == 0 and computer_action == 1) or 
          (user_action == 1 and computer_action == 2) or
          (user_action == 2 and computer_action == 0)):
        print(f"\nComputer selected {options[computer_action]}. You lose!\n")
        computer_wins += 1
    elif ((user_action == 0 and computer_action == 2) or
          (user_action == 1 and computer_action == 0) or
          (user_action == 2 and computer_action == 1)):
        print(f"\nComputer selected {options[computer_action]}. You Win!\n")
        user_wins += 1

 #   elif user_action == 0 and computer_action == 1:
 #       print(f"Computer selected {options[computer_action]}. You lose!")
 #       computer_wins += 1
 #   elif user_action == 0 and computer_action == 2:
 #       print(f"Computer selected {options[computer_action]}. You Win")
 #       user_wins += 1
 #   elif user_action == 1 and computer_action == 0:
 #       print(f"Computer selected {options[computer_action]}. You Win")
 #       user_wins += 1
 #   elif user_action == 1 and computer_action == 2:
 #       print(f"Computer selected {options[computer_action]}. You lose!")
 #       computer_wins += 1
 #   elif user_action == 2 and computer_action == 0:
 #       print(f"Computer selected {options[computer_action]}. You lose!")
 #       computer_wins += 1
 #   elif user_action == 2 and computer_action == 1:
 #       print(f"Computer selected {options[computer_action]}. You Win")
 #       user_wins += 1

    print(f"Score Count: Player Wins {user_wins} | Computer Wins {computer_wins}\n")




    

    #["rock", "paper", "scissors"]