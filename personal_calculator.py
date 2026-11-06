# 1. Ask the user for their name 
name = input("Enter your name:")

# 2. Ask for their age
age = int(input("Enter your age"))

print()

# 3. Ask for two numbers
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

 # 4. Calculate sum, subtraction, multiplication, and division
addition = num1 + num2
subtraction = num1- num2
multiplication = num1 * num2

if num2 != 0:
 division = num1 / num2
else:
  division = "Undefind (division by zero)"

print()
# 5. Display all information in a well-formatted output using f-strings
print(f"Hello, {name}!")
print(f"Your age is {age}.")
print()
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")


