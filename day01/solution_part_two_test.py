import unittest

from solution_part2 import solve

class SolutionPartTwoTest(unittest.TestCase):
    def test_should_read_first_and_last_word(self):
        line = "two1nine"
        print(line)
        expected = 29
        actual = solve(line)
        assert expected == actual

    def should_ignore_words_in_the_middle_test(self):
        line = "eightwothree"
        print(line)
        expected = 83
        actual = solve(line)
        assert expected == actual

    def test_should_read_words_in_the_middle(self):
        line = "abcone2threexyz"
        print(line)
        expected = 13
        actual = solve(line)
        assert expected == actual

    def test_should_do_stuff(self):
        line = "xtwone3four"
        print(line)
        expected = 24
        actual = solve(line)
        assert expected == actual

    def test_should_read_digits(self):
        line = "4nineeightseven2"
        print(line)
        expected = 42
        actual = solve(line)
        assert expected == actual

    def test_should_read_words_and_digits(self):
        line = "zoneight234"
        print(line)
        expected = 14
        actual = solve(line)
        assert expected == actual

    def test_should_do_some_more_stuff(self):
        line = "7pqrstsixteen"
        print(line)
        expected = 76
        actual = solve(line)
        assert expected == actual


