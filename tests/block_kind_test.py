import unittest

from block_kind import BlockKind


class BlockKindTest(unittest.TestCase):

    def test_comparison(self):
        self.assertEqual(BlockKind('yellow'), BlockKind('yellow'))
        self.assertNotEqual(BlockKind('yellow'), BlockKind('green'))


if __name__ == '__main__':
    unittest.main()