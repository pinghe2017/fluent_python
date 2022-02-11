import collections
#  here very import concept is namedtuple
# namedtuple is a class but like dictionary, it contains key and value and can be accesed by it its index
# my understanding: Class = collections.namedtuple('Class',['key1','key2','key3',...])
# 1. then i can assign value to such keys
# 2. instance = Class('value1','value2','value3'....)
# 3. instance[0] == value1 ....
# 4. instance.key1 == value1
# 5. getattr(instance,'key1'} = value1
Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck():
  ranks = [str(n) for n in range(2, 11)] + list('JQKA')
  suits = 'spades diamonds clubs hearts'.split()
  def __init__(self):
    # ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # suits = 'spades diamonds clubs hearts'.split()
    
    
    self._cards = [Card(rank, suit) for suit in self.suits
                                   for rank in self.ranks]
  def __len__(self):
    return len(self._cards)
  def __getitem__(self, position):
    return self._cards[position] 
suit_value = dict(spades = 3, hearts=2, diamands=1, clubs=0)

def spades_high(card):
  #fd = FrenchDeck()
  # here we use class FrenchDeck and its attribute
  # it is defined befor init and without self 
  # class atributes are shared by instances and added with self
  rank_value = FrenchDeck.ranks.index(card.rank)
  return rank_value*len(suit_value) +suit_value[card.suit]
if __name__ == "__main__":
     card = Card(rank ='3', suit='spades')
     print(spades_high(card))
# from random import choice
# choice(deck)