import string
import unittest
from unittest.mock import patch
from password_generator_oop import PasswordGenerator, prompt_boolean_input, prompt_integer_input


class PasswordGeneratorTest(unittest.TestCase):

    def test_generate_password_all_true(self):
        # Test case 1: All character types are enabled (upper, lower, digits, special chars)
        generator = PasswordGenerator(length=12, include_uppercase=True, include_lowercase=True,
                                       include_digits=True, include_special_chars=True)
        password = generator.generate_password()
        self.assertEqual(len(password), 12)
        self.assertTrue(any(char.isupper() for char in password))
        self.assertTrue(any(char.islower() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_generate_password_lower(self):
        # Test case 2: Only lowercase letters are enabled
        generator = PasswordGenerator(length=8, include_uppercase=False, include_lowercase=True,
                                       include_digits=False, include_special_chars=False)
        password = generator.generate_password()
        self.assertEqual(len(password), 8)
        self.assertTrue(all(char.islower() for char in password))

    def test_generate_password_digit(self):
         # Test case 3: Only digits are enabled
         generator = PasswordGenerator(length=10, include_uppercase=False, include_lowercase=False,
                                        include_digits=True, include_special_chars=False)
         password = generator.generate_password()
         self.assertEqual(len(password), 10)
         self.assertTrue(all(char.isdigit() for char in password))

    def test_generate_password_special(self):
        # Test case 4: Special characters only
        generator = PasswordGenerator(length=6, include_uppercase=False, include_lowercase=False,
                                       include_digits=False, include_special_chars=True)
        password = generator.generate_password()
        self.assertEqual(len(password), 6)
        self.assertTrue(all(char in string.punctuation for char in password))

    def test_generate_password_all_false(self):
        # Test case 5: No character type is enabled, should raise ValueError
        generator = PasswordGenerator(length=8, include_uppercase=False, include_lowercase=False,
                                      include_digits=False, include_special_chars=False)
        with self.assertRaises(ValueError):
            generator.generate_password()


    # prompt_boolean_input
    @patch('builtins.input', side_effect=['yes'])
    def test_prompt_boolean_input(self, mock_input):
        self.assertTrue(prompt_boolean_input("Include uppercase letters? (yes/no): "))
        mock_input.assert_called_once_with("Include uppercase letters? (yes/no): ")

    @patch('builtins.input', side_effect=['no'])
    def test_prompt_boolean_input_negative(self, mock_input):
        self.assertFalse(prompt_boolean_input("Include lowercase letters? (yes/no): "))
        mock_input.assert_called_once_with("Include lowercase letters? (yes/no): ")

    @patch('builtins.input', side_effect=[''])
    def test_prompt_boolean_input_blank(self, mock_input):
        self.assertTrue(prompt_boolean_input("Include lowercase letters? (yes/no): "))
        mock_input.assert_called_once_with("Include lowercase letters? (yes/no): ")

    @patch('builtins.input', side_effect=['YES'])
    def test_prompt_boolean_input_case_insensitive(self, mock_input):
        self.assertTrue(prompt_boolean_input("Include digits? (yes/no): "))
        mock_input.assert_called_once_with("Include digits? (yes/no): ")

    @patch('builtins.input', side_effect=['nO'])
    def test_prompt_boolean_input_case_insensitive_negative(self, mock_input):
        self.assertFalse(prompt_boolean_input("Include special characters? (yes/no): "))
        mock_input.assert_called_once_with("Include special characters? (yes/no): ")

    @patch('builtins.input', side_effect=['y'])
    def test_prompt_boolean_input_short_input(self, mock_input):
        self.assertTrue(prompt_boolean_input("Include digits? (yes/no): "))
        mock_input.assert_called_once_with("Include digits? (yes/no): ")

    @patch('builtins.input', side_effect=['N'])
    def test_prompt_boolean_input_short_input_negative(self, mock_input):
        self.assertFalse(prompt_boolean_input("Include special characters? (yes/no): "))
        mock_input.assert_called_once_with("Include special characters? (yes/no): ")

    @patch('builtins.input', side_effect=['invalid', 'yes'])
    def test_prompt_boolean_input_retry(self, mock_input):
        self.assertTrue(prompt_boolean_input("Include uppercase letters? (yes/no): "))
        self.assertEqual(mock_input.call_count, 2)
        mock_input.assert_called_with("Include uppercase letters? (yes/no): ")

    # prompt_integer_input
    @patch('builtins.input', side_effect=['12'])
    def test_prompt_integer_input_valid(self, mock_input):
        result = prompt_integer_input("Enter the desired password length [default is '8']: ")
        self.assertEqual(result, 12)
        mock_input.assert_called_once_with("Enter the desired password length [default is '8']: ")

    @patch('builtins.input', side_effect=['0', 'abc', '-5'])
    def test_prompt_integer_input_retry(self, mock_input):
        # Test invalid input, retry with valid input
        result = prompt_integer_input("Enter the desired password length [default is '8']: ")
        self.assertEqual(result, 5)
        self.assertEqual(mock_input.call_count, 3)
        mock_input.assert_called_with("Enter the desired password length [default is '8']: ")


if __name__ == '__main__':
    unittest.main()
