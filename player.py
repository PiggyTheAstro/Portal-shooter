from entity import Entity
from mathLib import MathLib
from fireManager import FireManager
import pygame

class Player(Entity):

    tag = "Player"

    def __init__(self, position, scale, gameLoop):
        super().__init__(position, scale, gameLoop)
        self.moveSpeed = 250
        self.fireManager = FireManager(0.5, self.position, gameLoop)
        self.wrapCooldown = 0
        self.image = pygame.image.load_extended(
            "resources/player.png").convert_alpha()
        self.rotation = 0

    def update(self, deltaTime):
        super().update(deltaTime)
        self.move(deltaTime)
        self.fireManager.update(deltaTime)
        fireVec = self.getInput(
            pygame.K_RIGHT, pygame.K_LEFT, pygame.K_DOWN, pygame.K_UP)
        if fireVec != [0, 0]:
            self.rotate(fireVec[0], fireVec[1])
            self.fireManager.shoot(fireVec)
        if self.wrapCooldown < 6:
            self.wrapCooldown += deltaTime

    def getInput(self, right, left, down, up):
        rawInput = [0, 0]
        rawInput[0] += self.inputManager.getInputEvent(right)
        rawInput[0] -= self.inputManager.getInputEvent(left)
        rawInput[1] += self.inputManager.getInputEvent(down)
        rawInput[1] -= self.inputManager.getInputEvent(up)
        rawInput = MathLib.normalizeVector(rawInput)
        return rawInput

    def setInputManager(self, inputManager):
        self.inputManager = inputManager

    def move(self, deltaTime):
        movementVector = self.getInput(
            pygame.K_d, pygame.K_a, pygame.K_s, pygame.K_w)
        self.position[0] += movementVector[0] * self.moveSpeed * deltaTime
        self.position[1] += movementVector[1] * self.moveSpeed * deltaTime

    def onCollisionEnter(self, other):
        if other.tag == "Bullet" and other.hostile or other.tag == "Enemy":
            self.kill()
            self.dead = True
            self.gameLoop.running = False

    def onWrap(self):
        if self.wrapCooldown > 5:
            self.gameLoop.addToScore(15)
            self.wrapCooldown = 0

    def rotate(self, x, y):
        xIndex = int(x + 1)
        yIndex = int(y + 1)
        table = [[self.rotation, 90, self.rotation], [0, self.rotation, 180],
                 [self.rotation, -90, self.rotation]]
        self.image = pygame.transform.rotate(
            self.image, table[xIndex][yIndex] - self.rotation)
        self.rotation = table[xIndex][yIndex]
