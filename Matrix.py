import pygame
import random
from global_vars import *
from MobileEnt import MobileEnt

class Matrix(MobileEnt):

	def __init__(self):
		self.str = chr(random.randint(52, 128))
		self.font = pygame.font.Font(None, 32)
		self.set_pos(random.randint(0, DISP_WIDTH), random.randint(DISP_HEIGHT-50, DISP_HEIGHT))
		self.set_vect_x(0)
		self.set_vect_y(random.randint(-4, -1))
		self.set_size(self.font.size(self.str))
		rand_c = random.randint(60, 250)
		self.text = self.font.render(self.str, 1, (rand_c, 255, rand_c))
		pass

	def __del__(self):
		del self

	def update(self):
		vect_x, vect_y = self.get_vect()
		vect_y *=1.01
		self.set_vect_y(vect_y)
		self.move()
		pass

	def markToDisplay(self, window):
		window.blit(self.text, self.get_pos())
		pass