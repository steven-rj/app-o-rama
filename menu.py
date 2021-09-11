import os
from phrase_hunter import game as phrase_hunt

def display_menu():
    
    choice = ""
    choices = ['q', '1']

    while choice not in choices:
        clear_screen()
        print(f"Below are the following apps.")
        print("Q to quit")
        print('1 for Phrase Hunter')
        choice = input("Press the key to the corresponding app you want, then pess Enter: ").casefold()

    run_app(choice)


def get_username():
    
    username = input("Enter your name: ")
    return username


def run_app(choice):
    
    if choice == 'q':
        exit()
    elif choice == '1':
        phrase_hunter = phrase_hunt.Game()
        phrase_hunter.start()


def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')


def main():

    clear_screen()
    display_menu()


if __name__ == "__main__":
    main()
    