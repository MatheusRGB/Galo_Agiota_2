import pygame
from utils import *
from animations import *
from estruturas import *


class World():
    def __init__(self):
        self.stage = 0
        self.background = Image(0, 0, WIDTH, HEIGHT, "data/environment/bg.png")
        self.ground = Image(0, HEIGHT - 125, WIDTH - 200, 75, "data/environment/ground.png")
        self.water = Image(0, HEIGHT - 50, WIDTH, 50, "data/environment/water/water.png")
        self.plataforms = None
        self.spikes = None
        self.waterfall = None
        self.collide = []
        self.objects = []
        self.objects.append(self.water)
        self.plataform()
        self.spike()
        self.createAnimatedWater()

    def createAnimatedWater(self):
        amount = 10
        scale = 3
        posX = 230
        posY = -35
        for i in range(amount):
            self.waterfall = Animations(posX, posY + (i * (24 * scale)), 16 * scale,24 * scale, "fall", 0.15, "data/environment/water/", "Left", True)
            self.objects.append(self.waterfall)
        self.waterfall = Animations(posX, posY + (amount * (24 * scale) - 24), 16 * scale, 8 * scale, "fall-bottom", 0.15, "data/environment/water/", "Left", True)
        self.objects.append(self.waterfall)

    def plataform(self):
        image = "data/environment/plataform.png"
        if self.stage != 0:
            image = "data/environment/stone.png"
        for i in range(len(plataforms_objeto[self.stage])):
            for x in range(plataforms_objeto[self.stage][i][2]):
                if plataforms_objeto[self.stage][i][3] == 0:
                    self.plataforms = Image( plataforms_objeto[self.stage][i][0] + (x * 50), plataforms_objeto[self.stage][i][1], 50, 50, image)
                    self.objects.append(self.plataforms)
                    self.collide.append(self.plataforms)
                else:
                    self.plataforms = Image(plataforms_objeto[self.stage][i][0], plataforms_objeto[self.stage][i][1] + (x * 50), 50, 50, image)
                    self.objects.append(self.plataforms)
                    self.collide.append(self.plataforms)

    def spike(self):
        for i in range(len(spikes_objeto[self.stage])):
            for x in range(spikes_objeto[self.stage][i][2]):
                if spikes_objeto[self.stage][i][3] == 0:
                    self.spikes = Image(
                        spikes_objeto[self.stage][i][0] + (x * 50), spikes_objeto[self.stage][i][1], 50, 50, "data/traps/Off.png")
                    self.objects.append(self.spikes)

                else:
                    self.spikes = Image(
                        spikes_objeto[self.stage][i][0], spikes_objeto[self.stage][i][1] + (x * 50), 50, 50, "data/traps/Off.png")
                    self.objects.append(self.spikes)
