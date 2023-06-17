import pygame
import sys

pygame.init()

screen = pygame.display.set_mod((300, 600))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

# start of the game loop (check 3 things)
while True:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# 