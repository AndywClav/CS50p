from twttr import shorten

def test_twttr_vowel():
    assert shorten("mAmAau") == "mm"


def test_twttr_number():
    assert shorten("pAPou1") == "pP1"


def test_twttr_point():
    assert shorten("joUY.aAN") == "jY.N"


def main():
    test_twttr_vowel()
    test_twttr_number()
    test_twttr_point()


if __name__ == "__main__":
    main()
