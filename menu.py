import os

def display_menu(username):
    
    username = username
    choice = ""
    choices = ["q"]

    while choice not in choices:
        clear_screen()
        print(f"Hello {username}! Below are the following apps.")
        print("Q to quit")
        choice = input("Press the key to the corresponding app you want, then pess Enter: ").casefold()

    run_app(choice)


def get_username():
    username = input("Enter your name: ")
    return username


def run_app(choice):
    
    if choice == 'q':
        exit()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():

    username = get_username()
    display_menu(username)


if __name__ == "__main__":
    main()