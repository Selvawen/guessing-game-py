# Import the 'random' module to generate random numbers

import random

# Define a function called 'display_title' to display the game's title and instructions

def display_title():
    print("Welcome to the Number Guessing Game!")  # Display a welcome message
    print("Guess a number between 1 and 10.")  # Instruct the player on how to play

# Define a function called 'play_game' to handle the game logic
    
def play_game():

    # Generate a random number between 1 and 10 and store it in 'random_number' variable

    random_number = random.randint(1, 10)
    
    # Use a while loop to allow the player to keep guessing until they get the correct number

    while True:

        # Prompt the player to input their guess and convert it to an integer

        guess = int(input("Enter your guess: "))
        
        # Check if the guess is lower than the random number

        if guess < random_number:
            print("Too low")  # Display a message indicating the guess was too low
        
        # Check if the guess is higher than the random number
            
        elif guess > random_number:
            print("Too high")  # Display a message indicating the guess was too high
        
        # If the guess matches the random number, the player guessed it correctly
            
        else:
            print("You guessed it!")  # Display a congratulatory message
            return  # Exit the function and return to the main program

# Define a function called 'main' to orchestrate the main flow of the program
        
def main():
    display_title()  # Call the 'display_title' function to show the game title and instructions
    
    # Initialize a variable 'play_again' with the value 'yes'

    play_again = "yes"
    
    # Use a while loop to allow the player to play the game multiple times if they want

    while play_again.lower() == "yes":
        play_game()  # Call the 'play_game' function to start the game
        
        # Ask the player if they want to play again and store their response in 'play_again' variable

        play_again = input("Do you want to play again? (yes/no): ")

# Check if the script is being run directly
        
if __name__ == "__main__":
    main()  # Call the 'main' function to start the program
