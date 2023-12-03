from typing import List, Tuple


def is_symbol(char: chr) -> bool:
    return char != "." and not char.isdigit()


def sum_part_numbers(lines: List[str]) -> int:
    height = len(lines)
    width = len(lines[0])

    total = 0
    y = 0

    while y < height:
        x0 = 0
        while x0 < width:
            if not lines[y][x0].isdigit():
                x0 += 1
                continue

            x1 = x0

            while x1 < width - 1 and lines[y][x1 + 1].isdigit():
                x1 += 1

            up = y - 1 >= 0 and any(
                is_symbol(lines[y - 1][x]) for x in range(x0, x1 + 1)
            )

            down = y + 1 < height and any(
                is_symbol(lines[y + 1][x]) for x in range(x0, x1 + 1)
            )
            right = x1 + 1 < width and is_symbol(lines[y][x1 + 1])

            left = x0 - 1 >= 0 and is_symbol(lines[y][x0 - 1])

            diagnoals_right = (x0 - 1 >= 0) and (
                y - 1 >= 0
                and is_symbol(lines[y - 1][x0 - 1])
                or y + 1 < height
                and is_symbol(lines[y + 1][x0 - 1])
            )

            diagnoals_left = (x1 + 1 < width) and (
                y - 1 >= 0
                and is_symbol(lines[y - 1][x1 + 1])
                or y + 1 < height
                and is_symbol(lines[y + 1][x1 + 1])
            )

            if up or down or right or left or diagnoals_right or diagnoals_left:
                total += int(lines[y][x0 : x1 + 1])

            x0 = x1 + 1
        y += 1

    return total


def main() -> None:
    with open("input.txt") as file:
        content = file.read()

    lines = content.splitlines()
    print(sum_part_numbers(lines))


if __name__ == "__main__":
    main()
