import pygame
from Platform import Platform

class DynamicLevel:
    """modelise le decor en gerant le scrolling  pour quil soit toujours centre sur le joueur"""

    VIT_MAX_SCROLLING = 40

    def __init__(self):
        self.entity_list = list()
        self.amount_scroll = 0.
        self.vit_scrolling = 0.
        self.pl_y_game = 30. # le joueur commence au niveau 0

        self.generatePlatform()

    def canFall(self, pl_x_game):
        """not pose sur une plateforme"""
        if( self.pl_y_game<= 0):
            return False
        return True

    def scrollTo(self, pl_y_game):
        self.vitesse_scroll = DynamicLevel.VIT_MAX_SCROLLING
        self.amount_scroll = self.pl_y_game - pl_y_game
        self.pl_y_game = pl_y_game

    def generatePlatform(self):
        new_plat = Platform(64., self.pl_y_game)
        self.entity_list.append( new_plat)

    def markToDisplay( self, window):
        for ent in self.entity_list:
            ent.markToDisplay(window)
