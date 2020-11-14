import random

import pygame

from GameEntity import GameEntity
from PitfallLevel import PitfallLevel
from global_vars import *
import global_vars as glvars


V_MAX_HORZ = 2.
DELTA_V_HORZ = 0.04


class Player(GameEntity):

    BASECOLOR = pygame.Color('darkred')
    BASE_SPEED = 2.
    SIZE = 16
    PUSH_POWER = 32.
    GRAVITE = 2.
    RALENTI = 16.

    def dist(self, ent):
        return abs(ent.y_game - self.y_game)

    def setEnviron(self, env):
        self.environ = env

    def hasSkill(self, id_sk):
        return (id_sk in self.dict_bonus.keys())

    def __init__(self, x_game, y_game):
        self.prev_score = HEIGHT_VICTORY
        self.environ = PitfallLevel()
        self.setXY(x_game, y_game)
        self.YINIT = self.y_game
        self.vx, self.vy = 0., 0.
        self.moving_right = self.moving_left = False
        self.in_air = False
        self.megaj = False

        self.time_in_air = 0.
        self.initGraphics('ludumdare-croquis-chevalier.png', 6., -64, -180)
        self.dict_bonus = dict()
        self.is_dead = False
        self.has_won = False

    def isDead(self):
        return self.is_dead

    def hasWon(self):
        return self.has_won

    def startMovingRight(self):
        self.moving_right = True

    def startMovingLeft(self):
        self.moving_left = True

    def stopMoving(self):
        self.moving_right = False
        self.moving_left = False

    def setXY(self, new_x, new_y):
        # super(Player,self).setXY(new_x, new_y )
        GameEntity.setXY(self, new_x, new_y)
        self.environ.scrollTo(new_y)

    def updatePosition(self):
        self.environ.updateEntities()

        # accelerating horizontaly
        if self.moving_right:
            if not abs(self.vx) > V_MAX_HORZ:
                self.vx += DELTA_V_HORZ
            if self.vx + self.x_game + self.getWidth() / 3 > DISP_WIDTH - SIZE_SK_BAR:  # collision bord droit
                self.vx = 0

        elif self.moving_left:
            if not abs(self.vx) > V_MAX_HORZ:
                self.vx -= DELTA_V_HORZ
            if self.vx + self.x_game < 0:  # collision bord
                self.vx = 0

        else:
            # simulates inertia
            if abs(self.vx) > 0.1:
                self.vx *= 0.9
            else:
                self.vx = 0.  # repos

        if self.in_air:
            self.vy -= (Player.GRAVITE / Player.RALENTI)

            y_future = self.y_game + (self.vy / Player.RALENTI)
            y_future -= (Player.GRAVITE * (1. / Player.RALENTI) * (self.time_in_air / Player.RALENTI)) / 2
            if y_future < self.y_game:
                self.megaj = False
            self.setXY(self.x_game + self.vx, y_future)

            # test pr victoire
            if self.y_game > HEIGHT_VICTORY:
                self.has_won = True
                return
            self.time_in_air += 1.
        else:
            self.setXY(self.x_game + self.vx, self.y_game)

        if self.megaj:  # ignore collisions when megajumping
            return

        value_fl = self.environ.getValueFloor(self.x_game, self.y_game)
        if (self.y_game <= value_fl):  # La valeur qu'il atteind a la fin d'une chute
            # collision avec sol/plateforme
            if (self.vy < 0 and self.vy < - glvars.LETHAL_SPEED):  # mort
                print("You just died.")
                self.is_dead = True
            self.y_game = value_fl
            self.vy = 0.
            self.in_air = False
            self.time_in_air = 0.
        else:
            self.in_air = True  # falling down

    def megajump(self):
        if (len(self.dict_bonus.keys()) == 0):
            return
        self.vy += Player.PUSH_POWER * 3
        self.in_air = True
        self.megaj = True

        if (3 in self.dict_bonus):
            del self.dict_bonus[3]
            return
        if (2 in self.dict_bonus):
            del self.dict_bonus[2]
            return
        if (1 in self.dict_bonus):
            del self.dict_bonus[1]
            return

    def jump(self):
        if (self.in_air == False):
            self.vy += Player.PUSH_POWER
        self.in_air = True

    def markToDisplay(self, surface):
        super(Player, self).markToDisplay(surface, self.y_game)
        x_screen, y_screen = game_to_scr_coord(self.x_game, self.y_game, self.y_game)
        sfx_color = (pygame.Color('yellow') if self.has_won else pygame.Color('red'))
        if (self.is_dead or self.has_won):
            for i in range(512):
                a, b = random.randint(-64, 64), random.randint(-172, -8)
                surface.set_at((x_screen + a, y_screen + b), sfx_color)
                surface.set_at((-1 + x_screen + a, y_screen + b), sfx_color)
                surface.set_at((+1 + x_screen + a, y_screen + b), sfx_color)
                surface.set_at((x_screen + a, 1 + y_screen + b), sfx_color)

    def getScore(self):
        n_score = HEIGHT_VICTORY - int(self.y_game)
        if (n_score <= 0):
            return 0
        if (abs(n_score - self.prev_score) < 15):
            return self.prev_score
        self.prev_score = n_score
        return n_score
