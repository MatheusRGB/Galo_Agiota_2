import pygame
from utils import *

class World():
    def __init__(self, sprites):
        self.data = sprites
        self.background = Image(0, 0, WIDTH, HEIGHT, "data/environment/bg.png")
        self.ground = Image(0, HEIGHT-45, WIDTH, 45, "data/environment/ground.png")
        
    def update(self):
        self.data = None
        #print(self.background.image)
        #self.background.swapImage("data/environment/ground.png")
