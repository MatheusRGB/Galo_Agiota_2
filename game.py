import pygame
from characters import *
from world import *
from structures import *


class Game():
    def __init__(self, surface):
        self.world = None
        self.player = None
        self.level = 0
        self.hard = False
        self.playing = False
        self.dead = False
        self.gameover = False
        self.collideTrap = False
        self.collideFlag = False
        self.time = None
        self.now = None
        self.points = 0
        self.timer = Text(surface, "0", 0, 0, "center", "", "8bits.ttf", 30, 0, 0, 0)
        self.gamepoints = Text(surface, "0", 0, 0, "", "", "8bits.ttf", 30, 0, 0, 0)
        self.createStage()

    def update(self):
        self.timer.update()
        self.gamepoints.update()
        if self.playing:
            self.time = pygame.time.get_ticks()
            self.playing = False
        self.now = (pygame.time.get_ticks() - self.time)/1000
        self.timer.swapMessage(str(self.now))
        self.gamepoints.swapMessage(str(self.points))
        self.isDead()
        self.isFinished()

    def isDead(self):
        for i in range(len(self.world.traps)):
            self.collideTrap = pygame.Rect.colliderect(self.player.animations.rect, self.world.traps[i])
            if self.collideTrap:
                self.dead = True
                self.level = 0
                self.points = 0
                break

    def isFinished(self):
        for i in range(len(self.world.flags)):
            self.collideFlag = pygame.Rect.colliderect(self.player.animations.rect, self.world.flags[i])
            if self.collideFlag:
                self.nextLevel()
                self.createStage()
                self.playing = True
                self.record()
                break

    def createStage(self):
        self.world = World(self.level, self.hard)
        self.player = Player(self.world.collide, self.level)

    def nextLevel(self):
        self.level += 1
        if self.level > len(PLATAFORMS_OBJECT)-1:
            self.level = 0
            self.gameover = True

    def record(self):
        if 1000 - (int(self.now)*10) >= 0:
            self.points += 1000 - (int(self.now) * 10)
        if self.hard:
            self.points += 500
