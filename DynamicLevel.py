import pygame

class DynamicLevel:

    def __init__(self):
        self.level_pl = 0 # le joueur commence au niveau 0
        pass

    def canFall(self, pl_x_game):
        return False

    def scrollTo(self, pl_y_game):
        self.level_pl = pl_y_game
