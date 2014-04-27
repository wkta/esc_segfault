import pygame
import random
from GameEntity import GameEntity
from PitfallLevel import PitfallLevel 
from DynamicLevel import DynamicLevel 
from global_vars import *

class Decor(GameEntity):

    def __init__(self, x_game, y_game ):
        self.environ=PitfallLevel()
        self.setXY(x_game,y_game )
        self.YINIT = self.y_game
        self.vx, self.vy = 0., 0.
        self.moving_right = self.moving_left = False
        self.in_air = False
        self.time_in_air = 0.
        self.rand = random.randint(1,2)
        if self.rand == 1:
            self.initGraphics('ludumdare-croquis-composant.png',6., -64, -185)
        else:
            self.initGraphics('ludumdare-croquis-composant2.png',6., -64, -185)
        self.list_bonus = list()


    def markToDisplay(self, surface):
        super(Decor,self).markToDisplay(surface, self.y_game )




























