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

font = pygame.font.Font('data/fonts/8bits.ttf', 30)

text = font.render("Use essas teclas para mover o Galo Agiota Jr", True, (0, 0, 0), (79, 189, 240))
text2 = font.render("Objetivo:", True, (0, 0, 0), (79, 189, 240))
text3 = font.render("Chegue ate a bandeira para avancar de fase.", True, (0, 0, 0), (79, 189, 240))
text4 = font.render("EVITE AS ARMADILHAS!", True, (0, 0, 0), (79, 189, 240))
text5 = font.render("Aperte R para voltar.", True, (0, 0, 0), (79, 189, 240))
text6 = font.render("Para Jogar o modo dificil aperte H e depois aperte P.", True, (0, 0, 0), (79, 189, 240))

textRect = text.get_rect()
textRect.center = (700, 220)

textRect2 = text.get_rect()
textRect2 = (555, 400)

textRect3 = text.get_rect()
textRect3 = (350, 450)

textRect4 = text.get_rect()
textRect4 = (480, 500)

textRect5 = text.get_rect()
textRect5 = (480, 550)

textRect6 = text.get_rect()
textRect6 = (350, 300)

# Controladora do jogo
GameSystem = Game(player.animations, world.traps, world.flags, CacheLevel)

# Musicas
MenuMusic = pygame.mixer.Sound("data/soundtrack/MenuSong.mp3")
GameMusic = pygame.mixer.Sound("data/soundtrack/GameSong.mp3")
MenuMusic.play()

# Fps do jogo
fps = pygame.time.Clock()

#Fim de fases
fim = Game(player.animations, world.traps,world.flags, CacheLevel)

# Organizando as funçoes
def draw():
    if MenuState == 0:
        drawGame.draw(display)
    elif MenuState == 1:
        drawMenu.draw(display)
    elif MenuState == 2:
        drawHowToPlay.draw(display)
        display.blit(text, textRect)
        display.blit(text2, textRect2)
        display.blit(text3, textRect3)
        display.blit(text4, textRect4)
        display.blit(text5, textRect5)
        display.blit(text6, textRect6)


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

                if event.key == pygame.K_h and MenuState == 1:
                    GameSystem.level = 2

                if event.key == pygame.K_o:
                    if GameSystem.level < 5:
                        GameSystem.level += 1
                    if GameSystem.level == 4:
                        MenuState = 1
                        GameMusic.stop()
                        MenuMusic.play()
                        GameSystem.level = 0



        if GameSystem.dead == 1:  # GameOver, Volta para o menu
            MenuState = 1
            CacheLevel = 0
            drawGame.empty()
            world = World(CacheLevel)
            player = Player(world.collide, CacheLevel)
            drawGame.add(world.background)
            drawGame.add(player.animations)
            drawGame.add(world.objects)
            GameSystem = Game(player.animations, world.traps, world.flags, CacheLevel)
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
