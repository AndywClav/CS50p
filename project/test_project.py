from project import choose_square_size, sys_square_size, get_random_difficulty
from unittest.mock import patch
import pytest

def test_choose_square_size():
    assert choose_square_size("1") == 1
    assert choose_square_size("2") == 2


def test_error_choose_square_size():
    with pytest.raises(OSError):
        assert choose_square_size(1) == "asd"
    with pytest.raises(OSError):
        assert choose_square_size(2) == 3


def test_sys_square_size():
    assert sys_square_size("1") == 1
    assert sys_square_size("2") == 2


@patch("random.randint", return_value=1)
def test_sys_square_size_invalid_input_returns_1(mock_randint):
    assert sys_square_size("abc") == 1
    assert sys_square_size("5") == 1
    assert sys_square_size("") == 1
    mock_randint.assert_called_with(1, 2)


@patch("random.randint", return_value=2)
def test_sys_square_size_invalid_input_returns_2(mock_randint):
    assert sys_square_size("xyz") == 2
    assert sys_square_size("0") == 2
    assert sys_square_size("-3") == 2
    mock_randint.assert_called_with(1, 2)


@patch("random.choice", return_value="easy")
def test_get_random_difficulty_easy(mock_randint):
    assert get_random_difficulty() == "easy"
    mock_randint.assert_called_with(["easy", "medium", "hard"])


@patch("random.choice", return_value="medium")
def test_get_random_difficulty_medium(mock_randint):
    assert get_random_difficulty() == "medium"
    mock_randint.assert_called_with(["easy", "medium", "hard"])


@patch("random.choice", return_value="hard")
def test_get_random_difficulty_hard(mock_randint):
    assert get_random_difficulty() == "hard"
    mock_randint.assert_called_with(["easy", "medium", "hard"])
