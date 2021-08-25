def day_calc(day):
    year = day // 365
    day %= 365
    month = day // 30
    day %= 30
    print(f"{year} years, {month} months and {day} days")


day = int(input())

# Function Call
day_calc(day)
