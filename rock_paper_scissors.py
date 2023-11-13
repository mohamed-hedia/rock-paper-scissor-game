import random

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ")
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Congratulatin, You win")
    else:
        print("Sorry, Computer wins")

def play_again():
    return input("Do you want to play again? (yes/no): ") == "yes"

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")

    determine_winner(user_choice, computer_choice)

    if not play_again():
        break
