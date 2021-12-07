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
        self.fall = True
        self.up = not self.fall
        self.height = 180
        self.diff = None
        self.diff_max = None
        self.min_gravity = 3
        self.max_gravity = 11
        self.gravity = self.min_gravity
        self.smooth = 0.4

    def update(self):
        self.collide = pygame.Rect.colliderect(self.character.rect, self.world.rect)
        self.maxJumpHeight()
        self.gravityController()

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
            # self.smooth += 0.007
            # if self.smooth >= 1:
            # self.smooth = 1
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
            #self.smooth = 0
            self.gravity = self.min_gravity



        

