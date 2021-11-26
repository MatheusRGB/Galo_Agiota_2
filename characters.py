import pygame

# Personagem principal
class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("data/character/GigaChad.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 100, 100)

    def update(self):
        keys = pygame.key.get_pressed()

        # Controles de movimento
        if keys[pygame.K_w]:
            self.rect.y -= 1

        if keys[pygame.K_a]:
            self.rect.x -= 1

        if keys[pygame.K_s]:
            self.rect.y += 1

        if keys[pygame.K_d]:
            self.rect.x += 1