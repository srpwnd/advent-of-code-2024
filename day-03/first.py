import re
from typing import List, Tuple


def main():
    print(calculate(extract_instructions(load_file())))


def load_file() -> str:
    with open("input.txt", "r") as file:
        return file.read()


def extract_instructions(input: str) -> List[Tuple[str, str]]:
    return re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input)


def calculate(input: List[Tuple[str, str]]) -> int:
    return sum([int(a) * int(b) for a, b in input])


if __name__ == "__main__":
    main()