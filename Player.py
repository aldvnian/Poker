class Player():
    def __init__(self, name):
        self.name = name
        self.deck = []
        self.fold = False
        self.coins = 10000
        self.rank = "High Card"
        self.raised = 0

    def set_rank(self, rank):
        self.rank = rank

    def get_rank(self):
        return self.rank

    def add_card(self, card):
        self.deck.append(card)

    def get_deck(self):
        return self.deck
    
    def print_deck(self):
        print("")
        print(self.name, "'s deck:")
        for item in self.deck:
            item.print_card()
        print("")

    def folding(self):
        self.fold = True

    def has_folded(self):
        return self.fold

    def reduce_coins(self, amount):
        self.coins -= amount

    def add_coins(self, amount):
        self.coins += amount

    def get_coins(self):
        return self.coins

    def print_coins(self):
        print("  Coins: ", self.coins)

    def get_name(self):
        return self.name
    
    def set_raised(self, amount):
        self.raised = amount

    def get_raised(self):
        return self.raised
    
    def add_to_raised(self, amount):
        self.raised += amount