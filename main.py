def mathGame():
    import random
    import time
    import operator

    def display_intro():
        title = "--- MATH QUIZ GAME ---"
        print ("-" * len(title))
        print(title)
        print ("-" * len(title))
        time.sleep(1)

    def greeting():
        greeting = "--- WELCOME TO MATH BRAIN TEASER! ---"
        print ("-" * len(greeting))
        print (greeting)
        print ("-" * len(greeting))

    class Player:
        def __init__(self, name):
            self.name = name

        def intro(self):
            print ("Hello " + self.name + ", have fun!\n")

        def outro(self):
            print("\nThank you " + self.name + " for playing!")

    def display_menu():
        menu_list = [" o EASY", " o AVERAGE", " o HARD"]
        print(menu_list[0])
        print(menu_list[1])
        print(menu_list[2])
        print()

    def user_level():
        while True:
                try:
                    level = str(input("Choose your level: "))

                    if level =="EASY" or level=="easy":
                        return level
                    elif level =="AVERAGE" or level=="average":
                        return level
                    elif level =="HARD" or level=="hard":
                        return level
                    else:
                        print("Invalid option.")
                        continue
                except:
                    print('Invalid.')
                    continue

    def random_problem():
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
        }

        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        operation = random.choice(list(operators.keys()))
        answer = operators.get(operation)(num1, num2)
        print(f'{num1}{operation}{num2}')
        return answer

    def question():
        while True:
            try:
                answer = random_problem()
                guess = int(input())
            except:
                print ("Invalid answer. Next question...")
                continue
            return guess == answer

    def display_outro():
        print()
        title = "--- THE END ---"
        print ("-" * len(title))
        print(title)
        print ("-" * len(title))

    def game():
        display_intro()
        name = str(input("Please enter your name: "))
        player = Player(name)
        greeting()
        player.intro()
        display_menu()
        level = user_level()
        if level == "EASY" or level=="easy":
            score = 0
            for x in range(5):
                if question() == True:
                    score += 1
        if level == "AVERAGE" or level=="average":
            score = 0
            for x in range(10):
                if question() == True:
                    score += 1
        if level == "HARD" or level=="hard":
            score = 0
            for x in range(20):
                if question() == True:
                    score += 1

        print(f'Your score is {score}')
        player.outro()
        display_outro()

    game()


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
    from random import randint


    class rock_paper_scissors:
        def __init__(self):
            self.choices = "rock", "paper", "scissors"
            self.player_wins = 0
            self.computer_wins = 0
            print(self.spacer(), '\n')

        def player_move(self):
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

        def computer_move(self):
            return randint(1,3)
            
        def check_winner(self):
            
            if self.player_wins == self.computer_wins:
                return 'Tie.'
            elif self.player_wins > self.computer_wins:
                return 'You won the set.'
            else:
                return 'Computer wins the set.'

        def spacer(self, length=95):
            return '=' * length
        
        def _play(self):
            times = int(input("How many times do you wish to play?: "))
            print("Let's start!")

            for i in range(times):
                player = self.player_move()
                computer = self.computer_move()
                print(f"You chose {self.choices[player-1]}.")
                print(f"The computer chose {self.choices[computer-1]}.")

                if player == computer:
                    print('Tie.\n')
                    print(self.spacer(), '\n')
                elif (player-computer) % 3 == 1:
                    print('You won.\n')
                    print(self.spacer(), '\n')
                    self.player_wins += 1
                else:
                    print('You lost.\n')
                    print(self.spacer(), '\n')
                    self.computer_wins += 1

            print(self.check_winner())
            input("Press enter to return to the main menu...")
            self.main()
            
        def main(self, length=95):
            name = str(input('Enter your Name: '))
            space = ('')
            yourname = space.center(43, ' ')
            while True:
                try:
                    print('*' * length)
                    print('''
                                Welcome to the ROCK, PAPER, SCISSORS Game!
                    ''')
                    print(yourname, "Good Luck,", name,"!", yourname)
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
                    print("Goodbye! Thank you for playing ROCK PAPER SCISSOR Game.")
                    print(self.spacer(), '\n')
                    main()
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
    import random

    def greeting():
        greeting = "--- WELCOME TO SUDOKU! ---"
        print ("-" * len(greeting))
        print (greeting)
        print ("-" * len(greeting))

    greeting()
    name = input("\nEnter you name: ")
    print("Hello %s," % (name), "have fun!")

    def duplicate_checker(a):
            b = set(a)
            result = len(a) != len(b)

            if(result == True):
                return True
                
    def check_row(a):
        for x in a:
            if(duplicate_checker(x) == True):
                return True

    def check_column(a):
        for y in range(len(a)):
            list = []
            for x in a:
                list.append(x[y])
            if(duplicate_checker(list) == True):
                return True
            
    def display_grid(grid):
        print("")
        count = 1
        print("   1  2  3")
        for x in grid:
            
            print(count,x,end=" ")
            count+=1
            print()
            
    def randomNumber(grid):
        for x in range(6):
            y = random.randint(0,2)
            x = random.randint(0,2)
            grid[x][y] = 0

    grid = [[1, 2, 3],[3, 1, 2] ,[2, 3, 1]]

    solved = False
    randomNumber(grid)
    display_grid(grid)

    while solved != True:
        y = int(input("Enter row [between 1-3] "))-1
        x = int(input("Enter column [between 1-3] "))-1
        num = int(input("Enter number to insert "))
        
        if grid[y][x] == 0:
            grid[y][x] = num
        else:
            if input("Do you want to overwrite? [y/n]") == "y":
                grid[y][x] = num
            
        display_grid(grid)
        full = True
        for x in grid:
            for y in x:
                if(y == 0):
                    full = False
        if(full ==True):
            if(check_row(grid) == True or check_column(grid) == True):
                print("Try again.")
            else:
                print("Congratulations! You solved it :)")
                solved =True
    
    print('\nGoodbye %s.' %(name), "Thank you for playing Sudoku.")
    print()

def main():
    title = "--- WELCOME TO GAME HUB! ---"
    print ("-" * len(title))
    print(title)
    print ("-" * len(title))
    while True:
        print("Choose a game")
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

