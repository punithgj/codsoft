def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
def calculator():
    while True:
        print("\nWelcome to the Basic Calculator!")
        print("Please choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input! Please enter numerical values.")
                continue

            if choice == '1':
                result = add(num1, num2)
                operation = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                operation = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                operation = '*'
            elif choice == '4':
                result = divide(num1, num2)
                operation = '/'

            print(f"The result of {num1} {operation} {num2} is: {result}")
        else:
            print("Invalid choice! Please select a valid operation.")

        again = input("Would you like to perform another operation? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()
