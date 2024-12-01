class Monster:
    def __init__(self, name, position, previousCoord, targetCoord):
        self.name = name
        self.position = position
        self.previousCoord = previousCoord
        self.targetCoord = targetCoord
        self.redCircleDuration = 0.25
        self.redCircleTimer = 0
        self.speed = None
        self.damage = None
        self.killScore = None


    def getKillScore(self):
        return self.killScore

    def getDamage(self):
        return self.damage

    def getSpeed(self):
        return self.speed

    def getPosition(self):
        return self.position

    def setPosition(self, newPosition):
        self.position = newPosition

    def getPreviousCoord(self):
        return self.previousCoord

    def setPreviousCoord(self, newPreviousCoord):
        self.previousCoord = newPreviousCoord

    def getTargetCoord(self):
        return self.targetCoord

    def setTargetCoord(self, newTargetCoord):
        self.targetCoord = newTargetCoord

    def showRedCircleEffect(self):
        self.redCircleTimer = self.redCircleDuration * 15

    def updateRedCircleEffect(self):
        if self.redCircleTimer > 0:
            self.redCircleTimer -= 1
            return True
        else:
            return False

class Serpent(Monster):
    healthPoints = 1000
    def __init__(self, position, previousCoord, targetCoord, name="Serpent"):
        super().__init__(name, position, previousCoord, targetCoord)
        self.iconPath = "assets/images/enemies/serpent.png"
        self.healthPoints = 1000
        self.reward = 50
        self.speed = 10
        self.movementType = "logarithmic"
        self.damage = 5
        self.killScore = 1000

    def getMovementType(self):
        return self.movementType

    def getIconPath(self):
        return self.iconPath

    def getReward(self):
        return self.reward

    def getHealth(self):
        return self.healthPoints

    def setHealth(self, newHealthPoints):
        if newHealthPoints < 0:
            self.healthPoints = 0
        else:
            self.healthPoints = newHealthPoints

class Slither(Monster):
    healthPoints = 500
    def __init__(self, position, previousCoord, targetCoord, name="Slither"):
        super().__init__(name, position, previousCoord, targetCoord)
        self.iconPath = "assets/images/enemies/slither.png"
        self.healthPoints = 500
        self.reward = 30
        self.speed = 10
        self.speedBoostActive = False
        self.movementType = "linear"
        self.damage = 3
        self.killScore = 1200

    def getMovementType(self):
        return self.movementType

    def getIconPath(self):
        return self.iconPath

    def getReward(self):
        return self.reward

    def getHealth(self):
        return self.healthPoints

    def setHealth(self, newHealthPoints):
        if newHealthPoints < 0:
            self.healthPoints = 0
        else:
            self.healthPoints = newHealthPoints

    def activateSpeedBoost(self):
        self.speedBoostActive = True

    def deactivateSpeedBoost(self):
        self.speedBoostActive = False

    def isSpeedBoostActive(self):
        return self.speedBoostActive


