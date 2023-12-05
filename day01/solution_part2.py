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
word_to_digit_reversed = {k[::-1]: v for k, v in word_to_digit.items()}


def solve(line: str) -> int:
    def is_matching(word: str, pattern: str, converter):
        return (word.find(pattern), converter[pattern])

    def aux(line, to_match, converter):
       min_idx, min_idx_number = float("inf"), None
       for pattern in to_match:
           idx, number = is_matching(line, pattern, converter)
           if idx >= 0 and idx < min_idx:
               min_idx = idx
               min_idx_number = number
       return min_idx_number

    first_digit = aux(line, NUMBERS, word_to_digit)
    second_digit = aux(line[::-1], REVERSE_NUMBER, word_to_digit_reversed)
    return int(first_digit + second_digit)


if __name__ == "__main__":
    with open("./01/input.txt", "r") as reader:
        acc = 0
        for line in reader:
            acc += solve(line)
        print(f"result: {acc}")
