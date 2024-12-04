from typing import List


def main():
    print(search(read_file()))


def search(field: List[List[str]]) -> int:
    count = 0
    for x, line in enumerate(field):
        if x in (0, len(field) - 1):
            continue
        for y, char in enumerate(line):
            if y in (0, len(line) - 1):
                continue
            if char == "A":
                if (
                    (field[x + 1][y + 1] == "M" and field[x - 1][y - 1] == "S")
                    or (field[x + 1][y + 1] == "S" and field[x - 1][y - 1] == "M")
                ) and (
                    (field[x + 1][y - 1] == "M" and field[x - 1][y + 1] == "S")
                    or (field[x + 1][y - 1] == "S" and field[x - 1][y + 1] == "M")
                ):
                    count += 1
    return count


def read_file() -> List[List[str]]:
    with open("input.txt") as file:
        return [list(line.strip()) for line in file]


if __name__ == "__main__":
    main()
