# write "Would you like to play a game?" to the console
print("Would you like to play a game?")

# import the random module
import random

#create a list of options
options = ["rock", "paper", "scissors"]

#create the score and round played variables
score = 0
rounds_played = 0

#while loop to keep the game going
while True:
    #get the user's choice
    user_choice = input("Choose rock, paper, or scissors: ")
    #get the computer's choice
    computer_choice = random.choice(options)
    #print the computer's choice
    print(f"Computer chose {computer_choice}")
    #check for a tie
    if user_choice == computer_choice:
        print("It's a tie!")
    #check for rock
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("You lose!")
            score -= 1
        else:
            print("You win!")
            score += 1
    #check for paper
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("You lose!")
            score -= 1
        else:
            print("You win!")
            score += 1
    #check for scissors
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("You lose!")
            score -= 1
        else:
            print("You win!")
            score += 1
    #print the score
    print(f"Score: {score}")
    #increment the rounds played
    rounds_played += 1
    #ask the user if they want to play again
    play_again = input("Would you like to play again? (y/n) ")
    #if the user doesn't want to play again, break out of the loop
    if play_again != "y":
        break
#print the number of rounds played
print(f"You played {rounds_played} rounds")







