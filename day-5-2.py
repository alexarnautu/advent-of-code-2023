from typing import Tuple, Optional, cast

from pprint import pprint

INPUT_FILE_NAME = "inputs/day-5.txt"

Rule = tuple[int, int, int]


def __extract_overlapping_and_non_overlapping_intervals(
    first: Tuple[int, int], second: Tuple[int, int]
) -> Tuple[Optional[Tuple[int, int]], list[Tuple[int, int]]]:
    print("Extracting overlapping and non-overlapping intervals", first, second)
    # First interval starts before the second interval
    if first[0] < second[0]:
        # Interval ends before the second interval ends
        if first[1] >= second[0] and first[1] <= second[1]:
            return (second[0], first[1]), [(first[0], second[0] - 1)]
        # Interval ends after the second interval ends
        if first[1] >= second[1]:
            return second, [(first[0], second[0] - 1), (second[1] + 1, first[1])]

    # First interval starts in the second interval
    if first[0] >= second[0] and first[0] <= second[1]:
        # Interval ends after the second interval ends
        if first[1] >= second[1]:
            return (first[0], second[1]), [(second[1] + 1, first[1])]
        # Interval ends before the second interval ends
        if first[1] <= second[1]:
            return first, []

    return None, [first]


def __parse_input_file() -> Tuple[list[tuple[int, int]], list[list[Rule]]]:
    with open(INPUT_FILE_NAME) as input_file:
        seeds = [
            int(stringified_number)
            for stringified_number in input_file.readline().strip().split()[1:]
        ]
        seed_intervals = [
            (seeds[index], seeds[index] + seeds[index + 1] - 1)
            for index in range(0, len(seeds), 2)
        ]

        rules_batches = []
        rules: list[Rule] = []
        for line in input_file.readlines():
            if line[0].isalpha():
                if rules:
                    rules_batches.append(rules)
                rules = []
                continue

            if line[0].isdigit():
                rules.append(
                    cast(
                        Rule,
                        (
                            int(stringified_number)
                            for stringified_number in line.strip().split()
                        ),
                    )
                )
                continue

        rules_batches.append(rules)

    return seed_intervals, rules_batches


def __calculate_next_generation(
    seed_intervals: list[tuple[int, int]], rules: list[list[Rule]]
) -> list[int]:
    new_seed_intervals = seed_intervals
    current_seed_intervals = seed_intervals

    for index, rule_batch in enumerate(rules, 1):
        print(f"Processing batch of rules #{index}")
        current_seed_intervals = new_seed_intervals
        new_seed_intervals = []

        while current_seed_intervals:
            seed_interval = current_seed_intervals.pop(0)

            print("Processing seed interval", seed_interval)
            matched_rule = False
            for rule in rule_batch:
                print("Processing rule", rule)

                rule_interval = (rule[1], rule[1] + rule[2] - 1)
                (
                    overlapping_interval,
                    non_overlapping_intervals,
                ) = __extract_overlapping_and_non_overlapping_intervals(
                    seed_interval, rule_interval
                )

                if overlapping_interval:
                    print(
                        "Overlapping interval",
                        overlapping_interval,
                        "Non-overlapping intervals",
                        non_overlapping_intervals,
                    )
                    matched_rule = True

                    overlapping_interval = (
                        overlapping_interval[0] - rule[1] + rule[0],
                        overlapping_interval[1] - rule[1] + rule[0],
                    )

                    new_seed_intervals.append(overlapping_interval)
                    if non_overlapping_intervals:
                        current_seed_intervals.extend(non_overlapping_intervals)
                    break

            if not matched_rule:
                print("Appending non-matched seed interval", seed_interval)
                new_seed_intervals.append(seed_interval)

    return [
        tuple_element for interval in new_seed_intervals for tuple_element in interval
    ]


def main() -> None:
    seeds_intervals, rules_batches = __parse_input_file()

    location_numbers = __calculate_next_generation(seeds_intervals, rules_batches)

    print("Result is:")
    pprint(min(location_numbers))


if __name__ == "__main__":
    main()
