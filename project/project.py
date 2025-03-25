import random
import sys
import cowsay
from fpdf import FPDF

MAX_ATTEMPTS: int = 2
TITLE_OPENING: str = "Welcome to my project! 😝"
TITLE: str = "SUDOKU"

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", '', 14)

class Sudoku:
    def __init__(self, size: int, difficulty: str, name_file: str = None):
        size = 2 if size == 1 else 3

        self.box_size = size
        self.size = size * size
        self.board = [[0] * self.size for _ in range(self.size)]

        self.name_file = name_file if name_file is not None else "solve.pdf"

        self.generate_board()
        self.remove_numbers(difficulty)
        self.display()


    def generate_board(self):
        base = [[(i * self.box_size + i // self.box_size + j) % self.size + 1
                 for j in range(self.size)] for i in range(self.size)]

        self.shuffle_board(base)
        self.board = base


    def shuffle_board(self, board):
        for _ in range(10):
            self.shuffle_rows(board)
            self.shuffle_columns(board)


    def shuffle_rows(self, board):
        for i in range(0, self.size, self.box_size):
            random.shuffle(board[i:i + self.box_size])


    def shuffle_columns(self, board):
        for i in range(0, self.size, self.box_size):
            cols = list(zip(*board))
            random.shuffle(cols[i:i + self.box_size])
            board[:] = [list(row) for row in zip(*cols)]


    def remove_numbers(self, difficulty: str):
        difficulty_levels = {"easy": 0.2, "medium": 0.4, "hard": 0.6}
        percent_to_remove = difficulty_levels.get(difficulty, 0.4)

        num_to_remove = int(self.size * self.size * percent_to_remove)
        positions = [(i, j) for i in range(self.size) for j in range(self.size)]
        random.shuffle(positions)

        for i, j in positions[:num_to_remove]:
            self.board[i][j] = 0


    def display(self):
        pdf.cell(0, 10, TITLE, ln=True, align='C')

        for i, row in enumerate(self.board):
            if i % self.box_size == 0 and i != 0:
                print("-" * (self.size * 2 + self.box_size - 1))

            row_str = ""
            for j, num in enumerate(row):
                if j % self.box_size == 0 and j != 0:
                    row_str += "| "
                row_str += (str(num) if num != 0 else ".") + " "

            pdf.cell(0, 20, row_str, ln=True)

        pdf.output(self.name_file)


def choose_square_size(square_size: str) -> int:
    """
    Asks the user to select a square size (2x2 or 3x3).
    If the input is invalid, the user gets two attempts before
    a random size (1 or 2) is selected automatically.
    """
    for _ in range(MAX_ATTEMPTS):
        if square_size in {"1", "2"}:
            return int(square_size)
        print("Invalid input. Please enter a valid option.")
        square_size = input("").strip()

    return random.randint(1, 2)


def sys_square_size(value: str) -> int:
    """
    Returns the integer value if it is '1' or '2'.
    Otherwise, returns a random number (1 or 2).
    """
    return int(value) if value in {"1", "2"} and value.isdigit() else random.randint(1, 2)


def get_random_difficulty():
    """Returns a random Sudoku difficulty level."""
    return random.choice(["easy", "medium", "hard"])


def main():
    character = "-" * (len(TITLE_OPENING) + 4)
    print(f"{character}\n| {TITLE_OPENING} |\n{character}\n")

    size = (
        choose_square_size(
            input(
                " What square do you want?\n"
                " Option 1: 2x2\n"
                " Option 2: 3x3\n"
                " [PLS] only number :)\n"
                ).strip())
            if len(sys.argv) != 2 else sys_square_size(sys.argv[1])
        )

    cowsay.miki(TITLE)

    sudoku = Sudoku(size, difficulty=get_random_difficulty())
    sudoku.display()


if __name__ == "__main__":
    main()
