def food_panda(food, destination="Dhanmondi"):
    price = {"Rice": 105, "Potato": 20, "Chicken": 250, "Beef": 510, "Oil": 85}
    total = 0
    for item in food:
        total += price[item]
    if destination == "Dhanmondi":
        total += 30
    else:
        total += 70
    return total


food = [item for item in input()[1:-1].replace('"', "").replace(" ", "").split(",")]
destination = input()

# Function Call
if len(destination) > 0:
    print(food_panda(food, destination))
else:
    print(food_panda(food))
