class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

n = int(input("Enter number of employees: "))
employees = []

for i in range(n):
    emp_id = input("Enter ID: ")
    name = input("Enter Name: ")
    salary = float(input("Enter Salary: "))
    employees.append(Employee(emp_id, name, salary))

employees.sort(key=lambda e: e.salary)

print("\nEmployees sorted by salary:")
for e in employees:
    print(e.emp_id, e.name, e.salary)
