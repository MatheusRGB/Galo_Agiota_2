import pygame
from characters import *
from world import *

class Game():
    def __init__(self):
        self.level = 0
        self.world = World(self.level)
        self.player = Player(self.world.collide, self.level)
        self.collideTrap = False
        self.collideFlag = False
        self.dead = False
        self.gameover = False

    def update(self):
        self.isDead()
        self.isFinished()

    def isDead(self):
        for i in range(len(self.world.traps)):
            self.collideTrap = pygame.Rect.colliderect(self.player.animations.rect, self.world.traps[i])
            if self.collideTrap:
                self.player.animations.rect.x = player_positions[self.level][0][0]
                self.player.animations.rect.y = player_positions[self.level][0][1]
                self.dead = True
                self.level = 0
                self.createStage()
                break

    def isFinished(self):
        for i in range(len(self.world.flags)):
            self.collideFlag = pygame.Rect.colliderect(self.player.animations.rect, self.world.flags[i])
            if self.collideFlag:
                self.nextLevel()
                self.createStage()
                break

    def createStage(self):
        self.world = World(self.level)
        self.player = Player(self.world.collide, self.level)

    def nextLevel(self):
        self.level += 1
        if self.level > 3:
            self.level = 0
            self.gameover = True

