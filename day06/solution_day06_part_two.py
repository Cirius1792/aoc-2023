from solution_day06 import solve

if __name__ == "__main__":
    with open("./day06/input_part_two.txt", "r") as reader:
        acc = solve(reader.readlines())
        print(f"result: {acc}")
