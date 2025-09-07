# Dice Battle
 
import random

# Computer choices

def computer_choice():

    computer_choice = random.randint(1,6)
    return computer_choice

# Player Choice
def user_choice():

    while True:
        try:
            player_inp = int(input("Role the dice: "))

            if(1<=player_inp<=6):
                return player_inp
            else:
                print("There are six number in dice. Please provide valid input")
        except ValueError:
            print("Invalid Input")

# Logic for Game
def play_game():


    computer_score = 0
    player_score = 0

    print("Welcome to the Dice Battle!")

    for round_num in range(1,6):

        print(f"\n--Round {round_num}---")

        user_num = user_choice()
        computer_num = computer_choice()

        if(user_num > computer_num):
            player_score +=1
            print(f"Player has won round {round_num}")
        elif(user_num<computer_num):
            computer_score +=1
            print(f"Computer has won this round {round_num}")
        elif(user_num == computer_num):
            print(f"{round_num} round was a tie")

    if(computer_score<player_score):
        print(f"\nPlayer has won by {player_score}")
    elif(computer_score>player_score):
        print(f"\nComputer has won by {computer_score} points")
    else:
        print(f"\nIt was a tie!")

play_game()