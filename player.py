############ SETUP ############
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.order = None
        self.points = 0
    
    def __repr__(self):
        print("This is a Jass-Player named {0}.".format(self.name))

    
    def show_cards(self):
        print("""
        {0} has the following cards:"
        """.format(self.name))
        for card in self.cards:
            print(card.full_name)
    
    def play_card(self, table, color=None):
        print(f"{self.name}'s turn:")
        color_to_select = color
        if color_to_select == None:
            for i in range(len(self.cards)):
                print(f"{i} {self.cards[i].full_name}")
            card_to_play = int(input("Select Card to Play by Number: "))
            if card_to_play not in range((len(self.cards))-1):
                print(f"Please select a number between 0 and {len(self.cards) - 1}")
            else:
                played_card = self.cards.pop(card_to_play)
                table.append(played_card)
                print(f"{self.name} played {played_card.full_name}")
        else:
            for i in range(len(self.cards)):
                print(f"{i} {self.cards[i].full_name}")
            card_to_play = int(input("Select Card to Play by Number: "))
            if card_to_play not in range((len(self.cards))-1):
                card_to_play = int(input(f"Please select a number between 0 and {len(self.cards) - 1}"))
            else:
                if self.cards[card_to_play].color != color_to_select:
                    you_sure = input("Are you sure you want to play this card? It is not the same color as the first card played. You might be cheating. Select y/n")
                    if you_sure == 'y':
                        played_card = self.cards.pop(card_to_play)
                        table.append(played_card)
                        print(f"{self.name} played {played_card.full_name}")
                    elif you_sure == 'n':
                        card_to_play = int(input("Select Card to Play by Number: "))
                    else:
                        you_sure = input("Please select either y or n!")
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
    color_played = ""
    player_1.play_card(table)
    color_played = table[0].color
    winning_player = player_1
    winning_card = table[0]
    player_2.play_card(table, color_played)
    if table[1].color == color_played:
        if table[1].might > winning_card.might:
            winning_player = player_2
            winning_card = table[1]
    player_3.play_card(table, color_played)
    if table[2].color == color_played:
        if table[2].might > winning_card.might:
            winning_player = player_3
            winning_card = table[2]
    player_4.play_card(table, color_played)
    if table[3].color == color_played:
        if table[3].might > winning_card.might:
            winning_player = player_4
            winning_card = table[3]
    print(" ")
    for card in table:
        print(card.full_name)
        winning_player.points += card.value
    print(winning_player.name, winning_card.full_name, winning_player.points)
    return winning_player


########### PLAY GAME ##################
def play_game(first_player, second_player, third_player, fourth_player):
    if len(first_player.cards) < 1:
        return "Round One Finished"
    winner = play_round(first_player, second_player, third_player, fourth_player)
    if winner == first_player:
        second = second_player
        third = third_player
        fourth = fourth_player
    elif winner == second_player:
        second = third_player
        third = fourth_player
        fourth = first_player
    elif winner == third_player:
        second = fourth_player
        third = first_player
        fourth = second_player
    elif winner == fourth_player:
        second = first_player
        third = second_player
        fourth = third_player
    play_game(winner, second, third, fourth)



############ COUNT POINTS ##############



############   TESTING ZONE    #################

player_1 = Player(input("What is your name?"))
player_2 = Player(input("What is your name?"))
player_3 = Player(input("What is your name?"))
player_4 = Player(input("What is your name?"))
card_stack = create_cards()
shuffle_cards(card_stack)
distribute_cards(player_1, player_2, player_3, player_4, card_stack)
play_game(player_1, player_2, player_3, player_4)
points_team_one = player_1.points + player_3.points
points_team_two = player_2.points + player_4.points
if points_team_one > points_team_two:
    print "Winner: {0} and {1}.".format(player_1.name, player_3.name)
elif points_team_two > points_team_one:
    print "Winner: {0} and {1}.".format(player_2.name, player_4.name)
else:
    print "There was no winner today."