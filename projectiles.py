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
    def __init__(self, position, targetEnemy, damage, tower):
        super().__init__(position, targetEnemy, damage, tower)
        self.actionType = "object"

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
        drawCircle(position[0], position[1], size)

class Laser(Projectile):
    def __init__(self, position, targetEnemy, damage, tower):
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
        if self.target != None:
            targetPosition = self.target.getPosition()
            drawLine(self.position[0], self.position[1], targetPosition[0], targetPosition[1], fill='red')

