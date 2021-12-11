import pygame
from characters import *
from world import *
from utils import *
from menu import *
#TESTE DE NOVA PASTA

# Initiation
pygame.init()
display = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Galo Agiota 2")

# Grupo de Sprites
drawGame = pygame.sprite.Group()  # Game
drawMenu = pygame.sprite.Group()  # Menu

world = World()
player = Player(world.collide)
drawGame.add(world.background)
drawGame.add(player.animations)
drawGame.add(world.objects)


# Menu do Jogo
menu = Menu(None)


drawMenu.add(menu.background)
drawMenu.add(menu.button1)

# Cenario do Menu
drawMenu.add(world.water)
drawMenu.add(world.ground)


# Musicas
# Tocar essa apenas em boss
# pygame.mixer.music.load("data/soundtrack/BossMusic.mp3")
# pygame.mixer.music.play(-1)

# Sons(Player/Ambiente)
LaserShoot = pygame.mixer.Sound("data/soundtrack/LaserGun.wav")

fps = pygame.time.Clock()


MenuState = 1

# Organizando as funçoes


def draw():
    if MenuState == 0:
        drawGame.draw(display)
    if MenuState == 1:
        drawMenu.draw(display)


def update():
    if MenuState == 0:
        drawGame.update()
        player.update()
    # world.update()


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

                if event.key == pygame.K_p:  # Tecla para começar o jogo
                    MenuState = 0

        # Tela

        draw()
        update()
        pygame.display.update()
