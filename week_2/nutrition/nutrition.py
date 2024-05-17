def main():
    fruit = input("Item: ").lower()
    if fruit != "":
        calories = return_calories(fruit)
        if calories != None:
            print("Calories:",calories)

def return_calories(fruit):

    calorie = ""
    cal = [
        {"fruit": "apple",          "calories": 130},
        {"fruit": "avocado",        "calories": 50},
        {"fruit": "banana",         "calories": 110},
        {"fruit": "cantaloupe",     "calories": 50},
        {"fruit": "grapefruit",     "calories": 60},
        {"fruit": "grapes",         "calories": 90},
        {"fruit": "honneydew melon","calories": 50},
        {"fruit": "sweet cherries", "calories": 100},
        {"fruit": "pear",           "calories": 100},
        {"fruit": "kiwifruit",      "calories": 90},
    ]

    for c in cal:
        if c["fruit"] == fruit:
            # print(c["fruit"], c["calories"])
            calorie = c["calories"]
    if calorie == "":
        calorie = None

    return calorie

main()
