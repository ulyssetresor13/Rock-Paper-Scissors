# Main.py

from RPS import RockPaperScissors

def main():
    game = RockPaperScissors()
    while True:
        game.run_game()
        game.print_score()

        continue_prompt = input('\nDo you wish to play again? (y/n): ').lower()
        if continue_prompt == 'n':
            print("Thanks for playing!")
            break
        elif continue_prompt == 'y':
            pass  # No need to explicitly break here; the loop continues naturally
        else:
            print("Invalid input!")

if __name__ == "__main__":
    main()
