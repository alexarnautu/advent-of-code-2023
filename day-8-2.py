from math import lcm

INPUT_FILE_NAME = "inputs/day-8.txt"


def __parse_input_file() -> tuple[list[str], dict[str, tuple[str, str]]]:
    with open(INPUT_FILE_NAME) as input_file:
        network = {}
        initial_route = None

        initial_route = list(input_file.readline().strip())

        for line in input_file.readlines():
            if line == "\n":
                continue
            clean_line = (
                line.strip()
                .replace("=", "")
                .replace("(", "")
                .replace(")", "")
                .replace(",", "")
                .replace("  ", " ")
            )
            source, destination_left, destination_right = clean_line.split(" ")

            network[source] = (destination_left, destination_right)

    return initial_route, network


def __find_steps_to_destinations(
    network: dict[str, tuple[str, str]], initial_route: list[str]
) -> int:
    copy_of_intial_route = initial_route.copy()

    starting_points = [point for point in network.keys() if point.endswith("A")]
    starting_points_steps = [0] * len(starting_points)

    print("Starting points: ", starting_points)

    for index, starting_point in enumerate(starting_points):
        actual_position = starting_point
        route = copy_of_intial_route.copy()
        steps = 0

        while not actual_position.endswith("Z"):
            if not len(route):
                route.extend(copy_of_intial_route)

            next_step = route.pop(0)

            steps += 1

            if next_step == "R":
                actual_position = network[actual_position][1]
            else:
                actual_position = network[actual_position][0]

        starting_points_steps[index] = steps

    return lcm(*starting_points_steps)


def main() -> None:
    initial_route, network = __parse_input_file()

    result = __find_steps_to_destinations(network, initial_route)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
