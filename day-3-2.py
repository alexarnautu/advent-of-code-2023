from typing import Generator, Tuple
from collections import defaultdict
from functools import reduce


INPUT_FILE_NAME = "inputs/day-3.txt"

ENGINE_SCHEMATIC = list[list[str]]
POSITION_WITH_START = tuple[int, int, int, int]

NAVIGATION_DIRECTIONS = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1),
)


def __find_adjacent_digits_positions(
    engine_schematic: ENGINE_SCHEMATIC,
) -> Generator[POSITION_WITH_START, None, None]:
    for row_index in range(len(engine_schematic)):
        for column_index in range(len(engine_schematic[row_index])):
            if not engine_schematic[row_index][column_index] == "*":
                continue

            for row_direction, column_direction in NAVIGATION_DIRECTIONS:
                if (
                    row_index + row_direction < 0
                    or row_index + row_direction >= len(engine_schematic)
                    or column_index + column_direction < 0
                    or column_index + column_direction
                    >= len(engine_schematic[row_index])
                ):
                    continue

                if engine_schematic[row_index + row_direction][
                    column_index + column_direction
                ].isdigit():
                    yield (
                        row_index,
                        column_index,
                        row_index + row_direction,
                        column_index + column_direction,
                    )


def __build_number_from_starting_position(
    row_index: int, column_index: int, engine_schematic: ENGINE_SCHEMATIC
) -> Tuple[int, int, int]:
    left_index, right_index = column_index, column_index

    while left_index >= 0 and engine_schematic[row_index][left_index - 1].isdigit():
        left_index -= 1

    while (
        right_index < len(engine_schematic[row_index]) - 1
        and engine_schematic[row_index][right_index + 1].isdigit()
    ):
        right_index += 1

    return (
        int("".join(engine_schematic[row_index][left_index : right_index + 1])),
        left_index,
        row_index,
    )


def __build_numbers_from_starting_positions(
    engine_schematic: ENGINE_SCHEMATIC,
) -> dict[tuple[int, int], set[tuple[int, int, int]]]:
    adjacent_digits_positions = __find_adjacent_digits_positions(engine_schematic)

    numbers_grouped_by_starting_position = defaultdict(set)

    for (
        start_row_index,
        start_column_index,
        row_index,
        column_index,
    ) in adjacent_digits_positions:
        number_and_range = __build_number_from_starting_position(
            row_index, column_index, engine_schematic
        )
        numbers_grouped_by_starting_position[(start_row_index, start_column_index)].add(
            number_and_range
        )

    return numbers_grouped_by_starting_position


def __compute_result(numbers: list[int]) -> int:
    return sum(numbers)


def __build_engine_schematic() -> ENGINE_SCHEMATIC:
    engine_schematic = []
    with open(INPUT_FILE_NAME) as input_file:
        for line in input_file.readlines():
            stripped_line = line.strip()
            engine_schematic.append(list(stripped_line))
    return engine_schematic


def main() -> None:
    engine_schematic = __build_engine_schematic()

    numbers_grouped_by_starting_position = __build_numbers_from_starting_positions(
        engine_schematic=engine_schematic
    )
    print("Numbers are:", numbers_grouped_by_starting_position)

    numbers = [
        reduce(lambda acc, curr: acc * curr[0], values, 1)
        for values in numbers_grouped_by_starting_position.values()
        if len(values) == 2
    ]

    result = __compute_result(numbers)

    print("Result is:", result)


if __name__ == "__main__":
    main()
