deck_of_cards = input().split()

number_of_shuffles = int(input())

for current_shuffle in range(number_of_shuffles):
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck:]
    deck_after_shuffling = []
    for i in range(len(left_part)):
        deck_after_shuffling.append(left_part[i])
        deck_after_shuffling.append(right_part[i])
    deck_of_cards = deck_after_shuffling.copy()

print(deck_after_shuffling)
