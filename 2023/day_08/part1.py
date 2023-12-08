from typing import Generator, Dict, List, Tuple


def move_generator(play: str) -> Generator[int, None, None]:
    index = -1
    while True:
        index = (index + 1) % len(play)
        yield 1 if play[index] == "R" else 0


def generate_mapping(lines: List[str]) -> Dict[str, Tuple[str, str]]:
    mapping = {}
    for line in lines:
        key, values = line.split(" = ")
        value1, value2 = values.replace("(", "").replace(")", "").split(", ")
        mapping[key] = (value1, value2)
    return mapping


def traverse(
    mapping: Dict[str, Tuple[str, str]],
    generator: Generator[int, None, None],
    start: str = "AAA",
    end: str = "ZZZ",
) -> int:
    current = start
    for count, move in enumerate(generator, 1):
        current = mapping[current][move]
        if current == end:
            return count
    return 0


def main() -> None:
    content = open("input.txt").read()
    lines = content.splitlines()
    generator = move_generator(lines[0])
    mapping = generate_mapping(lines[2:])
    count = traverse(mapping=mapping, generator=generator)
    print(count)


if __name__ == "__main__":
    main()
