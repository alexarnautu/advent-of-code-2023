from typing import Tuple
from functools import reduce


INPUT_FILE_NAME = "inputs/day-6.txt"


def __parse_input_file() -> Tuple[list[int], list[int]]:
    with open(INPUT_FILE_NAME) as input_file:
        time = int(input_file.readline().strip().split(":")[1].replace(" ", ""))
        distance = int(input_file.readline().strip().split(":")[1].replace(" ", ""))

    return [time], [distance]


def __calculate_options_per_race(times: list[int], distances: list[int]) -> list[int]:
    options_count = []
    for race_number in range(len(times)):
        race_options_count = 0
        for wait_time in range(1, times[race_number]):
            if (times[race_number] - wait_time) * wait_time > distances[race_number]:
                race_options_count += 1

        options_count.append(race_options_count)

    return options_count


def main() -> None:
    times, distances = __parse_input_file()

    race_options = __calculate_options_per_race(times, distances)

    print("Result is:")
    print(reduce(lambda curr, acc: curr * acc, race_options))


if __name__ == "__main__":
    main()
