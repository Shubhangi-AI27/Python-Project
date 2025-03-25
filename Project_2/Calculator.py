def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

# Dictionary for operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)  # Prints the calculator logo
    while True:  # Loop to restart the calculator
        num1 = float(input("What is the first number?: "))

        while True:
            for symbol in operations:
                print(symbol)
            operation_symbol = input("Pick an operation: ")

            if operation_symbol not in operations:
                print("Invalid operation. Please select from the given options.")
                continue

            num2 = float(input("What is the next number?: "))

            answer = operations[operation_symbol](num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")

            choice = input(f"Type 'y' to continue with {answer}, or 'n' to start a new calculation, or 'exit' to quit: ").lower()

            if choice == "y":
                num1 = answer  # Continue calculations with the result
            elif choice == "n":
                break  # Restart with a new number
            elif choice == "exit":
                print("Goodbye! 👋")
                return  # Exit the program
            else:
                print("Invalid choice, exiting...")
                return  # Exit the program

# Run the calculator
calculator()
