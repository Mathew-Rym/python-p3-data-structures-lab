spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]
print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    spice = [food for food in spicy_foods if (food["heat_level"] > 5)]
    return spice
print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        spice_level = "🌶" * food["heat_level"]
        food = food["name"] + " (" + food["cuisine"] + ") | Heat Level: " + spice_level
        print(food)
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower():
            return food
    return None
print(get_spicy_food_by_cuisine(spicy_foods, "American"))

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] >5:
            spice_level = "🌶" * food["heat_level"]
            food = food["name"] + " (" + food["cuisine"] + ") | Heat Level: " +spice_level
            print(food)

print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    average = total_heat / len(spicy_foods)
    return int(average)
print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
print(create_spicy_food(
    spicy_foods,
    {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
))