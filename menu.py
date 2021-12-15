import pygame
from utils import *
from world import *
from animations import *

# Menu Principal


class Menu:
    def __init__(self, sprites):
        self.data = sprites
        self.background = Image(0, 0, WIDTH, HEIGHT, "data/menu/MenuScreen.jpg")
        self.button1 = Image(522, 300, 160*1.25, 298 * 1.25, "data/menu/menu.png")
        self.logo = Image(380, 10, 1920/4, 1080/4, "data/menu/galo_slogan.png")   
        self.galinhaMenu = Animations(100, 550, 50, 50, "run", 0.15, "data/menu/", "Right", True) 
        self.chao_animado = Animations(0, HEIGHT - 125, WIDTH, 75, "chao", 0.15, "data/menu/", "Right", True) 

class HowToPlay:
    def __init__(self, sprites):
        self.data = sprites
        self.background = Image(0, 0, WIDTH, HEIGHT, "data/menu/MenuScreen.jpg")
        self.imagem1 = Image(250, 150, 130, 110, "data/menu/KeyArrow.png")
