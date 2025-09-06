from Pair import *
from Two_pair import *
from Three_of_a_kind import *
from Full_house import *
from Four_of_a_kind import *
from Straight import *
from Flush import *
from Straight_flush import *
from Royal_flush import *
from Player import *
from Card import *

class Evaluation():
    def __init__(self):
        self.pair = Pair()
        self.two = Two_pair()
        self.three = Three()
        self.full = Full_house()
        self.flush = Flush()
        self.straight = Straight()
        self.four = Four()
        self.SF = Straight_flush()
        self.RF = Royal_flush()
        self.list = [self.RF, self.SF, self.four, self.full, self.flush, 
                     self.straight, self.three, self.two, self.pair]
        self.checks = ['J', 'Q', 'K', 'A']

    def evaluate(self, player_hand):
        for item in self.list:
            store = item.check(player_hand)
            if store[0]:
                return item.name
        return 'High Card'
    
    def higher_card(self, first_card, second_card):
        if first_card in self.checks:
            first_value = 10 + self.checks.index(first_card) + 1
        else:
            first_value = int(first_card)
        if second_card in self.checks:
            second_value = 10 + self.checks.index(second_card) + 1
        else:
            second_value = int(second_card)

        if first_value > second_value:
            return True
        return False
    
    def hand_comparison(self, hand_to_use, players_list):
        winners = []
        highest_card = ""
        for player in players_list:
            store = hand_to_use.check(player.get_deck())
            if store[0] == False:
                continue
            card_value = store[1]
            if not highest_card == "":
                higher = self.higher_card(card_value, highest_card)
                if higher:
                    highest_card = card_value
            else:
                highest_card = card_value

        for player in players_list:
            store = hand_to_use.check(player.get_deck())
            card_value = store[1]
            if highest_card == card_value:
                winners.append(player)
        return winners
        
    def tie_breaker(self, rank, players_list):
        winners = []

        if rank == "High Card":
            cards = []
            for player in players_list:
                higher = self.higher_card(player.deck[5].get_value(), player.deck[6].get_value())
                if higher:
                    cards.append(player.deck[5])
                else:
                    cards.append(player.deck[6])

            highest_card = cards[0]
            for card in cards:
                stays_highest = self.higher_card(highest_card.get_value(), card.get_value())
                if not stays_highest:
                    highest_card = card

            for x in range(len(cards)):
                if highest_card.get_value() == cards[x].get_value():
                    winners.append(players_list[x])

        if rank == "Pair": #Works fully
            winners_list = self.hand_comparison(self.pair, players_list)
            winners = winners_list


        if rank == "Two Pair": #Works fully
            store_of_cards = []
            store_of_players = []
            for player in players_list:
                store = self.two.check(player.get_deck())
                if store[0] == False:
                    continue
                temp = [store[1], store[2]]
                store_of_cards.append(temp)
                store_of_players.append(player)

            highest_card = store_of_cards[0][0]
            for x in range(0, len(store_of_cards)):
                for y in range(2):
                    is_higher = self.higher_card(highest_card, store_of_cards[x][y])
                    if not is_higher:
                        highest_card = store_of_cards[x][y]
            
            for a in range(0, len(store_of_cards)):
                for b in range(2):
                    if store_of_cards[a][b] == highest_card:
                        winners.append(store_of_players[a])

        if rank == "Three Of A Kind":
            winners_list = self.hand_comparison(self.three, players_list)
            winners = winners_list

        if rank == "Straight":
            winners_list = self.hand_comparison(self.straight, players_list)
            winners = winners_list

        if rank == "Flush":
            winners_list = self.hand_comparison(self.flush, players_list)
            winners = winners_list

        if rank == "Full House":
            three = []
            pair = []
            players_with_three = []
            highest_three = ""
            highest_player = None
            highest_player_pair = ""

            for player in players_list:
                store = self.full.check(player.get_deck())
                if store[0] == False:
                    continue
                three.append(store[1])
                pair.append(store[2])
                players_with_three.append(player)

            for card in three:
                if highest_three == "":
                    highest_three = card
                else:
                    stays_higher = self.higher_card(highest_three, card)
                    if not stays_higher:
                        highest_three = card
            
            for player in players_with_three:
                store = self.full.check(player.get_deck())
                if store[1] == highest_three:
                    if highest_player == None:
                        highest_player = player
                        highest_player_pair = store[2]
                    else:
                        stays_highest = self.higher_card(highest_player_pair, store[2])
                        if highest_player_pair == store[2]:
                            winners.append(player)
                        elif not stays_highest:
                            highest_player = player
                            highest_player_pair = store[2]
            winners.append(highest_player)


        if rank == "Four Of A Kind":
            winners_list = self.hand_comparison(self.four, players_list)
            winners = winners_list

        if rank == "Straight Flush":
            winners_list = self.hand_comparison(self.SF, players_list)
            winners = winners_list

        if rank == "Royal Flush":
            for player in players_list:
                check = self.RF.check(player.get_deck())
                if check:
                    winners.append(player)
        return winners
    
# p1 = Player("Adnan")
# p2 = Player("Adrian")
# p1.deck = [Card("Spades", "Q"), Card("Diamonds", "2"), Card("Diamonds", "7"), Card("Clubs", "5"), Card("Hearts", "3"), Card("Clubs", "A"), Card("Diamonds", "9")]
# p2.deck = [Card("Spades", "Q"), Card("Diamonds", "2"), Card("Diamonds", "7"), Card("Clubs", "5"), Card("Hearts", "3"), Card("Spades", "A"), Card("Spades", "6")]
# eval = Evaluation()
# winning_player = eval.tie_breaker("High Card", [p1, p2])
# print(winning_player[0].name, winning_player[1].name)