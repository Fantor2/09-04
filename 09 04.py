import pygame as pg
import sys
from sky import Sky
from settings import *
import random
pg.init()
screen= pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pg.time.Clock()
sky = Sky("sky.png",screen , x, y)




while True:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
sky1 = Sky('sky.png',screen,(SCREEN_WIDTH - 200) // 2,0)
sky2 = Sky('sky.png',screen,(SCREEN_WIDTH - 200) // 2, - SCREEN_HEIGHT)

sky.update()
screen_fill((0,0,0))
pg.display.update()
