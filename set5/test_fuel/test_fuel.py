from fue import convert, gauge

def main():
    ...


def test_convert_0():
    assert gauge() == 'E'


def test_convert_0():
    assert gauge() == '25%'


def test_convert_0():
    assert gauge() == '75%'


def test_convert_0():
    assert gauge() == 'F'


if __name__ == "__main__":
    main()
