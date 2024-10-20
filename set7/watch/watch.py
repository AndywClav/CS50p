import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    """
    Get url youtube if you put iframe html
    """
    if url_yout := re.search(r"^https?://(www\.)?youtube\.com/.*$", s).group(0):
        return format(url_yout)
    return None


if __name__ == "__main__":
    main()
