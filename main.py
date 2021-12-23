import pygame
from utils import *
from menu import *
from game import *

# Initiation
pygame.init()
display = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Galo Agiota 2")

# Grupo de Sprites
drawGame = pygame.sprite.Group()  # Game
drawMenu = pygame.sprite.Group()  # Menu
drawHowToPlay = pygame.sprite.Group()  # Como jogar

# Cenario de Jogo
GameSystem = Game(display)


def initRender():
    drawGame.add(GameSystem.world.background)
    drawGame.add(GameSystem.player.animations)
    drawGame.add(GameSystem.world.objects)


initRender()

# Menu do Jogo
menu = Menu(display)

# Inicia o jogo no menu
MenuState = 1

# Cenario do Menu
drawMenu.add(menu.objects)

# Menu Como Jogar
ComoJogar = HowToPlay(display)
drawHowToPlay.add(ComoJogar.background)
drawHowToPlay.add(ComoJogar.imagem1)
drawHowToPlay.add(ComoJogar.imagem2)
drawHowToPlay.add(ComoJogar.imagem3)

drawHowToPlay.add(GameSystem.world.ground)
drawHowToPlay.add(GameSystem.world.water)

# Musicas
MenuMusic = pygame.mixer.Sound("data/soundtrack/MenuSong.mp3")
GameMusic = pygame.mixer.Sound("data/soundtrack/GameSong.mp3")
MenuMusic.play()

# Fps do jogo
fps = pygame.time.Clock()


def stopmusic():
    MenuMusic.stop()
    GameMusic.stop()


# Organizando as funçoes
def draw():
    if MenuState == 0:
        drawGame.draw(display)
    elif MenuState == 1:
        drawMenu.draw(display)
    elif MenuState == 2:
        drawHowToPlay.draw(display)


def update():
    if MenuState == 0:
        drawGame.update()
        GameSystem.player.update()
        GameSystem.update()
    elif MenuState == 1:
        drawMenu.update()
        menu.update()
    elif MenuState == 2:
        ComoJogar.update()


# Game rodando
GameLoop = True
if __name__ == '__main__':
    while GameLoop:

        fps.tick(60)
        #menustate 0 jogando
        #menustate 1 menu principal
        #menustate 2 como jogar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Sair do Jogo
                GameLoop = False

            if event.type == pygame.KEYDOWN:
                if MenuState == 1 and event.key == pygame.K_p:  # Tecla para começar o jogo
                    MenuState = 0
                    stopmusic()
                    GameMusic.play()
                    GameSystem.playing = True

                if event.key == pygame.K_c:  # Tecla para Menu Como Jogar
                    MenuState = 2

                if MenuState == 2 and event.key == pygame.K_r:  # Pressione R para voltar para o Menu
                    MenuState = 1

                if event.key == pygame.K_e:  # Tecla para sair do Jogo
                    GameLoop = False

                if event.key == pygame.K_h and MenuState == 1:
                    MenuState = 0
                    stopmusic()
                    GameMusic.play()
                    drawGame.empty()
                    GameSystem.level = 2
                    GameSystem.createStage()
                    initRender()
                    GameSystem.playing = True

                if event.key == pygame.K_o and MenuState == 0:  # Tecla para pular de fase
                    drawGame.empty()
                    GameSystem.nextLevel()
                    GameSystem.createStage()
                    initRender()
                    GameSystem.playing = True

        if GameSystem.collideFlag:
            drawGame.empty()
            initRender()
            if menu.points < GameSystem.points:
                menu.points = GameSystem.points

        if GameSystem.dead or GameSystem.gameover:  # GameOver, Volta para o menu
            GameSystem.gameover = False
            GameSystem.dead = False
            MenuState = 1
            drawGame.empty()
            initRender()
            stopmusic()
            MenuMusic.play()

        # Tela

        draw()
        update()
        pygame.display.update()
