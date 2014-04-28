
FPS = 33
DISP_WIDTH = 1024
DISP_HEIGHT = 600
SIZE_SK_BAR = 64
DEBUG_RECTS= False
HEIGHT_VICTORY = 600 * 27  # if you reach this, you win

def game_to_scr_coord(x_game, y_game, pl_y_game):
    return (
        int(x_game ),
        int(pl_y_game+(DISP_HEIGHT/2) -y_game )
        )
