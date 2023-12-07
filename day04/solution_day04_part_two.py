
from typing import List, Dict

from solution_day04 import parse_scratchcard, find_winning_numbers


def find_won_cards(card_id: int, winning_numbers) -> List[int]:
    cards = [(card_id + i + 1) for i in range(len(winning_numbers))]
    return cards


def count_won_cards(scratches: List[str]) -> Dict[int,int]:
    n_scratches = len(scratches)
    cards = {i + 1: 1 for i in range(n_scratches)}
    for card in scratches:
        id, your_numbers, card_numbers = parse_scratchcard(card)
        winning_numbers = find_winning_numbers(your_numbers, card_numbers)
        won_cards = find_won_cards(id, winning_numbers)
        increment = cards[id]
        for i in won_cards:
            if i in cards:
                cards[i] += increment
    return cards

def count_score(won_card_count:Dict[int,int]) -> int:
    return sum(won_card_count.values())

def solve(cards:List[str]) -> int:
    won_cards = count_won_cards(cards)
    return count_score(won_cards)

if __name__ == "__main__":
    with open("./day04/input.txt", "r") as reader:
        acc = solve(reader.readlines())
        print(f"result: {acc}")
