from working import convert
import pytest

def test_convert():
    assert convert('09:00 AM to 3:00 PM') == '09:00 to 15:00'
    assert convert('03:11 AM to 8:59 AM') == '03:11 to 08:59'


def test_error_convert():
    with pytest.raises(ValueError):
         convert('10:7 AM - 5:1 PM')
    with pytest.raises(ValueError):
         convert('8:60 AM to 4:60 PM')
    with pytest.raises(ValueError):
         convert('9 AM - 5 PM')
    with pytest.raises(ValueError):
         convert('9AM to 5PM')


if __name__ == '__main__':
    main()
