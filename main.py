import random

#Choices
choices = ["rock", "paper", "scissors"]
while True:
  #Get user input
  user_input = input("Enter rock, paper or scissors(or press q to quit): ").lower()

  #Quit
  if user_input == "q":
    print("Thank you for playing!😊")
    break

  #Check if user input is valid
  if user_input not in choices:
    print("Invalid input. Please try again.❌")
    continue
  
  #Computer choice
  computer_choice = random.choice(choices)
  
  #Show Choices
  print(f"You chose {user_input}, computer chose {computer_choice}.")
  
  #Conitions
  if user_input == computer_choice:
    print("It's a tie!")
  elif (
    (user_input == "rock" and computer_choice == "scissors")or
    (user_input == "paper" and computer_choice == "rock")or
    (user_input == "scissors" and computer_choice == "paper")
  ):
    print("You win!")
  else:
    print("You lose!")