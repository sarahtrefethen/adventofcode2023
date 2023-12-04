'''
# PART ONE
We need to help our elven friend tally up some scratch card winnings.

## Input 
Each line of the input starts with a card number, and then two lists of
integers separated by a |  character. The first list represents winning 
numbers, and the second list is the numbers on the elf's card.

## Objective
For each card, we need to count the number of integers that appear on 
both lists (winning numbers) and calculate the card's total point value, 
defined as 2^n-1, where n is the number of winning numbers. We return the
sum of the point values of all the cards in the input. 

## Approach
For each card, sort the two lists and compare the entries to count up 
the matches. 
'''
def part1():
    with open('D04input.txt', 'r') as file:
        input = file.read().split('\n')

    def score_card(winning_nums, my_nums):
        # sort in place
        winning_nums.sort()
        my_nums.sort()

        #accumulator to tally wins
        win_count = 0

        # keep track of where we are in each list
        win_idx = 0
        my_idx = 0

        while(my_idx < len(my_nums) and win_idx < len(winning_nums)):
            cur_win = winning_nums[win_idx]
            cur_my = my_nums[my_idx]
            if cur_my == cur_win: 
                win_count += 1
                win_idx += 1
                my_idx += 1
            elif cur_my > cur_win:
                win_idx += 1
            else:
                my_idx += 1

        return pow(2, win_count - 1) if win_count > 0 else 0

    cards = [
        [[int(n) for n in nums_list.strip().split(' ') if n != '']
        for nums_list  in line.split(': ')[1].split('|')] 
        for line in input]

    print(f'part 1: {sum([score_card(a, b) for [a, b] in cards])}')

'''
# PART 2
> There's no such thing as "points". Instead, scratchcards only 
> cause you to win more scratchcards equal to the number of winning 
> numbers you have.
> Specifically, you win copies of the scratchcards below the winning 
> card equal to the number of matches. So, if card 10 were to have 
> 5 matching numbers, you would win one copy each of cards 11, 12, 13, 
> 14, and 15.
> Copies of scratchcards are scored like normal scratchcards and have 
> the same card number as the card they copied. So, if you win a copy 
> of card 10 and it has 5 matching numbers, it would then win a copy 
> of the same cards that the original card 10 won: cards 11, 12, 13, 
> 14, and 15. This process repeats until none of the copies cause you 
> to win any more cards. (Cards will never make you copy a card past 
> the end of the table.)

## objective 
Return the total number of cards. 

## Approach
- calcualte the wins for each card into an array. 
- create a new array to count how many instances there are of each 
  card in the total
- iterate over the first array and update the second array as we go 

'''
def part2():
    with open('D04input.txt', 'r') as file:
        input = file.read().split('\n')

    def count_wins(winning_nums, my_nums):
        # sort in place
        winning_nums.sort()
        my_nums.sort()

        #accumulator to tally wins
        win_count = 0

        # keep track of where we are in each list
        win_idx = 0
        my_idx = 0

        while(my_idx < len(my_nums) and win_idx < len(winning_nums)):
            cur_win = winning_nums[win_idx]
            cur_my = my_nums[my_idx]
            if cur_my == cur_win: 
                win_count += 1
                win_idx += 1
                my_idx += 1
            elif cur_my > cur_win:
                win_idx += 1
            else:
                my_idx += 1

        return win_count

    cards = [
        [[int(n) for n in nums_list.strip().split(' ') if n != '']
        for nums_list  in line.split(': ')[1].split('|')] 
        for line in input]

    win_counts = [count_wins(a, b) for [a, b] in cards]
    num_of_cards = len(win_counts)
    
    # start out with one of each card
    totals = [1 for n in range(num_of_cards)]

    # looking at one card at a time, add however many instances we have of that
    # card to the total for all subsequent cards that will be increased by the 
    # current card. 
    for cur_card_idx in range(num_of_cards):
        addtl_card_count = win_counts[cur_card_idx]
        max_card_to_update = cur_card_idx + addtl_card_count + 1 if cur_card_idx + addtl_card_count + 1 < num_of_cards else num_of_cards
        for card_to_update in range(cur_card_idx + 1, max_card_to_update):
            totals[card_to_update] += totals[cur_card_idx]

    print(f'part 2: {sum(totals)}')

part1()
part2()