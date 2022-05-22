"""Controller module"""
import time
import numpy as np
import pygame
import models



def game_loop(screen, bc_color, dead_color, alive_color):
    """Game's loop"""
    cells = np.zeros((60,75))
    running = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    running=not running
                    models.print_cells(screen, cells, 10, bc_color, alive_color)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1]//10 , pos[0]//10]=1
                models.print_cells(screen, cells, 10, bc_color, alive_color)
                pygame.display.update()
        if running:
            cells = models.update_and_print(screen, cells, 10 ,bc_color, dead_color, alive_color)
            pygame.display.update()
            time.sleep(0.001)
