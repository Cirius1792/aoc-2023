def solve(line: str) -> int:
    i = 0
    first_digit = ""
    last_digit = ""
    while i < len(line) and (not first_digit or not last_digit):
        if not first_digit and line[i].isdigit():
            first_digit = line[i]
        j = -(i + 1)
        if not last_digit and line[j].isdigit():
            last_digit = line[j]
        i += 1
    return int(first_digit + last_digit)


if __name__ == "__main__":
    with open("./input.txt", "r") as reader:
        acc = 0
        for line in reader:
            acc += solve(line)
        print(f"result: {acc}")
