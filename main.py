import pygame
from characters import *

# Initiation
pygame.init()
display = pygame.display.set_mode([1280, 720])
pygame.display.set_caption('Galo Agiota 2')

# Fundo de tela
def draw():
    display.fill([48, 65, 92])

# Grupo de Sprites
drawGame = pygame.sprite.Group()
drawGame.player = Player(drawGame)

# Musicas
# Tocar essa apenas em boss
pygame.mixer.music.load("data/soundtrack/BossMusic.mp3")
pygame.mixer.music.play(-1)

# Sons(Player/Ambiente)
LaserShoot = pygame.mixer.Sound("data/soundtrack/LaserGun.wav")

# Game rodando
GameLoop = True
if __name__ == '__main__':
    while GameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Sair do Jogo
                GameLoop = False

            if event.type == pygame.KEYDOWN:  # Executar Som de Tiro
                if event.key == pygame.K_SPACE:
                    LaserShoot.play()
        # Tela
        draw()
        drawGame.draw(display)
        drawGame.player.update()
        pygame.display.update()
