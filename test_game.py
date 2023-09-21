import io
import sys
from io import StringIO
import unittest
from unittest.mock import patch, Mock
from game import Game



class TestGame(unittest.TestCase):
    """
    A class for testing the Game class.
    """
    def setUp(self):
        """
        This method sets up a new Game instance for each test.
        """
        self.game = Game()


    # Mock user input as "Gullbritt"
    @patch("builtins.input", side_effect=["Gullbritt"])
    def test_get_player_name_valid_input(self, mock_input):
        """
        Test the get_player_name method with valid input.

        This test case checks if the get_player_name method correctly
        returns the player's name when valid input is provided.

        Assertion:
        - Method returns the expected player name "Gullbritt".
        """
        # Assert that get_player_name returns "Gullbritt"
        self.assertEqual(self.game.get_player_name(), "Gullbritt")


    # Mock user input as "123Gullbritt" and then "Gullbritt"
    @patch("builtins.input", side_effect=["123Gullbritt", "Gullbritt"])
    def test_get_player_name_invalid_input_then_valid_input(self, mock_input):
        """
        Test the get_player_name method - invalid and valid input.

        This test case verifies that the get_player_name method
        handles invalid input by reprompting the user and correctly
        returns the valid input.

        Assertions:
        - The method returns the valid player name "Gullbritt."
        - "Invalid input." is in the captured output.
        """
        with StringIO() as mock_output:
            with patch("sys.stdout", mock_output):
                # Assert that get_player_name returns "Gullbritt"
                self.assertEqual(self.game.get_player_name(), "Gullbritt")
                # Get the output from mock_output
                output = mock_output.getvalue()
                # Assert that "Invalid input." is in the captured output
                self.assertIn("Invalid input.", output)


    # Mock user input as "19901231"
    @patch("builtins.input", side_effect=["19901231"])
    def test_get_player_birthdate_valid(self, mock_input):
        """
        Test the get_player_birthdate method with a valid date.

        This test case checks if the get_player_birthdate method
        correctly captures and returns a valid birthdate entered
        by the player.

        Assertion:
        - The method returns the entered valid birthdate as a string.
        """
        # Ensure the returned value matches the input
        self.assertEqual(self.game.get_player_birthdate(), "19901231")


    # Mock user input as "19901331" and then "19901231"
    @patch("builtins.input", side_effect=["19901331", "19901231"])
    def test_get_player_birthdate_invalid_then_valid_(self, mock_input):
        """
        Test the get_player_birthdate method - invalid and valid dates.

        This test case checks if the get_player_birthdate method
        handles an invalid date input followed by a valid date
        input correctly. It also verifies the error message in the output.

        Assertions:
        - Method returns the valid date "19901231".
        - Error message is present in the output for the invalid date input.
        """
        with StringIO() as mock_output:
            with patch("sys.stdout", mock_output):
                # Assert that get_player_birthdate returns "19901231".
                self.assertEqual(self.game.get_player_birthdate(), "19901231")
                output = mock_output.getvalue()
                # Verify an error message is present in the output
                self.assertIn("Invalid date. Please enter a valid date.", \
                              output)


    def test_calculate_player_age(self):
        """
        Test the calculate_player_age method of the Game class.

        This test case checks if the calculate_player_age method
        correctly calculates the player's age based on their birthdate
        and assigns it to the player_age attribute.

        Assertions:
        - Method calculates the player's age correctly.
        """
        # Create a Player instance with a known birthdate
        birthdate = "1990-01-01"
        # Create an instance of Game
        player = Game()
        # Mock the current year for testing purposes
        current_year = 2023
        # Calculate the expected age
        expected_age = current_year - int(birthdate[:4])
        # Set the current year for the player instance
        player.player_birthdate = birthdate
        # Call the method to calculate the age
        player.calculate_player_age()
        # Assert that the calculated age is equal to the expected age
        self.assertEqual(player.player_age, expected_age)


    def test_check_age_eligibility_valid_age(self):
        """
        Test the check_age_eligibility method with a valid age.

        This test case verifies that the check_age_eligibility method
        correctly returns the player's age when it is a valid age.

        Assertion:
        - Method returns player's age when player's age is set to 18.
        """
        # Set the player's age to 18 for this test case.
        self.game.player_age = 18
        
        # Assert that the check_age_eligibility method
        # returns 18 when the player's age is 18.
        self.assertEqual(self.game.check_age_eligibility(), 18)


    def test_check_age_eligibility_invalid_age(self):
        """
        Test the check_age_eligibility method with an invalid age.

        This test case sets the player's age to 17 and verifies
        that the check_age_eligibility method raises a SystemExit
        exception, indicating that the player is not eligible
        due to their age.
        
        Assertion:
        - Method raises a SystemExit exception.
        """
        # Set the player's age to 17
        self.game.player_age = 17
        # Use a context manager to catch SystemExit exceptions
        with self.assertRaises(SystemExit):
            # Call the 'check_age_eligibility' method
            # - expected to raise a SystemExit exception
            self.game.check_age_eligibility()


    def test_generate_lucky_list(self):
        """
        Test the generate_lucky_list method of the Game class.

        This test case checks if the generate_lucky_list method
        correctly generates a 'lucky_list' attribute with a
        length of 9 in the game object.

        Assertion:
        - The 'lucky_list' attribute has a length of 9.
        """
        # Call the method
        self.game.generate_lucky_list()
        # Assert that the length of the 'lucky_list' 
        # attribute in the game object is 9
        self.assertEqual(len(self.game.lucky_list), 9)


    def test_generate_lucky_number(self):
        """
        Test the generate_lucky_number method of the Game class.

        This test case checks if the generate_lucky_number method sets
        the lucky number within the range [0, 100].

        Assertions:
        - The generated lucky number is within the range [0, 100].
        """
        # Call the method
        self.game.generate_lucky_number()
        # Assert that the generated lucky number is within the range
        self.assertTrue(0 <= self.game.lucky_number <= 100)


    def test_handle_wrong_guess(self):
        """
        Test the handle_wrong_guess method of the Game class.

        This test case checks if the handle_wrong_guess method correctly prints a
        message indicating a wrong guess and prompts the player to try again.

        Assertions:
        - Method prints "Wrong number." to the output.
        - Method prompts the player to try again in the output.
        """
        # Set up the initial conditions for the game
        self.game.lucky_list = [10, 20, 30, 40, 50]
        self.game.lucky_number = 35
        self.game.player_input = 22
        # Redirect the standard output to a StringIO object for testing
        with StringIO() as mock_output:
            with patch("sys.stdout", mock_output):
                # Call the method
                self.game.handle_wrong_guess()
                # Get the output from the method
                output = mock_output.getvalue()
                # Check if the output contains certain expected strings
                self.assertIn("Wrong number.", output)
                self.assertIn("Let's try again", output)


    def test_congratulate_player(self):
        """
        Test the congratulate_player method of the Game class.

        This test case checks if the congratulate_player method correctly prints a
        congratulatory message along with the attempt number to the standard output.

        Assertions:
        - Method prints "Congratulations!" to the output.
        - Method prints the attempt number to the output.
        """
        # Create a StringIO object to capture printed output
        with StringIO() as mock_output:
            # Redirect the standard output to the StringIO object
            with patch("sys.stdout", mock_output):
                # Call the congratulate_player method with the argument 5
                self.game.congratulate_player(5)
                # Get the captured output from the StringIO object
                output = mock_output.getvalue()
                # Check if "Congratulations!" is present in the captured output
                self.assertIn("Congratulations!", output)
                # Check if "try 5" is present in the captured output
                self.assertIn("try 5", output)


    def test_exit_game(self):
        """
        Test the exit_game method of the Game class for correct exit message.

        Assertions:
        - Method raises a SystemExit exception.
        - Printed message matches the expected farewell message.
        """
        # Redirect stdout to capture the printed message
        captured_output = StringIO()
        sys.stdout = captured_output
        with self.assertRaises(SystemExit):
            self.game.exit_game()
        # Reset stdout
        sys.stdout = sys.__stdout__
        # Check if the printed message matches the expected message
        expected_output = "Thank you for playing! Goodbye.\n"
        self.assertEqual(captured_output.getvalue(), expected_output)



if __name__ == '__main__':
    unittest.main()
