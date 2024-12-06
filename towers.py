import random as rand

from map_assets import Minerals
from projectiles import *

class Tower:
    def __init__(self, name, position):
        self.level = 1
        self.name = name
        self.position = position
        self.iconPath = None
        self.tier = None
        self.towerType = "dynamic"
        self.towerRadius = None
        self.towerDamage = None
        self.cooldownDuration = None
        self.cooldown = None
        self.cost = None
        self.projectileType = None
        self.occupied = False
        self.hasProjectile = True
        self.doesAttack = True

    def getDoesAttack(self):
        return self.doesAttack

    def getLevel(self):
        return self.level

    def getName(self):
        return self.name

    def getHasProjectile(self):
        return self.hasProjectile

    def getTowerType(self):
        return self.towerType

    def getProjectileType(self):
        return self.projectileType

    def getPosition(self):
        return self.position

    def upgrade(self):
        if self.level < len(self.tiers):
            self.level += 1
            self.tier = self.tiers[self.level]
            self.towerRadius = self.tier[2]
            self.towerDamage = self.tier[3]

    def getUpgradeCost(self):
        return self.upgradeCosts.get(self.level+1, None)

    def getAttack(self):
        return self.tiers.get(self.level)

    def canAttack(self):
        if self.cooldown == 0:
            return True
        else:
            return False

    def reduceCooldown(self):
        if self.cooldown > 0:
            self.cooldown -= 1

    def startCooldown(self):
        self.cooldown = int(self.cooldownDuration*15)

    def getTowerDamage(self):
        return self.towerDamage

    def getTowerRadius(self):
        return self.towerRadius

    def getTowerCost(self):
        return self.cost

    def getIconPath(self):
        return self.iconPath

class Patrol_Tower(Tower):
    name = "Patrol_Tower"
    iconPath = "assets/images/towers/patrol-tower.png"
    initialTowerRadius = 100
    tiers = {1: [Bullet, 1, 100, 200],
             2: [Bullet, 3, 100, 300],
             3: [Bullet, 4, 200, 450]}
    towerCost = 100
    upgradeCosts = {2: 150, 3: 300}

    def __init__(self, position, name="Patrol_Tower"):
        super().__init__(name, position)
        self.projectileType = Bullet
        self.iconPath = "assets/images/towers/patrol-tower.png"
        self.tier = Patrol_Tower.tiers.get(self.level)
        self.towerRadius = self.tier[2]
        self.towerDamage = self.tier[3]
        self.cooldownDuration = 2
        self.cooldown = 0
        self.cost = 100

class Laser_Turret(Tower):
    name = "Laser_Turret"
    iconPath = "assets/images/towers/laser-turret.png"
    initialTowerRadius = 100
    #            PROJECTILE NONE RADIUS DAMAGE
    tiers = {1: [Laser, 1, 100, 5],
             2: [Laser, 1, 150, 10],
             3: [Laser, 1, 200, 15]}
    towerCost = 200
    upgradeCosts = {2: 200, 3: 400}

    def __init__(self, position, name="Laser_Turret"):
        super().__init__(name, position)
        self.projectileType = Laser
        self.iconPath = "assets/images/towers/laser-turret.png"
        self.tier = Laser_Turret.tiers.get(self.level)
        self.towerRadius = self.tier[2]
        self.towerDamage = self.tier[3]
        self.cooldownDuration = 0
        self.cooldown = 0
        self.cost = 100

# Teleportd enemies back to the start
class Magic_Portal(Tower):
    name = "Magic_Portal"
    iconPath = "assets/images/towers/magic-portal.png"
    initialTowerRadius = 100
    #            ANIMATION RADIUS DAMAGE NUM_TARGETS
    tiers = {1: [Light_Ray, 100, 5, 1],
             2: [Light_Ray, 100, 10, 3],
             3: [Light_Ray, 200, 15, 5]}
    towerCost = 100
    upgradeCosts = {2: 300, 3: 600}

    def __init__(self, position, name="Magic_Portal"):
        super().__init__(name, position)
        self.projectileType = Light_Ray
        self.iconPath = "assets/images/towers/magic-portal.png"
        self.tier = Magic_Portal.tiers.get(self.level)
        self.towerRadius = self.tier[1]
        self.towerDamage = self.tier[2]
        self.numMaxTargets = self.tier[3]
        self.cooldownDuration = 1.5
        self.cooldown = 0
        self.cost = 100

    def upgrade(self):
        if self.level < len(self.tiers):
            self.level += 1
            self.tier = self.tiers[self.level]
            self.towerRadius = self.tier[1]
            self.towerDamage = self.tier[2]

class Pulsar_Tower(Tower):
    name = "Pulsar_Tower"
    iconPath = "assets/images/towers/pulsar-tower.png"
    initialTowerRadius = 100
    tiers = {1: [Bullet, 1, 100, 100],
             2: [Bullet, 1, 100, 300],
             3: [Bullet, 1, 200, 450]}
    towerCost = 100
    upgradeCosts = {2: 150, 3: 300}

    def __init__(self, position, name="Pulsar_Tower"):
        super().__init__(name, position)
        self.iconPath = "assets/images/towers/pulsar-tower.png"
        self.tier = Patrol_Tower.tiers.get(self.level)
        self.towerRadius = self.tier[2]
        self.towerDamage = self.tier[3]
        self.cooldownDuration = 0.1
        self.cooldown = 0
        self.cost = 100


class Submarine(Tower):
    name = "Submarine"
    iconPath = "assets/images/towers/submarine.png"
    initialTowerRadius = 100
    #           PROJECTILE    RADIUS DAMAGE
    tiers = {1: [Bullet, 1, 300, 200],
             2: [Bullet, 1, 300, 300],
             3: [Bullet, 1, 400, 400]}
    towerCost = 100
    upgradeCosts = {2: 150, 3: 300}

    def __init__(self, position, name="Submarine"):
        super().__init__(name, position)
        self.iconPath = "assets/images/towers/submarine.png"
        self.tier = Patrol_Tower.tiers.get(self.level)
        self.towerRadius = self.tier[2]
        self.towerDamage = self.tier[3]
        self.cooldownDuration = 0.5
        self.cooldown = 0
        self.cost = 100
        self.boundaries = [(self.position[0],self.position[1]-100), (self.position[0], self.position[1] + 100),
                           (self.position[0]+200, self.position[1] + 100), (self.position[0]+200, self.position[1]-100)]
        self.targetCoord = self.boundaries[1]
        if not isWithinRectTopLeft(self.position[0], self.position[1] - 100, 200, 200, self.targetCoord[0], self.targetCoord[1]):
            self.targetCoord = (150,250)
            self.boundaries = [(150, 250), (150, 450), (550, 450), (550, 250)]
        self.projectileType = Bullet

    def move(self):
        oldPosition = self.position
        currentDist = getDistance(self.position, self.targetCoord)
        for stepX in [-5, 5]:
            newDist = getDistance((self.position[0]+stepX, self.position[1]), self.targetCoord)
            if newDist < currentDist:
                self.position = (self.position[0]+stepX, self.position[1])
                if getDistance(self.position, self.targetCoord) < 20:
                    index = (self.boundaries.index(self.targetCoord) + 1) % 4
                    self.targetCoord = self.boundaries[index]
                break
        if oldPosition == self.position:
            for stepY in [-5, 5]:
                newDist = getDistance((self.position[0], self.position[1]+stepY), self.targetCoord)
                if newDist < currentDist:
                    self.position = (self.position[0], self.position[1]+stepY)
                    if getDistance(self.position, self.targetCoord) < 20:
                        index = (self.boundaries.index(self.targetCoord) + 1) % 4
                        self.targetCoord = self.boundaries[index]
                    break

# Takes a set amount of health from N number of monsters
class Tooth_Trap(Tower):
    name = "Tooth_Trap"
    iconPath = "assets/images/towers/tooth-trap.png"
    initialTowerRadius = 25
    #           RADIUS DAMAGE NUM_TARGETS
    tiers = {1: [25, 200, 10],
             2: [25, 300, 15],
             3: [50, 450, 20]}
    towerCost = 100
    upgradeCosts = {2: 150, 3: 300}

    def __init__(self, position, name="Tooth_Trap"):
        super().__init__(name, position)
        self.iconPath = "assets/images/towers/tooth-trap.png"
        self.tier = Tooth_Trap.tiers.get(self.level)
        self.towerRadius = self.tier[0]
        self.towerDamage = self.tier[1]
        self.numMaxTargets = self.tier[2]
        self.attackedList = []
        self.isActive = True
        self.cost = 200
        self.towerType = "static"

    def doAction(self, enemy, *args):
        if enemy not in self.attackedList:
            self.attackedList.append(enemy)
            enemy.setHealth(enemy.getHealth() - self.towerDamage)
        elif len(self.attackedList) == self.numMaxTargets:
            self.isActive = False

    def getIsActive(self):
            return self.isActive

    def upgrade(self):
        if self.level < len(self.tiers):
            self.level += 1
            self.tier = self.tiers[self.level]
            self.towerRadius = self.tier[0]
            self.towerDamage = self.tier[1]
            self.numMaxTargets = self.tier[2]


# Slows enemies
class Monster_Net(Tower):
    name = "Monster_Net"
    iconPath = "assets/images/towers/monster-net.png"
    initialTowerRadius = 25
    #           RADIUS NUM_TARGETS
    tiers = {1: [25, 5],
             2: [25, 7],
             3: [50, 10]}
    towerCost = 100
    upgradeCosts = {2: 150, 3: 300}

    def __init__(self, position, name="Monster_Net"):
        super().__init__(name, position)
        self.iconPath = "assets/images/towers/monster-net.png"
        self.tier = Monster_Net.tiers.get(self.level)
        self.towerRadius = self.tier[0]
        self.numMaxTargets = self.tier[1]
        self.attackedList = []
        self.enemyDurationHoldingList = []
        self.holdingDuration = 0.3
        self.isActive = True
        self.maxReached = False
        self.cost = 200
        self.towerType = "static"
        self.doesAttack = False

    def upgrade(self):
        if self.level < len(self.tiers):
            self.level += 1
            self.tier = self.tiers[self.level]
            self.towerRadius = self.tier[0]
            self.numMaxTargets = self.tier[1]

    def doAction(self, enemy, *args):
        if not self.maxReached and len(self.attackedList) != self.numMaxTargets:
            if enemy not in self.attackedList:
                self.attackedList.append(enemy)
                self.enemyDurationHoldingList.append(self.holdingDuration * 15)
                enemy.setIsCaught(True)
        elif len(self.attackedList) == self.numMaxTargets:
            self.maxReached = True
        elif self.maxReached:
            if len(self.enemyDurationHoldingList) > 0:
                pass
            else:
                self.isActive = False

    def reduceHoldingDuration(self):
        if len(self.enemyDurationHoldingList) > 0:
            if self.enemyDurationHoldingList[0] <= 0:
                self.enemyDurationHoldingList.pop(0)
                self.attackedList[0].setIsCaught(False)
                self.attackedList.pop(0)
            else:
                self.enemyDurationHoldingList[0] -= 1

    def getIsActive(self):
        return self.isActive


# Mines resources and brings in profit
class Resource_Mine(Tower):
    name = "Resource_Mine"
    iconPath = "assets/images/towers/resource-mine.png"
    initialTowerRadius = 75
    #           RADIUS MONEY
    tiers = {1: [75, 200],
             2: [75, 400],
             3: [100, 800]}
    towerCost = 300
    upgradeCosts = {2: 600, 3: 1200}

    def __init__(self, position, name="Resource_Mine"):
        super().__init__(name, position)
        self.iconPath = "assets/images/towers/resource-mine.png"
        self.tier = Resource_Mine.tiers.get(self.level)
        self.towerRadius = self.tier[0]
        self.towerProfits = self.tier[1]
        self.cooldownDuration = 7
        self.cooldown = 0
        self.cost = 300
        self.isActive = True
        self.profitMultiplier = 1
        self.profit = 0
        self.towerType = "static"
        self.doesAttack = False

    def doAction(self, assetsList):
        for asset in assetsList:
            if (type(asset) == Minerals and getDistance(self.getPosition(), asset.getPosition()) < self.getTowerRadius()
                    + asset.getRadius()):
                self.profitMultiplier *= 1.1
        self.profit += int(self.towerProfits*self.profitMultiplier)

    def drawAnimation(self):
        if self.cooldown < 40:
            drawRect(self.position[0], self.position[1], 50, 50, fill='limegreen', opacity=(40-self.cooldown)*2.2,
                     align='center')
            drawStar(self.position[0]+rand.randint(30, 40), self.position[1]-rand.randint(5,10), 10, 10,
                     fill='blueViolet',align='center', rotateAngle=90)
            drawStar(self.position[0]-rand.randint(30, 40), self.position[1] -rand.randint(10,25), 10, 10,
                     fill='blueViolet', align='center',
                     rotateAngle=90)

    def upgrade(self):
        if self.level < len(self.tiers):
            self.level += 1
            self.tier = self.tiers[self.level]
            self.towerRadius = self.tier[0]
            self.towerProfits = self.tier[1]

    def getProfit(self):
        return self.profit

    def setProfit(self, amount):
        self.profit = amount

    def getIsActive(self):
        return self.isActive

