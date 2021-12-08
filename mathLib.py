import math
class MathLib():

    def getVectorMagnitude(vector):
        return math.sqrt(vector[0] * vector[0] + vector[1] * vector[1])

    def normalizeVector(vector):
        tempMagnitude = MathLib.getVectorMagnitude(vector)
        if tempMagnitude == 0:
            return vector
        vector[0] /= tempMagnitude
        vector[1] /= tempMagnitude
        return (vector[0], vector[1])
    
    def getDistance(firstVec, secondVec):
        return [firstVec[0] - secondVec[0], firstVec[1] - secondVec[1]]
