"""Viewer module"""
import pygame
import controller


bc_color=(10,10,10)
dead_color=(123, 3, 252)
alive_color=(0, 0, 250)


def init_view():
    """Tnitiating screen and controller"""
    pygame.init()
    pygame.display.set_caption('Game of Life')
    screen= pygame.display.set_mode((750,600))
    screen.fill(bc_color)
    pygame.display.update()
    controller.game_loop(screen, bc_color, dead_color, alive_color)
