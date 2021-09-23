import menu


class Game():

    def __init__(self):
        
        self.guesses = 0
        self.guess = 10
        self.correct = 'n'
        self.low = 0
        self.high = 50


    def main(self):

        self.display_welcome()

        while correct != 'y':
            correct = input(f"Is your guess {self.guess}? [y/n]").lower()
            
            if correct == 'y':
                break
            elif correct == 'n':
                high_low = self.check_high_low()

                if high_low == 'h':
                    pass
                else:
                    pass
            


    def display_welcome(self):

        print("Welcome to Number Guess AI Edition!")
        print("Think of a number between 1 and 50 (don't tell me!")
        print("I will try to guess it. Just tell me if it's higher, lower, or if I got it!")


    def check_high_low(self):

        high_low = ''
        options = ('h', 'l')
        while high_low not in options:
            high_low = input(f"Is your guess higher or lower than {self.guess}? [h/l] ").lower()

        return high_low


    def increase_guess(self, number):

        self.set_low(number)

        return (self.get_high() - self.get_low()) // 2

    
    def decrease_guess(self, number):

        self.set_high(number)

        return (self.get_high() - self.get_low()) // 2

    
    def get_guess(self):

        return self.guess

    
    def set_guess(self, number):

        self.guess = number


    def set_high(self, number):
    
        self.high = number


    def set_low(self, number):

        self.low = number


    def get_high(self):

        return self.high


    def get_low(self):

        return self.low


if __name__ == "__main__":

    game = Game()
    game.main()