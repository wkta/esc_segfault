import pygame
import random
from global_vars import *
from MobileEnt import MobileEnt

class Matrix(MobileEnt):

	def __init__(self):
		self.str = chr(random.randint(33, 128))
		self.font = pygame.font.Font(None, 32)
		self.set_pos(random.randint(0, DISP_WIDTH), 0)
		self.set_init_pos(self.get_pos())
		self.set_movement((0, DISP_HEIGHT))
		self.set_vect_y(random.randint(1, 4))
		self.set_size(pygame.font.size(self.str))
		self.text = self.font.render(self.str, 1, (255, 255, 255))
		pass

	#TODO : Un effet sympa serait que la vitesse augmente entre le début et la fin (pour l'instant, vitesse aléatoire)
	def update(self):
		if  abs(self.get_pos()[1] - self.get_init_pos()()[1]) > self.get_movement()[1]:
			self.__del__()
		else:
			self.move()
		pass

	def markToDisplay(self, window, pl_y_game):
		x, y = self.get_pos()

		x_screen, y_screen = game_to_scr_coord(x, y, pl_y_game)
		window.blit(self.text, self.get_pos())
		pass