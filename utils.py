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
        self.left = 5
        self.right = 5
        self.fall = True
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
            self.collide = pygame.Rect.colliderect(
                self.character.rect, self.world[i])
            if self.collide:
                break
        self.collision()
        self.maxJumpHeight()
        self.gravityController()

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
# import pygame

# WIDTH = 1280
# HEIGHT = 720

# class Text():
#     def __init__(self, text, x, y, w, h, fontName, size, cr, cg, cb):
#         self.text = text or ""
#         self.x = x
#         self.y = y
#         self.w = w
#         self.h = h
#         self.size = size
#         self.fontName = fontName
#         self.folder = "data/fonts/"
#         self.cr = cr
#         self.cg = cg
#         self.cb = cb
#         self.font = pygame.font.SysFont(self.folder+self.font, self.size)

# class Image(pygame.sprite.Sprite):
#     def __init__(self, x, y, w, h, data):
#         pygame.sprite.Sprite.__init__(self)
#         self.x = x
#         self.y = y
#         self.w = w
#         self.h = h
#         self.data = data
#         self.swapImage(self.data)

#     def swapImage(self, data):
#         self.data = data
#         self.image = pygame.image.load(self.data)
#         self.image = pygame.transform.scale(self.image, (self.w, self.h))
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y

# class Physics():
#     def __init__(self, sprites1, sprites2):
#         self.character = sprites1
#         self.world = sprites2
#         self.collide = False
#         self.bool = False
#         self.left = 5
#         self.right = 5
#         self.fall = True
#         self.up = not self.fall
#         self.height = 180
#         self.diff = None
#         self.diff_max = None
#         self.min_gravity = 3
#         self.max_gravity = 11
#         self.gravity = self.min_gravity
#         self.smooth = 0.4

#     def update(self):
#         self.collision()
#         self.maxJumpHeight()
#         self.gravityController()

#     def collision(self):
#         for j in range(len(self.world)):
#             self.collide = pygame.Rect.colliderect(self.character.rect, self.world[j])
#             up = self.world[j].rect.top - self.character.rect.bottom
#             down = self.world[j].rect.bottom - self.character.rect.top
#             left = self.world[j].rect.right - self.character.rect.left
#             right = self.world[j].rect.left - self.character.rect.right
#             widht = left - right
#             height = down - up
#             # if self.collide and not self.bool and up < 0:
#             #     self.bool = True
#             #     if self.world[j].rect.y-self.character.rect.y < self.world[j].rect.h:
#             #         teste = (self.world[j].rect.y-self.character.rect.y) - self.world[j].rect.h
#             #         self.character.rect.y += teste
#             #         print(teste)
#             #     up = self.world[j].rect.top - self.character.rect.bottom

#             if down > 0 :
#                 if left == 0 and up < 0:
#                     self.left = 0
#                 else:
#                     self.left = 5
#                 if right == 0 and up < 0:
#                     self.right = 0
#                 else:
#                     self.right = 5
#             if (widht - left > 0 and widht - left < widht) and (down > 0 and down < height - down):
#                 self.collide = False
#                 self.fall = True
#             if self.right == 0 or self.left == 0:
#                 break
#             if self.collide:
#                 break
#         self.bool = False

#     def maxJumpHeight(self):
#         if self.collide:
#             self.diff = False
#             self.fall = False
#             self.up = False
#         if not self.diff:
#             self.diff = self.character.rect.y
#             self.diff_max = self.diff-self.height
#         else:
#             if self.character.rect.y <= self.diff_max:
#                 self.fall = True
#                 self.up = False

#     def gravityController(self):
#         if not self.collide:
#             if not self.up and not self.fall:
#                 self.up = True
#                 self.gravity = self.max_gravity
#             # self.smooth += 0.007
#             # if self.smooth >= 1:
#             # self.smooth = 1
#             if not self.up:
#                 self.gravity += self.smooth
#                 if self.gravity >= self.max_gravity:
#                     self.gravity = self.max_gravity
#             else:
#                 self.gravity -= self.smooth
#                 if self.gravity <= self.min_gravity:
#                     self.gravity = self.min_gravity
#         else:
#             self.fall = False
#             #self.smooth = 0
#             self.gravity = self.min_gravity
