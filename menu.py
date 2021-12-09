import pygame
from utils import *
from world import *

# Menu Principal
class Menu:
    def __init__(self, sprites):
            self.data = sprites
            self.background = Image(0, 0, WIDTH, HEIGHT, "data/menu/MenuScreen.jpg")

            self.button1 = Image(1100, 300, 125, 70, "data/menu/PlayButton.png")
            self.button2 = Image(1100, 400, 125, 70, "data/menu/HowToPlayerButton.png")
            self.button3 = Image(1100, 500, 125, 70, "data/menu/QuitButton.png")



class HowToPlay:
    def __init__(self, sprites):
            self.data = sprites
            self.background = Image(0, 0, WIDTH, HEIGHT, "data/menu/MenuScreen.jpg")
