#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module provides a PasswordGenerator class and utility functions to generate random passwords
based on user-defined parameters.

Usage:
    1. Instantiate the PasswordGenerator class with desired parameters (length, character types).
    2. Call the generate_password method to obtain random password based on the defined parameters.

Example Output:
    ``` Enter the desired password length [default is '8']: 6
        Include uppercase letters? (yes/no):
        Include lowercase letters? (yes/no):
        Include digits? (yes/no):
        Include special characters? (yes/no):
        Generated password: Le5,?<
    ```

Class:
    PasswordGenerator:
        A class to generate random passwords based on user-defined parameters.

Functions:
    prompt_boolean_input:
        Prompt the user for a boolean input (yes/no) and return a bool value.

    prompt_integer_input:
        Prompt the user for an integer input and return the integer value.

"""

import random
import string


class PasswordGenerator:
    """
    A class to generate random passwords based on user-defined parameters.

    Attributes:
        length (int): The length of the generated password.
        include_uppercase (bool): Whether to include uppercase letters in the password.
        include_lowercase (bool): Whether to include lowercase letters in the password.
        include_digits (bool): Whether to include digits in the password.
        include_special_chars (bool): Whether to include special characters in the password.
    """

    def __init__(self,
                 length: int = 8,
                 include_uppercase: bool = True,
                 include_lowercase: bool = True,
                 include_digits: bool = True,
                 include_special_chars: bool = True):
        """
        Initialize the PasswordGenerator instance with default parameters.

        Parameters::
            length (int): The length of the generated password. Default is 8.
            include_uppercase (bool): Whether to include uppercase letters. Default is True.
            include_lowercase (bool): Whether to include lowercase letters. Default is True.
            include_digits (bool): Whether to include digits. Default is True.
            include_special_chars (bool): Whether to include special characters. Default is True.
        """
        self.length = length
        self.include_uppercase = include_uppercase
        self.include_lowercase = include_lowercase
        self.include_digits = include_digits
        self.include_special_chars = include_special_chars

    def generate_password(self) -> str:
        """
        Generate a random password based on the defined parameters.

        Returns:
            str: The generated random password.

        Raises:
            ValueError: If no character set is selected (all parameters are disabled).
        """
        chars = ""
        password_list = []
        if self.include_digits:
            chars += string.digits
            password_list.append(random.choices(string.digits, k=1)[0])
        if self.include_uppercase:
            chars += string.ascii_uppercase
            password_list.append(random.choices(string.ascii_uppercase, k=1)[0])
        if self.include_lowercase:
            chars += string.ascii_lowercase
            password_list.append(random.choices(string.ascii_lowercase, k=1)[0])
        if self.include_special_chars:
            chars += string.punctuation
            password_list.append(random.choices(string.punctuation, k=1)[0])
        if not chars:
            raise ValueError("No character set selected. Can't generate password.")

        if len(password_list) > self.length:
            random.shuffle(password_list)
            return ''.join(random.sample(password_list, k=self.length))

        while len(password_list) < self.length:
            password_list.append(random.choices(chars, k=1)[0])
        random.shuffle(password_list)
        result = ''.join(password_list)
        return result


def prompt_boolean_input(message: str) -> bool:
    """
    Prompt user for a boolean input.

    Args:
        message (str): The prompt message.

    Returns:
        bool: True if the user inputs 'yes' or 'y', False if 'no' or 'n'.
        Default is True if the user presses enter.
    """
    while True:
        user_input = input(message).lower()
        if user_input in ['yes', '', 'y']:
            return True
        if user_input in ['no', 'n']:
            return False
        print("Invalid input. Please enter '[yes', 'y'] or ['no', n]. "
                  "If you press enter = 'yes'")


def prompt_integer_input(message: str) -> int:
    """
    Prompt user for an integer input.

    Args:
        message (str): The prompt message.

    Returns:
        int: The user-inputted integer. Default is 8 if the user presses enter.

    Raises:
        ValueError: If the user input is not a valid integer.
    """
    while True:
        user_input = input(message)
        try:
            if user_input == '':
                length = 8
            else:
                length = abs(int(user_input))
                if length == 0:
                    print("Password length cannot be 0.")
                    raise ValueError()

            return length
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    """
    Main function to collect user input and generate a random password.
    """
    length = prompt_integer_input("Enter the desired password length [default is '8']: ")
    include_uppercase = prompt_boolean_input("Include uppercase letters? (yes/no): ")
    include_lowercase = prompt_boolean_input("Include lowercase letters? (yes/no): ")
    include_digits = prompt_boolean_input("Include digits? (yes/no): ")
    include_special_chars = prompt_boolean_input("Include special characters? (yes/no): ")

    password_generator = PasswordGenerator(
        length=length,
        include_uppercase=include_uppercase,
        include_lowercase=include_lowercase,
        include_digits=include_digits,
        include_special_chars=include_special_chars
    )

    try:
        generated_password = password_generator.generate_password()
        print("Generated password:", generated_password)
    except ValueError as ve:
        print(ve)


if __name__ == '__main__':
    main()
