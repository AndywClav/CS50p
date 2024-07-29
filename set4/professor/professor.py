import random


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        try:
            integre = int(input("Level: "))
            if integre > 0 and integre < 4:
                return integre
        except KeyboardInterrupt:
            print("\nProgram exited.")
            return None
        except:
            pass


def sum(x, y):
    return x + y


def generate_integer(level):
    if level:
        score = 0
        while True:
            try:
                match level:
                    case 1:
                        num_x_random = random.randint(0, 9)
                        num_y_random = random.randint(0, 9)
                        ok = True
                        while ok:
                            try:
                                answer = int(input(f'{num_x_random} + {num_y_random} = '))
                                value = sum(num_x_random, num_y_random)
                                if value == answer:
                                    score += 1
                                    ok = False
                            except ValueError:
                                print("EEE")
                    case 2:
                        num_x_random = random.randint(10, 99)
                        num_y_random = random.randint(10, 99)
                    case 3:
                        num_x_random = random.randint(100, 999)
                        num_y_random = random.randint(100, 999)
            except KeyboardInterrupt:
                print(f"\nScore: {score}")
                print("\nProgram exited.")
                break
            except:
                pass


if __name__ == "__main__":
    main()
