import math
from typing import List


def create_int_list(string: str) -> List[int]:
    return [int(num) for num in string.split()]


def get_range(t: int, x: int) -> int:
    root = math.sqrt(t * t - 4 * x)
    return math.ceil((t + root) / 2 - 1) - math.floor((t - root) / 2 + 1) + 1


def main() -> None:
    content = open("input.txt").read()
    lines = content.splitlines()
    times = create_int_list(lines[0].split(": ")[1])
    distances = create_int_list(lines[1].split(": ")[1])

    product = 1
    for t, x in zip(times, distances):
        product *= get_range(t=t, x=x)

    print(product)


if __name__ == "__main__":
    main()
