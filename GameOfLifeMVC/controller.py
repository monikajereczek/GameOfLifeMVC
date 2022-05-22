"""Controller module"""
import time
import numpy as np
import pygame
import models

class GameController:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Game of Life')
        self.screen= pygame.display.set_mode((750,600))
        self.screen.fill((10,10,10))
        pygame.display.update()
        self.cells=models.Cells(60,75,10,(10,10,10),(0, 0, 250))
        self.running=False
    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        self.running=not self.running
                        self.cells.print_cells(self.screen)
                        pygame.display.update()
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    self.cells.cells[pos[1]//10 , pos[0]//10]=1
                    self.cells.print_cells(self.screen)
                    pygame.display.update()
            if self.running:
                self.cells.update_and_print(self.screen)
                pygame.display.update()
                time.sleep(0.001)
