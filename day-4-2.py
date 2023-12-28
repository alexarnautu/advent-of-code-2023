from typing import Generator, Tuple
from collections import defaultdict

INPUT_FILE_NAME = "inputs/day-4.txt"


def __parse_input_file() -> Generator[Tuple[set[int], set[int]], None, None]:
    with open(INPUT_FILE_NAME) as input_file:
        for line in input_file.readlines():
            stripped_line = line.strip()
            line_without_card = stripped_line.split(":")[1]

            winning_numbers, our_numbers = line_without_card.split("|")
            winning_numbers_set = {
                int(stringified_number)
                for stringified_number in winning_numbers.split()
            }
            our_numbers_set = {
                int(stringified_number) for stringified_number in our_numbers.split()
            }

            yield winning_numbers_set, our_numbers_set


def _find_matches_for_card(
    card_number: int, winning_numbers: set[int], our_numbers: set[int]
) -> list[int]:
    matched_numbers = len(winning_numbers & our_numbers)

    return [card_number + index for index in range(1, matched_numbers + 1)]


def main() -> None:
    won_copies: dict[int, int] = defaultdict(lambda: 1)

    for card_number, (winning_numbers, our_numbers) in enumerate(
        __parse_input_file(), 1
    ):
        matches = _find_matches_for_card(card_number, winning_numbers, our_numbers)
        for _ in range(won_copies[card_number]):
            for match in matches:
                won_copies[match] += 1

    print("Result is:", sum(won_copies.values()))


if __name__ == "__main__":
    main()
