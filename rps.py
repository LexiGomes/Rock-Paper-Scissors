"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


import random
import time

moves = ['rock', 'paper', 'scissors']


def print_pause(message, seconds=2):
    print(message)
    time.sleep(seconds)


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    my_move = None
    their_move = None

    def move(self):
        pass

    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.my_move = my_move


def beats(you, opponent):
    return ((you == 'rock' and opponent == 'scissors') or
            (you == 'scissors' and opponent == 'paper') or
            (you == 'paper' and opponent == 'rock'))


class AllRockerPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ComputerPlayer(Player):
    def move(self, p2):
        self.p2 = p2
        p2 = random.choice(['rock', 'paper', 'scissors'])
        return p2


class HumanPlayer(Player):
    def move(self):
        attempts = 3
        p1 = input("What do you want to play? Rock, "
                   "paper or scissors?\n").lower()
        while True:
            if attempts == 0:
                print_pause("You failed to provide a correct option "
                            "to play the game. Good bye!")
                Game.play_again(self)
            elif p1 not in moves:
                print_pause("Please fill in a valid choice: rock, "
                            f"paper or scissors? You have {attempts} left.\n")
                attempts -= 1
            else:
                return p1


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        else:
            return 'rock'


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def check_won(self):
        if self.p1_score == self.p2_score:
            print_pause("The game ended in a tie! "
                        "But well played :)")
        elif self.p1_score < self.p2_score:
            print_pause("Too bad, you lost! As long "
                        "as you had fun :D.")
        elif self.p1_score > self.p2_score:
            print_pause("Woo hoo! You won. Nicely done!")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played: {move1}.\nOpponent played: {move2}.")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            self.p1_score += 1
            print_pause("You win!")
        elif beats(move2, move1):
            self.p2_score += 1
            print_pause("Opponent wins!")
        else:
            print_pause("It's a tie!")
        print_pause(f"Score\nYou: {self.p1_score}\n"
                    f"Opponent: {self.p2_score}\n\n")

    def play_again(self):
        again = input("Would you like to play again? (y/n).\n").lower()
        while True:
            if "y" in again:
                print_pause("Good choice. Starting game up.")
                Game.play_game(self)
                break
            elif "n" in again:
                print_pause("Thanks for playing! Good bye!")
                exit()
                break
            else:
                print_pause("Please enter a valid answer :).")
                break

    def play_game(self):
        print("Game start!")
        rounds = input("Would you like to play a round of five or "
                       "just one game? Please enter 5 or 1.\n")
        while True:
            if rounds == "5":
                for round in range(6):
                    print(f"Round {round}:")
                    self.play_round()
                print_pause("Game over!")
                Game.check_won(self)
                Game.play_again(self)
            elif rounds == "1":
                for round in range(1):
                    print(f"Round {round}:")
                    self.play_round()
                    print_pause("Game over!")
                    Game.check_won(self)
                    Game.play_again(self)
            else:
                print_pause("Please just enter the numbers 5 or 1")


if __name__ == '__main__':
    strategies = {
    "1": AllRockerPlayer(),
    "2": RandomPlayer(),
    "3": CyclePlayer(),
    "4": ReflectPlayer()
}
    user_input = input("Select the player strategy "
                       "you want to play against:\n"
                       "1 - Rock Player\n"
                       "2 - Random Player\n"
                       "3 - Cycle Player\n"
                       "4 - Reflect Player\n")
    game = Game(HumanPlayer(), strategies[user_input])
    game.play_game()
