from Card import *

class Royal_flush():
    def __init__(self):
        self.name = "Royal Flush"

    def check(self, player_hand):
        clubs = []
        diamonds = []
        hearts = []
        spades = []
        checks = ['A', 'K', 'Q', 'J', '10']

        for item in player_hand:
            if item.suit == "Clubs":
                clubs.append(item.value)
            elif item.suit == "Diamonds":
                diamonds.append(item.value)
            elif item.suit == "Hearts":
                hearts.append(item.value)
            else:
                spades.append(item.value)

        values = [clubs, diamonds, hearts, spades]

        for each in values:
            count = 0
            for x in range(0, len(each)):
                if each[x] in checks:
                    count += 1

                if count == 5:
                    return [True]
        return [False]