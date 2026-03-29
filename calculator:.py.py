def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def show_menu():
    print("\n=== Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. View History")
    print("6. Exit")

def main():
    history = []

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "6":
            print("Goodbye 👋")
            break

        if choice == "5":
            print("\n--- History ---")
            if not history:
                print("No calculations yet.")
            else:
                for item in history:
                    print(item)
            continue

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice, try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == "1":
            result = add(num1, num2)
            operation = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            operation = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            operation = "*"
        elif choice == "4":
            result = divide(num1, num2)
            operation = "/"

        output = f"{num1} {operation} {num2} = {result}"
        print("Result:", result)

        history.append(output)

if __name__ == "__main__":
    main()