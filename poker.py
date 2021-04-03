#!/usr/bin/python3

import random

class Hearts:
    def __str__(self):
        return '\u2665'
    def __repr__(self):
        return '\u2665'
class Diamonds:
    def __str__(self):
        return '\u2666'
    def __repr__(self):
        return '\u2666'
class Spades:
    def __str__(self):
        return '\u2660'
    def __repr__(self):
        return '\u2660'
class Clubs:
    def __str__(self):
        return '\u2663'
    def __repr__(self):
        return '\u2663'

class Player:
    def __init__(self, number: int, cards: list, chips: int):
        self.number = number
        self.cards = cards
        self.chips = chips

class Cards:
    def __init__(self):
        self.deck = list()
        self.shuffle_deck()

    def shuffle_deck(self):
        self.deck = self._deck_generator()
        random.seed()
        random.shuffle(self.deck)

    def _deck_generator(self):
        deck = list()
        kinds = [Hearts, Diamonds, Spades, Clubs]
        cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for k in kinds:
            for c in cards:
               deck.append((c, k()))
        return deck

    def deal_cards(self):
        deal = list()
        for i in range(2):
            deal.append(self.deck.pop(0))
        return deal

    def flop(self):
        self.deck.pop(0)
        l = []
        for i in range(3):
            l.append(self.deck.pop(0))
        return l

    def _pop(self):
        self.deck.pop(0)
        return self.deck.pop(0)

    def turn(self):
        return self._pop()

    def river(self):
        return self._pop()

class Betting:
    def __init__(self, scale: int = 1):
        self.pot = 0
        self.ante = 10 * scale
        self.small_blind = 15 * scale
        self.big_blind = 25 * scale
        self.default_chips = 2000 * scale

class Players:
    def __init__(self, cards: Cards, betting: Betting, player_count: int):
        self.cards = cards
        self.betting = betting
        self.player_count = player_count
        self.player_list = list()
        self.create_players()

    def getcards(self):
        return self.cards.deal_cards()

    def getchips(self):
        return self.betting.default_chips

    def create_players(self):
        self.player_list = list()
        for p in range(self.player_count):
            cards = self.getcards()
            chips = self.getchips()
            player = Player(p, cards, chips)
            self.player_list.append(player)

def main():
    player_count = 4
    cards = Cards()
    betting = Betting()
    players = Players(cards, betting, player_count)

    print(players.player_list[0].cards, players.player_list[0].chips)
    print(players.player_list[1].cards, players.player_list[1].chips)
    print(players.player_list[2].cards, players.player_list[2].chips)
    print(players.player_list[3].cards, players.player_list[3].chips)

    flop = cards.flop()
    turn = cards.turn()
    river = cards.river()
    print(flop, turn, river)

if __name__ == '__main__':
    main()
#EOF

