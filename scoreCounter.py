
class ScoreCounter():

    def __init__(self):
        self.score = 0

    def updateScore(self, deltaTime):
        self.score += deltaTime

    def addScore(self, value):
        self.score += value
