add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print(add(a, b))
elif op == "-":
    print(sub(a, b))
elif op == "*":
    print(mul(a, b))
elif op == "/":
    print(div(a, b))
else:
    print("Invalid operator")
