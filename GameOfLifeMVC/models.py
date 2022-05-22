"""Models module"""
import pygame
import numpy as np


def print_cells(screen, cells, size, bc_color, alive_color ):
    """Printing cells without calculations"""
    for row, col in np.ndindex(cells.shape):
        if cells[row, col]==1:
            pygame.draw.rect(screen, alive_color,
                             (col*size, row*size, size-1, size-1),border_radius=2)
        else:
            pygame.draw.rect(screen, bc_color, (col*size, row*size, size-1, size-1),border_radius=2)

def update_and_print(screen, cells, size, bc_color, dead_color, alive_color):
    """Printing cells with calculations"""
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    for row, col in np.ndindex(cells.shape):
        alive=np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row,col]
        color= bc_color if cells[row, col] == 0 else alive_color
        if cells[row, col]==1:
            #if alive <2 or alive >3:
            #    color= dead_color
            if 2 <=alive <= 3:
                updated_cells[row, col]=1
                color = alive_color
        else:
            if alive==3:
                updated_cells[row, col]=1
                color = alive_color
        pygame.draw.rect(screen, color, (col*size, row*size, size-1, size-1),border_radius=2)
    return updated_cells
