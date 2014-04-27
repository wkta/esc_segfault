import pygame
from global_vars import *

class Platform:
    markToDisplay = 'yo'

    def __init__(self, x_game, y_game):
        self.x_game = x_game
        self.y_game = y_game	
        self.w, self.h = 128,12
	
    def markToDisplay(self, window, pl_y_game):
		x_screen, y_screen = game_to_scr_coord( self.x_game, self.y_game, pl_y_game )
		pygame.draw.rect( window, pygame.Color('BLUE'),
            pygame.Rect(x_screen, y_screen, self.w, self.h )  )

    def canHit(self,pl_x_game):
        res = (pl_x_game > self.x_game) and ( pl_x_game <= (self.x_game+self.w) )
        return res

    def getValFloor(self):
        return self.y_game + self.h

    def isUnder(self, y_game):
        return y_game < self.y_game 
