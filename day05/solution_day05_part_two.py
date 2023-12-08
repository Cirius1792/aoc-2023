from tqdm import tqdm 
from typing import List, Generator

import multiprocessing 
import functools

from collections import namedtuple
from solution_day05 import parse_map

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

Range = namedtuple("Range", "target source lenght")


class MapRange:
    def __init__(self, map_name, ranges: List[Range]):
        self.map_name = map_name
        self.ranges: List[Range] = list(ranges)
        self.ranges.sort(key=lambda t: t.source)

    def map(self, v: int) -> int:
        range = self.ranges[-1]
        if not(range.source <= v <= range.source + range.lenght - 1):
            return v
        for r in self.ranges:
            if r.source <= v <= r.source + r.lenght - 1:
                range = r
                break
        return v - range.source + range.target

def map_seed(mappings: List[MapRange], seed: int) -> int:
    mapped = seed
    for mapping in mappings: 
        mapped = mapping.map(mapped)
    return mapped



def solve_part_two(lines: List[str]) -> int:
    seeds = parse_seed_range(lines[0])
    mappings = []
    map_lines = []
    for line in lines[2:]:
        if not line.strip():
            mapping = parse_map(map_lines)
            mappings.append(mapping)
            map_lines = []
        else:
            map_lines.append(line)
    mappings.append(parse_map(map_lines))

    pool = multiprocessing.Pool()
    min_val = None
    for v in pool.imap_unordered(functools.partial(map_seed, mappings), seeds, chunksize=50000):
        if not min_val or v < min_val:
            min_val = v
    return min_val






if __name__ == "__main__":
    with open("./day05/input.txt", "r") as reader:
        acc = solve_part_two(reader.readlines())
        print(f"result: {acc}")



