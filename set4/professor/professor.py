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


def validation(x, y):
    ok = True
    while ok:
        try:
            answer = int(input(f'{x} + {y} = '))
            value = sum(x, y)
            if value == answer:
                score += 1
                ok = False
            else:
                raise ValueError
        except ValueError:
            print("EEE")
        except KeyboardInterrupt:
            return score


def generate_integer(level):
    if level:
        score = 0
        while True:
            try:
                match level:
                    case 1:
                        num_x_random = random.randint(0, 9)
                        num_y_random = random.randint(0, 9)
                        result = validation(num_x_random, num_y_random)
                    case 2:
                        num_x_random = random.randint(10, 99)
                        num_y_random = random.randint(10, 99)
                        result = validation(num_x_random, num_y_random)
                    case 3:
                        num_x_random = random.randint(100, 999)
                        num_y_random = random.randint(100, 999)
                        result = validation(num_x_random, num_y_random)
            except KeyboardInterrupt:
                score = result
                print(f"\nScore: {score}")
                print("Program exited.")
                break
            except:
                pass


if __name__ == "__main__":
    main()


import random

def main():
    level = get_level()
    if level is not None:
        score = generate_integer(level)
        print(f"Final Score: {score}")

def get_level():
    while True:
        try:
            integre = int(input("Level (1-3): "))
            if 1 <= integre <= 3:
                return integre
        except KeyboardInterrupt:
            print("\nProgram exited.")
            return None
        except ValueError:
            pass

def sum_numbers(x, y):
    return x + y

def validation(x, y, score):
    ok = True
    while ok:
        try:
            answer = int(input(f'{x} + {y} = '))
            value = sum_numbers(x, y)
            if value == answer:
                score += 1
                ok = False
            else:
                raise ValueError
        except ValueError:
            print("EEE")
        except KeyboardInterrupt:
            return score
    return score

def generate_integer(level):
    score = 0
    while True:
        try:
            if level == 1:
                num_x_random = random.randint(0, 9)
                num_y_random = random.randint(0, 9)
            elif level == 2:
                num_x_random = random.randint(10, 99)
                num_y_random = random.randint(10, 99)
            elif level == 3:
                num_x_random = random.randint(100, 999)
                num_y_random = random.randint(100, 999)

            score = validation(num_x_random, num_y_random, score)
        except KeyboardInterrupt:
            print(f"\nScore: {score}")
            print("Program exited.")
            break
        except:
            pass
    return score

if __name__ == "__main__":
    main()
