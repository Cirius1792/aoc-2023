import unittest

def get_value_from_words(line:str) -> int:
    return 0

class SolutionPartTwoTest(unittest.TestCase):
    def test_should_return_the_first_and_last_digit(self):
        line = 'two1nine'
        expected = 29
        actual = get_value_from_words(line)
        assert actual == expected


    def test_should_take_only_the_first_digits_found(self):
        line = 'eightwothree'
        expected = 83
        actual = get_value_from_words(line)
        assert actual == expected


    def test_should_take_the_only_digit_as_first_and_last(self):
        line = 'abcone2threexyz'
        expected = 13
        actual = get_value_from_words(line)
        assert actual == expected

    def test_should_take_only_the_first_digit_matched(self):
        line = 'xtwone3four'
        expected = 24
        actual = get_value_from_words(line)
        assert actual == expected


    def test_should_work_also_for_numeric_digits(self):
        line = '4nineeightseven2'
        expected = 42
        actual = get_value_from_words(line)
        assert actual == expected

        line = 'zoneight234'
        expected = 14
        actual = get_value_from_words(line)
        assert actual == expected


    def test_should_not_match_words_above_nine(self):
        line = '7pqrstsixteen'
        expected = 76
        actual = get_value_from_words(line)
        assert actual == expected


if __name__ == '__main__':
    with open('./01/input_part_two.txt', 'r') as reader:
        acc = 0
        for line in reader:
            acc += get_value_from_words(line)
        print(f"result: {acc}")

