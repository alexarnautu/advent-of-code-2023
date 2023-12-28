from dataclasses import dataclass
from collections import defaultdict
from functools import cmp_to_key


INPUT_FILE_NAME = "inputs/day-7.txt"

COUNTS_PER_RANK = {
    (5,): 7,
    (4, 1): 6,
    (3, 2): 5,
    (3, 1, 1): 4,
    (2, 2, 1): 3,
    (2, 1, 1, 1): 2,
    (1, 1, 1, 1, 1): 1,
}

CARDS_ORDER = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


@dataclass
class HandWithScore:
    hand: str
    score: int
    rank: int = -1


def __parse_input_file() -> list[HandWithScore]:
    with open(INPUT_FILE_NAME) as input_file:
        hands_and_scores = []
        for line in input_file.readlines():
            hand, stringified_score = line.strip().split(" ")

            hands_and_scores.append(HandWithScore(hand, int(stringified_score)))

    return hands_and_scores


def __compute_ranks(hands_and_scores: list[HandWithScore]) -> list[HandWithScore]:
    for hand in hands_and_scores:
        cards: dict[str, int] = defaultdict(lambda: 0)
        for card in hand.hand:
            cards[card] += 1

        # Only one key means all the elements are the same
        hand_card_counts = tuple(sorted(cards.values(), reverse=True))
        hand.rank = COUNTS_PER_RANK[hand_card_counts]

    return hands_and_scores


def sort_key(a: HandWithScore, b: HandWithScore) -> int:
    if a.rank != b.rank:
        return a.rank - b.rank

    for card_a, card_b in zip(a.hand, b.hand):
        if card_a != card_b:
            return CARDS_ORDER.index(card_b) - CARDS_ORDER.index(card_a)
    return 0


def main() -> None:
    hands_and_scores = __parse_input_file()

    __compute_ranks(hands_and_scores)

    hands_and_scores.sort(key=cmp_to_key(sort_key))

    result = sum([hand.score * index for index, hand in enumerate(hands_and_scores, 1)])
    print("Result is:", result)


if __name__ == "__main__":
    main()
