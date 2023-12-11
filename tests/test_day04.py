from advent_of_code_2023.helpers.game_cards import card_parser, compare_numbers


def test_day04_example():
    test_cards = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

    for ind, game in enumerate(test_cards.split("\n")):
        score = compare_numbers(*card_parser(game))
        print(f"Card {ind+1} is worth {score} points")

    cards = test_cards.split("\n")
    card_value = [0] * len(cards)
    card_copies = [0] * len(cards)
    for ind, game in enumerate(cards):
        if len(game) > 0:
            card_copies[ind] += 1
            next_cards = compare_numbers(*card_parser(game))
            card_value[ind] += 2 ** (next_cards - 1) if next_cards > 0 else 0
            for i in range(next_cards):
                card_copies[ind + i + 1] += card_copies[ind]

    print(card_copies)

    part2_score = sum(card_copies)
    print(f"Example for Part 2: {part2_score}")


def test_day04():
    cards = open("inputs/input-04.txt").read().split("\n")[:-1]

    # Part 1
    total_score = 0
    for game in cards:
        if len(game) > 0:
            won = compare_numbers(*card_parser(game))
            total_score += 2 ** (won - 1) if won > 0 else 0

    print()
    print(f"Day 04, Part 01: {total_score}")

    # Part 2
    card_value = [0] * len(cards)
    card_copies = [0] * len(cards)
    for ind, game in enumerate(cards):
        if len(game) > 0:
            card_copies[ind] += 1
            next_cards = compare_numbers(*card_parser(game))
            card_value[ind] += 2 ** (next_cards - 1) if next_cards > 0 else 0
            for i in range(next_cards):
                card_copies[ind + i + 1] += card_copies[ind]

    part2_score = sum(card_copies)
    print(f"Day 04, Part 02: {part2_score}")
