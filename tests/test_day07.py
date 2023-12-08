from advent_of_code_2023.helpers.camel_cards import CamelCardOutcomes, classify_hand, CARD_RANKS_PART02

def test_card_classifier():
    hand_outcomes = {
        "AAAAA": CamelCardOutcomes.FiveOfAKind,
        "AAAAK": CamelCardOutcomes.FourOfAKind,
        "AAAKK": CamelCardOutcomes.FullHouse,
        "AAAKQ": CamelCardOutcomes.ThreeOfAKind,
        "AAKKQ": CamelCardOutcomes.TwoPair,
        "AAKQJ": CamelCardOutcomes.OnePair,
        "AKQJT": CamelCardOutcomes.HighCard,
    }

    for k, v in hand_outcomes.items():
        print(f"Classifying hand {k}, and expecting outcome {v}, {v.value}")
        outcome, strength = classify_hand(k)
        assert outcome == v
        print(f"Card strength is: {strength}")

def test_day07_example():
    hands = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

    print()
    hands_tuples = []
    for line in hands.split("\n"):
        if len(line) > 0:
            hand, score = line.split(" ")
            score = int(score)
            outcome, strength = classify_hand(hand)
            hands_tuples.append((outcome.value, *strength, score))

    hands_tuples.sort(key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5]), reverse=True)

    part1_score = 0
    for ind, hand in enumerate(hands_tuples):
        print(hand)
        part1_score += (ind+1)*hand[-1]

    print(f"Day 07, Part 01 Example: {part1_score}")


    print()
    hands_tuples = []
    for line in hands.split("\n"):
        if len(line) > 0:
            hand, score = line.split(" ")
            score = int(score)
            outcome, strength = classify_hand(hand, strength_lookup = CARD_RANKS_PART02, optimize_j=True)
            hands_tuples.append((outcome.value, *strength, score))

    hands_tuples.sort(key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5]), reverse=True)

    part2_score = 0
    for ind, hand in enumerate(hands_tuples):
        print(hand)
        part2_score += (ind+1)*hand[-1]

    print(f"Day 07, Part 02 Example: {part2_score}")

def test_day07():
    hands = open("inputs/input-07.txt").read()

    print()
    hands_tuples = []
    for line in hands.split("\n"):
        if len(line) > 0:
            hand, score = line.split(" ")
            score = int(score)
            outcome, strength = classify_hand(hand)
            hands_tuples.append((outcome.value, *strength, score))

    hands_tuples.sort(key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5]), reverse=True)

    part1_score = 0
    for ind, hand in enumerate(hands_tuples):
        part1_score += (ind+1)*hand[-1]

    print(f"Day 07, Part 01: {part1_score}")

    print()
    hands_tuples = []
    for line in hands.split("\n"):
        if len(line) > 0:
            hand, score = line.split(" ")
            score = int(score)
            outcome, strength = classify_hand(hand, strength_lookup = CARD_RANKS_PART02, optimize_j=True)
            hands_tuples.append((outcome.value, *strength, score))

    hands_tuples.sort(key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5]), reverse=True)

    part2_score = 0
    for ind, hand in enumerate(hands_tuples):
        print(hand)
        part2_score += (ind+1)*hand[-1]

    print(f"Day 07, Part 02 Example: {part2_score}")