from src.cell import *

def test_createCell():
    cell = Cell()
    assert cell.state==Cell_state.empty


def test_click():
    cell1 = Cell()
    cell2 = Cell()
    cell1.click(Cell_state.black)
    assert cell1.state==Cell_state.black
    cell2.click(Cell_state.marked)
    assert cell2.state==Cell_state.marked
    cell2.click(Cell_state.black)
    assert cell2.state==Cell_state.marked
