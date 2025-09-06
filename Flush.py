from Card import *

class Flush():
    def __init__(self):
        self.name = "Flush"

    def check(self, player_hand):
        for x in range(0, len(player_hand)):
            current_suit = player_hand[x].suit
            count = 0
            for y in range(0, len(player_hand)):
                temp_suit = player_hand[y].suit
                if x != y:
                    if current_suit == temp_suit:
                        count += 1
                if count == 4:
                    highest = self.find_highest(player_hand, current_suit)
                    return [True, highest]
        return [False, ""]

    def find_highest(self, player_hand, suit):
        ranking = {
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14,
        }

        highest = ''
        temp = -1000
        for item in player_hand:
            if item.suit == suit:
                if not item.value in ranking.keys():
                    if int(item.value) > temp:
                        temp = int(item.value)
                        highest = item.value
                else:
                    actual_value = ranking[item.value]
                    if int(actual_value) > temp:
                        temp = int(actual_value)
                        highest = item.value
        return highest