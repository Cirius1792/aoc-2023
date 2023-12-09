from typing import List, Tuple


from solution_day06 import solve


def parse_input(input_lines: List[str]) -> List[Tuple[int, int]]:
    assert len(input_lines) == 2
    time = int("".join(map(lambda x: x.strip(), input_lines[0].split(":")[1].split())))
    distance = int(
        "".join(map(lambda x: x.strip(), input_lines[1].split(":")[1].split()))
    )
    return [(time, distance)]


from numba import jit, prange

@jit(nopython=True, parallel=True)
def find_winning_tb(race: Tuple[int, int]) -> int:
    def eval_distance(ta: int, tc: int) -> int:
        return tc * ta

    winning_t_b = 0
    t = race[0] 
    for ta in prange (1, t):
        d = eval_distance(ta, t - ta)
        if  d > race[1]:
            winning_t_b += 1
    return winning_t_b


def solve(input_lines: List[str]) -> int:
    races = parse_input(input_lines)
    acc = 1
    for race in races:
        acc *= find_winning_tb(race)
    return acc


if __name__ == "__main__":
    with open("./day06/input.txt", "r") as reader:
        acc = solve(reader.readlines())
        print(f"result: {acc}")
