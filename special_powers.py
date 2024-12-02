from check_functions import *
from cmu_graphics import *

class Special_Power:
    def __init__(self, enemyList):
        self.targets = enemyList
        self.isAlive = True
        self.hitEnemies = False
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

    def getPosition(self):
        return self.position

class Missiles(Special_Power):
    def __init__(self, enemyList, *args):
        super().__init__(enemyList)

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

    def draw(self, position):
        drawImage('assets/images/special_powers/missile.png', position[0]-35, position[1]+45, width=90, height=90, align='center')
        drawImage('assets/images/special_powers/missile.png', position[0]-10, position[1]-10, width=120, height=120, align='center')
        drawImage('assets/images/special_powers/missile.png', position[0]+45, position[1]-35, width=90, height=90, align='center')
