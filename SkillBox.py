from GameEntity import GameEntity
import random


class SkillBox(GameEntity):

    POSSIB_SKILLS = {
        1: 'TELEPORT_UP',
        2: 'BIG_JUMP',
        3: 'GHOST_MODE'
    }

    def __init__(self, x_game_init, y_game_init):
        super(SkillBox, self).__init__()
        super(SkillBox, self).setXY(x_game_init, y_game_init)

        taille = len(SkillBox.POSSIB_SKILLS)
        diceroll = random.randint(1, taille)
        self.skill_id = diceroll
        self.skillname = SkillBox.POSSIB_SKILLS[diceroll]
        self.visible = True

    def updatePosition(self):
        # descente progressive des bonus skill
        x_ent, y_ent = self.getXY()
        self.setXY(x_ent, y_ent - 0.4)

    # def markToDisplay(self, surface):
    # x_ent,y_ent = self.getXY()
    # pygame.draw.rect( surface, pygame.Color('BROWN'),
    # pygame.Rect( x_ent,y_ent, 30,30)  )
