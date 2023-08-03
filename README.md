# DevOps_01_HW
**PYTHON**
- HW_1  - [X]
- HW_1* - [X]
- HW_2  - [X]
- HW_3  - [X]
- HW_GR - [ ]
- HW_4  - [x]

# Password Generator

This repository contains a Python script to generate random passwords based on user-defined parameters. The script provides a PasswordGenerator class and utility functions for user input.

## Usage
1. Install Python3.8 and higher, python3-venv package:
```bash
sudo apt update
sudo apt install python3 python3-venv
```
2. Clone this repository and navigate to its directory.
3. Create a virtual environment and install the required packages using the provided `install.sh` script.

```bash
./install.sh
```
___
* Once the virtual environment is activated, you can run the password generator using the following command:
```bash
python password_generator_oop.py
```

* The script will prompt you to enter the desired password length and select the character types (uppercase, lowercase, digits, special characters) to include in the password.
After providing the input, the script will generate a random password based on your selections.
___
* The repository includes unit tests for the password generator script. You can run the tests using the following command:
```bash
python -m unittest password_generator_oop_test.py
```
___
* To check the code with pylint, ensure you have activated the virtual environment, and then run the following command:
```bash
python3 -m pylint password_generator_oop_test.py
```
___
# Example:
```
Enter the desired password length [default is '8']: 12
Include uppercase letters? (yes/no): yes
Include lowercase letters? (yes/no): yes
Include digits? (yes/no): yes
Include special characters? (yes/no): yes
Generated password: c5T@8k!2e&Q1
```
___
___