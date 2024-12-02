
# Checks if a mouse action occurred inside a rectangle (rects must be aligned by their center)
def isWithinRect(centerX, centerY, width, height, mouseX, mouseY):
    if (centerX - width//2 <= mouseX <= centerX + width//2) and (centerY - height//2 <= mouseY <= centerY + height//2):
        return True
    return False

# Checks if a mouse action occurred inside a rectangle (rects aligned by their top left)
def isWithinRectTopLeft(topLeftX, topLeftY, width, height, mouseX, mouseY):
    if (topLeftX <= mouseX <= topLeftX + width) and (topLeftY <= mouseY <= topLeftY + height):
        return True
    return False

def writeLineCoord(fileName, coord):
    file = open(fileName, 'a')
    file.write(str(coord) + ' . ')
    file.close()

def readLineCoords(fileName):
    file = open(fileName, 'r')
    contents = file.read()

    coordsList = []
    for stringCoord in contents.split(" . "):
        if not stringCoord.isspace() and stringCoord != '':
            left = stringCoord.find("(")
            comma = stringCoord.find(",")
            right = stringCoord.find(")")
            x, y = int(stringCoord[left+1:comma]), int(stringCoord[comma+1:right])
            coordsList.append((x, y))
    return coordsList

# Gets the distance between two coordinates
def getDistance(coord1, coord2):
    coord1X, coord1Y = coord1
    coord2X, coord2Y = coord2
    distance = ((coord1X - coord2X)**2 + (coord1Y - coord2Y)**2)**0.5
    return distance