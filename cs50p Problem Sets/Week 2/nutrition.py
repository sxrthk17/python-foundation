item = input("Item: ")
fruit_calories = {
    "apple": 95,           # 1 medium fruit
    "banana": 110,         # 1 medium fruit
    "blueberry": 84,       # 1 cup
    "cherry": 97,          # 1 cup (pitted)
    "date": 20,            # 1 single date
    "fig": 37,             # 1 medium fresh fig
    "grape": 62,           # 1 cup
    "honeydew": 61,        # 1 cup diced
    "kiwi": 61,            # 1 medium fruit
    "lemon": 17,           # 1 medium fruit
    "lime": 20,            # 1 medium fruit
    "mango": 70,           # 3/4 cup sliced (approx. 202 per whole mango)
    "nectarine": 63,       # 1 medium fruit
    "orange": 62,          # 1 medium fruit
    "pear": 101,           # 1 medium fruit
    "raspberry": 65,       # 1 cup
    "strawberry": 49,      # 1 cup
    "tangerine": 47,       # 1 medium fruit
    "watermelon": 46,       # 1 cup diced
    "avocado": 50,
    "sweet cherries": 100
}
if item.strip().lower() in fruit_calories.keys():
    print(f"Calories: {fruit_calories[item.lower()]}")
