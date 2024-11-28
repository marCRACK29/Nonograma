import pygame
import pytest

from src.colorbutton import ColorButton
from src.Color import Color

@pytest.fixture
def colorbutton_prueba():
    pygame.init()
    color = Color.RED.value
    ficticia = pygame.Surface((50, 50))

    colorbutton = ColorButton(
        image_base=ficticia,
        image_flotante=ficticia,
        pos=(100, 100),
        color=color,
        size=(50, 50)
    )
    return colorbutton

def test_check_for_input_dentro(colorbutton_prueba):
    colorbutton = colorbutton_prueba
    estoy_dentro = (100, 100)
    assert colorbutton.checkForInput(estoy_dentro) is True

def test_check_for_input_fuera(colorbutton_prueba):
    colorbutton = colorbutton_prueba
    estoy_fuera = (200, 200)
    assert colorbutton.checkForInput(estoy_fuera) is False

def test_get_color(colorbutton_prueba):
    colorbutton = colorbutton_prueba
    assert colorbutton.get_color() == Color.RED.value

