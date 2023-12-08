from enum import Enum

class CamelCardOutcomes(Enum):
    FiveOfAKind = 0
    FourOfAKind = 1
    FullHouse = 2
    ThreeOfAKind = 3
    TwoPair = 4
    OnePair = 5
    HighCard = 6

CARD_RANKS_PART01 = {card: i for i, card in enumerate(["A","K","Q","J","T","9","8","7","6","5","4","3","2"])}
CARD_RANKS_PART02 = {card: i for i, card in enumerate(["A","K","Q","T","9","8","7","6","5","4","3","2","J"])}

def classify_hand(hand: str, strength_lookup: dict = CARD_RANKS_PART01, optimize_j: bool = False):
    # reject if length NE to 5
    assert len(hand) == 5

    card_counts = {}
    card_strength = []
    for card in hand:
        card_counts[card] = card_counts.get(card, 0) + 1
        card_strength.append(strength_lookup[card])

    if optimize_j:
        # do optimization here
        optimization_points = card_counts.get("J", 0)
        # If we have 5 Jokers then we have a 5 of a kind w/o having to optimize
        if optimization_points > 0 and optimization_points < 5:
            # can we just assign the points to the highest other card count?
            max_card = [(k, v) for k,v in card_counts.items() if k != "J"]
            # sort by count of cards
            max_card.sort(key=lambda x: x[1], reverse=True)

            card_counts[max_card[0][0]] += optimization_points
            # get rid of the Jokers now that we've reallocated them
            del card_counts["J"]

    # classify hand based on card counts
    if len(card_counts) == 1:
        return CamelCardOutcomes.FiveOfAKind, card_strength
    
    if len(card_counts) == 2:
        # check for 4 of a kind
        if len([k for k,v in card_counts.items() if v==4]) > 0:
            return CamelCardOutcomes.FourOfAKind, card_strength
        return CamelCardOutcomes.FullHouse, card_strength
    
    if len(card_counts) == 3:
        # check for three of a kind (which means XXXYZ hand else FH)
        if len([k for k,v in card_counts.items() if v==3]) > 0:
            return CamelCardOutcomes.ThreeOfAKind, card_strength
        return CamelCardOutcomes.TwoPair, card_strength
    
    if len(card_counts) == 4:
        return CamelCardOutcomes.OnePair, card_strength
    
    return CamelCardOutcomes.HighCard, card_strength


    
