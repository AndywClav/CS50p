def main():
    time = input("What time is it? ").strip()
    if time:
        convert(time)
    else:
        print('There is nothing')


def convert(time):
    if '.' in time:
        hours, minutes = time.split(".")
        minutes = int(minutes) * 0.6
    else:
        hours, minutes = time.split(":")

    hours = int(hours)
    minutes = int(minutes)

    decimal_time = hours + minutes / 60

    if 7 <= decimal_time <= 9:
        print('breakfast time')
    elif 12 <= decimal_time <= 13:
        print('lunch time')
    elif 18 <= decimal_time <= 19:
        print('dinner time')
    else:
        print('')


if __name__ == "__main__":
    main()
