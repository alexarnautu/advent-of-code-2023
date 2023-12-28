import graphviz  # type: ignore

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


def main() -> None:
    initial_route, network = __parse_input_file()

    graph = graphviz.Digraph(comment="Network", engine="neato")

    print("Building graph...")
    for key, value in network.items():
        custom_attributes = {"style": "filled"}
        if key.endswith("Z"):
            custom_attributes["color"] = "green"
        elif key.endswith("A"):
            custom_attributes["color"] = "red"
        graph.node(key, **custom_attributes)
        graph.edge(key, value[0])
        graph.edge(key, value[1])

    print("Rendering graph...")

    graph.render("network.gv", view=True)


if __name__ == "__main__":
    main()
