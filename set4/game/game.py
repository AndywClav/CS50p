import random

def ask_level():
    while True:
        try:
            integre = int(input("Level: "))
            if integre > 0:
                return integre
        except KeyboardInterrupt:
            print("\nProgram exited.")
            return None
        except:
            pass


def game(integre):
    if integre:
        num_random = random.randint(1, integre)

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


def main():
    integre = ask_level()
    game(integre)


if __name__ == "__main__":
    main()
