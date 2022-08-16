from deck import Deck

my_deck = Deck()
for i in my_deck.all_cards:
    print(i)
my_deck.shuffle_deck()
for i in my_deck.all_cards:
    print(i)
