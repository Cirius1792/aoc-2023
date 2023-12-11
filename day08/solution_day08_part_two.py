import math
from typing import List
from solution_day08 import Network, parse_network, navigate


def find_starting_nodes(network: Network) -> List[str]:
    return list(filter(lambda x: x[2] == "A", network.keys()))


def solve(problem_input: List[str]) -> int:
    def is_final_position(pos: str) -> bool:
        return pos[2] == "Z"

    route = problem_input[0].strip()
    route_len = len(route)
    network = parse_network(problem_input[2:])
    starting_postion = find_starting_nodes(network)
    initial_pos_cycle_time = {i: 0 for i in range(len(starting_postion))}
    for i, pos in enumerate(starting_postion):
        cur_pos = pos
        final_position_seen_count = 0
        while final_position_seen_count != 1:
            cur_pos = navigate(cur_pos, route, network)
            initial_pos_cycle_time[i] += 1
            if is_final_position(cur_pos):
                final_position_seen_count += 1
    return math.lcm(*initial_pos_cycle_time.values()) * route_len


if __name__ == "__main__":
    with open("./day08/input.txt", "r") as reader:
        solution = solve(reader.readlines())
        print(f"result: {solution}")
