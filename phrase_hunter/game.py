import random
import sys
import menu

from .phrase import Phrase

class Game:

    def __init__(self):

        self.missed = 0
        self.phrases = [ 
        {"Disney Songs": [Phrase("A Girl Worth Fighting For"), Phrase("Out There"),
        Phrase("I Just Cant Wait To Be King"), Phrase("Youve Got a Friend in Me"), 
        Phrase("I See the Light"), Phrase("Derezzed"), Phrase("This is Halloween"),
        Phrase("Poor Unfortunate Souls"), Phrase("You Can Fly"), Phrase("Friend Like Me"),
        Phrase("The Bare Necessities"), Phrase("Youre Welcome"), Phrase("Colors of the Wind"), Phrase("Un Poco Loco"),
        Phrase("Circle of Life"), Phrase("Hakuna Matata"), Phrase("Bibbidi Bobbidi Boo"), Phrase("Part of Your World"),
        Phrase("Supercalifragilisticexpialidocious"), Phrase("A Place Called Slaughter Race"),
        Phrase("Be Prepared"), Phrase("Reflection"), Phrase("Part of Your World"), Phrase("When You Wish Upon A Star"),
        Phrase("A Guy Like You"), Phrase("Thats What Friends Are For"), Phrase("Whistle While You Work"), 
        Phrase("Hi Diddle Dee Dee"), Phrase("Pink Elephants on Parade"), Phrase("Fee Fi Fo Fum"),
        Phrase("A Dream Is a Wish Your Heart Makes"), Phrase("The Walrus and the Carpenter"),
        Phrase("Scales and Arpeggios"), Phrase("The Phony King of England"), Phrase("Goodbye May Seem Forever"),
        Phrase("The Worlds Greatest Criminal Mind"), Phrase("Appreciate the Lady"), Phrase("Let Me Be Good To You"),
        Phrase("Goodbye So Soon"), Phrase("Once Upon A Time In New York City"), Phrase("Why Should I Worry"),
        Phrase("Daughters of Triton"), Phrase("Part of Your World"), Phrase("Fathoms Below"), Phrase("Arabian Nights"),
        Phrase("One Jump Ahead"), Phrase("I Put A Spell On You"), Phrase("Just Around the Riverbend"),
        Phrase("Colors of the Wind"), Phrase("God Help the Outcasts"), Phrase("Topsy Turvy"), Phrase("Go the Distance"),
        Phrase("The Gospel Truth"), Phrase("Two Worlds"), Phrase("Son of Man"), Phrase("Strangers Like Me"),
        Phrase("Honor To Us All") ]},

        {"Disney Movies": [Phrase("The Hunchback of Notre Dame"), Phrase("Mulan"), Phrase("Aladdin"),
        Phrase("Moana"), Phrase("The Princess and the Frog"), Phrase("The Lion King"), Phrase("Pirates of the Caribbean"),
        Phrase("Wreck It Ralph"), Phrase("Pinocchio"), Phrase("Dumbo"), Phrase("Fantasia"), Phrase("Bambi"),
        Phrase("Alice In Wonderland"), Phrase("Peter Pan"), Phrase("Lady and the Tramp"), Phrase("Old Yeller"),
        Phrase("Sleeping Beauty"), Phrase("The Parent Trap"), Phrase("One Hundred and One Dalmations"),
        Phrase("The Black Cauldron"), Phrase("The Great Mouse Detective"), Phrase("The Little Brave Toaster"),
        Phrase("Honey I Shrunk the Kids"), Phrase("The Little Mermaid"), Phrase("The Rescuers Down Under"),
        Phrase("The Rocketeer"), Phrase("Beauty and the Beast"), Phrase("The Nightmare Before Chritmas"),
        Phrase("Hocus Pocus"), Phrase("Cool Runnings"), Phrase("The Jungle Book"),  Phrase("Pocahontas"),
        Phrase("Hercules"), Phrase("Inspector Gadget"), Phrase("Monsters Inc"), Phrase("Cinderella"),
        Phrase("Snow White and the Seven Dwarves"), Phrase("Tom and Huck"), Phrase("White Fang"), Phrase("Toy Story"),
        Phrase("A Goofy Movie"), Phrase("James and the Giant Peach"), Phrase("Treasure Planet"),
        Phrase("The Reluctant Dragon"), Phrase("Star Wars Rogue One"), Phrase("The Phantom Menace"),
        Phrase("Attack of the Clones"), Phrase("Revenge of the Sith"), Phrase("A New Hope"),
        Phrase("The Empire Strikes Back"), Phrase("Return of the Jedi"), Phrase("The Force Awakens"),
        Phrase("The Rise of Skywalker"), Phrase("The Last Jedi"),  Phrase("Big Hero Six"), Phrase("Solo"),
        Phrase("The Mandalorian")]},
        
        {"Disney Characters": [Phrase("Mulan"), Phrase("Shan Yu"), Phrase("Simba"), Phrase("Mufasa"), Phrase("Scar"),
        Phrase("Ariel"), Phrase("Ursula"), Phrase("Aladdin"), Phrase("Jafar"), Phrase("Mr Incredible"), 
        Phrase("The Screenslaver"), Phrase("Beast"), Phrase("Gaston"), Phrase("Mowgli"), Phrase("Shere Khan"),
        Phrase("Hercules"), Phrase("Hades"), Phrase("Quasimodo"), Phrase("Dom Claude Frollo"), Phrase("Wreck It Ralph"),
        Phrase("King Candy"), Phrase("Cruella Devil"), Phrase("Snow White"),Phrase("Genie"), Phrase("Iago"),
        Phrase("Barley Lightfoot"), Phrase("Ian Lightfoot"), Phrase("Rafiki"), Phrase("Timon"), Phrase("Ed"),
        Phrase("Iago"), Phrase("Lilo"), Phrase("Stitch"), Phrase("Nala"), Phrase("Captain Jack Sparrow"),
        Phrase("Captain Salazar"), Phrase("Davy Jones"), Phrase("Sheriff Woody"), Phrase("Buzz Lightyear"),
        Phrase("Goofy"), Phrase("Max"),Phrase("Esmerelda"), Phrase("Tarzan"), Phrase("Queen of Hearts"), Phrase("Happy"),
        Phrase("Doppy"), Phrase("Doc"), Phrase("Mando"), Phrase("Grogu"), Phrase("Ahsoka Tano"), Phrase("Luke Skywalker"),
        Phrase("Anakin Skywalker"), Phrase("Boba Fett"), Phrase("Obi Wan Kenobi"), Phrase("General Grievous"),
        Phrase("Casian Andor"), Phrase("King Triton"), Phrase("Emperor Palpatine"), Phrase("Commander Cody"), 
        Phrase("Qui Gon Jinn")]} ]
        self.active_phrase = None
        self.guesses = []
        self.category = ""


    def start(self):

        self.welcome()
        self.active_phrase = self.get_random_phrase()
        # creates game loop
        while True:       
            print(f"\n\nCategory: {self.category}\n")
            self.active_phrase.display(self.guesses)
            
            # calls get_guess()
            guess = self.get_guess()
            # adds player's guess to the guesses list
            self.guesses.append(guess)
            # print(self.guesses)
            self.active_phrase.check_letter(guess)
            # increments missed if guess incorrect
            if not self.active_phrase.check_letter(guess):
                self.missed += 1
                print(f"\n** '{guess}' isn't in the phrase!")
                print(f"** {5 - self.missed} chances left!")
            # calls game_over()
            if self.missed > 4:
                self.game_over("lose")
            elif self.active_phrase.check_complete(self.guesses):
                self.game_over("win")


    def get_random_phrase(self):

        category = -1
        while category not in range(1, len(self.phrases)+1):
            try:
                print("\nCategories:")
                for index, subset in enumerate(self.phrases, start=1):
                    for cat in subset.keys():
                        print(index, cat) 
                    
                category = int(input("\nChoose a phrase category number >> "))
            except ValueError:
                print("Enter a category NUMBER!")

        self.category = list(self.phrases[category - 1].keys())[0]

        phrases = list(self.phrases[category - 1].values())[0]
        return random.choice(phrases)


    def welcome(self):

        print("\n\nP-H-R-A-S-E--H-U-N-T-E-R!!\n")

    
    def get_guess(self):

        # get guess from user, verifies it's a letter and hasn't been guessed yet
        guess = ""
        while not guess.isalpha():
            guess = input("\nEnter a letter to guess >> ").lower()

            if guess in self.guesses:
                print("\nYou've alread guessed that letter!")
                print(f"Past Guesses: {self.guesses}")
                guess = ""

        return guess


    def game_over(self, message):

        # print win or lose message
        if message == "lose":
            print("\nGAME OVER!!")
        elif message == "win":
            print("\nYOU WON!!")
        
        print(f"The phrase was: '{self.active_phrase}''")

        # ask for replay
        replay = ""
        while replay != "y" and replay != "n":
            replay = input("\nPlay again? [y/n] >> ").lower()
        
        if replay == "y":
            game = Game()
            game.start()
        elif replay == "n":
            menu.main()
