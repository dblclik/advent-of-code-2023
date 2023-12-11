def card_parser(card_string: str):
    card_string = card_string.replace("  ", " ")
    card_string = card_string.split(": ")[-1]
    card_string = card_string.replace(" | ", "|")
    card_string = card_string.replace(" ", ",")
    winning_numbers, scratches = card_string.split("|")
    winning_numbers = winning_numbers.split(",")
    scratches = scratches.split(",")

    return winning_numbers, scratches


def compare_numbers(winning_numbers, scratches):
    return len([s for s in scratches if s in winning_numbers])
