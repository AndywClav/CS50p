import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    """
    Get URL of YouTube from the iframe HTML string.
    """
    if url_yout := re.search(r'(<iframe.*)?(src="?(https?://(www\.)?youtube\.com/embed/[^"]+))".*?>', s):
        re.search(r'(<iframe.*?src="?(https?://(www\.)?youtube\.com/embed/[^"]+)"?.*?>|https?://(www\.)?youtube\.com/embed/[^"]+)', s)
        return url_yout.group(1)
    return None


if __name__ == "__main__":
    main()
