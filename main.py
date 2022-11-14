def mathGame():
    pass

def trivia():
    print("Hello, Welcome to Philippines Trivia!")

    ans = input("Are you ready to play? (YES/NO): ")
    score = 0
    total_q = 4                

    if ans.lower() == 'yes':
            ans = input("1. Name the oldest Philippine city.: ")
            if ans == 'cebu':
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

    print("Thank you for playing, you got", score, "correct answer/s!")
    mark = (score/total_q) * 100

    print("Mark:", str(mark) + '%')
    print('Goodbye')

    ans1 = input('You want to try again? (YES/NO): ')
    if ans1.lower() == 'yes' or ans1.upper() == 'yes':
        main()
    else:
        exit()

        
def rock_paper_scissors():
    pass

def wordGuess():
     import random

    class Name:
        def yourname(you):
            name = input("What is your name? ")
            print("Good Luck, ", name)

    class Category(Name):
        def game(cate):
            print()
            print("Category: Technology")
            print()

    k = Category()
    k.yourname()
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

