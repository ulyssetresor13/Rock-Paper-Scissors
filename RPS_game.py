# RPS_game.py

from RPS import play_round

def main():
    print("Welcome to Rock Paper Scissors!")
    play_again = True
    while play_again:
        play_round()
        play_again = input("Do you want to play again? (yes/no) ") == 'yes'

if __name__ == "__main__":
    main()
