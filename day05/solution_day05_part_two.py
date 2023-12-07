from tqdm import tqdm 
from typing import List, Generator


from solution_day05 import solve

def parse_seed_range(seed_ranges: str) -> Generator:
    seed_range_and_lenght = list(map(int, seed_ranges[6:].split()))

    tot_its = 0
    for i in range(0, len(seed_range_and_lenght), 2):
        range_lenght = seed_range_and_lenght[i + 1]
        tot_its += range_lenght
    with tqdm (total = tot_its) as pbar:
        for i in range(0, len(seed_range_and_lenght), 2):
            range_start = seed_range_and_lenght[i]
            range_lenght = seed_range_and_lenght[i + 1]
            for i in range(range_start, range_start + range_lenght):
                pbar.update(1)
                yield i   


def solve_part_two(problem_input: List[str]) -> int:
    return solve(problem_input, seeds_mapper=parse_seed_range)


if __name__ == "__main__":
    with open("./day05/input.txt", "r") as reader:
        acc = solve_part_two(reader.readlines())
        print(f"result: {acc}")



