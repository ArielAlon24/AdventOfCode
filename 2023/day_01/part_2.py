from typing import Dict

NUMBERS: Dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def extract_number(string: str) -> int:
    right = 0
    left = 0

    for i in range(len(string)):
        if right and left:
            break

        if not right:
            if string[len(string) - i - 1].isdigit():
                right = int(string[len(string) - i - 1])
            else:
                for key, value in NUMBERS.items():
                    if string[: len(string) - i].endswith(key):
                        right = value

        if not left:
            if string[i].isdigit():
                left = int(string[i])
            else:
                for key, value in NUMBERS.items():
                    if string[i - 1 :].startswith(key):
                        left = value

    return left * 10 + right


def main() -> None:
    with open("day_01/input.txt") as file:
        content = file.read()

    print(sum(extract_number(line) for line in content.splitlines()))


if __name__ == "__main__":
    main()
