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


def get_spiciest_foods(spicy_foods):
    get_spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return get_spiciest_foods
def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        print(f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {'🌶' * spicy_food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return [spicy_food for spicy_food in spicy_foods if spicy_food["cuisine"] == cuisine][0]

def print_spiciest_foods(spicy_foods):
    for spicy_food in spicy_foods:
        if spicy_food["heat_level"] > 5:
            print(f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {'🌶' * spicy_food['heat_level']}")

 
def get_average_heat_level(spicy_foods):
     average_heat_level= list() 
     my_food = len(spicy_foods)
     for spicy_food in spicy_foods:
        average_heat_level.append(spicy_food["heat_level"])
        
     return sum(average_heat_level) / my_food

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
