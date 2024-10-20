import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    """
    Get url youtube if you put iframe html
    """
    for line in s:
        if url_yout := re.search(r"^https?://(www\.)?youtube\.com/.*$", line):
            return format(url_yout.group(0))
    return None


if __name__ == "__main__":
    main()
