import pygame as pg
import sys
from game import Game

pg.init()
dark_blue = (44, 44, 127)

screen = pg.display.set_mode((300, 600))
pg.display.set_caption("Python Tetris")

clock = pg.time.Clock()

game = Game()

# start of the game loop (check 3 things)
while True:
    # event listener 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # Drawing
    screen.fill(dark_blue)
    game.draw(screen)
    
    pg.display.update()
    clock.tick(60)
      