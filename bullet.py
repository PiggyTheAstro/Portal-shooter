from entity import Entity
import pygame


class Bullet(Entity):

    tag = "Bullet"

    def __init__(self, position, scale, gameLoop, vector):
        super().__init__(position, scale, gameLoop)
        self.vector = vector
        self.hostile = False
        self.moveSpeed = 350
        self.image = pygame.image.load_extended(
            "resources/bullet.png").convert_alpha()

    def update(self, deltaTime):
        super().update(deltaTime)
        self.position[0] += self.vector[0] * self.moveSpeed * deltaTime
        self.position[1] += self.vector[1] * self.moveSpeed * deltaTime

    def onWrap(self):
        self.image = pygame.image.load_extended(
            "resources/hostileBullet.png").convert_alpha()
        self.hostile = True

    def onCollisionEnter(self, other):
        if self.hostile and other.tag != "Bullet":
            self.kill()
            self.dead = True
