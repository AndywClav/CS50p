def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[:2].isalpha():
        return False

    if not s.isalnum():
        return False

    #has_number = False
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False
            #has_number = True
            if s[i] == '0':
                return False
            break

    return True


main()
