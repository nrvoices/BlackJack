# -*- coding: utf-8 -*-
"""
Created on Mon May  6 17:40:35 2019

@author: hma
"""

import random
import time


suits = ['hearts', 'spades', 'diamonds', 'clubs']
ranks = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
values = {'two' : 2, 'three': 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9, 'ten' :10, 'jack' : 10, 'queen' : 10, 'king' : 10, 'ace' : 11}

class Deck():
    deck = []
    card = ''
    value = 0  
    
    def __init__(self):
        print("Starting a new deck")
    
    def shuffle(self):
        for suit in range(4):
            for rank in range(13):
                Deck.deck.append(ranks[rank] + " of " + suits[suit])
                       
    def draw(self):
        while True:
            try:
                for i in range(int(time.localtime().tm_sec)):
                    random.shuffle(Deck.deck)
            
                Deck.value = values[Deck.deck[0].split(' ', 1)[0]]
                Deck.card = Deck.deck[0]
                del Deck.deck[0]
                break
            except:
                print("Ran out of cards, building new deck")
                self.shuffle()
                
class Player():
    def __init__(self,name,hand=0,amount=0,bet=0,cards=[]):
        self.name = name
        self.hand = hand
        self.amount = amount
        self.bet = bet
        self.cards = cards
        
    def add(self,value,card):
        if value == 11:
            if self.hand + value < 21:
                self.hand += value
            else:
                self.hand += 1
        else:
            self.hand += value
        
        self.cards.append(card)
        if self.name == "Computer":
            print("{} draws {} for a total of {}".format(self.name,card,self.hand))
        else:
            print("{} draw {} for a total of {}".format(self.name,card,self.hand))
    
    def tally(self,winnings):
        self.amount += winnings
        if self.name == "You":
            print("You have ${}".format(self.amount))
        
    def clear(self):
        self.hand=0
        self.bet=0
        self.cards=[]

def take_bet(funds):
    bet = 0
    
    while True:
        try:
            bet = int(input("Enter an amount to bet: "))
        except:
            print("That is not a valid amount, try aagin.")
        else:
            if bet > funds:
                print("Don't you wish!")
            elif bet == 0:
                print("Minimum bet is $1")
            else:
                break

    return bet

def play_blackjack():
    mydeck.shuffle()
    
    mydeck.draw()
    player.add(mydeck.value,mydeck.card)
    mydeck.draw()
    player.add(mydeck.value,mydeck.card)
    
    if player.hand != 21:
        while True:
            hitme = input("Want another card? <Y/N> ")
            if hitme.upper() != "Y":
                break
            else:
                mydeck.draw()
                player.add(mydeck.value,mydeck.card)
                if player.hand > 20:
                    break

    if player.hand == 21:
        print("Blackjack, you win!")
    elif player.hand > 21:
        print("Bust, you lose!")
        player.bet *= -1
    else:
        while (computer.hand < player.hand or computer.hand < 20):
            mydeck.draw()
            computer.add(mydeck.value,mydeck.card)
        
        if computer.hand > 21:
            print("Computer bust, you win!")
        elif computer.hand > player.hand:
            print("Computer wins!")
            player.bet *= -1
        else:
            print("You win!")
        
    player.tally(player.bet)  
    player.clear()
    computer.clear()

#Start of game              

print('\n\n\n\n\n')
print("Welcome to BlackJack!")
print("You have $100")

mydeck=Deck()
player=Player(name="You",amount=100,bet=take_bet(100))
computer=Player(name="Computer")
    
while True:
    play_blackjack()
    if player.amount < 1:
        print("You have no more money.  Please come back!")
        break
    playagain = input("Would you like to play again? <Y/N> ")
    if playagain.upper() == "N":
        print("You leave the table with ${}".format(player.amount))
        break
    player.bet = take_bet(player.amount)
