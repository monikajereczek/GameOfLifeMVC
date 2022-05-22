"""Viewer module"""
import controller

def init_view():
    """Tnitiating screen and controller"""
    game=controller.GameController()
    game.game_loop()
