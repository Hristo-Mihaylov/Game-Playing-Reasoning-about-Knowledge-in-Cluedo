import random

class RandomAI:
    def __init__(self, nickname):
        self.nickname = nickname
        self.cards = []
        self.neighbours = []
        self.current_room = None
        self.has_won = False
        self.suspects = ["Colonel Mustard", "Professor Plum",
                         "Reverend Green", "Mrs. Peacock", "Miss Scarlett", "Mrs. White"]
        self.weapons = ["Dagger", "Candlestick",
                        "Revolver", "Rope", "Lead piping", "Spanner"]
        self.rooms = ["Hall", "Lounge", "Library", "Kitchen",
                      "Billiard Room", "Study", "Ballroom", "Conservatory", "Dining Room"]

        random.shuffle(self.suspects)
        random.shuffle(self.weapons)
        random.shuffle(self.rooms)

        self.all_cards = ["Colonel Mustard", "Professor Plum", "Reverend Green", "Mrs. Peacock", "Miss Scarlett", "Mrs. White", "Dagger", "Candlestick",
                          "Revolver", "Rope", "Lead piping", "Spanner", "Hall", "Lounge", "Library", "Kitchen", "Billiard Room", "Study", "Ballroom", "Conservatory", "Dining Room"]
        self.information_card = {}
        for card in self.all_cards:
            self.information_card[card] = True

    
    def add_card(self, card):
        self.cards.append(card)
        self.information_card[card] = False

    def set_current_room(self, room):
        self.current_room = room

    def go_to_room(self, verbose):
        next_room = random.choice(self.current_room.neighbours)
        if self.current_room == next_room and verbose == 1:
            print(self.nickname + " stays at " + self.current_room.name)
        else:
            self.current_room = next_room
            if verbose == 1:
                print(self.nickname + " goes to " + self.current_room.name)

    
    def make_guess(self, verbose):
        person = random.choice(self.suspects)
        weapon = random.choice(self.weapons)
        place = self.current_room.name
        
        if verbose == 1:
            print('\n' + self.nickname + "'s guess:")
            print("Person: " + person)
            print("Weapon: " + weapon)
            print("Place: " + place)

        return [person, weapon, place]

    def disprove_guess(self, player, guess, verbose = 0):
        cards_in_hand = []
        for card in guess:
            if card in self.cards:
                cards_in_hand.append(card)
        if len(cards_in_hand) == 0:
            return None, False
        elif len(cards_in_hand) == 1:
            if type(player.information_card[cards_in_hand[0]]) != dict:
                player.information_card[cards_in_hand[0]] = False
            return cards_in_hand[0], True
        elif len(cards_in_hand) > 1:
            card_to_show = random.choice(cards_in_hand)
            if type(player.information_card[card_to_show]) != dict:
                player.information_card[card_to_show] = False
            return card_to_show, True