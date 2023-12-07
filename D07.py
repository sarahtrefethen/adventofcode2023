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
we want to rank the hands in the input file by strength (winning hand = ), and 
then multiply each rank by it's bid. Add those numbers together
to solve the puzzle. 

# Approach
No algorithms here, folks. This is just a grind.

'''

CARDS = '23456789TJQKA'

def beats(a, b):
    return CARDS.find(a) > CARDS.find(b)

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

hands = [(list(cards), int(bid)) for [cards, bid] in input]

scored_hands = []

for (cards, bid) in hands:
    cards.sort(key=lambda card: CARDS.find(card))
    print(cards)
    previous_card = ''
    sequence_length = 1
    type = ''
    type_high_card = ''
    type_second_high_card = ''
    for card in cards:
        # print(f'card is {card} previous card is {previous_card}')
        if card == previous_card:
            # print('MATCH!')
            sequence_length += 1
            if sequence_length == 2:
                # print('found pair')
                if type == '':
                    type = PAIR
                    type_high_card = card
                    type_second_high_card = previous_card
                elif type == PAIR:
                    type = TWO_PAIR
                    if beats(card, type_high_card):
                        type_second_high_card = type_high_card
                        type_high_card = card
                elif type == THREE:
                    type = FULL_HOUSE
                    if beats(card, type_high_card):
                        type_second_high_card = type_high_card
                        type_high_card = card
            elif sequence_length == 3:
                # print('found three')
                if type == PAIR:
                    if type_high_card == card:
                        type = THREE
                        type_second_high_card = cards[1]
                elif type == TWO_PAIR:
                    type = FULL_HOUSE
                    if beats(card, type_high_card):
                        type_second_high_card = type_high_card
                        type_high_card = card
            elif sequence_length == 4:
                if type_high_card == card:
                    type = FOUR
                type_second_high_card = cards[0]

            elif sequence_length == 5:
                type = FIVE
        else:
            sequence_length = 1
            if(type != TWO_PAIR and type != FULL_HOUSE):
                if beats(card, type_second_high_card):
                    type_second_high_card = card    
        previous_card = card

    if type == '':
        type = HIGH_CARD
        type_high_card = cards[4]
        type_second_high_card = cards[3]

    print(f'type is: {type} high card is {type_high_card} second high card is {type_second_high_card}')

    score = ranked_types.index(type)*10000 + CARDS.find(type_high_card)*100
    if(type_second_high_card != ''):
        score += CARDS.find(type_second_high_card)

    scored_hands.append((score, bid, cards))

scored_hands.sort(key=lambda data: data[0])

for hand in scored_hands:
    print(hand)

print(sum([(i+1)*scored_hands[i][1] for i in range(len(scored_hands))]))
