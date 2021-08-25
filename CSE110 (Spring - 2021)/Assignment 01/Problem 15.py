hour = int(input("Time: "))

if hour >= 4 and hour <= 6:
    print("Breakfast")
elif hour >= 12 and hour <= 13:
    print("Lunch")
elif hour >= 16 and hour <= 17:
    print("Snacks")
elif hour >= 19 and hour <= 20:
    print("Dinner")
elif hour >= 0 and hour <= 23:
    print("Patience is a virtue")
else:
    print("Wrong Time")
