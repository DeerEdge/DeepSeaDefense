from projectiles import *

class Tower:
    def __init__(self, name, position):
        self.level = 1
        self.name = name
        self.position = position
        self.iconPath = None
        self.tier = None
        self.towerRadius = None
        self.towerDamage = None
        self.cooldownDuration = None
        self.cooldown = None
        self.cost = None
        self.projectileType = None
        self.occupied = False

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

class Magic_Portal(Tower):
    iconPath = "assets/images/towers/magic-portal.png"
    initialTowerRadius = 100
    tiers = {1: [Bullet, 1, 100, 100],
             2: [Bullet, 3, 100, 300],
             3: [Bullet, 4, 200, 450]}
    towerCost = 100
    upgradeCosts = {2: 150, 3: 300}

    def __init__(self, position, name="Magic_Portal"):
        super().__init__(name, position)
        self.iconPath = "assets/images/towers/magic-portal.png"
        self.tier = Patrol_Tower.tiers.get(self.level)
        self.towerRadius = self.tier[2]
        self.towerDamage = self.tier[3]
        self.cooldownDuration = 2
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

class Tooth_Trap(Tower):
    iconPath = "assets/images/towers/tooth-trap.png"
    initialTowerRadius = 100
    tiers = {1: [Bullet, 1, 100, 100],
             2: [Bullet, 3, 100, 300],
             3: [Bullet, 4, 200, 450]}
    towerCost = 100
    upgradeCosts = {2: 150, 3: 300}

    def __init__(self, position, name="Tooth_Trap"):
        super().__init__(name, position)
        self.iconPath = "assets/images/towers/tooth-trap.png"
        self.tier = Patrol_Tower.tiers.get(self.level)
        self.towerRadius = self.tier[2]
        self.towerDamage = self.tier[3]
        self.cooldownDuration = 2
        self.cooldown = 0
        self.cost = 100

class Monster_Net(Tower):
    iconPath = "assets/images/towers/monster-net.png"
    initialTowerRadius = 100
    tiers = {1: [Bullet, 1, 100, 100],
             2: [Bullet, 3, 100, 300],
             3: [Bullet, 4, 200, 450]}
    towerCost = 100
    upgradeCosts = {2: 150, 3: 300}

    def __init__(self, position, name="Monster_Net"):
        super().__init__(name, position)
        self.iconPath = "assets/images/towers/monster-net.png"
        self.tier = Patrol_Tower.tiers.get(self.level)
        self.towerRadius = self.tier[2]
        self.towerDamage = self.tier[3]
        self.cooldownDuration = 2
        self.cooldown = 0
        self.cost = 100

