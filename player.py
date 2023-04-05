############ SETUP ############
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.order = None
        self.points = 0
    
    def __repr__(self):
        print("This is a Jass-Player named {0}. They are in a team with {1}.".format(self.name, self.teammate))

    
    def show_cards(self):
        print("""
        {0} has the following cards:"
        """.format(self.name))
        for card in self.cards:
            print(card.full_name)
    
    def play_card(self, table):
        print(f"{self.name}'s turn:")
        for i in range(len(self.cards)):
            print(f"{i} {self.cards[i].full_name}")
        card_to_play = int(input("Select Card to Play by Number: "))
        if card_to_play not in range((len(self.cards))-1):
            print(f"Please select a number between 0 and {len(self.cards) - 1}")
        else:
            played_card = self.cards.pop(card_to_play)
            table.append(played_card)
            print(f"{self.name} played {played_card.full_name}")


class Cards:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.might = None
        self.value = None
        self.full_name = self.color + " " + self.name
    
    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color
    
    def get_might(self):
        return self.might
    
    def get_value(self):
        return self.value
    
    def set_might_value(self):
        name = self.name
        match name:
            case "Ass":
                self.might = 9
                self.value = 11
            case "Koenig":
                self.might = 8
                self.value = 4
            case "Ober":
                self.might = 7
                self.value = 3
            case "Under":
                self.might = 6
                self.value = 2
            case "Banner":
                self.might = 5
                self.value = 10
            case "Neun":
                self.might = 4
                self.value = 0
            case "Acht":
                self.might = 3
                self.value = 8
            case "Sieben":
                self.might = 2
                self.value = 0
            case "Sechs":
                self.might = 1
                self.value = 0




######### Create Cards ##############
def create_cards():
    card_colors = ["Rose", "Schilte", "Schelle", "Eichle"]
    card_names = ["Ass", "Koenig", "Ober", "Under", "Banner", "Neun", "Acht", "Sieben", "Sechs"]
    card_stack = []
    for color in card_colors:
        for name in card_names:
            card_stack.append(Cards(name, color))

    for card in card_stack:
        card.set_might_value()
    return card_stack


########## Create Players ##############
def create_player(player):
    return Player(player)



########## Shuffle Cards ###############
def shuffle_cards(card_stack):
    random.shuffle(card_stack)


########## Distribute Cards ###############
def distribute_cards(player_1, player_2, player_3, player_4, card_stack):
    while len(card_stack) > 0:
        player_1.cards.append(card_stack.pop(0))
        player_2.cards.append(card_stack.pop(0))
        player_3.cards.append(card_stack.pop(0))
        player_4.cards.append(card_stack.pop(0))


############ PLAY ROUND ###############
def play_round(player_1, player_2, player_3, player_4):
    table = []
    player_1.play_card(table)
    player_2.play_card(table)
    player_3.play_card(table)
    player_4.play_card(table)
    print(" ")
    for card in table:
        print(card.full_name)


############ COUNT POINTS ##############



############   TESTING ZONE    #################
card_stack = create_cards()
player_1 = create_player("Annemarie")
player_2 = create_player("Elisabeth")
player_3 = create_player("Xaver")
player_4 = create_player("Alfred")
shuffle_cards(card_stack)
distribute_cards(player_1, player_2, player_3, player_4, card_stack)
play_round(player_1, player_2, player_3, player_4)
play_round(player_1, player_2, player_3, player_4)
play_round(player_1, player_2, player_3, player_4)