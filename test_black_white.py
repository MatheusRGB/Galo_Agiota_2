from main import *

#===============TESTE DE CAIXA PRETA===============

#VERIFICA SE A PRIMEIRA TELA É O MENU
def test_menu_inicio():
    assert MenuState == 1

def test_game_iniciado():
    assert GameLoop == True

def test_draw_menu():
    assert len(drawMenu.sprites()) >= 1

def test_draw_game():
    assert len(drawGame.sprites()) >= 1

def test_draw_howtoplay():
    assert len(drawHowToPlay.sprites()) >= 1

#===============TESTE DE CAIXA BRANCA===============

def test_player_inicio():
    assert GameSystem.player != None

def test_world_inicio():
    assert GameSystem.world != None

def test_player_life():
    assert GameSystem.dead == False

def test_points_inicio():
    assert GameSystem.points == 0

def test_player_gameover():
    assert GameSystem.gameover == False

