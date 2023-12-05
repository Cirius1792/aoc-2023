import unittest

from solution_part1 import solve

class SolutionTest(unittest.TestCase):
    def test_should_return_the_first_and_last_digit(self):
        line = "1abc2"
        val = solve(line)
        assert 12 == val

    def test_should_return_the_digits_in_the_middle(self):
        line = "pqr3stu8vwx"
        val = solve(line)
        assert 38 == val

    def test_should_take_only_the_first_digits_found(self):
        line = "1b2c3d4e5f"
        val = solve(line)
        assert 15 == val

    def test_should_take_the_only_digit_as_first_and_last(self):
        line = "treb7uchet"
        val = solve(line)
        assert 77 == val


if __name__ == "__main__":
    with open("./01/input.txt", "r") as reader:
        acc = 0
        for line in reader:
            acc += solve(line)
        print(f"result: {acc}")
