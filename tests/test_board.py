import unittest

from numpy.ma.testutils import assert_equal

from src.board import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
class TestBoard(unittest.TestCase):
    def test_createBoard(self):
        board = Board(5,5,10,[150,200])
        self.assertEqual(board.width, 50)
        self.assertEqual(board.height, 50)
        self.assertEqual(board.pos[0],150)
        self.assertEqual(board.pos[1],200)
    def test_click(self):
        board = Board(5,5,10,[150,200])
        board.click([151,203],Cell_state.black)
        self.assertEqual(board.grid[0][0].state,Cell_state.black)
        board.click([175,26],Cell_state.marked)
        self.assertEqual(board.grid[2][2],Cell_state.marked)

if __name__ == '__main__':
    unittest.main()
