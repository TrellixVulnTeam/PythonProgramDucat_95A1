# Python Program to Shuffle Deck of Cards  ????               {any one 10 cards in the deck of card ok.. }


import random
deck=[]
for deck1 in range(1,52):
	deck.append(deck1)
	random.shuffle(deck)           # random order in the deck of cards in the order of range any order set deck of cards :
print(deck)



'''
# another mathod using the mathod of random shuffle deck of cards ????
# Python program to shuffle a deck of card using the module random and draw 10 cards
'''


# import modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# draw 10 cards
print("You got:")
for i in range(10):
   print(deck[i][0], "of", deck[i][1])
   
   
