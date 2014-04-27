from Level import Level
from Matrix import Matrix
import pygame
from global_vars import *
from SkillBox import SkillBox

# plutot que de faire un "vrai" scolling on va faire se deplacer des
# elements type matrix vers le haut de lecran

class PitfallLevel(Level):
    """classe decrivant un environnement de jeu qui simule une chute"""

    def __init__(self):
        self.debut_descente = pygame.time.get_ticks()
        self.val_fin_chute = self.debut_descente + 5000
        self.entity_list = list()
        #ajout d'entites fait ici, mais a modifier
        i = 0
        while i < 60:
            self.entity_list.append(Matrix())
            i += 1
        self.x_plat_list = list()
        self.y_plat_list = list()
        self.current_bonus = SkillBox(-1000,-1000)

    def hasFallEnded(self):
        now = pygame.time.get_ticks()
        if(now > self.val_fin_chute ):
            return True
        return False

    def updateEntities(self ):
        for el in self.entity_list:
            el.update()
        pass

    def markToDisplay(self, window ):
        # affichage d'un fond noir puis blit dessus des lettres
        background = pygame.Surface(window.get_size())
        background = background.convert()
        background.fill((0, 0, 0))
        window.blit(background, (0, 0))
        for el in self.entity_list:
            el.markToDisplay(window)
