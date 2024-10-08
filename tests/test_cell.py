import unittest

from src.cell import *

class TestCell(unittest.TestCase):
    def test_createCell(self):
        cell = Cell()
        self.assertEqual(cell.state,Cell_state.empty)
    def test_click(self):
        cell1 = Cell()
        cell2 = Cell()
        cell1.click(Cell_state.black)
        self.assertEqual(cell1.state,Cell_state.black)
        cell2.click(Cell_state.marked)
        self.assertEqual(cell2.state,Cell_state.marked)
        cell2.click(Cell_state.black)
        self.assertEqual(cell2.state,Cell_state.marked)
if __name__ == '__main__':
    unittest.main()
