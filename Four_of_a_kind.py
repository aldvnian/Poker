from Card import *

class Four():
    def __init__(self):
        self.name = "Four Of A Kind"

    def check(self, player_hand):
        for x in range(0, len(player_hand)):
            count = 0
            current_value = player_hand[x].value
            for y in range(0, len(player_hand)):
                if y != x:
                    temp_value = player_hand[y].value
                    if current_value == temp_value:
                        count += 1
                if count == 3:
                    return [True, current_value]
        return [False, ""]