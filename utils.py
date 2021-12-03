import pygame

WIDTH = 1280
HEIGHT = 720

class Text():
    def __init__(self, text, x, y, w, h, fontName, size, cr, cg, cb):
        self.text = text or ""
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.size = size
        self.fontName = fontName
        self.folder = "data/fonts/"
        self.cr = cr
        self.cg = cg
        self.cb = cb
        self.font = pygame.font.SysFont(self.folder+self.font, self.size)

class Physics():
    def __init__(self, sprites1, sprites2):
        self.character = sprites1
        self.world = sprites2
        self.collide = False
        self.fall = True
        self.height = 180
        self.diff = None
        self.diff_max = None
        self.min_gravity = 3
        self.standard_gravity = 5
        self.max_gravity = 7
        self.gravity = self.standard_gravity

    def update(self):
        self.collide = pygame.Rect.colliderect(self.character.rect, self.world.rect)
        self.maxJumpHeight()

    def maxJumpHeight(self):
        if not self.diff:
            self.diff = self.character.rect.y
            self.diff_max = self.diff-self.height
        else:
            if self.character.rect.y <= self.diff_max:
                self.fall = True
    # Criar função para acelerar suavemente a gravidade na queda e no pulo