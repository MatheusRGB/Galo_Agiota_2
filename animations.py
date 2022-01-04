import pygame
import os

# Classe das animações
class Animations(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, action, speed, folder, orientation, loop):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.sprites = []
        self.size = 0
        self.action = action
        self.speed = speed
        self.folder = folder
        self.orientation = orientation
        self.bool = True
        self.loop = loop
        self.inverted = self.bool
        self.image = False
        self.current = 0
        self.swapAnimation(self.action)
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def animation(self, loop):
        if loop:
            self.current += self.speed
            if self.current > self.size:
                self.current = 0
        self.image = self.sprites[int(self.current)]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.flipAnimation()

    # Função para atualizar as animações
    def update(self):
        if self.loop:
            self.animation(self.loop)

    # Função para iniciar o loop das animações
    def swapAnimation(self, str):
        self.action = str
        self.sprites = []
        for dir, _, files in os.walk(self.folder):
            for file in files:
                if dir == self.folder + self.action:
                    self.sprites.append(
                        pygame.image.load(os.path.join(dir, file)))
        self.current = 0
        self.size = len(self.sprites)
        self.image = self.sprites[self.current]
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.flipAnimation()

    # Função para rotacionar a direção da imagem
    def flipAnimation(self):
        if self.orientation == "Right":
            self.inverted = self.bool
        elif self.orientation == "Left":
            self.inverted = not self.bool
        self.image = pygame.transform.flip(self.image, self.inverted, False)
