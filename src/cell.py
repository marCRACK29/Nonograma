from enum import Enum
import pygame
import switch


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
    def __repr__(self):
        ret = ""
        if(self.state==Cell_state.empty):ret=" "
        elif(self.state==Cell_state.marked):ret="X"
        elif(self.state==Cell_state.black):ret="@"
        else:ret="?"
        return ret

cell = Cell()
cell.click(Cell_state.black)
print(cell)