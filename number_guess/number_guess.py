import menu
import random

class Game:
    
    def __init__(self):

        self.chance = 0
        self.guesses = []
        self.guess = 0


    def main(self):

        self.welcome()

        while True:

            guess = self.get_guess()
            secret = self.get_secret()

            if guess == secret:
                print("You won!")
                print(f"It took {self.get_chances()} guesses to guess {secret}")
                break
            elif guess != secret:
                if self.get_chances() > 5:
                    print(f"Game Over! The secret was {secret}")
                    break
                else:
                    self.increment_chances()
                    guess = self.get_guess()




    def welcome(self):
        print()
        print('Welcome to Number Guess!')
        print("You'll try to guess a number between 1 and 20.")
        print()


    def get_guess(self):

        while self.guess < 1 or self.guess > 20:
            try:
                self.guess = int(input("Enter a guess between 1 and 20: "))
                if self.guess in self.guesses:
                    print()
                    print(f"You've already guessed {self.guess}!")
                    print(f"Past Guesses: {self.guesses}")
            except ValueError:
                print("You didn't enter a number!")
            break

        self.guesses.append(self.guess)

        return self.guess


    def get_secret(self):

        return random.randint(1, 20)


    def increment_chances(self):

        self.chance += 1


    def get_chances(self):

        return self.chance


if __name__ == "__main__":
    game = Game()
    game.main()