#!/usr/bin/env python3
from subprocess	import Popen, PIPE, CalledProcessError, check_output
from string import punctuation
from PasswordGenerator import generate_password


def check_password_requirements(password: str) -> bool:
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in punctuation for char in password):
        return False
    return True


def processing_password() -> str:
    password: str = ''
    print(
        "NB! Specified requirements for password: [Length >= 8, Contains at least: one upper- and one lowercase letter, one digit, one special char]")
    print("\tEnter 1 if You want input password for this user.")
    print("\tEnter 2 if You want to generate password for this user. \n")
    while True:
        try:
            variant: int = int(input('Enter your choice: '))
            if variant == 1:
                password = input("Enter password: ")
                if check_password_requirements(password):
                    return password
                else:
                    print('Password does not meet the specified requirements. Please try again.')
            elif variant == 2:
                length_input = input("Enter the desired length (>= 8) of the password (Press enter for length '8'): ")
                length = 8 if (length_input == '' or int(length_input) < 8) else int(length_input)
                return generate_password(length)
            else:
                print('Invalid input. Please enter either 1 or 2.')

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def change_password(username: str, password: str) -> bool:
    try:
        process = Popen(['passwd', username],
                        stdin=PIPE,
                        stdout=PIPE,
                        stderr=PIPE)
        password_bytes = password.encode('utf-8')
        process.stdin.write(password_bytes + b'\n')
        process.stdin.write(password_bytes)
        process.stdin.flush()
        stdout, stderr = process.communicate()
        print('stderr:\t' + stderr.decode('utf-8'))
    except CalledProcessError as e:
        error_message = e.stderr.strip().decode('utf-8') if e.stderr else str(e)
        print(f"Failed to change password for user '{username}': {error_message}")
        return False


def obtain_existed_username() -> str:
    try:
        # extract users
        output = check_output(['getent', 'passwd']).decode().strip()
        usernames = [entry.split(':')[0] for entry in output.split('\n')]
        while True:
            username = input("Enter the username: ")
            if username in usernames:
                print(f"User '{username}' exists.")  # ?
                break
            else:
                print(f"User '{username}' doesn't exist. Please try again.")
        return username
    except CalledProcessError:
        print('Error with subprocess.')

    except Exception as ex:
        print(f"An error occurred: {ex}")


def main() -> None:
    username = obtain_existed_username()
    password = processing_password()
    print("Username:", username)
    print("Password:", password)
    change_password(username, password)


if __name__ == "__main__":
    main()
