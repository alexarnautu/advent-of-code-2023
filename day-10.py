from enum import Enum
from typing import Optional
from collections import namedtuple

INPUT_FILE_NAME = "inputs/day-10.txt"


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


directions_for_type: dict[str, list[Direction]] = {
    "|": [Direction.UP, Direction.DOWN],
    "-": [Direction.LEFT, Direction.RIGHT],
    "L": [Direction.UP, Direction.RIGHT],
    "J": [Direction.UP, Direction.LEFT],
    "7": [Direction.DOWN, Direction.LEFT],
    "F": [Direction.DOWN, Direction.RIGHT],
    ".": [],
    "S": [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT],
}


def __parse_input_file() -> list[str]:
    pipes_map = []
    with open(INPUT_FILE_NAME) as input_file:
        for line in input_file:
            pipes_map.append(line.strip())

    return pipes_map


Coordinates = namedtuple("Coordinates", ["x", "y"])


def __find_start_position(pipes_map: list[str]) -> Optional[Coordinates]:
    for row_index, line in enumerate(pipes_map):
        try:
            return Coordinates(row_index, line.index("S"))
        except ValueError:
            continue

    return None


def __fill_distances_in_map(
    pipes_map: list[str], start_position: Coordinates
) -> list[list[Optional[int]]]:
    distance_map: list[list[Optional[int]]] = []
    for line in pipes_map:
        distance_map.append([None] * len(line))

    to_visit_queue = [start_position]
    distance_map[start_position.x][start_position.y] = 0
    while len(to_visit_queue) > 0:
        visiting = to_visit_queue.pop(0)

        for direction in directions_for_type[pipes_map[visiting.x][visiting.y]]:
            if (
                direction == Direction.UP
                and visiting.x > 0
                and Direction.DOWN
                in directions_for_type[pipes_map[visiting.x - 1][visiting.y]]
                and distance_map[visiting.x - 1][visiting.y] is None
            ):
                distance_map[visiting.x - 1][visiting.y] = (
                    distance_map[visiting.x][visiting.y] + 1
                )
                to_visit_queue.append(Coordinates(visiting.x - 1, visiting.y))
            elif (
                direction == Direction.DOWN
                and visiting.x < len(pipes_map) - 1
                and Direction.UP
                in directions_for_type[pipes_map[visiting.x + 1][visiting.y]]
                and distance_map[visiting.x + 1][visiting.y] is None
            ):
                distance_map[visiting.x + 1][visiting.y] = (
                    distance_map[visiting.x][visiting.y] + 1
                )
                to_visit_queue.append(Coordinates(visiting.x + 1, visiting.y))
            elif (
                direction == Direction.LEFT
                and visiting.y > 0
                and Direction.RIGHT
                in directions_for_type[pipes_map[visiting.x][visiting.y - 1]]
                and distance_map[visiting.x][visiting.y - 1] is None
            ):
                distance_map[visiting.x][visiting.y - 1] = (
                    distance_map[visiting.x][visiting.y] + 1
                )
                to_visit_queue.append(Coordinates(visiting.x, visiting.y - 1))
            elif (
                direction == Direction.RIGHT
                and visiting.y < len(pipes_map[0]) - 1
                and Direction.LEFT
                in directions_for_type[pipes_map[visiting.x][visiting.y + 1]]
                and distance_map[visiting.x][visiting.y + 1] is None
            ):
                distance_map[visiting.x][visiting.y + 1] = (
                    distance_map[visiting.x][visiting.y] + 1
                )
                to_visit_queue.append(Coordinates(visiting.x, visiting.y + 1))

    return distance_map


def main() -> None:
    pipes_map = __parse_input_file()

    start_position = __find_start_position(pipes_map)

    if not start_position:
        return

    distance_map = __fill_distances_in_map(pipes_map, start_position)

    maximum_distance = 0
    for line in distance_map:
        for distance in line:
            if distance is not None and distance > maximum_distance:
                maximum_distance = distance

    print("Result", maximum_distance)


if __name__ == "__main__":
    main()
