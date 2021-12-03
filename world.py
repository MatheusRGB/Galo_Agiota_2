import pygame
from utils import *

class World():
    def __init__(self, sprites):
        self.data = sprites
        self.background = Image(0, 0, WIDTH, HEIGHT, "data/environment/bg.png")
        self.ground = Image(0, HEIGHT-45, WIDTH, 45, "data/environment/ground.png")
        
    # def update():
    #     print("teste")

class Image(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, data):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.data = data
        self.image = pygame.image.load(self.data)
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        