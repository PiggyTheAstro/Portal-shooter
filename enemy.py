from entity import Entity
from mathLib import MathLib
import pygame


class Enemy(Entity):

    tag = "Enemy"

    def __init__(self, position, scale, gameLoop, player, difficulty):
        super().__init__(position, scale, gameLoop)
        self.player = player
        self.moveSpeed = 100 + difficulty * 5
        self.health = 1 + difficulty / 5
        self.image = pygame.image.load_extended(
            "resources/enemy.png").convert_alpha()

    def update(self, deltaTime):
        super().update(deltaTime)
        vector = MathLib.normalizeVector(
            MathLib.getDistance(self.position, self.player.position))
        self.position[0] -= vector[0] * self.moveSpeed * deltaTime
        self.position[1] -= vector[1] * self.moveSpeed * deltaTime

    def onCollisionEnter(self, other):
        if other.tag == "Bullet" and other.hostile:
            self.health -= 1
            if self.health > 0:
                self.gameLoop.addToScore(100)
        if self.health < 1:
            self.kill()
            self.dead = True
