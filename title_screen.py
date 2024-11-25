from cmu_graphics import *
from check_functions import *
from game_screen import *
from mapeditor_screen import *

def onAppStart(app):
    app.color = "blue"
    app.width, app.height = 1000, 700
    app.pointerColor = "red"
    app.pointerLocation = (0, 0)

def title_redrawAll(app):
    drawLabel('Deep Sea Defense', app.width // 2, app.height // 5, size=80, font="monospace", bold=True)
    drawRect(app.width // 2, app.height // 2 - 50, app.width // 4, app.height // 10, align='center', fill='white',
             border='black')
    drawRect(app.width // 2, app.height // 2 + 40, app.width // 4, app.height // 10, align='center', fill='white',
             border='black')
    drawRect(app.width // 2, app.height // 2 + 130, app.width // 4, app.height // 10, align='center', fill='white',
             border='black')
    drawLabel('Start Game!', app.width // 2, app.height // 2 - 50, size=30, font="monospace", bold=True)
    drawLabel('Rulebook', app.width // 2, app.height // 2 + 40, size=30, font="monospace", bold=True)
    drawLabel('Map Editor', app.width // 2, app.height // 2 + 130, size=30, font="monospace", bold=True)

    drawCircle(app.pointerLocation[0], app.pointerLocation[1], 5, fill=app.pointerColor)

def title_onMousePress(app, mouseX, mouseY):
    app.pointerColor = 'lightgreen'
    if isWithinRect(app.width // 2, app.height // 2 - 50, app.width // 4, app.height // 10, mouseX, mouseY):
        setActiveScreen('game')
    elif isWithinRect(app.width // 2, app.height // 2 + 130, app.width // 4, app.height // 10, mouseX, mouseY):
        setActiveScreen('mapeditor')

def title_onMouseMove(app, mouseX, mouseY):
    app.pointerColor = 'red'
    app.pointerLocation = (mouseX, mouseY)

def main():
    runAppWithScreens(initialScreen='title')

main()
