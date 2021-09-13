import menu
import random


def main():

    print()
    print('Welcome to Number Guess')
    end = int(input("You would like to guess a number between 1 and, what?: "))
    num_chances = int(input("And how many chances would you like?: "))
    chance = 0
    cont = ''

    secret = random.randint(1, end-1)
    guess = 0

    while True:
        
        guess = int(input("Enter a guess: "))
        chance += 1

        if guess == secret:
            print(f"Wow you got it! The secret number was {secret}, which you got in {chance} guesses!")
            break
        elif guess != secret and chance <= num_chances:
            print(f"{guess} was not it!")
            continue
        elif guess != secret and chance >= num_chances:
            print(f"Sorry! The secret number was {secret}")
            break

    while cont != 'n' or 'y':
        cont = input("Press y to play again, n to quit: ").lower()
        if cont == 'y':
            main()
        else:
            menu.display_menu()
