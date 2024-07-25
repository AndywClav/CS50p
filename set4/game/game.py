
while True:
    try:
        integre = int(input("Level: "))
        if integre > 0:
            break
    except KeyboardInterrupt:
        break
    except:
        pass

if integre:
    while True:
        try:
            game = int(input("Guess: "))
            if game == 5:
                print("Just right! ")
                break
        except KeyboardInterrupt:
            break
        except:
            pass
