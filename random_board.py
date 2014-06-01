from random import choice
from block_kind import BlockKind
from board import Board

class RandomBoard(Board):
    def __init__(self, width, height):
        super(RandomBoard, self).__init__(width, height)
        for column in blocks:
            for element in column:
                self.blocks[column + row] = BlockKind(choice(available_colors))
