from cmu_graphics import *
from check_functions import *
from widgets import *

def mapeditor_onScreenActivate(app):
    app.coordsList = []
    app.pointerLocation = (0, 0)
    app.saveButton = Button('save', 900, 95, 150, 50, 'Save', fill='green', border='black', textFill='white')
    app.resetButton = Button('reset', 900, 155, 150, 50, 'Reset', fill='red', border='black', textFill='white')
    app.backButton = Button("back", 70, 670, 120, 40, "←  Back", fill='midnightBlue', border='black', textFill='white')
    app.allAssets = ["sea-cliff.png", "peaks.png", "tornado.png", "fog.png", "minerals.png", "acid-74.png"]

def mapeditor_redrawAll(app):
    drawImage("assets/images/game_screen/wood_background.jpg", 0, 0, width=1000, height=700)
    drawRect(10, 10, 790, 590, fill='white', border='black', borderWidth=2)
    drawRect(12, 12, 786, 586, fill=rgb(0, 79, 180))

    # Draw line path
    for i in range(1, len(app.coordsList)):
        drawLine(app.coordsList[i - 1][0], app.coordsList[i - 1][1],
                 app.coordsList[i][0], app.coordsList[i][1],
                 lineWidth=20, fill=rgb(5, 89, 185))

    # Draw right-side wall
    for shiftY in range(61):
        if shiftY % 5 == 0:
            drawRect(785, 11 + shiftY * 9.63, 14, 10, fill='silver', border='black', borderWidth=1)
        else:
            drawRect(790, 11 + shiftY * 9.63, 9, 10, fill='gray', border='black', borderWidth=1)

    # Draw right-side of editor
    drawLabel('Edit Map', 900, 32, size=30, bold=True, fill='white')
    drawRect(810, 55, 180, 140, fill='aliceBlue', opacity=80, border='black', borderWidth=2)

    drawLabel('Assets', 900, 222, size=30, bold=True, fill='white')
    for posX in range(2):
        for posY in range(3):
            drawRect(813 + posX*90, 245 + posY*90, 85, 85, fill='white', border='black', borderWidth=2)
            icon_path = "assets/images/map_assets/" + app.allAssets[posX*3 + posY]
            drawImage(icon_path, 815 + posX*90, 247 + posY*90, width=81, height=81)

    # Draw buttons
    app.saveButton.draw()
    app.resetButton.draw()
    app.backButton.draw()

    # Draw Mouse Pointer
    drawCircle(app.pointerLocation[0], app.pointerLocation[1], 5, fill=app.pointerColor)

def mapeditor_onMousePress(app, mouseX, mouseY):
    app.pointerColor = "lightgreen"
    if app.saveButton.containsPoint(mouseX, mouseY):
        with open("sample_paths.txt", "w") as file:
            for coord in app.coordsList:
                file.write(f"({coord[0]},{coord[1]}) . ")
        print("Path saved")
        # if isWithinRectTopLeft( 10, 10, 790, 590, mouseX, mouseY):
        #     writeLineCoord("sample_paths.txt", (mouseX, mouseY))
        #     print("Added point: ", (mouseX, mouseY))

    elif app.resetButton.containsPoint(mouseX, mouseY):
        app.coordsList = []

    elif isWithinRect(400, 300, 780, 580, mouseX, mouseY):
        app.coordsList.append((mouseX, mouseY))
        print("Added point:", (mouseX, mouseY))

    elif app.backButton.containsPoint(mouseX, mouseY):
        setActiveScreen('title')

def mapeditor_onMouseMove(app, mouseX, mouseY):
    app.pointerLocation = (mouseX, mouseY)



