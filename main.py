import pygame as pg
import sys
from game import Game

pg.init()
dark_blue = (44, 44, 127)

screen = pg.display.set_mode((300, 600))
pg.display.set_caption("Tetris")

clock = pg.time.Clock()

game = Game()

GAME_UPDATE = pg.USEREVENT
pg.time.set_timer(GAME_UPDATE, 200)

# start of the game loop (check 3 things)
while True:
    # Event Listener
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                game.move_left()
            if event.key == pg.K_RIGHT:
                game.move_right()
            if event.key == pg.K_DOWN:
                game.move_down()
            if event.key == pg.K_UP:
                game.rotate()
        if event.type == GAME_UPDATE:
            game.move_down()

    # Drawing
    screen.fill(dark_blue)
    game.draw(screen)

    # Updating
    pg.display.update()
    clock.tick(60)
      