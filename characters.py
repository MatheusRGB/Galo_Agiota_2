import pygame
import os

# Personagem principal
class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.sprites = []
        self.idle = True
        self.jump = False
        self.run = False
        self.folder = "data/character/"
        self.swapAnimation("idle")

        # self.idle = [True, False, False] # Estado/Inicio/Fim
        # self.jump = [False, False, False]
        # self.run = [False, False, False]
        # self.fileName = []
        # for dir, _, files in os.walk("data/character/"):
        #     for file in files:
        #         self.fileName.append(file)
        #         self.sprites.append(pygame.image.load(os.path.join(dir,file)))
        #         if file[0] == "i":
        #             if not self.idle[1]:
        #                 self.idle[1] = len(self.sprites)
        #             self.idle[2] = len(self.sprites)
        #         elif file[0] == "j":
        #             if not self.jump[1]:
        #                 self.jump[1] = len(self.sprites)
        #             self.jump[2] = len(self.sprites)
        #         elif file[0] == "r":
        #             if not self.run[1]:
        #                 self.run[1] = len(self.sprites)
        #             self.run[2] = len(self.sprites)

        self.current = 0
        self.image = self.sprites[self.current]
        self.rect = pygame.Rect(800, 400, 100, 100)

    def update(self):
        keys = pygame.key.get_pressed()

        # Controles de movimento
        if keys[pygame.K_w]:
            self.rect.y -= 1
            self.animation("jump")

        if keys[pygame.K_a]:
            self.rect.x -= 1
            self.animation("run")

        if keys[pygame.K_d]:
            self.rect.x += 1
            self.animation("run")
        
        if keys[pygame.K_s]:
            self.rect.y += 1
            self.animation("idle")

    def animation(self, str):
        if not self.jump:
            if str == "jump":
                self.idle = False
                self.jump = True
                self.swapAnimation(str)
        if self.idle:
            if str == "run" and not self.run:
                self.idle = False
                self.run = True
                self.swapAnimation(str)
            if str == "idle":
                self.jump = False
                self.run = False
                self.idle = True
                self.swapAnimation(str)
        else:
            self.current += 0.15
            
        if self.current >= len(self.sprites):
            self.idle = True
            self.jump = False
            self.run = False
            self.current = 0
        
        # if str == "jump":
        #     self.idle[0] = False
        #     self.jump[0] = True
        #     self.current = self.jump[1]
        # if self.idle[0]:
        #     if str == "run":
        #         self.idle[0] = False
        #         self.run[0] = True
        #         self.current = self.run[1]
        # if self.run[0]:
        #     if self.current >= self.run[2]:
        #         self.run[0] = False
        #         self.current = self.run[1]
        #         self.idle[0] = True
        # if self.jump[0]:
        #     if self.current >= self.jump[2]:
        #         self.jump[0] = False
        #         self.current = self.jump[1]
        #         self.idle[0] = True
        
        self.image = self.sprites[int(self.current)]

    def swapAnimation(self, str):
        self.current = 0
        self.sprites = []
        for dir,_,files in os.walk(self.folder):
            for file in files:
                if dir == self.folder+str:
                    self.sprites.append(pygame.image.load(os.path.join(dir,file)))
        self.image = self.sprites[self.current]