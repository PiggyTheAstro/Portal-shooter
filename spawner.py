from entity import Entity
from mathLib import MathLib
from enemy import Enemy
import random


class Spawner(Entity):

    def __init__(self, position, scale, gameLoop, player):
        super().__init__(position, scale, gameLoop)
        self.player = player
        self.currentTime = 0
        self.difficulty = 0
        self.rerollSpawnTime()

    def update(self, deltaTime):
        super().update(deltaTime)
        self.currentTime += deltaTime
        if self.currentTime > self.nextSpawn:
            self.spawnEnemy()
            self.currentTime = 0

    def rerollSpawnTime(self):
        self.nextSpawn = float(random.randrange(200, 600) / 100)
        self.difficulty += float(random.randrange(10, 100) / 100)

    def spawnEnemy(self):
        self.randMove()
        Enemy(self.position, (25, 25), self.gameLoop, self.player, self.difficulty)
        self.rerollSpawnTime()

    def randMove(self):
        self.position[0] = random.randint(0, 600)
        self.position[1] = random.randint(0, 600)
        if MathLib.getVectorMagnitude(MathLib.getDistance(self.position, self.player.position)) < 100:
            self.randMove()
