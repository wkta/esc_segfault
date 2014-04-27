from Level import Level
import pygame
from global_vars import *

# plutot que de faire un "vrai" scolling on va faire se deplacer des
# elements type matrix vers le haut de lecran

class PitfallLevel(Level):
    """classe decrivant un environnement de jeu qui simule une chute"""

    def __init__(self):
        self.debut_descente = pygame.time.get_ticks()
        self.val_fin_chute = self.debut_descente + 5000
        self.entity_list = list()
        self.x_plat_list = list()
        self.y_plat_list = list()

    def hasFallEnded(self):
        now = pygame.time.get_ticks()
        if(now > self.val_fin_chute ):
            return True
        return False

    def updateEntities(self ):
        pass

    def markToDisplay(self, window ):
        # affichage du rect pour debug collisions
        pygame.draw.rect(window, pygame.Color('YELLOW'),
            (0, 0, DISP_WIDTH, DISP_HEIGHT)  )

    def getValueFloor(self, x,y):
        return 0
