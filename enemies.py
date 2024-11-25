class Monster:
    def __init__(self, name, position, previousCoord, targetCoord):
        self.name = name
        self.position = position
        self.previousCoord = previousCoord
        self.targetCoord = targetCoord

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

class Serpent(Monster):
    def __init__(self, position, previousCoord, targetCoord, name="Serpent"):
        super().__init__(name, position, previousCoord, targetCoord)
        self.iconPath = "assets/images/enemies/serpent.png"

    def getIconPath(self):
        return self.iconPath