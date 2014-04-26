# LUDUM DARE 29: ESCAPE THE SEGFAULT!

import pygame
from Player import Player
from time import sleep

DISP_WIDTH = 1024
DISP_HEIGHT = 600

class Game:
    """ permet de faire tourner le jeu avec boucles d'évènement et gestion de l'état du jeu"""
    pl = Player()
    window = None

    ST_INTRO = 0
    ST_PLATEFORMER = 1
    ST_GAME_OVER = 2

    def __init__(self):
        pygame.init()
        Game.pl = Player()
        Game.window = pygame.display.set_mode( (DISP_WIDTH, DISP_HEIGHT) )
        self.state = 

    def __del__(self):
        del Game.pl
        del Game.window
        pygame.quit()

