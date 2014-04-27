import pygame
from Level import Level
from global_vars import *

import os

def load_image(name ):
    fullname = os.path.join('assets', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    return image, image.get_rect()


class IntroScreen(Level):
    FONTSIZE = 32

    def __init__(self, text, max_t_len = 40, offset_y = 0):
        self.font = pygame.font.SysFont("courier", IntroScreen.FONTSIZE)

        self.text = text
        self.max_t_len = max_t_len
        self.offset_y = offset_y
        self.text_disp = True
        self.current_bonus = None
        self.turnImgOn()

    def turnImgOn(self):
        self.img, self.noneed_rect = load_image( 'ecran_intro.png')
        self.img_disp= True

    def turnImgOff(self):
        self.img_disp = False

    def markToDisplay(self,surface):
        surface.fill(  pygame.Color('black') )

        if(self.img_disp):
            surface.blit( self.img, (0,0)  )

        if(self.img_disp):  #code debile a corriger
            return

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
        
