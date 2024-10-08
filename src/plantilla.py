from src.cell import *
class Plantilla:
    def __init__(self, rows, columns, scale, pos):
        self.grid = [[Cell() for i in range(columns)] for j in range(rows)]
        self.width = columns * scale
        self.height = rows * scale
        self.scale = scale
        self.pos = pos

    def click(self,mousePos,color):
        relativeMousePos = [mousePos[0]-self.pos[0],mousePos[1]-self.pos[1]]
        gridPos = [(relativeMousePos[0]//self.scale),(relativeMousePos[1]//self.scale)]
        self.grid[gridPos[0]][gridPos[1]].click(color)

