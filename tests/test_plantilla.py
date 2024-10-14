from src.plantilla import *


def test_createPlantilla():
    plantilla = Plantilla(5,5,10,[150,200])
    assert plantilla.width==50
    assert plantilla.height==50
    assert plantilla.pos[0]==150
    assert plantilla.pos[1]==200
def test_click():
    plantilla = Plantilla(5,5,10,[150,200])
    plantilla.click([151,203],Cell_state.black)
    assert plantilla.grid[0][0].state==Cell_state.black
    plantilla.click([175,226],Cell_state.marked)
    assert plantilla.grid[2][2].state==Cell_state.marked

