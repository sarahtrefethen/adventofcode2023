'''
# PART ONE 

we are playing poker

# Input 
The first string in each line is a five-card poker hand, the
second string is a bid. 

for example: 
    32T3K 765
    T55J5 684
    KK677 28
    KTJJT 220
    QQQJA 483

Cards are, in descending order or strength: A K Q J T 9 8 7 6 5 4 3 2
Possible hands are, ordered by strength:
    five of a kind
    four of a kind 
    full house (three of a kind + a pair)
    three of a kind 
    two pair
    one pair 
    high card

# Puzzle description 
we want to rank the hands in the input file by strength (winning hand = highest number), and 
then multiply each rank by it's bid. Add those numbers together
to solve the puzzle. 

# Approach
- Sort the cards in each hand to categorize them. 
- score the hands for sorting by mutliplying the criteria by powers of 10.
- sort the hands.
- calculate the final score of each hand
'''


FIVE = 'five'
FOUR = 'four'
FULL_HOUSE = 'full_house'
THREE = 'three'
TWO_PAIR = 'two_pair'
PAIR = 'pair'
HIGH_CARD = 'high_card'

ranked_types = [FIVE, FOUR, FULL_HOUSE, THREE, TWO_PAIR, PAIR, HIGH_CARD]
ranked_types.reverse()

with open('D07.txt', 'r') as file:
    input = [line.split(' ') for line in file.read().splitlines()]

hands = [(list(cards), int(bid), cards) for [cards, bid] in input]

def part1():
    CARDS = '23456789TJQKA'

    scored_hands = []

    for (cards, bid, og_cards) in hands:
        cards.sort(key=lambda card: CARDS.find(card))
        previous_card = ''
        sequence_length = 1
        type = ''
        for card in cards:
            if card == previous_card:
                sequence_length += 1
                if sequence_length == 2:
                    if type == '':
                        type = PAIR
                    elif type == PAIR:
                        type = TWO_PAIR
                    elif type == THREE:
                        type = FULL_HOUSE
                elif sequence_length == 3:
                    if type == PAIR:
                            type = THREE
                    elif type == TWO_PAIR:
                        type = FULL_HOUSE
                elif sequence_length == 4:
                    type = FOUR
                elif sequence_length == 5:
                    type = FIVE
            else:
                sequence_length = 1
            previous_card = card

        if type == '':
            type = HIGH_CARD
        
        score = ranked_types.index(type)*100000000000 + CARDS.find(og_cards[0])*100000000 + CARDS.find(og_cards[1])*1000000 + CARDS.find(og_cards[2])*10000 + CARDS.find(og_cards[3])*100 + CARDS.find(og_cards[4])

        scored_hands.append((score, bid, og_cards))

    scored_hands.sort(key=lambda data: data[0])

    print(sum([(i+1)*scored_hands[i][1] for i in range(len(scored_hands))]))

''''
# PART 2

Js are now wild cards that have the lowest point value in ranking 

## Approach
same as before, but count the Js and change the hand type based on how many 
wild cards are available. Not very elegant but it works.

'''


def part2():
    CARDS = 'J23456789TQKA'

    scored_hands = []

    for (cards, bid, og_cards) in hands:
        cards.sort(key=lambda card: CARDS.find(card))
        previous_card = ''
        sequence_length = 1
        type = ''
        joker_count = 0
        for card in cards:
            if card == 'J':
                joker_count += 1
            elif card == previous_card:
                sequence_length += 1
                if sequence_length == 2:
                    if type == '':
                        type = PAIR
                    elif type == PAIR:
                        type = TWO_PAIR
                    elif type == THREE:
                        type = FULL_HOUSE
                elif sequence_length == 3:
                    if type == PAIR:
                            type = THREE
                    elif type == TWO_PAIR:
                        type = FULL_HOUSE
                elif sequence_length == 4:
                    type = FOUR
                elif sequence_length == 5:
                    type = FIVE
            else:
                sequence_length = 1
            previous_card = card

        if type == '':
            type = HIGH_CARD

        if joker_count > 3:
            type = FIVE
        if joker_count == 3:
            if type == PAIR:
                type = FIVE
            else:
                type = FOUR
        if joker_count == 2:
            if type == THREE:
                type = FIVE
            elif type == PAIR:
                type = FOUR
            else:
                type = THREE
        if joker_count == 1:
            if type == FOUR:
                type = FIVE
            elif type == THREE:
                type = FOUR
            elif type == PAIR:
                type = THREE
            elif type == TWO_PAIR:
                type = FULL_HOUSE
            else:
                type = PAIR

        
        score = ranked_types.index(type)*100000000000 + CARDS.find(og_cards[0])*100000000 + CARDS.find(og_cards[1])*1000000 + CARDS.find(og_cards[2])*10000 + CARDS.find(og_cards[3])*100 + CARDS.find(og_cards[4])

        scored_hands.append((score, bid, og_cards, type))

    scored_hands.sort(key=lambda data: data[0])

    print(sum([(i+1)*scored_hands[i][1] for i in range(len(scored_hands))]))

part1()
part2()