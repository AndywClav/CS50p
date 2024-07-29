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


def generate_integer(level):
    if level:
        num_x_random = random.randint(1, 10)
        num_y_random = random.randint(1, 10)
        while True:
            try:
                match level:
                    case 1:
                        answer = input(f'{num_x_random} + {num_y_random}: ')
                        value = num_x_random + num_y_random
                        if value == answer:
                            break
            except KeyboardInterrupt:
                print("\nProgram exited.")
                break
            except:
                pass


if __name__ == "__main__":
    main()
