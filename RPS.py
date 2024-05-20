# RPS.py

import random

class RockPaperScissors:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.options = {'rock': 0, 'paper': 1, 'scissors': 2}

    def random_choice(self):
        return random.choice(list(self.options.keys()))

    def check_win(self, player, opponent):
        result = (player - opponent) % 3
        if result == 0:
            self.ties += 1
            print("The game is a tie You are a most worthy opponent!")
        elif result == 1:
            self.wins += 1
            print("You win My honor demands a rematch!")
        elif result == 2:
            self.losses += 1
            print("Haha, I am victorious Dare you challenge me again?")

    def print_score(self):
        print(f"You have {self.wins} wins, {self.losses} losses, and {self.ties} ties.")

    def run_game(self):
        while True:
            user_choice = input("Choices are 'rock', 'paper', or 'scissors'. Which do you choose? ").lower()
            if user_choice not in self.options.keys():
                print("Invalid input, try again!")
            else:
                break
        opponent_choice = self.random_choice()
        print(f"You've picked {user_choice}, and I picked {opponent_choice}.")
        self.check_win(self.options[user_choice], self.options[opponent_choice])

if __name__ == "__main__":
    game = RockPaperScissors()
    while True:
        game.run_game()
        game.print_score()

        continue_prompt = input('\nDo you wish to play again? (y/n): ').lower()
        if continue_prompt == 'n':
            print("You are weak!")
            exit()
        elif continue_prompt == 'y':
            break
        else:
            print("Invalid input!\n")
            continue
