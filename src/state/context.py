import pygame

class Context:
    _state = None
    
    def __init__(self, state: 'State') -> None:
        self.transition_to(state)
        
    def transition_to(self, state: 'State'):
        print(f"Transicion a ... {state.__class__.__name__}")
        self._state = state
        self._state.context = self

    def request1(self):
        self._state.go_to()

    def request2(self):
        self._state.back_to()

    def run(self):
        running = True
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Nonograma")

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # Aquí nos aseguramos de que se pase el evento a handle_events
                if hasattr(self._state, 'handle_events'):
                    self._state.handle_events(event)
            # Dibujar el estado actual
            if self._state is not None:
                self._state.draw(screen)
            else:
                print("No state is set!")  # Depuración
            pygame.display.flip()
        pygame.quit()