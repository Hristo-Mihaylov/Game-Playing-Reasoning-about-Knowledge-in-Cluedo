from Room import Room
from Player import Player
from User import User
from Utils import Utils
from AdvancedAI import AdvancedAI
from RandomAI import RandomAI
import random
import time


class Game:

    def __init__(self):
        self.rounds = 0
        self.current_player = None
        self.secret_envelope = []
        self.game_over = False
        self.all_cards_1 = ["Colonel Mustard", "Professor Plum", "Reverend Green", "Mrs. Peacock", "Miss Scarlett", "Mrs. White", "Dagger",
                          "Candlestick", "Revolver", "Rope", "Lead piping", "Spanner", "Hall", "Lounge", "Library", "Kitchen", "Billiard Room", "Study", "Ballroom", "Conservatory", "Dining Room"]
        self.all_cards = ["Colonel Mustard", "Professor Plum", "Reverend Green", "Mrs. Peacock", "Miss Scarlett", "Mrs. White", "Dagger",
                          "Candlestick", "Revolver", "Rope", "Lead piping", "Spanner", "Hall", "Lounge", "Library", "Kitchen", "Billiard Room", "Study", "Ballroom", "Conservatory", "Dining Room"]
        self.suspects = ["Colonel Mustard", "Professor Plum",
                         "Reverend Green", "Mrs. Peacock", "Miss Scarlett", "Mrs. White"]
        self.weapons = ["Dagger", "Candlestick",
                        "Revolver", "Rope", "Lead piping", "Spanner"]
        self.rooms = ["Hall", "Lounge", "Library", "Kitchen",
                      "Billiard Room", "Study", "Ballroom", "Conservatory", "Dining Room"]

        self.labels = Utils()

    def initialize_players(self):
        inp = input("Enter the number of players (3-6): ")
        while not inp.isdigit() or int(inp)<3 or int(inp)>6:
            print("Incorrect input! Please choose a number between 3 and 6.")
            inp = input("Enter the number of players (3-6): ")
        print()
        print("The game will be played by " + str(inp) + " players!")
        time.sleep(2)

        input_name = input("\nYou are player 1! Please choose a nickname: ")
        while input_name in ["Hristo", "Iva", "Ivaylo", "Kamen", "Boris"]:
            input_name = input("This nickname is reserved for the AIs. Please choose another nickname: ")

        self.player1 = User(input_name)
        print("\nWelcome, " + input_name + "!")

        time.sleep(2)
        print("\nLet's intriduce the other players...")
        time.sleep(2)

        self.player2 = Player("Iva")
        self.player3 = AdvancedAI("Hristo")
        self.players = [self.player1, self.player2, self.player3]
        if int(inp) >= 4:
            self.player4 = RandomAI("Kamen")
            self.players.append(self.player4)
        if int(inp) >= 5:
            self.player5 = Player("Ivaylo")
            self.players.append(self.player5)
        if int(inp) >= 6:
            self.player6 = RandomAI("Peter")
            self.players.append(self.player6)

        for player in self.players:
            if isinstance(player, RandomAI):
                print("\n" + player.nickname + " is a Random AI player.")
                time.sleep(2)
            elif isinstance(player, Player) and not isinstance(player, User):
                print("\n" + player.nickname + " is a Medium level AI player.")
                time.sleep(2)
            elif isinstance(player, AdvancedAI):
                print("\n" + player.nickname + " is an Advanced AI player.")
                time.sleep(2)
        print("\n------------------------------------------------------------------\n")

        for player in self.players:
            player.neighbours = []
            for p in self.players:
                if self.players.index(p) > self.players.index(player):
                    player.neighbours.append(p)
            for p in self.players:
                if self.players.index(p) < self.players.index(player):
                    player.neighbours.append(p)
        
        for player in self.players:
            if isinstance(player, AdvancedAI):
                player.fill_possible_opponent_cards(self.players)
                player.fill_shown_cards(self.players)

        for player in self.players:
            if isinstance(player, AdvancedAI) or isinstance(player, User):
                player.fill_information_card(self.players)




    def initialize_rooms(self):
        self.kitchen = Room("Kitchen")
        self.ballroom = Room("Ballroom")
        self.conservatory = Room("Conservatory")
        self.billiard_room = Room("Billiard Room")
        self.library = Room("Library")
        self.study = Room("Study")
        self.hall = Room("Hall")
        self.lounge = Room("Lounge")
        self.dining_room = Room("Dining Room")

        # Normal neighbours
        self.kitchen.set_neighbour(self.ballroom)
        self.ballroom.set_neighbour(self.conservatory)
        self.conservatory.set_neighbour(self.billiard_room)
        self.billiard_room.set_neighbour(self.library)
        self.library.set_neighbour(self.study)
        self.study.set_neighbour(self.hall)
        self.hall.set_neighbour(self.lounge)
        self.lounge.set_neighbour(self.dining_room)
        self.dining_room.set_neighbour(self.kitchen)

        # Secret passages
        self.kitchen.set_secret_passage(self.study)
        self.conservatory.set_secret_passage(self.lounge)

        self.all_rooms = [self.kitchen, self.ballroom, self.conservatory, self.billiard_room, self.library, self.study, self.hall, self.lounge, self.dining_room]
        self.all_rooms_copy = [self.kitchen, self.ballroom, self.conservatory, self.billiard_room, self.library, self.study, self.hall, self.lounge, self.dining_room]

        for room in self.all_rooms:
            random.shuffle(room.neighbours)
            

    def distribute_rooms(self):
        print()
        print("The players are now randomly placed in the following rooms:\n")
        time.sleep(3)
        for player in self.players:
            room = random.choice(self.all_rooms_copy)
            player.set_current_room(room)
            self.all_rooms_copy.remove(room)
            print(player.nickname + ": " + player.current_room.name)
            time.sleep(1)

    def distribute_rooms_test(self):
        # print()
        # print("The players are now randomly placed in the following rooms:")
        for player in self.players:
            room = random.choice(self.all_rooms_copy)
            player.set_current_room(room)
            self.all_rooms_copy.remove(room)
            # print(player.nickname + ": " + player.current_room.name)


    def distribute_cards(self):
        card1 = random.choice(self.all_cards[0:6])
        self.secret_envelope.append(card1)
        card2 = random.choice(self.all_cards[6:12])
        self.secret_envelope.append(card2)
        card3 = random.choice(self.all_cards[12:])
        self.secret_envelope.append(card3)
        self.all_cards.remove(card1)
        self.all_cards.remove(card2)
        self.all_cards.remove(card3)
        # print("\nSecret envelope: " + str(self.secret_envelope) + "\n")

        self.distribute_cards_players()

    def distribute_cards_players(self):
        leftover = len(self.all_cards) % len(self.players)
        r = int(len(self.all_cards)/len(self.players))

        for i in range(r):
            for player in self.players:
                player.add_card(random.choice(self.all_cards))
                self.all_cards.remove(player.cards[-1])

        if leftover != 0:
            rep = []
            while leftover != 0:
                i = random.randint(0, len(self.players)-1)
                while i in rep:
                    i = random.randint(0, len(self.players)-1)
                rep.append(i)

                self.players[i].add_card(random.choice(self.all_cards))
                self.all_cards.remove(self.players[i].cards[-1])
                leftover -= 1

        for player in self.players:
            if isinstance(player, AdvancedAI) or isinstance(player, User):
                player.update_for_cards_not_in_hand()


        print("\nCards are distributed... ")
        time.sleep(3)
        for player in self.players:
            if isinstance(player, User):
                print()
                print(player.nickname + " has the following cards: " + str(player.cards))
                time.sleep(2)
            
    def intro(self):
        # self.labels.print_beginning()
        # time.sleep(2)
        self.labels.print_room_map()
        time.sleep(3)
        self.initialize_players()
        self.distribute_cards()
        time.sleep(2)
        self.initialize_rooms()
        self.distribute_rooms()
        time.sleep(2)


    def main(self):
        
        self.intro()

        while not self.game_over:
            self.rounds += 1
            print("\n------------------------------------------------------------------")
            print("\nROUND " + str(self.rounds))
            print("\n------------------------------------------------------------------")
            print()
            time.sleep(2)
            self.current_player = self.players[(
                self.rounds-1) % len(self.players)]

            if isinstance(self.current_player, User):
                self.labels.print_room_map()
                time.sleep(3)
                print()
            
            if isinstance(self.current_player, User):
                print(self.current_player.nickname + "'s cards: " + str(self.current_player.cards))
                print()
                time.sleep(2)
            print(self.current_player.nickname + " is currently at " + self.current_player.current_room.name)
            print()
            time.sleep(1)

            if isinstance(self.current_player, User):
                inp = input("Would you like to view your information card (y/n)? ")
                while inp!='y' and inp!='n':
                    print("\nInvalid input!")
                    inp = input("Would you like to view your information card (y/n)? ")
                if inp == 'y':
                    print("\nYour information card: \n")
                    print(self.current_player.information_card)
                    ent = input("\nPress enter to continue: ")
            
            if self.rounds > len(self.players):
                self.current_player.go_to_room(1)
                time.sleep(2)

            if isinstance(self.current_player, AdvancedAI):
                for card in self.all_cards_1:
                    self.current_player.check_if_card_is_in_envelope(card, 0)
                self.current_player.check_for_known_cards()

            guess = self.current_player.make_guess(1)
            time.sleep(2)

            card = None
            does_disprove = False

            for neighbour in self.current_player.neighbours:

                card, does_disprove = neighbour.disprove_guess(self.current_player, guess, 0)

                if does_disprove == True:

                    if isinstance(self.current_player, User) or isinstance(neighbour, User):
                        print('\n' + neighbour.nickname + " disproves: " + card)
                        time.sleep(2)
                    else:
                        print('\n' + neighbour.nickname + " disproves.")
                        time.sleep(2)

                    
                    if isinstance(self.current_player, AdvancedAI) or isinstance(self.current_player, User):
                        self.current_player.auto_update_information_card(card, neighbour.nickname)
                    else:
                        self.current_player.information_card[card] = False

                    for player in self.players:
                        if isinstance(player, AdvancedAI):
                            player.two_cards_that_are_known(neighbour.nickname, guess, 0)
                            for card in self.all_cards:
                                player.check_if_card_is_in_envelope(card, 0)

                    for player in self.players:
                        if isinstance(player, AdvancedAI):
                            player.one_known_card_deduction(neighbour.nickname, guess, 0)

                    break
                else:
                    print('\n' + neighbour.nickname + " cannot disprove.")
                    time.sleep(2)

                    for player in self.players:
                        if isinstance(player, AdvancedAI):
                            player.no_cards_in_person(neighbour.nickname, guess, 0)

            if not does_disprove:
                print("\nNobody can disprove your claim!")
                time.sleep(2)
                if isinstance(self.current_player, RandomAI) and (self.current_player.information_card[guess[0]] == True and self.current_player.information_card[guess[1]] == True and self.current_player.information_card[guess[2]] == True):
                    print("\n" + self.current_player.nickname + " makes an accusation: " + str(guess))
                    time.sleep(2)
                    if guess == self.secret_envelope:
                        print('\n' + self.current_player.nickname + " wins!")
                        self.current_player.has_won = True
                        self.game_over = True
                        winner_ = self.current_player
                        break
                    else:
                        print('\n' + self.current_player.nickname + " loses!")
                        time.sleep(2)
                        self.players.remove(self.current_player)

                if isinstance(self.current_player, Player) and not isinstance(self.current_player, User) and (self.current_player.information_card[guess[0]] == True and self.current_player.information_card[guess[1]] == True and self.current_player.information_card[guess[2]] == True):
                    print("\n" + self.current_player.nickname + " makes an accusation: " + str(guess))
                    time.sleep(2)
                    if guess == self.secret_envelope:
                        print('\n' + self.current_player.nickname + " wins!")
                        self.current_player.has_won = True
                        self.game_over = True
                        winner_ = self.current_player
                        break
                    else:
                        print('\n' + self.current_player.nickname + " loses!")
                        time.sleep(2)
                        self.players.remove(self.current_player)

            for player in self.players:
                if isinstance(player, AdvancedAI):
                    for card in self.all_cards_1:
                        player.check_if_card_is_in_envelope(card, 0)
                    player.check_if_card_is_in_envelope2(0)



            if isinstance(self.current_player, AdvancedAI):
                if self.current_player.winning_cards[0] != " " and self.current_player.winning_cards[1] != " " and self.current_player.winning_cards[2] != " ":
                    print("\n" + self.current_player.nickname + " makes an accusation: " + str(self.current_player.winning_cards))
                    time.sleep(2)
                    if self.current_player.winning_cards == self.secret_envelope:
                        print('\n' + self.current_player.nickname + " wins!")
                        self.current_player.has_won = True
                        self.game_over = True
                        winner_ = self.current_player
                        break
                    else:
                        print('\n' + self.current_player.nickname + " loses!")
                        time.sleep(2)
                        self.players.remove(self.current_player)

                
            if isinstance(self.current_player, User):
                inp = input("\nWould you like to make an accusation (y/n)? ")
                while inp!="y" and inp!="n":
                    print("Invalid input!")
                    inp = input("Would you like to make an accusation (y/n)? ")
                if inp == "y":
                    guess = self.current_player.make_guess(1)
                    print("\n" + self.current_player.nickname + " makes an accusation: " + str(guess))
                    time.sleep(2)
                    if guess == self.secret_envelope:
                        print('\n' + self.current_player.nickname + " wins!")
                        self.current_player.has_won = True
                        self.game_over = True
                        break
                    else:
                        print('\n' + self.current_player.nickname + " loses!")
                        time.sleep(2)
                        self.players.remove(self.current_player)

            

            time.sleep(1)
            enter = input("\nPress enter to continue:")




# -----------------------------METHODS FOR AI ONLY!!!------------------------------------------------------------------------------------------------------------------------

    def distribute_cards_test(self, verbose):
            card1 = random.choice(self.all_cards[0:6])
            self.secret_envelope.append(card1)
            card2 = random.choice(self.all_cards[6:12])
            self.secret_envelope.append(card2)
            card3 = random.choice(self.all_cards[12:])
            self.secret_envelope.append(card3)
            self.all_cards.remove(card1)
            self.all_cards.remove(card2)
            self.all_cards.remove(card3)

            if verbose == 1:
                print("Cards are being distributed... ")
                time.sleep(3)
                print("\nSecret envelope: " + str(self.secret_envelope) + "\n")

            self.distribute_cards_players_test(verbose)

    def distribute_cards_players_test(self, verbose):
        leftover = len(self.all_cards) % len(self.players)
        r = int(len(self.all_cards)/len(self.players))

        for i in range(r):
            for player in self.players:
                player.add_card(random.choice(self.all_cards))
                self.all_cards.remove(player.cards[-1])

        if leftover != 0:
            rep = []
            while leftover != 0:
                i = random.randint(0, len(self.players)-1)
                while i in rep:
                    i = random.randint(0, len(self.players)-1)
                rep.append(i)

                self.players[i].add_card(random.choice(self.all_cards))
                self.all_cards.remove(self.players[i].cards[-1])
                leftover -= 1

        for player in self.players:
            if isinstance(player, AdvancedAI):
                player.update_for_cards_not_in_hand()


        if verbose == 1:
            for player in self.players:
                print(player.nickname + ": " + str(player.cards))

    def initialize_players_test(self, inp, verbose):

        self.player3 = Player("Boris")
        self.player1 = AdvancedAI("Hristo")
        self.player2 = Player("Kamen")
        self.players = [self.player1, self.player2, self.player3]
        if inp >= 4:
            self.player4 = RandomAI("Iva")
            self.players.append(self.player4)
        if inp >= 5:
            self.player5 = Player("Ivaylo")
            self.players.append(self.player5)
        if inp >= 6:
            self.player6 = RandomAI("Pesho")
            self.players.append(self.player6)

        if verbose == 1:
            print("\nLet's introduce the AI players...")
            time.sleep(2)
            for player in self.players:
                if isinstance(player, RandomAI):
                    print("\n" + player.nickname + " is a Random AI player.")
                    time.sleep(2)
                elif isinstance(player, Player):
                    print("\n" + player.nickname + " is a Medium level AI player.")
                    time.sleep(2)
                elif isinstance(player, AdvancedAI):
                    print("\n" + player.nickname + " is an Advanced AI player.")
                    time.sleep(2)
            print("\n------------------------------------------------------------------\n")

        for player in self.players:
            player.neighbours = []
            for p in self.players:
                if self.players.index(p) > self.players.index(player):
                    player.neighbours.append(p)
            for p in self.players:
                if self.players.index(p) < self.players.index(player):
                    player.neighbours.append(p)
        
        for player in self.players:
            if isinstance(player, AdvancedAI):
                player.fill_information_card(self.players)
                player.fill_possible_opponent_cards(self.players)
                player.fill_shown_cards(self.players)

    def test_main(self, inp):

        # self.labels.print_beginning()
        # time.sleep(2)
        self.labels.print_room_map()
        time.sleep(2)

        print()
        print("The game will be played by " + str(inp) + " players.\n")
        self.initialize_players_test(inp, 1)
        time.sleep(2)
        self.distribute_cards_test(1)
        time.sleep(2)
        self.initialize_rooms()
        
        self.distribute_rooms()
        time.sleep(2)
        
        while not self.game_over:
            self.rounds += 1
            print("\n------------------------------------------------------------------")
            print("\nROUND " + str(self.rounds))
            print("\n------------------------------------------------------------------")
            print()
            time.sleep(2)
            self.labels.print_room_map()
            self.current_player = self.players[(
                self.rounds-1) % len(self.players)]

            print("Secret Envelope: " + str(self.secret_envelope))
            print()
            print(self.current_player.nickname + "'s cards: " + str(self.current_player.cards))
            print()
            time.sleep(2)


            # if isinstance(self.current_player, AdvancedAI):
            #     print(self.current_player.nickname + "'s information card:")
            #     print(self.current_player.information_card)
            #     print()


            print(self.current_player.nickname + " is currently at " + self.current_player.current_room.name)
            print()
            time.sleep(2)
            
            if self.rounds > len(self.players):
                self.current_player.go_to_room(1)
                time.sleep(2)

            if isinstance(self.current_player, AdvancedAI):
                for card in self.all_cards_1:
                    self.current_player.check_if_card_is_in_envelope(card, 1)
                self.current_player.check_for_known_cards()
                # print("Known cards: " + str(self.current_player.known_cards))
                # print("Winning cards: " + str(self.current_player.winning_cards))

            guess = self.current_player.make_guess(1)
            time.sleep(2)

            card = None
            does_disprove = False

            

            for neighbour in self.current_player.neighbours:

                card, does_disprove = neighbour.disprove_guess(self.current_player, guess, 0)

                if does_disprove == True:

                    print('\n' + neighbour.nickname + " disproves: " + card)
                    time.sleep(2)

                    if isinstance(self.current_player, AdvancedAI):
                        self.current_player.auto_update_information_card(card, neighbour.nickname)
                    else:
                        self.current_player.information_card[card] = False

                    for player in self.players:
                        if isinstance(player, AdvancedAI):
                            player.two_cards_that_are_known(neighbour.nickname, guess, 1)
                            for card in self.all_cards:
                                player.check_if_card_is_in_envelope(card, 1)
                    

                    for player in self.players:
                        if isinstance(player, AdvancedAI):
                            player.one_known_card_deduction(neighbour.nickname, guess, 1)

                    # used to be here!
                    break
                else:
                    print('\n' + neighbour.nickname + " cannot disprove.")
                    time.sleep(2)

                    for player in self.players:
                        if isinstance(player, AdvancedAI):
                            player.no_cards_in_person(neighbour.nickname, guess, 1)


            if not does_disprove:
                print("\nNobody can disprove the claim!")
                time.sleep(2)
                if isinstance(self.current_player, RandomAI) and (self.current_player.information_card[guess[0]] == True and self.current_player.information_card[guess[1]] == True and self.current_player.information_card[guess[2]] == True):
                    print("\n" + self.current_player.nickname + " makes an accusation: " + str(guess))
                    time.sleep(2)
                    if guess == self.secret_envelope:
                        print('\n' + self.current_player.nickname + " wins!")
                        self.current_player.has_won = True
                        self.game_over = True
                        winner_ = self.current_player
                        break
                    else:
                        print('\n' + self.current_player.nickname + " loses!")
                        time.sleep(2)
                        self.players.remove(self.current_player)

                if isinstance(self.current_player, Player) and (self.current_player.information_card[guess[0]] == True and self.current_player.information_card[guess[1]] == True and self.current_player.information_card[guess[2]] == True):
                    print("\n" + self.current_player.nickname + " makes an accusation: " + str(guess))
                    time.sleep(2)
                    if guess == self.secret_envelope:
                        print('\n' + self.current_player.nickname + " wins!")
                        self.current_player.has_won = True
                        self.game_over = True
                        winner_ = self.current_player
                        break
                    else:
                        print('\n' + self.current_player.nickname + " loses!")
                        time.sleep(2)
                        self.players.remove(self.current_player)
            

            for player in self.players:
                if isinstance(player, AdvancedAI):
                    for card in self.all_cards_1:
                        player.check_if_card_is_in_envelope(card, 1)
                    player.check_if_card_is_in_envelope2(1)
                    print("\nWinning cards for " + player.nickname + ": " + str(player.winning_cards))
                    player.winning_card_in_envelope(1)
                    print("Possible opponent cards for Advanced AI " + player.nickname + "'s opponents: " + str(player.possible_opponent_cards))
                    print("Known cards for " + player.nickname + ": " + str(player.known_cards))
                    print()
                    time.sleep(2)


            if isinstance(self.current_player, AdvancedAI):
                if self.current_player.winning_cards[0] != " " and self.current_player.winning_cards[1] != " " and self.current_player.winning_cards[2] != " ":
                    print("\n" + self.current_player.nickname + " makes an accusation: " + str(self.current_player.winning_cards))
                    time.sleep(2)
                    if self.current_player.winning_cards == self.secret_envelope:
                        print('\n' + self.current_player.nickname + " wins!")
                        self.current_player.has_won = True
                        self.game_over = True
                        winner_ = self.current_player
                        break
                    else:
                        print('\n' + self.current_player.nickname + " loses!")
                        time.sleep(1)
                        self.players.remove(self.current_player)

            enter = input("Press enter to continue:")

        return winner_










# ------------------------------- main method for multiple games -------------------------------------------


    def test_main_multiple(self, inp):

        self.initialize_players_test(inp, 0)
        self.distribute_cards_test(0)
        
        self.initialize_rooms()
        
        self.distribute_rooms_test()
        
        while not self.game_over:
            self.rounds += 1
            self.current_player = self.players[(
                self.rounds-1) % len(self.players)]

            if self.rounds > len(self.players):
                self.current_player.go_to_room(0)

            if isinstance(self.current_player, AdvancedAI):
                for card in self.all_cards_1:
                    self.current_player.check_if_card_is_in_envelope(card, 0)
                self.current_player.check_for_known_cards()

            guess = self.current_player.make_guess(0)

            card = None
            does_disprove = False

            

            for neighbour in self.current_player.neighbours:

                if isinstance(neighbour, AdvancedAI):

                    card, does_disprove = neighbour.disprove_guess(
                        self.current_player, guess, 0)
                
                else:
                    card, does_disprove = neighbour.disprove_guess(
                        self.current_player, guess, 0)

                if does_disprove == True:
                    if isinstance(self.current_player, AdvancedAI):
                        self.current_player.auto_update_information_card(card, neighbour.nickname)
                    else:
                        self.current_player.information_card[card] = False

                    for player in self.players:
                        if isinstance(player, AdvancedAI):
                            player.two_cards_that_are_known(neighbour.nickname, guess, 0)
                            for card in self.all_cards:
                                player.check_if_card_is_in_envelope(card, 0)

                    for player in self.players:
                        if isinstance(player, AdvancedAI):
                            player.one_known_card_deduction(neighbour.nickname, guess, 0)
                    break
                else:
                    for player in self.players:
                        if isinstance(player, AdvancedAI):
                            player.no_cards_in_person(neighbour.nickname, guess, 0)


            if not does_disprove:
                if isinstance(self.current_player, RandomAI) and (self.current_player.information_card[guess[0]] == True and self.current_player.information_card[guess[1]] == True and self.current_player.information_card[guess[2]] == True):
                    if guess == self.secret_envelope:
                        self.current_player.has_won = True
                        self.game_over = True
                        winner_ = self.current_player
                        break
                    else:
                        self.players.remove(self.current_player)

                if isinstance(self.current_player, Player) and (self.current_player.information_card[guess[0]] == True and self.current_player.information_card[guess[1]] == True and self.current_player.information_card[guess[2]] == True):
                    if guess == self.secret_envelope:
                        self.current_player.has_won = True
                        self.game_over = True
                        winner_ = self.current_player
                        break
                    else:
                        self.players.remove(self.current_player)

            

            for player in self.players:
                if isinstance(player, AdvancedAI):
                    
                    for card in self.all_cards_1:
                        player.check_if_card_is_in_envelope(card, 0)
                    player.check_if_card_is_in_envelope2(0)
                    player.winning_card_in_envelope(0)
                    


            if isinstance(self.current_player, AdvancedAI):
                if self.current_player.winning_cards[0] != " " and self.current_player.winning_cards[1] != " " and self.current_player.winning_cards[2] != " ":
                    if self.current_player.winning_cards == self.secret_envelope:
                        self.current_player.has_won = True
                        self.game_over = True
                        winner_ = self.current_player
                        break
                    else:
                        self.players.remove(self.current_player)

                
            # if isinstance(self.current_player, Player):
            #     if guess == self.secret_envelope:
                    
            #         self.current_player.has_won = True
            #         self.game_over = True
            #         winner_ = self.current_player
            #         break

        return winner_
