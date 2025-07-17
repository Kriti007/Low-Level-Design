from Snake import Snake
from Ladder import Ladder
from Board import Board
from Player import Player
from Game import Game


class SnLDemo:
    @staticmethod
    def run():
        snakes = [Snake(17, 7), Snake(98,10)]
        ladders = [Ladder(2, 18), Ladder(50, 78)]
        board = Board(snakes, ladders, 100)
        players = [Player("1"), Player("2"), Player("3"), Player("4")]
        game = Game(players, board)
        game.play()

if __name__=="__main__":
    SnLDemo.run()