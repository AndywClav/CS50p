
def items():
    items = {}
    try:
        while True:
            item = input("").strip().lower()
            contador = 0
            items[item] = contador
            if item in items:
                items[item] = contador + 1
    except KeyboardInterrupt:
        return print(f"{items[item]} {items.keys()}")


items()
