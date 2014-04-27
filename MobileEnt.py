import pygame
from GameEntity import GameEntity
from global_vars import *

class MobileEnt(GameEntity):
	"""Classe de base pour les entites mobiles"""

	def __init__(self):
		self.x_game, self.y_game = 0, 0
		self.__INIT_X, self.__INIT_Y = 0, 0
		self.w, self.h = 48, 48 #TODO : des tailles variables ? Laisser les sous classes s'en charger et gérer les collisions dedans ?
		self.vx, self.vy = 0, 0
		self.x_movement, self.y_movement = 0, 0
		pass

	def set_pos(self, x, y):
		self.x_game, self.y_game = x, y
		pass

	def get_pos(self):
		return(self.x_game, self.y_game)

	def set_vect(self, vector):
		self.vx, self.vy = vector[0], vector[1]
		pass

	def get_vect(self):
		return(self.vx, self.vy)

	def move(self):
		self.x_game += self.vx
		self.y_game += self.vy
		pass

	def set_init_pos(self, init_x, init_y):
		self.__INIT_X, self.__INIT_Y = init_x, init_y
		pass

	def get_init_pos(self):
		return(self.__INIT_X, __INIT_Y)

	def set_movement(self, range_x, range_y):
		self.x_movement, self.y_movement = range_x, range_y
		pass

	def get_movement(self):
		return(self.x_movement, self.y_movement)

	def markToDisplay(self, window, pl_y_game):
		x_screen, y_screen = game_to_scr_coord( self.x_game, self.y_game, pl_y_game)
		pygame.draw.rect( window, pygame.Color('RED'),
			pygame.Rect(x_screen, y_screen, self.w, self.h ))
		pass