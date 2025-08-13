# Creating a dictionary
student = {
    "name": "John",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Physics", "English"]
}

# Accessing values
print("Student name:", student["name"])
print("Student age:", student.get("age"))  # safer way using get()

# Modifying values
student["age"] = 21
student["grade"] = "B+"

# Adding new key-value pairs
student["city"] = "New York"

# Removing items
del student["grade"]  # remove specific key
removed_item = student.pop("subjects")  # remove and return value

# Dictionary methods
print("\nDictionary methods:")
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Checking if key exists
if "name" in student:
    print("\nName exists in dictionary")

# Looping through dictionary
print("\nLooping through dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares = {x: x*x for x in range(5)}
print("\nSquares dictionary:", squares)