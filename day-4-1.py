from typing import Generator, Tuple


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


def __count_matches_per_card(winning_numbers: set[int], our_numbers: set[int]) -> int:
    return len(winning_numbers & our_numbers)


def __compute_scores_based_on_matches_count(matches: int) -> int:
    if matches == 0:
        return 0
    return int(2 ** (matches - 1))


def main() -> None:
    scores = [
        __compute_scores_based_on_matches_count(
            __count_matches_per_card(winning_numbers, our_numbers)
        )
        for winning_numbers, our_numbers in __parse_input_file()
    ]

    print("Result is:", sum(scores))


if __name__ == "__main__":
    main()
