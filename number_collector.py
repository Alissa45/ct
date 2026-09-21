# num1
try:
    num1 = int(input("Enter a number: "))
except ValueError:
    num1 = 0
    print("That's not a valid number. Using 0 instead.")

# num2
try:
    num2 = int(input("Enter a number: "))
except ValueError:
    num2 = 0
    print("That's not a valid number. Using 0 instead.")

# num3
try:
    num3 = int(input("Enter a number: "))
except ValueError:
    num3 = 0
    print("That's not a valid number. Using 0 instead.")

print(f"Your Numbers: {num1},{num2},{num3}")
