import pygame
from Platform import Platform
from global_vars import *
from SkillBox import SkillBox

class DynamicLevel:
    """modelise le decor en gerant le scrolling  pour quil soit toujours centre sur le joueur"""

    VIT_MAX_SCROLLING = 40

    def __init__(self):
        self.entity_list = list()
        self.amount_scroll = 0.
        self.vit_scrolling = 0.
        self.pl_y_game = 30. # le joueur commence au niveau 0

        self.current_bonus = None
        self.generateBonus()

        self.generatePlatform(32, 100)
        self.generatePlatform(512, 200)
        self.generatePlatform(800, 312)

    def generateBonus(self):
        if( None != self.current_bonus):
            return
        self.current_bonus = SkillBox( DISP_WIDTH/2, self.pl_y_game+ (DISP_HEIGHT/2) )

    def getValueFloor(self, pl_x_game, pl_y_game):
        """retourne position y de la plateform la plus proche"""
        sub_entity_l = list()
        #constr list entite quon peut taper en tombant
        for ent in self.entity_list:
            if( ent.canHit( pl_x_game) ):
                sub_entity_l.append( ent)
        # TODO sort
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
        #affichage des plateformes
        for ent in self.entity_list:
            ent.markToDisplay(window,self.pl_y_game)
        #affichage du sol
        x_screen, y_screen = game_to_scr_coord( 0,0, self.pl_y_game )
        pygame.draw.rect( window, pygame.Color('BLACK'),
            pygame.Rect(x_screen, y_screen, DISP_WIDTH, DISP_HEIGHT/2 )  )
        #affichage des bonus
        self.current_bonus.markToDisplay( window, self.pl_y_game )

    def updateEntities(self ):
        self.current_bonus.updatePosition()

