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
		self.color = pygame.Color('GREEN')
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

	def set_size(self, size): #tuple size attendu
		self.w, self.h = size
		pass

	def get_size(self):
		return self.w, self.h

	def set_vect_x(self, vector_x, vector_y):
		self.vx = vector_x
		pass

	def set_vect_y(self, vector_y):
		self.vy = vector_y
		pass

	def get_vect(self):
		return(self.vx, self.vy)

	def move(self):
		self.x_game += self.vx
		self.y_game += self.vy
		pass

	def set_init_pos(self, pos_init):
		self.__POS_INIT__ = pos_init
		pass

	def get_init_pos(self):
		return(self.__POS_INIT__)

	def set_movement(self, range_xy): #tuple range x et y attendu
		self.movement = range_xy
		pass

	def get_movement(self):
		return(self.movement)
