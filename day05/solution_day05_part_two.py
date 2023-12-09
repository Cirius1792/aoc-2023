from typing import List, Tuple

from time import perf_counter

from solution_day05 import parse_map, MapRange

def profiler(method):
    def wrapper_method(*arg, **kw):
        t = perf_counter()
        ret = method(*arg, **kw)
        print(
            "Method "
            + method.__name__
            + " took : "
            + "{:2.5f}".format(perf_counter() - t)
            + " sec"
        )
        return ret

    return wrapper_method

def parse_seed_range(seed_ranges: str) -> List[Tuple[int, int]]:
    seed_range_and_lenght = list(map(int, seed_ranges[6:].split()))
    ranges = []
    for i in range(0, len(seed_range_and_lenght), 2):
        range_start = seed_range_and_lenght[i]
        range_lenght = seed_range_and_lenght[i + 1]
        ranges.append((range_start, range_lenght))
    return ranges

def is_in_seed_range(seeds:List[Tuple[int, int]], v:int) -> bool:
    #print(f"Checking  {v}")
    for seed_range in seeds:
        if seed_range[0] <= v <= seed_range[0] + seed_range[1]:
            return True
    return False

#@profiler
def map_seed(mappings: List[MapRange], seed: int) -> int:
    mapped = seed
    for mapping in mappings:
        mapped = mapping.map(mapped)
    return mapped

def map_reverse(mappings: List[MapRange], location: int):
    #print("-"*10)
    mapped = location
    for mapping in mappings[::-1]:
        old = mapped
        mapped = mapping.map_reverse(mapped)
        #print(f"{old} -> {mapped} using: {mapping.map_name}")
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

    min_val = None
    loc,v = 0, -1
    while not min_val:
        v = map_reverse(mappings, loc)
        if is_in_seed_range(seeds, v):
            min_val  = loc
        loc += 1
    return min_val


if __name__ == "__main__":
    with open("./day05/input.txt", "r") as reader:
        acc = solve_part_two(reader.readlines())
        print(f"result: {acc}")
