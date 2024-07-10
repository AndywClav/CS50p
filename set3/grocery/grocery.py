def items():
    items = {}
    try:
        while True:
            item = input().strip().lower()
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
    except EOFError:
        pass
    except KeyboardInterrupt:
        print("")
        pass
    finally:
        for item in sorted(items):
            print(f"{items[item]} {item.upper()}")

items()
