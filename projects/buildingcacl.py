num1 = int(input('Enter first number\n'))
op = input('Enter Operator\n')
num2 = int(input('Enter Second number\n'))

if op == "+":
    print(f'The addition is {num1 + num2}')
elif op == "-":
    print(f'The subtraction is {num1 - num2}')
elif op == "*":
    print(f'The multiplication is {num1 * num2}')
elif op == "/":
    print(f'The division is {num1 / num2}')
else:
    print('Invalid operator')