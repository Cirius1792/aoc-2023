
from solution_day02 import parse_game, minimum_viable_game

def solve(line:str):
    _, extractions = parse_game(line)
    mvb = minimum_viable_game(extractions) # minimum_viable_solution
    return mvb.red * mvb.green * mvb.blue

if __name__ == "__main__":
    with open("./day02/input.txt", "r") as reader:
        acc = 0
        for line in reader:
            acc += solve(line)
        print(f"result: {acc}")
 


