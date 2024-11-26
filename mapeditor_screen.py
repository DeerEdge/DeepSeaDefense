from cmu_graphics import *
from check_functions import *
from widgets import *

def mapeditor_onScreenActivate(app):
    app.coordsList = []
    app.pointerLocation = (0, 0)
    app.saveButton = Button('save', 880, 70, 120, 50, 'Save', fill='green', border='black', textFill='white')
    app.resetButton = Button('reset', 880, 130, 120, 50, 'Reset', fill='red', border='black', textFill='white')
    app.backButton = Button('back', 880, 190, 120, 50, 'Back', fill='gray', border='black', textFill='white')

def mapeditor_redrawAll(app):
    drawRect(10, 10, 790, 590, fill='white', border='black', borderWidth=2)
    drawRect(12, 12, 786, 586, fill=rgb(0, 79, 180))

    # Draw line path
    for i in range(1, len(app.coordsList)):
        drawLine(app.coordsList[i - 1][0], app.coordsList[i - 1][1],
                 app.coordsList[i][0], app.coordsList[i][1],
                 lineWidth=20, fill=rgb(5, 89, 185))

    # Draw buttons
    app.saveButton.draw()
    app.resetButton.draw()
    app.backButton.draw()

    # Draw the pointer
    drawCircle(app.pointerLocation[0], app.pointerLocation[1], 5, fill='red')

def mapeditor_onMousePress(app, mouseX, mouseY):
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



