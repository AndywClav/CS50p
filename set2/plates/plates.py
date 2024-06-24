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

    found_number = False
    for i in range(len(s)):
        if s[i].isdigit():
            found_number = True
            if not s[i:].isdigit() or (i > 0 and s[i] == '0' and not s[i - 1].isalpha()):
                return False

    return True

main()
