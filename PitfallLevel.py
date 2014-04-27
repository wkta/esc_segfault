from Level import Level
from Matrix import Matrix
import pygame
import random
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
        self.x_plat_list = list()
        self.y_plat_list = list()
        self.current_bonus = SkillBox(-1000,-1000)

    def hasFallEnded(self):
        now = pygame.time.get_ticks()
        if(now > self.val_fin_chute ):
            return True
        return False

    def updateEntities(self ):
        if not random.randint(0, 3):
            i = 0
            rand = random.randint(1, 10)
            while i < rand:
                self.entity_list.append(Matrix())
                i+=1
        for el in self.entity_list:
            if el.get_pos()[1] < -(el.get_size()[1]):
                el.__del__()
                
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
