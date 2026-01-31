employees_happiness = list(map(int, input().split()))
happiness_improvement_factor = int(input())
count = 0

updated_employees_happiness = [num * happiness_improvement_factor for num in employees_happiness]

average_happiness = sum(updated_employees_happiness) / len(updated_employees_happiness)

for employee in updated_employees_happiness:
    if employee > average_happiness:
        count += 1

if count >= len(updated_employees_happiness) / 2:
    print(f"Score: {count}/{len(updated_employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {count}/{len(updated_employees_happiness)}. Employees are not happy!")