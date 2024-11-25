from cmu_graphics import *
from check_functions import *
from enemies import *

def game_onScreenActivate(app):
    app.pointerColor = "red"
    app.pointerLocation = (0, 0)
    app.spawnedEnemiesList = []
    app.toBeSpawnedList = []
    app.towersList = []
    app.roundStarted = False
    app.stepsPerSecond = 15
    app.coordsList = readLineCoords("sample_paths.txt")
    app.startCoord = app.coordsList[0]
    app.enemySpawnTimer = 0
    app.spawnInterval = 1 # Spawn a monster at every second

def game_redrawAll(app):
    # drawLabel('Started', app.width // 2, app.height // 5, size=80, font="monospace", bold=True)
    # Board drawing
    drawRect(10, 10, 790, 590, fill='white', border='black', borderWidth=2)
    drawLabel('Towers', 900, 30, size=30, font="monospace", bold=True)
    drawLabel('Towers', 900, 30, size=30, font="monospace", bold=True)
    for posX in range(2):
        for posY in range(6):
            drawRect(810 + posX*90, 50 + posY*90, 85, 85, fill='white', border='black', borderWidth=2)

    if len(app.coordsList) > 1:
        for index in range(1, len(app.coordsList)):
            drawLine(app.coordsList[index-1][0], app.coordsList[index-1][1], app.coordsList[index][0], app.coordsList[index][1])

    for enemy in app.spawnedEnemiesList:
        currentPosition = enemy.getPosition()
        enemyIcon = enemy.getIconPath()
        drawImage(enemyIcon, currentPosition[0], currentPosition[1], width=50, height=50, align='center')

    # Draw Mouse Pointer
    drawCircle(app.pointerLocation[0], app.pointerLocation[1], 5, fill=app.pointerColor)

def spawnEnemies(app, numMonsters=2):
    for i in range(numMonsters):
        enemy = Serpent(app.startCoord, app.startCoord, app.coordsList[1])
        app.toBeSpawnedList.append(enemy)

def game_onStep(app):
    # Get and set the positions of the enemies after they move
    if app.spawnedEnemiesList != []:
        for enemy in app.spawnedEnemiesList:
            currentPosition = enemy.getPosition()
            newPosition = getNextPosition(app, currentPosition, enemy)
            enemy.setPosition(newPosition)

    if app.roundStarted and app.toBeSpawnedList != []:
        app.enemySpawnTimer += 1
        if app.enemySpawnTimer >= app.spawnInterval * app.stepsPerSecond:
            app.spawnedEnemiesList.append(app.toBeSpawnedList.pop(0))
            app.enemySpawnTimer = 0

def getNextPosition(app, currentPosition, enemy):
    previousCoord = enemy.getPreviousCoord()
    targetCoord = enemy.getTargetCoord()
    distance = getDistance(currentPosition, targetCoord)
    stepSize = 10
    print("prev", previousCoord, "tar", targetCoord)

    if distance < 2:
        previousCoord = targetCoord
        targetCoord = app.coordsList[app.coordsList.index(targetCoord)+1]
        enemy.setPreviousCoord(previousCoord)
        enemy.setTargetCoord(targetCoord)
        print("dist less","prev",previousCoord,"tar",targetCoord)

    return (currentPosition[0] + (targetCoord[0]-currentPosition[0])/stepSize, currentPosition[1] +
            (targetCoord[1]-currentPosition[1])/stepSize)


def game_onMousePress(app, mouseX, mouseY):
    app.pointerColor = "lightgreen"
    if app.roundStarted == False:
        spawnEnemies(app, 5)
        app.roundStarted = True
    # if isWithinRectTopLeft( 10, 10, 790, 590, mouseX, mouseY):
    #     writeLineCoord("sample_paths.txt", (mouseX, mouseY))
    #     print("Added point: ", (mouseX, mouseY))

def game_onMouseMove(app, mouseX, mouseY):
    app.pointerColor = 'red'
    app.pointerLocation = (mouseX, mouseY)
