try:
    num = int(input("Enter a number: "))
    result = num / 0 
    print("Result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
