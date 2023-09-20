

class Game:
    """
    A class...

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

    def input_player_name(self):
        """
        Ask the player for their first name,
        Validate that it contains only characters,
        capitalize the first letter,
        save it and print out message.

        Return:
            string:
            A string containing the player name.
        """
        while True:
            # Prompt the user to enter their full name
            # and store it in self.player_name
            self.player_name = input("Enter your full name: ")
            # Check if input contains only alphabetical characters
            if self.player_name.isalpha():
                # If the input is valid,
                # capitalize the first letter of the name
                self.player_name = self.player_name.capitalize()
                # Print a welcome message with the capitalized name
                print(f"★ Let the game begin {self.player_name} ★")
                # Return the capitalized name
                return self.player_name
            else:
                # If the input is not valid 
                # (contains non-alphabetical characters),
                # - print an error message and 
                # loop to prompt for input again
                print("Invalid input. \n"
                      "Your game name can only contain characters and/or whitespaces.")

    def input_player_birthdate(self):
        pass

    def calculate_player_age(self):
        pass

    def check_age_eligibility(self):
        pass

    def generate_lucky_list(self):
        pass

    def generate_lucky_number(self):
        pass

    def ask_for_player_input(self):
        pass

    def congratulate_player(self, tries_count):
        pass

    def ask_play_again(self):
        pass

    def generate_shorter_lucky_list(self):
        pass

    def ask_for_player_input_again(self, shorter_lucky_list):
        pass

    def handle_wrong_guess(self):
        pass



if __name__ == "__main__":
    game = Game()
    print("Welcome to the Lucky Number Game!")
    print("In this game, you'll have the chance to test your luck.")
    print("Here's how it works:")
    print("1. Enter your full name and birthdate to get started.")
    print("2. We'll generate a list of lucky numbers.")
    print("3. Your goal is to guess the lucky number from the list.")
    print("4. You can keep guessing until you get it right or there are only 2 numbers left.")
    print("5. Let's see if you have what it takes to find the lucky number!")
    
    game.input_player_name()