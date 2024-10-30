import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    """
    Extract and convert a YouTube URL from an iframe HTML string to a shortened youtu.be format.
    """
    url_yout_iframe = r'<iframe.*?src="(https?://(?:www\.)?youtube\.com/embed/([^"]+))".*?></iframe>$'
    url_match = re.search(url_yout_iframe, s)

    if not url_match:
        return None

    video_id = url_match.group(2)
    return f"https://youtu.be/{video_id}"


if __name__ == "__main__":
    main()
