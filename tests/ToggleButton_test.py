import pytest, pygame, os
from src.State.ToggleButton import ToggleButton

# Creando un fixture para ocupar el mismo botón en todos los tests
@pytest.fixture
def test_toggle_button_initialization():
    # Obtener la ruta relativa a la carpeta resources
    image_path = os.path.join(os.path.dirname(__file__), "../resources/der.png")
    goto_img = pygame.image.load(image_path)
    x = 100
    y = 200
    scale = 2
    button = ToggleButton(x, y, goto_img, scale)
    return button

def test_button_click(toggle_button):
    button = toggle_button
    button.click()
    assert button.clicked == True





