import pygame
from global_vars import *

class Platform:
	def __init__(self, x_game, y_game):
		self.x_game = x_game
		self.y_game = y_game	
	
	def markToDisplay(self, window, pl_y_game):
		x_screen, y_screen = game_to_scr_coord( self.x_game, self.y_game, pl_y_game )
		pygame.draw.rect( window, pygame.Color('BLUE'),
			pygame.Rect(x_screen, y_screen, 128,32)  )
