# Print Sudoku
## About the Creator

Hi there! I'm __Andrés Clavijo__.
__I’m__ a software development student from Colombia, now living in Argentina. I love programming and problem-solving, always looking for ways to improve my coding skills.

- **GitHub**: [AndywClav][https://github.com/AndywClav]
- **Edx**: Andy22_24
- **Linkedin**: [andywclav][https://www.linkedin.com/in/andywclav/?originalSubdomain=ar]
- **City**: Buenos Aires, Argentina

## Project Description

- Print Sudoku is a simple Sudoku generator that creates a puzzle for you to play on paper. You just run it in the terminal, pick a grid size (either 2x2 or 3x3), and the program will generate a puzzle with some numbers already filled in. It removes a few numbers depending on the difficulty, and then gives you a PDF to download and print so you can solve it at home.

## Features

- ✔️ Written in Python
- ✔️ Provides randomly generated Sudoku puzzles
- ✔️ Allows selection of difficulty level
- ✔️ Saves the puzzle as a PDF file
- ✔️ Uses only three functions outside the Sudoku class
- ✔️ Includes unit tests

## How to Use the Project
### Installation

- Before running the project, you need to install the required dependencies. Run the following command:

`pip install -r requirements.txt`

### Running the Program

- To start the Sudoku generator, run the following command:

`python project.py`

- The program will ask you to select a grid size:


Option 1: 2x2 (4x4 board)
Option 2: 3x3 (9x9 board)

- After selecting the grid size, the program will generate a Sudoku puzzle with a random difficulty level (easy, medium, or hard). The puzzle will be printed in the terminal and saved as a PDF file (solve.pdf).

Example Output

```bash
    ----------------------------
    | Welcome to my project! 😝 |
    ----------------------------
    What square do you want?
    Option 1: 2x2
    Option 2: 3x3
    [PLS] only number :)
```

- After selecting a grid size, the program will print a Sudoku puzzle in the terminal, formatted with numbers and empty spaces (represented by dots .).

## About the Tests

- The project includes unit tests to ensure that the functions work correctly. The tests are located in the test.project.py file and cover the following functions:

## Test Cases

- choose_square_size(): Ensures that valid user input ("1" or "2") returns the correct grid size.
- sys_square_size(): Checks that valid inputs return the expected results and invalid inputs return a random value.
- get_random_difficulty(): Verifies that a random difficulty level is chosen correctly.

## Running the Tests

- To run the tests, use the following command:

`pytest test.project.py`

- If all tests pass, you will see output indicating that the functions are working correctly.

## Video Demo

- **Video URL**: [Click to watch](https://youtu.be/roxQQ2bK1c0)
- **Recording Date**: February 12, 2025

I hope you enjoy my project 🎉
