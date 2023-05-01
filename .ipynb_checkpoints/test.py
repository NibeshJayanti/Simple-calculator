# Define a function for addition
def add(x, y):
    return x + y

# Define a function for subtraction
def subtract(x, y):
    return x - y

# Define a function for multiplication
def multiply(x, y):
    return x * y

# Define a function for division
def divide(x, y):
    return x / y

# Print a menu of operations for the user to choose from
print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Prompt the user to choose an operation
choice = input("Enter choice (1/2/3/4): ")

# Prompt the user to enter two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the chosen operation and print the result
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")
