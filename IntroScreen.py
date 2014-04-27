import pygame
from Level import Level
from global_vars import *

class IntroScreen(Level):
    FONTSIZE = 32

    def __init__(self, text, max_t_len = 40, offset_y = 0):
        self.font = pygame.font.SysFont("courier", IntroScreen.FONTSIZE)

        self.text = text
        self.max_t_len = max_t_len
        self.offset_y = offset_y
        self.text_disp = True
        self.current_bonus = None

    def turnDispOn(self):
        self.text_disp = True

    def turnDispOff(self):
        self.text_disp = False

    def markToDisplay(self,surface):
        surface.fill(  pygame.Color('black') )

        #creation de labels pour autant de lignes
        remaining = self.text
        local_offset = self.offset_y
        while ( len(remaining)>self.max_t_len  ):
            remaining= remaining[ self.max_t_len: ]
            substr= remaining[ :self.max_t_len ]
            label = self.font.render( substr, 1, (0, 255, 0) )
            surface.blit( label, ( (DISP_WIDTH/2)-428, local_offset ))
            local_offset += IntroScreen.FONTSIZE+4

        #label final
        #label = self.font.render( substr, 1, (0, 255, 0) )
        #surface.blit( label, (0, local_offset ))
        
