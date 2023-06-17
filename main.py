import pygame as pg
import sys
from grid import Grid

pg.init()
dark_blue = (44, 44, 127)

screen = pg.display.set_mode((300, 600))
pg.display.set_caption("Python Tetris")

clock = pg.time.Clock()

game_grid = Grid()

game_grid.grid[0][0] = 1
game_grid.grid[3][5] = 4
game_grid.grid[17][8] = 7

game_grid.print_grid()

# start of the game loop (check 3 things)
while True:
    # event listener 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # Drawing
    screen.fill(dark_blue)
    game_grid.draw(screen)

    pg.display.update()
    clock.tick(60)
      