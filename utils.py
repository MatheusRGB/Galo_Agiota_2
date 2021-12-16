import pygame
import os
from estruturas import *

WIDTH = 1280
HEIGHT = 720


class Text():
    def __init__(self, surface, msg, x, y, fontName, size, cr, cg, cb):
        self.surface = surface
        self.msg = msg
        self.x = x
        self.y = y
        self.size = size
        self.fontName = os.path.join("data/fonts", fontName)
        self.cr = cr
        self.cg = cg
        self.cb = cb
        self.swapMessage(self.msg)

    def update(self):
        self.surface.blit(self.text, self.rect)
    
    def swapMessage(self, msg):
        self.msg = msg
        self.font = pygame.font.Font(self.fontName, self.size)
        self.text = self.font.render(self.msg, True, (self.cr, self.cg, self.cb))
        self.rect = self.text.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Image(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, data):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.data = data
        self.swapImage(self.data)

    def swapImage(self, data):
        self.data = data
        self.image = pygame.image.load(self.data)
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Physics():
    def __init__(self, sprites1, sprites2):
        self.character = sprites1
        self.world = sprites2
        self.collide = False
        self.left = 5
        self.right = 5
        self.fall = True
        self.aux = []
        self.aux.append(self.character.rect.y)
        self.up = not self.fall
        self.height = 180
        self.diff = None
        self.diff_max = None
        self.min_gravity = 3
        self.max_gravity = 11
        self.gravity = self.min_gravity
        self.smooth = 1

    def update(self):
        for i in range(len(self.world)):
            self.collide = pygame.Rect.colliderect(self.character.rect, self.world[i])
            if self.collide:
                break
        self.collision()
        self.maxJumpHeight()
        self.gravityController()
        self.objectFall()

    def collision(self):
        limit = False
        for i in range(len(self.world)):
            up = self.world[i].rect.top - self.character.rect.bottom
            down = self.world[i].rect.bottom - self.character.rect.top
            left = self.world[i].rect.right - self.character.rect.left
            right = self.world[i].rect.left - self.character.rect.right
            width = left - right
            height = down - up
            if down > 0 and down < height-self.max_gravity:
                if width - left == 0:
                    self.right = 0
                    limit = True
                if width - left == width:
                    self.left = 0
                    limit = True
            if down <= 0 and down+self.gravity >= 0:
                if width - left > 0 and width - left < width:
                    self.collide = False
                    self.fall = True
            if not limit:
                self.left = 5
                self.right = 5

    def maxJumpHeight(self):
        if self.collide:
            self.diff = False
            self.fall = False
            self.up = False
        if not self.diff:
            self.diff = self.character.rect.y
            self.diff_max = self.diff-self.height
        else:
            if self.character.rect.y <= self.diff_max:
                self.fall = True
                self.up = False

    def gravityController(self):
        if not self.collide:
            if not self.up and not self.fall:
                self.up = True
                self.gravity = self.max_gravity
            if not self.up:
                self.gravity += self.smooth
                if self.gravity >= self.max_gravity:
                    self.gravity = self.max_gravity
            else:
                self.gravity -= self.smooth
                if self.gravity <= self.min_gravity:
                    self.gravity = self.min_gravity
        else:
            self.fall = False
            self.gravity = self.min_gravity

    def objectFall(self):
        self.aux.append(self.character.rect.y)
        if len(self.aux) > 2:
            self.aux.clear()
        else:
            if len(self.aux) == 2:
                if self.aux[0] < self.aux[1]:
                    self.fall = True
                    self.up = False


class Game():
    def __init__(self, sprites1, sprites2, sprites3, stage):
        self.character = sprites1
        self.spikes = sprites2
        self.flags = sprites3
        self.collideTrap = False
        self.collideFlag = False
        self.dead = 0
        self.level = stage

    def update(self):
        self.isDead()
        self.isFinished()

    def isDead(self):
        for i in range(len(self.spikes)):
            self.collideTrap = pygame.Rect.colliderect(self.character.rect, self.spikes[i])
            if self.collideTrap:
                self.character.rect.x = player_positions[self.level][0][0]
                self.character.rect.y = player_positions[self.level][0][1]
                self.dead = 1
                self.level = 0
                break

    def isFinished(self):
        for i in range(len(self.flags)):
            self.collideFlag = pygame.Rect.colliderect(self.character.rect, self.flags[i])
            if self.collideFlag:
                self.level += 1
                break
