from bank import value

def main():
    test_value_0()
    test_value_20()
    test_value_100()
    # test_value_str()


def test_value_0():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello") == 0


def test_value_20():
    assert value("how?") == 20
    assert value("HOW?") == 20
    assert value("How?") == 20


def test_value_100():
    assert value("what's your name?") == 100
    assert value("WHAT'S YOUR NAME?") == 100
    assert value("What's your name?") == 100


# def test_value_str():
#     assert value("") == 'This is outher alternative'


if __name__ == "__main__":
    main()
