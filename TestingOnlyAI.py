from Game import Game

class TestingOnlyAI:

    def main(self):
        g = Game()
        num = input("\nEnter the number of players (3-6): ")
        while not num.isdigit() or int(num)<3 or int(num)>6:
            print("Incorrect input! Please choose a number between 3 and 6.")
            num = input("Enter the number of players (3-6): ")
        winner = g.test_main(int(num))


test = TestingOnlyAI()
test.main()