import pygame
from GameEntity import GameEntity
from DynamicLevel import DynamicLevel 

class Player(GameEntity):
    BASECOLOR = pygame.Color('darkred')
    BASE_SPEED = 2
    SIZE = 16
    PUSH_POWER = 20.

    def __init__(self, x_game, y_game ):
        # TODO: ajouter vitesse , fonctions de saut et de deplacement
        self.x_game, self.y_game = x_game,y_game
        self.x_screen = x_game
        self.y_screen = y_game
        self.vx = 0
        self.vy = 0
        self.in_air = False
        self.time_in_air = 0
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
        '''self.moving_right = False # on verifie la valeur avant ?
        self.moving_left = False'''

    def updatePosition(self):
        #$if (self.begin_jump):
         #   self.vy = Player.BASE_SPEED - self.time_in_air

        if not (self.moving_right or self.moving_left):
            self.vx = 0.
        else:
            if self.moving_right:
                self.vx = Player.BASE_SPEED
            if self.moving_left:
                self.vx = -Player.BASE_SPEED

        if (self.environ.canFall):#valeur a recuperer du decor):
            self.in_air = False
            self.time_in_air = 0

        if (self.in_air):
            self.time_in_air += 1
            self.x_game += self.vx * self.time_in_air
            self.x_screen = self.x_game
            self.y_game += self.vy * self.time_in_air - ((self.time_in_air)^2)/2
            self.y_screen = self.y_game
        else:
            self.x_game += self.vx
            self.x_screen = self.x_game

    def jump(self):
        self.vy += Player.PUSH_POWER
        self.in_air = True

    def test(self):
        print "yoyo"

    def markToDisplay(self, surface):
        pygame.draw.circle( surface, pygame.Color('RED') ,
            (int(self.x_game ),int(self.y_game )), Player.SIZE) 
