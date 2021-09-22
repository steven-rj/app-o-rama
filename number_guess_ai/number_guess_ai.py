import menu


class Game():

    def main(self):

        self.display_welcome()



    def display_welcome(self):

        print("Welcome to Number Guess AI Edition!")
        print("Think of a number between 1 and 20 (don't tell me!")
        print("I will try to guess it. Just tell me if it's higher, lower, or if I got it!")

if __name__ == "__main__":

    game = Game()
    game.main()