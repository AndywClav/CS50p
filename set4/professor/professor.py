import random


def main():
    level = get_level()
    #generate_integer(level)


def get_level():
    while True:
        try:
            integre = int(input("Level: "))
            if integre > 0 or integre < 4:
                return integre
        except KeyboardInterrupt:
            print("\nProgram exited.")
            return None
        except:
            pass


def generate_integer(level):
    if level:
        num_random = random.randint(1, level)

        while True:
            try:
                guess = int(input("Guess: "))
                if guess < num_random:
                    print("Too small!")
                elif guess > num_random:
                    print("Too large!")
                elif guess == num_random:
                    print("Just right!")
                    break
            except KeyboardInterrupt:
                print("\nProgram exited.")
                break
            except:
                pass


if __name__ == "__main__":
    main()
