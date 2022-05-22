"""Models module"""
import pygame
import numpy as np

class Cells:
    """Cells class"""
    def __init__(self,cells_array_size, cell_size, bc_color, alive_color):
        """Initiating cells"""
        self.cells=np.zeros(cells_array_size)
        self.size=cell_size
        self.bc_color=bc_color
        self.alive_color=alive_color
    def print(self, screen):
        """Priting cells"""
        for row, col in np.ndindex(self.cells.shape):
            if self.cells[row, col]==1:
                pygame.draw.rect(screen, self.alive_color,
                                 (col*self.size, row*self.size, self.size-1, self.size-1),
                                 border_radius=2)
            else:
                pygame.draw.rect(screen, self.bc_color,
                                 (col*self.size, row*self.size, self.size-1, self.size-1),
                                 border_radius=2)
    def update(self):
        """Updating the cells"""
        updated_cells = np.zeros((self.cells.shape[0], self.cells.shape[1]))
        for row, col in np.ndindex(self.cells.shape):
            alive=np.sum(self.cells[row-1:row+2, col-1:col+2]) - self.cells[row,col]
            if self.cells[row, col]==1:
                if 2 <=alive <= 3:
                    updated_cells[row, col]=1
            else:
                if alive==3:
                    updated_cells[row, col]=1
        self.cells=updated_cells
