# LUDUM DARE 29: ESCAPE THE SEGFAULT!

import pygame
import random
from Player import Player
from SkillBar import SkillBar 
from time import sleep

from  IntroScreen import IntroScreen 
from DynamicLevel import DynamicLevel
from PitfallLevel import PitfallLevel

from global_vars import *

Fdelay = 1000 / FPS

class Game:
    """ permet de faire tourner le jeu avec boucles d'evenement et gestion de l'etat du jeu"""
    pl = None
    window = None

    ST_INTRO = 0
    ST_PLATEFORMER = 1
    ST_GAME_OVER = 2
    ST_GAME_FALL = 3
    ST_QUIT = 9

    def __init__(self):
        pygame.init()
        Game.pl = Player( 0, 0 )  #TODO :  position realiste

        self.prepareNewState( )
        self.updateState()

        self.last_refr = pygame.time.get_ticks()

        Game.sk_bar = SkillBar( Game.pl )
        Game.window = pygame.display.set_mode( (DISP_WIDTH, DISP_HEIGHT) )
        self.x_plat_list = list()
        self.y_plat_list = list()
        self.affich_new_plat = True
        self.y_last_affich = 0

    def updateState(self ):
        if(self.future_state==None):
            raise Exception('no future state')

        if(self.future_state==Game.ST_INTRO):
            Game.pl.setEnviron( IntroScreen("hoj hoj hoj")  )
        elif(self.future_state==Game.ST_GAME_FALL):
            Game.pl.setEnviron( PitfallLevel() )
        elif(self.future_state==Game.ST_PLATEFORMER):
            Game.pl.setEnviron( DynamicLevel() )
        elif(self.future_state==Game.ST_QUIT):
            pass
        else:
            raise Exception('unknown future state')
        self.state = self.future_state
        self.future_state = None

    def prepareNewState(self,new_st=ST_INTRO):
        self.future_state = new_st

    def hasNewState(self):
        return not (self.future_state==None)

    def __del__(self):
        del Game.pl
        del Game.window
        pygame.quit()


    def run(self):
        """gere la boucle d'evenements"""
        prog_done = False
        self.x_plat_list = None
        self.y_plat_list = None
       
        while True:
            if(self.state==Game.ST_INTRO):
                f_events = self.processEvIntro
                f_play = self.playIntro
            elif(self.state==Game.ST_GAME_FALL):
                f_events = self.processEvFall
                f_play = self.playFall
            elif(self.state==Game.ST_PLATEFORMER):
                f_events = self.processEvPlatformer
                f_play = self.playPlateformer
            else:
                raise Exception('unknown game state')

            while not self.hasNewState():
                time_now = pygame.time.get_ticks()

                #controles
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        self.prepareNewState( Game.ST_QUIT)
                        continue
                    if event.type is pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.prepareNewState( Game.ST_QUIT)
                        continue
                    f_events( event )
                #modele et affichage
                f_play( time_now )

            #mise a jour etat jeu
            self.updateState() 
            if(self.state==Game.ST_QUIT):
                break


    def processEvPlatformer(self, event): 
        if event.type is pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Game.pl.jump()
            if event.key == pygame.K_RIGHT:
                Game.pl.startMovingRight()
            if event.key == pygame.K_LEFT:
                Game.pl.startMovingLeft()
        if event.type is pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                Game.pl.stopMoving()
            if event.key == pygame.K_LEFT:
                Game.pl.stopMoving()

    def processEvIntro(self, event):
        if event.type is pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.prepareNewState( Game.ST_GAME_FALL)

    def processEvFall(self,event):
        return

    def playIntro(self,time):
        self.refreshScreen()

    def playFall(self,time):
        if( Game.pl.environ.hasFallEnded() ):
            self.prepareNewState( Game.ST_PLATEFORMER)
        Game.pl.environ.updateEntities()
        self.refreshScreen()

    def playPlateformer(self, time ):
        self.x_plat_list = Game.pl.environ.x_plat_list
        self.y_plat_list = Game.pl.environ.y_plat_list
        if (abs(self.y_last_affich - Game.pl.y_game)>(600/2)):
            self.affich_new_plat = True
        if (self.affich_new_plat):
            #print(len(Game.pl.environ.entity_list))
            Game.pl.environ.removeAllPlatform()
            #print(len(Game.pl.environ.entity_list))
            for y_plat in self.y_plat_list:
                #print(len(Game.pl.environ.entity_list))
                if (abs(y_plat - Game.pl.y_game)<(600)):
                    Game.pl.environ.generatePlatform(self.x_plat_list[self.y_plat_list.index(y_plat)], y_plat)
            self.affich_new_plat = False
            self.y_last_affich = Game.pl.y_game
            #print(len(Game.pl.environ.entity_list))
        Game.pl.environ.current_bonus.collide(Game.pl)
        #gestion bonus
        if not Game.pl.environ.current_bonus.visible:
            if random.randint(1,5000) == 42:
                Game.pl.environ.generateBonus()
                x_bonus, y_bonus = Game.pl.environ.current_bonus.getXY()
                if (Game.pl.y_game-y_bonus>DISP_HEIGHT*2):
                    Game.pl.environ.current_bonus.visible = False
        #fin gestion bonus
        #fin gestion plateformes

        Game.pl.environ.updateEntities()
        #if( time- self.last_refr <= Fdelay ):
            #return
        Game.pl.updatePosition()
        self.refreshScreen()

    def refreshScreen(self):
        Game.pl.environ.markToDisplay( Game.window )
        if( self.state==Game.ST_PLATEFORMER ):
            Game.sk_bar.markToDisplay(Game.window)
            Game.pl.markToDisplay( Game.window ) 
        # TODO cest le joueur qui pourrait declencher le declencehement du dessin du terrain
        pygame.display.flip() 
        self.last_refr = pygame.time.get_ticks()
          

g = Game()
g.run()
del g
