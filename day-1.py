from typing import Optional

INPUT_FILE_NAME = "inputs/day-1.txt"

STRING_TO_DIGIT_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def __compute_calibration_value(digits: list[str]) -> int:
    return int(digits[0] + digits[-1])


def __find_digit_word_at_string_start(string: str) -> Optional[str]:
    for string_number in STRING_TO_DIGIT_MAP.keys():
        if string.startswith(string_number):
            return string_number

    return None


def main() -> None:
    result = None

    with open(INPUT_FILE_NAME) as input_file:
        numbers = []

        for line in input_file.readlines():
            stripped_line = line.strip().lower()

            line_index = 0
            digits_in_line = []
            while line_index < len(stripped_line):
                if stripped_line[line_index].isdigit():
                    digits_in_line.append(stripped_line[line_index])
                elif matched_digit_word := __find_digit_word_at_string_start(
                    stripped_line[line_index:]
                ):
                    digits_in_line.append(STRING_TO_DIGIT_MAP[matched_digit_word])

                line_index += 1

            numbers.append(__compute_calibration_value(digits_in_line))

    result = sum(numbers)
    print("Result is:", result)


if __name__ == "__main__":
    main()
