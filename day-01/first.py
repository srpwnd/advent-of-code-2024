from typing import List, Tuple


def main():
    left_list, right_list = load_file()
    print(process(left_list, right_list))


def load_file() -> Tuple[List[int], List[int]]:
    with open("input.txt", "r") as file:
        left_list, right_list = [], []
        for line in file.readlines():
            left, right = line.strip().split()
            left_list.append(int(left))
            right_list.append(int(right))
        return left_list, right_list


def process(left_list: List[int], right_list: List[int]) -> int:
    return sum(
        [
            abs(left - right)
            for left, right in zip(sorted(left_list), sorted(right_list))
        ]
    )


if __name__ == "__main__":
    main()
