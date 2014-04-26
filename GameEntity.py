#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import os
from math import ceil

loaded_data_img = dict()

class GameEntity:
    """sert a decrire une entite du jeu"""

    #TODO :faut -il avoir un x, y _jeu dans cette classe ?

    def __init__(self, fich_img, resize_fact = 1. ):
        pass

#        self.sprite = pygame.sprite.Sprite()
  #      self.initGraphics( fich_img, resize_fact )
   #     self.way = "left"

    def initGraphics(self, fich_img, resize_fact ):
        if(not fich_img in img_data.keys() ):
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
            img_data[ fich_img] = (tmp_img, tmp_rect)
        self.image, self.rect = img_data[fich_img ][0], img_data[fich_img][1].copy()

    def changeWay(self):
        self.image = pygame.transform.flip(self.image, 1, 0)


def load_image(name ):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    return image, image.get_rect()

