import random

def main():
    level = get_level()
    if level is not None:
        score = generate_integer(level)
        print(f"Score: {score}")


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
    attempts = 0
    while attempts < 3:
        try:
            answer = int(input(f'{x} + {y} = '))
            value = sum_numbers(x, y)
            if value == answer:
                score += 1
                return score
            else:
                attempts += 1
                print("EEE")
        except ValueError:
            print("EEE")
    print(f"The correct answer is {sum_numbers(x, y)}")
    return score


def generate_integer(level):
    score = 0
    for _ in range(10):
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
            print("\nProgram exited.")
            break
    return score


if __name__ == "__main__":
    main()
