class Pair():
    def __init__(self):
        self.name = "Pair"

    def check(self, player_hand):
        for x in range(0, len(player_hand)):
            current_value = player_hand[x].value
            for y in range(0, len(player_hand)):
                if y != x:
                    temp_value = player_hand[y].value
                    if current_value == temp_value:
                        return [True, current_value]
        return [False, '']