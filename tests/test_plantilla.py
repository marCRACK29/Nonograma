import unittest

from numpy.ma.testutils import assert_equal

from src.plantilla import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
class TestPlantilla(unittest.TestCase):
    def test_createPlantilla(self):
        plantilla = Plantilla(5,5,10,[150,200])
        self.assertEqual(plantilla.width, 50)
        self.assertEqual(plantilla.height, 50)
        self.assertEqual(plantilla.pos[0],150)
        self.assertEqual(plantilla.pos[1],200)
    def test_click(self):
        plantilla = Plantilla(5,5,10,[150,200])
        plantilla.click([151,203],Cell_state.black)
        self.assertEqual(plantilla.grid[0][0].state,Cell_state.black)
        plantilla.click([175,26],Cell_state.marked)
        self.assertEqual(plantilla.grid[2][2],Cell_state.marked)

if __name__ == '__main__':
    unittest.main()
