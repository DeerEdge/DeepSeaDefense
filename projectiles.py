from check_functions import *
from cmu_graphics import *

class Projectile:
    def __init__(self, position, targetEnemy, damage, parentTower, speed=5):
        self.position = position
        self.target = targetEnemy
        self.damage = damage
        self.speed = speed
        self.parentTower = parentTower
        self.isAlive = True
        self.hitEnemy = False
        self.actionType = None
        self.pathCoordsList = None

    def changeEnemy(self, enemiesList, currentEnemy):
        currentEnemyIndex = enemiesList.index(currentEnemy)
        if len(enemiesList) > currentEnemyIndex+1:
            newTarget = enemiesList[currentEnemyIndex+1]
            self.target = newTarget
        else:
            self.target = None

    def getEnemy(self):
        return self.target

    def getActionType(self):
        return self.actionType

    def getPosition(self):
        return self.position

    def getParentTower(self):
        return self.parentTower

class Bullet(Projectile):
    def __init__(self, position, targetEnemy, damage, tower, *args):
        super().__init__(position, targetEnemy, damage, tower)
        self.actionType = "object"
        self.speed=15

    def move(self):
        if self.isAlive == False:
            return self.position

        targetPosition = self.target.getPosition()
        distance = getDistance(targetPosition, self.position)

        if distance < self.speed:
            self.position = targetPosition
            self.hitEnemy = True
            self.isAlive = False
        else:
            distChangeX = (targetPosition[0] - self.position[0])/distance
            distChangeY = (targetPosition[1] - self.position[1])/distance
            self.position = (self.position[0] + distChangeX * self.speed,
                             self.position[1] + distChangeY * self.speed)
        return self.position

    def draw(self, position, size):
        if getDistance(self.target.getPosition(), self.parentTower.getPosition()) < self.parentTower.getTowerRadius():
            drawCircle(position[0], position[1], size)

class Laser(Projectile):
    def __init__(self, position, targetEnemy, damage, tower, *args):
        super().__init__(position, targetEnemy, damage, tower)
        self.actionType = "continuous"

    def __repr__(self):
        return f'Laser pointing at {self.target}'

    def move(self):
        targetPosition = self.target.getPosition()
        if self.target.getHealth() <= 0 or (getDistance(targetPosition, self.getParentTower().getPosition()) > self.getParentTower().getTowerRadius()):
            self.isAlive = False

        return targetPosition

    def draw(self, position, intensity):
        if self.target != None and getDistance(self.target.getPosition(), self.parentTower.getPosition()) < self.parentTower.getTowerRadius():
            targetPosition = self.target.getPosition()
            drawLine(self.position[0], self.position[1], targetPosition[0], targetPosition[1], fill='red')

class Light_Ray(Projectile):
    def __init__(self, position, targetEnemy, damage, tower, pathCoordsList):
        super().__init__(position, targetEnemy, damage, tower)
        self.actionType = "object"
        self.stepCounter = 0
        self.pathCoordsList = pathCoordsList

    def move(self):
        targetPosition = self.target.getPosition()
        if self.target.getHealth() <= 0 or (getDistance(targetPosition, self.getParentTower().getPosition()) > self.getParentTower().getTowerRadius()):
            self.isAlive = False
        if self.stepCounter > 7:
            self.stepCounter = 0
            self.target.setPreviousCoord(self.pathCoordsList[0])
            self.target.setTargetCoord(self.pathCoordsList[1])
            self.target.setPosition(self.pathCoordsList[0])

        return targetPosition

    def draw(self, position, intensity):
        self.stepCounter += 1
        if self.stepCounter < 3:
            innerColorFill = "white"
            borderLeftColorFill = "darkViolet"
            borderRightColorFill = "indigo"
        elif self.stepCounter < 6:
            innerColorFill = "white"
            borderLeftColorFill = "indigo"
            borderRightColorFill = "purple"
        else:
            innerColorFill = "indigo"
            borderLeftColorFill = "darkMagenta"
            borderRightColorFill = "white"

        if self.target != None and getDistance(self.target.getPosition(), self.parentTower.getPosition()) < self.parentTower.getTowerRadius():
            targetPosition = self.target.getPosition()
            drawLine(self.position[0], self.position[1], targetPosition[0]+3, targetPosition[1]-3, fill=borderRightColorFill, lineWidth=3)
            drawLine(self.position[0], self.position[1], targetPosition[0] - 3, targetPosition[1] + 3, fill=innerColorFill, lineWidth=5)
            drawLine(self.position[0], self.position[1], targetPosition[0], targetPosition[1], fill=borderLeftColorFill, lineWidth=3)
            drawStar(targetPosition[0], targetPosition[1], 30, 7, fill=borderLeftColorFill, opacity=(self.stepCounter*9))
            drawStar(targetPosition[0], targetPosition[1], 30, 7, fill="mediumSlateBlue", opacity=(self.stepCounter*5), rotateAngle=45)
        elif self.target != None:
            targetPosition = self.target.getPosition()
            drawStar(targetPosition[0], targetPosition[1], 30, 7, fill="indigo", opacity=80)





