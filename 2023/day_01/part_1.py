def extract_number(string: str) -> int:
    left = 0
    right = len(string) - 1

    for _ in range(len(string)):
        if string[left].isdigit() and string[right].isdigit():
            break

        if not string[left].isdigit():
            left += 1
        if not string[right].isdigit():
            right -= 1

    return 10 * int(string[left]) + int(string[right])


def main() -> None:
    with open("day_01/input.txt") as file:
        content = file.read()

    print(sum(extract_number(line) for line in content.splitlines()))


if __name__ == "__main__":
    main()
