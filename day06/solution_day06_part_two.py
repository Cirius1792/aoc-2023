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
    def eval_distance(ta: int, tc: int, tc_1: int) -> int:
        if ta == tc:
            return 0
        if ta == 0:
            return 0
        return tc_1 + ta

    winning_t_b = 0
    t = race[0] + 1
    tc_1 = 0
    for ta in prange (1, t):
        tc_1 = 0
        for tc in range(ta +1, t):
            #print(f"ta: {ta} tc:{tc} tc_1: {tc_1}")
            tc_1 = eval_distance(ta, tc, tc_1)
            if tc_1 > race[1]:
                winning_t_b += 1
                break
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
