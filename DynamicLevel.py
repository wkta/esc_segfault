import pygame
import random
from Platform import Platform
from global_vars import *

class DynamicLevel:
    """modelise le decor en gerant le scrolling  pour quil soit toujours centre sur le joueur"""

    VIT_MAX_SCROLLING = 40

    def __init__(self):
        self.entity_list = list()
        self.amount_scroll = 0.
        self.vit_scrolling = 0.
        self.pl_y_game = 30. # le joueur commence au niveau 0

        self.xrand_temp = 512
        for i in range(1,100):
            self.xrand = random.randint(0,900)
            while (abs(self.xrand-self.xrand_temp)>700):
                self.xrand = random.randint(0,900)
            self.generatePlatform(self.xrand, i*100 + random.randint(0,10))
            self.xrand_temp = self.xrand

    def getValueFloor(self, pl_x_game, pl_y_game):
        """retourne position y de la plateform la plus proche"""
        sub_entity_l = list()
        #constr list entite quon peut taper en tombant
        for ent in self.entity_list:
            if( ent.canHit( pl_x_game) ):
                sub_entity_l.append( ent)
        # TODO sort
        sub_entity_l.reverse()
        for ent in sub_entity_l:
            if( ent.isUnder( pl_y_game) ):
                continue
            return ent.getValFloor()
        return 0
    
    def canFall(self, pl_x_game):
        """not pose sur une plateforme"""
        if( self.pl_y_game<= 0):
            return False
        return True

    def scrollTo(self, pl_y_game):
        self.vitesse_scroll = DynamicLevel.VIT_MAX_SCROLLING
        self.amount_scroll = self.pl_y_game - pl_y_game
        self.pl_y_game = pl_y_game

    def generatePlatform(self, x_game_start, y_game):
        new_plat = Platform( x_game_start,  y_game)
        self.entity_list.append( new_plat)

    def markToDisplay( self, window):
        for ent in self.entity_list:
            ent.markToDisplay(window,self.pl_y_game)
        x_screen, y_screen = game_to_scr_coord( 0,0, self.pl_y_game )
        pygame.draw.rect( window, pygame.Color('BLACK'),
            pygame.Rect(x_screen, y_screen, DISP_WIDTH, DISP_HEIGHT/2 )  )

