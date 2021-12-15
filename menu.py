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
        self.arvore = Image(1280, 418, 726/4, 798/4, "data/menu/MenuTree.png")
        self.water = Image(0, HEIGHT - 50, WIDTH, 50, "data/environment/water/water.png")
        self.nuvem = Image(1200, 100, 726/5, 798/5, "data/menu/nuvem.png")
        self.nuvem2 = Image(1200, 250, 726/5, 798/5, "data/menu/nuvem.png")
        self.galinhaMenu = Animations(100, 550, 50, 50, "run", 0.15, "data/menu/", "Right", True) 
        self.chao_animado = Animations(0, HEIGHT - 125, WIDTH, 75, "chao", 0.15, "data/menu/", "Right", True)

        self.objects = [] 
        self.objects.append(self.background)
        self.objects.append(self.nuvem)
        self.objects.append(self.nuvem2)
        self.objects.append(self.galinhaMenu)
        self.objects.append(self.arvore)
        self.objects.append(self.chao_animado)
        self.objects.append(self.water)
        self.objects.append(self.logo)
        self.objects.append(self.button1)

    def update(self):
        self.arvore.rect.x -= 2
        self.nuvem.rect.x -= 4
        self.nuvem2.rect.x -= 5

        if self.arvore.rect.x < -175:
            self.arvore.rect.x = 1280
        
        if self.nuvem.rect.x < -125:
            self.nuvem.rect.x = 1280

        if self.nuvem2.rect.x < -125:
            self.nuvem2.rect.x = 1280  

class HowToPlay:
    def __init__(self, sprites):
        self.data = sprites
        self.background = Image(0, 0, WIDTH, HEIGHT, "data/menu/MenuScreen.jpg")
        self.imagem1 = Image(250, 150, 130, 110, "data/menu/KeyArrow.png")


    