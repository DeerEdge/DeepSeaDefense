from cmu_graphics import *
from check_functions import *
from widgets import *

def mapeditor_onScreenActivate(app):
    app.coordsList = readLineCoords("paths/custom_map1.txt")
    app.mapPath = "paths/custom_map1.txt"
    app.pointerLocation = (0, 0)
    app.saveButton = Button('save', 900, 95, 150, 50, 'Save', fill='green', border='black', textFill='white')
    app.resetButton = Button('clear', 900, 155, 150, 50, 'Clear', fill='red', border='black', textFill='white')
    app.undoButton = Button('undo', 900, 215, 150, 50, 'Undo', fill='royalBlue', border='black', textFill='white')
    app.backButton = Button("back", 70, 670, 120, 40, "←  Back", fill='midnightBlue', border='black', textFill='white')
    app.allAssets = ["sea-cliff.png", "peaks.png", "tornado.png", "fog.png", "minerals.png", "acid-74.png"]
    app.mapToEdit = "Map 1"

def mapeditor_redrawAll(app):
    drawImage("assets/images/game_screen/wood_background.jpg", 0, 0, width=1000, height=700)
    drawRect(10, 10, 790, 590, fill='white', border='black', borderWidth=2)
    drawRect(12, 12, 786, 586, fill=rgb(0, 79, 180))
    drawLabel(f"{app.pointerLocation}", 17, 588, fill="white", size=15, align='left')

    # Draw line path
    for i in range(1, len(app.coordsList)):
        drawLine(app.coordsList[i - 1][0], app.coordsList[i - 1][1], app.coordsList[i][0], app.coordsList[i][1],
                 lineWidth=20, fill=rgb(5, 89, 185))

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
            icon_path = "assets/images/map_assets/" + app.allAssets[posX*3 + posY]
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

    # Draw Mouse Pointer
    drawCircle(app.pointerLocation[0], app.pointerLocation[1], 5, fill=app.pointerColor)

def mapeditor_onMousePress(app, mouseX, mouseY):
    app.pointerColor = "lightgreen"
    if app.saveButton.containsPoint(mouseX, mouseY):
        clearFile(app.mapPath)
        for coord in app.coordsList:
            writeLineCoord(app.mapPath, coord)
        print("Path saved")
        # if isWithinRectTopLeft( 10, 10, 790, 590, mouseX, mouseY):
        #     writeLineCoord("sample_paths.txt", (mouseX, mouseY))
        #     print("Added point: ", (mouseX, mouseY))

    if app.resetButton.containsPoint(mouseX, mouseY):
        app.coordsList = readLineCoords(app.mapPath)
        clearFile(app.mapPath)

    if app.undoButton.containsPoint(mouseX, mouseY):
        app.coordsList = app.coordsList[:-1]
        clearFile(app.mapPath)

    if isWithinRect(400, 300, 780, 580, mouseX, mouseY):
        app.coordsList.append((mouseX, mouseY))
        print("Added point:", (mouseX, mouseY))

    if app.backButton.containsPoint(mouseX, mouseY):
        setActiveScreen('title')

    # Select map to edit
    if isWithinRectLeft(30+180, 630, 270, 40, mouseX, mouseY):
        app.mapToEdit = "Map 1"
        app.coordsList = readLineCoords("paths/custom_map1.txt")
        app.mapPath = "paths/custom_map1.txt"
    elif isWithinRectLeft(30+270, 630, 270, 40, mouseX, mouseY):
        app.mapToEdit = "Map 2"
        app.coordsList = readLineCoords("paths/custom_map2.txt")
        app.mapPath = "paths/custom_map2.txt"
    elif isWithinRectLeft(30+360, 630, 270, 40, mouseX, mouseY):
        app.mapToEdit = "Map 3"
        app.coordsList = readLineCoords("paths/custom_map3.txt")
        app.mapPath = "paths/custom_map3.txt"

def mapeditor_onMouseMove(app, mouseX, mouseY):
    app.pointerLocation = (mouseX, mouseY)



