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


# Nested dictionary example
print("\nNested Dictionary Example:")
students = {
    "student1": {
        "name": "John",
        "age": 20,
        "scores": {
            "math": 90,
            "science": 85,
            "english": 88
        }
    },
    "student2": {
        "name": "Emma",
        "age": 19,
        "scores": {
            "math": 95,
            "science": 92,
            "english": 90
        }
    }
}

# Accessing nested dictionary values
print("\nAccessing nested values:")
print(f"Student1 name: {students['student1']['name']}")
print(f"Student2 math score: {students['student2']['scores']['math']}")

# Modifying nested values
students['student1']['scores']['math'] = 92

# Looping through nested dictionary
print("\nAll students scores:")
for student_id, student_info in students.items():
    print(f"\n{student_info['name']}'s scores:")
    for subject, score in student_info['scores'].items():
        print(f"{subject}: {score}")

# Converting dictionary values to lists
print("\nDictionary to List Conversions:")

# Convert values to list
values_list = list(students.values())
print("\nAll values as list:", values_list)

# Get list of all student names
names_list = [student['name'] for student in students.values()]
print("\nList of names:", names_list)

# Get list of all science scores
science_scores = [student['scores']['science'] for student in students.values()]
print("\nList of science scores:", science_scores)

# Get list of all scores for each student
all_scores = [student['scores'] for student in students.values()]
print("\nList of all score dictionaries:", all_scores)

# Get list of keys and values separately
keys_list = list(students.keys())
values_list = list(students.values())
print("\nKeys list:", keys_list)
print("Values list:", values_list)

# Convert nested scores to list of tuples
score_tuples = [(student['name'], list(student['scores'].values())) 
                for student in students.values()]
print("\nScores as list of tuples:", score_tuples)