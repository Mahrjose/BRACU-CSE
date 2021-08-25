working_hours = int(input("Input: "))

if working_hours <= 40:
    salary = working_hours * 200
    print("Output:", salary)
else:
    extra_hours = working_hours - 40
    salary = 8000 + (extra_hours * 300)
    print("Output:", salary)
