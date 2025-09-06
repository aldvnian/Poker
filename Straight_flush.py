from Card import *

class Straight_flush():
    def __init__(self):
        self.name = "Straight Flush"

    def check(self, player_hand):
        clubs = []
        diamonds = []
        hearts = []
        spades = []
        special = ["J", "Q", "K", "A"]

        for item in player_hand:
            if item.value in special:
                value = 11 + special.index(item.value)
            else:
                value = int(item.value)
            if item.suit == "Clubs":
                clubs.append(int(value))
            elif item.suit == "Diamonds":
                diamonds.append(int(value))
            elif item.suit == "Hearts":
                hearts.append(int(value))
            else:
                spades.append(int(value))

        clubs = sorted(clubs)
        diamonds = sorted(diamonds)
        hearts = sorted(hearts)
        spades = sorted(spades)
        values = [clubs, diamonds, hearts, spades]

        for x in range(0, len(values)):
            count = 1
            if not len(values[x]) == 0:
                for y in range(1, len(values[x])):
                    if values[x][y] == values[x][y-1] + 1:
                        count += 1

                    if count == 5:
                        if values[x][y] > 10:
                            value_to_send = values[x][y] - 11
                            return [True, special[value_to_send]]
                        return [True, values[x][y]]
        return [False, '']
    
# card1 = Card("Spades", "6")
# card2 = Card("Spades", "10")
# card3 = Card("Spades", "9")
# card4 = Card("Spades", "8")
# card5 = Card("Spades", "7")
# card6 = Card("Diamonds", "3")
# card7 = Card("Hearts", "Q")
# hand = [card1, card2, card3, card4, card5, card6, card7]
# SF = Straight_flush()
# print(SF.check(hand))