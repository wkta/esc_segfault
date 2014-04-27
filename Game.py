# LUDUM DARE 29: ESCAPE THE SEGFAULT!

import pygame
from Player import Player
from SkillBar import SkillBar 
from time import sleep

from global_vars import *

Fdelay = 1000 / FPS

class Game:
    """ permet de faire tourner le jeu avec boucles d'evenement et gestion de l'etat du jeu"""
    pl = None
    window = None

    ST_INTRO = 0
    ST_PLATEFORMER = 1
    ST_GAME_OVER = 2

    def __init__(self):
        pygame.init()
        Game.pl = Player( 0, 0 )  #TODO :  position realiste
        Game.sk_bar = SkillBar( Game.pl )
        Game.window = pygame.display.set_mode( (DISP_WIDTH, DISP_HEIGHT) )
        self.state = Game.ST_PLATEFORMER
        self.x_plat_list = list()
        self.y_plat_list = list()
        self.affich_new_plat = True
        self.y_last_affich = 0

    def __del__(self):
        del Game.pl
        del Game.window
        pygame.quit()

    def run(self):
        """gere la boucle d'evenements"""
        prog_done = False
        last_ref = pygame.time.get_ticks()
        self.refreshScreen()
        self.x_plat_list = Game.pl.environ.x_plat_list
        self.y_plat_list = Game.pl.environ.y_plat_list
        
        while not prog_done:
        
            if (abs(self.y_last_affich - Game.pl.y_game)>(600/2)):
                self.affich_new_plat = True
            if (self.affich_new_plat):
                Game.pl.environ.removeAllPlatform()
                for y_plat in self.y_plat_list:
                    if (abs(y_plat - Game.pl.y_game)<(600)):
                        Game.pl.environ.generatePlatform(self.x_plat_list[self.y_plat_list.index(y_plat)], y_plat)
                self.affich_new_plat = False
                self.y_last_affich = Game.pl.y_game
                    
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    prog_done = True
                    break 
                if event.type is pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        prog_done = True
                        break 
                    if event.key == pygame.K_UP:
                        Game.pl.jump()
                    if event.key == pygame.K_RIGHT:
                        Game.pl.startMovingRight()
                    if event.key == pygame.K_LEFT:
                        Game.pl.startMovingLeft()

                if event.type is pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        Game.pl.stopMoving()
                    if event.key == pygame.K_LEFT:
                        Game.pl.stopMoving()

            now = pygame.time.get_ticks()
            if now - last_ref > Fdelay:
                Game.pl.updatePosition()
                Game.pl.environ.current_bonus.collide(Game.pl)
                # TODO affichage des plateformes proches du player
                self.refreshScreen()

    def refreshScreen(self ):
        Game.window.fill(  pygame.Color('BurlyWood') )
        Game.pl.markToDisplay( Game.window ) 
        Game.sk_bar.markToDisplay(Game.window)
        # TODO cest le joueur qui pourrait declencher le declencehement du dessin du terrain
        Game.pl.environ.markToDisplay( Game.window )
        pygame.display.flip() 
          

g = Game()
g.run()
del g
