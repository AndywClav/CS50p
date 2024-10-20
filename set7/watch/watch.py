import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    """
    Get url youtube if you put iframe html
    """
    if url_yout := re.search(r"^https?://(www\.)?youtube\.com/.*$", s):
        return format(url_yout.group(0))
    return None


if __name__ == "__main__":
    main()
