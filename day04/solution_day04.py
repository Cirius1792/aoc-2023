from typing import List, Set


def parse_scratchcard(card: str):
    def build_num_set(num_line: str) -> Set[str]:
        number_set = set()
        for n in filter(lambda x: x, map(lambda x: x.strip(), num_line.split(" "))):
            assert n not in number_set
            number_set.add(n)
        return number_set

    card_raw = card.split(":")
    card_id = card_raw[0].split(" ")[1].strip()
    [your_numbers_raw, winning_numbers_raw] = card_raw[1].split("|")
    your_numbers = build_num_set(your_numbers_raw)
    winning_numbers = build_num_set(winning_numbers_raw)
    return card_id, your_numbers, winning_numbers


def find_winning_numbers(your_numbers: Set[str], card_numbers: Set[str]):
    return your_numbers.intersection(card_numbers)


def score(winning_numbers: Set[str]) -> int:
    return 2 ** (len(winning_numbers) - 1) if len(winning_numbers) != 0 else 0


def solve(scratches: List[str]) -> int:
    tot_score = 0
    for card in scratches:
        _, your_numbers, card_numbers = parse_scratchcard(card)
        winning_numbers = find_winning_numbers(your_numbers, card_numbers)
        tot_score += score(winning_numbers)
    return tot_score


if __name__ == "__main__":
    with open("./day04/input.txt", "r") as reader:
        acc = solve(reader.readlines())
        print(f"result: {acc}")
