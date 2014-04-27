from MobileEnt import MobileEnt

class Glitch(MobileEnt):
	"""Classe qui permet de generer des glitch et de definir leurs mouvements"""

	def __init__(self, x_game, y_game, x_movement, y_movement, size, color):
		self.set_pos(x_game, y_game)
		self.set_init_pos(x_game, y_game)
		self.set_movement(x_movement, y_movement)
		self.set_size(size)
		self.set_color(color)
		pass

	def inverse_vector_x(self):
		vector_x, vector_y = self.get_vect()
		self.set_vect((-vector_x, vector_y))
		pass

	def inverse_vector_y(self):
		vector_x, vector_y = self.get_vect()
		self.set_vect((vector_x, -vector_y))
		pass

	#TODO : un mouvement qui ralentit avant d'atteindre la limite et reprends de la vitesse dans l'autre sens si le temps le permet
	def update_pos(self):
		if self.get_movement()[0]:
			if abs(self.get_init_pos()[0] - self.get_pos()[0]) > self.get_movement()[0]:
				self.inverse_vector_x()
		if self.get_movement()[1]:
			if abs(self.get_init_pos()[1] - self.get_pos()[1]) > self.get_movement()[1]:
				self.inverse_vector_y()
		self.move()


