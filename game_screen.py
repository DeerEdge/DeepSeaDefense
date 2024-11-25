from cmu_graphics import *
from check_functions import *
from enemies import *

def game_onScreenActivate(app):
    app.pointerColor = "red"
    app.pointerLocation = (0, 0)
    app.enemiesList = []
    app.towersList = []
    app.roundStarted = False
    app.stepsPerSecond = 20

def game_redrawAll(app):
    # drawLabel('Started', app.width // 2, app.height // 5, size=80, font="monospace", bold=True)
    # Board drawing
    drawRect(10, 10, 790, 590, fill='white', border='black', borderWidth=2)
    drawLabel('Towers', 900, 30, size=30, font="monospace", bold=True)
    for posX in range(2):
        for posY in range(6):
            drawRect(810 + posX*90, 50 + posY*90, 85, 85, fill='white', border='black', borderWidth=2)

    coordsList = readLineCoords("sample_paths.txt")
    if len(coordsList) > 1:
        for index in range(1, len(coordsList)):
            print(coordsList[index-1], coordsList[index])
            drawLine(coordsList[index-1][0], coordsList[index-1][1], coordsList[index][0], coordsList[index][1])

    for enemy in app.enemiesList:
        currentPosition = enemy.getPosition()
        drawCircle(currentPosition[0], currentPosition[1], 10)
    # Draw Mouse Pointer
    drawCircle(app.pointerLocation[0], app.pointerLocation[1], 5, fill=app.pointerColor)

def spawnEnemies(app, numMonsters=1):
    for i in range(numMonsters):
        enemy = Monster("Serpent", (10,10))
        app.enemiesList.append(enemy)

def game_onStep(app):
    if app.enemiesList != []:
        for enemy in app.enemiesList:
            currentPosition = enemy.getPosition()
            positionX, positionY = currentPosition
            newPosition = (positionX + 10, positionY + 10)
            enemy.setPosition(newPosition)

def game_onMousePress(app, mouseX, mouseY):
    app.pointerColor = "lightgreen"
    if app.roundStarted == False:
        spawnEnemies(app)
        app.roundStarted = True
    # if isWithinRectTopLeft(10, 10, 790, 590, mouseX, mouseY):
    #     writeLineCoord("sample_paths.txt", (mouseX, mouseY))
    #     print("Added point: ", (mouseX, mouseY))

def game_onMouseMove(app, mouseX, mouseY):
    app.pointerColor = 'red'
    app.pointerLocation = (mouseX, mouseY)