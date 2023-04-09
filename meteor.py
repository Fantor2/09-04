from settings import *
import pygame as pg


class Meteor(pygame.sprite.Sprite):

    def __init__(self,scrren,x,y):
        self.screen=screen
        pygame.sprite.Sprite.__init(self)
        self.image = pygame.image.load(METEOR_FILE_NAME).covert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy = 2
        
    def update(self):
        self.rect.y +=self.speedy
        def draw (self):
            self.screen_blit(self.image.self.rect)
