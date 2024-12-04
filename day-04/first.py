from typing import List, Tuple


def main():
    print(count_phrases(read_file(), "XMAS"))


def recursive_search(
    field: List[List[str]], x: int, y: int, direction: Tuple[int, int], phrase: str
) -> int:
    if not phrase:
        return 1
    if x < 0 or x >= len(field) or y < 0 or y >= len(field[0]):
        return 0
    if field[x][y] != phrase[0]:
        return 0

    xdir, ydir = direction
    return recursive_search(field, x + xdir, y + ydir, direction, phrase[1:])


def search(field: List[List[str]], x: int, y: int, phrase: str) -> int:
    return (
        recursive_search(field, x, y, (1, 0), phrase)
        + recursive_search(field, x, y, (-1, 0), phrase)
        + recursive_search(field, x, y, (0, 1), phrase)
        + recursive_search(field, x, y, (0, -1), phrase)
        + recursive_search(field, x, y, (1, 1), phrase)
        + recursive_search(field, x, y, (1, -1), phrase)
        + recursive_search(field, x, y, (-1, -1), phrase)
        + recursive_search(field, x, y, (-1, 1), phrase)
    )


def count_phrases(field: List[List[str]], phrase: str) -> int:
    count = 0
    for x, line in enumerate(field):
        for y, _ in enumerate(line):
            count += search(field, x, y, phrase)
    return count


def read_file() -> List[List[str]]:
    with open("input.txt") as file:
        return [list(line.strip()) for line in file]


if __name__ == "__main__":
    main()
