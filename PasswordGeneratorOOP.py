#!/usr/bin/env python3
import random
import string


class PasswordGenerator:
    # initialize passwordGenerator instance, have default parameters
    def __init__(self,
                 length: int = 8,
                 include_uppercase: bool = True,
                 include_lowercase: bool = True,
                 include_digits: bool = True,
                 include_special_chars: bool = True):
        self.length = length
        self.include_uppercase = include_uppercase
        self.include_lowercase = include_lowercase
        self.include_digits = include_digits
        self.include_special_chars = include_special_chars

    # method generate password
    def generate_password(self) -> str:
        # create string with chars.
        chars = ""
        if self.include_uppercase:
            chars += string.ascii_uppercase
        if self.include_lowercase:
            chars += string.ascii_lowercase
        if self.include_digits:
            chars += string.digits
        if self.include_special_chars:
            chars += string.punctuation
        # show error if all parameters disabled
        if not chars:
            raise ValueError("No character set selected. Can't generate password.")
        # from string with chars create list with chars by random lib
        password = random.sample(chars, self.length)
        # from list make string
        return ''.join(password)


#function to process keyboard input commands for string parameters.
def prompt_boolean_input(message: str) -> bool:
    while True:
        user_input = input(message).lower()
        if user_input in ['yes', '', 'y']:
            return True
        elif user_input in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter '[yes', 'y'] or ['no', n]. If you press enter = 'yes'")


#function to process keyboard input commands for integer parameter.
def prompt_integer_input(message: str) -> int:
    while True:
        user_input = input(message)
        try:
            # get integer
            if user_input == '':
                lenght = 8
            else:
                lenght = abs(int(user_input))
                if lenght == 0:
                    print("Password length cannot be 0.")
                    raise ValueError()

            return lenght
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    # collect inputted value from input
    length = prompt_integer_input("Enter the desired password length [press enter for default '8']: ")
    include_uppercase = prompt_boolean_input("Include uppercase letters? (yes/no): ")
    include_lowercase = prompt_boolean_input("Include lowercase letters? (yes/no): ")
    include_digits = prompt_boolean_input("Include digits? (yes/no): ")
    include_special_chars = prompt_boolean_input("Include special characters? (yes/no): ")

    # make instance
    password_generator = PasswordGenerator(
        length=length,
        include_uppercase=include_uppercase,
        include_lowercase=include_lowercase,
        include_digits=include_digits,
        include_special_chars=include_special_chars
    )

    try:
        # generate password with method
        generated_password = password_generator.generate_password()
        print("Generated password: ", generated_password)
    except ValueError as ve:
        print(ve)


if __name__ == '__main__':
    main()
