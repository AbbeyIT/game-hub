def mathGame():
    pass

def trivia():
    print("\nWelcome to the Philippines Trivia Game!")
    name = input("\nEnter you name: ")
    print("Hello %s," % (name), "have fun!")
    ans = input("\nAre you ready to play, %s? (YES/NO): " % (name))

    score = 0
    total_questions = 5               

    print("\nTrivia Question")
    if ans.lower() == 'yes':
            ans = input("1. Name the oldest Philippine city.: ")
            if ans.lower() == 'cebu':
                score += 1
                print("Correct!")
            else:
                print("Incorrect")

            ans = input("2. What place in the Philippines is also known as the “walled city”?: ")
            if ans.lower() == 'intramuros':
                score += 1
                print("Correct!")
            else:
                print("Incorrect")

            ans = input("3. What is the capital of the Republic of the Philippines?: ")
            if ans.lower() == 'manila':
                score += 1
                print("Correct!")
            else:
                print("Incorrect")

            ans = input("4. Philippines is located in which continent: ")
            if ans.lower() == 'asia':
                score += 1
                print("Correct!")
            else:
                print("Incorrect")

            ans = input("5. Philippines national food is?: ")
            if  ans.lower() == 'lechon':
                score += 1
                print("Correct!")
            else:
                print("Incorrect")

    print("\nThank you for playing; you got", score, "correct answer/s!")
    mark = (score/total_questions) * 100

    print("Mark:", str(mark) + '%')
    print('\nGoodbye %s.' %(name), "Thank you for playing Philippines Trivia Game.")
    print()

        
def rock_paper_scissors():
    from os import system
    from random import randint


    class rock_paper_scissors:
        def __init__(self):
            self.choices = "rock", "paper", "scissors"
            self.player_wins = 0
            self.computer_wins = 0
            StudentID = int(input('Enter your Student ID: '))
            age = int(input('Enter your age: '))

        def _spacer_size(self, length=95):
            return '=' * length

        def _player_move(self):
            while True:
                try:
                    option = int(input('Choose an option between Rock (1), Paper (2), Scissors (3): '))

                    if 1 <= option <= 3:
                        break
                    else:
                        print('You can only enter a number between 1, 2 and 3.')    
                except ValueError:
                    print('The value entered is invalid. You can only enter numeric values.')

            return option

        def _computer_move(self):
            return randint(1,3)

        def _check_winner(self):
            if self.player_wins == self.computer_wins:
                return 'Tie.'
            elif self.player_wins > self.computer_wins:
                return 'You won the set.'
            else:
                return 'Computer wins the set.'

        def _play(self):
            times = int(input("How many times do you wish to play?: "))
            print("Let's start!")

            for i in range(times):
                player = self._player_move()
                computer = self._computer_move()
                print(f"You chose {self.choices[player-1]}.")
                print(f"The computer chose {self.choices[computer-1]}.")

                if player == computer:
                    print('Tie.\n')
                    print(self._spacer_size(), '\n')
                elif (player-computer) % 3 == 1:
                    print('You won.\n')
                    print(self._spacer_size(), '\n')
                    self.player_wins += 1
                else:
                    print('You lost.\n')
                    print(self._spacer_size(), '\n')
                    self.computer_wins += 1

            print(self._check_winner())
            input("Press enter to return to the main menu...")
            self.main()

        def main(self, length=95):
            while True:
                try:
                    print('*' * length)
                    print('''
                                         ROCK, PAPER, AND SCISSORS                                     
                    '''.center(10))
                    print('*' * length, '\n')
                    print('1. Play'.center(length))
                    print('2. Instructions'.center(length))
                    print('3. Exit'.center(length))
                    choice = int(input('\nEnter an option: '))
                except ValueError:
                    print('The value entered is invalid. You can only enter numeric values.')

                if choice == 1:
                    self._play()
                    break
                elif choice == 2:
                    print("  Instructions for Rock, Paper, Scissors: ")
                    print("- Options: (1)Rock, (2)Paper, (3)Scissors")
                    print("- You can only enter a number between 1, 2, and 3.")
                    print("- Rock wins over scissors (because rock smashes scissors).")
                    print("- Scissors wins over paper (because scissors cut paper).")
                    print("- Paper wins over rock (because paper covers rock).")
                    print("- If both players show the same sign, it's a tie.\n")
                    input("Press enter to return to the main menu...")
                elif choice == 3:
                    exit()
                else:
                    print("You have entered a number that isn't in the list.")

    if __name__ == '__main__':
        game = rock_paper_scissors()
        game.main()


def wordGuess():
    import random
    
    print("\nWelcome to Word Guessing Game!")

    class Player: 
        def __init__(self, Name):
            self.Name = Name

        def introduce(self):
            print("Good luck, " + self.Name)

        def goodbye(self):
            print("\nGoodbye, " + self.Name + ". Thank you for playing Word Guessing Game.\n")

    name = input("\nWhat is your name? ")
    playerOne = Player(name)

    def intro(obj):
        obj.introduce()
    intro(playerOne)

    class Category(Name):
        def game(cate):
            print()
            print("Category: Technology")
            print()

    k = Category()
    k.game()

    words = ['phone', 'computer', 'television', 'programming',
            'python', 'internet', 'database', 'machine',
            'games', 'gadgets']


    word = random.choice(words)


    print("Guess the characters")

    guesses = ''

    turns = 12


    while turns > 0:

        failed = 0

        for char in word:

            if char in guesses:
                print(char, end=" ")

            else:
                print("_")

                failed += 1

        if failed == 0:
            print("\n\nYou Win!")

            print("The word is: ", word)
            break

        print()
        guess = input("\nguess a character:")

        guesses += guess

        if guess not in word:

            turns -= 1

            print("Wrong")
            print()

            print("You have", + turns, 'more guesses')

            if turns == 0:
                print("You Lose...")
                
     def bye(obj):
        obj.goodbye()
     bye(playerOne)


def sudoku():
    pass


def main():
    while True:
        print("1. Math Game\n2. Trivia\n3. Rock Paper Scissor\n4. Word Guessing Game\n5. Sudoku\n6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            mathGame()
        elif choice == "2":
            trivia()
        elif choice == "3":
            rock_paper_scissors()
        elif choice == "4":
            wordGuess()
        elif choice == "5":
            sudoku()
        elif choice == "6":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

