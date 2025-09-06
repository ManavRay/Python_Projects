# Random Number Guesser
import random

random_num = random.randint(1,10)

# Takes Number and validate it
def user_num():
    while True:
        try:
            player_inp = int(input("Guess number between 1 to 10: "))
            if (1<= player_inp<= 10):
                    return player_inp
            else:
                print("Invalid Input")
        except ValueError:
            print("Please enter a valid input")

# count the number of guesses
def play_game():
    no_guess = 0

    while True:
         player_num = user_num()
         no_guess += 1

         if(player_num > random_num):
              print("Your Guess is too high!")
         elif(player_num < random_num):
            print("Your Guess is too low!")
         elif(player_num == random_num):
            print("Congrats your guess is correct")
            print(f"Number of guesses {no_guess}")
            break
    
play_game()