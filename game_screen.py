from cmu_graphics import *
from check_functions import *

def game_onScreenActivate(app):
    app.pointerColor = "red"
    app.pointerLocation = (0, 0)

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

    # Draw Mouse Pointer
    drawCircle(app.pointerLocation[0], app.pointerLocation[1], 5, fill=app.pointerColor)

def game_onMousePress(app, mouseX, mouseY):
    app.pointerColor = "lightgreen"
    if isWithinRectTopLeft(10, 10, 790, 590, mouseX, mouseY):
        writeLineCoord("sample_paths.txt", (mouseX, mouseY))
        print("Added point: ", (mouseX, mouseY))

def game_onMouseMove(app, mouseX, mouseY):
    app.pointerColor = 'red'
    app.pointerLocation = (mouseX, mouseY)