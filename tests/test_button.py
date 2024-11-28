import pytest
import pygame
from src.button import Button

@pytest.fixture
def button_prueba():
    pygame.init()
    font = pygame.font.SysFont(None, 30)
    button = Button(
        image=None,
        pos=(100, 100),
        text_input="Click Me",
        font=font,
        base_color=(255, 255, 255),
        color_flotante=(255, 0, 0)
    )
    return button

def test_dentro_boton(button_prueba):
    button = button_prueba
    estoy_dentro = (100, 100)
    assert button.checkForInput(estoy_dentro) is True

def test_fuera_boton(button_prueba):
    button = button_prueba
    estoy_fuera = (200, 200)
    assert button.checkForInput(estoy_fuera) is False

def test_cambiar_color_uno(button_prueba):
    button = button_prueba
    posicion_flotante = (100, 100)
    button.changeColor(posicion_flotante)
    assert button.text.get_at((0, 0))[:3] == button.color_flotante

def test_cambiar_color_dos(button_prueba):
    button = button_prueba
    posicion_no_flotante = (200, 200)
    button.changeColor(posicion_no_flotante)
    assert button.text.get_at((0, 0))[:3] == button.base_color
