import pygame
from game import Game
from player import Player
from enemy import Enemy
from spawner import Spawner
def main():
    gameLoop = Game()
    playerShip = Player((300, 300), (20, 20), gameLoop)
    enemySpawner = Spawner((80, 100), (0, 0), gameLoop, playerShip)
    playerShip.setInputManager(gameLoop.eventManager)
    loop(gameLoop)

def loop(gameLoop):
    while gameLoop.running:
        print(gameLoop.clock.get_fps())
        gameLoop.processEvents()
        gameLoop.update()
        gameLoop.render()

    while True:
        gameLoop.processEvents()
        gameLoop.gameOver()

if __name__ == '__main__':
    main()
