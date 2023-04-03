############SETUP############
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.teammate = None
        self.order = None
        self.points = 0
    
    def __repr__(self):
        print("This is a Jass-Player named {0}. They are in a team with {1}.".format(self.name, self.teammate))
    
    def set_teammate(self, teammate):
        self.teammate = teammate
    
    def play_card(self, card):
        self.cards.pop(card)
        print(card)
        return card

class Cards:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.might = None
        self.value = None
    
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

card_colors = ["Rose", "Schilte", "Schelle", "Eichle"]
card_names = ["Ass", "Koenig", "Ober", "Under", "Banner", "Neun", "Acht", "Sieben", "Sechs"]
card_stack = []

for color in card_colors:
    for name in card_names:
        card_stack.append(Cards(name, color))

for card in card_stack:
    card.set_might_value()

player_1 = Player("Xaver")
player_2 = Player("Annemarie")
player_3 = Player("Alfred")
player_4 = Player("Elisabeth")



random.shuffle(card_stack)
print(player_1.name)
print(player_2.name)
print(player_3.name)
print(player_4.name)


############GAME PLAY###############
def supply_cards(card_stack):
    pass

print(player_1.cards)