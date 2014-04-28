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

E_LINE =''.join([' ' for i in xrange(34)])  #very dirty way to print an empty line in a intro screen
class Game:
    """ permet de faire tourner le jeu avec boucles d'evenement et gestion de l'etat du jeu"""
    pl = None
    window = None
    
    TEXT_VICT = "                                  You have won! Congratulations.    You should be able to save the    princess now. Oh. Wait. We forgot to code this part,sorry :) Thanks for playing!                      ***Credits***             " \
        + E_LINE + \
        "Code:     Thomas Iwaszko                    Antoine Favre-Felix               Alexandre Thiry " +\
        E_LINE +\
        "      Graphics:   Fabien Hulot"

    ST_INTRO = 0
    ST_PLATEFORMER = 1
    ST_GAME_OVER = 2
    ST_GAME_FALL = 3

    ST_VICTORY = 8
    ST_QUIT = 9

    def __init__(self):
        self.switch_img = False #dirty trick press enter intro screen

        pygame.init()
        self.fake_depth = 0
        self.font = pygame.font.SysFont("courier", 24)  #will be used to disp score

        Game.pl = Player( 0,0)  #TODO :  position realiste

        self.prepareNewState( )
        self.updateState()

        #self.last_refr = pygame.time.get_ticks()

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
            Game.pl.setEnviron( IntroScreen("                                  In this Ludum Dare#29 game,you are the brave hero who must save the princess!! Unfortunately, due  to drunk python coders the game is   super bugged.  While  you    walk towards her, you bump into a BIG  bug and fall into the depths of    the  software,beneath the surface ..."+\
"(collect cubes and press  UP  for  megajump)"
            ,  34
            ,84 )
                )
        elif(self.future_state==Game.ST_GAME_FALL):
            Game.pl.setEnviron( PitfallLevel() )
            Game.pl.setXY( DISP_WIDTH/2, DISP_HEIGHT/2  )
        elif(self.future_state==Game.ST_PLATEFORMER):
            Game.pl.setEnviron( DynamicLevel() )
            Game.pl.setXY( DISP_WIDTH/2, 0)
        elif(self.future_state==Game.ST_VICTORY):
            end_screen = IntroScreen( Game.TEXT_VICT,  34, 50)
            end_screen.turnImgOff()
            Game.pl.setEnviron( end_screen)
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
            elif(self.state==Game.ST_VICTORY):
                f_events = self.processEvIntro
                f_play = self.playIntro
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
        if event.type is pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                Game.pl.stopMoving()
            if event.key == pygame.K_LEFT:
                Game.pl.stopMoving()
        if (Game.pl.isDead() or Game.pl.hasWon() ):  #controles bloque quand joueur mort/a gagne
            return
        if event.type is pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if(not Game.pl.megaj ):
                    Game.pl.megajump()
            if event.key == pygame.K_SPACE:
                Game.pl.jump()
            if event.key == pygame.K_RIGHT:
                Game.pl.startMovingRight()
            if event.key == pygame.K_LEFT:
                Game.pl.startMovingLeft()

    def processEvIntro(self, event):
        if event.type is pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if(Game.pl.has_won  ):  #deja fini le jeu
                    self.prepareNewState(Game.ST_QUIT )
                    return
        
                #le jeu commence
                if(self.switch_img):
                    self.prepareNewState( Game.ST_GAME_FALL)
                else:
                    self.switch_img = True
                    Game.pl.environ.turnImgOff()

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
        if( Game.pl.hasWon() ):
            self.prepareNewState( Game.ST_VICTORY )
            return

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
            if random.randint(0,4096) == 42:  # proba faible
                Game.pl.environ.generateBonus()
                x_bonus, y_bonus = Game.pl.environ.current_bonus.getXY()
                if (y_bonus+(DISP_HEIGHT) < Game.pl.y_game ):
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
        cond1 = self.state==Game.ST_PLATEFORMER
        cond2 = self.state==Game.ST_GAME_FALL
        if(cond1  ):
            Game.sk_bar.markToDisplay(Game.window)
            #ajout score reel
            real_score = Game.pl.getScore()
            label = self.font.render( str(real_score)+" meters below the game's surface"  , 1, (0, 255, 0) )
            Game.window.blit( label, ( DISP_WIDTH-532, 16 ) )

        if(cond2):
            #ajout score fake
            if(self.fake_depth<HEIGHT_VICTORY ):
                self.fake_depth+=37
            label = self.font.render( str(self.fake_depth)+" meters below the game's surface"  , 1, (0, 255, 0) )
            Game.window.blit( label, ( DISP_WIDTH-532, 16 ) )
            
        if( cond1 or cond2 ):
            Game.pl.markToDisplay( Game.window ) 

        # TODO cest le joueur qui pourrait declencher le declencehement du dessin du terrain
        pygame.display.flip() 
        #self.last_refr = pygame.time.get_ticks()
          

g = Game()
g.run()
del g
