from utils import *
from world import *
from animations import *

# Menu Principal


class Menu:
    def __init__(self, surface):
        self.points = 0
        self.highpoints = Text(surface, "Melhor Pontuacao: 0", 0, 0, "center", "", "8bits.ttf", 30, 0, 0, 0)
        self.background = Image(0, 0, WIDTH, HEIGHT, "data/menu/MenuScreen.jpg")
        self.button1 = Image(522, 300, 160*1.25, 298 * 1.25, "data/menu/menu.png")
        self.logo = Image(380, 10, 1920/4, 1080/4, "data/menu/galo_slogan.png")
        self.arvore = Image(1280, 408, 726/3, 798/3, "data/menu/MenuTree.png")
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
        self.highpoints.update()
        self.highpoints.swapMessage("Melhor Pontuacao: "+ str(self.points))
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
    def __init__(self, surface):
        self.background = Image(0, 0, WIDTH, HEIGHT, "data/menu/MenuScreen.jpg")
        self.imagem1 = Image(210, 130, 120, 100, "data/menu/KeyArrow.png")
        self.imagem2 = Image(270, 250, 55, 65, "data/environment/GameFlag.png")
        self.imagem3 = Image(430, 330, 40, 40, "data/traps/Off.png")
        self.text1 = Text(surface, "Use essas teclas para mover o Galo Agiota Jr", 0, 200, "center", "" ,"8bits.ttf", 30, 0, 0, 0)
        self.text2 = Text(surface, "Chegue ate a bandeira para avancar de fase.", 0, 270, "center", "", "8bits.ttf",30, 0, 0, 0)
        self.text3 = Text(surface, "EVITE AS ARMADILHAS!", 0, 340, "center", "", "8bits.ttf", 30, 0, 0, 0)
        self.text4 = Text(surface, "Aperte R para voltar.", 0, 570, "center", "", "8bits.ttf", 30, 0, 0, 0)
        self.text5 = Text(surface, "Para Jogar o modo dificil aperte H no menu principal.", 0, 410, "center", "", "8bits.ttf", 30, 0, 0, 0)
        self.objects = []
        self.objects.append(self.background)
        self.objects.append(self.imagem1)
        self.objects.append(self.imagem2)
        self.objects.append(self.imagem3)

    def update(self):
        self.text1.update()
        self.text2.update()
        self.text3.update()
        self.text4.update()
        self.text5.update()


