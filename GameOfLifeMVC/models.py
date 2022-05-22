"""Models module"""
import pygame
import numpy as np

class Cells:
    def __init__(self, x, y, size, bc_color, alive_color):
        self.cells=np.zeros((x,y))
        self.size=size
        self.bc_color=bc_color
        self.alive_color=alive_color
    def print_cells(self, screen):
        for row, col in np.ndindex(self.cells.shape):
            if self.cells[row, col]==1:
                pygame.draw.rect(screen, self.alive_color,(col*self.size, row*self.size, self.size-1, self.size-1),border_radius=2)
            else:
                pygame.draw.rect(screen, self.bc_color, (col*self.size, row*self.size, self.size-1, self.size-1),border_radius=2)
    def update_and_print(self, screen):
        updated_cells = np.zeros((self.cells.shape[0], self.cells.shape[1]))
        for row, col in np.ndindex(self.cells.shape):
            alive=np.sum(self.cells[row-1:row+2, col-1:col+2]) - self.cells[row,col]
            color= self.bc_color if self.cells[row, col] == 0 else self.alive_color
            if self.cells[row, col]==1:
                if 2 <=alive <= 3:
                    updated_cells[row, col]=1
                    color = self.alive_color
            else:
                if alive==3:
                    updated_cells[row, col]=1
                    color = self.alive_color
            pygame.draw.rect(screen, color, (col*self.size, row*self.size, self.size-1, self.size-1),border_radius=2)
        self.cells=updated_cells
       

