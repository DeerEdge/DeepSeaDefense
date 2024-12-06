from check_functions import *
from cmu_graphics import *

class Asset:
    def __init__(self, position):
        self.position = position
        self.radius = None
        self.color = None
        self.borderColor = None
        self.iconPath = ''
        self.name = ''

    def getColor(self):
        return self.color

    def getBorderColor(self):
        return self.borderColor

    def getPosition(self):
        return self.position

    def getRadius(self):
        return self.radius

    def getIconPath(self):
        return self.iconPath

    def getName(self):
        return self.name


class Acid_74(Asset):
    iconPath = "assets/images/map_assets/acid-74.png"
    radius = 100
    color = "paleGreen"
    borderColor = 'darkRed'
    name = "Acid_74"
    function = "Heals enemies in"
    functionCont = "range"
    def __init__(self, position, *args):
        super().__init__(position)
        self.iconPath = "assets/images/map_assets/acid-74.png"
        self.radius = 100
        self.color = "paleGreen"
        self.borderColor = 'darkRed'
        self.name = "Acid_74"

    def __repr__(self):
        return self.name + str(self.position)

    def draw(self, position):
        drawCircle(position[0], position[1])


class Fog(Asset):
    iconPath = "assets/images/map_assets/fog.png"
    radius = 100
    color = "silver"
    borderColor = 'dimGray'
    name = "Fog"
    function = "Invisible to towers"
    functionCont = "in area"
    def __init__(self, position, *args):
        super().__init__(position)
        self.iconPath = "assets/images/map_assets/fog.png"
        self.radius = 100
        self.color = "silver"
        self.borderColor = 'dimGray'
        self.name = "Fog"

    def __repr__(self):
        return self.name + str(self.position)

    def draw(self, position):
        drawCircle(position[0], position[1])


class Minerals(Asset):
    iconPath = "assets/images/map_assets/minerals.png"
    radius = 150
    color = 'orchid'
    borderColor = 'mediumOrchid'
    name = "Minerals"
    function = "Boosts resource"
    functionCont = "mining"
    def __init__(self, position, *args):
        super().__init__(position)
        self.iconPath = "assets/images/map_assets/minerals.png"
        self.radius = 150
        self.color = "orchid"
        self.borderColor = 'mediumOrchid'
        self.name = "Minerals"

    def __repr__(self):
        return self.name + str(self.position)

    def draw(self, position):
        drawCircle(position[0], position[1])


class Tornado(Asset):
    iconPath = "assets/images/map_assets/Tornado.png"
    radius = 75
    color = 'dimGray'
    borderColor = 'black'
    name = "Tornado"
    function = "Damages enemies"
    functionCont = "in range"
    def __init__(self, position, *args):
        super().__init__(position)
        self.iconPath = "assets/images/map_assets/Tornado.png"
        self.radius = 75
        self.color = "dimGray"
        self.borderColor = 'black'
        self.name = "Tornado"

    def __repr__(self):
        return self.name + str(self.position)

    def draw(self, position):
        drawCircle(position[0], position[1])

