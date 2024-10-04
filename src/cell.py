from enum import Enum
class Cell_state(Enum):
    empty = 1
    marked = 2
    black = 3

class Cell:
    def __init__(self):
        self.state=Cell_state.empty
    def click(self,newState):
        if(self.state == Cell_state.empty):
            self.state = newState
