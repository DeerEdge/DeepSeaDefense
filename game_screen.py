import random as rand
from cmu_graphics import *
from check_functions import *
import mapeditor_screen
from enemies import *
from towers import *
from projectiles import *
from levels import *
from widgets import *
from special_powers import *
from map_assets import *
from mapeditor_screen import unpackAssets

# Initialize variables
def game_onScreenActivate(app):
    app.pointerColor = "red"
    app.pointerLocation = (0, 0)
    app.spawnedEnemiesList = []
    app.toBeSpawnedList = []
    app.allTowers = [Patrol_Tower, Laser_Turret, Magic_Portal, Resource_Mine, Submarine, Tooth_Trap, Monster_Net,
                     Resource_Mine]
    app.allAssets = [Acid_74, Fog, Minerals, Tornado]
    app.spawnedTowersList = []
    app.projectilesList = []
    app.missilesList = []
    app.canFireMissiles = True
    app.roundStarted = False
    app.preRound = True
    app.showRoundLabel = False
    app.roundLabelTimer = 0
    app.stepsPerSecond = 15
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
    app.score = 0
    app.backButton = Button("back", 70, 670, 120, 40, "←  Back", fill='midnightBlue', border='black',
                            textFill='white')
    app.quitButton = Button("quit", 196, 670, 120, 40, "Quit Game", fill='red', border='black', textFill='white',
                            borderWidth=2)
    app.chosenPath = readLine("paths/chosen_path.txt")
    app.coordsList = readLineCoords(app.chosenPath)
    app.startCoord = app.coordsList[0]
    app.chosenAssetsPath = readLine("paths/chosen_assets_path.txt")
    app.spawnedAssets = unpackAssets(app.chosenAssetsPath)
    app.hoverOverCard = False
    app.hoveringOver = None
    app.hoveringOverSpawned = False
    app.towerPosition = (0, 0)
    app.missilesUsed = False


def game_redrawAll(app):
    # Board drawing
    drawRect(0, 0, 1000, 700, fill=rgb(170, 123, 70))
    drawRect(5, 5, 990, 690, fill=rgb(188, 146, 87))
    drawImage("assets/images/game_screen/wood_background.jpg", 0, 0, width=1000, height=700)
    drawRect(10, 50, 790, 590, fill='white', border='black', borderWidth=2)
    drawRect(12, 52, 786, 586, fill=rgb(0, 79, 180))
    drawLabel(f"{app.pointerLocation}", 17, 628, fill="white", size=15, align='left')
    drawLabel('Towers', 900, 30, size=30, bold=True, fill='white')

    # Currency, defense health, and round labels
    heart_icon_path = "assets/images/game_screen/heart_icon.jpg"
    drawImage(heart_icon_path, 20, 15, width=30, height=30)
    drawLabel(f"{app.defenseHealth}", 55, 30, size=25, fill="white", align="left", bold=True)
    cash_icon_path = "assets/images/game_screen/dollar.png"
    drawImage(cash_icon_path, 120, 15, width=30, height=30)
    drawLabel(f"${app.currency}k", 160, 30, size=25, fill="white",font='grenze', align="left", bold=True)
    star_icon_path = "assets/images/game_screen/star_icon.png"
    drawImage(star_icon_path, 260, 15, width=30, height=30)
    drawLabel(f"{app.score}", 300, 30, size=25, fill="white", align="left", bold=True)
    drawLabel(f"Round {app.round}", 690, 30, size=25, fill="white", align="left", bold=True)
    drawRect(670, 45, 130, 3, fill='white', align="left")

    # Draw right-side tower store
    for posX in range(2):
        for posY in range(4):
            drawRect(810 + posX*90, 50 + posY*90, 85, 85, fill='white', border='black', borderWidth=2)
            icon_path = app.allTowers[posX*4 + posY].iconPath
            drawImage(icon_path, 812 + posX*90,  52 + posY*90, width=81, height=81)

    # Draw special power
    if app.missilesUsed == False:
        drawRect(898, 528, 180, 230, fill=rgb(38, 138, 87), border="limeGreen", align="center", borderWidth=2,
                 opacity=100)
    else:
        drawRect(898, 528, 180, 230, fill='salmon', border='darkRed', align="center", borderWidth=2,
                 opacity=100)
    drawImage('assets/images/special_powers/missile.png', 898 - 35, 528 + 45, width=90, height=90,
              align='center')
    drawImage('assets/images/special_powers/missile.png', 898 - 10, 528 - 10, width=120, height=120,
              align='center')
    drawImage('assets/images/special_powers/missile.png', 898 + 45, 528 - 35, width=90, height=90,
              align='center')

    # Bottom Buttons
    app.backButton.draw()
    app.quitButton.draw()

    # Draw line path
    if len(app.coordsList) > 1:
        for index in range(1, len(app.coordsList)):
            drawLine(app.coordsList[index-1][0], app.coordsList[index-1][1], app.coordsList[index][0],
                     app.coordsList[index][1], lineWidth=20, fill=rgb(5, 89, 185))

    # Draw right-side wall
    for shiftY in range(61):
        if shiftY % 5 == 0:
            drawRect(785, 51 + shiftY*9.63, 14, 10, fill='silver', border='black', borderWidth=1)
        else:
            drawRect(790, 51 + shiftY*9.63, 9, 10, fill='gray', border='black', borderWidth=1)

    # Before the round starts, show a greyed out screen with Start Button
    if app.preRound:
        drawRect(0, 0, 1000, 700, fill='gray', opacity=50)
        drawRect(app.width//2 - 100, app.height//2 - 40, 200, 80, fill='white', border='black', borderWidth=2)
        drawLabel('Start Round', app.width//2, app.height//2, size=20, bold=True)

    # Draw all assets that were generated or added in map editor
    for asset in app.spawnedAssets:
        currentPosition = asset.getPosition()
        assetIcon = asset.getIconPath()
        drawCircle(currentPosition[0], currentPosition[1], asset.radius, fill=asset.color, border=asset.borderColor,
                   align="center", borderWidth=2, opacity=40)
        drawImage(assetIcon, currentPosition[0], currentPosition[1], width=50, height=50, align='center')

    # Draw all towers that were added to the playable area
    for tower in app.spawnedTowersList:
        currentPosition = tower.getPosition()
        towerIcon = tower.getIconPath()
        drawImage(towerIcon, currentPosition[0], currentPosition[1], width=50, height=50, align='center')
        drawLabel(f"Lvl. {tower.level}", currentPosition[0], currentPosition[1]-40, size=12, fill="white")
        if type(tower) == Resource_Mine:
            tower.drawAnimation()

    # Draw all enemies that were added to the playable area
    for enemy in app.spawnedEnemiesList:
        currentPosition = enemy.getPosition()
        enemyIcon = enemy.getIconPath()
        enemyHealthBarValue = enemy.getHealth()/type(enemy).healthPoints
        drawRect(currentPosition[0]-20, currentPosition[1] - 35, 40, 5, fill='crimson', align='left')
        drawRect(currentPosition[0]-20, currentPosition[1] - 35, 40*enemyHealthBarValue+0.0001, 5, fill='limeGreen', align='left')
        drawImage(enemyIcon, currentPosition[0], currentPosition[1], width=50, height=50, align='center')

        # Show attacked animation
        if enemy.redCircleTimer > 0:
            drawCircle(currentPosition[0], currentPosition[1], 10, fill=rgb(160, 0, 0), border='red', borderWidth=3)

    # Draw all projectiles that were created and added to the playable area
    for projectile in app.projectilesList:
        if projectile.isAlive:
            projectilePosition = projectile.getPosition()
            projectile.draw(projectilePosition, 5)

    # Draw all missiles from activating the special powerup
    for missile in app.missilesList:
        if missile.isAlive:
            missilePosition = missile.getPosition()
            missile.drawIcon(missilePosition)

    # If a tower is chosen, its effective area of impact will be highlighted on the board
    if app.selectedTower != None:
        locationX, locationY = app.pointerLocation[0], app.pointerLocation[1]
        if app.pointerLocation[0] <= 25: locationX = 25
        elif app.pointerLocation[0] > 786: locationX = 786
        if app.pointerLocation[1] <= 25: locationY = 25
        elif app.pointerLocation[1] > 586: locationY = 586
        if app.selectedTower.iconPath == "assets/images/towers/submarine.png":
            drawLine(locationX, locationY - 100, locationX, locationY + 100, fill='red', lineWidth=2)
            drawLine(locationX, locationY + 100, locationX + 200, locationY + 100, fill='red', lineWidth=2)
            drawLine(locationX + 200, locationY + 100, locationX + 200, locationY - 100, fill='red', lineWidth=2)
            drawLine(locationX + 200, locationY - 100, locationX, locationY - 100, fill='red', lineWidth=2)
        drawCircle(locationX, locationY, app.selectedTower.initialTowerRadius, fill=rgb(160, 0, 0), border="red",
                   align="center", borderWidth=2, opacity=40)
        drawImage(app.selectedTower.iconPath, app.pointerLocation[0]-25, app.pointerLocation[1]-25, width=50, height=50)

    # If mouse is hovering over a tower card, we draw the tower's info
    if app.hoverOverCard:
        drawInfoCard(app, app.hoveringOver, app.hoveringOverSpawned)

    # If the round hasn't started we have a preliminary screen to start the round
    if app.roundStarted != True and app.defenseHealth > 0:
        drawRect(0, 0, 1000, 700, fill='gray', opacity=50)
        drawRect(app.width // 2 - 100, app.height // 2 - 40, 200, 80, fill='gray', border='black', borderWidth=2)
        drawLabel("Start Round", app.width // 2, app.height // 2, size=30, fill='white')

    # Show Round # label before round starts
    if app.showRoundLabel:
        drawLabel(f"Round {app.round}", app.width // 2 - 100, app.height // 5, size=50, bold=True,
                  fill=rgb(223, 181, 72),
                  border='yellow', borderWidth=2)

    # If we lose all of our health points, we display the game over screen
    if app.gameOver:
        drawRect(0, 0, app.width, app.height, fill='black', opacity=50)
        drawLabel("GAME OVER", app.width//2, app.height//2 - 50, size=50, fill='red', bold=True)
        drawLabel(f"Towers Placed: {app.towersPlaced}", app.width//2, app.height//2 + 20, size=30, fill='white')
        drawLabel(f"Enemies Defeated: {app.enemiesDefeated}", app.width//2, app.height//2 + 60, size=30,
                  fill='white')
        drawLabel(f"Total Score: {app.score}",app.width // 2, app.height // 2 + 100, size=30,fill='white')
        drawLabel(f"({app.round-1} Round(s) * 2000 + {app.enemiesDefeated} Enemies Defeated * 100 = {app.score})",
                  app.width // 2, app.height // 2 + 140, size=20,fill='white')
        drawLabel("Press R to Restart", app.width//2, app.height//2 + 200, size=20, fill='lightgray')

    # Draw Mouse Pointer
    drawCircle(app.pointerLocation[0], app.pointerLocation[1], 5, fill=app.pointerColor)

# Adds all enemies that will be spawned in the round to a list to processed
def spawnEnemies(app):
    if app.round in levels:
        level_monsters = levels[app.round]
        for monster_type, count in level_monsters.items():
            for i in range(count):
                if monster_type == "serpents":
                    enemy = Serpent(app.startCoord, app.startCoord, app.coordsList[1])
                elif monster_type == "slithers":
                    enemy = Slither(app.startCoord, app.startCoord, app.coordsList[1])
                elif monster_type == "queens":
                    enemy = Queen(app.startCoord, app.startCoord, app.coordsList[1])
                elif monster_type == "worms":
                    enemy = Worm(app.startCoord, app.startCoord, app.coordsList[1])
                app.toBeSpawnedList.append(enemy)

def game_onStep(app):
    # If the health of defenses reach 0, the game is over
    if app.defenseHealth <= 0:
        app.gameOver = True
        app.roundStarted = False
        return

    if app.roundStarted and app.defenseHealth > 0 and app.spawnedEnemiesList == [] and app.toBeSpawnedList == []:
        app.projectilesList = []
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

    # Controls the spawning of enemies so there is separation
    if app.roundStarted and app.toBeSpawnedList != []:
        app.enemySpawnTimer += 1
        if app.enemySpawnTimer >= app.spawnInterval * app.stepsPerSecond:
            app.spawnedEnemiesList.append(app.toBeSpawnedList.pop(0))
            app.enemySpawnTimer = 0

    manageTowers(app)
    manageProjectiles(app)
    manageEnemies(app)
    manageMissiles(app)

# Manages towers and activates the tower's attacks if an enemy comes in range. Actions are separated by whether the
# towers are static or dynamic. Special actions such as the Submarine's movement are processed individually.
def manageTowers(app):
    for tower in app.spawnedTowersList:
        if tower.getTowerType() == "dynamic":
            tower.reduceCooldown()
            if type(tower) == Submarine:
                tower.move()
            if tower.canAttack():
                for enemy in app.spawnedEnemiesList:
                    enemyPosition = enemy.getPosition()
                    towerPosition = tower.getPosition()
                    distance = getDistance(towerPosition, enemyPosition)
                    towerRadius = tower.getTowerRadius()

                    if tower.getHasProjectile() and distance <= towerRadius and enemy.getVisibilty():
                        # Launch a projectile towards the enemy
                        projectileType = tower.getProjectileType()
                        projectile = projectileType(towerPosition, enemy, tower.getTowerDamage(), tower, app.coordsList)
                        app.projectilesList.append(projectile)
                        tower.startCooldown()
                        break
        elif tower.getTowerType() == "static":
            if tower.getIsActive():
                if type(tower) == Resource_Mine:
                    tower.reduceCooldown()
                    if tower.cooldown == 0:
                        tower.doAction(app.spawnedAssets)
                        tower.startCooldown()
                else:
                    for enemy in app.spawnedEnemiesList:
                        enemyPosition = enemy.getPosition()
                        towerPosition = tower.getPosition()
                        distance = getDistance(towerPosition, enemyPosition)
                        towerRadius = tower.getTowerRadius()

                        if distance <= towerRadius:
                            tower.doAction(enemy, app.spawnedAssets)
            else:
                app.spawnedTowersList.remove(tower)
            if type(tower) == Monster_Net:
                tower.reduceHoldingDuration()
            if type(tower) == Resource_Mine:
                if tower.getProfit() > 0:
                    app.currency += tower.getProfit()
                    tower.setProfit(0)

# Manage the movement and attacks of the created projectiles
def manageProjectiles(app):
    for projectile in app.projectilesList:
        if projectile.isAlive:
            projectilePosition = projectile.move()

            # Check for collision with enemy
            for enemy in app.spawnedEnemiesList:
                if type(projectile) in [Bullet] and getDistance(projectilePosition, enemy.getPosition()) < 25:
                    enemy.setHealth(enemy.getHealth() - projectile.damage)
                    # Show red circle when hit
                    enemy.showRedCircleEffect()
                    app.projectilesList.remove(projectile)
                    break
                elif type(projectile) in [Laser, Light_Ray]:
                    if projectile.getEnemy().getHealth() <= 0 or ((getDistance(projectile.getEnemy().getPosition(),
                            projectile.getParentTower().getPosition()) > projectile.getParentTower().getTowerRadius())):
                        projectile.changeEnemy(app.spawnedEnemiesList, enemy)
                        if projectile.getEnemy() == None:
                            app.projectilesList.remove(projectile)
                        break
                    else:
                        projectile.getEnemy().setHealth(projectile.getEnemy().getHealth() - projectile.damage)
                        # Show red circle when hit
                        projectile.getEnemy().showRedCircleEffect()
                        break

# Manage enemies and their health + movement
def manageEnemies(app):
    for enemy in app.spawnedEnemiesList:
        enemy.updateRedCircleEffect()
        if enemy.getHealth() <= 0:
            app.enemiesDefeated += 1
            app.currency += enemy.getReward()
            app.spawnedEnemiesList.remove(enemy)

        currentPosition = enemy.getPosition()
        if isEnemyAtEnd(app, currentPosition):
            enemyDamage = enemy.getDamage()
            app.defenseHealth -= enemyDamage
            app.spawnedEnemiesList.remove(enemy)
        else:
            newPosition = getNextPosition(app, currentPosition, enemy)
            enemy.setPosition(newPosition)
        enemy.setVisibilty(True)

        # Account for effects of assets on the enemy
        for asset in app.spawnedAssets:
            if asset.getName() == "Acid_74" and getDistance(asset.getPosition(), enemy.getPosition()) < asset.getRadius():
                enemy.setHealth(enemy.getHealth() + 5)
                if enemy.getHealth() > type(enemy).healthPoints:
                    enemy.setHealth(type(enemy).healthPoints)
            elif asset.getName() == "Tornado" and getDistance(asset.getPosition(), enemy.getPosition()) < asset.getRadius():
                enemy.setHealth(enemy.getHealth() - 5)
            elif asset.getName() == "Fog" and getDistance(asset.getPosition(), enemy.getPosition()) < asset.getRadius():
                enemy.setVisibilty(False)

# Manage special powerup missiles
def manageMissiles(app):
    for missile in app.missilesList:
        if missile.isAlive:
            missilePosition = missile.move()
            # Check for collision with enemy
            for enemy in app.spawnedEnemiesList:
                if getDistance(missilePosition, enemy.getPosition()) < 25:
                    enemy.setHealth(enemy.getHealth() - missile.damage)
                    # Show red circle when hit
                    enemy.showRedCircleEffect()
                    app.missilesList.remove(missile)
                    break

# Calculate the next position of the enemy based on its movement type
def getNextPosition(app, currentPosition, enemy):
    if enemy.getIsCaught():
        return currentPosition

    previousCoord = enemy.getPreviousCoord()
    targetCoord = enemy.getTargetCoord()
    distance = getDistance(currentPosition, targetCoord)
    movementType = enemy.getMovementType()
    enemySpeed = enemy.getSpeed()
    stepSize = enemySpeed/100

    if distance < 20:
        previousCoord = targetCoord
        targetCoord = app.coordsList[app.coordsList.index(targetCoord)+1]
        enemy.setPreviousCoord(previousCoord)
        enemy.setTargetCoord(targetCoord)

    # Check for which movementType it is
    if movementType == "linear":
        changeX = (targetCoord[0]-previousCoord[0])*stepSize
        changeY = (targetCoord[1]-previousCoord[1])*stepSize
        return (currentPosition[0] + changeX, currentPosition[1] + changeY)
    elif movementType == "logarithmic":
        changeX = (targetCoord[0]-currentPosition[0])*stepSize
        changeY = (targetCoord[1]-currentPosition[1])*stepSize
        return (currentPosition[0] + changeX, currentPosition[1] + changeY)

def enemyShift(app, currentPosition):
    posX, posY = currentPosition
    shiftX = rand.randint(-5, 5)
    shiftY = rand.randint(-5, 5)
    return (posX + shiftX, posY + shiftY)

def game_onMousePress(app, mouseX, mouseY):
    app.pointerColor = "lightgreen"

    if app.roundStarted != True and isWithinRect(app.width//2, app.height//2, 200, 80, mouseX, mouseY):
        if app.score == 0:
            app.score += (app.round-1)*2000+app.enemiesDefeated*100
        else:
            app.score += 2000 + app.enemiesDefeated * 100
        app.missilesUsed = False
        app.preRound = False
        app.showRoundLabel = True
        app.roundStarted = True
        spawnEnemies(app)

    # Check if back button was clicked
    if isWithinRect(70, 670, 120, 40, mouseX, mouseY):
        setActiveScreen('levels')

    # Check if quit button was clicked
    if isWithinRect(196, 670, 120, 40, mouseX, mouseY):
        app.gameOver = True
        app.roundStarted = False

    # Launch missiles
    if isWithinRect(898, 528, 180, 230, mouseX, mouseY) and len(app.spawnedEnemiesList) >= 5 and not app.missilesUsed:
        app.missilesUsed = True
        app.canFireMissiles = True
        missile = Missiles((775,150), app.spawnedEnemiesList[0], 10000, app.coordsList)
        app.missilesList.append(missile)
        missile = Missiles((775, 250), app.spawnedEnemiesList[1], 10000, app.coordsList)
        app.missilesList.append(missile)
        missile = Missiles((775, 350), app.spawnedEnemiesList[2], 10000, app.coordsList)
        app.missilesList.append(missile)
        missile = Missiles((775, 450), app.spawnedEnemiesList[3], 10000, app.coordsList)
        app.missilesList.append(missile)
        missile = Missiles((775, 550), app.spawnedEnemiesList[4], 10000, app.coordsList)
        app.missilesList.append(missile)
    else:
        app.canFireMissiles = False

    # Check if towers are upgraded
    for tower in app.spawnedTowersList:
        towerX, towerY = tower.getPosition()
        if isWithinRect(towerX, towerY, 50, 50, mouseX, mouseY):
            upgradeCost = tower.getUpgradeCost()
            if upgradeCost != None and app.currency >= upgradeCost:
                app.currency -= upgradeCost
                tower.upgrade()
                break

    # Check if tower has been selected to be placed
    notFound = True
    if isWithinRectTopLeft(810, 50, 180, 540, mouseX, mouseY):
        if app.selectedTower == None and app.roundStarted == True:
            for posX in range(0,2):
                for posY in range(0,4):
                    towerX, towerY = 812 + posX*90, 52 + posY*90
                    if isWithinRectTopLeft(towerX, towerY, 81, 81, mouseX, mouseY):
                        tower = getSelectedTower(app, posX*4 + posY)
                        if app.currency >= tower.towerCost:
                            app.selectedTower = tower
                        notFound = False
                        break
                if notFound:
                    continue
                else:
                    break
    elif app.selectedTower != None and isWithinRectTopLeft(10, 10, 790, 590, mouseX, mouseY):
        tower = app.selectedTower((mouseX, mouseY))
        app.spawnedTowersList.append(tower)
        app.currency -= tower.towerCost
        app.towersPlaced += 1
        app.selectedTower = None

# Check if enemy has reached the end of the path
def isEnemyAtEnd(app, currentPosition):
    endCoord = app.coordsList[-1]
    if getDistance(currentPosition, endCoord) <= 20:
        return True
    else:
        return False

# Get the selected tower
def getSelectedTower(app, index):
    return app.allTowers[index]

def game_onMouseMove(app, mouseX, mouseY):
    app.hoverOverCard = False
    app.hoveringOver = None
    app.hoveringOverSpawned = False
    app.pointerColor = 'red'
    app.pointerLocation = (mouseX, mouseY)

    # Check if mouse is hovering over a spawned tower
    for tower in app.spawnedTowersList:
        towerX, towerY = tower.getPosition()
        if isWithinRect(towerX, towerY, 50, 50, mouseX, mouseY):
            app.hoverOverCard = True
            app.hoveringOver = tower
            app.hoveringOverSpawned = True
            break

    # Check if mouse is hovering over a tower store tower
    if isWithinRectTopLeft(810, 50, 180, 540, mouseX, mouseY):
        if app.selectedTower == None and app.roundStarted == True:
            for posX in range(0,2):
                for posY in range(0,4):
                    towerX, towerY = 812 + posX*90, 52 + posY*90
                    if isWithinRectTopLeft(towerX, towerY, 81, 81, mouseX, mouseY):
                        tower = getSelectedTower(app, posX * 4 + posY)
                        app.hoverOverCard = True
                        app.hoveringOver = tower
                        app.hoveringOverSpawned = False
                        app.towerPosition = (towerX, towerY)
                        break

def game_onKeyPress(app, key):
    if key == 'r' and app.gameOver:
        game_onScreenActivate(app)

# Draw the info card about a tower in the tower store, or about a spawned tower
def drawInfoCard(app, tower, hoveringOverSpawned):
    if hoveringOverSpawned:
        towerPostion = tower.getPosition()
        drawRect(towerPostion[0], towerPostion[1], 150, 200, fill='silver', border='darkGray', align='top-right', borderWidth=4, opacity=80)
        drawLabel(tower.getName(), towerPostion[0]-75, towerPostion[1]+20,fill='black', bold=True, size=20, align='center')
        drawLabel("Current Level: ", towerPostion[0] - 75, towerPostion[1] + 60, fill='black', bold=True, size=15,
                  align='center')
        drawLabel(str(tower.getLevel()), towerPostion[0] - 75, towerPostion[1] + 80, fill='black', bold=True, size=15,
                  align='center')
        drawLabel("Cost to Upgrade:", towerPostion[0] - 75, towerPostion[1] + 110, fill='black', bold=True, size=15,
                  align='center')
        upgradeCost = tower.getUpgradeCost()
        if upgradeCost != None:
            cost = str(tower.getUpgradeCost()) + "k"
        else:
            cost = "Maxed out tower!"
        drawLabel(cost, towerPostion[0] - 75, towerPostion[1] + 130, fill='black', bold=True, size=15,
                  align='center')
        if tower.getDoesAttack():
            drawLabel("Current Damage: ", towerPostion[0] - 75, towerPostion[1] + 160, fill='black', bold=True, size=15,
                      align='center')
            drawLabel(str(tower.getTowerDamage()), towerPostion[0] - 75, towerPostion[1] + 180, fill='black', bold=True, size=15,
                      align='center')
    else:
        drawRect(app.towerPosition[0]-2, app.towerPosition[1]+4, 150, 200, fill='silver', border='darkGray', align='top-right',
                 borderWidth=2, opacity=80)
        drawLabel(tower.name, app.towerPosition[0]-75, app.towerPosition[1]+20, fill='black', bold=True, size=20, align='center')
        drawLabel("Initial Tower Radius: ", app.towerPosition[0] - 75, app.towerPosition[1] + 60, fill='black', bold=True, size=15,
                  align='center')
        drawLabel(str(tower.initialTowerRadius), app.towerPosition[0] - 75, app.towerPosition[1] + 80, fill='black', bold=True, size=15,
                  align='center')
        drawLabel("Tower Cost:", app.towerPosition[0] - 75, app.towerPosition[1] + 110, fill='black', bold=True,
                  size=15,
                  align='center')
        drawLabel(str(tower.towerCost), app.towerPosition[0] - 75, app.towerPosition[1] + 130, fill='black', bold=True,
                  size=15,
                  align='center')
        drawLabel("Upgrades (Lvl: Cost):", app.towerPosition[0] - 75, app.towerPosition[1] + 160, fill='black', bold=True,
                  size=15,
                  align='center')
        drawLabel(str(tower.upgradeCosts), app.towerPosition[0] - 75, app.towerPosition[1] + 180, fill='black', bold=True,
                  size=15,
                  align='center')

