import random
import string


def generate_password(length: int = 8) -> str:
    password = random.choices(string.ascii_uppercase, k=1) \
               + random.choices(string.ascii_lowercase, k=1) \
               + random.choices(string.digits, k=1) \
               + random.choices(string.punctuation, k=1) \
               + random.choices(string.ascii_uppercase
                                + string.ascii_lowercase
                                + string.digits
                                + string.punctuation,
                                k=(length - 4)
                                )
    random.shuffle(password)
    return ''.join(password)


def main():
    print("Welcome to the Linux User Password Generator!")
    try:
        length = input("Please enter the desired password length (Minimum is 8 | default is 8): ")
        if length.strip() == "":
            print("Generated password:", generate_password())
        else:
            length = max(int(length), 8)
        print("Generated password:", generate_password(length))
    except ValueError:
        print("Invalid input. Please enter a valid integer")


if __name__ == "__main__":
    main()
