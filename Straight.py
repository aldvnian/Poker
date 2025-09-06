from Card import *

class Straight():
    def __init__(self):
        self.name = "Straight"

    def check(self, player_hand):
        special_cards = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        reverse = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
        values = []
        count = 1
        highest_card = ''

        for item in player_hand:
            if item.value in special_cards.keys():
                values.append(int(special_cards[item.value]))
            else:
                values.append(int(item.value))

        values = sorted(set(values))

        for index in range(1, len(values)):
            if values[index] == values[index - 1] + 1:
                count += 1
            else:
                count = 1
            if count == 5:
                if values[index] > 10:
                    return [True, reverse[values[index]]]
                return [True, str(values[index])]
        return [False, '']