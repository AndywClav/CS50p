def main():
    time = input("What time is it? ").strip()
    convert(time)


def convert(time):
    hours, minutes = time.split(":")


if __name__ == "__main__":
    main()
