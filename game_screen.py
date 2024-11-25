from cmu_graphics import *
from check_functions import *
from enemies import *
from towers import *
from projectiles import *
from levels import *

def game_onScreenActivate(app):
    app.pointerColor = "red"
    app.pointerLocation = (0, 0)
    app.spawnedEnemiesList = []
    app.toBeSpawnedList = []
    app.allTowers = [Patrol_Tower]
    app.spawnedTowersList = []
    app.projectilesList = []
    app.roundStarted = False
    app.preRound = True
    app.showRoundLabel = False
    app.roundLabelTimer = 0
    app.stepsPerSecond = 15
    app.coordsList = readLineCoords("sample_paths.txt")
    app.startCoord = app.coordsList[0]
    app.enemySpawnTimer = 0
    app.spawnInterval = 1 # Spawn a monster at every second
    app.redCircleTimer = 0
    app.selectedTower = None
    app.round = 1
    app.currency = 500
    app.defenseHealth = 100
    app.gameOver = False
    app.towersPlaced = 0
    app.enemiesDefeated = 0

def game_redrawAll(app):
    # drawLabel('Started', app.width // 2, app.height // 5, size=80, font="monospace", bold=True)
    # Board drawing
    drawRect(10, 10, 790, 590, fill='white', border='black', borderWidth=2)
    drawRect(12, 12, 786, 586, fill=rgb(0, 79, 180))
    drawLabel('Towers', 900, 30, size=30, font="monospace", bold=True)
    drawLabel('Towers', 900, 30, size=30, font="monospace", bold=True)

    # Currency and defense health labels
    drawLabel(f"Currency: ${app.currency}", 20, 20, size=20, fill="white", align="left", bold=True)
    drawLabel(f"Defense Health: {app.defenseHealth}%", 20, 50, size=20, fill="white", align="left", bold=True)

    # Tower store drawing
    for posX in range(2):
        for posY in range(6):
            drawRect(810 + posX*90, 50 + posY*90, 85, 85, fill='white', border='black', borderWidth=2)
            drawImage("assets/images/towers/patrol_tower.png", 812 + posX*90, 52 + posY*90, width=81, height=81)

    # Draw line path
    if len(app.coordsList) > 1:
        for index in range(1, len(app.coordsList)):
            drawLine(app.coordsList[index-1][0], app.coordsList[index-1][1], app.coordsList[index][0],
                     app.coordsList[index][1], lineWidth=20, fill=rgb(5, 89, 185))

    # Before the round starts, show a greyed out screen with Start Button
    if app.preRound:
        drawRect(10, 10, 980, 650, fill='gray', opacity=50)
        drawRect(app.width//2 - 100, app.height//2 - 40, 200, 80, fill='white', border='black', borderWidth=2)
        drawLabel('Start Round', app.width//2, app.height//2, size=20, bold=True)

    # Show Round # label before round starts
    if app.showRoundLabel:
        drawLabel(f"Round {app.round}", app.width//2, app.height//3, size=50, bold=True, fill=rgb(223, 181, 72),
                  border='yellow', borderWidth=2)

    for enemy in app.spawnedEnemiesList:
        currentPosition = enemy.getPosition()
        enemyIcon = enemy.getIconPath()
        enemyHealthBarValue = enemy.getHealth()/type(enemy).healthPoints
        print(enemyHealthBarValue, enemy.getHealth())
        drawRect(currentPosition[0]-20, currentPosition[1] - 35, 40, 5, fill='crimson', align='left')
        drawRect(currentPosition[0]-20, currentPosition[1] - 35, 40*enemyHealthBarValue+0.0001, 5, fill='limeGreen', align='left')
        drawImage(enemyIcon, currentPosition[0], currentPosition[1], width=50, height=50, align='center')

        if enemy.redCircleTimer > 0:
            drawCircle(currentPosition[0], currentPosition[1], 10, fill=rgb(160, 0, 0), border='red', borderWidth=3)

    for tower in app.spawnedTowersList:
        currentPosition = tower.getPosition()
        towerIcon = tower.getIconPath()
        drawImage(towerIcon, currentPosition[0], currentPosition[1], width=50, height=50, align='center')
        drawLabel(f"Lvl. {tower.level}", currentPosition[0], currentPosition[1]-40, size=12, fill="white")

    for projectile in app.projectilesList:
        projectilePosition = projectile.getPosition()
        drawCircle(projectilePosition[0], projectilePosition[1], 5)

    if app.selectedTower != None:
        locationX, locationY = app.pointerLocation[0], app.pointerLocation[1]
        if app.pointerLocation[0] <= 25: locationX = 25
        elif app.pointerLocation[0] > 786: locationX = 786
        if app.pointerLocation[1] <= 25: locationY = 25
        elif app.pointerLocation[1] > 586: locationY = 586

        drawCircle(locationX, locationY, app.selectedTower.initialTowerRadius, fill=rgb(160, 0, 0), border="red",
                   align="center", borderWidth=2, opacity=40)
        drawImage(app.selectedTower.iconPath, app.pointerLocation[0]-25, app.pointerLocation[1]-25, width=50, height=50)

    if app.roundStarted != True and app.defenseHealth > 0:
        drawRect(app.width // 2 - 100, app.height // 2 - 40, 200, 80, fill='gray', border='black', borderWidth=2)
        drawLabel("Start Round", app.width // 2, app.height // 2, size=30, fill='white')

    if app.gameOver:
        drawRect(0, 0, app.width, app.height, fill='black', opacity=50)
        drawLabel("GAME OVER", app.width//2, app.height//2 - 50, size=50, fill='red', bold=True)
        drawLabel(f"Towers Placed: {app.towersPlaced}", app.width//2, app.height//2 + 20, size=30, fill='white')
        drawLabel(f"Enemies Defeated: {app.enemiesDefeated}", app.width//2, app.height//2 + 60, size=30,
                  fill='white')
        drawLabel("Press R to Restart", app.width//2, app.height//2 + 120, size=20, fill='lightgray')

    # Draw Mouse Pointer
    drawCircle(app.pointerLocation[0], app.pointerLocation[1], 5, fill=app.pointerColor)

def spawnEnemies(app):
    if app.round in levels:
        numMonsters = levels[app.round].get("monsters")
        for i in range(numMonsters):
            enemy = Serpent(app.startCoord, app.startCoord, app.coordsList[1])
            app.toBeSpawnedList.append(enemy)

def game_onStep(app):
    if app.defenseHealth <= 0:
        app.gameOver = True
        app.roundStarted = False
        return

    if app.roundStarted and app.defenseHealth > 0 and app.spawnedEnemiesList == [] and app.toBeSpawnedList == []:
        app.round += 1
        app.roundStarted = False
        if app.round in levels:
            spawnEnemies(app)

    if app.showRoundLabel == True:
        app.roundLabelTimer += 1
        if app.roundLabelTimer > app.stepsPerSecond:
            app.showRoundLabel = False
            app.roundLabelTimer = 0

    if app.roundStarted == False:
        return

    # Get and set the positions of the enemies after they move
    if app.spawnedEnemiesList != []:
        for enemy in app.spawnedEnemiesList:
            currentPosition = enemy.getPosition()
            newPosition = getNextPosition(app, currentPosition, enemy)
            enemy.setPosition(newPosition)

    # Controls the spawning of enemies
    if app.roundStarted and app.toBeSpawnedList != []:
        app.enemySpawnTimer += 1
        if app.enemySpawnTimer >= app.spawnInterval * app.stepsPerSecond:
            app.spawnedEnemiesList.append(app.toBeSpawnedList.pop(0))
            app.enemySpawnTimer = 0

    for tower in app.spawnedTowersList:
        tower.reduceCooldown()
        if tower.canAttack():
            for enemy in app.spawnedEnemiesList:
                enemyPosition = enemy.getPosition()
                towerPosition = tower.getPosition()
                distance = getDistance(towerPosition, enemyPosition)
                towerRadius =  tower.getTowerRadius()

                if distance <= towerRadius:
                    # Launch a projectile towards the enemy
                    projectile = Bullet(towerPosition, enemy, tower.getTowerDamage())
                    app.projectilesList.append(projectile)
                    tower.startCooldown()
                    break

    for projectile in app.projectilesList:
        if projectile.isAlive:
            projectilePosition = projectile.move()
            # Check for collision with enemy
            for enemy in app.spawnedEnemiesList:
                if getDistance(projectilePosition, enemy.getPosition()) < 25:
                    enemy.setHealth(enemy.getHealth() - projectile.damage)
                    # Show red circle when hit
                    enemy.showRedCircleEffect()
                    app.projectilesList.remove(projectile)
                    break

    for enemy in app.spawnedEnemiesList:
        enemy.updateRedCircleEffect()
        if enemy.getHealth() == 0:
            app.enemiesDefeated += 1
            app.currency += enemy.getReward()
            app.spawnedEnemiesList.remove(enemy)

        currentPosition = enemy.getPosition()
        if isEnemyAtEnd(app, currentPosition):
            app.defenseHealth -= 10
            app.spawnedEnemiesList.remove(enemy)

def getNextPosition(app, currentPosition, enemy):
    previousCoord = enemy.getPreviousCoord()
    targetCoord = enemy.getTargetCoord()
    distance = getDistance(currentPosition, targetCoord)
    stepSize = 10

    if distance < 2:
        previousCoord = targetCoord
        targetCoord = app.coordsList[app.coordsList.index(targetCoord)+1]
        enemy.setPreviousCoord(previousCoord)
        enemy.setTargetCoord(targetCoord)

    return (currentPosition[0] + (targetCoord[0]-currentPosition[0])/stepSize, currentPosition[1] +
            (targetCoord[1]-currentPosition[1])/stepSize)


def game_onMousePress(app, mouseX, mouseY):
    app.pointerColor = "lightgreen"

    if app.roundStarted != True and isWithinRect(app.width//2, app.height//2, 200, 80, mouseX, mouseY):
        app.preRound = False
        app.showRoundLabel = True
        app.roundStarted = True
        spawnEnemies(app)

    for tower in app.spawnedTowersList:
        towerX, towerY = tower.getPosition()
        if isWithinRect(towerX, towerY, 50, 50, mouseX, mouseY):
            upgradeCost = tower.getUpgradeCost()
            if upgradeCost != None and app.currency >= upgradeCost:
                app.currency -= upgradeCost
                tower.upgrade()
                break

    if isWithinRectTopLeft(810, 50, 180, 540, mouseX, mouseY):
        if app.selectedTower == None and app.roundStarted == True:
            for posX in range(2):
                for posY in range(6):
                    towerX, towerY = 810 + posX*90, 50 + posY*90
                    if isWithinRectTopLeft(towerX, towerY, towerX + 85, towerY + 85, mouseX, mouseY):
                        tower = getSelectedTower(app, posX*6 + posY)
                        if app.currency >= tower.towerCost:
                            app.selectedTower = tower
                        break
    elif app.selectedTower != None and isWithinRectTopLeft(10, 10, 790, 590, mouseX, mouseY):
        tower = app.selectedTower((mouseX, mouseY))
        app.spawnedTowersList.append(tower)
        app.currency -= tower.towerCost
        app.towersPlaced += 1
        app.selectedTower = None

def isEnemyAtEnd(app, currentPosition):
    endCoord = app.coordsList[-1]
    if getDistance(currentPosition, endCoord) <= 10:
        return True
    else:
        return False

def getSelectedTower(app, index):
    return app.allTowers[index]

def game_onMouseMove(app, mouseX, mouseY):
    app.pointerColor = 'red'
    app.pointerLocation = (mouseX, mouseY)

def game_onKeyPress(app, key):
    if key == 'r' and app.gameOver:
        game_onScreenActivate(app)
