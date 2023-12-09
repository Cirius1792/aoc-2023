from typing import List, Tuple 


def parse_input(input_lines: List[str]) -> List[Tuple[int, int]]:
    assert len(input_lines) == 2
    times = map(lambda x: int(x.strip()), input_lines[0].split(":")[1].split())
    distances = map(lambda x: int(x.strip()), input_lines[1].split(":")[1].split())
    return [(t, d) for t, d in zip(times, distances)]


def find_winning_tb(race: Tuple[int, int]) -> List[int]:
    def eval_distance(ta:int, tc:int, m: List[List[int]]) -> int:
        if ta == tc: 
            return 0
        if ta == 0: 
            return 0
        return m[ta][tc-1] + ta

    winning_t_b = set()
    t = race[0] +1
    m:List[List[int]]= [[0 for _ in range(t)] for _ in range(t)]
    for ta in range(t):
        for tc in range(ta, t):
            m[ta][tc] = eval_distance(ta, tc, m)
#            print(f"ta {ta}, tc {tc} -> {m[ta][tc]}")
            if m[ta][tc] > race[1]:
                winning_t_b.add(ta)
#    for line in m: 
#        print(line)

    return list(winning_t_b)

def solve(input_lines:List[str]) -> int:
    races = parse_input(input_lines)
    acc = 1
    for race in races: 
        acc *= len(find_winning_tb(race))
    return acc


if __name__ == "__main__":
    with open("./day06/input.txt", "r") as reader:
        acc = solve(reader.readlines())
        print(f"result: {acc}")
