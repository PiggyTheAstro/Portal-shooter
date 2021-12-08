import pygame
import sys
from eventQueue import EventQueue
from scoreCounter import ScoreCounter
class Game():

    def __init__(self):
        pygame.init()
        self.running = True
        self.window = pygame.display.set_mode((600, 600))
        self.entities = []
        self.deadEntities = []
        self.eventManager = EventQueue()
        self.scoreCounter = ScoreCounter()
        self.clock = pygame.time.Clock()
        self.scoreFont = pygame.font.SysFont("Hightowertext", 30)
        self.gameOverFont = pygame.font.SysFont("Papyrus", 50)
    
    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.eventManager.addInputEvent(event.key)
            elif event.type == pygame.KEYUP:
                self.eventManager.removeInputEvent(event.key)

    def update(self):
        self.clock.tick()
        deltaTime = self.clock.get_time()
        self.detectCollisions()
        for i in range(len(self.entities)):
            self.entities[i].update(deltaTime / 1000)
        for i in range(len(self.deadEntities) - 1, -1, -1):
            if self.deadEntities[i].tag == "Enemy":
                self.scoreCounter.addScore(500)
            self.entities.remove(self.deadEntities[i])
            del self.deadEntities[i]
        self.scoreCounter.updateScore(deltaTime / 1000)

    def detectCollisions(self):
        for i in range(len(self.entities)):
            for j in range(len(self.entities)):
                if i is not j and pygame.Rect.colliderect(self.entities[i].rect, self.entities[j].rect):
                    self.entities[i].onCollisionEnter(self.entities[j])

    def render(self):
        self.window.fill((0, 0, 0))
        for i in range(len(self.entities)):
            pass
            pygame.draw.rect(self.window, (0, 0, 0), self.entities[i].rect)
            self.window.blit(self.entities[i].image, self.entities[i].rect)
        self.window.blit(self.scoreFont.render(str(int(self.scoreCounter.score)), 1, (255, 255, 255)), (30, 30))
        pygame.display.flip()

    def addEntity(self, entity):
        self.entities.append(entity)
    
    def kill(self, entity):
        self.deadEntities.append(entity)

    def addToScore(self, value):
        self.scoreCounter.addScore(value)

    def gameOver(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.gameOverFont.render("Score: " + str(int(self.scoreCounter.score)), 1, (255, 0, 0)), (20, 300))
        self.window.blit(self.gameOverFont.render("GAME OVER!", 1, (255, 0, 0)), (100, 200))
        pygame.display.flip()
        



