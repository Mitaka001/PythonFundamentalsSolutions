cards = input().split()
count_of_shuffles = int(input())

for shuffle in range(count_of_shuffles):
    final_deck = []

    half_deck = len(cards) // 2
    first_half = cards[0:half_deck]
    second_half = cards[half_deck:]

    for card_index in range(len(first_half)):
        final_deck.append(first_half[card_index])
        final_deck.append(second_half[card_index])
    cards = final_deck
print(final_deck)
