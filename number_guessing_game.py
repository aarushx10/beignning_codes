import random
class NumberGussingGame:
    def __init__(self):
        self.count = 0
        game_iteration = int(input("Enter how many times you want to play game: "))
        for i in range(game_iteration):
            self.userinput = int(input("Guess number between 1 to 10: "))
            computerguess = random.randrange(1,10)
            if self.userinput == computerguess:
                print("You and computer guess the same number")
                self.count = self.count + 1
            else: 
                print(f"You Guess: {self.userinput} Computer Guess: {computerguess}")
    def count_occurence_of_samenumber(self):
        print(f"Occurence of samenumber of your and computer: {self.count}")

if __name__ == "__main__":    
    game = NumberGussingGame()
    game.count_occurence_of_samenumber()
