def main():
    time = input("What time is it? ").strip()
    if time == time.leght:
        print('There is nothing')
    else:
        convert(time)


def convert(time):
    hours, minutes = time.split(":")

    if int(hours) >= 7 and int(hours) <= 9:
        print('breakfast time')
    elif int(hours) >= 12 and int(hours) <= 13:
        print('lunch time')
    elif int(hours) >= 18 and int(hours) <= 19:
        print('dinner time')
    else:
        print('')


if __name__ == "__main__":
    main()
