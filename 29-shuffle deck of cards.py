#shuffle deck of cards
import random

# Create a deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [rank + " of " + suit for suit in suits for rank in ranks]

# Shuffle the deck
random.shuffle(deck)

# Print the shuffled deck
for card in deck:
    print(card)
    