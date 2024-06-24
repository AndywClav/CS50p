def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    no_valid = ['.', ',', ':', ';']
    if s.isupper():
        if len(s) >= 2 and len(s) <= 6:
            if '.' not in s:
                return True


main()
