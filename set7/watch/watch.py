import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    """
    Get URL of YouTube from the iframe HTML string.
    """
    if url_yout := re.search(r'<iframe.*?src="?(https?://(www\.)?youtube\.com/embed/[^"]+)"?.*?>', s):
        return url_yout.group(1)
    elif url_yout == re.search(r"^https?://(www\.)?youtube\.com/.*$", s).group(0):
        return url_yout
    else:
        None


if __name__ == "__main__":
    main()
