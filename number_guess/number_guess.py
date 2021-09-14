#import menu
import random

class Game:
    
    def __init__(self):

        self.secret = random.randint(1, 20)
        self.chance = 0
        self.guesses = []

    def main(self):

        self.welcome()

        while True:

            guess = self.get_guess()
            if guess == 2:
                print("You won!")
            break

    def welcome(self):
        print()
        print('Welcome to Number Guess!')
        print("You'll try to guess a number between 1 and 20.")
        print()

    def get_guess(self):

        guess = 0

        while guess < 1 or guess > 20:
            try:
                guess = int(input("Enter a guess between 1 and 20: "))
                if guess in self.guesses:
                    print()
                    print(f"You've already guessed {guess}!")
                    print(f"Past Guesses: {self.guesses}")
            except ValueError:
                print("You didn't enter a number!")

        return guess


if __name__ == "__main__":
    game = Game()
    game.main()