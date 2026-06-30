num1 = int(input("enter the number :"))
num2 = int(input("enter the number :"))
op = input("enter yout operator :")



if op == '+':
    print("result",num1 + num2)
elif op == '-':
    print("result",num1 - num2)
elif op == '*':
    print("result",num1 * num2)
elif op == '/':
    print("result",num1 / num2)
else:
    print("invalid operation")