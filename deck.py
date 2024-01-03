import decks
import random


class deck:

    def __init__(self):
        self.drawpile = decks.decks().getstartingdeck()
        self.hand = []
        self.discardpile = []

    def draw(self):
        card = random.randint(0,len(self.drawpile) - 1)
        self.hand.append(self.drawpile[card])
        self.drawpile.pop(card)

    def show(self):
        print("drawpile:")
        for card in self.drawpile:
            print("    " + card.getname())

        print("hand:")
        for card in self.hand:
            print("    " + card.getname())

        print("discardpile:")
        for card in self.discardpile:
            print("    " + card.getname())


    def play(self,cardnumber):
        card = self.hand[cardnumber]
        self.hand.pop(cardnumber)
        self.discardpile.append(card)