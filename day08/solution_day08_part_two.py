from typing import List
from solution_day08 import Network, parse_network, navigate


def find_starting_nodes(network: Network) -> List[str]:
    return list(filter(lambda x: x[2] == "A", network.keys()))


def solve(problem_input: List[str]) -> int:
    acc = 0
    route = problem_input[0].strip()
    network = parse_network(problem_input[2:])
    current_position = find_starting_nodes(network)
    while not all(map(lambda pos: pos[2] == "Z", current_position)):
        for i, pos in enumerate(current_position):
            current_position[i] = navigate(pos, route, network)
        acc += len(route)
    return acc


if __name__ == "__main__":
    with open("./day08/input.txt", "r") as reader:
        solution = solve(reader.readlines())
        print(f"result: {solution}")
