import pygame
from global_vars import *

class SkillBar(object):
    def __init__(self, player):
        self.ref_pl = player

    def markToDisplay(self, window):
        pygame.draw.rect(window, pygame.Color('BROWN') ,
			pygame.Rect(DISP_WIDTH-SIZE_SK_BAR, 0, SIZE_SK_BAR, DISP_HEIGHT) )
        pygame.draw.rect( window, pygame.Color('BLUE'), pygame.Rect(DISP_WIDTH-SIZE_SK_BAR+20,DISP_HEIGHT/2-100, 40,40))
        pygame.draw.rect( window, pygame.Color('GREEN'), pygame.Rect(DISP_WIDTH-SIZE_SK_BAR+20,DISP_HEIGHT/2, 40,40))
        pygame.draw.rect( window, pygame.Color('YELLOW'), pygame.Rect(DISP_WIDTH-SIZE_SK_BAR+20,DISP_HEIGHT/2+100, 40,40))
        #todo: dessiner les competences en fonction des competences dont dispose le joueur
