def calculate_tax(age, salary, job):
    if age < 18 or job == "president" or salary < 10000:
        return 0
    elif salary > 10000 and salary < 20000:
        return (5 / 100) * salary
    else:
        return (10 / 100) * salary


age = int(input())
salary = int(input())
job = input().lower()

# Function Call
print(calculate_tax(age, salary, job))
