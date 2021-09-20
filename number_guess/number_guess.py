import random
import menu

class Game:
    
    def __init__(self):

        self.chance = 1
        self.guesses = []
        self.guess = 0


    def main(self):

        self.welcome()

        secret = self.get_secret()
        print(f"DEBUG: secret = {secret}")

        while not self.game_over():

            self.get_guess()

            if self.guess == secret:
                print("You won!")
                print(f"It took {self.get_chances()} guesses to guess {secret}")
                break

            elif self.guess != secret:
                self.increment_chances()
                if self.game_over():
                    print()
                    print(f"Game Over! The secret was {secret}")
                    break
                
                else:
                    print()
                    print(f"Sorry, it isn't {self.guess}!")
                    print(f"Chances left: {5-self.chance}")

        self.replay()


    def welcome(self):
        print()
        print('Welcome to Number Guess!')
        print()
        print("You'll try to guess a number between 1 and 20.")
        print()


    def get_guess(self):

        print()
        self.guess = input("Enter your guess: ")
        while not self.validate_guess():
            print()
            self.guess = input("Enter your guess: ")

        return self.guess


    def validate_guess(self):

        try:
            self.guess = int(self.guess)
        except ValueError:
            print("You didn't enter a number!")
            print()
            return False

        if self.guess > 20:
            print("Your guess must be less than 20")
            print()
            return False

        elif self.guess < 1:
            print("Your guess must be greater than 1")
            print()
            return False

        if self.guess in self.guesses:
            print(f"You already guessed {self.guess}!")
            print(f"Previous guesses: {self.guesses}")
            print()
            return False

        self.guesses.append(self.guess)

        return True


    def get_secret(self):

        return random.randint(1, 20)


    def increment_chances(self):

        self.chance += 1


    def get_chances(self):

        return self.chance


    def game_over(self):

        return self.chance > 5


    def replay(self):

        replay = ""
        while replay != "y" and replay != "n":
            replay = input("\nPlay again? [y/n] >> ").lower()
        
        if replay == "y":
            menu.clear_screen()
            game = Game()
            game.main()
        elif replay == "n":
            menu.main()


if __name__ == "__main__":
    game = Game()
    game.main()