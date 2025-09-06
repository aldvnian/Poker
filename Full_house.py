from Card import *

class Full_house():
    def __init__(self):
        self.name = "Full House"

    def check(self, player_hand):
        three = None
        pair = None
        value_store = []
        for item in player_hand:
            value_store.append(item.value)

        for value in value_store:
            count = value_store.count(value)
            if count == 3:
                three = value
            if count == 2:
                pair = value
            if three != None and pair != None:
                return [True, three, pair]
        return [False, '', '']