def tic_tac_toe():
  print("test")

def snake_game(): 
  pass

def rock_paper_scissors():    
  pass

def hangman_game():
  pass


def main():
    while True:
        print("1. Tic tac toe\n2. Snake Game\n3. Rock Paper Scissor\n4. Hangman Game\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            tic_tac_toe()
        elif choice == "2":
            snake_game()
        elif choice == "3":
            rock_paper_scissors()
        elif choice == "4":
            hangman_game()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
  main()
