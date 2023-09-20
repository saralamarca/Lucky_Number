import unittest
from unittest.mock import patch, Mock
import io
from io import StringIO
import sys
from game import Game
from itertools import cycle


class TestGame(unittest.TestCase):
    """
    A class for testing the Game class.
    """
    def setUp(self):
        """
        This method sets up a new Game instance for each test.
        """
        self.game = Game()
        self.initial_tries_count = None


    # Mock user input as "Gullbritt"
    @patch("builtins.input", side_effect=["Gullbritt"])
    def test_get_player_name_valid_input(self, mock_input):
        """
        Test the get_player_name method with valid input.
        """
        # Assert that get_player_name returns "Gullbritt"
        self.assertEqual(self.game.get_player_name(), "Gullbritt")


    # Mock user input as "123Gullbritt" and then "Gullbritt"
    @patch("builtins.input", side_effect=["123Gullbritt", "Gullbritt"])
    def test_get_player_name_invalid_input_then_valid_input(self, mock_input):
        """
        Test the get_player_name method with invalid input
        followed by valid input.
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
        """
        # Ensure the returned value matches the input
        self.assertEqual(self.game.get_player_birthdate(), "19901231")


    # Mock user input as "19901331" and then "19901231"
    @patch("builtins.input", side_effect=["19901331", "19901231"])
    def test_get_player_birthdate_invalid_then_valid_(self, mock_input):
        """
        Test the get_player_birthdate method with an invalid date
        followed by a valid date.
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
        player = Game()
        player.player_age = 18
        self.assertEqual(player.check_age_eligibility(), 18)


    def test_check_age_eligibility_invalid_age(self):
        player = Game()
        player.player_age = 17
        with self.assertRaises(SystemExit):
            player.check_age_eligibility()


    def test_generate_lucky_list(self):
        player = Game()
        player.generate_lucky_list()
        self.assertEqual(len(player.lucky_list), 9)


    def test_generate_lucky_number(self):
        player = Game()
        player.generate_lucky_number()
        self.assertTrue(0 <= player.lucky_number <= 100)


    def test_handle_wrong_guess(self):
        player = Game()
        player.lucky_list = [10, 20, 30, 40, 50]
        player.lucky_number = 35
        player.player_input = 22
        with StringIO() as mock_output:
            with patch("sys.stdout", mock_output):
                player.handle_wrong_guess()
                output = mock_output.getvalue()
                self.assertIn("Wrong number.", output)
                self.assertIn("Let's try again", output)


    def test_congratulate_player(self):
        player = Game()
        with StringIO() as mock_output:
            with patch("sys.stdout", mock_output):
                player.congratulate_player(5)
                output = mock_output.getvalue()
                self.assertIn("Congratulations!", output)
                self.assertIn("try 5", output)






if __name__ == '__main__':
    unittest.main()
