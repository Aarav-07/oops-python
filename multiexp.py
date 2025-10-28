try:
    num = int(input("Enter a number: "))
    result = num / 0 
    print("Result is:", result)
except (ZeroDivisionError, ValueError) as error:
    print(f"Error occurred: {error}")
