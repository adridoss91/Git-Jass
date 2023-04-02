class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.teammate = None
        self.order = None
        self.points = 0
    
    def __repr__(self):
        print("This")
    
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
            case "König":
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
card_names = ["Ass", "König", "Ober", "Under", "Banner", "Neun", "Acht", "Sieben", "Sechs"]
card_stack = []

for color in card_colors:
    for name in card_names:
        card_stack.append(Cards(name, color))

print(card_stack)
print("Is this working?")