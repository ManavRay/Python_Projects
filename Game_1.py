# Stone , Paper, Scissor
import random

def play_round():

    # Inputs form Computer and Player
    computer_int = random.randint(1,3)

    player_inp = input("Player Choice(Stone, Paper, Scissor): ").capitalize()

    # Mapping
    choice = {
        1:"Stone",
        2:"Paper",
        3:"Scissor"
    }

    rev_choice = {
        "Stone":1,
        "Paper":2,
        "Scissor":3
    }

    # Condition for input having only three choices
    if player_inp not in rev_choice:
        print("Invalid Input")
        return None
    player_int = rev_choice[player_inp]

    print(f"Player choice {player_inp}")
    print(f"Computer choice {choice[computer_int]}")

    # To decide winner

    if(player_int == computer_int):
        return 1
    elif(player_int == 1 and computer_int == 2 or player_int == 3 and computer_int == 1 or player_int == 2 and computer_int == 3):
        return 2
        # Computer win
    else:
        return 3
        # Player win

# Starts The game
def play_game():
    # Initializing the score
    computer_score = 0
    player_score=0

    for round_num in range(1,6):
        print(f"\n---{round_num}---")
        result = play_round()
        if(result == 2):
            computer_score+=1
            print("Computer has Won this round")
        elif(result == 3):
            player_score+=1
            print("Player has won this round")
        elif(result ==1):
            print("It was a tie")

    # Declare the result
    if(computer_score > player_score):
        print(f"Computer has won this game by {computer_score} point")
    elif(computer_score <player_score):
        print(f"Player has won this game by {player_score} point")
    else:
        print(f"It was a tie! by {player_score} score")

play_game()