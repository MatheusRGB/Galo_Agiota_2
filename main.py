import pygame
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
CacheLevel = 0
world = World(CacheLevel)
player = Player(world.collide, CacheLevel)
drawGame.add(world.background)
drawGame.add(player.animations)
drawGame.add(world.objects)

# Menu do Jogo
menu = Menu()

# Inicia o jogo no menu
MenuState = 1

# Cenario do Menu
drawMenu.add(menu.objects)

# Menu Como Jogar
ComoJogar = HowToPlay()
drawHowToPlay.add(ComoJogar.background)
drawHowToPlay.add(ComoJogar.imagem1)
drawHowToPlay.add(world.ground)
drawHowToPlay.add(world.water)

# Controladora do jogo
GameSystem = Game(player.animations, world.traps, world.flags, CacheLevel)

# Musicas
MenuMusic = pygame.mixer.Sound("data/soundtrack/MenuSong.mp3")
GameMusic = pygame.mixer.Sound("data/soundtrack/GameSong.mp3")
MenuMusic.play()

# Fps do jogo
fps = pygame.time.Clock()

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
        player.update()
        GameSystem.update()
    elif MenuState == 1:
        drawMenu.update()
        menu.update()


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
                    MenuMusic.stop()
                    GameMusic.stop()
                    GameMusic.play()

                if event.key == pygame.K_c:  # Tecla para Menu Como Jogar
                    MenuState = 2

                if MenuState == 2 and event.key == pygame.K_r:  # Pressione R para voltar para o Menu
                    MenuState = 1

                if event.key == pygame.K_e:  # Tecla para sair do Jogo
                    GameLoop = False
        if GameSystem.dead == 1:  # GameOver, Volta para o menu
            MenuState = 1
            GameSystem.dead = 0
            GameMusic.stop()
            MenuMusic.stop()
            MenuMusic.play()
        if GameSystem.level != world.stage:
            if CacheLevel < GameSystem.level:
                CacheLevel = GameSystem.level
            drawGame.empty()
            world = World(CacheLevel)
            player = Player(world.collide, CacheLevel)
            drawGame.add(world.background)
            drawGame.add(player.animations)
            drawGame.add(world.objects)
            GameSystem = Game(player.animations, world.traps, world.flags, CacheLevel)

        # Tela

        draw()
        update()
        pygame.display.update()
