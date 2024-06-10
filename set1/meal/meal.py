def main():
    time = input("What time is it? ").strip()
    if time:
        convert(time)
    else:
        print('There is nothing')


def convert(time):
    hours, minutes = time.split(":")

    if float(hours) >= 7 and float(hours) <= 9:
        print('breakfast time')
    elif int(hours) >= 12 and int(hours) <= 13:
        print('lunch time')
    elif int(hours) >= 18 and int(hours) <= 19:
        print('dinner time')
    else:
        print('')


if __name__ == "__main__":
    main()
