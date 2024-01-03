import deck


d = deck.deck()


while True:
    inpt = input("next move?")

    if inpt == "draw":
        d.draw()
        d.show()
    if inpt.startswith("play"):
        cardnumber = int(inpt[5:])
        d.play(cardnumber)
        d.show()
    else:
        print(inpt + " is not a valid command")