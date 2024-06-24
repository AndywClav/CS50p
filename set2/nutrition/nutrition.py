food = [{'Apple': 130},
        {'Avocado': 50},
        {'Sweet Cherries': 100},
        {'Kiwifruit': 90},
        {'Pear': 100}]


def food_validation(ask):
    for item in food:
        for key, value in item.items():
            if ask == key:
                return value
    return None


def main():
    ask = input("Item: ").title().strip()
    calories = food_validation(ask)
    if calories is not None:
        print(f"Calories: { calories }")
    else:
        print('')

main()
