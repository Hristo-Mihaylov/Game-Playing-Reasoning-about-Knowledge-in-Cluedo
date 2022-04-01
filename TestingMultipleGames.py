from Game import Game
from Room import Room
from Player import Player
from User import User
from Utils import Utils
from AdvancedAI import AdvancedAI
from RandomAI import RandomAI


class TestingMultipleGames:

    def main(self, games):
        num = input("\nEnter the number of players (3-6): ")
        while not num.isdigit() or int(num)<3 or int(num)>6:
            print("Incorrect input! Please choose a number between 3 and 6.")
            num = input("Enter the number of players (3-6): ")

        print("\nTotal games to be played: " + str(games))
        games_won = 0
        for i in range(games):
            g = Game()
            winner = g.test_main_multiple(int(num))
            if isinstance(winner, AdvancedAI):
                games_won += 1
            # if winner.nickname == "Hristo":
            #     games_won += 1

        print("\nTotal games won by the Advanced AI: " + str(games_won))
        # print("\nTotal games won by Hristo: " + str(games_won))
        # print("\nWin rate of Hristo : " + str(games_won*100/games) + " %")
        print("\nWin rate of Advanced AI : " + str(games_won*100/games) + " %")


test = TestingMultipleGames()

test.main(10000)