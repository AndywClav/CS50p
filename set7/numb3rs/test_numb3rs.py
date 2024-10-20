import numb3rs

def main():
    test_valid_ipv4()
    test_invalid_ipv4()


def test_valid_ipv4():
    """
    This function validate the function with valid IPv4
    addresses.
    """
    assert numb3rs.validate("192.168.0.1") == True
    assert numb3rs.validate("10.0.0.1") == True
    assert numb3rs.validate("0.0.0.0") == True
    assert numb3rs.validate("255.255.255.255") == True
    assert numb3rs.validate("172.16.0.1") == True
    assert numb3rs.validate("8.8.8.8") == True
    assert numb3rs.validate("192.168.01.1") == True


def test_invalid_ipv4():
    """
    This function validate the function with invalid IPv4
    addresses.
    """
    assert numb3rs.validate("256.0.0.0") == False
    assert numb3rs.validate("192.133.0.256") == False
    assert numb3rs.validate("192.168..1") == False
    assert numb3rs.validate("192.168.0.1.2") == False
    assert numb3rs.validate("10.10.10.10.10") == False
    assert numb3rs.validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False


if __name__ == "__main__":
    main()
