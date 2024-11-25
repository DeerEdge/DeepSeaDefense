class Monster:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def getPosition(self):
        return self.position

    def setPosition(self, newPosition):
        self.position = newPosition
