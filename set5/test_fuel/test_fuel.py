from fue import convert, gauge


def main():
    # test_fuel()
    test_fuel_0()
    test_fuel_25()
    test_fuel_75()
    test_fuel_100()


# def test_fuel():
#     convert_fraction = convert("1/0")
#     if isinstance(convert_fraction, float):
#             percentage = gauge(convert_fraction)
#             return print(percentage)

#      assert convert_fraction == "ZeroDivisionError"


def test_fuel_0():
    percentage = convert("0/1")
    assert gauge(percentage) == 'E'


def test_fuel_25():
    percentage = convert("1/4")
    assert gauge(percentage) == '25%'


def test_fuel_75():
    percentage = convert("9/12")
    assert gauge(percentage) == '75%'


def test_fuel_100():
    percentage = convert("1/1")
    assert gauge(percentage) == 'F'


if __name__ == "__main__":
    main()
