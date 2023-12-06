from typing import List, Tuple


def section_to_ranges(section: str) -> List[Tuple[int, int, int]]:
    ranges = []
    for line in section.splitlines()[1:]:
        ranges.append(tuple(map(int, line.split())))
    return ranges


def seed_generator(inputs: List[int]) -> List[Tuple[int, int]]:
    seeds = []
    for i in range(0, len(inputs), 2):
        seeds.append((inputs[i], inputs[i] + inputs[i + 1]))
    return seeds


def process_seeds(
    seeds: List[Tuple[int, int]], ranges: List[Tuple[int, int, int]]
) -> List[Tuple[int, int]]:
    new_seeds = []
    while seeds:
        start, end = seeds.pop()
        for a, b, c in ranges:
            os = max(start, b)
            oe = min(end, b + c)
            if os < oe:
                new_seeds.append((os - b + a, oe - b + a))
                if os > start:
                    seeds.append((start, os))
                if end > oe:
                    seeds.append((oe, end))
                break
        else:
            new_seeds.append((start, end))
    return new_seeds


def main() -> None:
    with open("input.txt") as file:
        inputs, *blocks = file.read().split("\n\n")

    inputs = list(map(int, inputs.split(": ")[-1].split()))
    seeds = seed_generator(inputs)

    for block in blocks:
        ranges = section_to_ranges(block)
        seeds = process_seeds(seeds, ranges)

    print(min(seeds)[0])


if __name__ == "__main__":
    main()
