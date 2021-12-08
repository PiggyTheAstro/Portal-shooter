from bullet import Bullet
class FireManager():
    
    def __init__(self, fireRate, playerPos, gameLoop):
        self.fireRate = fireRate
        self.ticksPassed = 0
        self.canFire = True
        self.playerPos = playerPos
        self.gameLoop = gameLoop
        self.lastVector = [0, 0]

    def update(self, deltaTime):
        if not self.canFire:
            self.ticksPassed += deltaTime
            if self.ticksPassed > self.fireRate:
                self.canFire = True

    def shoot(self, vector):
        if not self.canFire:
            return
        bullet = Bullet(self.playerPos, (10, 10), self.gameLoop, vector)
        if self.lastVector != vector:
            self.gameLoop.addToScore(5)
        self.gameLoop.addToScore(5)
        self.canFire = False
        self.ticksPassed = 0
        self.lastVector = vector
