n = int(input("Enter the number of subjects: "))

total = 0
for i in range(1, n+1):
    marks = float(input(f"Enter marks for subject {i}: "))
    total += marks

average = total / n
print("\nTotal Marks =", total)
print("Average Marks =", average)

if average >= 80:
    print("Grade: A+ (Excellent!)")
elif average >= 60 and average < 80:
    print("Grade: A (Very Good)")
elif average >= 40 and average < 60:
    print("Grade: B (Good)")
elif average >= 30 and average < 40:
    print("Grade: C (Pass)")
else:
    print("Grade: BETTER LUCK NEXT TIME ")
