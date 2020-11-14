#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import os
from math import ceil
from global_vars import *

loaded_data_img = dict()

class GameEntity(object):
    """sert a decrire une entite du jeu"""

    DEF_WIDTH, DEF_HEIGHT = 40,40

    #TODO :faut -il avoir un x, y _jeu dans cette classe ?


    def __init__(self ):
#, fich_img, resize_fact = 1. ):
        self.image = None
        self.rect = pygame.Rect(0,0,GameEntity.DEF_WIDTH, GameEntity.DEF_HEIGHT)
        self.offset_x , self.offset_y = 0,0
        self.way = "left"
        self.visible = True
        self.col = ''

    def initGraphics(self, fich_img, resize_fact, offset_x, offset_y ):
        if(not fich_img in loaded_data_img.keys() ):
            tmp_img, tmp_rect = load_image( fich_img )
            #resizing
            if (resize_fact!=1. ):
                curr_width,curr_height = tmp_img.get_width(), tmp_img.get_height()
                n_width = int( ceil( curr_width  / resize_fact))
                n_height = int( ceil( curr_height  / resize_fact))
                delta_x = curr_width - n_width
                delta_y = curr_height - n_height
                tmp_img = pygame.transform.scale(tmp_img, (n_width,n_height) )
                #application de la meme reduction sur le Rect (utile pour collider)
                tmp_rect.inflate_ip( -delta_x-16, -delta_y-16 )  #4 & 16 for artificial reduce of collisions
            loaded_data_img[ fich_img] = (tmp_img, tmp_rect)
        self.image, self.rect = loaded_data_img[fich_img ][0], \
            loaded_data_img[fich_img][1].copy()
        self.offset_x = offset_x
        self.offset_y = offset_y

    def getWidth(self):
        if(self.image !=None):
            return self.rect.width
        return 128

    def changeWay(self):
        self.image = pygame.transform.flip(self.image, 1, 0)

    def collide(self, entite):
        #TODO: utiliser la fonction getRect
        x_ent, y_ent = entite.getXY()
        if (abs(self.x_game - x_ent )<40 and abs(self.y_game - y_ent) <40):
            if self.visible == True:  #implique aussi que cest un skill box
                entite.dict_bonus[ self.skill_id ]=True
            self.visible = False
            return True
        return False

    def getRect(self):
        return self.rect

    def setXY(self, new_x, new_y ):
        self.x_game = new_x
        self.y_game = new_y

    def getXY(self):
        return self.x_game,self.y_game

    def markToDisplay(self, window, pl_y_game ):
        x_screen, y_screen = game_to_scr_coord(self.x_game, self.y_game, pl_y_game)
        # affichage du rect pour debug collisions
        if DEBUG_RECTS:
            pygame.draw.rect(window, pygame.Color('RED') ,
                (x_screen, y_screen-self.getRect().height, self.getRect().width, self.getRect().height ) )

        # association (pour fixer un bug rapidement) entre couleur str et tuple(r,g,b)
        fast_convert = {
            'BLUE': (10, 10, 245),
            'GREEN': (10, 220, 25),
            'YELLOW': (88, 88, 3)
        }

        if self.image is None and hasattr(self, 'skill_id'):
            if self.skill_id == 1:
                self.col = 'BLUE'
            elif self.skill_id == 2:
                self.col = 'GREEN'
            elif self.skill_id == 3:
                self.col = 'YELLOW'
            else:
                print('** warning: skill_id= {}'.format(self.skill_id))
            pygame.draw.rect(window, fast_convert[self.col], (x_screen, y_screen-40, 40, 40))
            return

        blit_target = (x_screen+self.offset_x, y_screen+self.offset_y)
        window.blit(self.image, blit_target)

    def updatePosition(self, surface):
        #by default, we do nothing to update the position of the game entity
        pass


def load_image(name ):
    fullname = os.path.join('assets', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:'+ fullname)
        print(message)
        raise SystemExit
    return image, image.get_rect()
