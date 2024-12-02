from typing import List


def main():
    print(check_all_levels(load_file()))


def load_file() -> List[List[int]]:
    with open("input.txt") as file:
        output = []
        for line in file:
            output.append(list(map(int, line.strip().split())))

        return output


def check_level_safety(level: List[int]) -> bool:
    for i in range(len(level)):
        skipped = level[:i] + level[i + 1 :]
        if check_max_step(skipped) and check_increasing_decreasing(skipped):
            return True
    return False


def check_max_step(level: List[int]) -> bool:
    return all(
        [1 <= abs(first - second) <= 3 for first, second in zip(level, level[1:])]
    )


def check_increasing_decreasing(level: List[int]) -> bool:
    return all([first > second for first, second in zip(level, level[1:])]) or all(
        [first < second for first, second in zip(level, level[1:])]
    )


def check_all_levels(levels: List[List[int]]) -> int:
    return sum(map(check_level_safety, levels))


if __name__ == "__main__":
    main()
