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
    clearFile("generated_path.txt")

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
        applyMathFuncByLevel(app, "hard", 9)
        setActiveScreen('game')

def applyMathFuncByLevel(app, level, nSubdivisions):
    pointValues = []
    if level == "hard":
        for i in range(nSubdivisions):
            x = i * 2 * math.pi / nSubdivisions
            pointValues.append((x, sineSquared(x)))

    tangentLines = []
    for i in range(len(pointValues)-1):
        tangentLines.append((pointValues[i+1][1]-pointValues[i][1])/(pointValues[i+1][0]-pointValues[i][0]))

    print(pointValues, tangentLines)
    return generatePathBasedOnLevel(app, tangentLines, nSubdivisions)

def writePathList(coordsList):
    for coord in coordsList:
        writeLineCoord("generated_path.txt", coord)

def generatePathBasedOnLevel(app, tangentLines, nSubdivisions, turnSharpness=1, randomnessWeight=1):
    initialCoord = (20, rand.randint(30, app.gameHeight-30))
    coordsList = []
    coordsList.append(initialCoord)
    print("initital", coordsList)
    resultPathList = solvePath(app, copy.copy(coordsList), tangentLines, nSubdivisions)
    print(resultPathList)
    writePathList(resultPathList)

def solvePath(app, coordsList, tangentLines, nSubdivisions):
    divisionWidth = app.gameWidth//nSubdivisions
    possibleNextCoords = getPossibleNextCoords(app, coordsList, nSubdivisions, divisionWidth)
    print(divisionWidth, coordsList, possibleNextCoords)
    lastCoord = coordsList[-1]
    closestPointOnEdge = (12 + app.gameWidth, lastCoord[1])
    if (getDistance(lastCoord, closestPointOnEdge) < 40):
        lastCoord = coordsList[-1]
        lastCoord = (lastCoord[0]-20,lastCoord[1])
        coordsList.pop()
        coordsList.append(lastCoord)
        return coordsList
    else:
        while len(possibleNextCoords) > 0:
            randomIndex = rand.randint(0, len(possibleNextCoords)-1)
            nextCoord = possibleNextCoords[randomIndex]
            if canAddCoordToList(nextCoord, coordsList, tangentLines, divisionWidth):
                coordsList.append(nextCoord)
                solution = solvePath(app, coordsList, tangentLines, nSubdivisions)
                if solution != None:
                    return solution
                coordsList.pop()
            else:
                possibleNextCoords.pop(randomIndex)
        return None

def canAddCoordToList(nextCoord, coordsList, tangentLines, divisionWidth):
    previousCoord = coordsList[-1]
    i = len(coordsList)-2
    tangentValue = abs(tangentLines[i])
    xDist = abs(divisionWidth)
    print(getDistance(previousCoord, nextCoord), xDist + 10*tangentValue, xDist + 20*tangentValue)
    if xDist + 10*tangentValue <= getDistance(previousCoord, nextCoord) <= xDist*1.1 + 40*tangentValue:
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