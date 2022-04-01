from Game import Game
from Room import Room
from Player import Player
from User import User
from Utils import Utils
from AdvancedAI import AdvancedAI
from RandomAI import RandomAI
import time

class Main:

    def main(self):
        g = Game()
        # g.labels.print_beginning()
        g.labels.print_beginning()
        time.sleep(2)
        print('''Welcome to Cluedo!

1. Play a game.
2. Watch different AIs play the game.''')
        inp = input("\nPlease choose an option: ")
        while not inp.isdigit() or int(inp)<1 or int(inp)>2:
            inp = input("\nInvalid input! Please choose an option: ")
        if int(inp) == 1:
            g.main()
        elif int(inp) == 2:
            num = input("\nEnter the number of players (3-6): ")
            while not num.isdigit() or int(num)<3 or int(num)>6:
                print("\nIncorrect input! Please choose a number between 3 and 6.")
                num = input("Enter the number of players (3-6): ")
            winner = g.test_main(int(num))
        

main_game = Main()
main_game.main()
