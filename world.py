from utils import *
from animations import *
from structures import *

# Inicia a classe do mundo, com suas caracteristicas iniciais (Background, chão ....)
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
    # Função para iniciar a cachoeira animada
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
    # Função para popular a telas, alocar traps , plataformas...
    def generateWorld(self):
        self.createObjectsWorld(PLATAFORMS_OBJECT[self.stage], "plataforms")
        self.createObjectsWorld(SPIKES_OBJECT[self.stage], "traps")
        if self.hard:
            self.createObjectsWorld(SPIKES_OBJECT_HARD[self.stage], "traps")
        self.createObjectsWorld(FLAGS_OBJECT[self.stage], "flags")
    # Função usada para populas a tela, alocar os objetos nos respectivos x e y
    def createObjectsWorld(self, data, type):
        for i in range(len(data)):
            for j in range(data[i][4]):
                x , y , w , h , orientation, image = data[i][0], data[i][1], data[i][2], data[i][3], data[i][5], data[i][6]
                if orientation == "horizontal":
                    self.object = Image(x + (j * w), y, w, h, image)
                elif orientation == "vertical":
                    self.object = Image(x, y + (j * h), w, h, image)
                self.objects.append(self.object)
                if type == "plataforms":
                    self.collide.append(self.object)
                elif type == "traps":
                    self.traps.append(self.object)
                elif type == "flags":
                    self.flags.append(self.object)