import pygame
from utils import *
from animations import *
from structures import *

# Personagem principal
class Player():
    def __init__(self, sprites, level):
        self.animations = Animations(PLAYER_POSITIONS[level][0][0],  PLAYER_POSITIONS[level][0][1], 50, 50, "idle", 0.15, "data/character/", "Right", False) # Seta as animações
        self.physics = Physics(self.animations, sprites) # Coloca física no objeto
        self.idle = True
        self.jump = False
        self.run = False
        self.keys = None
    # Função de atualização do personagem e de sua física
    def update(self):
        self.physics.update()
        self.keys = pygame.key.get_pressed()

        # Controles de movimento
        if self.keys[pygame.K_w]:
            if not self.physics.fall:
                self.animations.rect.y -= self.physics.gravity*2 # Muda a posição do objeto
                self.controller("jump") # Muda o controlador para alterar a animação

        if self.keys[pygame.K_a]:
            self.animations.rect.x -= self.physics.left # Muda a posição do objeto
            self.animations.orientation = "Left" # Muda a direção que o objeto ta virado
            self.controller("run") # Muda o controlador para alterar a animação

        if self.keys[pygame.K_d]:
            self.animations.rect.x += self.physics.right # Muda a posição do objeto
            self.animations.orientation = "Right" # Muda a direção que o objeto ta virado
            self.controller("run") # Muda o controlador para alterar a animação

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
