import unittest

from block import Block
from block_kind import BlockKind

class BlockTest(unittest.TestCase):

    def test_comparison(self):
        self.assertEqual(Block(BlockKind('red')), Block(BlockKind('red')))
        self.assertNotEqual(Block(BlockKind('red')), Block(BlockKind('green')))


if __name__ == '__main__':
    unittest.main()