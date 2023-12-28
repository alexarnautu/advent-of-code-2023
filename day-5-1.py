from typing import Tuple, cast
from pprint import pprint

INPUT_FILE_NAME = "inputs/day-5.txt"

Rule = tuple[int, int, int]


def __parse_input_file() -> Tuple[list[int], list[list[Rule]]]:
    with open(INPUT_FILE_NAME) as input_file:
        seeds = [
            int(stringified_number)
            for stringified_number in input_file.readline().strip().split()[1:]
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

    return seeds, rules_batches


def __calculate_next_generation(seeds: list[int], rules: list[list[Rule]]) -> list[int]:
    location_numbers = []

    for seed in seeds:
        value = seed
        for index, rule_batch in enumerate(rules, 1):
            print(f"Processing batch of rules #{index}")
            for rule in rule_batch:
                print("Processing rule", rule)
                if value >= rule[1] and value < rule[1] + rule[2]:
                    old_value = value
                    value = value - rule[1] + rule[0]
                    print(
                        "Found matching rule",
                        rule,
                        "new value is",
                        value,
                        "old value was",
                        old_value,
                    )
                    break

        location_numbers.append(value)
    return location_numbers


def main() -> None:
    seeds, rules_batches = __parse_input_file()

    location_numbers = __calculate_next_generation(seeds, rules_batches)

    print("Result is:")
    pprint(min(location_numbers))


if __name__ == "__main__":
    main()
