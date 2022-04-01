import random


class Player:

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
            # True - no information, False - seen the card

    def add_card(self, card):
        self.cards.append(card)
        self.information_card[card] = False

    def print_information_card(self):
        for key in self.information_card.keys():
            print(str(key) + ": " + str(self.information_card[key]))

    # Method for the current room
    def set_current_room(self, room):
        self.current_room = room

    # Method for going to adjacent rooms
    def go_to_room(self, verbose):
        for room in self.current_room.neighbours:
            if self.information_card[room.name] == True:
                next_room = room
                if self.current_room == next_room and verbose == 1:
                    print(self.nickname + " stays at " + self.current_room.name)
                else:
                    self.current_room = room
                    if verbose == 1:
                        print(self.nickname + " goes to " + self.current_room.name)
                return

        # One step look ahead
        for room in self.current_room.neighbours:
            for adj in room.neighbours:
                if self.information_card[adj.name] == True:
                    self.current_room = room
                    if verbose == 1:
                        print(self.nickname + " goes to " + self.current_room.name)
                    return
        
        self.current_room = random.choice(self.current_room.neighbours)

    # Edit this method
    def make_guess(self, verbose):
        person = None
        place = self.current_room.name
        weapon = None
        for p in self.suspects:
            if self.information_card[p] == True:
                person = p
                break
        if not person:
            person = random.choice(self.suspects)
        for w in self.weapons:
            if self.information_card[w] == True:
                weapon = w
                break
        if not weapon:
            weapon = random.choice(self.weapons)


        if verbose == 1:
            print()
            print(self.nickname + "'s guess:")
            print()
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

