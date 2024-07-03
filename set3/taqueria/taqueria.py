foods = {
    "Baja Taco": 4.25,
    "Burrito": 27.00,
    "Bowl": 27.00,
    "Nachos": 27.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 6.00,
    "Tortilla Salad": 14.00
}

def validation(prompt):
    while True:
        try:
            product = input(prompt).title()
            if foods:
                print(f'Total: ${foods[product]:.2f}')
                pass
        except ValueError:
            break
        except EOFError:
            break
        except KeyError:
            break


def main():
    validation('Item: ')


if __name__ == "__main__":
   main()
