# Calculator App

# Python Calculator App
# Beginner Python Project

history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

def remainder(a, b):
    if b == 0:
        return "Cannot calculate remainder with zero!"
    return a % b

def power(a, b):
    return a ** b


def calculator():
    print("\n" + "=" * 50)
    print("       🧮 PYTHON CALCULATOR")
    print("=" * 50)
    print("       Welcome to Calculator!")

    while True:
        print("\n--------- MAIN MENU ---------")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Remainder (%)")
        print("6. Power (**)")
        print("7. History")
        print("8. Exit")
        print("-" * 30)

        choice = input("Enter your choice (1-8): ")

        if choice == "8":
            print("\nThank you for using Calculator! 😊")
            break

        if choice == "7":
            print("\n📋 CALCULATION HISTORY")
            if history:
                for item in history:
                    print(item)
            else:
                print("No calculations yet.")
            continue

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("❌ Invalid choice! Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        except ValueError:
            print("❌ Please enter valid numbers!")
            continue

        if choice == "1":
            result = add(num1, num2)
            symbol = "+"

        elif choice == "2":
            result = subtract(num1, num2)
            symbol = "-"

        elif choice == "3":
            result = multiply(num1, num2)
            symbol = "*"

        elif choice == "4":
            result = divide(num1, num2)
            symbol = "/"

        elif choice == "5":
            result = remainder(num1, num2)
            symbol = "%"

        elif choice == "6":
            result = power(num1, num2)
            symbol = "**"
    

        print("\n" + "=" * 30)
        print("          RESULT")
        print("=" * 30)
        print(f"{num1} {symbol} {num2} = {result}")
        print("=" * 30)

        if isinstance(result, (int, float)):
            history.append(f"{num1} {symbol} {num2} = {result}")


if __name__ == "__main__":
    calculator()