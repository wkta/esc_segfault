import pygame
from GameEntity import GameEntity
from DynamicLevel import DynamicLevel 
from global_vars import *

V_MAX_HORZ = 2.
DELTA_V_HORZ = 0.04

class Player(GameEntity):
    BASECOLOR = pygame.Color('darkred')
    BASE_SPEED = 2.
    SIZE = 16
    PUSH_POWER = 32.
    GRAVITE = 2.
    RALENTI = 16.

    def __init__(self, x_game, y_game ):
        self.environ = DynamicLevel()
        self.setXY(x_game,y_game )
        self.YINIT = self.y_game
        self.vx, self.vy = 0., 0.
        self.moving_right = self.moving_left = False
        self.in_air = False
        self.time_in_air = 0.
        self.initGraphics('ludumdare-croquis-chevalier.png',6., -64, -185)

    def startMovingRight(self):
        self.moving_right = True

    def startMovingLeft(self):
        self.moving_left  = True

    def stopMoving(self):
        self.moving_right = False
        self.moving_left  = False

    def setXY( self, new_x, new_y ):
        #super(Player,self).setXY(new_x, new_y )
        GameEntity.setXY(self, new_x, new_y)
        self.environ.scrollTo( new_y)

    def updatePosition(self):
        self.environ.updateEntities()

        #accelerating horizontaly
        if( self.moving_right ):
            if( not abs(self.vx)>V_MAX_HORZ):
                self.vx +=  DELTA_V_HORZ
            if(self.vx + self.x_game >= DISP_WIDTH ): #collision bord
                self.vx = 0
        elif( self.moving_left):
            if( not abs(self.vx)>V_MAX_HORZ):
                self.vx -=  DELTA_V_HORZ
            if(self.vx + self.x_game < 0 ): #collision bord
                self.vx = 0
        else:
            #simulates inertia
            if ( abs(self.vx)>0.1 ):
                self.vx *= 0.97
            else:
                self.vx = 0.  #repos

        if (self.in_air):
            self.vy -= (Player.GRAVITE/Player.RALENTI)
            self.setXY( self.x_game + self.vx,
                self.y_game + \
                self.vy / Player.RALENTI - \
                ( Player.GRAVITE*(1./Player.RALENTI)*(self.time_in_air/Player.RALENTI))/2
                )
            self.time_in_air += 1.
        else:
            self.setXY( self.x_game + self.vx, self.y_game )

        #if not (self.environ.canFall( self.x_game ) ):
            #self.in_air = False
            #self.time_in_air = 0.
        value_fl = self.environ.getValueFloor( self.x_game, self.y_game )
        if (self.y_game <= value_fl): # La valeur qu'il atteind a la fin d'une chute
            self.y_game = value_fl
            self.vy = 0.
            self.in_air = False
            self.time_in_air = 0.
        else:
            self.in_air=True  # falling down

    def jump(self):
        self.vy += Player.PUSH_POWER
        self.in_air = True

    def markToDisplay(self, surface):
        super(Player,self).markToDisplay(surface, self.y_game )
        #x_screen, y_screen= game_to_scr_coord( self.x_game, self.y_game, self.y_game)
        #pygame.draw.circle( surface, pygame.Color('RED') ,
        #    (x_screen, y_screen), Player.SIZE) 

