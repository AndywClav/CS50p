foods = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def validation(prompt):
    while True:
        try:
            product = input(prompt).title()
            if key in product:
                print(f'Total: ${product[key]:.2f}')
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
