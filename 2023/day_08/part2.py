from typing import Generator, Dict, List, Tuple
import math


def main() -> None:
    content = open("input.txt").read()
    lines = content.splitlines()

    generator = move_generator(lines[0])
    mapping = generate_mapping(lines[2:])
    starters = filter_starters(mapping)

    shortest_paths = find_shortest_paths(
        starters=starters, mapping=mapping, move_generator=generator
    )

    print(math.lcm(*shortest_paths))


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


def filter_starters(mapping: Dict[str, Tuple[str, str]]) -> List[str]:
    starters = []
    for key in mapping.keys():
        if key.endswith("A"):
            starters.append(key)
    return starters


def find_shortest_paths(
    starters: List[str],
    mapping: Dict[str, Tuple[str, str]],
    move_generator: Generator[int, None, None],
) -> List[int]:
    currents = starters
    least_moves = [0 for _ in range(len(currents))]
    for count, move in enumerate(move_generator, 1):
        news = []
        for index, current in enumerate(currents):
            new = mapping[current][move]
            if new.endswith("Z") and least_moves[index] == 0:
                least_moves[index] = count
            news.append(new)
        currents = news

        if not 0 in least_moves:
            break

    return least_moves


if __name__ == "__main__":
    main()
