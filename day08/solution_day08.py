from typing import List, Dict, Tuple

Network = Dict[str, List[str]]


def parse_network(network_lines: List[str]) -> Network:
    def split_line(line: str) -> Tuple[str, str, str]:
        return (line[0:3], line[7:10], line[12:15])

    network = {}
    for line in network_lines:
        node, edge_l, edge_r = split_line(line)
        network[node] = [edge_l, edge_r]
    return network


def navigate(
    current_node: str,
    instruction: str,
    network: Network
) -> str:
    curr_pos = current_node
    for i in instruction:
        branch = 0 if i == "L" else 1
        curr_pos = network[curr_pos][branch]
    return curr_pos


def solve(problem_input: List[str]) -> int:
    acc = 0
    route = problem_input[0].strip()
    network = parse_network(problem_input[2:])
    current_position = "AAA"
    while current_position != "ZZZ":
        current_position = navigate(current_position, route, network)
        acc += len(route)
    return acc


if __name__ == "__main__":
    with open("./day08/input.txt", "r") as reader:
        solution = solve(reader.readlines())
        print(f"result: {solution}")
