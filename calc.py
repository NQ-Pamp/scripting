num1 = float(input("Enter a number : "))
num2 = float(input("Enter another number : "))
op = input("Enter an operator : ")

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
