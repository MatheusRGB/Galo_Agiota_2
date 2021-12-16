import pygame
from utils import *
from animations import *

# Personagem principal
class Player():
    def __init__(self, sprites, CacheLevel):
        self.animations = Animations(player_positions[CacheLevel][0][0],  player_positions[CacheLevel][0][1], 50, 50, "idle", 0.15, "data/character/", "Right", False)
        self.physics = Physics(self.animations, sprites)
        self.idle = True
        self.jump = False
        self.run = False
        self.keys = None

    def update(self):
        self.physics.update()
        self.keys = pygame.key.get_pressed()

        # Controles de movimento
        if self.keys[pygame.K_w]:
            if not self.physics.fall:
                self.animations.rect.y -= self.physics.gravity*2
                self.controller("jump")

        if self.keys[pygame.K_a]:
            self.animations.rect.x -= self.physics.left
            self.animations.orientation = "Left"
            self.controller("run")

        if self.keys[pygame.K_d]:
            self.animations.rect.x += self.physics.right
            self.animations.orientation = "Right"
            self.controller("run")

        # Aciona o update nas animações quando executar alguma ação e evita loops de animações enquanto no ar
        if self.jump:
            if self.animations.current < self.animations.size-1:
                self.animations.animation(self.jump)
            else:
                self.animations.current = self.animations.size-1
                self.animations.animation(False)
        elif self.run:
            self.animations.animation(self.run)
        elif self.idle:
            self.animations.animation(self.idle)

        # Verifica se existe colisão e atualiza a animação entre idle e jump
        if not self.physics.collide:
            self.animations.rect.y += self.physics.gravity
            self.controller("jump")
        else:
            if self.jump and not self.idle:
                self.controller("idle")
            if self.run and not self.idle:
                self.controller("idle")

    # Controladora das animações
    def controller(self, str):
        if not self.jump:
            if str == "jump":
                self.idle = False
                self.jump = True
                self.run = False
                self.animations.swapAnimation(str)
            if self.idle:
                if str == "run" and not self.run:
                    self.idle = False
                    self.jump = False
                    self.run = True
                    self.animations.swapAnimation(str)
            else:
                if str == "idle" and self.run and not self.keys[pygame.K_a] and not self.keys[pygame.K_d]:
                    self.idle = True
                    self.jump = False
                    self.run = False
                    self.animations.swapAnimation(str)
        else:
            if not self.idle and str == "idle":
                self.idle = True
                self.jump = False
                self.run = False
                self.animations.swapAnimation(str)
