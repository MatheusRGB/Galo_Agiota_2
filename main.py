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

#Função para iniciar o grupo de sprites Game
def initRender():
    drawGame.add(GameSystem.world.background)
    drawGame.add(GameSystem.player.animations)
    drawGame.add(GameSystem.world.objects)


initRender()

# Menu do Jogo
menu = Menu(display)

# Inicia o jogo no menu
MenuState = 1
#MenuState 0 jogando
#MenuState 1 menu principal
#MenuState 2 como jogar

# Cenario do Menu
drawMenu.add(menu.objects)

# Menu Como Jogar
howToPlay = HowToPlay(display)
drawHowToPlay.add(howToPlay.objects)
drawHowToPlay.add(GameSystem.world.ground)
drawHowToPlay.add(GameSystem.world.water)

# Musicas
MenuMusic = pygame.mixer.Sound("data/soundtrack/MenuSong.mp3")
GameMusic = pygame.mixer.Sound("data/soundtrack/GameSong.mp3")
MenuMusic.play() # Inicia a musica do menu

#Função para parar a música
def stopmusic():
    MenuMusic.stop()
    GameMusic.stop()


# Organizando as funçoes
def draw():
    if MenuState == 0: # Seting do jogo
        drawGame.draw(display)
    elif MenuState == 1: # Seting do menu
        drawMenu.draw(display)
    elif MenuState == 2: # Seting da aba como jogar
        drawHowToPlay.draw(display)

# Funções de atualização de cada State
def update():
    if MenuState == 0:
        drawGame.update()
        GameSystem.player.update()
        GameSystem.update()
    elif MenuState == 1:
        drawMenu.update()
        menu.update()
    elif MenuState == 2:
        howToPlay.update()

# Função para preparar o início do jogo
def startGame():
    stopmusic() # Para a música do menu
    drawGame.empty()
    GameSystem.playing = True
    GameSystem.points = 0 # Zera os pontos
    GameSystem.createStage() # Cria o nível
    GameMusic.play() #Inicia a música do jogo
    initRender() # Renderiza o game


# Fps do jogo
fps = pygame.time.Clock()
# Game rodando
GameLoop = True
if __name__ == '__main__':
    while GameLoop:
        fps.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Sair do Jogo
                GameLoop = False

            if event.type == pygame.KEYDOWN:
                if MenuState == 1 and event.key == pygame.K_p:  # Tecla para começar o jogo
                    MenuState = 0 # Coloca o State do jogo
                    GameSystem.hard = False # Deixa a dificuldade no fácil
                    startGame() # Inicia o jogo

                if event.key == pygame.K_c:  # Tecla para Menu Como Jogar
                    MenuState = 2 # Coloca o State de como jogar

                if MenuState == 2 and event.key == pygame.K_r:  # Pressione R para voltar para o Menu
                    MenuState = 1 # Coloca o State do menu do jogo

                if event.key == pygame.K_e:  # Tecla para sair do Jogo
                    GameLoop = False # Fecha o jogo

                if event.key == pygame.K_h and MenuState == 1: # Modo dificil
                    MenuState = 0 # Coloca o State do jogo
                    GameSystem.hard = True # Deixa a dificuldade no difícil
                    startGame() # Inicia o jogo

                if event.key == pygame.K_o and MenuState == 0:  # Tecla para pular de fase
                    GameSystem.nextLevel() # Passa o nível
                    startGame() # Inicia nível

        if GameSystem.collideFlag: # Atualizando sprites da tela e pontos do menu
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

        draw()
        update()
        pygame.display.update()
