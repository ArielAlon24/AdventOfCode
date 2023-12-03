from typing import List, Tuple

MOVES: List[Tuple[int, int]] = [
    (0, 1),
    (1, 0),
    (1, 1),
    (0, -1),
    (-1, 0),
    (-1, -1),
    (-1, 1),
    (1, -1),
]


def extract_number(lines: List[str], x1: int, y1: int) -> int:
    if not lines[y1][x1].isdigit():
        raise ValueError("(x1, y1) must be a digit.")
    x0 = x2 = x1
    while x0 - 1 >= 0 and lines[y1][x0 - 1].isdigit():
        x0 -= 1
    while x2 + 1 < len(lines[0]) and lines[y1][x2 + 1].isdigit():
        x2 += 1
    return int(lines[y1][x0 : x2 + 1])


def sum_gear_ratios(lines: List[str]) -> int:
    height = len(lines)
    width = len(lines[0])

    result = 0

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != "*":
                continue

            numbers = set()

            for move in MOVES:
                x1, y1 = x + move[0], y + move[1]
                if lines[y1][x1].isdigit():
                    numbers.add(extract_number(lines=lines, x1=x1, y1=y1))

            if len(numbers) == 2:
                result += numbers.pop() * numbers.pop()

    return result


def main() -> None:
    with open("input.txt") as file:
        content = file.read()

    lines = content.splitlines()

    print(sum_gear_ratios(lines))


if __name__ == "__main__":
    main()
