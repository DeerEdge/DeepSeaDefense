class Tower:
    def __init__(self, name, position):
        self.level = 1
        self.name = name
        self.position = position

    def getPosition(self):
        return self.position

class Patrol_Tower(Tower):
    iconPath = "assets/images/towers/patrol_tower.png"
    def __init__(self, position, name="Patrol_Tower"):
        super().__init__(name, position)
        self.iconPath = "assets/images/towers/patrol_tower.png"
        self.tiers = {1:["projectile", 1, 20],
                      2:["projectile", 3, 20],
                      3:["projectile", 4, 30]}

    def getAttack(self):
        return self.tiers.get(self.level)

    def getIconPath(self):
        return self.iconPath