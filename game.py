import pygame
from characters import *
from world import *


class Game():
    def __init__(self, surface):
        self.level = 0
        self.world = None #World(self.level)
        self.player = None #Player(self.world.collide, self.level)
        self.collideTrap = False
        self.collideFlag = False
        self.dead = False
        self.gameover = False
        self.time = False
        self.now = False
        self.playing = False
        self.createStage()
        self.timer = Text(surface, "0", 0, 0, "center", "", "8bits.ttf", 30, 0, 0, 0)
        self.points = 0
        self.gamepoints = Text(surface, str(self.points), 0, 0, "", "", "8bits.ttf", 30, 0, 0, 0)


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
                self.createStage()
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
        self.world = World(self.level)
        self.player = Player(self.world.collide, self.level)

    def nextLevel(self):
        self.level += 1
        if self.level > 3:
            self.level = 0
            self.gameover = True

    def record(self):
        if 1000 - (int(self.now)*10) >= 0:
            self.points += 1000 - (int(self.now) * 10)
