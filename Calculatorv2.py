# Python Calculator v2.0
# This version supports addition, subtraction, multiplication, and division.
operator = input("enter operator (+, -, *, /): ")
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)