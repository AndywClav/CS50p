import random

integre = None

def ask_level():
    while True:
        try:
            integre = int(input("Level: "))
            if integre > 0:
                break
        except KeyboardInterrupt:
            print("\nProgram exited.")
            break
        except:
            pass


def game():
    ask_level()
    if integre:
        num_random = random.randrange(1, integre)

        while True:
            try:
                game = int(input("Guess: "))
                if game < num_random:
                    print("Too small!")
                elif game > num_random:
                    print("Too large!")
                elif game == num_random:
                    print("Just right!")
                    break
            except KeyboardInterrupt:
                print("\nProgram exited.")
                break
            except:
                pass


def main():
    game()


if __name__ == "__main__":
    main()
