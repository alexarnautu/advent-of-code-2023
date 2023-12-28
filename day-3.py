from typing import Generator, Tuple


INPUT_FILE_NAME = "inputs/day-3.txt"

ENGINE_SCHEMATIC = list[list[str]]
POSITION = tuple[int, int]

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


def __is_symbol(symbol: str) -> bool:
    return not (symbol.isalnum() or symbol == ".")


def __find_adjacent_digits_positions(
    engine_schematic: ENGINE_SCHEMATIC,
) -> Generator[POSITION, None, None]:
    for row_index in range(len(engine_schematic)):
        for column_index in range(len(engine_schematic[row_index])):
            if not __is_symbol(engine_schematic[row_index][column_index]):
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
                    yield (row_index + row_direction, column_index + column_direction)


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
) -> Generator[Tuple[int, int, int], None, None]:
    adjacent_digits_positions = __find_adjacent_digits_positions(engine_schematic)

    for row_index, column_index in adjacent_digits_positions:
        yield __build_number_from_starting_position(
            row_index, column_index, engine_schematic
        )


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

    numbers_and_ranges = set(
        __build_numbers_from_starting_positions(engine_schematic=engine_schematic)
    )
    numbers = [number[0] for number in numbers_and_ranges]
    print("Numbers are:", numbers)

    result = __compute_result(numbers)

    print("Result is:", result)


if __name__ == "__main__":
    main()
