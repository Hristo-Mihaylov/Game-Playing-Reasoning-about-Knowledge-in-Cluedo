import random

class AdvancedAI:

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

        self.known_cards = [[], [], []]

        self.all_cards = ["Colonel Mustard", "Professor Plum", "Reverend Green", "Mrs. Peacock", "Miss Scarlett", "Mrs. White", "Dagger", "Candlestick",
                          "Revolver", "Rope", "Lead piping", "Spanner", "Hall", "Lounge", "Library", "Kitchen", "Billiard Room", "Study", "Ballroom", "Conservatory", "Dining Room"]

        self.number_of_players = 0
        # self.opponents = []

        self.shown_cards = {}
        self.possible_opponent_cards = {}

        self.winning_cards = [" ", " ", " "]

        self.information_card = {}
        for card in self.all_cards:
            self.information_card[card] = {}


    def fill_information_card(self, players):
        for card in self.all_cards:
            for player in players:
                self.information_card[card][player.nickname] = "NA"
            self.information_card[card]["Secret envelope"] = "NA"

    def fill_shown_cards(self, players):
        for player in players:
            if player != self: 
                self.shown_cards[player.nickname] = []


    def update_for_cards_not_in_hand(self):
        for card in self.all_cards:
            if card not in self.cards:
                self.information_card[card][self.nickname] = "NoNA"
        

    def fill_possible_opponent_cards(self, players):
        for player in players:
            if player != self: 
                self.possible_opponent_cards[player.nickname] = []
        self.possible_opponent_cards["Secret envelope"] = []

    def auto_update_information_card(self, card, person):
        for p in self.information_card[card]:
            if p == person:
                self.information_card[card][p] = "Yes"
            else:
                self.information_card[card][p] = "No"


    def add_card(self, card):
        self.cards.append(card)
        self.auto_update_information_card(card, self.nickname)


    def check_for_known_cards(self):
        self.known_cards = [[], [], []]
        for card in self.suspects:
            if self.information_card[card]["Secret envelope"] == "No":
                self.known_cards[0].append(card)
            
        for card in self.weapons:
            if self.information_card[card]["Secret envelope"] == "No":
                self.known_cards[1].append(card)

        for card in self.rooms:
            if self.information_card[card]["Secret envelope"] == "No":
                self.known_cards[2].append(card)



    def check_if_card_is_in_envelope2(self, verbose):
        if self.winning_cards[0] == " " or self.winning_cards[1] == " " or self.winning_cards[2] == " ":
            self.check_for_known_cards()
            if len(self.known_cards[0]) == 5 and self.winning_cards[0] == " ":
                for card in self.suspects:
                    if card not in self.known_cards[0]:
                        self.winning_cards[0] = card
                        self.auto_update_information_card(self.winning_cards[0], "Secret envelope")
                        if verbose == 1:
                            print("\n77777777777 The Advanced AI " + self.nickname + " learned that " + card + " is in the Secret Envelope")
                            # self.winning_card_in_envelope(verbose)
                            print()
            if len(self.known_cards[1]) == 5 and self.winning_cards[1] == " ":
                for card in self.weapons:
                    if card not in self.known_cards[1]:
                        self.winning_cards[1] = card
                        self.auto_update_information_card(self.winning_cards[1], "Secret envelope")
                        if verbose == 1:
                            print("\n77777777777 The Advanced AI " + self.nickname + " learned that " + card + " is in the Secret Envelope")
                            # self.winning_card_in_envelope(verbose)
                            print()
            if len(self.known_cards[2]) == 8 and self.winning_cards[2] == " ":
                for card in self.rooms:
                    if card not in self.known_cards[2]:
                        self.winning_cards[2] = card
                        self.auto_update_information_card(self.winning_cards[2], "Secret envelope")
                        if verbose == 1:
                            print("\n77777777777 The Advanced AI " + self.nickname + " learned that " + card + " is in the Secret Envelope")
                            # self.winning_card_in_envelope(verbose)
                            print()
            self.check_for_new_information(verbose)


    # Now simple asking - to do clever asking later
    def make_guess(self, verbose):
        guess = []

        for player_card in self.suspects:
            if self.information_card[player_card]["Secret envelope"] == "Yes":
                guess.append(player_card)
                break
        if len(guess) < 1:
            for player_card in self.suspects:
                if self.information_card[player_card][self.nickname] == "NoNA":
                    guess.append(player_card)
                    break

        for weapon_card in self.weapons:
            if self.information_card[weapon_card]["Secret envelope"] == "Yes":
                guess.append(weapon_card)
                break
        if len(guess) < 2:
            for weapon_card in self.weapons:
                if self.information_card[weapon_card][self.nickname] == "NoNA":
                    guess.append(weapon_card)
                    break
        
        guess.append(self.current_room.name)

        if verbose == 1:
            print()
            print(self.nickname+"'s guess:")
            print()
            print("Person: " + guess[0])
            print("Weapon: " + guess[1])
            print("Place: " + self.current_room.name)

        return guess

    def set_current_room(self, room):
        self.current_room = room

    # movement through the rooms
    def go_to_room(self, verbose):
        for room in self.current_room.neighbours:
            if self.information_card[room.name]["Secret envelope"] == "Yes":
                next_room = room
                if self.current_room == next_room and verbose == 1:
                    print(self.nickname + " stays at " + self.current_room.name)
                else:
                    self.current_room = room
                    if verbose == 1:
                        print(self.nickname + " goes to " + self.current_room.name)
                return
            else:
                if self.information_card[room.name][self.nickname] == "NoNA":
                    next_room = room
                    if self.current_room == next_room and verbose == 1:
                        print(self.nickname + " stays at " + self.current_room.name)
                    else:
                        self.current_room = room
                        if verbose == 1:
                            print(self.nickname + " goes to " + self.current_room.name)
                    return

        for room in self.current_room.neighbours:
            for adj in room.neighbours:
                if self.information_card[adj.name]["Secret envelope"] == "Yes":
                    self.current_room = room
                    if verbose == 1:
                        print(self.nickname + " goes to " + self.current_room.name)
                    return
                else:
                    if self.information_card[adj.name][self.nickname] == "NoNA":
                        self.current_room = room
                        if verbose == 1:
                            print(self.nickname + " goes to " + self.current_room.name)
                        return

        for room in self.current_room.neighbours:
            for adj1 in room.neighbours:
                for adj2 in adj1.neighbours:
                    if self.information_card[adj2.name]["Secret envelope"] == "Yes":
                        self.current_room = room
                        if verbose == 1:
                            print(self.nickname + " goes to " + self.current_room.name)
                        return
                    else:
                        if self.information_card[adj2.name][self.nickname] == "NoNA":
                            self.current_room = room
                            if verbose == 1:
                                print(self.nickname + " goes to " + self.current_room.name)
                            return

        

    def check_if_card_is_in_envelope(self, card, verbose):
        if card not in self.winning_cards:
            if self.information_card[card][self.nickname] == "NoNA" and self.information_card[card]['Secret envelope'] == "NA":
                counter = 0
                for player in self.neighbours:
                    if self.information_card[card][player.nickname] == "No":
                        counter += 1
                if counter == len(self.neighbours):
                    self.auto_update_information_card(card, "Secret envelope")
                    if verbose == 1:
                        print("\n!!!!!!!!! The Advanced AI " + self.nickname + " learned that " + card + " is in the Secret Envelope")
                        # self.winning_card_in_envelope(verbose)
                    if card in self.suspects and self.winning_cards[0] == " ":
                        self.winning_cards[0] = card
                    elif card in self.weapons and self.winning_cards[1] == " ":
                        self.winning_cards[1] = card
                    elif card in self.rooms and self.winning_cards[2] == " ":
                        self.winning_cards[2] = card
                # self.winning_card_in_envelope(verbose)
                self.check_for_new_information(verbose)

    def winning_card_in_envelope(self, verbose):
        if self.winning_cards[0] != " " or self.winning_cards[1] != " " or self.winning_cards[2] != " ":
            for card in self.winning_cards:
                if card != " ":
                    self.auto_update_information_card(card, "Secret envelope")
            self.check_for_new_information(verbose)

    
    # Use player.nickname or "Secret Envelope"
    def card_in_player(self, card):
        for nickname in self.information_card[card].keys():
            if self.information_card[card][nickname] == "Yes":
                return True
        return False


    # Strategies - see Adv. AI strategies.txt

    # 4. When sb asks for 3 cards and sb cannot disprove
    def no_cards_in_person(self, nickname, guess, verbose):
        guess_new = []
        if nickname != self.nickname:
            for card in guess:
                if self.information_card[card][nickname] == "NA":
                    self.information_card[card][nickname] = "No"
                    guess_new.append(card)
            if len(guess_new) > 0:
                if verbose == 1:
                    print("\nThe Advanced AI " + self.nickname + " learned that " + nickname + " has none of the cards " + str(guess_new))
            self.check_for_new_information(verbose)

    # 1 and 2 - 2 known cards in sb's guess
    def two_cards_that_are_known(self, nickname, guess, verbose):
        if self.nickname != nickname:
            if not (self.card_in_player(guess[0]) and self.card_in_player(guess[1]) and self.card_in_player(guess[2])):
                if self.card_in_player(guess[0]) and self.card_in_player(guess[1]):
                    if self.information_card[guess[0]][nickname] != "Yes" and self.information_card[guess[1]][nickname] != "Yes":
                        self.auto_update_information_card(guess[2], nickname)
                        if verbose == 1:
                            print("\n------- The Advanced AI " + self.nickname + " learned that " + nickname + " has " + guess[2])
                elif self.card_in_player(guess[0]) and self.card_in_player(guess[2]):
                    if self.information_card[guess[0]][nickname] != "Yes" and self.information_card[guess[2]][nickname] != "Yes":
                        self.auto_update_information_card(guess[1], nickname)
                        if verbose == 1:
                            print("\n------- The Advanced AI " + self.nickname + " learned that " + nickname + " has " + guess[1])
                elif self.card_in_player(guess[1]) and self.card_in_player(guess[2]):
                    if self.information_card[guess[1]][nickname] != "Yes" and self.information_card[guess[2]][nickname] != "Yes":
                        self.auto_update_information_card(guess[0], nickname)
                        if verbose == 1:
                            print("\n------- The Advanced AI " + self.nickname + " learned that " + nickname + " has " + guess[0])
                # print()
                self.check_for_new_information(verbose)

    # Strategy 3
    def one_known_card_deduction(self, nickname, guess, verbose):
        if self.nickname != nickname:
            if self.card_in_player(guess[0]) and not self.card_in_player(guess[1]) and not self.card_in_player(guess[2]):
                if self.information_card[guess[0]][nickname] != "Yes":
                    if [guess[1], guess[2]] not in self.possible_opponent_cards[nickname]:
                        self.possible_opponent_cards[nickname].append([guess[1], guess[2]])
                        if verbose == 1:
                            print("\n0000000 The Advanced AI " + self.nickname + " learned that " + nickname + " has either " + guess[1] + " or " + guess[2])
            if self.card_in_player(guess[1]) and not self.card_in_player(guess[0]) and not self.card_in_player(guess[2]):
                if self.information_card[guess[1]][nickname] != "Yes":
                    if [guess[0], guess[2]] not in self.possible_opponent_cards[nickname]:
                        self.possible_opponent_cards[nickname].append([guess[0], guess[2]])
                        if verbose == 1:
                            print("\n0000000 The Advanced AI " + self.nickname + " learned that " + nickname + " has either " + guess[0] + " or " + guess[2])
            if self.card_in_player(guess[2]) and not self.card_in_player(guess[0]) and not self.card_in_player(guess[1]):
                if self.information_card[guess[2]][nickname] != "Yes":
                    if [guess[0], guess[1]] not in self.possible_opponent_cards[nickname]:
                        self.possible_opponent_cards[nickname].append([guess[0], guess[1]])
                        if verbose == 1:
                            print("\n0000000 The Advanced AI " + self.nickname + " learned that " + nickname + " has either " + guess[0] + " or " + guess[1])
            # print()
            self.check_for_new_information(verbose)

    
    def check_for_new_information(self, verbose):
        for nickname in self.possible_opponent_cards.keys():
            if len(self.possible_opponent_cards[nickname]) > 0:
                for pair in self.possible_opponent_cards[nickname]:
                    if self.information_card[pair[0]][nickname] == "No":
                        if self.information_card[pair[1]][nickname] != "Yes":
                            self.information_card[pair[1]][nickname] == "Yes"  
                            self.auto_update_information_card(pair[1], nickname)
                            if verbose == 1:
                                print("\n454545454545 The Advanced AI " + self.nickname + " learned that " + nickname + " has " + pair[1])
                        self.possible_opponent_cards[nickname].remove(pair)
                        # if verbose == 1:
                        #     print("\n++++++++ Removed the pair ++++++++\n")
                        #     print("Possible opponent cards: " + str(self.possible_opponent_cards))
                    elif self.information_card[pair[1]][nickname] == "No":
                        if self.information_card[pair[0]][nickname] != "Yes":
                            self.information_card[pair[0]][nickname] == "Yes"  
                            self.auto_update_information_card(pair[0], nickname)
                            if verbose == 1:
                                print("\n454545454545 The Advanced AI " + self.nickname + " learned that " + nickname + " has " + pair[0])
                        self.possible_opponent_cards[nickname].remove(pair)
                        # if verbose == 1:
                        #     print("\n++++++++ Removed the pair ++++++++\n")
                        #     print("Possible opponent cards: " + str(self.possible_opponent_cards))


    def disprove_guess(self, player, guess, verbose):
        # if verbose == 1:
            # print("Shown cards to other players: " + str(self.shown_cards))
        cards_to_disprove = []
        card_to_show = None
        for card in guess:
            if card in self.cards:
                cards_to_disprove.append(card)

        if len(cards_to_disprove) == 0:
            return None, False
        elif len(cards_to_disprove) == 1:
            if cards_to_disprove[0] not in self.shown_cards[player.nickname]:
                self.shown_cards[player.nickname].append(cards_to_disprove[0])
            return cards_to_disprove[0], True
        elif len(cards_to_disprove) > 1:
            if cards_to_disprove[0] in self.shown_cards[player.nickname]:
                return cards_to_disprove[0], True
            if cards_to_disprove[1] in self.shown_cards[player.nickname]:
                return cards_to_disprove[1], True
            if len(cards_to_disprove) == 3:
                if cards_to_disprove[2] in self.shown_cards[player.nickname]:
                    return cards_to_disprove[0], True
            if cards_to_disprove[0] not in self.shown_cards[player.nickname] and cards_to_disprove[1] not in self.shown_cards[player.nickname]:
                self.shown_cards[player.nickname].append(cards_to_disprove[0])
                return cards_to_disprove[0], True

 