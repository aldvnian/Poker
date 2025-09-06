from Player import *
from Card import *
from Evaluation import *
import random


class Game():
    def __init__(self, nr_of_players):
        self.stage = 1
        self.players = []

        #Adding player objects to the list
        for x in range(1, nr_of_players + 1):
            name = input(f"Name of player{x}:\n")
            self.players.append(Player(name))

        self.current_player = self.players[0]
        self.community = [] #community cards
        self.coins_collection = 0
        self.last_raised = -1
        self.evaluation = Evaluation() #class with methods to evaluate the winner hand
        self.ranking = ["High Card", "Pair", "Two Pair", "Three Of A Kind", "Straight", "Flush", 
                        "Full House", "Four Of A Kind", "Straight Flush", "Royal Flush"]
        self.used_cards = [[], [], [], []]
        self.last_raised_player = None
        self.extra_coins = 0
        self.minimum = 0
        self.max = len(self.players)*10000


    #Joins player hand with community cards
    def join_decks(self, player_hand, deck):
        lst = []
        for item in deck:
            lst.append(item)
        for item in player_hand:
            lst.append(item)
        return lst


    #Queries the current player for input
    def user_input(self, coins, last_raised, player_raised):
        print("\nRaising the bet is allowed only in 50 coins\n")
        amount = int(input(f"How much would you like to raise?\nOptions:\nCheck - {last_raised - player_raised}\nall in ({coins})\n"))
        while amount > coins or amount % 50 != 0 or amount < (last_raised - player_raised):
            if amount == coins:
                break
            print("\nThat is an incorrect amount\n")
            amount = int(input(f"How much would you like to raise?\nOptions:\nCheck - {last_raised - player_raised}\nall in ({coins})\n"))
        return amount


    #Display community cards
    def print_community(self):
        for card in self.community:
            card.print_card()


    def display(self, current_player):
        current_player.print_deck() #Print deck
        joint_deck = self.join_decks(current_player.get_deck(), self.community)
        hand = self.evaluation.evaluate(joint_deck)
        current_player.set_rank(hand) #Evaluating player deck and setting it to their rank
        print("  Current hand:\n  ", hand, "\n")
        print("  Community cards:")
        for card in self.community:
            card.print_card()
        print("")
        current_player.print_coins() #Displays player coins
        print("  Collected coins: ", self.coins_collection) #Displays total collected coins


    # def protocol(self, player):
    #     if player.fold: #if player folds

    #         #If end of array reached
    #         if self.players.index(player) + 1 > len(self.players) - 1:
    #             if self.players[0] == self.last_raised_player: #If next player is the last raised player, returns if true
    #                 return
    #             self.protocol(self.players[0]) #Else call the next player which is at the start of the array

    #         #Otherwise checks if next player is last raised player, returns if true
    #         elif self.players[self.players.index(player) + 1] == self.last_raised_player:
    #             return
            
    #         #Finally if none of the above conditions meet, we recurse with next player
    #         else:
    #             self.protocol(self.players[self.players.index(player) + 1])
    #             return
            
    #     if self.everyone_folded()[0] == True:
    #         return
        
    #     self.display(player)
    #     print("\nLast Raised: ", self.last_raised)
    #     fold = input("Would you like to fold\ny/n?\n")

    #     if fold == 'y':
    #         player.folding() #Set player as folded
    #         if self.players.index(player) + 1 > len(self.players) - 1: #If last player in the list

    #             #Check if first player in the list is the last raised player
    #             if self.players[0] == self.last_raised_player:
    #                 return
            
    #         #Check if next player in the list is the last raised player
    #         elif self.players[self.players.index(player) + 1] == self.last_raised_player:
    #             return
       
    #     else:

    #         #Getting the bet amount and setting it as last raised if it is greater
    #         bet_amount = self.user_input(player.get_coins(), self.last_raised, player.raised)
    #         if bet_amount > self.last_raised:
    #             self.last_raised_player = player
    #             self.last_raised = bet_amount

    #         #Set player raised amount to bet amount if it is greater
    #         if bet_amount >= player.raised:
    #             player.raised += bet_amount

    #         previous_coins = player.coins
    #         player.reduce_coins(bet_amount)
    #         self.coins_collection += bet_amount
    #         if self.players.index(player) + 1 > len(self.players) - 1:
    #             if self.players[0] == self.last_raised_player:
    #                 if player.raised == self.last_raised or player.raised == previous_coins:
    #                     return
    #         elif self.players[self.players.index(player) + 1] == self.last_raised_player:
    #             if player.raised == self.last_raised or player.raised == previous_coins:
    #                 return

    #     temp = self.players.index(player)
    #     if temp + 1 < len(self.players):
    #         self.protocol(self.players[temp + 1])
    #     else:
    #         self.protocol(self.players[0])

    def protocol(self, player):
        self.display(player)
        print("\nMinimum: ", self.minimum)
        fold = input("Would you like to fold?\ny/n\n")
        if fold == "y":
            player.fold = True
        else:
            amount = self.user_input(player.coins, self.minimum, player.raised)
            player.coins -= amount
            player.raised += amount
            self.coins_collection += amount
            if amount > self.last_raised:
                self.last_raised = amount
                self.minimum = amount
                self.last_raised_player = player


    def roundly_chores(self):
        player = self.current_player
        while True:
            if not self.players.index(player) == len(self.players) - 1:
                player = self.players[self.players.index(player) + 1]
            else:
                player = self.players[0]
            if player == self.last_raised_player:
                break
            if not player.fold == True:
                self.protocol(player)

        self.last_raised = -1
        self.last_raised_player = None
        self.minimum = 0
        for player in self.players:
            player.set_raised(0)

        check_winner = self.everyone_folded()
        if check_winner[0] == True:
            self.win(check_winner[1], self.coins_collection)
            return
        
        if self.all_players_in():
            if self.stage == 1:
                self.community = self.make_card(5)
            elif self.stage == 2:
                self.community = self.make_card(2)
            elif self.stage == 3:
                self.community = self.make_card(1)
            for player in self.players:
                joint_deck = self.join_decks(player.get_deck(), self.community)
                player.deck = joint_deck
                if not player.fold:
                    print(player.get_name() + ":")
                    for card in joint_deck:
                        card.print_card()
                    print("")
                hand = self.evaluation.evaluate(player.deck)
                player.set_rank(hand)
            self.round_end_winners()
            self.stage = 1

        else:
            if self.stage < 4:
                self.stage += 1
            else:
                self.stage = 1

        players_to_remove = []
        for player in self.players:
            if player.get_coins() == 0:
                players_to_remove.append(player)
        for player in players_to_remove:
            self.players.remove(player)
    
    #Checks if everyone folded and returns remaining player
    def everyone_folded(self):
        count = 0
        remaining = 0
        for player in self.players:
            if not player.has_folded():
                count += 1
                remaining = player

        if count > 1: #If there is more than one player
            return [False, remaining]
        return [True, remaining]
    
    def win(self, player, amount):
        player.add_coins(amount)
        print("")
        print(player.get_name(), " has won the round!")
        self.stage = 1

    #If any player collects all the coins of other players, game terminates

    def make_card(self, amount):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        card_list = []
        for x in range(amount):
            while True:
                suit = random.choice(suits)
                value = random.choice(values)
                current_card = Card(suit, value)
                if not value in self.used_cards[suits.index(suit)]:
                    self.used_cards[suits.index(suit)].append(value)
                    card_list.append(current_card)
                    break
        return card_list

    def end_game(self):
        for player in self.players:
            coins =  player.get_coins()
            if coins == self.max:
                return True
        return False
    
    def all_players_in(self):
        condition = True
        for player in self.players:
            if not player.fold:
                if not player.get_coins() == 0:
                    condition = False
        return condition
    
    def round_end_winners(self):
        winners = []
        winning_deck = ""
        
        for player in self.players:
            if not player.has_folded():
                if winning_deck == "":
                    deck = player.get_rank()
                    winning_deck = deck
                else:
                    deck = player.get_rank()
                    winning_index = self.ranking.index(winning_deck)
                    temp_index = self.ranking.index(deck)
                    if winning_index < temp_index:
                        winning_deck = deck
                
        for player in self.players:
            if not player.fold:
                player_rank = player.get_rank()
                if self.ranking.index(winning_deck) == self.ranking.index(player_rank):
                    winners.append(player)

        if len(winners) == 1:
            self.win(winners[0], self.coins_collection)
        else:
            actual_winners = self.evaluation.tie_breaker(winning_deck, winners)
            winners_count = len(actual_winners)
            if winners_count == 1:
                self.win(actual_winners[0], self.coins_collection)
            elif winners_count > 1:
                if not self.coins_collection % winners_count == 0:
                    remainder = self.coins_collection % winners_count
                    reward = int((self.coins_collection - remainder)/winners_count)
                    self.extra_coins = remainder
                else:
                    reward = int(self.coins_collection/winners_count)
                for each_winner in actual_winners:
                    self.win(each_winner, reward)

    def main_game(self):
        #Initialising necessary variables
        start = 0
        round = 1
        increase_counter = 3
        winners = []
        winning_deck = ""
        
        #Main game loop
        while True:
            if self.stage == 1: #Round 1
                self.current_player = self.players[start]

                #Taking away initial amount, adding it to
                #the collection
                if self.current_player.get_coins() < round*250:
                    all_coins = self.current_player.get_coins()
                    self.coins_collection += all_coins
                    self.current_player.reduce_coins(all_coins)
                    self.minimum = all_coins
                    self.current_player.add_to_raised(all_coins)
                else:
                    self.current_player.reduce_coins(round*250)
                    self.coins_collection += round*250
                    self.minimum = round*250
                    self.current_player.add_to_raised(round*250)

                #Giving each player 2 random cards
                for player in self.players:
                    temp = self.make_card(2)
                    player.add_card(temp[0])
                    player.add_card(temp[1])

                self.roundly_chores()
                if self.end_game() == True: #Checks if whole game ended
                    break

            if self.stage == 2: #Round 2
                temp = self.make_card(3)
                for card in temp:
                    self.community.append(card)

                self.roundly_chores()
                if self.end_game() == True:
                    break

            if self.stage == 3: #Round 3
                temp = self.make_card(1) #Adding 1 card to community cards
                self.community.append(temp[0])


                self.roundly_chores()
                if self.end_game() == True: #Checks if whole game ended
                    break

            if self.stage == 4:
                temp = self.make_card(1) #Adding 1 card to community cards
                self.community.append(temp[0])

                self.roundly_chores()
                if self.end_game() == True:
                    break

                self.round_end_winners()

            for player in self.players:
                player.deck = []
                player.rank = None
                player.fold = False

            self.community.clear()
            self.coins_collection = 0
            increase_counter -= 1
            if increase_counter == 0:
                round *= 2
                increase_counter = 3

            for lst in self.used_cards:
                lst.clear()
            
            if start >= len(self.players) - 1:
                start = 0
            else:
                start += 1
        
        print("\nThe game has ended!")