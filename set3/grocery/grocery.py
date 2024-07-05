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

items()
