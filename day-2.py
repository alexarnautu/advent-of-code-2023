from collections import defaultdict
from functools import reduce

INPUT_FILE_NAME = "inputs/day-2.txt"

LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def main() -> None:
    with open(INPUT_FILE_NAME) as input_file:
        valid_game_ids = []
        sum_of_game_powers = 0
        for game_id, line in enumerate(input_file.readlines(), start=1):
            stripped_line = line.strip()

            extractions = stripped_line.split(":")[1].split(";")

            maximum_balls_per_color: dict[str, int] = defaultdict(lambda: 0)

            for extraction in extractions:
                numbers_and_colors = extraction.split(",")
                for number_and_color in numbers_and_colors:
                    number, color = number_and_color.strip().split(" ")
                    maximum_balls_per_color[color] = max(
                        maximum_balls_per_color[color], int(number)
                    )

            invalid = False
            game_power = reduce(
                lambda curr, result: curr * result, maximum_balls_per_color.values()
            )
            sum_of_game_powers += game_power

            for color, maximum_balls in maximum_balls_per_color.items():
                if maximum_balls > LIMITS[color]:
                    invalid = True
                    break

            if not invalid:
                valid_game_ids.append(game_id)

    print("Sum of game IDs:", sum(valid_game_ids))
    print("Sum of game powers:", sum_of_game_powers)


if __name__ == "__main__":
    main()
