def mathGame():
    pass

def trivia():
    pass

def rock_paper_scissors():
    pass

def wordGuess():
    pass

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

