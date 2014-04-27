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
		self.color = pygame.Color('WHITE')
		pass

	def set_pos(self, x, y):
		self.x_game, self.y_game = x, y
		pass

	def get_pos(self):
		return(self.x_game, self.y_game)

	def set_color(self, color):
		self.color = color
		pass

	def get_color(self):
		return self.color

	def set_size(self, size):#tuple size attendu
		self.w, self.h = size
		pass

	def get_size(self):
		return self.w, self.h

	def set_vect(self, vector):#tuple vector attendu
		self.vx, self.vy = vector
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
		x, y = self.get_pos()
		width, height = self.get_size()
		x_screen, y_screen = game_to_scr_coord(x, y, pl_y_game)
		pygame.draw.rect(window, self.get_color(),
			pygame.Rect(x_screen, y_screen, width, height))
		pass