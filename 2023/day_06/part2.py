import math


def get_range(t: int, x: int) -> int:
    root = math.sqrt(t * t - 4 * x)
    return math.ceil((t + root) / 2 - 1) - math.floor((t - root) / 2 + 1) + 1


def main() -> None:
    content = open("input.txt").read()
    lines = content.splitlines()
    time = int(lines[0].split(": ")[1].replace(" ", ""))
    distance = int(lines[1].split(": ")[1].replace(" ", ""))

    print(get_range(time, distance))


if __name__ == "__main__":
    main()
