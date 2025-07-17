from threading import Lock
from Dice import Dice

class Board:
    _lock = Lock()
    _instance = None
    _initialized = False


    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, snakes_list, ladders_list, board_size):
        if not self.__class__._initialized:
            self.snakes = {}
            for snake in snakes_list:
                self.snakes[snake.head] = snake.tail

            self.ladders = {}

        for ladder in ladders_list:
            self.ladders[ladder.start] = ladder.end

        self.board_size = board_size
        self.__class__._initialized = True


    def get_next_position(self, curr_position):
        if curr_position in self.snakes:
            return self.snakes[curr_position]

        if curr_position in self.ladders:
            return self.ladders[curr_position]
        return curr_position



