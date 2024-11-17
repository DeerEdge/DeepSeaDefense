from cmu_graphics import *
from check_functions import *
from game_screen import *

def onAppStart(app):
    app.color = "blue"
    app.width, app.height = 1000, 700

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
    drawLabel('Credits', app.width // 2, app.height // 2 + 130, size=30, font="monospace", bold=True)


def title_onMousePress(app, mouseX, mouseY):
    if isWithinRect(app.width // 2, app.height // 2 - 50, app.width // 4, app.height // 10, mouseX, mouseY):
        setActiveScreen('game')

def main():
    runAppWithScreens(initialScreen='title')

main()
