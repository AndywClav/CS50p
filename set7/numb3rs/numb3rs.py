import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """
    This function validate if the ipv4 is correct with regular expressions, only ipv4
    """
    if format_ipv4 := re.search(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip):
        split_ip = ip.split(".")
        for i in split_ip:
            if int(i) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
