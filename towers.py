class Tower:
    def __init__(self, name, position):
        self.level = 1
        self.name = name
        self.position = position

    def getPosition(self):
        return self.position

class Patrol_Tower(Tower):
    iconPath = "assets/images/towers/patrol-tower.png"
    initialTowerRadius = 100
    tiers = {1: ["bullet", 1, 100, 100],
             2: ["bullet", 3, 100, 300],
             3: ["bullet", 4, 200, 450]}
    towerCost = 100
    upgradeCosts = {2: 150, 3: 300}

    def __init__(self, position, name="Patrol_Tower"):
        super().__init__(name, position)
        self.iconPath = "assets/images/towers/patrol-tower.png"
        self.tier = Patrol_Tower.tiers.get(self.level)
        self.towerRadius = self.tier[2]
        self.towerDamage = self.tier[3]
        self.cooldownDuration = 2
        self.cooldown = 0
        self.cost = 100

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

class Laser_Turret(Tower):
    iconPath = "assets/images/towers/laser-turret.png"

class Magic_Portal(Tower):
    iconPath = "assets/images/towers/magic-portal.png"

class Tesla_Coil(Tower):
    iconPath = "assets/images/towers/tesla-coil.png"

class Resource_Mine(Tower):
    iconPath = "assets/images/towers/resource-mine.png"

class Missile_Mech(Tower):
    iconPath = "assets/images/towers/missile-mech.png"

class Pulsar_Tower(Tower):
    iconPath = "assets/images/towers/pulsar-tower.png"

class Submarine(Tower):
    iconPath = "assets/images/towers/submarine.png"

class Tooth_Trap(Tower):
    iconPath = "assets/images/towers/tooth-trap.png"

class Monster_Net(Tower):
    iconPath = "assets/images/towers/monster-net.png"

