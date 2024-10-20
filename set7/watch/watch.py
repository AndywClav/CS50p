import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    """
    Get url youtube if you put iframe html
    """
    if url_yout := re.search(r"^http(s)?://(www\.)?youtube.com/.$") in s:
        return url_yout


if __name__ == "__main__":
    main()
