from twttr import shorten

def test_twttr():
    assert shorten("mAmAau") == "mm"


def main():
    test_twttr()


if __name__ == "__main__":
    main()
