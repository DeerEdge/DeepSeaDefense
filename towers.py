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
    iconPath = "assets/images/towers/patrol-tower.png"
    initialTowerRadius = 100
    tiers = {1: [Bullet, 1, 100, 100],
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
    iconPath = "assets/images/towers/laser-turret.png"
    initialTowerRadius = 100
    #            PROJECTILE NONE RADIUS DAMAGE
    tiers = {1: [Laser, 1, 100, 5],
             2: [Laser, 3, 150, 10],
             3: [Laser, 4, 200, 15]}
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

class Tesla_Coil(Tower):
    iconPath = "assets/images/towers/tesla-coil.png"
    initialTowerRadius = 100
    tiers = {1: [Bullet, 1, 100, 100],
             2: [Bullet, 3, 100, 300],
             3: [Bullet, 4, 200, 450]}
    towerCost = 100
    upgradeCosts = {2: 150, 3: 300}

    def __init__(self, position, name="Tesla_Coil"):
        super().__init__(name, position)
        self.iconPath = "assets/images/towers/tesla-coil.png"
        self.tier = Patrol_Tower.tiers.get(self.level)
        self.towerRadius = self.tier[2]
        self.towerDamage = self.tier[3]
        self.cooldownDuration = 0
        self.cooldown = 0
        self.cost = 100

class Resource_Mine(Tower):
    iconPath = "assets/images/towers/resource-mine.png"
    initialTowerRadius = 100
    tiers = {1: [Bullet, 1, 100, 100],
             2: [Bullet, 3, 100, 300],
             3: [Bullet, 4, 200, 450]}
    towerCost = 100
    upgradeCosts = {2: 150, 3: 300}

    def __init__(self, position, name="Resource_Mine"):
        super().__init__(name, position)
        self.iconPath = "assets/images/towers/resource-mine.png"
        self.tier = Patrol_Tower.tiers.get(self.level)
        self.towerRadius = self.tier[2]
        self.towerDamage = self.tier[3]
        self.cooldownDuration = 2
        self.cooldown = 0
        self.cost = 100

class Missile_Mech(Tower):
    iconPath = "assets/images/towers/missile-mech.png"
    initialTowerRadius = 100
    tiers = {1: [Bullet, 1, 100, 100],
             2: [Bullet, 3, 100, 300],
             3: [Bullet, 4, 200, 450]}
    towerCost = 100
    upgradeCosts = {2: 150, 3: 300}

    def __init__(self, position, name="Missile_Mech"):
        super().__init__(name, position)
        self.iconPath = "assets/images/towers/missile-mech.png"
        self.tier = Patrol_Tower.tiers.get(self.level)
        self.towerRadius = self.tier[2]
        self.towerDamage = self.tier[3]
        self.cooldownDuration = 2
        self.cooldown = 0
        self.cost = 100

class Pulsar_Tower(Tower):
    iconPath = "assets/images/towers/pulsar-tower.png"
    initialTowerRadius = 100
    tiers = {1: [Bullet, 1, 100, 100],
             2: [Bullet, 3, 100, 300],
             3: [Bullet, 4, 200, 450]}
    towerCost = 100
    upgradeCosts = {2: 150, 3: 300}

    def __init__(self, position, name="Pulsar_Tower"):
        super().__init__(name, position)
        self.iconPath = "assets/images/towers/pulsar-tower.png"
        self.tier = Patrol_Tower.tiers.get(self.level)
        self.towerRadius = self.tier[2]
        self.towerDamage = self.tier[3]
        self.cooldownDuration = 2
        self.cooldown = 0
        self.cost = 100

class Submarine(Tower):
    iconPath = "assets/images/towers/submarine.png"
    initialTowerRadius = 100
    tiers = {1: [Bullet, 1, 100, 100],
             2: [Bullet, 3, 100, 300],
             3: [Bullet, 4, 200, 450]}
    towerCost = 100
    upgradeCosts = {2: 150, 3: 300}

    def __init__(self, position, name="Submarine"):
        super().__init__(name, position)
        self.iconPath = "assets/images/towers/submarine.png"
        self.tier = Patrol_Tower.tiers.get(self.level)
        self.towerRadius = self.tier[2]
        self.towerDamage = self.tier[3]
        self.cooldownDuration = 2
        self.cooldown = 0
        self.cost = 100

# Takes a set amount of health from N number of monsters
class Tooth_Trap(Tower):
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

    def doAction(self, enemy):
        if enemy not in self.attackedList:
            self.attackedList.append(enemy)
            enemy.setHealth(enemy.getHealth() - self.towerDamage)
        elif len(self.attackedList) == self.numMaxTargets:
            self.isActive = False

    def getIsActive(self):
            return self.isActive

# Slows enemies
class Monster_Net(Tower):
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

    def doAction(self, enemy):
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
        print(self.attackedList)
        print(self.enemyDurationHoldingList)
        if len(self.enemyDurationHoldingList) > 0:
            if self.enemyDurationHoldingList[0] <= 0:
                self.enemyDurationHoldingList.pop(0)
                self.attackedList[0].setIsCaught(False)
                self.attackedList.pop(0)
            else:
                self.enemyDurationHoldingList[0] -= 1

    def getIsActive(self):
        return self.isActive
