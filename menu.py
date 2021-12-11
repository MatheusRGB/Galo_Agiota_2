import pygame
from utils import *
from world import *

# Menu Principal


class Menu:
    def __init__(self, sprites):
        self.data = sprites
        self.background = Image(0, 0, WIDTH, HEIGHT,
                                "data/menu/MenuScreen.jpg")

        self.button1 = Image(1080, 300, 160*1.25, 298 *
                             1.25, "data/menu/menu.png")


class HowToPlay:
    def __init__(self, sprites):
        self.data = sprites
        self.background = Image(0, 0, WIDTH, HEIGHT,
                                "data/menu/MenuScreen.jpg")
