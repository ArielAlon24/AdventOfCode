from typing import List
from range_mapping import RangeMapping


def section_to_mapping(section: str) -> RangeMapping:
    range_mapping = RangeMapping()
    for line in section.splitlines()[1:]:
        range_mapping.add(*(int(num) for num in line.split(" ")))

    return range_mapping


def traverse_almanac(content: str) -> List[int]:
    sections = content.split("\n\n")

    seeds = [int(num) for num in sections[0].split(": ")[-1].split()]
    mappings = [section_to_mapping(section) for section in sections[1:]]

    locations = []
    for seed in seeds:
        location = seed
        for mapping in mappings:
            location = mapping[location]
        locations.append(location)

    return locations


def main() -> None:
    content = open("input.txt").read()

    print(min(traverse_almanac(content)))


if __name__ == "__main__":
    main()
