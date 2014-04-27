import pygame
from Level import Level

class IntroScreen(Level):
    FONTSIZE = 64

    def __init__(self, text, max_t_len = 64, offset_y = 0):
        self.font = pygame.font.SysFont("comicsansms", 64)

        self.text = text
        self.max_t_len = max_t_len
        self.offset_y = offset_y
        self.text_disp = True

    def turnDispOn(self):
        self.text_disp = True

    def turnDispOff(self):
        self.text_disp = False

    def markToDisplay(self,surface):
        surface.fill(  pygame.Color('black') )

        #creation de labels pour autant de lignes
        remaining = self.text
        local_offset = self.offset_y
        substr = self.text
        while ( len(remaining)>self.max_t_len  ):
            substr = self.text[ :self.max_t_len ]
            remaining = self.text[ self.max_t_len: ]
            label = self.font.render( substr, 1, (0, 255, 0) )
            surface.blit( label, (0, local_offset ))
            local_offset += FONTSIZE+4

        #label final
        label = self.font.render( substr, 1, (0, 255, 0) )
        surface.blit( label, (0, local_offset ))
        
