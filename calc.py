import random

try:
    num1 = float(input("Enter a number : "))
    num2 = float(input("Enter another number : "))
    op = input("Enter an operator : ")
except ValueError:
    print("Invalid number")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print('Invalid operator')


def dice_roll(num):
    return random.randint(1, num)

