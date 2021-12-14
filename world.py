import pygame
from utils import *
from animations import *
from estruturas import *


class World():
    def __init__(self):
        self.background = Image(0, 0, WIDTH, HEIGHT, "data/environment/bg.png")
        self.ground = Image(0, HEIGHT-125, WIDTH-200, 75,
                            "data/environment/ground.png")
        self.plataforms = Image(250, HEIGHT, 50, 50,
                                "data/environment/plataform.png")
        self.water = Image(0, HEIGHT-50, WIDTH, 50,
                           "data/environment/water/water.png")
        self.waterfall = None
        self.collide = []
        self.objects = []
        self.collide.append(self.ground)
        self.collide.append(self.plataforms)
        self.objects.append(self.ground)
        self.objects.append(self.water)
        self.objects.append(self.plataforms)
        self.createAnimatedWater()
        self.plataform()

    def createAnimatedWater(self):
        amount = 10
        scale = 3
        posX = 200
        posY = -35
        for i in range(amount):
            self.waterfall = Animations(posX, posY+(i*(24*scale)), 16*scale,
                                        24*scale, "fall", 0.15, "data/environment/water/", "Left", True)
            self.objects.append(self.waterfall)
        self.waterfall = Animations(posX, posY+(amount*(24*scale)-24), 16*scale,
                                    8*scale, "fall-bottom", 0.15, "data/environment/water/", "Left", True)
        self.objects.append(self.waterfall)

    def plataform(self):
        for i in range(len(plataforms_objeto)):
            for x in range(plataforms_objeto[i][2]):

                if plataforms_objeto[i][3] == 0:
                    self.plataforms = Image(
                        plataforms_objeto[i][0] + (x * 48), plataforms_objeto[i][1], 50, 50, "data/environment/plataform.png")
                    self.objects.append(self.plataforms)
                    self.collide.append(self.plataforms)
                else:
                    self.plataforms = Image(
                        plataforms_objeto[i][0], plataforms_objeto[i][1] + (x * 48), 50, 50, "data/environment/plataform.png")
                    self.objects.append(self.plataforms)
                    self.collide.append(self.plataforms)
