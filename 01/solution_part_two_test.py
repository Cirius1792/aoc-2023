import unittest


word_to_digit = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "0": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

NUMBERS = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
REVERSE_NUMBER = [w[::-1] for w in NUMBERS]
word_to_digit_reversed = {k[::-1]:v for k,v in word_to_digit.items()}

def solve(line: str) -> int:
    def is_matching(word: str, pattern: str, converter):
        return (word.find(pattern), converter[pattern])

    def aux(line, to_match, converter):
        for i in range(len(line)):
            min_idx, min_idx_number = float("inf"), None
            for pattern in to_match:
                idx, number = is_matching(line[i:], pattern, converter)
                if idx >= 0 and idx < min_idx:
                    min_idx = idx
                    min_idx_number = number
            return min_idx_number

    first_digit = aux(line, NUMBERS, word_to_digit)
    second_digit = aux(line[::-1], REVERSE_NUMBER, word_to_digit_reversed)
    return int(first_digit + second_digit)


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

if __name__ == '__main__':
    with open('./01/input.txt', 'r') as reader:
        acc = 0
        for line in reader:
            acc += solve(line)
        print(f"result: {acc}")

