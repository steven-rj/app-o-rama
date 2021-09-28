import os
from phrase_hunter import game as phrase_hunt
from number_guess import number_guess
from number_guess_ai import number_guess_ai

def display_menu():
    """
    Displays menu for games.
    Gets string input for selection from user, sends to run_app()
    """
    choice = ""
    choices = ['q', '1', '2', '3']

    while choice not in choices:
        clear_screen()
        print("Welcome to App-o-Rama!!")
        print(f"Below are the following apps.")
        print("Q to quit")
        print('1 for Phrase Hunter')
        print('2 for Number Guess')
        print('3 for Number Gues AI Edition')
        print()
        choice = input("Press the key to the corresponding app you want, then pess Enter: ").casefold()

    run_app(choice)


def run_app(choice):
    """
    Gets string input from display menu, runs appropriate instance of app
    """
    
    clear_screen()
    if choice == 'q':
        exit()
    elif choice == '1':
        phrase_hunter = phrase_hunt.Game()
        phrase_hunter.start()
    elif choice == '2':
        num_guess = number_guess.Game()
        num_guess.main()
    elif choice == '3':
        num_ai = number_guess_ai.Game()
        num_ai.main()


def clear_screen():
    """
    Clears the terminal window
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """
    Runs display_menu() 
    """
    clear_screen()
    display_menu()


if __name__ == "__main__":
    main()
    