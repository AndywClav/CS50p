def main():
    time = input("What time is it? ").strip()
    convert(time)


def convert(time):
    hours, minutes = time.split(":")
    print('breakfast time') if int(hours) >= 8 or int(hours) <= 9 else print('')


if __name__ == "__main__":
    main()
