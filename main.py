from player import Player
from deck import Deck
from random import shuffle


i = int(input("Enter 1 to start: "))

if i == 1:
    new_deck = Deck()
    new_deck.shuffle_deck()
    cards = new_deck.all_cards
    player_1 = Player("player_1")
    player_2 = Player("player_2")

    player_1.add_cards(cards[0:25:1])
    player_2.add_cards(cards[26:51:1])

    ip = input("Enter 'y' to make move and 'n' to stop : ")

    while ip == 'y':
        player_1_card = player_1.remove_one()
        player_2_card = player_2.remove_one()

        print("Cards on the table:")
        print(player_1_card)
        print(player_2_card)

        if player_1_card.value > player_2_card.value:
            print("player_1 won this round.")
            player_1.add_cards([player_1_card, player_2_card])
        elif player_2_card.value > player_1_card.value:
            print("player_2 won this round.")
            player_2.add_cards([player_1_card, player_2_card])
        else:
            pass
        shuffle(player_1.all_cards)
        shuffle(player_2.all_cards)

        ip = input("Enter 'y' to make move and 'n' to stop: ")
    else:
        print("You stopped the game.")
        print("By far: ")
        if len(player_1.all_cards) > len(player_2.all_cards):
            print("player_1 WON!")
        elif len(player_1.all_cards) < len(player_2.all_cards):
            print("player_2 WON!")
        else:
            print("Draw!")
