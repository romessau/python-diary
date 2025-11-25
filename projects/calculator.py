import art_mod as art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


operands = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(art.logo)
    num1 = None

    while True:  # loop until i say stop
        try:
            if num1 is None:  # need to know if empty or prev result needed by user
                num1 = float(input("Enter the first number: "))

            for symbol in operands:
                print(symbol)

            user_select_operand = input("Enter the operand: ").strip()
            if user_select_operand not in operands:
                print(f"Invalid operand: {user_select_operand}")
                continue  # used if error but want to let user type again
            # go back to top dont do calculation enter smthn againa

            num2 = float(input("Enter the second number: "))
            result = operands[user_select_operand](num1, num2)
            print(f"{num1} {user_select_operand} {num2} = {result}")

            choice = input(
                f"Type 'y' to continue with {result}, or 'n' to exit: ").strip().lower()
            if choice == "y":
                num1 = result
            else:
                print("\n" * 20)
                break
# dont want the program to stop and continue it running basically it enters again
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")


calculator()
# num1 = result if user wants to continue
