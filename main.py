import pygame as pg
import sys
from game import Game
from colors import Colors

pg.init()

title_font = pg.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

score_rect = pg.Rect(320, 55, 170, 60)
next_rect = pg.Rect(320, 215, 170, 180)

screen = pg.display.set_mode((500, 620))
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
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pg.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pg.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pg.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pg.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    # Drawing
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pg.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx,
        centery = score_rect.centery))
    pg.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)

    # Updating
    pg.display.update()
    clock.tick(60)
      