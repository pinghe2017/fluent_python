from cards import *
from random import choice
beer_card = Card('7', 'diamonds')
print(beer_card)
deck = FrenchDeck()
print(len(deck))

print(choice(deck))