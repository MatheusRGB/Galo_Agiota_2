import pygame
from characters import *
from world import *
from utils import *

# Initiation
pygame.init()
display = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Galo Agiota 2")

drawGame = pygame.sprite.Group()
world = World()
player = Player(world.collide)
drawGame.add(world.background)
drawGame.add(player.animations)
drawGame.add(world.objects)

# Organizando as funçoes
def draw():
    drawGame.draw(display)

def update():
    drawGame.update()
    player.update()
    #world.update()

# Musicas
# Tocar essa apenas em boss
# pygame.mixer.music.load("data/soundtrack/BossMusic.mp3")
# pygame.mixer.music.play(-1)

# Sons(Player/Ambiente)
LaserShoot = pygame.mixer.Sound("data/soundtrack/LaserGun.wav")
fps = pygame.time.Clock()
# Game rodando
GameLoop = True
if __name__ == '__main__':
    while GameLoop:
        fps.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Sair do Jogo
                GameLoop = False

            if event.type == pygame.KEYDOWN:  # Executar Som de Tiro
                if event.key == pygame.K_SPACE:
                    LaserShoot.play()
        # Tela
        draw()
        update()
        pygame.display.update()