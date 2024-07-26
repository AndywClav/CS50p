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
    num_random = random.randrange(0, integre)
    print(num_random + 1, integre)
    while True:
        try:
            game = int(input("Guess: "))
            if game < 5:
                print("Too small!")
            elif game > 5:
                print("Too large!")
            elif game == 5: # Put the variable where goint tu random number
                print("Just right!")
                break
        except KeyboardInterrupt:
            print("\nProgram exited.")
            break
        except:
            pass


