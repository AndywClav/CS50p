import random

def choose_square_size(square_size: str) -> int:
    """
    The user to select a square size (2x2 or 3x3), or picks randomly if invalid.
    """
    MAX_ATTEMPTS: int = 2
    count: int = 0

    while True:
        if square_size in {"1", "2"}:
            break

        if count == MAX_ATTEMPTS:
            square_size = random.randint(1, 2)
            print(f"Your square was random.\n It's {square_size}.\n")
            break

        print("Invalid input. Please enter a valid option.")
        input("")

        count += 1

    return int(square_size)


def main():
    TITLEO_PENING: str = "Welcome to my game! 😝"
    TITLE: str = "SUDOKU"
    character = "-" * (len(TITLEO_PENING) + 4)
    print(f"{character}\n| {TITLEO_PENING} |\n{character}\n")

    size: int = choose_square_size(input(" What square do you want?\n Option 1: 2x2\n Option 2: 3x3\n[PLS] only number :)\n").strip())

    print(TITLE)


if __name__ == "__main__":
    main()

# json
# requests
# sys
# cowsay
# statistics
# pytest
# open
# csv
# PIL
# re



# Implementar Titulo grande, bien lindo de la libreria
# Estructure of cuadrade 2x2 or 2^2
# print("1 2 4 3 ")
# print("3 4 2 1 ")
# print("2 1 3 4 ")
# print("4 3 1 2 ")
# print("[1][2][4][3]\n"
#       "[3][4][2][1]\n"
#       "[2][1][3][4]\n"
#       "[4][3][1][2]")


# the cuadrade is a potential, Ej 2^2 = 4
#                                 3^3 = 9
# My game only have 2 table


