import math
import random as rand
import copy
from cmu_graphics import *
from check_functions import *
from widgets import *
from math_functions import *

def levels_onScreenActivate(app):
    app.gameLeftTopX, app.gameLeftTopY = 12, 12
    app.gameWidth, app.gameHeight = 786, 586
    app.pointerColor = "red"
    app.pointerLocation = (0, 0)
    app.backButton = Button("back", 70, 670, 120, 40, "←  Back", fill='midnightBlue', border='black', textFill='white')
    app.easyLevelButton = Button("easy", app.width // 5, 205, 224, 174, image='assets/images/levels_screen/easyLevelSample.png',
                                 imageWidth=220, imageHeight=170, border='white', borderWidth=5)
    app.mediumLevelButton = Button("medium", app.width // 2, 205, 224, 174, image='assets/images/levels_screen/mediumLevelSample.png',
                                 imageWidth=220, imageHeight=170, border='white', borderWidth=5)
    app.hardLevelButton = Button("hard",  4 * app.width // 5, 205, 224, 174, image='assets/images/levels_screen/hardLevelSample.png',
                                 imageWidth=220, imageHeight=170, border='white', borderWidth=5)
    app.backButton = Button("back", 70, 670, 120, 40, "←  Back", fill='midnightBlue', border='black', textFill='white')
    clearGeneratedPath(app)

def clearGeneratedPath(app):
    clearFile("paths/generated_path.txt")

def levels_redrawAll(app):
    drawImage("assets/images/game_screen/wood_background.jpg", 0, 0, width=1000, height=700)
    drawLabel('Game Levels', app.width//2, 50, size=50, bold=True, fill='white')
    drawLabel('Easy', app.width // 5, 100, size=25, bold=True, fill='white')
    drawLabel('Medium', app.width // 2, 100, size=25, bold=True, fill='white')
    drawLabel('Hard', 4 * app.width // 5, 100, size=25, bold=True, fill='white')
    app.easyLevelButton.draw()
    app.mediumLevelButton.draw()
    app.hardLevelButton.draw()
    drawLabel('(Longest Path)', app.width // 5, 300, size=15, bold=True, fill='white')
    drawLabel('(Normal Path)', app.width // 2, 300, size=15, bold=True, fill='white')
    drawLabel('(Shortest Path)', 4 * app.width // 5, 300, size=15, bold=True, fill='white')
    app.backButton.draw()

    drawLabel('Custom Levels', app.width // 2, 350, size=30, bold=True, fill='white')

    # Draw Mouse Pointer
    drawCircle(app.pointerLocation[0], app.pointerLocation[1], 5, fill=app.pointerColor)

def levels_onMousePress(app, mouseX, mouseY):
    app.pointerColor = "lightgreen"
    # Check if back button was clicked
    if isWithinRect(70, 670, 120, 40, mouseX, mouseY):
        setActiveScreen('title')

    if isWithinRect(4 * app.width // 5, 205, 224, 174, mouseX, mouseY):
        applyMathFuncByLevel(app, "hard", 10, 1.9, 1)
        setActiveScreen('game')
    elif isWithinRect(app.width // 2, 205, 224, 174, mouseX, mouseY):
        applyMathFuncByLevel(app, "medium", 12, 1.5, 20)
        setActiveScreen('game')
    elif isWithinRect(app.width // 5, 205, 224, 174, mouseX, mouseY):
        applyMathFuncByLevel(app, "easy", 15, 1.2, 40)
        setActiveScreen('game')

def applyMathFuncByLevel(app, level, nSubdivisions, turnSharpness, randomnessWeight):
    pointValues = []
    if level == "hard":
        for i in range(nSubdivisions):
            x = i * 2 * math.pi / nSubdivisions
            pointValues.append((x, sineSquared(x)/2))
    elif level == "medium":
        for i in range(nSubdivisions):
            x = i * 2 * math.pi / nSubdivisions
            pointValues.append((x, sineSquared(x)/2))
    elif level == "easy":
        for i in range(nSubdivisions):
            x = i * 2 * math.pi / nSubdivisions
            pointValues.append((x, sineSquared(x)/2))

    tangentLines = []
    for i in range(len(pointValues)-1):
        tangentLines.append((pointValues[i+1][1]-pointValues[i][1])/(pointValues[i+1][0]-pointValues[i][0]))
        tangentLines[-1] = tangentLines[-1]*rand.randint(100, 100*randomnessWeight)/100*rand.randint(-1,1)

    print(pointValues, tangentLines)
    return generatePathBasedOnLevel(app, tangentLines, nSubdivisions, turnSharpness)

def writePathList(coordsList):
    for coord in coordsList:
        writeLineCoord("paths/generated_path.txt", coord)

def generatePathBasedOnLevel(app, tangentLines, nSubdivisions, turnSharpness):
    initialCoord = (20, rand.randint(80, app.gameHeight-80))
    coordsList = []
    coordsList.append(initialCoord)
    print("initital", coordsList)
    resultPathList = solvePath(app, copy.copy(coordsList), tangentLines, nSubdivisions, turnSharpness)
    print(resultPathList)
    writePathList(resultPathList)

def solvePath(app, coordsList, tangentLines, nSubdivisions, turnSharpness):
    divisionWidth = app.gameWidth//nSubdivisions
    possibleNextCoords = getPossibleNextCoords(app, coordsList, nSubdivisions, divisionWidth)
    # print(divisionWidth, coordsList, possibleNextCoords)
    lastCoord = coordsList[-1]
    closestPointOnEdge = (12 + app.gameWidth, lastCoord[1])
    if (getDistance(lastCoord, closestPointOnEdge) < 20):
        lastCoord = coordsList[-1]
        lastCoord = (lastCoord[0]-20,lastCoord[1])
        coordsList.pop()
        coordsList.append(lastCoord)
        return coordsList
    else:
        while len(possibleNextCoords) > 0:
            randomIndex = rand.randint(0, len(possibleNextCoords)-1)
            nextCoord = possibleNextCoords[randomIndex]
            if canAddCoordToList(nextCoord, coordsList, tangentLines, divisionWidth, turnSharpness):
                coordsList.append(nextCoord)
                solution = solvePath(app, coordsList, tangentLines, nSubdivisions, turnSharpness)
                if solution != None:
                    return solution
                coordsList.pop()
            else:
                possibleNextCoords.pop(randomIndex)
        return None

def canAddCoordToList(nextCoord, coordsList, tangentLines, divisionWidth, turnSharpness):
    previousCoord = coordsList[-1]
    i = len(coordsList)-2
    tangentValue = abs(tangentLines[i])
    xDist = abs(divisionWidth)
    print(previousCoord, nextCoord, xDist + 10*tangentValue, getDistance(previousCoord, nextCoord), xDist + 20*tangentValue)
    if len(coordsList) < 2 and abs(xDist*turnSharpness + 10*tangentValue) <= getDistance(previousCoord, nextCoord) <= abs(xDist*1.1*turnSharpness + 40*tangentValue):
        return True
    elif len(coordsList) >= 2:
        secondLastCoord = coordsList[0]
        previousSlope = getSlope(secondLastCoord, previousCoord)
        print("--->", previousCoord, nextCoord, previousSlope - tangentValue, getSlope(previousCoord, nextCoord), previousSlope + tangentValue)
        if previousSlope*turnSharpness - 2*tangentValue <= abs(getSlope(previousCoord, nextCoord)) <= abs(previousSlope*1.3*turnSharpness + 2*tangentValue):
            return True
    return False

def getPossibleNextCoords(app, coordsList, nSubdivisions, divisionWidth):
    recentCoord = coordsList[-1]
    xSetAt = recentCoord[0]+divisionWidth
    nextCoordsList = []
    for coordY in range(30, app.gameHeight-30):
        nextCoordsList.append((xSetAt, coordY+30))
    return nextCoordsList


def levels_onMouseMove(app, mouseX, mouseY):
    app.pointerColor = 'red'
    app.pointerLocation = (mouseX, mouseY)