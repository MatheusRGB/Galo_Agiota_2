import pygame

import characters
from characters import *
from world import *
from utils import *
from menu import *

# Initiation
pygame.init()
display = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Galo Agiota 2")

# Grupo de Sprites
drawGame = pygame.sprite.Group()  # Game
drawMenu = pygame.sprite.Group()  # Menu
drawHowToPlay = pygame.sprite.Group()  # Como jogar

# Cenario de Jogo
world = World()
player = Player(world.collide)
drawGame.add(world.background)
drawGame.add(player.animations)
drawGame.add(world.objects)

# Menu do Jogo
menu = Menu(None)

drawMenu.add(menu.background)
drawMenu.add(menu.logo)
drawMenu.add(menu.galinhaMenu)
drawMenu.add(menu.chao_animado)

# Cenario do Menu
drawMenu.add(world.water)
drawMenu.add(menu.button1)

# Menu Como Jogar
ComoJogar = HowToPlay(None)
drawHowToPlay.add(ComoJogar.background)
drawHowToPlay.add(ComoJogar.imagem1)
drawHowToPlay.add(world.ground)
drawHowToPlay.add(world.water)

# Sons(Player/Ambiente)

fps = pygame.time.Clock()

# GameOver
traps = Traps(player.animations, world.traps)

MenuState = 1

# Musicas
pygame.mixer.music.load("data/soundtrack/MenuSong.mp3")
pygame.mixer.music.play(-1)

MenuMusic = pygame.mixer.Sound("data/soundtrack/MenuSong.mp3")
GameMusic = pygame.mixer.Sound("data/soundtrack/GameSong.mp3")


# Organizando as funçoes
def draw():
    if MenuState == 0:
        drawGame.draw(display)
    if MenuState == 1:
        drawMenu.draw(display)
    if MenuState == 2:
        drawHowToPlay.draw(display)


def update():
    if MenuState == 0:
        drawGame.update()
        player.update()
        traps.update()

    elif MenuState == 1:
        drawMenu.update()


# Game rodando
GameLoop = True
if __name__ == '__main__':
    while GameLoop:
        fps.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Sair do Jogo
                GameLoop = False

            if event.type == pygame.KEYDOWN:  # Executar Som de Tiro
                if MenuState == 1 and event.key == pygame.K_p:  # Tecla para começar o jogo
                    MenuState = 0
                    pygame.mixer.music.stop()
                    GameMusic.play()

                if event.key == pygame.K_c:  # Tecla para Menu Como Jogar
                    MenuState = 2

                if MenuState == 2 and event.key == pygame.K_r:  # Pressione R para voltar para o Menu
                    MenuState = 1

                if traps.stage == 1:  # GameOver, Volta para o menu
                    MenuState = 1
                    traps.stage = 0
                    GameMusic.stop()
                    MenuMusic.play()

                if event.key == pygame.K_e:  # Tecla para sair do Jogo
                    GameLoop = False

        # Tela

        draw()
        update()
        pygame.display.update()
