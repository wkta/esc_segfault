import pygame

class MobileEnt(GameEntity):
	"""Classe de base pour les entites mobiles"""
	def __init__(self):
		self.x, self.y = 0, 0
		self.vx, self.vy = 0, 0
		pass

	def set_pos(self, x, y):
		self.x, self.y = x, y
		pass

	def get_pos(self):
		return(self.x, self.y)

	def set_vect(self, vx, vy):
		self.vx, self.vy = vx, vy

	def get_vect(self):
		return(self.vx, self.vy)