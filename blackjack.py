# -*- coding: utf-8 -*-
"""
Created on Mon May  6 17:40:35 2019

@author: hma
"""


from collections import defaultdict

suits = ['hearts', 'spades', 'diamonds', 'clubs']
ranks = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']
values = {'two' : 2, 'three': 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9, 'ten' :10, 'jack' : 10, 'queen' : 10, 'king' : 10, 'ace' : 11}


class Deck():
    
    def __init__(self, deck=defaultdict(dict)):
        self.deck = deck
        print("Starting a new deck")

    def __string__(self):
        return(self.deck)    
   
mydeck=Deck(defaultdict(dict))

ct(dict))

self.deck[suits[suit]][ranks[rank]] = values[ranks[rank]]
                
    def draw(self):
        numcards=0
        
        while True:
            numcards += 1
            if numcards == 52:
                self.shuffle()
                numcards = 1
            suit=random.randint(0, 3)
            rank=random.randint(0, 11)
            drawn=self.deck[suits[suit]][ranks[rank]]
            if drawn != 0:
                break
        
        print("Card drawn: {} of {}".format(suits[suit],ranks[rank]))
        self.deck[suits[suit]][ranks[rank]] = 0
        
        return(drawn)

    def __string__(self):
        return(self.deck)
        
   
mydeck=Deck(defaultdict(dict))

huffle()
print(mydeck)