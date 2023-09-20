from datetime import datetime
import random
from game import Game



if __name__ == "__main__":
    # Create an instance of the Game class
    game = Game()

    # Print a welcome message to the player
    print("\nWelcome to Lucky Number!\n")

    # Provide an introduction to the game
    print("In this game, you'll have the chance to test your luck.")
    print("Here's how it works:")
    print("1. Enter your full name and birthdate to get started.")
    print("2. We'll generate a list of lucky numbers.")
    print("3. Your goal is to guess the lucky number from the list.")
    print("4. You can keep guessing until you get it right or there are only 2 numbers left.")
    print("5. Let's see if you have what it takes to find the lucky number!\n")

    # Get the player's name using the game object
    name = game.get_player_name()

    # Get the player's birthdate using the game object
    game.get_player_birthdate()

    # Calculate the player's age using the game object
    game.calculate_player_age()

    # Check if the player's age meets the eligibility criteria
    game.check_age_eligibility()

    # Print a message indicating that the game will begin
    print(f"\n★ {name}, Let the game begin ★\n")

    # Generate a list of lucky numbers using the game object
    game.generate_lucky_list()

    # Generate the lucky number that the player needs to guess
    game.generate_lucky_number()

    # Ask the player for their input (guess)
    game.ask_for_player_input()

    # Handle the case where the player's guess is wrong
    game.handle_wrong_guess()

    # Congratulate the player on guessing the
    # lucky number and display the number of tries
    game.congratulate_player(game.tries_count)

    # Ask the player if they want to play the game again
    game.play_again()
