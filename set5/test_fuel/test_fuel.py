from fue import convert, gauge

def main():
    test_convert_0():
    test_convert_25():
    test_convert_75():
    test_convert_100():


def test_convert_0():
    percentage = convert("0/1")
    assert gauge(percentage) == 'E'


def test_convert_25():
    percentage = convert("1/4")
    assert gauge(percentage) == '25%'


def test_convert_75():
    percentage = convert("0/1")
    assert gauge(percentage) == '75%'


def test_convert_100():
    percentage = convert("1/1")
    assert gauge(percentage) == 'F'


if __name__ == "__main__":
    main()
