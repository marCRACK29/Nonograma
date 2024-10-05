import State

class Context:
    _state = None
    
    def __init__(self, state: State) -> None:
        self.state = None
        self.transition_to(state)
        
    def transition_to(self, state: State):
        self._state = state
        self.state.context = self

    def request1(self):
        self._state.go_to()

    def request2(self):
        self._state.back_to()