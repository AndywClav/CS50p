
def items():
    items = {}
    try:
        while True:
            item = input("").strip().lower()
            items[item] = 0
            if item in items:
                items[item] += 1
                print(f"{items[item]} {items.keys()}")
    except:
        return print(items)

items()

def items():
    items = {}
    try:
        while True:
            item = input().strip().lower()
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
    except:
        pass
    finally:
        print(f"{items[item]} {item}")
        print(items)

items()

