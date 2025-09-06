from Card import *
from Pair import *

class Two_pair(Pair):
    def __init__(self):
        self.name = "Two Pair"

    def check(self, player_hand):
        card_checked = ''
        count = 0
        return_list = []
        for x in range(0, len(player_hand)):
            current_value = player_hand[x].value
            if count == 2:
                return_list.append(True)
                return return_list[::-1]
            if card_checked == current_value:
                continue
            for y in range(0, len(player_hand)):
                if x != y:
                    temp_value = player_hand[y].value
                    if current_value == temp_value:
                        count += 1
                        card_checked = current_value
                        return_list.append(current_value)
                        break
        return [False, '', '']