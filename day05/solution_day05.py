from typing import List

from collections import namedtuple
from typing import List
from prettytable import PrettyTable

Range = namedtuple("Range", "target source lenght")


class MapRange:
    def __init__(self, map_name, ranges: List[Range]):
        self.map_name = map_name
        self.ranges: List[Range] = list(ranges)
        self.ranges.sort(key=lambda t: t.source)

    def map(self, v: int) -> int:
        range = None
        for r in self.ranges:
            if r.source <= v <= r.source + r.lenght - 1:
                #        print(f"Found range{r}")
                range = r
                break
        if range:
            return v - range.source + range.target
        return v


def parse_map(lines: List[str]) -> MapRange:
    ranges = []
    for line in lines[1:]:
        values_per_line = list(map(int, line.split()))
        ranges.append(Range(values_per_line[0], values_per_line[1], values_per_line[2]))

    return MapRange(lines[0].split()[0], ranges)


def parse_seeds(line: str) -> List[int]:
    return list(map(int, line.split()[1:]))


def map_seed(mappings: List[MapRange], seed: int) -> int:
    if not mappings:
        print("-"*10)
        return seed
    mapped = mappings[0].map(seed)
    print(f"Mapping {seed} \t-> {mapped} | using:\t {mappings[0].map_name}")
    return map_seed(mappings[1:], mapped)


def solve(lines: List[str]) -> int:
    seeds = parse_seeds(lines[0])
    mappings = []
    map_lines = []
    for line in lines[2:]:
        print(f"Line: {line}")
        if not line.strip():
            mapping = parse_map(map_lines)
            print(f"Mapped: {mapping.map_name}")
            mappings.append(mapping)
            map_lines = []
        else:
            map_lines.append(line)
    mappings.append(parse_map(map_lines))
    return min(map(lambda s: map_seed(mappings, s), seeds))


if __name__ == "__main__":
    with open("./day05/input.txt", "r") as reader:
        acc = solve(reader.readlines())
        print(f"result: {acc}")
