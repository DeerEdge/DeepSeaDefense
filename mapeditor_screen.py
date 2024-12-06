from cmu_graphics import *
from check_functions import *
from widgets import *
from map_assets import *

def mapeditor_onScreenActivate(app):
    app.coordsList = readLineCoords("paths/custom_map1.txt")
    app.mapPath = "paths/custom_map1.txt"
    app.mapAssetsPath = "paths/custom_map1_assets.txt"
    app.pointerLocation = (0, 0)
    app.saveButton = Button('save', 900, 95, 150, 50, 'Save', fill='green', border='black', textFill='white')
    app.resetButton = Button('clear', 900, 155, 150, 50, 'Clear', fill='red', border='black', textFill='white')
    app.undoButton = Button('undo', 900, 215, 150, 50, 'Undo', fill='royalBlue', border='black', textFill='white')
    app.backButton = Button("back", 70, 670, 120, 40, "←  Back", fill='midnightBlue', border='black', textFill='white')
    app.allAssets = [Sea_Cliff, Acid_74, Fog, Minerals, Peaks, Tornado]
    app.mapToEdit = "Map 1"
    app.selectedAsset = None
    app.spawnedAssets = unpackAssets(app.mapAssetsPath)

def mapeditor_redrawAll(app):
    drawImage("assets/images/game_screen/wood_background.jpg", 0, 0, width=1000, height=700)
    drawRect(10, 10, 790, 590, fill='white', border='black', borderWidth=2)
    drawRect(12, 12, 786, 586, fill=rgb(0, 79, 180))
    drawLabel(f"{app.pointerLocation}", 17, 588, fill="white", size=15, align='left')

    # Draw line path
    for i in range(1, len(app.coordsList)):
        drawLine(app.coordsList[i - 1][0], app.coordsList[i - 1][1], app.coordsList[i][0], app.coordsList[i][1],
                 lineWidth=20, fill=rgb(5, 89, 185))

    for asset in app.spawnedAssets:
        currentPosition = asset.getPosition()
        assetIcon = asset.getIconPath()
        drawCircle(currentPosition[0], currentPosition[1], asset.radius, fill=asset.color, border=asset.borderColor,
                   align="center", borderWidth=2, opacity=40)
        drawImage(assetIcon, currentPosition[0], currentPosition[1], width=50, height=50, align='center')

    # Draw right-side wall
    for shiftY in range(61):
        if shiftY % 5 == 0:
            drawRect(785, 11 + shiftY * 9.63, 14, 10, fill='silver', border='black', borderWidth=1)
        else:
            drawRect(790, 11 + shiftY * 9.63, 9, 10, fill='gray', border='black', borderWidth=1)

    # Draw right-side of editor
    drawLabel('Edit Map', 900, 32, size=30, bold=True, fill='white')
    drawRect(810, 55, 180, 200, fill='aliceBlue', opacity=80, border='black', borderWidth=2)

    drawLabel('Assets', 900, 282, size=30, bold=True, fill='white')
    for posX in range(2):
        for posY in range(3):
            drawRect(813 + posX*90, 305 + posY*90, 85, 85, fill='white', border='black', borderWidth=2)
            icon_path = app.allAssets[posX*3 + posY].iconPath
            drawImage(icon_path, 815 + posX*90, 307 + posY*90, width=81, height=81)

    # Draw buttons
    app.saveButton.draw()
    app.resetButton.draw()
    app.undoButton.draw()
    app.backButton.draw()

    drawLabel('Currently Editing: ', 200, 630, size=25, bold=True, fill='white', align='left')
    drawRect(30+370, 630, 270, 40, fill='navy', align='left', border='black', borderWidth=2)
    if app.mapToEdit == "Map 1":
        xCoord = 30+370
    elif app.mapToEdit == "Map 2":
        xCoord = 30+460
    elif app.mapToEdit == "Map 3":
        xCoord = 30+550
    drawRect(xCoord, 630, 90, 40, fill='cornflowerBlue', border = 'white', align='left')
    drawLabel("Map 1", 30+390, 630, fill='white', align='left', size=20)
    drawLabel("Map 2", 30+480, 630, fill='white', align='left', size=20)
    drawLabel("Map 3", 30+570, 630, fill='white', align='left', size=20)

    if app.selectedAsset != None:
        locationX, locationY = app.pointerLocation[0], app.pointerLocation[1]
        if app.pointerLocation[0] <= 12: locationX = 12
        elif app.pointerLocation[0] > 786: locationX = 786
        if app.pointerLocation[1] <= 12: locationY = 12
        elif app.pointerLocation[1] > 586: locationY = 586

        drawCircle(locationX, locationY, app.selectedAsset.radius, fill=app.selectedAsset.color, border=app.selectedAsset.borderColor,
                   align="center", borderWidth=2, opacity=40)
        drawImage(app.selectedAsset.iconPath, app.pointerLocation[0]-25, app.pointerLocation[1]-25, width=50, height=50)

    # Draw Mouse Pointer
    drawCircle(app.pointerLocation[0], app.pointerLocation[1], 5, fill=app.pointerColor)

def unpackAssets(path):
    rawAssetsList = getAssetsFromFile(path)
    unpackedAssetsList = []
    for assetInfo in rawAssetsList:
        assetObj = None
        assetPosition = None
        for i in range(len(assetInfo)):
            if assetInfo[i] in ['Sea_Cliff', 'Acid_74', 'Fog', 'Minerals', 'Peaks', 'Tornado']:
                if assetInfo[i] == 'Sea_Cliff':
                    assetObj = Sea_Cliff
                elif assetInfo[i] == 'Acid_74':
                    assetObj = Acid_74
                elif assetInfo[i] == 'Fog':
                    assetObj = Fog
                elif assetInfo[i] == 'Minerals':
                    assetObj = Minerals
                elif assetInfo[i] == 'Peaks':
                    assetObj = Peaks
                elif assetInfo[i] == 'Tornado':
                    assetObj = Tornado

            if type(assetInfo[i]) == tuple:
                assetPosition = assetInfo[i]
        asset = assetObj(position=assetPosition)
        unpackedAssetsList.append(asset)
    return unpackedAssetsList


def mapeditor_onMousePress(app, mouseX, mouseY):
    app.pointerColor = "lightgreen"
    if app.saveButton.containsPoint(mouseX, mouseY):
        clearFile(app.mapPath)
        clearFile(app.mapAssetsPath)
        for coord in app.coordsList:
            writeLineCoord(app.mapPath, coord)
        for asset in app.spawnedAssets:
            writeObjectsAndAttributes(app.mapAssetsPath, asset.getName(), asset.getPosition(), asset.getRadius(),
                                      asset.getColor(), asset.getBorderColor())
        print(unpackAssets(app.mapAssetsPath))
        print("Path saved")
        # if isWithinRectTopLeft( 10, 10, 790, 590, mouseX, mouseY):
        #     writeLineCoord("sample_paths.txt", (mouseX, mouseY))
        #     print("Added point: ", (mouseX, mouseY))

    if app.resetButton.containsPoint(mouseX, mouseY):
        app.coordsList = readLineCoords(app.mapPath)
        clearFile(app.mapPath)
        clearFile((app.mapAssetsPath))

    if app.undoButton.containsPoint(mouseX, mouseY):
        app.coordsList = app.coordsList[:-1]
        app.spawnedAssets = app.spawnedAssets[:-1]
        clearFile(app.mapPath)
        clearFile(app.mapAssetsPath)

    if app.selectedAsset == None and isWithinRect(400, 300, 780, 580, mouseX, mouseY):
        app.coordsList.append((mouseX, mouseY))
        print("Added point:", (mouseX, mouseY))

    if app.backButton.containsPoint(mouseX, mouseY):
        setActiveScreen('title')

    # Select map to edit
    if isWithinRectLeft(30+180, 630, 270, 40, mouseX, mouseY):
        app.mapToEdit = "Map 1"
        app.coordsList = readLineCoords("paths/custom_map1.txt")
        app.mapPath = "paths/custom_map1.txt"
        app.mapAssetsPath = "paths/custom_map1_assets.txt"
        app.spawnedAssets = unpackAssets(app.mapAssetsPath)
    elif isWithinRectLeft(30+270, 630, 270, 40, mouseX, mouseY):
        app.mapToEdit = "Map 2"
        app.coordsList = readLineCoords("paths/custom_map2.txt")
        app.mapPath = "paths/custom_map2.txt"
        app.mapAssetsPath = "paths/custom_map2_assets.txt"
        app.spawnedAssets = unpackAssets(app.mapAssetsPath)
    elif isWithinRectLeft(30+360, 630, 270, 40, mouseX, mouseY):
        app.mapToEdit = "Map 3"
        app.coordsList = readLineCoords("paths/custom_map3.txt")
        app.mapPath = "paths/custom_map3.txt"
        app.mapAssetsPath = "paths/custom_map3_assets.txt"
        app.spawnedAssets = unpackAssets(app.mapAssetsPath)

    if isWithinRectTopLeft(810, 50, 180, 540, mouseX, mouseY):
        if app.selectedAsset == None:
            for posX in range(0,2):
                for posY in range(0,4):
                    assetX, assetY = 815 + posX*90, 307 + posY*90
                    if isWithinRectTopLeft(assetX, assetY, 81, 81, mouseX, mouseY):
                        asset = getSelectedAsset(app, posX * 3 + posY)
                        app.selectedAsset = asset
                        break
    elif app.selectedAsset != None and isWithinRectTopLeft(10, 10, 790, 590, mouseX, mouseY):
        asset = app.selectedAsset((mouseX, mouseY))
        app.spawnedAssets.append(asset)
        app.selectedAsset = None

def getSelectedAsset(app, index):
    return app.allAssets[index]

def mapeditor_onMouseMove(app, mouseX, mouseY):
    app.pointerLocation = (mouseX, mouseY)




