import manager

class input_processor:
    def __init__(self):
        self.manager = manager.manager()

    def input_loop(self):
        while(True):
            inpt = input(self.heading())
            if inpt == "quit":
                break
            elif inpt.startswith("transfer all"):
                try:
                    self.transfer_all(inpt)
                except:
                    print("ERROR. check your spelling")
            elif inpt.startswith("transfer multiple"):
                self.transfer_multiple(inpt)
            elif inpt.startswith("transfer"):
                try:
                    self.transfer(inpt)
                except:
                    print("ERROR. check your spelling")
            elif inpt.startswith("view"):
                try:
                    self.view(inpt)
                except:
                    print("ERROR. check your spelling")


    def heading(self):
        answer = "commands: 'quit' 'transfer [original deck],[deck to transfer to]' 'view [deck]' \n" \
                 "'transfer all [original deck],[new deck]' 'transfer multiple [original deck],[deck to transfer to],[number of cards]' \n" \
                "\n"
        answer += self.manager.get_deck_ammounts()
        answer += "\n> "
        return answer

    def transfer(self,inpt):
        data = inpt[9:]
        original_deck = ""
        new_deck = ""

        #get old and new decks
        pre_comma = True
        for ch in data:
            if ch == ",":
                pre_comma = False
            elif pre_comma:
                original_deck += ch
            else:
                new_deck += ch

        #transfer from old to new
        self.manager.transfer(original_deck,new_deck)


    def view(self,inpt):
        target_deck = inpt[5:]
        self.manager.view(target_deck)

    def transfer_all(self, inpt):
        data = inpt[13:]
        original_deck = ""
        new_deck = ""

        # get old and new decks
        pre_comma = True
        for ch in data:
            if ch == ",":
                pre_comma = False
            elif pre_comma:
                original_deck += ch
            else:
                new_deck += ch

        # transfer from old to new
        self.manager.transfer_all(original_deck, new_deck)

    def transfer_multiple(self,inpt):
        num_commas = 0
        num_transfers = ""
        #get number of transfers (everything after the second comma
        for ch in inpt:
            if ch == ",":
                num_commas += 1
            elif num_commas == 2:
                num_transfers += ch

        inpt = inpt[9:]
        inpt = inpt[:len(inpt) - (len(num_transfers) + 1)]
        num_transfers = int(num_transfers)

        #calls transfer for num_transfers of times
        for i in range(0,num_transfers):
            self.transfer(inpt)