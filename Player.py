class Player:
    BASECOLOR = pygame.Color('darkred')
    SIZE = 16

    def __init__(self, x, y ):
        # TODO: ajouter vitesse , fonctions de saut et de déplacement
        self.x, self.y = x,y
        self.environ = DynamicLevel()
        self.img = 

    def test(self):
        print "yoyo"

    def markToDisplay(self, surface):
        pygame.draw.circle( surface, self.color, (int(self.x),int(self.y)), Player.SIZE) 
