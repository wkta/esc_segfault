import pygame
from GameEntity import GameEntity
from DynamicLevel import DynamicLevel 
from global_vars import *

class Player(GameEntity):
    BASECOLOR = pygame.Color('darkred')
    BASE_SPEED = 2.
    SIZE = 16
    PUSH_POWER = 10.
    GRAVITE = 1.
    RALENTI = 1.

    def __init__(self, x_game, y_game ):
        # TODO: ajouter vitesse , fonctions de saut et de deplacement
        self.x_game, self.y_game = x_game,y_game
        self.x_screen = x_game
        self.y_screen = y_game
        self.YINIT = self.y_game
        self.vx = 0.
        self.vy = 0.
        self.in_air = False
        self.time_in_air = 0.
        self.environ = DynamicLevel()
        # self.img = 
        self.moving_right = self.moving_left = False

    def startMovingRight(self):
        self.moving_right = True
        self.moving_left  = False

    def startMovingLeft(self):
        self.moving_left  = True
        self.moving_right = False

    def stopMoving(self):
        self.moving_right = False
        self.moving_left  = False

    def setY( self, new_y ):
        self.y_game = new_y
        self.environ.scrollTo( new_y)

    def updatePosition(self):

        if not (self.moving_right or self.moving_left):
            self.vx = 0.
        else:
            if self.moving_right:
                self.vx = Player.BASE_SPEED
            if self.moving_left:
                self.vx = -Player.BASE_SPEED

        if not (self.environ.canFall):
            self.in_air = False
            self.time_in_air = 0.

        if (self.in_air):
            self.x_game += self.vx
            self.x_screen = self.x_game
            #self.vy -= (Player.GRAVITE*self.time_in_air/Player.RALENTI)
            #self.y_game += self.vy * self.time_in_air/Player.RALENTI - (Player.GRAVITE*(self.time_in_air/Player.RALENTI)*(self.time_in_air/Player.RALENTI))/2
            self.vy += (Player.GRAVITE/Player.RALENTI)
            self.setY( self.y_game - \
                self.vy / Player.RALENTI - (Player.GRAVITE*(1./Player.RALENTI)*(self.time_in_air/Player.RALENTI))/2
                )

            self.y_screen = self.y_game
            self.time_in_air += 1.
            print(self.y_game, self.time_in_air)
        else:
            self.x_game += self.vx
            self.x_screen = self.x_game

        if (self.y_game <= self.YINIT): # La valeur qu'il atteind a la fin d'une chute
            self.y_game = self.YINIT
            self.vy = 0.
            self.in_air = False
            self.time_in_air = 0.

    def jump(self):
        #self.vy += Player.PUSH_POWER
        self.vy -= Player.PUSH_POWER
        self.in_air = True

    def test(self):
        print "yoyo"

    def markToDisplay(self, surface):
        x_screen, y_screen= game_to_scr_coord( self.x_game, self.y_game, self.y_game)
        pygame.draw.circle( surface, pygame.Color('RED') ,
            (x_screen, y_screen), Player.SIZE) 

