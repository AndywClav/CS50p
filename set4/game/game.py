import random

integre = None

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


