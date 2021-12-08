import pygame
class Entity():

    tag = "Entity"

    def __init__(self, position, scale, gameLoop):
        self.position = [position[0], position[1]]
        self.scale = [scale[0], scale[1]]
        self.rect = pygame.Rect(self.position[0], self.position[1], self.scale[0], self.scale[1])
        self.image = pygame.image.load_extended("resources/blank.png").convert_alpha()
        self.gameLoop = gameLoop
        self.gameLoop.addEntity(self)
        self.dead = False

    def update(self, deltaTime):
        self.rect = pygame.Rect(self.position[0], self.position[1], self.scale[0], self.scale[1])
        self.deltaTime = deltaTime
        self.wrapAround()

    def wrapAround(self):
        wrapCount = 2
        if self.position[0] > 600:
            self.position[0] = 0 - self.scale[0]
            
        elif self.position[0] + self.scale[0] < 0:
            self.position[0] = 600
        
        else:
            wrapCount -= 1

        if self.position[1] > 600:
            self.position[1] = 0 - self.scale[1]

        elif self.position[1] + self.scale[1] < 0:
            self.position[1] = 600

        else: 
            wrapCount -= 1

        if wrapCount > 0:
            self.onWrap()

    def onWrap(self):
        pass

    def kill(self):
        if not self.dead:
            self.gameLoop.kill(self)

    def onCollisionEnter(self, other):
        pass