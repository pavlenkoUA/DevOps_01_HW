def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return num1 / num2


def handler(variant, num1, num2):
    try:
        if variant == 1:
            result = addition(num1, num2)
            method = "addition"
        elif variant == 2:
            result = subtraction(num1, num2)
            method = "subtraction"
        elif variant == 3:
            result = multiplication(num1, num2)
            method = "multiplication"
        elif variant == 4:
            result = division(num1, num2)
            method = "division"
        print(f"The result of {method} is: {result}")

    except ZeroDivisionError as zde:
        print(str(zde))


def verify_choice_operation(variant):
    if int(variant) in range(1, 5):
        return True
    else:
        return False


def obtain_value(label):
    return input(label)


def initial():
    try:
        num1 = float(obtain_value("Please enter the first number: "))
        num2 = float(obtain_value("Please enter the second number: "))
        print("Please select an operation: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        variant = obtain_value("Please enter the first number: ")
        while not verify_choice_operation(variant):
            print("Incorrect! \n Only 1, 2, 3, 4 available")
            variant = input("Enter your choice (1-4): ")
        handler(int(variant), num1, num2)

    except ValueError as ve:
        print('Incorrect Value! Calculator accept only digital values \n Try again')
        initial()

    except Exception as ex:
        print(str(ex))


print("Welcome to the Calculator Program!")
initial()
