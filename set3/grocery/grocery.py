def items():
    items = {}
    try:
        while True:
            item = input().strip().lower()
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
            print(f"{items[item]} {item}")
    except:
        pass
    finally:
        print(items)

items()
