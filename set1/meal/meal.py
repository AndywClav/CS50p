def main():
    time = input("What time is it? ").strip()
    convert(time)


def convert(time):
    hours, minutes = time.split(":")

    if int(hours) >= 8 and int(hours) <= 9:
        if int(minutes) < 1:
            print('breakfast time')
    else:
        print('')


if __name__ == "__main__":
    main()
