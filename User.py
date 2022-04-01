from Player import Player


class User(Player):

    def __init__(self, nickname):
        Player.__init__(self, nickname)
        self.number_of_players = 0
        self.information_card = {}
        for card in self.all_cards:
            self.information_card[card] = {}

    def fill_information_card(self, players):
        for card in self.all_cards:
            for player in players:
                self.information_card[card][player.nickname] = "NA"
            self.information_card[card]["Secret envelope"] = "NA"
            

    def update_for_cards_not_in_hand(self):
        for card in self.all_cards:
            if card not in self.cards:
                self.information_card[card][self.nickname] = "No"

    def auto_update_information_card(self, card, person):
        for p in self.information_card[card]:
            if p == person:
                self.information_card[card][p] = "Yes"
            else:
                self.information_card[card][p] = "No"

    def add_card(self, card):
        self.cards.append(card)
        self.auto_update_information_card(card, self.nickname)


    def go_to_room(self, verbose = 0):
        inp = input("Would you like to go to another room (y/n)? ")
        while inp != "y" and inp != "n":
            print("Invalid input!")
            inp = input("Would you like to go to another room (y/n)? ")
        if inp == "y":
            available_rooms_names = {}
            available_rooms = {}
            count = 1
            for room in self.current_room.neighbours:
                if room != self.current_room:
                    available_rooms[count] = room
                    available_rooms_names[count] = room.name
                    count += 1

            print()
            print(available_rooms_names)
            inp1 = input("\nPlease choose an index for the room you want to go: ")
            while not inp1.isdigit() or int(inp1)<1 or int(inp1)>len(available_rooms):
                print("Invalid input!")
                inp1 = input("Please choose an index for the room you want to go: ")

            self.current_room = available_rooms[int(inp1)]
            print()
            print(self.nickname + " goes to " + self.current_room.name)

        else:
            print()
            print(self.nickname + " stays at " + self.current_room.name)
            
            

    def make_guess(self, verbose):
        susp = {
            1: "Colonel Mustard",
            2: "Professor Plum",
            3: "Reverend Green",
            4: "Mrs. Peacock",
            5: "Miss Scarlett",
            6: "Mrs. White"
        }
        print()
        print(susp)
        inp = input("\nPlease choose the index of the person you want to guess: ")
        while not inp.isdigit() or int(inp)<1 or int(inp)>6:
            print("Invalid input! Please enter a number between 1 and 6.")
            inp = input("Please choose the index of the person you want to guess: ")
        person = susp[int(inp)]

        weap = {
            1: "Dagger",
            2: "Candlestick",
            3: "Revolver",
            4: "Rope",
            5: "Lead piping",
            6: "Spanner"
        }
        print()
        print(weap)
        inw = input("\nPlease choose the index of the weapon you want to guess: ")
        while not inw.isdigit() or int(inw)<1 or int(inw)>6:
            print("Invalid input! Please enter a number between 1 and 6.")
            inw = input("Please choose the index of the weapon you want to guess: ")
        weapon = weap[int(inw)]

        print()
        print(self.nickname+"'s guess:")
        print()
        print("Person: " + person)
        print("Weapon: " + weapon)
        print("Place: " + self.current_room.name)
        return [person, weapon, self.current_room.name]

    def disprove_guess(self, player, guess, verbose = 0):
        ans = {}
        index = 1
        for card in guess:
            if card in self.cards:
                ans[index] = card
                index += 1

        if ans:
            print("\nCards to disprove:")
            print()
            print(ans)
            inp = input("\nPlease enter the index of the card you want to show: ")
            while not inp.isdigit() or int(inp)<1 or int(inp)>len(ans):
                print("Invalid input!")
                inp = input("Please enter the index of the card you want to show: ")
            return ans[int(inp)], True
        else:
            return None, False
