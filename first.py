print("ENTER 2 NUMBER FOR CALCULATION")
X = input("ENTER YOUR FIRST NUMBER: ")
Y = input("ENTER YOUR SECOND NUMBER: ")

print("\nChoose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    print("SUM OF TWO NUMBER IS: ", int(X) + int(Y))
elif choice == '2':
    print("DIFFERENCE OF TWO NUMBER IS: ", int(X) - int(Y))
elif choice == '3':
    print("PRODUCT OF TWO NUMBER IS: ", int(X) * int(Y))
else:
    print("Invalid choice! Please select 1, 2, or 3")
