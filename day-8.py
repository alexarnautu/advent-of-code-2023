INPUT_FILE_NAME = "inputs/day-8.txt"


def __parse_input_file() -> tuple[str, str, list[str], dict[str, tuple[str, str]]]:
    with open(INPUT_FILE_NAME) as input_file:
        network = {}
        initial_route = None

        initial_route = list(input_file.readline().strip())
        starting_point = ""
        destination_point = ""

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

            destination_point = source
            if not starting_point:
                starting_point = source

            network[source] = (destination_left, destination_right)

    return starting_point, destination_point, initial_route, network


def __find_steps_to_destination(
    network: dict[str, tuple[str, str]],
    initial_route: list[str],
    starting_point: str,
    destination_point: str,
) -> int:
    steps = 0

    copy_of_intial_route = initial_route.copy()
    starting_point = "AAA"
    destination_point = "ZZZ"

    while starting_point != destination_point:
        print(
            "Step",
            steps,
            "Starting point",
            starting_point,
            "Destination point",
            destination_point,
        )
        if not len(initial_route):
            initial_route.extend(copy_of_intial_route)

        next_step = initial_route.pop(0)

        steps += 1

        if next_step == "R":
            starting_point = network[starting_point][1]
        else:
            starting_point = network[starting_point][0]

    return steps


def main() -> None:
    starting_point, destination_point, initial_route, network = __parse_input_file()

    result = __find_steps_to_destination(
        network, initial_route, starting_point, destination_point
    )

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
