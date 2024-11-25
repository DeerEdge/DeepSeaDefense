from check_functions import *

class Projectile:
    def __init__(self, position, targetEnemy, damage, speed=5):
        self.position = position
        self.target = targetEnemy
        self.damage = damage
        self.speed = speed
        self.isAlive = True
        self.hitEnemy = False

class Bullet(Projectile):
    def __init__(self, position, targetEnemy, damage, ):
        super().__init__(position, targetEnemy, damage)

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

    def getPosition(self):
        return self.position