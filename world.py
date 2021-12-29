from utils import *
from animations import *
from structures import *


class World():
    def __init__(self, stage, hard):
        self.stage = stage
        self.hard = hard
        self.background = Image(0, 0, WIDTH, HEIGHT, "data/environment/bg.png")
        self.ground = Image(0, HEIGHT - 125, WIDTH, 75, "data/environment/ground.png")
        self.water = Image(0, HEIGHT - 50, WIDTH, 50, "data/environment/water/water.png")
        self.object = None
        self.collide = []
        self.objects = []
        self.traps = []
        self.flags = []
        self.objects.append(self.water)
        self.generateWorld()
        self.createAnimatedWater()

    def createAnimatedWater(self):
        amount = 10
        scale = 3
        posX = 230
        posY = -35
        for i in range(amount):
            self.object = Animations(posX, posY + (i * (24 * scale)), 16 * scale,24 * scale, "fall", 0.15, "data/environment/water/", "Left", True)
            self.objects.append(self.object)
        self.object = Animations(posX, posY + (amount * (24 * scale) - 24), 16 * scale, 8 * scale, "fall-bottom", 0.15, "data/environment/water/", "Left", True)
        self.objects.append(self.object)

    def generateWorld(self):
        self.createObjectsWorld(PLATAFORMS_OBJECT, "plataforms")
        self.createObjectsWorld(SPIKES_OBJECT, "traps")
        if self.hard:
            self.createObjectsWorld(SPIKES_OBJECT_HARD, "traps")
        self.createObjectsWorld(FLAGS_OBJECT, "flags")

    def createObjectsWorld(self, data, type):
        for i in range(len(data[self.stage])):
            for x in range(data[self.stage][i][4]):
                if data[self.stage][i][5] == "horizontal":
                    self.object = Image(data[self.stage][i][0] + (x * data[self.stage][i][2]), data[self.stage][i][1], data[self.stage][i][2], data[self.stage][i][3], data[self.stage][i][6])
                elif data[self.stage][i][5] == "vertical":
                    self.object = Image(data[self.stage][i][0], data[self.stage][i][1] + (x * data[self.stage][i][3]), data[self.stage][i][2], data[self.stage][i][3], data[self.stage][i][6])
                self.objects.append(self.object)
                if type == "plataforms":
                    self.collide.append(self.object)
                elif type == "traps":
                    self.traps.append(self.object)
                elif type == "flags":
                    self.flags.append(self.object)