import re
import sys


def main():
    output_time = input_time()
    print(convert(output_time))


def convert(s):
    """
     Convert a time range from 12-hour AM/PM format to 24-hour format.
    """
    time = s.upper()

    if not time.endswith("AM") and not time.endswith("PM"):
        raise ValueError

    format_time = r"^(1[0-2]|0?[1-9])(:[0-5][0-9])? (AM|PM) TO (1[0-2]|0?[1-9])(:[0-5][0-9])? (AM|PM)$"
    if not re.search(format_time, time):
        raise ValueError

    part1_time, part2_time = time.replace(" ", "").split("TO")

    am_pm1 = "AM" if "AM" in part1_time else "PM"
    am_pm2 = "AM" if "AM" in part2_time else "PM"

    part1_time = part1_time.replace("AM", "").replace("PM", "")
    part2_time = part2_time.replace("AM", "").replace("PM", "")

    hour1, minute1 = part1_time.split(':') if ':' in part1_time else (part1_time, '00')
    hour2, minute2 = part2_time.split(':') if ':' in part2_time else (part2_time, '00')

    hour1 = int(hour1)
    hour2 = int(hour2)
    minute1 = minute1.zfill(2)
    minute2 = minute2.zfill(2)

    if am_pm1 == "PM" and hour1 < 12:
        hour1 += 12
    elif am_pm1 == "AM" and hour1 == 12:
        hour1 = 0

    if am_pm2 == "PM" and hour2 < 12:
        hour2 += 12
    elif am_pm2 == "AM" and hour2 == 12:
        hour2 = 0

    return f"{hour1:02}:{minute1} to {hour2:02}:{minute2}"


def input_time():
    """
    Retrieve time input from the user, either from command
    line arguments or through interactive terminal input.
    """
    if sys.argv[1:]:
        time = sys.argv[1:]
        if len(time) < 6:
            time = " ".join(time)
            return time

    return input("Hours: ")


if __name__ == "__main__":
    main()
