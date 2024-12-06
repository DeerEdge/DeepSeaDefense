
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

# Checks if a mouse action occurred inside a rectangle (rects aligned by their left-side)
def isWithinRectLeft(topLeftX, topLeftY, width, height, mouseX, mouseY):
    if (topLeftX <= mouseX <= topLeftX + width) and (topLeftY - height//2 <= mouseY <= topLeftY + height//2):
        return True
    return False

def clearFile(fileName):
    file = open(fileName, 'w')
    return

def writeObjectsAndAttributes(fileName, objectName, position, radius, color, borderColor):
    file = open(fileName, 'a')
    file.write(str(["NAME:"+objectName, "POSITION:("+str(position[0])+"|"+str(position[1])+")", "RADIUS:"+str(radius), "COLOR:"+str(color),
                    "BORDERCOLOR:"+str(borderColor)]) + ' . ')
    file.close()

def writeLine(fileName, text):
    clearFile(fileName)
    file = open(fileName, 'a')
    file.write(str(text))
    file.close()

def readLine(fileName):
    file = open(fileName, 'r')
    contents = file.read()
    file.close()
    return contents

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

def getSlope(coord1, coord2):
    coord1X, coord1Y = coord1
    coord2X, coord2Y = coord2
    return (coord2Y-coord1Y)/(coord2X-coord1X)

def getAssetsFromFile(fileName):
    file = open(fileName, 'r')
    contents = file.read()

    assets = []
    for assetInfo in contents.split(" . "):
        print(assetInfo)
        if not assetInfo.isspace() and assetInfo != '':
            left = assetInfo.find("[")
            right = assetInfo.find("]")
            for parameter in assetInfo.split(","):
                print(parameter)
                if "NAME:" in parameter:
                    assetName = parameter[parameter.find(":")+1:len(parameter)-1]
                elif "POSITION:" in parameter:
                    assetPosition = parameter[parameter.find(":")+1:len(parameter)-1]
                    left = assetPosition.find("(")
                    comma = assetPosition.find("|")
                    right = assetPosition.find(")")
                    x, y = int(assetPosition[left + 1:comma]), int(assetPosition[comma + 1:right])
                    assetPosition = (x, y)
                elif "RADIUS:" in parameter:
                    assetRadius = int(parameter[parameter.find(":") + 1:len(parameter) - 1])
                elif "BORDERCOLOR:" in parameter:
                    assetBorderColor = parameter[parameter.find(":")+1:len(parameter)-2]
                elif "COLOR:" in parameter:
                    assetColor = parameter[parameter.find(":")+1:len(parameter)-1]
            assets.append((assetName, assetPosition, assetRadius, assetColor, assetBorderColor))

    return assets
