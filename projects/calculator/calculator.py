import art_mod as art


# ---- Operation Functions ---- #
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


# Mapping operators to their functions
operands = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


# ---- Main Calculator Logic ---- #
def calculator():
    print(art.logo)
    num1 = None  # holds result if user continues

    while True:
        try:
            if num1 is None:
                num1 = float(input("Enter the first number: "))

            print("\nAvailable operations:")
            print(" ".join(operands.keys()))  # + - * /

            operation = input("Enter the operand: ").strip()

            if operation not in operands:
                print(f"Invalid operand: {operation}")
                continue

            num2 = float(input("Enter the second number: "))

            result = operands[operation](num1, num2)
            print(f"\n{num1} {operation} {num2} = {result}")

            choice = input(
                f"Type 'y' to continue with {result}, or 'n' to exit: "
            ).strip().lower()

            if choice == "y":
                num1 = result  # continue with latest result
            else:
                print("\n" * 20)
                break

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")


# ---- Run Program ---- #
if __name__ == "__main__":
    calculator()
