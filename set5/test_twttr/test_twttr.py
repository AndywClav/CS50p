from twttr import shorten

def test_twttr():
    assert shorten("mAmAau") == "mm"
    assert shorten("pAPou1") == "pP1"
    assert shorten("joUY.aAN") == "jY.N"


def main():
    test_twttr()


if __name__ == "__main__":
    main()
