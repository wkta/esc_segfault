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

	