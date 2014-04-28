import pygame
import random
from Platform import Platform
from global_vars import *
from SkillBox import SkillBox

from Level import Level 

class DynamicLevel(Level):
    """modelise le decor en gerant le scrolling  pour quil soit toujours centre sur le joueur"""

    VIT_MAX_SCROLLING = 40

    def __init__(self):
        super(DynamicLevel,self).__init__()
        self.amount_scroll = 0.
        self.vit_scrolling = 0.
        self.pl_y_game = 30. # le joueur commence au niveau 0

        self.current_bonus = SkillBox(-DISP_WIDTH, 2*DISP_HEIGHT )
        self.current_bonus.visible = False

        self.xrand_temp = DISP_WIDTH/2
        for i in range(1,1000):
            self.xrand = random.randint(0,DISP_WIDTH-SIZE_SK_BAR-192 )
            while (abs(self.xrand-self.xrand_temp)>700):
                self.xrand = random.randint(0,900)
            self.x_plat_list.append(self.xrand)
            self.y_plat_list.append(i*100 + random.randint(0,10))
            self.xrand_temp = self.xrand

        for i in range(0,5):
            self.generatePlatform(self.x_plat_list[i], self.y_plat_list[i])

    def generateBonus(self):
        self.x_bonus = random.randint(0,DISP_WIDTH-SIZE_SK_BAR-192 )
        self.current_bonus = SkillBox( self.x_bonus, self.pl_y_game+ (DISP_HEIGHT/2) )

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
        self.addEntity( new_plat)
        
    def removePlatform(self, plat_to_remove):
        self.entity_list.remove( plat_to_remove)
        
    def removeAllPlatform(self):
        self.entity_list = list()

    def markToDisplay( self, window):
        window.fill(  pygame.Color('black') )
        super(DynamicLevel,self).markToDisplay( window)

        #affichage du sol
        x_screen, y_screen = game_to_scr_coord( 0,0, self.pl_y_game )
        pygame.draw.rect( window, pygame.Color('darkgray'),
            pygame.Rect(x_screen, y_screen, DISP_WIDTH, DISP_HEIGHT/2 )  )
        #affichage des bonus
        if self.current_bonus.visible:
            self.current_bonus.markToDisplay( window, self.pl_y_game )

    def updateEntities(self ):
        self.current_bonus.updatePosition()

