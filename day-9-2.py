INPUT_FILE_NAME = "inputs/day-9.txt"


def __parse_input_file() -> list[list[int]]:
    histories = []
    with open(INPUT_FILE_NAME) as input_file:
        for line in input_file.readlines():
            histories.append([int(value) for value in line.strip().split(" ")])

    return histories


def __build_sequences_for_history(history: list[int]) -> list[list[int]]:
    # Add history a starting sequence
    sequences = [history]
    while any(sequences[-1]):
        new_sequence = []
        for index in range(len(sequences[-1]) - 1):
            new_sequence.append(sequences[-1][index + 1] - sequences[-1][index])

        sequences.append(new_sequence)

    return sequences


def __predict_next_number(history: list[int]) -> int:
    sequences = __build_sequences_for_history(history)
    sequences[-1].append(0)

    for sequence_index in range(len(sequences) - 1, 0, -1):
        sequences[sequence_index - 1].insert(
            0, sequences[sequence_index - 1][0] - sequences[sequence_index][0]
        )

    print("Predicted number", sequences[0][0], "for sequneces", sequences)
    return sequences[0][0]


def main() -> None:
    histories = __parse_input_file()

    print(__build_sequences_for_history(histories[0]))

    result = sum(__predict_next_number(history) for history in histories)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
