import xml.etree.ElementTree as ET
import card_handler


class manager:
    def __init__(self):
        self.file_name = "decks.xml"
        self.decks = {
            "hand": []
        }

        self.make_decks()


    def make_decks(self):
        tree = ET.parse(self.file_name)
        root = tree.getroot()

        for deck in root:
            temp_deck = card_handler.deck()
            deck_name = deck.attrib["name"]
            for card in deck:
                name = card[0].text
                type = card[1].text
                cost = card[2].text
                rules = card[3].text
                num_times = int(card[4].text)

                temp_card = card_handler.card()
                temp_card.set_card(name,type,cost, rules)
                for i in range (0,num_times):
                    temp_deck.add_card(temp_card)
            self.decks[deck_name] = temp_deck

    def view(self,deck_name):
        """selects random card from displays the card drawn"""
        for card in self.decks[deck_name].get_all_cards():
            print(card.get_name())
            print("type: ",card.get_type())
            print("cost: ",card.get_cost())
            print(card.get_rules())
            print("----------------------------------------------------")


    def transfer(self,original_deck,target_deck,card_name=None):
        """draws random card from original deck and puts it in the target deck.
        name will draw a card with that name instead of a random one."""
        if card_name == None:
            card = self.decks[original_deck].draw_rand_card()
        else:
            card = self.decks[original_deck].draw_specific_card(card_name)

        #add card to target

        self.decks[target_deck].add_card(card)


    def transfer_all(self,original_deck,target_deck):
        cards = self.decks[original_deck].get_all_cards()
        self.decks[target_deck].add_cards(cards)
        self.decks[original_deck].empty()


    def get_deck_ammounts(self):
        header = ""
        for deck in self.decks:
            header += deck + ": " + str(self.decks[deck].number_of_cards()) + "  "
        return header