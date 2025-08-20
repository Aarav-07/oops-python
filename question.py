employee = {"E2806":5000, "E2704":30000, "E2807":10000, "E2705":20000}

for emp_id, salary in employee.items():
    print(f"Employee {emp_id}: {salary}")

max_salary = max(employee.values())
min_salary = min(employee.values())

for emp_id, salary in employee.items():
    if salary == max_salary:
        employee[emp_id] = salary * 1.02
        print(f"\nEmployee {emp_id} salary increased from {salary} to {employee[emp_id]}")
    elif salary == min_salary:
        employee[emp_id] = salary * 1.10
        print(f"Employee {emp_id} salary increased from {salary} to {employee[emp_id]}")

print("\nFinal updated salaries:")
for emp_id, salary in employee.items():
    print(f"Employee {emp_id}: {salary}")