from venv import create
from values_suits_ranks import suits
from values_suits_ranks import ranks
from card import Card
from random import shuffle


class Deck():

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                temp_card = Card(suit, rank)
                self.all_cards.append(temp_card)

    def shuffle_deck(self):
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
