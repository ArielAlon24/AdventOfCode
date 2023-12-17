from typing import List, Tuple

START_CHAR = "S"

VERTICAL = "|"
HORIZONTAL = "-"
NORTH_EAST = "L"  # TOP RIGHT
NORTH_WEST = "J"  # TOP LEFT
SOUTH_WEST = "7"  # BOTTOM LEFT
SOUTH_EAST = "F"  # BOTTOM RIGHT

TOP = [VERTICAL, SOUTH_EAST, SOUTH_WEST]
BOTTOM = [VERTICAL, NORTH_EAST, NORTH_WEST]
LEFT = [NORTH_EAST, SOUTH_EAST, HORIZONTAL]
RIGHT = [NORTH_WEST, SOUTH_WEST, HORIZONTAL]


def main() -> None:
    content = open("input.txt").read()

    lines = content.splitlines()
    x0, y0 = find_start(lines)

    pointers: List[Tuple[int, int]] = []
    prevs: List[Tuple[int, int]] = []

    if x0 - 1 >= 0 and lines[y0][x0 - 1] in LEFT:
        pointers.append((x0 - 1, y0))
        prevs.append((x0, y0))
    if x0 + 1 < len(lines[0]) and lines[y0][x0 + 1] in RIGHT:
        pointers.append((x0 + 1, y0))
        prevs.append((x0, y0))
    if y0 - 1 >= 0 and lines[y0 - 1][x0] in TOP:
        pointers.append((x0, y0 - 1))
        prevs.append((x0, y0))
    if y0 + 1 < len(lines) and lines[y0 + 1][x0] in BOTTOM:
        pointers.append((x0, y0 + 1))
        prevs.append((x0, y0))

    print(pointers, prevs)
    count = 0
    while len(set(pointers)) == len(pointers) and len(pointers) != 0:
        count += 1
        for index, (prev, pointer) in enumerate(zip(prevs, pointers)):
            x0, y0 = prev
            x1, y1 = pointer
            dx, dy = x1 - x0, y1 - y0
            char = lines[y1][x1]

            if (
                char == HORIZONTAL
                and dx == 1
                and x1 + 1 < len(lines[0])
                and lines[y1][x1 + 1] in RIGHT
            ):
                prevs[index] = (x1, y1)
                pointers[index] = (x1 + 1, y1)
            elif (
                char == HORIZONTAL
                and dx == -1
                and x1 - 1 >= 0
                and lines[y1][x1 - 1] in LEFT
            ):
                prevs[index] = (x1, y1)
                pointers[index] = (x1 - 1, y1)

            if (
                char == HORIZONTAL
                and 0 <= x1 + dx < len(lines[0])
                and (dx > 0 and lines[y1][x1 + dx] in UP)
                or (dx < 0 and lines[y1][x1 + dx] in DOWN)
            ):
                prevs[index] = (x1, y1)
                pointers[index] = (x1 + dx, y1)
            elif (
                char == VERTICAL
                and 0 <= y1 + dy < len(lines)
                and (dy < 0 and lines[y1 + dy][x1] in RIGHT)
                or (dy > 0 and lines[y1 + dy][x1] in LEFT)
            ):
                prevs[index] = (x1, y1)
                pointers[index] = (x1, y1 + dy)
            elif (
                char == NORTH_EAST
                and 0 <= x1 + 1 < len(lines[0])
                and lines[y1][x1 + 1] in RIGHT
            ):
                prevs[index] = (x1, y1)
                pointers[index] = (x1 + 1, y1 + 1)
            elif (
                char == NORTH_WEST
                and 0 <= x1 - 1 < len(lines[0])
                and lines[y1][x1 - 1] in LEFT
            ):
                prevs[index] = (x1, y1)
                pointers[index] = (x1 - 1, y1)
            elif (
                char == SOUTH_WEST
                and 0 <= x1 - 1 < len(lines[0])
                and lines[y1][x1 - 1] in LEFT
            ):
                prevs[index] = (x1, y1)
                pointers[index] = (x1 - 1, y1)
            elif (
                char == SOUTH_EAST
                and 0 <= x1 + 1 < len(lines[0])
                and lines[y1][x1 + 1] in RIGHT
            ):
                prevs[index] = (x1, y1)
                pointers[index] = (x1 + 1, y1)
            else:
                prevs.pop(index)
                pointers.pop(index)
    print(count)


def find_start(lines: List[str]) -> Tuple[int, int]:
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == START_CHAR:
                return x, y

    return 0, 0


if __name__ == "__main__":
    main()
