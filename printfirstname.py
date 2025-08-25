full_name = input("Enter your full name: ")

first_name = ""
for letter in full_name:
    if letter == " ":
        break
    first_name += letter

print("First name is:", first_name)
