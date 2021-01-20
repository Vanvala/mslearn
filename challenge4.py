import random

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = []

for suit in suits:
    for rank in ranks:
        deck.append(f'{rank} of {suit} ')

print(f'There are {len(deck)} cards in the deck.')

player = random.choices(deck, k = 5)

for i in player:
    deck.remove(i)


print(f'Dealing ... \nThere are {len(deck)} cards in the deck.\nPlayer has the following cards in their hand: \n{player}')