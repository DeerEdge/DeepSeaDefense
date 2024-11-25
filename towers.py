class Tower:
    def __init__(self, name, position):
        self.level = 1
        self.name = name
        self.position = position

    def getPosition(self):
        return self.position

class Patrol_Tower(Tower):
    iconPath = "assets/images/towers/patrol_tower.png"
    initialTowerRadius = 100
    tiers = {1: ["bullet", 1, 100, 100],
             2: ["bullet", 3, 100, 300],
             3: ["bullet", 4, 200, 450]}
    towerCost = 100

    def __init__(self, position, name="Patrol_Tower"):
        super().__init__(name, position)
        self.iconPath = "assets/images/towers/patrol_tower.png"
        self.tier = Patrol_Tower.tiers.get(self.level)
        self.towerRadius = self.tier[2]
        self.towerDamage = self.tier[3]
        self.cooldownDuration = 2
        self.cooldown = 0
        self.cost = 100

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