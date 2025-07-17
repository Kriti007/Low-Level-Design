import random
from threading import Lock


class Dice:
    _lock = Lock()
    _instance = None

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance


    def roll(self):
        return random.randint(1,6)