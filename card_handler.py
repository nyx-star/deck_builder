import random

class card:

    def __init__(self):
        self.name = "ERROR"
        self.type = "ERROR"
        self.rules = "ERROR"
        self.cost = "ERROR"

    def set_card(self, name, type, cost, rules):
        self.name = name
        self.type = type
        self.cost = cost
        self.rules = rules

    def get_name(self):
        return self.name
    def get_type(self):
        return self.type
    def get_cost(self):
        return self.cost
    def get_rules(self):
        return self.rules


class deck:

    def __init__(self):
        self.cards = []

    def add_card(self,card):
        self.cards.append(card)

    def draw_rand_card(self):
        """removes random card from deck and returns that card"""
        length = len(self.cards)
        card_number = random.randint(0,length-1)
        card = self.cards[card_number]
        self.cards.remove(card)
        return card

    def draw_specific_card(self,card_name):
        for card in self.cards:
            if card.get_name == card_name:
                self.cards.remove(card)
                return card

    def get_all_cards(self):
        return self.cards

    def number_of_cards(self):
        return len(self.cards)

    def empty(self):
        self.cards = []

    def add_cards(self,cards):
        for card in cards:
            self.cards.append(card)