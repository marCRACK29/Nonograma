import pytest, pygame, os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from state.ToggleButton import ToggleButton

# Creación de un fixture para ocupar el mismo botón en todos los tests
@pytest.fixture
def toggle_button():
    pygame.init()
    # Obtener la ruta relativa a la carpeta resources
    image_path = os.path.join(os.path.dirname(__file__), "../resources/der.png")
    goto_img = pygame.image.load(image_path)
    x = 100
    y = 200
    scale = 2
    button = ToggleButton(x, y, goto_img, scale)
    yield button  # Devuelve el objeto ToggleButton para los tests
    # Al finalizar el test, cerramos pygame
    pygame.quit()

def test_button_click(toggle_button):
    button = toggle_button
    # Simulamos la posición del mouse sobre el botón
    pygame.mouse.set_pos((button.rect.x + 1, button.rect.y + 1))
    # Simulamos que el botón izquierdo del mouse está presionado
    pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1))
    # Ejecutamos el metodo click
    button.click()
    # Verificamos que el botón ha sido clicado
    assert button.clicked == True






