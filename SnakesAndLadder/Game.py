from collections import deque
from threading import Lock
from Dice import Dice

class Game:
    _lock = Lock()
    _instance = None
    _initialized = False


    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, players, board):
        if not self.__class__._initialized:
            self.players = deque(players)
            self.dice = Dice()
            self.board = board

    def play(self):
        while not self.game_over():
            curr_player = self.players.popleft()

            dice_roll = self.dice.roll()
            print(dice_roll)
            new_position = self.board.get_next_position(curr_player.position+dice_roll)
            if 1 <= new_position < self.board.board_size:
                print(f"{curr_player.name} position from {curr_player.position} to {new_position}")
                curr_player.position = new_position
                self.players.append(curr_player)

            elif new_position == self.board.board_size:
                print(f"{curr_player.name} WINS!!!!!!")

            else:
                print("Invalid position, Roll Again")
                self.players.append(curr_player)

    def game_over(self):
        if len(self.players) == 1:
            print("Only 1 player left, game over")

            return True
        return False


