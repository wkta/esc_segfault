

class Level(object):
    """classe ABSTRAITE pour decrire un environnement de jeu bateau, sans scrolling"""

    def __init__(self):
        self.entity_list = list()
        self.x_plat_list = list()
        self.y_plat_list = list()
        self.current_bonus = None

    def addEntity(self, ent):
        self.entity_list.append(ent)

    def markToDisplay(self,window):
        """affichage des entites de decor"""
        #affichage des plateformes
        for ent in self.entity_list:
            ent.markToDisplay(window,self.pl_y_game)

    def removeAllPlatform(self):
        self.entity_list = list()
        
    def updateEntities(self ):
        pass

    def populateEntities(self):
        pass

    def scrollTo(self, pl_y_game):
        pass
