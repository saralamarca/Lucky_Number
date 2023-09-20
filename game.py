from datetime import datetime
import random



class Game:
    """
    A class representing the Lucky Number game.

    This class encapsulates the logic for the Lucky Number game,
    where the player provides their name and birthdate, attempts
    to guess a lucky number, and plays until they find the lucky number
    or there are only 2 numbers left in the list.
    
    Attributes:
        player_name (str): The player's name.
        player_birthdate (str): The player's birthdate in YYYYMMDD format.
        player_age (int): The player's age calculated from their birthdate.
        lucky_list (list): A list of 10 random integers between 0 and 100.
        lucky_number (int): The lucky number that the player aims to guess.
        tries_count (int): Count the number of times the player has guessed.

    """
    def __init__(self) -> None:
        """
        Initialize the Game instance.
            
        Args:
            None
        """
        self.player_name = ""
        self.player_birthdate = ""
        self.player_age = 0
        self.lucky_list = []
        self.lucky_number = 0
        self.tries_count = 1


    def get_player_name(self):
        """
        Ask the player for their first name.
        Validate that it contains only characters,
        capitalize the first letter and
        save it. If the input is not valid,
        prompt the user to input again.

        Return:
            string:
                A string containing the player name.
        """
        while True:
            # Prompt the user to enter their full name
            # and store it in self.player_name
            self.player_name = input("Enter your first name: ")
            # Check if input contains only alphabetical characters
            if self.player_name.isalpha():
                # If the input is valid,
                # capitalize the first letter of the name
                self.player_name = self.player_name.capitalize()
                # Return the capitalized name
                return self.player_name
            else:
                # If the input is not valid 
                # (contains non-alphabetical characters),
                # print error message and
                # loop to prompt for input again
                print("Invalid input. \n"
                      "Your game name can only contain characters.")


    def get_player_birthdate(self):
        """
        Ask the player for their birthdate.
        Validate that it contains only digits
        and save it. If the input is not valid,
        prompt the user to input again.

        Return:
            int:
                An integer containing the player age.
        """
        while True:
            # Ask the user for their birthdate
            birthdate_input = input("Enter your birthdate (YYYYMMDD): ")

            # Check if the input has 8 characters and consists of digits
            if len(birthdate_input) == 8 and birthdate_input.isdigit():
                year = int(birthdate_input[:4])
                month = int(birthdate_input[4:6])
                day = int(birthdate_input[6:8])

                # Validate year, month and day ranges
                if 1900 <= year <= 9999 and 1 <= month <= 12 and \
                     1 <= day <= 31:
                    self.player_birthdate = birthdate_input
                    # Return the valid input
                    return self.player_birthdate
                else:
                    print("Invalid date. Please enter a valid date.")
            else:
                print("Invalid format. Please use YYYYMMDD format.")


    def calculate_player_age(self):
        """
        Calculate the player's age from their birthdate and save it.
        """
        # Get the current year
        current_year = datetime.now().year
        # Extract the year part from the birthdate
        birth_year = int(self.player_birthdate[:4])
        # Calculate the age
        self.player_age = current_year - birth_year


    def check_age_eligibility(self):
        """
        Check if the player is 18 years or older.
        If they are - set the eligibility_checked attribute.
        If they're not - raise an AgeEligibilityError.
        """
        if self.player_age >= 18:
            return self.player_age
        else:
            print("You must be 18 years or older to play this game.\n"\
                  "Exiting the game.")
            exit()


    def generate_lucky_list(self):
        """
        Generate a list of 9 integers between 0-100 and 
        save it in the lucky_list attribute.
        """
        self.lucky_list = [random.randint(0, 100) for _ in range(9)]


    def generate_lucky_number(self):
        """
        Generate a lucky number between 0 and 100 and
        add it to the lucky_list.
        """
        self.lucky_number = random.randint(0, 100)
        # Add the lucky number to the lucky_list
        self.lucky_list.append(self.lucky_number)
        print(self.lucky_list)


    def ask_for_player_input(self):
        """
        Continuously prompts the player for input
        and handles guesses and errors.
        """
        while True:
            try:
                # Capture player's input
                self.player_input = int(input("Pick a number from the list: "))
                
                # Check if the player's input is in the lucky_list
                if self.player_input in self.lucky_list and self.player_input == self.lucky_number:
                    self.congratulate_player(self.tries_count)
                    if not self.play_again():
                        print("Thank you for playing! Goodbye.")
                        exit()
                    return
                # Handle cases where input is in lucky_list but doesn't match lucky_number
                elif self.player_input in self.lucky_list and self.player_input != self.lucky_number:
                    self.handle_wrong_guess()
                else:
                    print("Invalid choice. Pick a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")

            # Increment tries_count each time the player guesses
            self.tries_count += 1


    def handle_wrong_guess(self):
        """
        Handle the case when the player's guess is wrong.
        Generates a new shorter list by removing the guessed number
        and numbers differing by 10 or less from the lucky number.
        """
        # Check if the lucky number is in the lucky_list
        if self.lucky_number in self.lucky_list:
            # Remove the guessed number from the list
            self.lucky_list.remove(self.player_input)

        # Generate a new shorter list
        self.shorter_lucky_list = [num for num in self.lucky_list if \
                                   abs(num - self.lucky_number) <= 10]

        # Check if there are enough numbers for another guess
        if len(self.shorter_lucky_list) >= 2:
            print(f"Wrong number. This was your {self.tries_count} try.\n"
                f"Let's try again from a shorter list.\n"
                f"{self.shorter_lucky_list}")
        else:
            # If there are not enough numbers in the shorter list
            print("GAME OVER")
            self.play_again()
            exit()


    def congratulate_player(self, tries_count):
        """
        Congratulate the player if they guessed the lucky number.
        
        Args:
            tries_count (int): The number of attempts made by the player.
        """
        print(f"Congratulations!\n"
              f"You got the lucky number from try {tries_count}\n")


    def play_again(self):
        """
        Allows the player to decide whether to play another round.
        Handles player input for different scenarios.
        """
        while True:
            # Prompt the player for input and remove
            # leading/trailing whitespace, make it lowercase
            play_again = input \
                ("Do you want to play again?\n (y: Yes, n: No): ")\
                .strip().lower()
            if play_again == 'y':
                # Start a new round
                self.start_new_round()
            elif play_again == 'n':
                # Exit the game
                self.exit_game()
            else:
                # Handle invalid input
                self.handle_invalid_input()


    def start_new_round(self):
        """
        Reset game state and start a new round.
        """
        # Reset the number of tries
        self.tries_count = 1
        # Generate a new list of lucky numbers
        self.generate_lucky_list()
        # Generate a new lucky number
        self.generate_lucky_number()
        # Ask for the player's input in the new round
        self.ask_for_player_input()


    def exit_game(self):
        """
        Exit the game.
        """
        # Print a message and exit the game
        print("Thank you for playing! Goodbye.")
        exit()


    def handle_invalid_input(self):
        """
        Handle invalid input from the player.
        """
        # Print an error message for invalid input
        print("Invalid input. Enter 'y' for Yes or 'n' for No.")

