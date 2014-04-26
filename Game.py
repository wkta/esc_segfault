# LUDUM DARE 29: ESCAPE THE SEGFAULT!

import pygame
from Player import Player
from time import sleep

DISP_WIDTH = 1024
DISP_HEIGHT = 600

class Game:
    """ permet de faire tourner le jeu avec boucles d'evenement et gestion de l'etat du jeu"""
    pl = None
    window = None

    ST_INTRO = 0
    ST_PLATEFORMER = 1
    ST_GAME_OVER = 2

    def __init__(self):
        pygame.init()
        Game.pl = Player( 0, 0 )  #TODO osition realiste
        Game.window = pygame.display.set_mode( (DISP_WIDTH, DISP_HEIGHT) )
        self.state = Game.ST_PLATEFORMER

    def __del__(self):
        del Game.pl
        del Game.window
        pygame.quit()

    def run(self):
        """gere la boucle d'evenements"""
        prog_done = False
        while not prog_done:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    prog_done = True
                    break 
                if event.type is pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Game.pl.jump()
                    if event.key == pygame.K_RIGHT:
                        Game.pl.moveRight()
                    if event.key == pygame.K_RIGHT:
                        Game.pl.moveRight()
                    elected_item = (selected_item +1) % 3 

g = Game()
g.run()
del g
