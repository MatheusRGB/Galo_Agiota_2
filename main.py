import pygame

# Initiation
pygame.init()
display = pygame.display.set_mode([1280, 720])
pygame.display.set_caption('Galo Agiota 2')

# Imagem de fundo
Backgound = pygame.image.load("data/environment/bg.png")
Backgound = pygame.transform.scale(Backgound, [1280, 720])


# Chao
class Ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("data/environment/ground.png")
        self.image = pygame.transform.scale(self.image, (1300, 45))
        self.rect = self.image.get_rect()
        self.rect[1] = 720 - 45


Solo = pygame.sprite.Group()
ground = Ground()
Solo.add(ground)


# Personagem
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("data/character/galo.png")
        self.rect = pygame.Rect(100, 100, 100, 100)

    def update(self):
        keys = pygame.key.get_pressed()

        # Controles de movimento
        if keys[pygame.K_w]:
            self.rect.y -= 15

        if keys[pygame.K_a]:
            self.rect.x -= 3
            print("teste")

        if keys[pygame.K_d]:
            self.rect.x += 3
            print("teste2")

        if keys[pygame.K_s]:
            self.rect.y += 1

        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect[1] += Gravity


# Musicas
# Tocar essa apenas em boss
# pygame.mixer.music.load("data/soundtrack/BossMusic.mp3")
# pygame.mixer.music.play(-1)

# Sons(Player/Ambiente)
LaserShoot = pygame.mixer.Sound("data/soundtrack/LaserGun.wav")

# FPS do Jogo
fps = pygame.time.Clock()


# Grupo de Sprites
drawPlayer = pygame.sprite.Group()
player = Player()
drawPlayer.add(player)


# Organizando as funçoes
def draw():
    drawPlayer.draw(display)
    Solo.draw(display)


def update():
    Solo.update()
    drawPlayer.update()


# Game rodando
GameLoop = True
if __name__ == '__main__':
    while GameLoop:
        fps.tick(60)
        display.blit(Backgound, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Sair do Jogo
                GameLoop = False

            if event.type == pygame.KEYDOWN:  # Executar Som de Tiro
                if event.key == pygame.K_SPACE:
                    LaserShoot.play()

        if pygame.sprite.groupcollide(drawPlayer, Solo, False, False):
            Gravity = 0
            print("Colisi")
        else:
            Gravity = 7

        # Tela
        draw()

        update()

        pygame.display.update()
