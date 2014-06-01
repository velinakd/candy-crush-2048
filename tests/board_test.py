import unittest

from itertools import chain
from board import Board

class BoardTest(unittest.TestCase):

    def test_board_width(self):
        board = Board(6,5)
        self.assertEqual(len(board.blocks), 5)

    def test_board_height(self):
        board = Board(6,5)
        self.assertTrue(all(map(lambda x: len(x) == 6, board.blocks)))

    def test_board_elements_all_none(self):
        board = Board(6,5)
        self.assertTrue(all(map(lambda x: x is None, chain(*board.blocks))))

if __name__ == '__main__':
    unittest.main()